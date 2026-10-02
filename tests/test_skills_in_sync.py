"""Shared reference files must be identical in every skill that ships them (skills are installed separately).
Run: python tests/test_skills_in_sync.py"""
import glob, os, re, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SHARED = {"idea-card.md": os.path.join(ROOT, "docs", "idea-card.md"), "tests.md": None}
bad = []
for name, canon in SHARED.items():
    copies = sorted(glob.glob(os.path.join(ROOT, "skills", "*", "references", name)))
    canon = canon or copies[0]
    ref = open(canon, encoding="utf-8").read()
    for c in copies:
        if open(c, encoding="utf-8").read() != ref: bad.append(os.path.relpath(c, ROOT))
for skill in glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md")):
    text = open(skill, encoding="utf-8").read()
    m = re.match(r"---\nname: ([a-z0-9-]+)\ndescription: (.+?)\n---\n", text, re.S)
    d = os.path.basename(os.path.dirname(skill))
    if not m or m.group(1) != d: bad.append(f"{d}: frontmatter name mismatch")
    elif len(m.group(2)) > 500: bad.append(f"{d}: description over 500 chars ({len(m.group(2))})")
    elif re.search(r"\b(then|process|step|workflow)\b", m.group(2), re.I): bad.append(f"{d}: description may summarize the workflow")
    for ref in re.findall(r"`(references/[\w.-]+)`", text):
        if not os.path.exists(os.path.join(os.path.dirname(skill), ref)): bad.append(f"{d}: missing {ref}")
print("FAIL:\n  " + "\n  ".join(bad) if bad else "skills in sync")
sys.exit(1 if bad else 0)
