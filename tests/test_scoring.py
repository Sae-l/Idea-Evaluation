"""Run: python tests/test_scoring.py  (no dependencies; xlsx check runs if openpyxl is installed)."""
import json, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(HERE, "..", "skills", "idea-evaluation", "scripts")
sys.path.insert(0, SCRIPTS)
from scoring import config, economics, score, sensitivity

data = json.load(open(os.path.join(HERE, "sample_ideas.json")))
w, ev, th = config(data)
by = {i["idea"]: i for i in data["ideas"]}

# hand-computed: course raw 3.85 * 0.90 = 3.465 -> 3.5 (A); newsletter 4.0 * 0.8 = 3.2 (B)
assert score(by["Course"], w, ev, th) == (3.5, "A")
assert score(by["Newsletter"], w, ev, th) == (3.2, "B")
assert score(by["Device"], w, ev, th) == (2.2, "C")
assert score(by["Marketplace"], w, ev, th) == (2.6, "C")
assert score(by["Blocked"], w, ev, th) == (None, "Stopped")   # gate "no" overrides everything
assert score(by["Partial"], w, ev, th) == (None, "incomplete")
assert economics(by["Course"]) == (37, 17)                    # 600 / 37 = 16.2 -> 17 customers
assert economics(by["Newsletter"]) == (None, None)
assert abs(sum(w.values()) - 1) < 1e-9
s = sensitivity([i for i in data["ideas"] if i["idea"] in ("Course", "Newsletter", "Device", "Marketplace")], w, ev, th)
assert s["runs"] == 12 and s["top"] == ["Course"], s
print("scoring ok;", s)

try:
    import openpyxl  # noqa: F401
except ImportError:
    print("openpyxl missing: xlsx check skipped"); sys.exit()
with tempfile.TemporaryDirectory() as d:
    for fmt, name in (("--csv", "o.csv"), ("", "o.xlsx")):
        cmd = [sys.executable, os.path.join(SCRIPTS, "build_xlsx.py"), os.path.join(HERE, "sample_ideas.json"), os.path.join(d, name)]
        r = subprocess.run(cmd + ([fmt] if fmt else []), capture_output=True, text=True)
        assert r.returncode == 0, r.stderr
    wb = openpyxl.load_workbook(os.path.join(d, "o.xlsx"))
    assert wb.sheetnames == ["Comparison", "Settings", "Capacity"]
    assert wb["Settings"]["B2"].value == 0.25 and wb["Settings"]["B18"].value == 3.4
    print("build ok")
