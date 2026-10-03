"""Mechanical checks for a saved Quick-mode answer. Usage: python check_output.py answer.txt [--mode quick|update]"""
import re, sys
from lang import LENIENCY, mostly_latin

text = open(sys.argv[1], encoding="utf-8").read()
latin = mostly_latin(text)
scale = 1 if latin else LENIENCY
mode = sys.argv[sys.argv.index("--mode") + 1] if "--mode" in sys.argv else "quick"
words = len(text.split())
fails = []
if mode == "quick":
    if words > 450 * scale: fails.append(f"too long: {words} words (max ~{int(450 * scale)})")
    labels = (("Next", ("next", "nächst")), ("Revisit", ("revisit", "wiedervorlage"))) if latin else ()  # English or German labels
    for need, alts in labels:
        if not any(a in text.lower() for a in alts): fails.append(f"missing '{need}'")
    rows = [l for l in text.splitlines() if l.startswith("|") and not re.match(r"\|[-| ]+\|$", l.strip())]
    if len(rows) > 9: fails.append(f"table too long: {len(rows) - 1} rows (max 8)")
    if rows and max(l.count("|") for l in rows) - 1 > 6: fails.append("table has more than 6 columns")
else:
    if words > 120 * 3 * scale: fails.append(f"update too long: {words} words")
if latin and re.search(r"\b(I have used the skill|I used the skill|as a language model)\b", text, re.I):
    fails.append("contains preamble about the skill")
print(f"{words} words{'' if latin else ' (non-Latin text: label checks skipped)'};", "FAIL: " + "; ".join(fails) if fails else "mechanical checks passed")
sys.exit(1 if fails else 0)
