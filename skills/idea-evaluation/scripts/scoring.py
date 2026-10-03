"""Pure scoring logic (standard library only). Used by build_xlsx.py and the tests.

CLI: python scoring.py ideas.json [--sensitivity]
  prints adjusted score / priority / margin / break-even per idea;
  --sensitivity perturbs weights (+/-20 %), evidence factors (+/-0.05) and thresholds (+/-0.1)
  and reports whether the top idea and the A/B/C/D classes stay stable.
Exit codes: 0 ok, 2 invalid input or usage (unreadable file, bad JSON, failed validation) - the same in build_xlsx.py.

Rounding matches the spreadsheet exactly: raw = ROUND(sum(weight*rating), 2) half-up,
adjusted = ROUND(raw * evidence factor, 1) half-up, priority from the rounded adjusted score.
"""
import json, math, sys
from decimal import Decimal, ROUND_HALF_UP

CRIT = ["upside", "demand", "feasibility", "cost", "speed", "fit"]
WEIGHTS = {"upside": .25, "demand": .20, "feasibility": .15, "cost": .15, "speed": .15, "fit": .10}
EVIDENCE = {"E0": .80, "E1": .85, "E2": .90, "E3": .95, "E4": 1.0}
THRESHOLDS = {"A": 3.4, "B": 2.8, "C": 2.2}
GATES = ("gate_desirability", "gate_feasibility", "gate_viability")
GATE_VALUES = ("yes", "no", "unknown")
FLOOR = ("demand", "feasibility", "cost")   # a rating of 1 here is a fatal weakness: priority capped at C


class InputError(ValueError):
    """Raised for invalid input; the message names the problem."""


def _num(v):
    """True for real, finite numbers (bool, NaN and infinity are rejected)."""
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def _d(x):
    return Decimal(str(x))


def _q(x, places):
    return x.quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP)


def config(data):
    """Return (weights, evidence factors, thresholds) with user overrides applied and checked."""
    w, ev, th = dict(WEIGHTS), dict(EVIDENCE), dict(THRESHOLDS)
    for name, base, given in (("weights", w, data.get("weights", {})), ("evidence_factors", ev, data.get("evidence_factors", {})),
                              ("thresholds", th, data.get("thresholds", {}))):
        if not isinstance(given, dict) or set(given) - set(base):
            raise InputError(f"'{name}' must be an object with keys {sorted(base)}")
        for k, v in given.items():
            if not _num(v) or v < 0:
                raise InputError(f"'{name}.{k}' must be a finite number >= 0")
        base.update(given)
    if abs(sum(w.values()) - 1) > 1e-6:
        raise InputError(f"weights must sum to 1 (got {sum(w.values()):.4f})")
    if not th["A"] > th["B"] > th["C"]:
        raise InputError("thresholds must satisfy A > B > C")
    return w, ev, th


def normalize(d):
    """Copy of an idea with case/whitespace-insensitive gates and evidence."""
    n = dict(d)
    for g in GATES:
        if isinstance(n.get(g), str):
            n[g] = n[g].strip().lower()
    if isinstance(n.get("evidence"), str):
        n["evidence"] = n["evidence"].strip().upper()
    return n


def validate(data):
    """Return a list of problems (empty list = valid)."""
    errs = []
    if not isinstance(data, dict):
        return ["top level must be a JSON object"]
    ideas = data.get("ideas")
    if not isinstance(ideas, list):
        return ["'ideas' must be a list"]
    try:
        config(data)
    except InputError as e:
        errs.append(str(e))
    hours = data.get("time_budget_h_week", 8)
    if not _num(hours) or hours <= 0:
        errs.append("'time_budget_h_week' must be a positive finite number")
    if "currency" in data and not isinstance(data["currency"], str):
        errs.append("'currency' must be text")
    if "notes" in data and not (isinstance(data["notes"], list) and all(isinstance(x, str) for x in data["notes"])):
        errs.append("'notes' must be a list of strings")
    names = set()
    for i, raw in enumerate(ideas, 1):
        if not isinstance(raw, dict):
            errs.append(f"idea #{i}: must be an object"); continue
        d = normalize(raw)
        label = f"idea #{i} ({d.get('idea')!r})"
        if not isinstance(d.get("idea"), str) or not d["idea"].strip():
            errs.append(f"idea #{i}: 'idea' (name) is required")
        elif d["idea"].strip().casefold() in names:
            errs.append(f"{label}: duplicate name")
        else:
            names.add(d["idea"].strip().casefold())
        for c in CRIT:
            v = d.get(c)
            if v is None:
                continue
            if not _num(v) or not 1 <= v <= 5 or v != int(v):
                errs.append(f"{label}: '{c}' must be a whole number from 1 to 5 (got {v!r})")
        for g in GATES:
            if d.get(g) is not None and d[g] not in GATE_VALUES:
                errs.append(f"{label}: '{g}' must be one of {GATE_VALUES} (got {raw.get(g)!r})")
        if d.get("evidence") is not None and d["evidence"] not in EVIDENCE:
            errs.append(f"{label}: 'evidence' must be one of {sorted(EVIDENCE)} (got {raw.get('evidence')!r})")
        for k in ("price", "variable_cost", "fixed_costs", "hours_week", "weeks_to_first_evidence"):
            v = d.get(k)
            if v is not None and (not _num(v) or v < 0):
                errs.append(f"{label}: '{k}' must be a finite number >= 0 (got {v!r})")
        for k in ("id", "problem", "riskiest_assumption", "test", "pass_threshold", "premortem", "notes", "cost_to_mvp"):
            v = d.get(k)
            if v is not None and not isinstance(v, str) and not _num(v):
                errs.append(f"{label}: '{k}' must be text or a number (got {type(v).__name__})")
    return errs


