---
name: idea-evaluation
description: Use when the user wants to evaluate, compare or prioritize ideas (business, product, invention, project, brainstorm or idea lists), decide which idea to start first or park, or check whether an idea is worth pursuing. Not for shopping or everyday decisions.
---

# Idea Evaluation (v3.1)

**Decision first, reasons second, one next action last. Every fact once.** Any user, domain, currency; never assume personal facts, collect or label as assumptions. Reply in the user's language. Neutral, no hype, no shame ("parked" ≠ "bad").

## Modes
**Quick** (default, template below, ~450 words) · **Capture** (brain dump → one line per idea, cluster, park with revisit date, no scoring) · **Update** (new idea/evidence → re-score only what changed, show rank movement, ≤120 words per idea) · **Deep** (one idea → `idea-to-plan` or `idea-redteam` if installed) · **Export** (spreadsheet/CSV via `scripts/build_xlsx.py`, or Idea Card / `ideas.md` state file, see `references/idea-card.md`).

## Process (internal, do not narrate)
1. **Inputs, one pass:** ideas (message, files, `ideas.md`), goal and **path** (bootstrap, venture, side-project, non-profit, research; default bootstrap/side-project), hours/week, money ceiling. Ask **once, max 3 short questions** only if the answer changes the ranking; else assume and list assumptions. If told to assume, never ask. User claims are hypotheses; label numbers `fact (source)`, `assumption`, `unchecked`.
2. **Triage** if >7 ideas: merge duplicates, cluster, score survivors only.
3. **Per idea, one line:** who has the problem; what they do today (the real competitor). Solution without problem → restate in one line. Idea generation is a brainstorming step, not here.
4. **Gate** (desirability, feasibility, viability): clear "no" or harm = **Stop**. Unknown ≠ no: it becomes the test.
5. **Score 1–5, one criterion across all ideas at a time** (anchors, path bars: `references/methods.md`): Upside 25 % · Demand 20 % · Feasibility 15 % · Cost to MVP 15 % · Speed to first evidence 15 % · Fit 10 %.
   **Adjusted = score × evidence factor:** E0 assumption .80 · E1 stated interest .85 · E2 observed behavior .90 · E3 commitment (deposit, pre-order, paid pilot) .95 · E4 repeat paying use 1.0.
   **Priority:** A ≥ 3.4 · B ≥ 2.8 · C ≥ 2.2 · else D, one decimal. **Knockout floor:** Demand, Feasibility or Cost = 1 caps A/B at C and names the reason.
   Re-read the top three in reverse order; if the order flips or scores are within 0.3, call it a tie and prefer the cheaper test. Never rate your own suggestions above the user's without evidence.
6. **Capacity:** one active idea, two at most; everything else parked with a revisit date.
7. **Up to three A/B ideas:** riskiest assumption (user, problem, solution, business, feasibility, adoption) → cheapest test as **"At least X % of Y will Z"** (Z costs money, time or data) with time-box and threshold set before running (`references/tests.md`); unit economics if money matters (margin = price − variable cost; break-even = fixed ÷ margin; customers reachable in 12 months); base rate in one clause (number only if sourced). Only if relevant: build route (`environment.md`), TRL and prior art (`invention-check.md`), rules "verify locally" (`legal-flags.md`), other risks (`checks.md`). Optional market check (3 competitors or substitutes with source) only if search is available and the user wants it; else "unchecked".
8. **Pre-mortem for #1:** "12 months later it failed: most likely reason?" One sentence.
9. **Escape routes:** every Recycle or Stop names one pivot or fix; every B idea gets "lifts to A if …". A low-scoring favorite is never just shot down.

**Verdicts:** Start (A/B, test now) · Recycle (named fix) · Park (revisit date) · Stop (no or harm).
**Edge cases:** one idea → gate + score, no table, ≤350 words: verdict, scores in one line, one Top-3-style block, test with kill criterion, next step · conflicting goals → ask which dominates, default profit · new idea during an active project → park it unless it has stronger evidence, is time-critical, or the active idea hit its kill criterion.

## Output (Quick)
```
**Start with:** [Idea]. [Why, one sentence.] **Next, within 30 min:** [one concrete action].
**Then / later:** [sequence]   **Pre-mortem (#1):** [one sentence]

| # | Idea | Score | Evidence | Cost to MVP | Prio |
|---|---|---|---|---|---|
| 1 | … | 3.5 | E1 | low | A |

**Parked** (revisit [date]): Idea (reason ≤8 words; "→ fix X" if Recycle) · …
**Stopped:** Idea (reason; pivot) · …

### Top 3   (up to three A/B ideas)
**1. Idea**: who pays for what; today solved by …  (B: "lifts to A if …")
- **Riskiest assumption** → **Test:** At least X % of Y will Z | time-box | pass if …
- **Economics:** … | **Base rate:** … | **Check first:** (only if applicable)

**Capacity:** one sentence. **Revisit:** [date ≈ 4 weeks], add test results (Update).
*Estimates ±50 %, unverified. Assumed: [path, goal, hours, budget, currency] … Next step: `idea-to-plan` for the first idea, `idea-redteam` to stress-test it, or ask for a spreadsheet.*
```

## Style (also the ADHD-friendly design)
**Brevity is a hard requirement** (structure is the limit): Top-3 block ≤90 words, Economics/Base rate/Check first one line each, no sentence that changes no decision. Bottom line first, same layout every time, table ≤6 columns and ≤8 rows (A–C only), cells = numbers or ≤4 words. One next action, ≤30 min, verb first; time-box every test, give calendar dates (ISO). Park, never delete; agree the stop criterion in advance. Suggest one commitment aid for #1 in half a sentence (tell someone, fixed slot, body-doubling). Use the user's currency; none given → plain amounts, say so. No preamble or method lectures; frameworks stay internal.

## Honesty and budget
Name competitors, survivorship bias and uncertainty in half-sentences. Prices, laws, tax: "verify" unless checked now. A clearly better variant of an idea: evaluate that and say so. No web search unless one fact would change the ranking. Load `references/` only when the topic applies (`example.md` only to check format). Prefer Update over re-evaluating.
