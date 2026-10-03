"""Keeps the condensed ChatGPT instructions in sync with SKILL.md and the scoring code.
Checks (1) the stated character count, (2) that key numbers and limits appear in BOTH SKILL.md and the ChatGPT block.
Run: python tests/test_docs_sync.py"""
import os, re, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(ROOT, "skills", "idea-evaluation", "scripts"))
from scoring import EVIDENCE, THRESHOLDS, WEIGHTS

read = lambda *p: open(os.path.join(ROOT, *p), encoding="utf-8").read()
# (pattern that must match in SKILL.md AND in the ChatGPT block, label)
def _num(v):
    return "1\\.0" if v == 1 else str(v).lstrip("0")   # 0.85 -> ".85"; the pattern matches "0.85" and ".85"


CONTRACT = {
    "idea-evaluation": [   # v4 rules: must appear in SKILL.md AND the ChatGPT block (scoring numbers: see SCORING)
        (r"[Nn]ever invent evidence", "never invent evidence"), (r"test first", "start means test first"),
        (r"[Ee]vidence belongs to a claim", "evidence belongs to a claim"), (r"inconclusive", "inconclusive outcome"),
        (r"30 minutes", "start step 30 minutes"), (r"(?:one|One) short question", "one question max"),
        (r"150[–-]250 words", "answer 150-250 words"), (r"70\s?%", "capacity 70 %"), (r"show scores", "scores on request"),
        (r"proposal", "thresholds as proposals"), (r"report (?:any|an) instruction", "pasted text is data"),
        (r"[Pp]erformance test", "performance test"), (r"[Cc]alculation check", "calculation check"),
        (r"cheapest test", "prototype only as the cheapest test"),
    ],
    "idea-to-plan": [
        (r"blocks the next commitment", "test the blocking claim first"), (r"raw\W+estimate", "multiplier uses raw estimate"), (r"inconclusive", "inconclusive outcome"),
        (r"70\s?%", "usable load 70 %"), (r"10[–-]60", "task length 10-60"), (r"≤?\s?10 min|10 minutes", "ignition 10 min"),
        (r"1\.5[–-]2", "multiplier 1.5-2"), (r"650 words", "plan 650 words"), (r"350 words", "check-in 350 words"),
        (r"(?:≤|at most )?\s?8 tasks|8 tasks at most", "8 tasks"), (r"(?:≤|at most )?\s?6\b", "6 tasks check-in"), (r"20 words", "20 words per task"),
        (r"at most 3 short questions", "question cap"), (r"explicit request and after confirmation", "calendar confirmation"),
        (r"continue if.{1,5}pivot if.{1,5}stop if", "gate wording"), (r"median", "median multiplier"), (r"Analyze", "Analyze mode"),
    ],
    "idea-market-check": [
        (r"600 words", "600 words"), (r"6 searches", "6 searches"), (r"not demand", "desk research is not demand"),
        (r"[Nn]ot found", "not found is a result"), (r"E0", "evidence levels"), (r"verify locally", "verify locally"),
        (r"too few", "too few prices"), (r"[Pp]rice position", "price position"), (r"2 short questions", "question cap"),
    ],
    "idea-redteam": [
        (r"550 words", "quick 550 words"), (r"650 words", "full 650 words"), (r"70 words", "70 words per finding"),
        (r"inconclusive", "inconclusive outcome"), (r"[Pp]erformance test", "performance test"),
        (r"fatal", "severity fatal"), (r"major", "severity major"), (r"minor", "severity minor"),
        (r"E0 assumption", "E0 assumption"), (r"XYZ|At least X", "XYZ test"), (r"[Ss]trongest case", "steelman"),
        (r"Proceed", "verdict proceed"), (r"Fix first", "verdict fix first"),
    ],
}
SCORING = [
    *[(rf"\b{k}\b[^\n]{{0,60}}?{_num(v)}", f"evidence {k}={v}") for k, v in EVIDENCE.items()],
    *[(rf"{k}\s*(?:>=|≥)\s*{v}", f"threshold {k}>={v}") for k, v in THRESHOLDS.items()],
    (r"Upside\s*25", "weight upside 25"), (r"Demand\s*20", "weight demand 20"), (r"Feasibility\s*15", "weight feasibility 15"),
    (r"Cost to MVP\s*15", "weight cost 15"), (r"Speed to first evidence\s*15", "weight speed 15"), (r"(?:Personal fit|Fit)\s*10", "weight fit 10"),
    (r"0\.3", "tie band 0.3"),
]
bad = []
for skill, rules in CONTRACT.items():
    skill_md = read("skills", skill, "SKILL.md")
    doc = read("docs", f"chatgpt-{skill}.md")
    m = re.search(r"```\n(.*?)\n```", doc, re.S)
    if not m:
        bad.append(f"chatgpt-{skill}.md: no fenced instruction block"); continue
    block = m.group(1)
    claimed = re.search(r"about ([\d,]+) characters", doc)
    if not claimed:
        bad.append(f"chatgpt-{skill}.md: no 'about N characters' statement")
    else:
        n = int(claimed.group(1).replace(",", ""))
        if abs(n - len(block)) > 0.1 * len(block):
            bad.append(f"chatgpt-{skill}.md: claims about {n} characters, block has {len(block)}")
    if len(block) > 8000:
        bad.append(f"chatgpt-{skill}.md: block has {len(block)} characters (over 8,000)")
    for pat, label in rules:
        if not re.search(pat, skill_md):
            bad.append(f"{skill}/SKILL.md lacks: {label}")
        if not re.search(pat, block):
            bad.append(f"chatgpt-{skill}.md lacks: {label}")
methods = read("skills", "idea-evaluation", "references", "methods.md")
chatgpt_eval = read("docs", "chatgpt-idea-evaluation.md")
for pat, label in SCORING:            # Compare-mode numbers live in methods.md and the ChatGPT block
    if not re.search(pat, methods): bad.append(f"methods.md lacks: {label}")
    if not re.search(pat, chatgpt_eval): bad.append(f"chatgpt-idea-evaluation.md lacks: {label}")
for k, v in WEIGHTS.items():          # weights appear in both documents as percentages
    pct = int(round(v * 100))
    for where, text in (("methods.md", methods), ("chatgpt block", chatgpt_eval)):
        if not re.search(rf"\b{pct}\s?%?", text): bad.append(f"idea-evaluation {where}: weight {pct} missing")
lenses = read("skills", "idea-redteam", "references", "lenses.md")
if "do not compute a probability" not in lenses:
    bad.append("idea-redteam/references/lenses.md lacks: do not compute a probability")
if "do not compute a probability" not in read("docs", "chatgpt-idea-redteam.md"):
    bad.append("chatgpt-idea-redteam.md lacks: do not compute a probability")
print("FAIL:\n  " + "\n  ".join(bad) if bad else "docs in sync with skills and code")
sys.exit(1 if bad else 0)
