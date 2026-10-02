# Extended checks (load for Deep mode, or when the named risk is plausible)

**Reversibility (one-way vs. two-way door).** Cheap, reversible steps: just do them. Costly or irreversible steps (signing, hiring, big purchase, public disclosure of an invention, quitting a job): require stronger evidence (E2+) and a written kill criterion first.

**Affordable loss.** State the maximum amount of money, time and reputation the user can lose without regret. Size the first test to a small fraction of it. Never rank by hoped-for return alone.

**Timing and window.** Is something changing (regulation, technology, season, competitor) that makes now better or worse? A closing window raises urgency; an unproven trend lowers it. One sentence.

**Advantage.** Why would this user succeed where others do not (access, skill, data, audience, cost, speed)? No advantage and a crowded field → lower Demand or Fit, say so.

**Portfolio view (several ideas).** Check dependencies (does idea B need A's audience or tool?), shared assets (one test serves two ideas), and option value (a cheap test that keeps a big idea alive). Prefer sequences where early ideas build assets for later ones. Avoid running two ideas that compete for the same scarce resource (time, attention, cash).

**Ethics and harm.** One line: could the idea hurt users, third parties or vulnerable groups, or depend on deception, exploitation of addiction/attention, privacy violations, or illegal activity? A clear yes → Stop (name a pivot), whatever the score.

**Non-commercial goals.** Map *Upside* to the user's goal: impact (people reached × depth × durability), learning (skill gained per hour), research (novelty × significance), enjoyment/portfolio (sustained interest). Say which meaning was used. Skip unit economics unless money matters.

**Sensitivity.** In Export mode or with 3 or more ideas, run `python scripts/scoring.py ideas.json --sensitivity`: if the top idea or classes change when any weight moves ±20 %, call the ranking fragile and decide by the cheaper test instead.
