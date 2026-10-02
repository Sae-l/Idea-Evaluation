# Idea Evaluation v2.1

A portable, user-neutral skill that evaluates and prioritizes ideas (business, product, invention, project, brainstorm output) and answers three questions: **what to start first, what to park, and the cheapest test for each.**

- Decision first, one concrete next action, ≤ ~450-word output, same layout every time.
- Designed to be low-friction for people with ADHD (and everyone else): bottom line up front, one next step, work-in-progress limit, "park, never delete" with revisit dates, time-boxed tests, pre-agreed kill criteria.
- Replies in the user's language; the skill itself is written in English.
- No personal assumptions: time, budget, currency and goals are asked once (max 3 questions) or labelled as assumptions.

## Method (in short)
Viability gate (desirability / feasibility / viability) → six-criterion weighted score → **goal-specific evidence adjustment** (E0–E4 for prioritization, not a replacement for project evidence classes) → priority A–D → riskiest assumption → cheapest test with numeric pass threshold → unit economics, base rate, pre-mortem. Technology readiness level and prior-art check for inventions. Details load on demand from `references/` to save tokens.

## Layout
```
idea-evaluation/
  SKILL.md                    core instructions (always loaded)
  references/methods.md       rating anchors, JTBD, assumption mapping, unit economics, base rates
  references/tests.md         test library (smoke test, concierge MVP, pre-sale, ...)
  references/invention-check.md   TRL scale, prior-art/patent search
  references/legal-flags.md   jurisdiction-neutral regulatory flags
  references/environment.md   cheapest build route by idea type
  references/example.md       worked example (format and length check)
  scripts/build_xlsx.py       optional spreadsheet/CSV export (openpyxl)
```

## Install
- **Claude (Claude Code, claude.ai):** copy `idea-evaluation/` to `~/.claude/skills/` (or `.claude/skills/` in a project), or zip the folder as `idea-evaluation.skill` and upload it under Skills.
- **VS Code / GitHub Copilot (agent skills):** copy to `.github/skills/idea-evaluation/` (also read from `.claude/skills/` and `.agents/skills/`).
- **Codex:** install the `idea-evaluation/` folder using the skill installer.
- **ChatGPT / other chat tools:** paste `SKILL.md` into a Custom GPT's or Project's instructions and upload the `references/` files as knowledge.

## Use
"Evaluate these ideas: …", "which idea should I start with?", "prioritize my project list", or add new ideas/results later (Update mode).

## Export
`python idea-evaluation/scripts/build_xlsx.py ideas.json Ideas.xlsx` (`--csv` works without dependencies). JSON schema is in the script header.

## Sources behind the method
Desirability/Viability/Feasibility (IDEO), Stage-Gate (Cooper), Assumption Mapping (Bland & Osterwalder, *Testing Business Ideas*), Lean Startup, Jobs-to-be-Done, The Mom Test, Pretotyping, Effectuation (Sarasvathy), Pre-mortem (Klein), reference-class forecasting (Kahneman), ICE/RICE/WSJF, TRL. Base-rate example: US BLS Business Employment Dynamics.

Scores, evidence factors and priority bands are configurable heuristics, not calibrated success probabilities. Interpret demand and evidence relative to profit, impact, research or learning. State uncertainty from available evidence rather than assigning a universal percentage. Preliminary prior-art searches do not establish freedom to operate.

CSV and XLSX classify unrounded scores, then display one decimal. Formula-looking CSV text is prefixed with an apostrophe; XLSX text stays literal. Workbooks contain formulas that recalculate in Excel or another compatible application; the exporter does not calculate formula caches. Editing weights or thresholds does not automatically re-sort rows; use sorting in the spreadsheet application.

## Verification
Install `openpyxl` for XLSX export and run `python -m unittest discover -s tests -v`. CSV has no third-party runtime dependency. Tests cover score boundaries, missing evidence, stopped/incomplete ideas, input validation, literal text, decimal break-even calculations, and generated workbook formulas. The workflow uses these tests instead of Django scaffolding.

