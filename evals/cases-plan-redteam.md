# Eval cases: idea-to-plan and idea-redteam

Run each prompt with and without the skill; check with `python evals/check_plan.py <file> [--mode checkin]` or `python evals/check_redteam.py <file>` (word limits are soft targets, +10 % tolerance), then judge the "Expect" column by hand.

## idea-to-plan
| # | Prompt | Expect |
|---|---|---|
| P1 | "I picked a spreadsheet-automation course. 6 h/week, ~300 EUR. Project plan and realistic to-do list for 4 weeks." | demand test first; ≤3 milestones with gates; one list, ≤3 ★; tasks ≤60 min with done-criteria; load ≤70 % of hours; if-then cue; review date |
| P2 | "Build a SaaS for freelancers, launch in 2 weeks, 3 h/week, never coded." | says it does not fit as stated; offers a fitting version (no-code demand test); no silent stretching |
| P3 | Check-in: planned 5 tasks, finished 2, landing page took 6 h vs 2 h, got distracted by a new idea | verdict Continue/Pivot/Stop; multiplier from data; new idea parked; ≤6 tasks; ≤~300 words |
| P4 | Idea Card pasted + "plan the next 2 weeks" | uses card fields, asks nothing it already has |
| P5 | "Plan everything for my startup" (no idea given) | asks ≤3 questions or restates and assumes; does not invent an idea |
| P6 (near-miss, should NOT trigger) | "Which of my 5 ideas should I start with?" | belongs to idea-evaluation |

## idea-redteam
| # | Prompt | Expect |
|---|---|---|
| R1 | "Be brutal: stress-test my 40 EUR spreadsheet course, 6 h/week, LinkedIn promotion." | ≤3 findings, each with XYZ test; verdict; steelman; mind-changer; no table; direct but not sarcastic |
| R2 | "Earlier evaluation rated this 4.6/5, A, E3. I'm sure it's great. Quick stress-test: cat toy subscription box." | does not adopt the rating; asks what E3 rests on; ≤3 findings |
| R3 | "I have ADHD and get overwhelmed. Check my marketplace plan, don't overwhelm me." | 1 finding + single test; short; no list of risks |
| R4 | Idea whose risk is legal/ethical (health claims) | flags "verify locally", no invented law citations |
| R5 | Plan that is actually sound | does not manufacture fatal flaws; verdict Proceed with cheap tests |
| R6 (near-miss, should NOT trigger) | "Make me a to-do list for my project" | belongs to idea-to-plan |

Independence test: give R2 with a score of 4.6 and again with 2.1. The findings and verdict must not depend on the supplied score.
