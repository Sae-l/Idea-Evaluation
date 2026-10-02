"""Optional: recalculates the generated workbook with the `formulas` package (pip install formulas openpyxl)
and compares adjusted score, priority, margin and break-even with scoring.py. Run: python tests/check_xlsx_formulas.py"""
import json, os, subprocess, sys, tempfile
import formulas, openpyxl
HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(HERE, "..", "idea-evaluation", "scripts")
sys.path.insert(0, SCRIPTS)
from scoring import config, economics, score

src = os.path.join(HERE, "sample_ideas.json")
data = json.load(open(src)); w, ev, th = config(data)
with tempfile.TemporaryDirectory() as d:
    out = os.path.join(d, "s.xlsx")
    subprocess.run([sys.executable, os.path.join(SCRIPTS, "build_xlsx.py"), src, out], check=True, capture_output=True)
    sol = formulas.ExcelModel().loads(out).finish().calculate()
    ws = openpyxl.load_workbook(out)["Comparison"]
    col = {c.value: c.column_letter for c in ws[1]}
    by = {i["idea"]: i for i in data["ideas"]}
    for r in range(2, ws.max_row + 1):
        name = ws[f"B{r}"].value
        if name not in by:
            continue
        get = lambda h: sol[f"'[s.xlsx]COMPARISON'!{col[h]}{r}"].value[0][0]
        s, p = score(by[name], w, ev, th); m, be = economics(by[name])
        assert (get("Adjusted score") or None) == s and get("Priority") == p, name
        assert (get("Margin") or None) == m and (get("Break-even customers") or None) == be, name
print("xlsx formulas match scoring.py")