def score(d, w=WEIGHTS, ev=EVIDENCE, th=THRESHOLDS):
    """Return (adjusted score rounded to 1 decimal or None, priority).
    Priorities: A/B/C/D, 'Stopped' (a gate says no), 'incomplete' (missing ratings).
    Knockout floor: Demand, Feasibility or Cost = 1 caps A/B at C."""
    d = normalize(d)
    if any(d.get(g) == "no" for g in GATES):
        return None, "Stopped"
    if any(d.get(c) is None for c in CRIT):
        return None, "incomplete"
    raw = _q(sum(_d(w[c]) * _d(d[c]) for c in CRIT), 2)
    adj = _q(raw * _d(ev.get(d.get("evidence") or "E0", ev["E0"])), 1)
    prio = "A" if adj >= _d(th["A"]) else "B" if adj >= _d(th["B"]) else "C" if adj >= _d(th["C"]) else "D"
    if prio in ("A", "B") and any(d[c] <= 1 for c in FLOOR):
        prio = "C"   # fatal weaknesses are not averaged away
    return float(adj), prio


def economics(d):
    """Return (margin, break-even customers). Margin needs price and variable cost; break-even additionally
    needs fixed costs and a positive margin, otherwise it is None."""
    price, var, fixed = d.get("price"), d.get("variable_cost"), d.get("fixed_costs")
    if price is None or var is None:
        return None, None
    m = price - var
    return m, (-(-fixed // m) if fixed is not None and m > 0 else None)


def breakeven_label(d):
    m, be = economics(d)
    return "no margin" if (m is not None and m <= 0 and d.get("fixed_costs") is not None) else be


def sort_key(d, w=WEIGHTS, ev=EVIDENCE, th=THRESHOLDS):
    s, p = score(d, w, ev, th)
    return ({"A": 0, "B": 1, "C": 2, "D": 3}.get(p, 4), -(s or 0))


def sensitivity(ideas, w, ev, th, delta=.2):
    """Perturb weights (+/-delta, renormalized), evidence factors (+/-0.05) and thresholds (+/-0.1).
    The top idea is chosen like the export orders ideas: priority class first (a knockout idea is capped at C), then the
    displayed (rounded) adjusted score; ideas are identified by position, so duplicate names are fine."""
    def norm(x):
        t = sum(x.values()); return {k: v / t for k, v in x.items()}

    order = {"A": 0, "B": 1, "C": 2, "D": 3}

    def run(w_, ev_, th_):
        s = [score(i, w_, ev_, th_) for i in ideas]
        live = [k for k, (sc, p) in enumerate(s) if sc is not None]
        if not live:
            return (), [p for _, p in s]
        best_class = min(order[s[k][1]] for k in live)          # same order as the export: class first, then displayed score
        pool = [k for k in live if order[s[k][1]] == best_class]
        best = max(s[k][0] for k in pool)
        top = tuple(k for k in pool if s[k][0] == best)         # equal displayed scores are a tie, as in the export
        return top, [p for _, p in s]

    w0 = norm(w)
    top0, cls0 = run(w0, ev, th)
    scenarios = []
    for c in CRIT:
        for sign in (-1, 1):
            w2 = dict(w0); w2[c] *= 1 + sign * delta
            scenarios.append((norm(w2), ev, th))
    for sign in (-1, 1):
        scenarios.append((w0, {k: min(1.0, v + sign * .05) for k, v in ev.items()}, th))
        scenarios.append((w0, ev, {k: v + sign * .1 for k, v in th.items()}))
    flips = changes = 0
    for sc in scenarios:
        top, cls = run(*sc)
        flips += top != top0
        changes += sum(a != b for a, b in zip(cls, cls0))
    return {"runs": len(scenarios), "top_changed_in": flips, "class_changes_total": changes,
            "top": [ideas[k].get("idea") for k in top0]}


def _no_constant(name):
    raise ValueError(f"{name} is not allowed in JSON input")


def load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f, parse_constant=_no_constant)   # rejects NaN / Infinity
    except (OSError, ValueError) as e:                         # JSONDecodeError is a ValueError
        print(f"cannot read {path}: {e}", file=sys.stderr)
        sys.exit(2)


def main(argv):
    files = [a for a in argv if not a.startswith("--")]
    if len(files) != 1:
        print(__doc__, file=sys.stderr)
        return 2
    data = load(files[0])
    errs = validate(data)
    if errs:
        print("invalid input:\n  " + "\n  ".join(errs), file=sys.stderr)
        return 2
    w, ev, th = config(data)
    for i in data["ideas"]:
        print(i["idea"], *score(i, w, ev, th), *economics(i))
    if "--sensitivity" in argv:
        print(sensitivity(data["ideas"], w, ev, th))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
