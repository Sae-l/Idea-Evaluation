# Methods and scoring anchors (load when scoring or in Deep mode)

## Gate: Desirability / Feasibility / Viability (IDEO)
- **Desirability:** does a specific person have this problem, and would they switch from what they do today?
- **Feasibility:** can it be built or delivered with reachable skills, tools, partners? (Inventions: see `invention-check.md`.)
- **Viability:** can revenue or benefit plausibly exceed cost over time?
Clear "no" = Stopped. "Unknown" = becomes the riskiest assumption. Stage-gate logic: continue, pivot, park or stop at each checkpoint, not once.

## Rating anchors (1–5). Rate relative to the user's stated constraints, not absolute amounts.
| Criterion | 5 | 3 | 1 |
|---|---|---|---|
| **Upside** (profit: revenue potential; impact: people reached × depth; research: novelty × significance) | large, repeatable, scalable | solid but bounded | marginal or one-off |
| **Demand** (people pay or act today for the problem) | many, urgent, already paying for workarounds | some, mild pain | none visible |
| **Feasibility** | proven parts, user can do it | needs learning/partners | needs unproven tech or permissions |
| **Cost to MVP** (vs user's money ceiling) | < 5 % of ceiling | ~ 50 % | exceeds ceiling |
| **Speed to first evidence** (first real signal, not finished product) | ≤ 1 week | ≤ 1–2 months | > 6 months |
| **Personal fit** (skills, access, sustained interest) | strong on all three | some | weak |
Use 2 and 4 as in-betweens.

## Path sets the bar for Upside (state it; default `bootstrap`/`side-project` unless the user says otherwise)
| Path | Upside 5 means | Typical consequence |
|---|---|---|
| bootstrap / side-project | covers a meaningful part of the user's income goal within ~12 months at the stated hours, no outside money | small niches can score well |
| venture | credible route to a very large market with repeatable growth and a defensible edge; outside funding plausible | most lifestyle ideas drop to 2–3; Demand evidence and moat matter more |
| non-profit / impact | many people reached x depth x durability, funding model identified | skip profit economics, check funding |
| research / learning | novelty or skill gained per hour, publishable or portfolio-worthy | Cost and Speed dominate |
The same idea can be A as bootstrap and D as venture. Say which path was used in the footer.

## Knockout floor (fatal weaknesses are not averaged away)
Demand = 1 (no one visibly wants it), Feasibility = 1 (needs the unproven or forbidden) or Cost = 1 (exceeds the ceiling) caps the priority at C and the reason is named in the table row or Parked line. A high average never overrides it. If no ceiling is known, assume a small personal budget and label it as an assumption in the footer.

## Jobs-to-be-Done (internal)
Who, in what situation, wants what progress, and what do they "hire" today (including doing nothing)? Opportunity = high importance + low satisfaction with today's solution.

## Assumption mapping (Bland/Osterwalder)
List what must be true (desirability, viability, feasibility). Plot importance × evidence. Test first: **important and no evidence**.

## Evidence: say vs. do
Opinions and compliments are weak; past behavior is stronger; money, time or commitment is strongest. Interviews: ask about past behavior, not hypotheticals ("Mom Test"). Never count AI or own opinion as evidence above E0.

## Unit economics (top ideas)
`margin = price − variable cost`; `break-even customers = fixed costs ÷ margin`; reachable customers in 12 months = realistic channel reach × conversion, not total market size. If break-even exceeds reachable, say it plainly.

## Base rates (outside view)
Name the reference class (e.g. new employer businesses, consumer apps, hardware startups). Quote a number only with its source, year and country (for example official business-survival statistics of the user's country); otherwise stay qualitative ("most fail without an existing audience"). Adjust the inside view toward the base rate.

## Pre-mortem (Klein)
Assume failure after 12 months; list the most likely cause. If it is fixable cheaply, add the fix to the test.

## Effectuation (Sarasvathy)
Start from means (who I am, what I know, whom I know) and affordable loss, not from a perfect plan. Feeds *fit* and the money ceiling.

## Compare mode: weights, evidence factors, thresholds (only on an explicit "show scores" request)
Rate 1–5, one criterion across all ideas at a time. Weights: Upside 25 % · Demand 20 % · Feasibility 15 % · Cost to MVP 15 % · Speed to first evidence 15 % · Fit 10 %.
Adjusted = weighted score × evidence factor: E0 assumption 0.80 · E1 stated interest 0.85 · E2 observed behavior 0.90 · E3 commitment (deposit, pre-order, paid pilot) 0.95 · E4 repeat paying use 1.0.
Priority from the adjusted score: A ≥ 3.4 · B ≥ 2.8 · C ≥ 2.2 · else D. If the top two are within 0.3, call it a tie and prefer the cheaper test. A B idea gets "lifts to A if …". Show the basis of every rating and say that ratings vary by about ±0.5 between runs. Scores order ideas for a decision; they are never evidence and never replace the test.

## Rounding (identical in `scoring.py` and the spreadsheet)
The weighted raw score is rounded half-up to two decimals, multiplied by the evidence factor, then rounded half-up to one decimal; the priority comes from that one-decimal value.

## Prioritization cross-checks (optional, Deep mode)
ICE (impact × confidence × ease) and RICE (reach × impact × confidence ÷ effort) are quick sanity checks; WSJF (cost of delay ÷ size) when timing matters. If they disagree strongly with the main score, re-examine the ratings.
