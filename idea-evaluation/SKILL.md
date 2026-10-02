---
name: idea-evaluation
description: Evaluates, compares and prioritizes ideas (business, product, invention, project, brainstorm output) and says which to start first, which to park, and the cheapest test for each. Uses a viability gate, evidence-adjusted scoring, riskiest-assumption testing and a pre-mortem. Built to be low-friction for people with ADHD. Use for "evaluate this idea", "which idea first", "prioritize my ideas", "is this worth pursuing", "rank my project list". Not for shopping or everyday decisions.
---

# Idea Evaluation (v2.1)

Principle: **decision first, reasons second, one next action last. Every fact appears once.**
Work for any user, any domain, any currency. Never assume personal facts (time, money, skills, location, employer); collect them or label them as assumptions.

## Language and tone
Reply in the user's language (this file is English only). Neutral, concrete, no shame or hype. "Parked" never means "bad".

## Modes
| Mode | When | Output |
|---|---|---|
| **Quick** (default) | one or more ideas | template below, max ~450 words |
| **Update** | new idea(s) or new evidence for known ideas | re-score only what changed, show rank movement, max 120 words per idea |
| **Deep** | "details on X" | one-idea dossier: assumptions map, unit economics, 3 tests, kill criteria |
| **Export** | user wants a spreadsheet/file | `scripts/build_xlsx.py` (or CSV fallback), see bottom |

## Process (internal; do not narrate)
1. **Context, one pass.** Take ideas from the message, attachments, or files already in context. Needed inputs: *success goal* (profit / impact / research / learning / other; infer only from explicit context, otherwise label the assumption), *time per week*, *money ceiling per idea*. If a missing input would change the ranking, ask **once, max 3 short questions**, in a single message. Otherwise assume a modest default and list the assumption in the footer. Never block on questions.
2. **Triage (>7 ideas).** Merge duplicates, cluster by theme, one-line gate each. Score only survivors.
3. **Clarify each idea in one line:** who has the problem, what they do today (the real competitor, often a spreadsheet, habit or doing nothing). If only a solution is stated and no problem is identifiable, say so in one sentence and offer a problem-first brainstorm instead of guessing.
4. **Gate** (Desirability / Feasibility / Viability, see `references/methods.md`): any clear "no" → **Stopped** (give a pivot if one exists). Unknowns are not "no"; they become the test.
5. **Score** each surviving idea 1–5 on six criteria, **one criterion across all ideas at a time** (reduces halo effect). Anchors in `references/methods.md`.
   Adapt the meaning of demand, upside and evidence to the goal using `references/methods.md`. Do not penalize research or public-benefit projects for lacking paying customers. Preserve existing project gates and evidence taxonomies; label this skill's E0–E4 as **idea-prioritization evidence**, never overwrite a project registry.
   Upside 25 % · Demand 20 % · Feasibility 15 % · Cost to MVP 15 % · Speed to first evidence 15 % · Personal fit 10 %.
   `Score = Σ(weight × rating)`, then `Adjusted = Score × evidence factor`.
   **Business evidence ladder** (use goal-specific anchors in `references/methods.md` for other goals): E0 assumption/own belief ×0.80 · E1 stated interest/compliments ×0.85 · E2 observed past behavior/real demand data ×0.90 · E3 commitment (deposit, pre-order, LOI, paid pilot) ×0.95 · E4 repeat paying use ×1.00.
   Treat weights, factors and thresholds as configurable heuristics, not a validated prediction of success. If modest changes would reverse the recommendation, report the ranking as sensitive. Classify using the unrounded adjusted value; round only its display.
   **Priority on Adjusted:** A ≥ 3.4 · B ≥ 2.8 · C ≥ 2.2 · D below. Show one decimal only (no false precision). Override only with a half-sentence reason.
   Ties (within 0.3): prefer the cheaper, faster test.
