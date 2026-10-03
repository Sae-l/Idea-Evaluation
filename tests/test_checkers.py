"""The eval checkers must accept good answers and reject bad ones. Run: python tests/test_checkers.py"""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
EVALS, FIX = os.path.join(HERE, "..", "evals"), os.path.join(HERE, "fixtures")
cases = [("check_output.py", "quick_ok.md", [], 0), ("check_output.py", "plan_bad.md", [], 1),
         ("check_plan.py", "plan_checkin_ok.md", ["--mode", "checkin"], 0), ("check_plan.py", "plan_bad.md", [], 1),
         ("check_redteam.py", "redteam_ok.md", [], 0), ("check_redteam.py", "redteam_bad.md", [], 1),
         ("check_redteam.py", "redteam_calc_ok.md", [], 0),
         ("check_market.py", "market_ok.md", [], 0), ("check_market.py", "market_bad.md", [], 1),
         ("check_output.py", "quick_ar_ok.md", [], 0), ("check_output.py", "quick_ar_bad.md", [], 1),
         ("check_market.py", "market_ar_ok.md", [], 0), ("check_market.py", "market_ar_bad.md", [], 1)]   # non-Latin text: labels skipped, structure checked
bad = []
for script, fixture, extra, want in cases:
    r = subprocess.run([sys.executable, os.path.join(EVALS, script), os.path.join(FIX, fixture), *extra], capture_output=True, text=True)
    if r.returncode != want:
        bad.append(f"{script} {fixture}: exit {r.returncode}, wanted {want}: {r.stdout.strip()[:120]}")
print("FAIL:\n  " + "\n  ".join(bad) if bad else "eval checkers behave as expected")
sys.exit(1 if bad else 0)
