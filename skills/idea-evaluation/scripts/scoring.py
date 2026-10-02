"""Pure scoring logic (no dependencies). Used by build_xlsx.py and tests.

CLI: python scoring.py ideas.json [--sensitivity]
  prints score/priority per idea; --sensitivity perturbs each weight by +/-20 %
  (renormalized) and reports whether the top idea and the A/B/C/D classes are stable.
"""
import json, sys

CRIT = ["upside", "demand", "feasibility", "cost", "speed", "fit"]
WEIGHTS = {"upside": .25, "demand": .20, "feasibility": .15, "cost": .15, "speed": .15, "fit": .10}
EVIDENCE = {"E0": .80, "E1": .85, "E2": .90, "E3": .95, "E4": 1.0}
THRESHOLDS = {"A": 3.4, "B": 2.8, "C": 2.2}
GATES = ("gate_desirability", "gate_feasibility", "gate_viability")
FLOOR = ("demand", "feasibility", "cost")   # a rating of 1 here is a fatal weakness: priority capped at C



def config(data):
    w = {**WEIGHTS, **data.get("weights", {})}
    return w, {**EVIDENCE, **data.get("evidence_factors", {})}, {**THRESHOLDS, **data.get("thresholds", {})}


def score(d, w=WEIGHTS, ev=EVIDENCE, th=THRESHOLDS):
    """Return (adjusted score rounded to 1 decimal or None, priority). Knockout floor: Demand, Feasibility or Cost = 1 caps A/B at C."""
    if any(d.get(g) == "no" for g in GATES):
        return None, "Stopped"
    if any(d.get(c) is None for c in CRIT):
        return None, "incomplete"
    raw = sum(w[c] * d[c] for c in CRIT)
    adj = round(raw * ev.get(d.get("evidence", "E0"), ev["E0"]), 1)
    prio = "A" if adj >= th["A"] else "B" if adj >= th["B"] else "C" if adj >= th["C"] else "D"
    if prio in ("A", "B") and any(d[c] <= 1 for c in FLOOR):
        prio = "C"   # fatal weaknesses are not averaged away
    return adj, prio


def economics(d):
    """Return (margin, break-even customers or None)."""
    try:
        m = d["price"] - d["variable_cost"]
        return m, (-(-d["fixed_costs"] // m) if m > 0 else None)
    except (KeyError, TypeError):
        return None, None


def sensitivity(ideas, w, ev, th, delta=.2):
    """Perturb each weight by +/-delta, renormalize; report rank/class stability."""
    base = {i["idea"]: score(i, w, ev, th) for i in ideas}
    ranked = lambda s: [k for k, v in sorted(s.items(), key=lambda kv: -(kv[1][0] or 0)) if v[0] is not None]
    top, flips, class_changes = ranked(base)[:1], 0, 0
    runs = 0
    for c in CRIT:
        for sign in (-1, 1):
            w2 = dict(w); w2[c] *= 1 + sign * delta
            t = sum(w2.values()); w2 = {k: v / t for k, v in w2.items()}
            s = {i["idea"]: score(i, w2, ev, th) for i in ideas}
            runs += 1
            flips += ranked(s)[:1] != top
            class_changes += sum(s[k][1] != base[k][1] for k in s)
    return {"runs": runs, "top_changed_in": flips, "class_changes_total": class_changes, "top": top}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    w, ev, th = config(data)
    for i in data["ideas"]:
        print(i["idea"], *score(i, w, ev, th), *economics(i))
    if "--sensitivity" in sys.argv:
        print(sensitivity(data["ideas"], w, ev, th))