6. **Capacity.** Recommend **one active idea, two at most** (work-in-progress limit). Everything else is parked with a revisit date. Compare required hours to the user's stated time.
7. **Top 3 only** (up to three A/B ideas; fewer if fewer qualify):
   - *Riskiest assumption* (user, problem, solution, business, feasibility, adoption): the one that kills the idea if false = high importance, no evidence.
   - *Cheapest test* from `references/tests.md`: time-boxed, with a numeric pass/fail threshold set **before** running it.
   - *Unit economics* if money is involved: `price − variable cost = margin; break-even = fixed costs ÷ margin`, plus customers realistically reachable in 12 months (not total market).
   - *Base rate*: one clause on how often this kind of venture succeeds. Quote a number only from a checked source with a relevant reference class; otherwise say "base rate unknown" without inventing a failure rate.
   - *Cheapest build route:* one line, tool-agnostic (`references/environment.md`).
   - *Invention/hardware only:* Technology Readiness Level and a prior-art/patent search note (`references/invention-check.md`).
   - *Rules/regulation:* flag only relevant categories (`references/legal-flags.md`); say "verify locally", never assert specifics.
8. **Pre-mortem for #1:** "It is 12 months later and this failed. Most likely reason?" One sentence.
9. **Do not shoot down by number.** If the user's favorite or a high-impact idea scores low, state in a half-sentence what would have to be true to make it A, or a pivot.

## Output template (Quick)
```
**Start with:** [Idea]. [Why in one sentence.] **Next, within 30 min:** [one concrete first action].
**Then / later:** [what follows, what waits]
**Pre-mortem (#1):** [one sentence]

| # | Idea | Score | Evidence | Cost to MVP | Prio |
|---|---|---|---|---|---|
| 1 | … | 3.5 | E1 | low | A |

**Parked** (revisit [date]): Idea (reason ≤5 words) · …
**Stopped:** Idea (reason; pivot if any) · …

### Top 3
**1. Idea**: who pays for what; today solved by … (one line)
- **Riskiest assumption** → **Test:** … | pass if … | time-box …
- **Economics:** … | **Base rate:** …
- **Check first:** only if applicable (rules, prior art, TRL)

**Capacity:** one sentence with numbers. **Revisit:** [date ≈ 4 weeks] with test results (Update mode).
*Assumptions: … Evidence gaps: … State numeric uncertainty only when supported. Want a spreadsheet or details on any idea?*
```

## Style rules (also the ADHD-friendly design)
- Bottom line first; short chunks; the same layout every time; no walls of text.
- Table ≤ 6 columns, ≤ 8 rows (A–C only). Cells hold numbers or ≤ 4 words. No footnote asterisks, no unexplained abbreviations.
- Exactly **one** next action, small enough to start in ≤ 30 minutes, starting with a verb. Time-box every test and give a calendar date.
- Park, never delete: parked ideas keep a revisit date, which removes fear of losing them.
- Decide in advance when to stop (kill criteria) to prevent sunk-cost and endless rabbit holes.
- Interest and energy are real data (criterion *fit*); because novelty fades, suggest one commitment aid for the top idea (tell someone, fixed slot, co-working/body-doubling) in a half-sentence.
- No preamble, no method lecture, no repetition. Formats: numbers per the user's locale, dates unambiguous (e.g. 2026-11-01).

## Honesty (brief, never omit)
- Name known competitors, survivorship bias and uncertainty in a half-sentence, not as a separate list.
- Prices, laws, sanctions, tax: say "verify", unless checked now.
- If a promising variant exists, keep the original assessment and present the variant separately; do not silently substitute the user's idea.

## Boundaries and token budget
- This skill **converges** (judges, decides). Generating or widening ideas belongs to a brainstorming step; do that only if asked.
- Frameworks are internal tools: never explain them unless asked.
- Follow the host environment's research rules and explicit search requests. Verify current prices, legal claims, products and base-rate numbers when relied upon; otherwise label them unverified. Avoid unrelated research. Load a `references/` file only when its topic applies (`example.md` only to check format). Run the script only on request. Prefer Update over re-evaluating from scratch.

## Export
Write JSON (schema in `scripts/build_xlsx.py` header), then:
`python scripts/build_xlsx.py ideas.json Ideas_Comparison.xlsx` (add `--csv` if `openpyxl` is unavailable). Set the JSON `goal` and use the matching anchors in `references/methods.md` before rating. The sheet recalculates scores from editable weights, thresholds and evidence levels in a formula-capable spreadsheet application. Classify unrounded scores, display one decimal. Empty lists and invalid inputs are rejected. CSV neutralizes formula-like text with a leading apostrophe; XLSX stores supplied text as literal strings.

