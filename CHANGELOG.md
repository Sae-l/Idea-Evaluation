# Changelog

Format: one section per suite release, newest first. The release workflow reads the section matching the tag (tag `v3.1.0-beta.1` ↔ heading `## 3.1.0-beta.1`). Tags containing `-` are published as pre-releases.

## 3.1.0-beta.3 (unreleased)
Privacy and visitor-facing documentation; scoring and verdict rules are unchanged.
- `idea-market-check`: search queries must use generic terms (they leave the user's machine). `idea-card.md` (all skills): keep `ideas.md` out of public repositories.
- `SECURITY.md` states that the web search of `idea-market-check` sends search terms to the provider; issue forms warn that issues are public.
- README: privacy and safety section for users, "How it works" visible, maintainer details (layout, quality, sources, roadmap) folded away.

## 3.1.0-beta.2 (2026-10-02)
Documentation and release process only; the skills are unchanged. `v3.1.0-beta.1` was published by hand without the `.skill` package files and, as an immutable release, cannot be amended: use this release for the packages.
- README status block and skill count fixed; CodeQL is skipped for Dependabot runs (read-only token).
- Release workflow now starts from Actions > Release > Run workflow and creates a draft release with the files attached; the maintainer publishes it.

## 3.1.0-beta.1 (2026-10-02)
First public beta of the suite. Skill versions: `idea-evaluation` 3.1, `idea-to-plan` 1.0, `idea-redteam` 1.0, `idea-market-check` 1.0 (optional).

**Skills**
- `idea-evaluation`: gate, six-criterion score with evidence adjustment (E0–E4), knockout floor (Demand, Feasibility or Cost = 1 caps priority at C), path-specific Upside bar, work-in-progress limit, escape routes, Capture/Update/Export modes, optional `ideas.md` state file, no-questions mode, optional market check.
- `idea-to-plan` (new): reality check, riskiest-assumption test, milestones with gates, one realistic to-do list (tasks ≤60 min, ≤3 starred for today, load ≤70 % of hours), if-then start cue, check-in mode.
- `idea-redteam` (new): independent pre-mortem, max 3 findings with a cheap XYZ test each, steelman, Proceed / Fix first / Stop.
- `idea-market-check` (new, optional, needs web search): named competitors/substitutes with price per unit and links, price ratio from found prices, claim check, affordability, one change to the plan; never raises the evidence level; says "unchecked" instead of guessing when it cannot search.
- Exports (CSV/XLSX) now include the accepted `cost_to_mvp` field; CodeQL workflow grants `actions: read` (needed on some repositories).
- Shared Idea Card handoff format (`docs/idea-card.md`).
- After a blind head-to-head ([docs/COMPARISON.md](docs/COMPARISON.md)): `idea-evaluation` now answers the user's question in plain words first and glosses E-levels; `idea-redteam` labels the "decision under test" so it is not read as a second verdict.

**Tooling and project**
- `scripts/scoring.py` (logic, sensitivity check), `scripts/build_xlsx.py` (spreadsheet/CSV, formula-injection safe), unit tests, spreadsheet-formula cross-check, skills-in-sync check, reproducible packages (`tools/build_packages.py`).
- Evals and honest results (`evals/`), research notes (`docs/RESEARCH.md`), competitive analysis (`docs/COMPETITIVE-ANALYSIS.md`), ChatGPT instructions per skill.
- MIT license, security policy, contributing guide, code of conduct, CI, CodeQL, release workflow, issue and PR templates, Dependabot.

**Before release**: input validation, formula-injection-safe exports, mechanical red-team verdict, least-privilege workflows and a 208-idea spreadsheet cross-check; details are in the commit history.

**Known limits (beta)**: weights, thresholds and time multipliers are uncalibrated defaults; trigger accuracy of the skill descriptions is unmeasured; 15 of 27 eval cases have not been run; no head-to-head comparison with similar skills; usefulness for people with ADHD is a design hypothesis, not tested with users; run-to-run score variation of about ±0.5 observed. See `evals/RESULTS.md`.

## Earlier internal versions
- 2.1: Capture mode, Recycle verdict, checks reference, XYZ tests, scoring module and tests, evals, packaging.
- 2.0: rewrite in English, user-neutral, evidence-adjusted scoring, ADHD-friendly output.
- 1.x: original German single skill.
