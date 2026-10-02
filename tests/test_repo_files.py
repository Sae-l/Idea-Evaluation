"""Structural checks for repository metadata. Run: python tests/test_repo_files.py   (needs PyYAML)"""
import glob, os, re, sys
import yaml
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
bad = []
for f in sorted(glob.glob(os.path.join(ROOT, ".github", "**", "*.yml"), recursive=True)):
    rel = os.path.relpath(f, ROOT)
    try:
        doc = yaml.safe_load(open(f, encoding="utf-8"))
    except yaml.YAMLError as e:
        bad.append(f"{rel}: invalid YAML: {e}"); continue
    if "ISSUE_TEMPLATE" in rel and rel.endswith("config.yml"):
        continue
    if "ISSUE_TEMPLATE" in rel:                                   # issue forms
        for k in ("name", "description", "body"):
            if k not in doc: bad.append(f"{rel}: missing '{k}'")
        for item in doc.get("body", []):
            for opt in item.get("attributes", {}).get("options", []):
                if not isinstance(opt, str): bad.append(f"{rel}: option {opt!r} is not a string (quote yes/no/on/off)")
    if "workflows" in rel:                                        # workflows: least privilege, bounded runtime
        if "permissions" not in doc: bad.append(f"{rel}: no top-level 'permissions'")
        for name, job in (doc.get("jobs") or {}).items():
            if "timeout-minutes" not in job: bad.append(f"{rel}: job '{name}' has no timeout-minutes")
        text = open(f, encoding="utf-8").read()
        for line in re.findall(r"^\s*-?\s*uses:\s*(\S+)", text, re.M):
            if "@" not in line: bad.append(f"{rel}: action '{line}' is not versioned")
owners = open(os.path.join(ROOT, ".github", "CODEOWNERS"), encoding="utf-8").read().split()
if len(owners) < 2 or not owners[1].startswith("@"): bad.append("CODEOWNERS: no owner")
print("FAIL:\n  " + "\n  ".join(bad) if bad else "repository metadata ok")
sys.exit(1 if bad else 0)
