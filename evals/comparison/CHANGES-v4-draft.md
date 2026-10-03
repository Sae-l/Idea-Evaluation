# v4.0-draft: what changed and why

| Change | Reason |
|---|---|
| Core rewritten around "which small commitment now?" | the real question; ranking is secondary |
| Numeric scores moved to Compare mode (on request) | hidden mental arithmetic cost reasoning without changing visible output; run-to-run variation (about ±0.5) exceeded class gaps |
| "Start" = test first; build needs commitment evidence | 6 × 5 at E0 produced 4.0 / A |
| Evidence attached to a claim, in words | one factor per idea overstated confidence |
| Three test types + "inconclusive" + test-vs-idea failure | XYZ alone does not fit inventions or calculations |
| Thresholds as proposals derived from the decision | fixed numbers are not valid for every market |
| Example rewritten: evidence is in the input | the old example invented "colleagues paid" |
| Description: pushy, German and Arabic phrases, explicit exclusions | triggering unmeasured; competing skills installed |
| One question max (was three) | friction; assume and state instead |
| Body 1121 → about 700 words | still above the 300–400 target: the "why" sentences were kept because they improve adherence |

## Unchanged (reused as is)
`references/methods.md`, `idea-card.md`, `environment.md`, `invention-check.md`, `legal-flags.md`, `checks.md`, `scripts/scoring.py`, `scripts/build_xlsx.py`.

## Still to do after the comparison
- Copy the new `tests.md` to `idea-to-plan` and `idea-redteam` (the sync test will require it).
- `idea-to-plan`: replace "demand test first" with "test the claim that blocks the next commitment"; specify that actual ÷ estimate uses the **raw** estimate.
- Update README example, `docs/chatgpt-idea-evaluation.md`, checkers (`evals/check_output.py` expects the old labels).
- Version and CHANGELOG only after the comparison passes.
