---
name: idea-evaluation
description: Use when the user wants to evaluate, compare or prioritize ideas (business, product, invention, project, brainstorm or idea lists), decide which idea to start first or park, or check whether an idea is worth pursuing. Not for shopping or everyday decisions.
---

# Idea Evaluation (v3.0)

**Decision first, reasons second, one next action last. Every fact once.** Works for any user, domain and currency; never assume personal facts (time, money, skills, employer): collect or label as assumptions. Reply in the user's language. Neutral tone, no hype, no shame ("parked" is not "bad").

## Modes
- **Quick** (default): template below, max ~450 words.
- **Capture**: brain dump / "just save these" → one line per idea, cluster, park with revisit date, no scoring.
- **Update**: new idea or new evidence → re-score only what changed, show rank movement, ≤120 words per idea.
- **Deep**: one idea in detail → hand over to `idea-to-plan` (analysis, plan, to-do) or `idea-redteam` (stress test) if installed; otherwise do assumptions, economics, 3 tests.
- **Export**: spreadsheet/CSV/Idea Card (`references/idea-card.md`); `scripts/build_xlsx.py` (`--csv` without openpyxl).

## Process (internal, do not narrate)
1. **Inputs, one pass:** ideas (message, attachments, files in context), success goal (default profit), hours/week, money ceiling. If a missing input changes the ranking, ask **once, max 3 short questions**; else assume and list assumptions in the footer.
2. **Triage** if >7 ideas: merge duplicates, cluster, one-line gate each; score survivors only.
3. **Per idea, one line:** who has the problem; what they do today (the real competitor). Only a solution, no problem? Restate in one line; ask only if the restatement could be wrong. Idea generation → brainstorming step, not here.
4. **Gate** (desirability, feasibility, viability) → clear "no" or harm = **Stop** (give a pivot). Unknown ≠ no: it becomes the test.
5. **Score 1–5, one criterion across all ideas at a time** (anchors: `references/methods.md`): Upside 25 % · Demand 20 % · Feasibility 15 % · Cost to MVP 15 % · Speed to first evidence 15 % · Personal fit 10 %.
   **Adjusted = score × evidence factor**: E0 assumption .80 · E1 stated interest .85 · E2 observed behavior .90 · E3 commitment (deposit, pre-order, paid pilot) .95 · E4 repeat paying use 1.0.
   **Priority:** A ≥ 3.4 · B ≥ 2.8 · C ≥ 2.2 · else D. One decimal. Override only with a half-sentence reason.
   Re-read the top three in reverse order; if the order flips (or scores are within 0.3) treat as tie and prefer the cheaper test. Never rate your own suggestions above the user's without evidence.
6. **Capacity:** one active idea, two at most; hours vs. stated time. Everything else parked with a revisit date.
7. **Up to three A/B ideas:** riskiest assumption (user, problem, solution, business, feasibility, adoption: the one that kills the idea if false) → cheapest test as **"At least X % of Y will Z"** (Z costs something: money, time, data), time-box, threshold set before running (`references/tests.md`); unit economics if money matters (price − variable cost = margin; break-even = fixed ÷ margin; customers reachable in 12 months); base rate in one clause (number only if reliably sourced); cheapest build route (`references/environment.md`); inventions: TRL + prior-art note (`references/invention-check.md`); rules: flag as "verify locally" (`references/legal-flags.md`); other risks only if plausible (`references/checks.md`).
8. **Pre-mortem for #1:** "12 months later it failed: most likely reason?" One sentence.
9. **Favorites:** a low-scoring favorite or high-impact idea is not shot down: say what would have to be true to reach A, or a pivot.

**Verdicts:** Start (A/B, test now) · Recycle (named fix needed) · Park (hold, revisit date) · Stop (no or harm).
**Edge cases:** one idea → gate + score vs. bands, no ranking table, end with test and kill criterion · conflicting goals → ask which dominates, default profit · non-commercial goal → map Upside to impact/learning/research · new idea during an active project → captured and parked unless it has stronger evidence, is time-critical, or the active idea hit its kill criterion (`references/checks.md`).

## Output (Quick)
```
**Start with:** [Idea]. [Why, one sentence.] **Next, within 30 min:** [one concrete action].
**Then / later:** [sequence]   **Pre-mortem (#1):** [one sentence]

| # | Idea | Score | Evidence | Cost to MVP | Prio |
|---|---|---|---|---|---|
| 1 | … | 3.5 | E1 | low | A |

**Parked** (revisit [date]): Idea (reason ≤5 words; "→ fix X" if Recycle) · …
**Stopped:** Idea (reason; pivot) · …

### Top 3   (up to three A/B ideas)
**1. Idea**: who pays for what; today solved by …
- **Riskiest assumption** → **Test:** At least X % of Y will Z | time-box | pass if …
- **Economics:** … | **Base rate:** … | **Check first:** (only if applicable)

**Capacity:** numbers. **Revisit:** [date ≈ 4 weeks], add test results (Update).
*Estimates ±50 %, unverified. Assumed: … Next step: `idea-to-plan` for the first idea, `idea-redteam` to stress-test it, or ask for a spreadsheet.*
```

## Style (also the ADHD-friendly design)
**Brevity is a hard requirement** (word counts are soft targets, structure is the limit): each Top-3 block ≤90 words and its Economics/Base-rate/Check-first on one line each; Capacity one sentence; Parked/Stopped reasons ≤8 words. Cut any sentence that does not change a decision. **Currency:** use the user's currency; if none was given, write plain amounts without a currency symbol and say so in the footer.
Bottom line first; same layout every time; table ≤6 columns, ≤8 rows (A–C only), cells = numbers or ≤4 words, no footnote asterisks. Exactly one next action, startable in ≤30 min, verb first; time-box every test and give a calendar date. Park, never delete. Agree the stop criterion in advance. Interest is data (fit) but fades: suggest one commitment aid for #1 (tell someone, fixed slot, body-doubling) in a half-sentence. No preamble, method lectures or repetition. Dates ISO.

## Honesty and budget
Name competitors, survivorship bias and uncertainty in half-sentences. Prices, laws, tax: "verify" unless checked now. If a clearly better variant exists, evaluate that and say so. No web search unless one fact would change the ranking. Load `references/` only when the topic applies (`example.md` only to check format). Prefer Update over re-evaluating. Frameworks stay internal.
