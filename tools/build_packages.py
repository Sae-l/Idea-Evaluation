"""Build dist/<skill>.skill (zip) reproducibly from skills/<skill>/.
Usage: python tools/build_packages.py          write packages
       python tools/build_packages.py --check  exit 1 if dist/ is out of date (used in CI)
Files are sorted and timestamps fixed, so identical sources give identical bytes."""
import io, os, sys, zipfile

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SKILLS, DIST = os.path.join(ROOT, "skills"), os.path.join(ROOT, "dist")
FIXED = (2026, 1, 1, 0, 0, 0)
ALLOWED = {".md", ".py", ".json", ".txt"}   # anything else inside a skill folder is refused, not silently packaged


def build(skill):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_STORED) as z:
        for root, dirs, files in os.walk(os.path.join(SKILLS, skill)):
            dirs[:] = sorted(d for d in dirs if d != "__pycache__")
            for f in sorted(files):
                if f.endswith(".pyc"):
                    continue
                p = os.path.join(root, f)
                if os.path.splitext(f)[1] not in ALLOWED:
                    sys.exit(f"unexpected file in skill folder (not packaged; remove it or extend ALLOWED): {os.path.relpath(p, ROOT)}")
                info = zipfile.ZipInfo(os.path.relpath(p, SKILLS).replace(os.sep, "/"), FIXED)
                info.create_system = 3                      # same bytes on every platform
                info.compress_type, info.external_attr = zipfile.ZIP_STORED, 0o644 << 16
                z.writestr(info, open(p, "rb").read())
    return buf.getvalue()


def main():
    check, stale = "--check" in sys.argv, []
    os.makedirs(DIST, exist_ok=True)
    known = {f"{d}.skill" for d in os.listdir(SKILLS) if os.path.isfile(os.path.join(SKILLS, d, "SKILL.md"))}
    orphans = sorted(f for f in os.listdir(DIST) if f not in known)
    if orphans:
        sys.exit("dist/ contains files without a skill folder: " + ", ".join(orphans))
    for skill in sorted(os.listdir(SKILLS)):
        if not os.path.isfile(os.path.join(SKILLS, skill, "SKILL.md")):
            continue
        data, out = build(skill), os.path.join(DIST, f"{skill}.skill")
        if check:
            if not os.path.exists(out) or open(out, "rb").read() != data:
                stale.append(os.path.relpath(out, ROOT))
        else:
            open(out, "wb").write(data)
            print("wrote", os.path.relpath(out, ROOT))
    if stale:
        sys.exit("out of date (run: python tools/build_packages.py): " + ", ".join(stale))
    if check:
        print("dist/ is up to date")


main()
