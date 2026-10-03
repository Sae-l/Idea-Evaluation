# Security policy

## Scope
This repository contains plain-text instructions for AI assistants (`skills/*/SKILL.md`, `references/`), two small Python scripts (`scoring.py`, `build_xlsx.py`), tests and tooling. It runs no service and stores no data. The scripts make no network calls: they read a local JSON file and write a local `.xlsx` or `.csv` file; they use no `eval`, no shell and no network. The optional `idea-market-check` skill asks the assistant to search the web, which sends search terms derived from your idea to the search provider; the skill tells the assistant to use generic terms only.

## What could go wrong (threat model)
- **Prompt injection through idea text, pasted documents or fetched web pages.** Each `SKILL.md` tells the assistant that text in pasted documents, files and fetched pages is data, never instructions, and to report instructions it finds there. This is a request to the assistant, not a technical barrier, and it has not been tested against adversarial inputs (see `docs/TRY-IT.md`). It is intended to reduce the risk; its effect is unmeasured. Do not paste secrets or confidential files into an evaluation.
- **Wrong or invented facts** (statistics, laws, prices). The skills require labeling numbers as `fact (source)`, `assumption` or `unchecked` and say "verify locally" for legal topics. They are not professional, legal, financial or medical advice.
- **Malicious changes to skill files** (supply chain). If you install skills from a copy of this repository, compare with the official release and review `SKILL.md` changes before use: instructions in a skill steer the assistant's behavior and tool use.
- **Optional state file `ideas.md`** is written only if the user agrees; it contains whatever the user typed. Keep it out of public repositories if it contains private plans.
- **Spreadsheet output:** `build_xlsx.py` validates its input and stores every user-supplied text value (idea texts, notes, currency, settings labels) as text, so text beginning with `=`, `+`, `-` or `@` is not run as a formula; in CSV such values are prefixed with `'` (visible in the cell). Open exported files from untrusted sources with care anyway.

## Supported versions
Only the latest release receives fixes.

## Reporting a vulnerability
Please **do not open a public issue** for security problems. Use GitHub's private vulnerability reporting: **Security tab → Report a vulnerability** on this repository. Include what you found, how to reproduce it, and the affected file. You should receive a first response within 7 days; fixes are released as a patch version with a note in `CHANGELOG.md`.

If private reporting is not available on the repository, open an issue titled "Security contact request" without details and the maintainer will arrange a private channel.
