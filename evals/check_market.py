"""Mechanical checks for idea-market-check answers. Usage: python check_market.py answer.md"""
import re, sys
from lang import LENIENCY, mostly_latin

text = open(sys.argv[1], encoding="utf-8").read()
latin = mostly_latin(text)   # non-Latin text: English label checks are NOT RUN, only structure is checked
TOLERANCE = 1.1  # word limit is a soft target; allow +10 %
words, fails = len(text.split()), []
if words > TOLERANCE * (1 if latin else LENIENCY) * 600: fails.append(f"too long: {words} words")
if latin and not re.search(r"market check:\s*\**\s*(supports|weakens|changes the plan|inconclusive)", text, re.I): fails.append("no verdict line")
rows = [l for l in text.splitlines() if l.strip().startswith("|") and not re.match(r"\s*\|[\s\-|:]+\|\s*$", l)]
if len(rows) - 1 > 5: fails.append(f"{len(rows) - 1} table rows (max 5)")
no_web = re.search(r"cannot browse|can't browse|no web search|unchecked", text, re.I)
if latin and not re.search(r"https?://", text) and not no_web: fails.append("no source links and no 'unchecked' statement")
if latin and not re.search(r"not demand", text, re.I): fails.append("missing 'desk research is not demand'")
m = re.search(r"searches:\s*(\d+)", text, re.I)
if latin and not m and not no_web: fails.append("missing 'Searches: N' footer")
elif m and int(m.group(1)) > 6: fails.append(f"{m.group(1)} searches (max 6)")
bare = [l for l in text.splitlines() if latin and re.search(r"(€|\$|£|EUR|USD)\s?\d|\d\s?(%|€|EUR|USD)", l)
        and not re.search(r"https?://|fact|estimate|source|unchecked|assum|official|vendor|study|blog|verify|At least|user'?s? (price|figure)|you (said|stated)|found|contradicted|market check:", l, re.I)
        and not l.strip().startswith("|")]
if bare: fails.append(f"{len(bare)} lines with unlabeled numbers: " + " | ".join(b.strip()[:60] for b in bare[:3]))
print(f"{words} words, {len(rows) - 1 if rows else 0} table rows{'' if latin else ' (non-Latin text: verdict, source, searches and number-label checks NOT RUN)'};", "FAIL: " + "; ".join(fails) if fails else "mechanical checks passed")
sys.exit(1 if fails else 0)
