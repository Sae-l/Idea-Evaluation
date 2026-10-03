# Contributing

Thanks for helping. This is a small project with strict goals: **short outputs, honest limits, neutral and portable skills.**

## Principles (check every change against these)
1. **Token budget.** `SKILL.md` stays small (target about 1,000 words or less; details go to `references/`, loaded only when needed). Adding text means removing text.
2. **No personal assumptions.** No fixed budgets, hours, currencies, countries or employers. Collect inputs or label assumptions.
3. **No invented facts.** Numbers need a source or the label `assumption`. State where something is a design default, not research.
4. **Test before you claim.** A behavior change needs an eval case (`evals/`) and, if it is computational, a unit test (`tests/`). Report results honestly, including cases where the skill made no difference.
5. **Description says when, not how.** The frontmatter `description` begins with "Use when…" and must not summarize the workflow (the model may follow it instead of the body).

## How to contribute
- Open an issue first for larger changes (new skill, new scoring rule).
- Fork, branch, change, run the checks, open a pull request using the template.
- Keep commits focused; explain *why* in the message.

## Try your change in 5 minutes
1. Copy the skill folder you changed to `~/.claude/skills/` (or `.claude/skills/` in a test project).
2. Ask one of the example prompts from the README (Use table) and read the answer.
3. Compare with the cases in `evals/` and the checker for that skill (for example `python evals/check_output.py answer.md`).

Python 3.10 or newer is needed for the tests (CI runs 3.10 and 3.12). New here? Issues labelled `good first issue` are a good start.

## Checks (run before every PR)
```bash
pip install -r requirements-dev.txt
python tools/build_packages.py          # rebuild dist/*.skill after changing skills/, commit the result
python tests/run_all.py                 # all tests, docs sync, metadata, package check
```
Shared files must be identical across skills (`references/idea-card.md`, `references/tests.md`): edit `docs/idea-card.md` or one copy, then copy to the others; `test_skills_in_sync.py` verifies.

## Evals
Add prompts to `evals/` and record results in `evals/RESULTS.md` (method, sample size, what changed). LLM-judged quality claims must say who judged.

## Licensing
By contributing you agree that your contribution is licensed under the MIT License (see `LICENSE`).
