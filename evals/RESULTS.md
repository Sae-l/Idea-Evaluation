# Eval results (2026-10-02)

Method: same prompts run by a general-purpose subagent (a) without any skill ("baseline") and (b) after reading the skill's SKILL.md. Mechanical checks via `check_plan.py`, `check_redteam.py`, `check_output.py`. **Quality judgments were made by the skill's author (an LLM), not by independent human reviewers; sample sizes are 1 run per prompt, and the same prompt varied by up to ±30 % in length between runs.** Treat as development evidence, not proof.

## idea-to-plan and idea-redteam: baseline vs. skill (words)
| Prompt | Baseline | Skill (first draft) | Skill (after fixes) |
|---|---|---|---|
| P1 course plan | 1,848 | 693 | not re-run |
| P2 unrealistic SaaS plan | 1,562 | 614 | 612 (all checks pass) |
| P3 check-in | 700 | 350 | 461, then 298 after structural limits (passes) |
| R1 brutal stress test | 1,450 (8 findings) | 473 (3 findings) | 516 / 513 (3 findings, passes with +10 % tolerance) |
| R2 pre-rated idea "4.6 / A / E3" | 992 (8 findings, table) | 378 (3 findings) | not re-run |
| R3 overwhelmed user | 326 (4 findings) | 341 (1 finding + single test) | not re-run |

What the skills added over the baseline (baselines were already competent on content): a verdict with stop criteria, a single start step, ≤3 findings with an XYZ test each, steelman and "would change my mind", labeled assumptions instead of unlabeled numbers, one task list (no duplicates) with done-criteria and ≤60 min tasks. In R2 both baseline and skill refused to adopt the supplied rating, so independence was not created by the skill, only made explicit and shorter.

## Findings that changed the skills
- Word limits are followed only loosely by the model; structural limits (sentences/lines per element) worked better (check-in 461 → 298 words). The red-team Quick limit was recalibrated from 350 to 500 words after four runs measured 378–516; checkers allow +10 %.
- Plan answers used "60–90 min" tasks and listed tasks twice (Today and This week) → rule "upper bound ≤60 min", single list with ★.
- idea-evaluation (after trimming to ~990 words): case 9 initially assumed dollars and ran 551 words → currency rule and per-block limits; re-run 432 words, no currency symbol. Case 10 (German) 522 → 380 words, German labels kept.
- **Instability:** in case 10 the top idea flipped between two runs (Excel course vs. tutoring matching). The scores were tied (3.0 vs 3.0), which the skill reports as a tie, but users should treat near-ties as "either is fine; pick the cheaper test", not as a ranking.

## Regression of idea-evaluation (3 of 12 cases re-run: 1, 9, 10)
Case 1: 446 words, passes. Case 9: stops the harmful idea with pivot and "verify locally"; passes after fix. Case 10: passes after fix. Cases 2–8, 11–12 not re-run.

## Not yet measured
Trigger accuracy of the three descriptions (see below if filled in), behavior with real user ideas, effect on users with ADHD, calibration of weights/thresholds/multipliers.
