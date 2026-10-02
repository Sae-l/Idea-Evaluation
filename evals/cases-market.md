# Eval cases: idea-market-check

Each case is run with the skill's `SKILL.md` and checked with `python evals/check_market.py answer.md`.

| Case | Prompt (summary) | What a good answer does |
|---|---|---|
| M1 | Meal-prep box for night-shift nurses in Hamburg, EUR 69/week; "40 % skip meals", "billions market"; web search available | named competitors with price per portion and links, price ratio computed from found prices, the 40 % claim traced or "not found", affordability, registration rule, evidence level unchanged |
| M2 | Same idea, web search NOT available | no invented prices or statistics; table rows marked "unchecked"; 3 concrete queries to run; claims "unchecked" (not "not found") |
| M3 | Payment-reminder tool for translators, EUR 9/month, claim "most freelancers wait over 30 days"; web search available | finds free alternatives, checks the claim against translator-specific data, distinguishes agreed terms from lateness, tests the self-serve price |
