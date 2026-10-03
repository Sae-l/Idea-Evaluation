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
    if latin:
        for need in ("Start with", "Deciding claim", "Test"):   # a bold label without content is not an answer
            for m in re.finditer(rf"\*\*{need}:?\*\*:?", text, re.I):
                if len(" ".join(text[m.end():].split("\n")[:3]).split()) < 3: fails.append(f"'{need}' has no content")
        if not re.search(r"inconclusive|unclear|between pass and stop", text, re.I): fails.append("missing inconclusive rule")
    else:   # label checks are skipped, so require visible structure: several lines, a number (threshold/time-box), a date or pass/stop figures
        lines = [l for l in text.splitlines() if l.strip()]
        if len(lines) < 4: fails.append("fewer than 4 non-empty lines (decision, claim, test, parked expected)")
        if not re.search(r"\d", text): fails.append("no number: a test needs a time-box and a pass/stop threshold")
else:
    if words > 120 * 3 * scale: fails.append(f"update too long: {words} words")
if latin and re.search(r"\b(I have used the skill|I used the skill|as a language model)\b", text, re.I):
    fails.append("contains preamble about the skill")
print(f"{words} words{'' if latin else ' (non-Latin text: label checks NOT RUN)'};", "FAIL: " + "; ".join(fails) if fails else "mechanical checks passed")
sys.exit(1 if fails else 0)
