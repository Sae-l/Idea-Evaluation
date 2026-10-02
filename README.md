# Idea Evaluation Suite

> **Status: public beta** · MIT licensed · [Changelog](CHANGELOG.md) · [Security](SECURITY.md) · [Contributing](CONTRIBUTING.md)
> Weights and thresholds are uncalibrated defaults, skill triggering is unmeasured, and the ADHD-friendly design is a hypothesis not yet tested with users. See [evals/RESULTS.md](evals/RESULTS.md) and [docs/RESEARCH.md](docs/RESEARCH.md).

Three small, portable, user-neutral skills for going from a pile of ideas to a decision, a realistic plan and a stress test. Designed with ADHD-friendly principles (not yet tested with users): verdict first, one small next action, work-in-progress limit, "park, never delete", time-boxed tests with stop criteria agreed in advance. Replies follow the user's language; the skills are written in English.

| Skill | Use it when | Output |
|---|---|---|
| [`idea-evaluation`](skills/idea-evaluation) | you have one or many ideas and need to know what to start, park or stop | ranked table, top-3 tests, next action (≤~450 words) |
| [`idea-to-plan`](skills/idea-to-plan) | you picked an idea and need analysis, MVP cut, milestones with gates and a realistic to-do list, or a weekly check-in | verdict, milestones, one task list (★ = today), review date |
| [`idea-redteam`](skills/idea-redteam) | you want an idea or plan attacked before committing time or money | Proceed / Fix first / Stop, max 3 weaknesses with a cheap test each |
| [`idea-market-check`](skills/idea-market-check) (optional, needs web search) | you want competitor prices, a claim or a statistic checked for one idea | named alternatives with price per unit, price position, claim check; never changes the evidence level |

How it differs from similar skills (and where those are stronger): [docs/COMPETITIVE-ANALYSIS.md](docs/COMPETITIVE-ANALYSIS.md).

Flow: `idea-evaluation` → `idea-to-plan` → `idea-redteam` → (after results) `idea-evaluation` again; `idea-market-check` is an optional side trip for one idea. Each skill works alone; they hand over a small [Idea Card](docs/idea-card.md). Skills do not reliably call each other, so each ends with a "Next step" line and you invoke the next one.

## Method (in short)
Viability gate (desirability / feasibility / viability) → six-criterion weighted score → **evidence adjustment** (opinion < behavior < commitment, E0–E4) → priority A–D → riskiest assumption → cheapest test with numeric pass threshold → unit economics, base rate, pre-mortem. Technology readiness level and prior-art check for inventions. Details load on demand from `references/` to save tokens.

## Layout
```
skills/<skill>/SKILL.md          core instructions (loaded when the skill triggers)
skills/<skill>/references/       details, loaded only when needed (idea-card.md and tests.md are identical copies)
skills/idea-evaluation/scripts/  scoring.py (logic + sensitivity check), build_xlsx.py (spreadsheet/CSV export)
docs/                            idea-card.md, RESEARCH.md, COMPETITIVE-ANALYSIS.md, RELEASING.md, chatgpt-<skill>.md
tests/                           unit tests, spreadsheet-formula cross-check, skills-in-sync check
evals/                           eval cases, results (RESULTS.md), output checkers, trigger/ query sets
dist/                            packaged <skill>.skill files (rebuilt by tools/build_packages.py, checked in CI)
tools/                           build_packages.py
requirements-dev.txt             test dependencies (openpyxl, formulas, PyYAML)
.github/                         CI, CodeQL, release workflow, issue/PR templates, Dependabot
SECURITY.md · CONTRIBUTING.md · CODE_OF_CONDUCT.md · LICENSE · docs/RELEASING.md
```

## Install
- **Claude (Claude Code, claude.ai):** copy the skill folders to `~/.claude/skills/` (or `.claude/skills/` in a project), or upload `dist/<skill>.skill` under Skills.
- **VS Code / GitHub Copilot (agent skills):** copy to `.github/skills/<skill>/` (according to the VS Code documentation, `.claude/skills/` and `.agents/skills/` are read too; not tested by this project).
- **ChatGPT / other chat tools:** paste `docs/chatgpt-<skill>.md` into a Custom GPT or Project and upload that skill's `references/` files as knowledge.

## Use
"Evaluate these ideas …", "which idea should I start with?" → `idea-evaluation`. "Plan this idea", "make me a realistic to-do list", "check in on my project" → `idea-to-plan`. "Red-team this", "what could go wrong?" → `idea-redteam`.

## Export
`python skills/idea-evaluation/scripts/build_xlsx.py ideas.json Ideas.xlsx` (`--csv` works without dependencies). JSON schema is in the script header.

## Quality
See `docs/RESEARCH.md` for sources, confidence per design decision and known limits (weights are uncalibrated; ADHD benefit is a design hypothesis, not yet tested with users; trigger accuracy of the descriptions is untested, see `evals/RESULTS.md`). Run `pip install -r requirements-dev.txt && python tests/run_all.py` after changes (CI does the same); `evals/` holds eval cases and checkers (`check_output.py`, `check_plan.py`, `check_redteam.py`) and `evals/RESULTS.md` the latest measured results.

## Sources behind the method
Desirability/Viability/Feasibility (IDEO), Stage-Gate (Cooper), Assumption Mapping (Bland & Osterwalder, *Testing Business Ideas*), Lean Startup, Jobs-to-be-Done, The Mom Test, Pretotyping, Effectuation (Sarasvathy), Pre-mortem (Klein), reference-class forecasting (Kahneman), ICE/RICE/WSJF, TRL. Base-rate example: US BLS Business Employment Dynamics.

Estimates produced by the skills are rough (±50 %) and not professional, legal, financial or medical advice. Feedback from real use, especially from people with ADHD, is the most useful contribution: see the issue templates.

**Privacy:** when you use the skills in a hosted assistant (Claude, ChatGPT, Copilot), your ideas are sent to that provider under its terms. Do not paste secrets or confidential plans you are not allowed to share.

License: [MIT](LICENSE).
