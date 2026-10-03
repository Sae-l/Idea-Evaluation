"""Mechanical checks for idea-redteam answers. Usage: python check_redteam.py answer.md [--mode quick|full]"""
import re, sys
from lang import LENIENCY, mostly_latin

text = open(sys.argv[1], encoding="utf-8").read()
latin = mostly_latin(text)   # non-Latin text: verdict, XYZ, steelman and unlabeled-number checks are skipped
mode = sys.argv[sys.argv.index("--mode") + 1] if "--mode" in sys.argv[:-1] else "quick"
TOLERANCE = 1.1  # word limits are soft targets; allow +10 %
words, fails = len(text.split()), []
if words > TOLERANCE * (1 if latin else LENIENCY) * (650 if mode == "full" else 550): fails.append(f"too long: {words} words")
if latin and (not re.search(r"verdict", text, re.I) or not re.search(r"proceed|fix first|stop", text, re.I)): fails.append("no verdict")
findings = [l for l in text.splitlines() if re.match(r"\s*(\*\*)?\s*\d\.\s", l)]
if len(findings) > 3: fails.append(f"{len(findings)} numbered findings (max 3)")
if len(findings) < 1: fails.append("no findings")
if any(l.strip().startswith("|") for l in text.splitlines()): fails.append("contains a table")
for pat, name in (((r"At least \d+(?: ?%| of)|performance test|calculation", "typed test"), (r"strongest case", "steelman"), (r"change my mind", "what would change my mind")) if latin else ()):
    if not re.search(pat, text, re.I): fails.append(f"missing {name}")
bare = [l for l in text.splitlines() if latin and re.search(r"\d\s?%", l)
        and not re.search(r"assum|fact|verify|source|unchecked|At least|pass if|threshold|stop if|range|estimate|change my mind|strongest case|kill", l, re.I)]
if bare: fails.append(f"{len(bare)} lines with unlabeled numbers: " + " | ".join(b.strip()[:60] for b in bare[:3]))
print(f"{words} words, {len(findings)} findings{'' if latin else ' (non-Latin text: label checks NOT RUN)'};", "FAIL: " + "; ".join(fails) if fails else "mechanical checks passed")
sys.exit(1 if fails else 0)
