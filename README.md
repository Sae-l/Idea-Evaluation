# Idea Evaluation

A portable, user-neutral skill that evaluates and prioritizes ideas (business, product, invention, project, brainstorm output) and answers three questions: **what to start first, what to park, and the cheapest test for each.**

- Decision first, one concrete next action, ≤ ~450-word output, same layout every time.
- Designed to be low-friction for people with ADHD (and everyone else): bottom line up front, one next step, work-in-progress limit, "park, never delete" with revisit dates, time-boxed tests, pre-agreed kill criteria.
- Replies in the user's language; the skill itself is written in English.
- No personal assumptions: time, budget, currency and goals are asked once (max 3 questions) or labelled as assumptions.

## Method (in short)
Viability gate (desirability / feasibility / viability) → six-criterion weighted score → **evidence adjustment** (opinion < behavior < commitment, E0–E4) → priority A–D → riskiest assumption → cheapest test with numeric pass threshold → unit economics, base rate, pre-mortem. Technology readiness level and prior-art check for inventions. Details load on demand from `references/` to save tokens.

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
  references/checks.md        extended checks (reversibility, portfolio, ethics, bias, sensitivity)
  scripts/scoring.py          scoring logic + sensitivity check (no dependencies)
  scripts/build_xlsx.py       optional spreadsheet/CSV export (openpyxl)
tests/      unit tests and spreadsheet-formula cross-check
evals/      12 eval cases + mechanical output checker
docs/       RESEARCH.md (sources, confidence, limits), ChatGPT instructions
dist/       packaged idea-evaluation.skill
```

## Install
- **Claude (Claude Code, claude.ai):** copy `idea-evaluation/` to `~/.claude/skills/` (or `.claude/skills/` in a project), or zip the folder as `idea-evaluation.skill` and upload it under Skills.
- **VS Code / GitHub Copilot (agent skills):** copy to `.github/skills/idea-evaluation/` (also read from `.claude/skills/` and `.agents/skills/`).
- **ChatGPT / other chat tools:** use the condensed instructions in `docs/chatgpt-instructions.md` (Custom GPT or Project) and upload the `references/` files as knowledge.

## Use
"Evaluate these ideas: …", "which idea should I start with?", "prioritize my project list", or add new ideas/results later (Update mode).

## Export
`python idea-evaluation/scripts/build_xlsx.py ideas.json Ideas.xlsx` (`--csv` works without dependencies). JSON schema is in the script header.

## Quality
See `docs/RESEARCH.md` for sources, confidence per design decision and known limits (weights are uncalibrated; ADHD benefit is a design hypothesis, not yet tested with users). Run `python tests/test_scoring.py` after changing the scripts.

## Sources behind the method
Desirability/Viability/Feasibility (IDEO), Stage-Gate (Cooper), Assumption Mapping (Bland & Osterwalder, *Testing Business Ideas*), Lean Startup, Jobs-to-be-Done, The Mom Test, Pretotyping, Effectuation (Sarasvathy), Pre-mortem (Klein), reference-class forecasting (Kahneman), ICE/RICE/WSJF, TRL. Base-rate example: US BLS Business Employment Dynamics.

Estimates produced by the skill are rough (±50 %) and not professional advice.
