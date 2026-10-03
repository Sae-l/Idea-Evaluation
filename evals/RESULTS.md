# Eval results

**v4 note (2026-10-03):** the results below were measured on `idea-evaluation` 3.1 and are kept as history. A 3-case, 9-run comparison of v3.1, v4 and a plain prompt exists but has not been scored or recorded here. Mechanical check on the three v4 answers of that run: two exceeded the 350-word tolerance (366 and 418 words; the skill aims for 150–250), so v4 does not yet meet its own length target.

Last updated 2026-10-02 after the full repository review (skill versions: `idea-evaluation` 3.1, `idea-to-plan` 1.0, `idea-redteam` 1.0, with review fixes).

**Method.** A general-purpose subagent (Claude Sonnet) answers each prompt (a) without any skill ("baseline", first round only) and (b) after reading the skill's `SKILL.md`. Mechanical checks: `check_output.py`, `check_plan.py`, `check_redteam.py` (word limits are soft targets: `check_plan.py` and `check_redteam.py` allow +10 %, `check_output.py` is strict). Content judgments were made by the skill author (an LLM), **not by independent humans**. Usually 1 run per prompt; the same prompt varies by up to about ±30 % in length and about ±0.5 in score between runs. Treat this as development evidence, not proof.

## Status of every defined case
`run` = executed at least once on the current rules; `older rules` = executed only before the review fixes; `not run` = defined but never executed.

| Case | Topic | Status | Latest result |
|---|---|---|---|
| 1 | 5 ideas, income, 6 h/week | run | 428 words, passes; course first, hardware parked |
| 2 | one idea (bakery café) | not run | – |
| 3 | vague idea | not run | – |
| 4 | 25 ideas | not run | – |
| 5 | invention (coating) | not run | – |
| 6 | non-profit | not run | – |
| 7 | Update with new evidence | not run | – |
| 8 | shiny-object idea mid-project | not run | – |
| 9 | harmful idea (fake followers) | run | 429 words; stopped with pivot; no currency invented |
| 10 | German prompt | run | 382 words; German labels kept |
| 11 | no constraints given | not run | – |
| 12 | user insists on low-score favorite | not run | – |
| 13 | same idea, venture vs. bootstrap | run (2×2 runs) | venture C 2.7 in both rounds; within one answer the bootstrap view scored higher (2.9 B), but separate bootstrap runs scored 2.4–2.5 C. **Run-to-run variation is larger than the path effect: path-awareness is not demonstrated.** |
| 14 | "don't ask", impossible idea + deposits | run | no questions; cold fusion stopped; deposit idea first with E3 (3.5 A) |
| 15 | Demand = 1 with high average | run | the idea was stopped by the gate (desirability "no") instead; the knockout floor itself is verified only in unit tests and the 208-idea spreadsheet cross-check, **not in a model run** |
| P1 | 4-week course plan | run | 644 words, 7 tasks, passes |
| P2 | unrealistic SaaS plan | run | 523 words; says it does not fit, offers no-code demand test |
| P3 | check-in after overrun | older rules | 368 words (over the then 300 target) → Check-in format now has a Gate line and a 350-word target; not re-measured |
| P4 | plan from an Idea Card | not run | – |
| P5 | "plan my startup", no idea given | not run | – |
| P6 | near-miss (should not trigger) | not run | trigger accuracy unmeasured, see below |
| R1 | "be brutal" | older rules | 568 words, 3 findings (limit then 500 → now 550, see calibration note) |
| R2 / R2b | independence: prior 4.6/A/E3 vs. 2.1/D/E0 | run (2+2 after fix) | **first round failed**: same findings, but verdict "Fix first" vs. "Proceed". Verdict rule made mechanical (any fatal/major → Fix first). Re-run 2× each: all four "Fix first", same core findings (willingness to pay, margin, churn). |
| R3 | overwhelmed user | run | 261 words, one finding + one test |
| R4 | legal/ethical risk | not run | – |
| R5 | sound plan (should Proceed) | not run | – |
| R6 | near-miss (should not trigger) | not run | – |

Run on current rules: 10 of 27 cases (most only once); 2 more (P3, R1) only under the previous length limits; not run: 15 (2–8, 11–12, P4–P6, R4–R6).

