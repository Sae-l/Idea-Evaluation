# Test library (cheapest test that can falsify the riskiest assumption)
Write every test as an **XYZ hypothesis** (Savoia): "At least X % of Y will do Z", where Z carries *skin in the game* (time, money, personal data), not just an opinion.
Always set before running: **time-box, numeric `pass if` threshold and numeric `stop if` threshold.** Prefer tests that produce behavior or commitment over opinions.

| Test | Proves | Typical effort | Example pass signal |
|---|---|---|---|
| Problem interviews (past behavior) | problem is real and costly | 5–10 talks, days | ≥ 6 of 10 describe the problem unprompted and a current workaround |
| Competitor / price teardown | context only (alternatives, prices), not demand | hours | ≥ 3 paid alternatives with visible customers |
| Search / community demand check | people look for a solution | hours | ≥10 distinct questions in 30 days across 3 communities |
| Smoke test / fake door (landing page + sign-up) | interest in the offer | 1–3 days | ≥ 5 % of targeted visitors leave contact data |
| Pre-sale / deposit / letter of intent | willingness to pay | 1–2 weeks | ≥ 3 paid commitments or signed LOIs |
| Concierge MVP (do it by hand for 1–3 customers) | value of the outcome | 1–2 weeks | ≥2 of 3 customers pay or ask for a second round unprompted |
| Wizard of Oz (fake automation) | usability and value | 1–2 weeks | ≥70 % complete the task; ≥3 of 5 return within 7 days |
| Paper / clickable mock-up | comprehension | 1–3 days | ≥4 of 5 users complete the main task unaided |
| Technical spike | feasibility of the hardest part | 1–5 days | meets the stated minimum (write the number first) in ≥8 of 10 runs |
| Prior-art search | novelty / freedom to operate | hours | 0 blocking claims found in 3 databases |
| Single-feature MVP or paid pilot | retention and economics | 2–6 weeks | ≥40 % use it again within 14 days and margin > 0 |
| Crowdfunding / waitlist with price | scaled demand | 2–4 weeks | ≥X % of waitlist pre-pays (set X first) |
| Calculation check (runway, budget, hours) | survives a bad case under stated assumptions (not demand) | 20–60 min | cash stays above the reserve you chose first, in the zero-revenue case, until the deadline |

Rules: if the result lands between `pass if` and `stop if`, do one re-run or one pivot, decided before the test; one assumption per test; a test that cannot fail is not a test; record the result as an evidence level (E0–E4) and re-score (`idea-evaluation` Update mode, or the Check-in of `idea-to-plan`).
