---
name: idea-to-plan
description: Use when the user has chosen one idea or project and wants a plan and a realistic to-do list for it, or a progress check-in or re-plan of an existing plan. Not for comparing several ideas.
---

# Idea to Plan (v1.0)

**Smallest plan that tests the riskiest assumption. Realistic beats ambitious. Fixed time, variable scope.** Any user, domain and currency; never assume personal facts, label assumptions. Reply in the user's language, neutral and encouraging, no shame. Short and scannable: verdict first, one starting step, small tasks.

## Inputs (one pass)
Idea Card if present (`references/idea-card.md`), else the idea, who it is for, **hours per week**, **money ceiling**, **horizon**. Ask at most 3 short questions in total, only if the answer changes the plan; if told to assume, never ask. Otherwise assume (default horizon 4 weeks) and list assumptions in the footer.

## Modes
- **Plan** (default): Reality check → Analysis → Milestones → To-do. One answer, aim for ≤650 words.
- **Analyze**: only the analysis block, Analyze format below.
- **Check-in**: user reports planned vs. done, actual hours, test results → use the Check-in format, aim for ≤350 words.

## Process (internal, do not narrate)
1. **Reality check first.** Usable load = **70 % of stated hours** (default). If the goal does not fit time, skills or money, say so in one sentence and offer the fitting version (smaller scope or longer horizon); never silently stretch the plan.
2. **Analysis (brief).** Who has the problem, what they do today. Riskiest assumption (user, problem, solution, business, feasibility, adoption) and the **smallest thing that can falsify it** as an XYZ test: "At least X % of Y will Z" (Z costs something), time-box, `pass if` and `stop if` (`references/tests.md`). Unit economics only if money matters. MVP = that smallest test, not a product: demand test first, build second.
3. **Milestones (max 4; ≤3 for horizons up to 4 weeks).** Each: outcome, date, **gate** (continue / pivot / stop criteria fixed in advance). **Circuit breaker:** a missed gate means stop or shrink scope by default; extending needs a new explicit decision. Name what is cut first if time runs short (`references/planning.md`).
4. **To-do list.**
   - Tasks 10–60 min, verb first, each with "done when …". Tests are tasks too (with the threshold).
   - Estimate as a range, apply the multiplier first (first-time or unfamiliar tasks ×1.5–2, planning fallacy), then split anything whose **upper bound exceeds 60 min** ("45–60", never "60–90"). Week total ≤ usable load.
   - **Ignition step:** the very first task, ≤10 min, doable today.
   - One **This week** list (total ≤ load); mark the first ≤3 tasks with ★ = today. Never repeat a task in two lists. **Later** = parked, unscheduled, one line.
   - **If-then start cue** for the first session: "When [existing routine], I open [file/tool] and do [ignition]". One weekly review slot and one slack block. New ideas go to Later.
5. **Stop rule + revisit date** (≈ weekly). Offer to update the Idea Card.

## Check-in logic
Compare done vs. planned and actual vs. estimated hours → new multiplier (median of actual ÷ estimate; per task type if ≥3 samples of that type, else overall). Convert test results to evidence level (E0 assumption … E4 repeat paying use). Verdict against the gate: **Continue / Pivot / Stop**; if behind, cut scope before adding hours. Re-cut next week's list with the same rules. Name what went well in one line, factually.

## Output (Plan)
```
**Verdict:** [fits / fits only as … / does not fit because …]. **Start now (≤10 min):** [ignition step].
**Problem:** who has it · today solved by …   **MVP cut:** Must … · Won't now …
**Riskiest assumption → test:** At least X % of Y will Z | time-box | pass if … | stop if …
**Economics:** … (only if money matters)

| Milestone | By | Gate (continue if … / pivot if … / stop if …) |
|---|---|---|

**Stop rule:** [one line, fixed in advance]

**This week** (load ≈ N h of M h; ★ = do today, max 3):
- [ ] ★ ignition task · est. ≤10 min · done when …
- [ ] task · est. 30–45 min · done when …
**Later (parked):** …
**If-then cue:** When …, I … **Review:** [date]
*Estimates are defaults (×1.5–2 first-time tasks, 70 % load); adjust after check-in. Assumed: … Continue with: `idea-redteam` (stress-test this plan). Want the Idea Card updated?*
```

## Output (Analyze)
```
**Problem:** who has it · today solved by …
**Riskiest assumption** (type) → **Test:** At least X % of Y will Z | time-box | pass if … | stop if …
**Economics:** price − variable cost = margin; break-even = fixed ÷ margin; customers reachable in 12 months (only if money matters)
**MVP cut:** Must … · Should … · Won't now …
*Assumed: … Continue with: `idea-to-plan` Plan mode.*
```

## Output (Check-in)
```
**Verdict:** Continue | Pivot | Stop, one line why against the gate. [One factual line on what went well.]
**Numbers:** done X/Y · hours planned vs. actual · multiplier (median actual ÷ estimate) · evidence now E_
**Gate:** [the pass/stop criterion for the current test; if none exists, propose one and mark it assumed]
**Next week** (load ≈ N h of M h): ★-marked task list as above, scope cut first if behind.
**Parked:** (new ideas, unfinished leftovers)  **Review:** [date]
```

## Rules
**Brevity is a hard requirement** (structure is the limit): Verdict ≤2 sentences; Numbers one line; Plan ≤8 tasks, Check-in ≤6, each one line ≤20 words; no explanations of multipliers or methods; delete any sentence that changes no decision or action.
≤3 ★ tasks, one ignition step, every task has a done-criterion and ≤60 min, never schedule 100 % of hours. Calendar entries only on explicit request and after confirmation. Dates ISO. No preamble; frameworks stay internal. Prices, laws, tax: "verify". Generating new ideas is not part of this skill.