## Baseline vs. skill (first round, before the review fixes)
| Prompt | Baseline words | With skill |
|---|---|---|
| P1 | 1,848 | 693 |
| P2 | 1,562 | 614 |
| P3 | 700 | 350 |
| R1 | 1,450 (8 findings) | 473 (3 findings) |
| R2 | 992 (8 findings, table) | 378 (3 findings) |
| R3 | 326 (4 findings) | 341 (1 finding) |

Baselines were already competent on content. The skills added structure: a verdict with stop criteria, one start step, ≤3 findings with an XYZ test each, labeled assumptions, one task list with done-criteria. **No difference or no benefit:** R3 was not shorter than the baseline; in R2 the baseline also refused to adopt the supplied rating, so independence was not created by the skill.

## Calibration notes (honest about tuning)
- Word limits were adjusted to measured outputs: red-team Quick 350 → 500 → 550 (five runs measured 464–568 words), check-in 300 → 350 (format gained a Gate line). These are fitted defaults, not evidence of brevity.
- Structural limits (sentences per element, tasks per list) shortened outputs more reliably than word counts (check-in 461 → 298 words in the first round).

## Trigger accuracy: not measured
The skill-creator trigger harness (`evals/trigger/*.json`, 8 queries per skill: 4 should trigger, 4 should not; 2 runs each; since 4.0.0-beta.3 `idea-evaluation` has a fifth, Arabic positive query matching its description, not yet run) produced almost no triggers in this sandbox. Per skill, only 1 of 4 positive queries triggered, and only in 1 of 2 runs. A control with the older German skill, whose description matched the queries, also scored 0 of 4. With 100+ competing skills and headless `claude -p`, the harness does not discriminate here. Re-run in a real client.

## Head-to-head with similar skills
See `docs/COMPARISON.md`: 3 cases x 3-4 systems, blind LLM judges. No sign that the suite beats a skill-less baseline; better on one concrete first step, worse on plain-language clarity and depth. After the comparison, `idea-evaluation` puts a plain-language answer first (re-run on 3 cases: sum score +1, +3, +3 out of 25, one run each, weak evidence).

## idea-market-check (cases M1-M3, `evals/cases-market.md`)
M1 (web) 529 words, 6 searches, mechanical checks pass; blind judge: 21/25 vs 18 and 18 for the two rivals with web (1 run, 1 judge, narrower prompt, see `docs/COMPARISON.md`). M2 (no web): nothing invented, rows "unchecked"; the first run wrote "not found (not checked)", so the labels were tightened and not re-run. M3 (web): found free competing tools and a translator-specific counter-fact; checker false positive fixed. Trigger accuracy: not measured.

## Second external check: ChatGPT simulation (2026-10-03, main at `74cb63a`)
Not an independent measurement: one ChatGPT run that simulated the instructions (no skill installed, no code run), with the plain-answer control A written in a context that already contained the instructions (contaminated). Four cases, three variants: A plain answer, B the ChatGPT block as written, B2 the same content without numeric scores, E-codes and score table. Words A/B/B2: 145/189/127, 128/321/132, 125/272/120, 105/261/110. B2 was rated best in all four (clarity/actionability/honesty/low overwhelm/depth, 1-5), B2 and A were close in two; B2 also shortened and reworded the answer, so the effect of hiding scores alone is not isolated. A benign injection note in a pasted text was reported and ignored once. Decision: scores, weights and E-codes are hidden by default and shown on request or in the export (3.1.0-beta.4); this rests on weak evidence and is reversible. Findings left open: the Capacity sheet counts all A and B ideas and does not enforce the limit of two active ideas; the quick-answer checker is strict (450 words) while the plan and red-team checkers allow +10 %.

## Checkers and language
The checkers (`evals/check_*.py`) look for English (quick check: also German) labels. For text that is mostly not Latin script, for example Arabic, they report "label checks NOT RUN" and verify structure only (including `check_market.py`) (length with a 25 % allowance, tables, numbered findings, checkbox and starred tasks); those limits are unmeasured. No Arabic skill answer has been run through them yet beyond a hand-made fixture.

## Not yet measured
Trigger accuracy; the "not run" cases above; behavior with real user ideas; usefulness for people with ADHD; calibration of weights, thresholds and time multipliers against real outcomes.
