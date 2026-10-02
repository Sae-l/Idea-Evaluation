"""Run every check. Usage: python tests/run_all.py   (needs requirements-dev.txt for the spreadsheet checks)"""
import os, subprocess, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
steps = [["tests/test_scoring.py"], ["tests/test_checkers.py"], ["tests/test_skills_in_sync.py"], ["tests/test_repo_files.py"], ["tests/check_xlsx_formulas.py"], ["tools/build_packages.py", "--check"]]
failed = []
for s in steps:
    print("::", " ".join(s), flush=True)
    if subprocess.run([sys.executable] + s, cwd=ROOT).returncode:
        failed.append(" ".join(s))
print("FAILED: " + ", ".join(failed) if failed else "all checks passed")
sys.exit(1 if failed else 0)
