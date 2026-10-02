"""Mechanical checks for idea-to-plan answers. Usage: python check_plan.py answer.md [--mode plan|checkin]"""
import re, sys

text = open(sys.argv[1], encoding="utf-8").read()
mode = sys.argv[sys.argv.index("--mode") + 1] if "--mode" in sys.argv else "plan"
TOLERANCE = 1.1  # word limits are soft targets; allow +10 %
words, fails = len(text.split()), []
if words > TOLERANCE * (350 if mode == "checkin" else 650): fails.append(f"too long: {words} words")

def minutes(line):
    m = re.search(r"(\d+)\s*[-–]\s*(\d+)\s*min", line)          # range: take upper bound
    if m: return int(m.group(2))
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*(?:min|m)\b", line)
    if m: return float(m.group(1).replace(",", "."))
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*(?:h|hr|hrs|hours?)\b", line)
    return float(m.group(1).replace(",", ".")) * 60 if m else None

tasks = [l for l in text.splitlines() if re.match(r"\s*[-*]?\s*\[ \]", l)]
if mode == "plan" and not tasks: fails.append("no checkbox tasks")
no_dur = [t for t in tasks if minutes(t) is None]
too_big = [t for t in tasks if (minutes(t) or 0) > 60]
no_done = [t for t in tasks if not re.search(r"done when|done:|✓|finished when|pass if", t, re.I)]
if no_dur: fails.append(f"{len(no_dur)} tasks without duration")
if too_big: fails.append(f"{len(too_big)} tasks over 60 min")
if tasks and len(no_done) > len(tasks) * 0.3: fails.append(f"{len(no_done)}/{len(tasks)} tasks lack a done-criterion")
stars = len(re.findall(r"\[ \]\s*★", text))
if stars > 3: fails.append(f"{stars} starred (today) tasks (max 3)")
if mode == "plan" and stars < 1: fails.append("no starred (today) task")
names = [re.sub(r"\W+", " ", re.sub(r"\[ \]|★|·.*", "", t)).strip().lower() for t in tasks]
if len(set(names)) < len(names): fails.append("duplicate tasks listed twice")
if mode == "plan":
    for need, pat in (("gate/stop criterion", r"stop if|stop\b.*if|gate"), ("review date", r"review"), ("if-then cue", r"\bwhen\b.*\bI\b"), ("ignition step", r"start now|ignition|first step|≤ ?10 min")):
        if not re.search(pat, text, re.I): fails.append(f"missing {need}")
else:
    if not re.search(r"continue|pivot|stop", text, re.I): fails.append("no verdict")
print(f"{words} words, {len(tasks)} tasks;", "FAIL: " + "; ".join(fails) if fails else "mechanical checks passed")
sys.exit(1 if fails else 0)
