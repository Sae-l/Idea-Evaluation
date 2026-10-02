# Changelog

## 3.0 (unreleased)
- Monorepo: `skills/idea-evaluation`, new `skills/idea-to-plan` (analysis, milestones with gates, realistic to-do list, check-in), new `skills/idea-redteam` (independent pre-mortem, max 3 findings, Proceed / Fix first / Stop).
- Shared Idea Card handoff format (`docs/idea-card.md`), kept identical across skills by `tests/test_skills_in_sync.py`.
- `idea-evaluation` trimmed from 1,350 to ~930 words; description now says only when to use it.
- Evals with baseline-vs-skill runs for the new skills (`evals/RESULTS.md`), new checkers `check_plan.py` and `check_redteam.py`.
- ChatGPT instructions per skill (`docs/chatgpt-<skill>.md`); packages `dist/<skill>.skill`.

## 2.1
- Added Capture mode, Recycle verdict, edge-case rules, shiny-object rule.
- Added `references/checks.md` (reversibility, affordable loss, timing, advantage, portfolio, ethics, non-commercial goals, sensitivity, ranking bias).
- Tests are written as XYZ hypotheses with skin in the game.
- Scoring logic moved to `scripts/scoring.py` with `--sensitivity`; unit tests in `tests/`; Excel formulas cross-checked against Python.
- Added `evals/` (12 cases + mechanical output checker), `docs/RESEARCH.md`, ChatGPT instructions, packaged `dist/idea-evaluation.skill`.

## 2.0
- Full rewrite in English, user-neutral, evidence-adjusted scoring, ADHD-friendly output, references on demand.
