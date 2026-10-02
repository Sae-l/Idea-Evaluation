---
name: idea-evaluation
description: Use when the user wants to evaluate, compare or prioritize ideas (business, product, invention, project, brainstorm or idea lists), decide which idea to start first or park, or check whether an idea is worth pursuing. Not for shopping or everyday decisions.
---

# Idea Evaluation (v3.1)

**Decision first, reasons second, one next action last. Every fact once.** Any user, domain, currency; never assume personal facts, label assumptions. Reply in the user's language. Neutral, no hype, no shame ("parked" ≠ "bad").

## Modes
**Quick** (default, template below, ~450 words) · **Capture** (brain dump → one line per idea, cluster, park with revisit date, no scoring) · **Update** (new idea/evidence → re-score only what changed, show rank movement, ≤120 words per idea) · **Deep** (one idea in detail: also load `references/methods.md` and `checks.md`; if `idea-to-plan` is installed, hand over to it and offer `idea-redteam` afterwards, else give assumptions, economics and 3 tests) · **Export** (spreadsheet/CSV via `scripts/build_xlsx.py`, or Idea Card / `ideas.md` state file, see `references/idea-card.md`).

## Process (internal, do not narrate)
1. **Inputs, one pass:** ideas (message, files, `ideas.md`), goal and **path** (bootstrap, venture, side-project, non-profit, research; default bootstrap/side-project), hours/week, money ceiling. Ask **at most 3 short questions in total** (one message), only if the answer changes the ranking; else assume and list assumptions. If told to assume, never ask. User claims are hypotheses; label numbers `fact (source)`, `assumption`, `unchecked`.
2. **Triage** if >7 ideas: merge duplicates, cluster, score survivors only.
3. **Per idea, one line:** who has the problem; what they do today (the real competitor). Solution without problem → restate in one line. Generating new ideas is not part of this skill.
4. **Gate** (desirability, feasibility, viability): a clear "no" or harm = **Stop**, which overrides every score. Unknown ≠ no: it becomes the test.
5. **Score 1–5, one criterion across all ideas at a time** (anchors, path bars: `references/methods.md`): Upside 25 % · Demand 20 % · Feasibility 15 % · Cost to MVP 15 % · Speed to first evidence 15 % · Fit 10 %.
   **Adjusted = score × evidence factor:** E0 assumption .80 · E1 stated interest .85 · E2 observed behavior .90 · E3 commitment (deposit, pre-order, paid pilot) .95 · E4 repeat paying use 1.0.
   **Priority** from the adjusted score rounded half-up to one decimal: A ≥ 3.4 · B ≥ 2.8 · C ≥ 2.2 · else D. **Knockout floor:** Demand, Feasibility or Cost = 1 caps A/B at C and names the reason (a gate "no" is stronger: Stop).
   Re-read the top three in reverse order; if the order flips or scores are within 0.3, call it a tie and prefer the cheaper test. Never rate your own suggestions above the user's without evidence.
6. **Capacity:** one active idea, two at most, measured against 70 % of the stated hours; everything else parked with a revisit date.
7. **Up to three A/B ideas:** riskiest assumption (user, problem, solution, business, feasibility, adoption) → cheapest test as **"At least X % of Y will Z"** (Z costs money, time or data) with time-box and threshold set before running (`references/tests.md`); unit economics if money matters (margin = price − variable cost; break-even = fixed ÷ margin; customers reachable in 12 months); base rate in one clause (number only if sourced). Only if relevant: build route (`environment.md`), TRL and prior art (`invention-check.md`), rules "verify locally" (`legal-flags.md`), other risks (`checks.md`). Market check (3 competitors or substitutes with source): only on request, see Honesty.
8. **Pre-mortem for #1:** "12 months later it failed: most likely reason?" One sentence.
9. **Escape routes:** every Recycle or Stop names one pivot or fix; every B idea gets "lifts to A if …". A low-scoring favorite is never just shot down.

**Verdicts:** A → **Start** (at most two at once; capacity decides) · B → Start only if capacity remains, else Park · C → **Recycle** (name the fix) or Park · D → Park · **Stop** only for a gate "no" or harm.
**Edge cases:** one idea → gate + score, no table, ≤350 words: verdict, scores in one line, one Top-3-style block, test with kill criterion, next step · conflicting goals → default profit (use one of the 3 questions only if it changes the ranking) · new idea during an active project → park it unless it has stronger evidence, is time-critical, or the active idea hit its kill criterion.

## Output (Quick)
```
**Start with:** [Idea]. [Why, one sentence.] **Next, within 30 min:** [one concrete action].
**Then / later:** [sequence]   **Pre-mortem (#1):** [one sentence]

| # | Idea | Adj. score | Evidence | Cost to MVP | Prio |
|---|---|---|---|---|---|
| 1 | … | 3.5 | E1 | low | A |

**Parked** (revisit [date]): Idea (reason ≤8 words; "→ fix X" if Recycle) · …
**Stopped:** Idea (reason; pivot) · …

### Top 3   (up to three A/B ideas)
**1. Idea**: who pays for what; today solved by …  (B: "lifts to A if …")
- **Riskiest assumption** → **Test:** At least X % of Y will Z | time-box | pass if … | stop if …
- **Economics:** … | **Base rate:** … | **Check first:** (only if applicable)

**Capacity:** one sentence. **Revisit:** [date ≈ 4 weeks], add test results (Update).
*Estimates ±50 %, unverified. Assumed: [path, goal, hours, budget, currency] … Continue with: `idea-to-plan` (plan #1) · `idea-redteam` (stress-test #1) · spreadsheet on request.*
```

## Style (also the ADHD-friendly design)
**Brevity is a hard requirement** (structure is the limit): Top-3 block ≤90 words, its Economics/Base rate/Check first on one line, delete any sentence that changes no decision. Same layout every time, table ≤6 columns and ≤8 rows (A–C only), cells = numbers or ≤4 words. One next action, ≤30 min, verb first; time-box every test, ISO dates. Park, never delete; fix the stop criterion in advance. One commitment aid for #1 inside the Capacity sentence (tell someone, fixed slot, body-doubling). User's currency; none given → plain amounts, say so. No preamble or method lectures.

## Honesty and budget
Name competitors, survivorship bias and uncertainty in half-sentences. Prices, laws, tax: "verify" unless checked now. A clearly better variant of an idea: evaluate that and say so. Web search only if the user asks for a market check or one fact would change the ranking; otherwise label such facts "unchecked". Load `references/` only when the topic applies (`example.md` only to check format). Prefer Update over re-evaluating.
