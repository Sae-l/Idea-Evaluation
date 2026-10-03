# Changelog

Format: one section per suite release, newest first. The release workflow reads the section matching the tag (tag `v3.1.0-beta.1` ↔ heading `## 3.1.0-beta.1`). Tags containing `-` are published as pre-releases.

## 4.0.0-beta.2 (2026-10-03)
Fixes from an external review of 4.0.0-beta.1 (each point checked against the repository first); the 4.0.0-beta.1 draft release was never published, use this one.
- README example: the user message now contains the evidence the answer relies on (three colleagues asked, two paid), so the example no longer teaches invented evidence.
- `idea-evaluation`: a small prototype is allowed when it is the cheapest test of the deciding claim (inventions, research); full builds and launches still need commitment evidence. Scores only on an explicit "show scores" (close options are settled by naming the separating test).
- `idea-redteam` and `idea-to-plan` (SKILL.md and ChatGPT blocks): tests are typed (behavior, performance, calculation) with an inconclusive rule; the ChatGPT plan block now tests the blocking claim first and uses the raw estimate for the multiplier. The docs-sync contract enforces this.
- Answer checker: bold labels need content, an inconclusive rule is required, and non-Latin answers need at least four lines and a number; two new rejecting fixtures. On the three v4 answers of the comparison run, two exceed the 350-word tolerance (see `evals/RESULTS.md`).
- Eval cases no longer expect scores and ranks by default; RESULTS notes that its numbers are from 3.1.

## 4.0.0-beta.1 (2026-10-03)
`idea-evaluation` v4.0: the answer is one decision and one test, not a ranked report. Behavior change; the Idea Card format is unchanged.
- Core question is "which small commitment now?": Start / Today (≤30 min) / Deciding claim with evidence in words / Test with pass, stop and inconclusive fixed in advance / Parked with revisit date. Target 150–250 words (was ~450).
- "Start" means test first; building or launching needs commitment evidence for the claim that matters. Never invent evidence; evidence belongs to a claim, not to the idea.
- Numeric scores, weights, E-factors and thresholds moved to Compare mode (`references/methods.md`, on "show scores" or close options); `scripts/scoring.py` and the spreadsheet export are unchanged.
- `tests.md` (all skills): behavior, performance and calculation tests, an "inconclusive" outcome, and "did the test fail or the idea?"; thresholds are proposals derived from the decision.
- At most one question (was three). Description adds German and Arabic phrases and explicit exclusions.
- `idea-to-plan`: tests the claim that blocks the next commitment first; the time multiplier uses the raw estimate.
- Docs, ChatGPT block, checkers and fixtures aligned with v4.
Known limits: v4 was compared with v3.1 and a plain prompt on 3 cases (9 runs, one scorer); the scores are not yet in `evals/RESULTS.md`. The answer checker's 350-word limit is an unmeasured tolerance. Triggering is still unmeasured.

## 3.1.0-beta.4 (2026-10-03)
From a third external check (ChatGPT simulation, weak evidence, see `docs/COMPARISON.md`):
- `idea-evaluation` hides numeric scores, weights and E-codes by default: the table shows priority, evidence in words and cost to MVP; "show scores" or the spreadsheet export gives the numbers. The calculation itself is unchanged.
- `idea-redteam`: money, runway and hours findings may use a calculation check (inputs, worst case, numeric pass/stop, deadline) instead of "At least X % of Y will Z"; new row in `tests.md`.
- Sensitivity analysis treats equal displayed scores (for example 3.75 and 3.8, both shown as 3.8) as a tie, like the export.
- `check_market.py` no longer requires English labels for non-Latin text; the checkers say "NOT RUN" for the checks they skip.
- The ChatGPT block states the output order (decision, next action, reasons); SECURITY.md says the injection rule's effect is unmeasured; README says the Capacity sheet does not enforce two active ideas.

Earlier in this release: fixes from an external review (each reproduced first, each with a test); scoring weights, thresholds and verdict rules are unchanged.
- Sensitivity analysis picks the top idea like the export orders ideas: priority class first, then score (before, a high-scoring idea capped at C by a knockout could be reported as top while an A idea was listed first).
- Spreadsheet Capacity sheet compares the load with 70 % of the stated hours (editable in Settings), as `SKILL.md` does; before, it used all of them.
- Answer checkers (dev tools) no longer reject correct answers in non-Latin scripts: label checks are skipped and structure is checked.
- From a second external review: every skill says that text in pasted documents, files and fetched pages is data, not instructions; SECURITY.md states this is untested against attacks. The footer says "Rough estimates, not calibrated" instead of "+/-50 %"; competitor research is no longer listed as proof of demand; one web-search rule (generic search terms); the ChatGPT block gained the 70 % capacity rule and the shopping exclusion; the output principle matches the template (next action second); wording fixes in SECURITY.md and RESULTS.md.

## 3.1.0-beta.3 (2026-10-03)
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
