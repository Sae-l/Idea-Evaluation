# Head-to-head comparison (2026-10-02)

Short version: **no proof that this suite beats a plain, skill-less answer.** It is better at one concrete first step with a stop criterion; it is about equal at labeling unverified claims; it is worse at plain-language clarity and depth. Rivals with web research add verifiable market facts that this suite deliberately leaves out, at 1.5–2× the length.

## What was run
- **Cases** (`evals/comparison/cases.md`): A1 one idea with convincing numbers but weak evidence (night-shift meal-prep box) · A2 one idea with real evidence (4 paid deposits, 3 months of use) · B five ideas, 6 h/week.
- **Systems:** S0 no skill (baseline) · S1 this suite (`idea-evaluation`; for A1/A2 followed by `idea-redteam`) · S2 `validate-idea` (claude-skills-founder, MIT, 686 words) · S3 `grill-my-idea` (EmanuelVogt, MIT, 2,049 words, "don't ask me anything" mode). S2/S3 ran from their public SKILL.md only, without their other files. `business-idea-validator` (about 8,200 words, mandatory web research, no license found) was **not run**; it is compared by reading only.
- **Runs:** 11 without web search (S3 skipped for B; S2 on B was asked to cover all five ideas, which it is not built for), 2 with web search (A1, S2 and S3), 3 re-runs of S1 after a change, 1 run per cell. Subagent model: Sonnet. This is 16 system runs; the plan capped the comparison at 13, the 3 extra are the planned re-test after the change.
- **Judging:** 2 independent blind LLM judges per case (answers shuffled and renamed; 6 judge runs), 1–5 on decision clarity, actionability, honesty, low overwhelm (ADHD-friendliness) and depth. Raw scores: `evals/comparison/judge_scores.json`. Mechanical metrics: `evals/compare_metrics.py`.

## Results (mean of 2 judges, sum of 5 criteria, max 25)
| Case | S0 baseline | S1 this suite | S2 validate-idea | S3 grill-my-idea |
|---|---|---|---|---|
| A1 weak evidence | **20.5** | 20.0 | 17.0 | 19.0 |
| A2 good evidence | **20.0** | 18.5 | 19.5 | 19.0 |
| B five ideas | **21.0** | 19.0 | 20.5 | not run |

Words: S0 880–1,120 · S1 570–860 (A1/A2 include the red-team part) · S2 1,500–1,800 · S3 1,380–1,420.
Criterion pattern over all cases: S1 scored highest on **actionability** (4.5–5 vs 3.5–4 for the baseline); honesty was about equal (S1 4.5–5, baseline 4–5); S1 scored lowest on **decision clarity** (3–3.5 vs 4.5–5) and **depth** (3 vs 4–4.5). S3 had the best depth and the worst overwhelm score (1–2); S2 sat between.

**How much to trust this:** one run per cell, three cases, LLM judges (position and self-preference bias possible, blinding imperfect because the output formats are recognizable). Differences of 1–2 points are noise. Read it as "no sign that the suite is better", not as "the baseline is better".

## Where the others are stronger (observed)
1. **Verifiable market facts.** With web search, both rivals produced what this suite only flags as "unchecked": five named Hamburg competitors at about EUR 5–8 per portion against the user's EUR 13.80, a source for the registration rules, the finding that the "40 %" claim could not be found, and a price-to-take-home ratio (about 10–13 %). The verdict direction stayed the same (not as a launch; test first), but the price gap is a sharper reason (outputs read by the author, not blind-judged). Cost: 4–6 searches, 1,370–1,430 words.
2. **Depth of economics** (scenarios, LTV/CAC, capacity maths such as "6 h/week supports about 8 subscribers"): S3 and S2 were rated deeper than S1.
3. **Plain language.** Judges named jargon (E1, adjusted score, Prio) or two stacked verdicts in all 6 round-1 weakness notes for S1.

## Where this suite is better (observed, not proven)
1. **One cheap first step with a pass/stop threshold**: the baseline gave multi-week plans without a single start-today step in the judges' notes; S2/S3 gave experiments but buried them.
2. **Explicit labels**: friends' praise and unsourced statistics were marked unverified (E1/assumption) in every run; the baseline also doubted them, in prose, so honesty scores were about equal.
3. **Size**: 570–860 words vs 1,400–1,800 for the rivals, no web cost; **portfolio handling** (B) is not offered by the single-idea rivals at all, but the baseline handled it at least as well in these runs.

## Decision: what was adopted
| Candidate | Evidence | Decision |
|---|---|---|
| Plain-language answer first, E-levels glossed on first use (+≈30 words in `idea-evaluation`) | Judges' main complaint about S1 | **Adopted, re-tested.** Re-run S1b vs S1: sum 19 vs 18 (A1), 19 vs 16 (A2), 21 vs 18 (B); S1b ranked first in B, second in A1/A2. One run per case, so weak evidence; word count 570–910, no regression. Jargon is still the top complaint. |
| "Decision under test, not a verdict" wording in `idea-redteam` | Red team said "decision = start" while the evaluation said Park | Adopted (wording only, not separately tested) |
| Market check with web search (competitor prices, claim check, affordability) | Clear added facts in 2 of 2 web runs | **Not adopted into the core.** Already available "on request". Candidate for an optional separate skill (`idea-market-check`); needs its own test and your decision. |
| Scenario economics (LTV/CAC, three cases) | Judged deeper, also longer and more guesswork ("invented scenario numbers") | Not adopted (cost, speculation) |
| Hard research gates, PDF/HTML dossiers, `verdict.json` | Not run / not measured | Not adopted |

## Still open
Jargon-free output, a fair test of the optional market check, and a blind test by a real user (3 minutes: `evals/comparison/cases.md` plus any two outputs). Trigger accuracy and the 15 unrun eval cases are listed in `evals/RESULTS.md`.
