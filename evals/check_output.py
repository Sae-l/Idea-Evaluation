"""Mechanical checks for a saved answer in the v4 template (Start with / Deciding claim / Test). Usage: python check_output.py answer.txt [--mode quick|update]"""
import re, sys
from lang import LENIENCY, mostly_latin

text = open(sys.argv[1], encoding="utf-8").read()
latin = mostly_latin(text)
scale = 1 if latin else LENIENCY
mode = sys.argv[sys.argv.index("--mode") + 1] if "--mode" in sys.argv else "quick"
words = len(text.split())
fails = []
if mode == "quick":   # v4 template: ~150-250 words, so 350 is a tolerance, not a target
    if words > 350 * scale: fails.append(f"too long: {words} words (max ~{int(350 * scale)})")
    labels = (("Start with", ("start with", "beginne mit")), ("Deciding claim", ("deciding claim", "entscheidende annahme")),
              ("Test", ("test:", "test**")), ("pass", ("pass if", "bestanden")), ("stop", ("stop if", "abbruch"))) if latin else ()
    for need, alts in labels:
        if not any(a in text.lower() for a in alts): fails.append(f"missing '{need}'")
else:
    if words > 120 * 3 * scale: fails.append(f"update too long: {words} words")
if latin and re.search(r"\b(I have used the skill|I used the skill|as a language model)\b", text, re.I):
    fails.append("contains preamble about the skill")
print(f"{words} words{'' if latin else ' (non-Latin text: label checks NOT RUN)'};", "FAIL: " + "; ".join(fails) if fails else "mechanical checks passed")
sys.exit(1 if fails else 0)
