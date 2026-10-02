# Test library (cheapest test that can falsify the riskiest assumption)
Always set before running: **time-box, numeric pass threshold, kill criterion.** Prefer tests that produce behavior or commitment over opinions.

| Test | Proves | Typical effort | Example pass signal |
|---|---|---|---|
| Problem interviews (past behavior) | problem is real and costly | 5–10 talks, days | ≥ 6 of 10 describe the problem unprompted and a current workaround |
| Competitor / price teardown | demand and price range exist | hours | ≥ 3 paid alternatives with visible customers |
| Search / community demand check | people look for a solution | hours | recurring questions, steady search volume |
| Smoke test / fake door (landing page + sign-up) | interest in the offer | 1–3 days | ≥ 5 % of targeted visitors leave contact data |
| Pre-sale / deposit / letter of intent | willingness to pay | 1–2 weeks | ≥ 3 paid commitments or signed LOIs |
| Concierge MVP (do it by hand for 1–3 customers) | value of the outcome | 1–2 weeks | customers pay or return unprompted |
| Wizard of Oz (fake automation) | usability and value | 1–2 weeks | task completed, repeated use |
| Paper / clickable mock-up | comprehension | 1–3 days | users complete the main task unaided |
| Technical spike | feasibility of the hardest part | 1–5 days | works at minimum required quality |
| Prior-art search | novelty / freedom to operate | hours | no blocking existing claims found |
| Single-feature MVP or paid pilot | retention and economics | 2–6 weeks | repeat use, margin > 0 |
| Crowdfunding / waitlist with price | scaled demand | 2–4 weeks | target reached or conversion threshold met |

Rules: one assumption per test; a test that cannot fail is not a test; record the result as an evidence level (E0–E4) and re-score in Update mode.
