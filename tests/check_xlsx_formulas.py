"""Recalculates a generated workbook with the `formulas` package and compares every idea with scoring.py:
adjusted score, priority, margin, break-even. Uses the sample ideas plus 200 seeded random ideas (all ratings 1-5,
all evidence levels, gates), so rounding edge cases and the knockout floor are covered.
Needs: pip install -r requirements-dev.txt.  Run: python tests/check_xlsx_formulas.py"""
import json, os, random, subprocess, sys, tempfile
import formulas, openpyxl
HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(HERE, "..", "skills", "idea-evaluation", "scripts")
sys.path.insert(0, SCRIPTS)
from decimal import Decimal
from scoring import CRIT, EVIDENCE, breakeven_label, config, economics, normalize, score

data = json.load(open(os.path.join(HERE, "sample_ideas.json")))
rng = random.Random(7)
extra = [{"idea": f"rnd{i}", **{c: rng.randint(1, 5) for c in CRIT}, "evidence": rng.choice(list(EVIDENCE)),
          "gate_viability": rng.choice(["yes", "unknown", "no", None, None, None]),
          "price": rng.choice([None, 10, 20]), "variable_cost": rng.choice([None, 5, 20]), "fixed_costs": rng.choice([None, 100, 600])}
         for i in range(200)]
extra.append({"idea": "edge", **{c: 1 for c in CRIT}, "evidence": "E1"})          # 0.85 must round half-up to 0.9
data["ideas"] = data["ideas"] + extra
w, ev, th = config(data)
by = {i["idea"]: i for i in data["ideas"]}
with tempfile.TemporaryDirectory() as d:
    src, out = os.path.join(d, "in.json"), os.path.join(d, "s.xlsx")
    json.dump(data, open(src, "w"))
    subprocess.run([sys.executable, os.path.join(SCRIPTS, "build_xlsx.py"), src, out], check=True, capture_output=True)
    sol = formulas.ExcelModel().loads(out).finish().calculate()
    ws = openpyxl.load_workbook(out)["Comparison"]
    col = {c.value: c.column_letter for c in ws[1]}
    checked = ties = 0


    def is_tie(idea):
        """True if raw * factor lands exactly on x.x5. Real Excel/LibreOffice round such values half-up on the decimal
        value (2.85 -> 2.9); the `formulas` evaluator rounds binary floats (2.8499999... -> 2.8). Python here follows the
        documented Excel behaviour; this checker cannot verify real Excel, so these exact ties are skipped."""
        n = normalize(idea)
        if any(n.get(c) is None for c in CRIT):
            return False
        raw = sum(Decimal(str(w[c])) * Decimal(str(n[c])) for c in CRIT).quantize(Decimal("0.01"))
        return (raw * Decimal(str(ev[n.get("evidence") or "E0"]))) % Decimal("0.1") == Decimal("0.05")

    for r in range(2, ws.max_row + 1):
        name = ws[f"B{r}"].value
        if name not in by:
            continue
        def get(h):
            v = sol[f"'[s.xlsx]COMPARISON'!{col[h]}{r}"].value[0][0]
            return None if v in ("", None) else v   # blank cell = None; a margin of 0 stays 0
        s, p = score(by[name], w, ev, th); m, _ = economics(by[name]); be = breakeven_label(by[name])
        if is_tie(by[name]):
            ties += 1
        else:
            assert get("Adjusted score") == s, (name, get("Adjusted score"), s)
            assert get("Priority") == p, (name, get("Priority"), p)
        assert get("Margin") == m, (name, get("Margin"), m)
        assert get("Break-even customers") == be, (name, get("Break-even customers"), be)
        checked += 1
print(f"xlsx formulas match scoring.py for {checked} ideas ({ties} exact x.x5 ties skipped, see is_tie)")
