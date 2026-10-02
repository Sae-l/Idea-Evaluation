---
name: idea-to-plan
description: Use when the user has chosen an idea or project and wants it analyzed, cut into a first prototype or MVP, turned into a project plan and a realistic to-do list, or wants a progress check-in or re-plan of an existing plan. Not for comparing several ideas.
---

# Idea to Plan (v1.0)

**Smallest plan that tests the riskiest assumption. Realistic beats ambitious. Fixed time, variable scope.** Works for any user, domain and currency; never assume personal facts, collect them or label assumptions. Reply in the user's language, neutral and encouraging, no shame. Output must be short and scannable (ADHD-friendly): decision first, one starting step, small tasks.

## Inputs (one pass)
Idea Card if present (`references/idea-card.md`), else: what the idea is and who it is for; **hours per week**, **money ceiling**, **horizon/deadline**. Ask once (max 3 short questions) only if the answer changes the plan; otherwise assume (default horizon 4 weeks) and list assumptions in the footer.

## Modes
- **Plan** (default): Reality check → Analysis → Milestones → To-do. One answer, aim for ≤650 words.
- **Analyze**: only the analysis block (assumptions, economics, MVP cut).
- **Check-in**: user reports planned vs. done, actual hours, test results → use the Check-in format, aim for ≤300 words.

## Process (internal, do not narrate)
1. **Reality check first.** Usable load = **70 % of stated hours** (default; covers switching and overruns). If the goal does not fit time, skills or money (e.g. launch in 2 weeks at 3 h/week, no experience), say so in one sentence and offer the fitting version: smaller scope or longer horizon, never silently stretch the plan.
2. **Analysis (brief).** Who has the problem, what they do today. Riskiest assumption (user, problem, solution, business, feasibility, adoption) and the **smallest thing that can falsify it** as an XYZ test: "At least X % of Y will Z" (Z costs something) with time-box and threshold (`references/tests.md`). Unit economics if money matters: price − variable cost = margin; break-even = fixed ÷ margin. MVP = that smallest test, not a product. Evidence before building: run the demand test first, build second.
3. **Milestones (max 4; ≤3 rows for horizons up to 4 weeks).** Each: outcome, date, **gate** = continue / pivot / stop criterion fixed in advance. **Circuit breaker:** if a gate is missed, the default is stop or shrink scope; extending needs a new explicit decision. Say what is cut first if time runs short (`references/planning.md`).
4. **To-do list.**
   - Tasks 15–60 min, verb first, each with "done when …". The **upper bound of any range must be ≤60 min** ("45–60 min", never "60–90"); bigger → split. Tests are tasks too (with the threshold).
   - Estimates as ranges; first-time or unfamiliar tasks ×1.5–2 (planning fallacy). Week total ≤ usable load.
   - **Ignition step:** the very first task ≤10 min, doable today.
   - One **This week** list (total ≤ load); mark the first ≤3 tasks with ★ = today. Never repeat a task in two lists. **Later** = parked, unscheduled, one line.
   - **If-then start cue** for the first session: "When [existing routine/time], I open [file/tool] and do [ignition]".
   - Include one review slot per week and one slack block. New ideas go to Later (shiny-object rule).
5. **Stop rule + revisit date** (≈ weekly). Offer to update the Idea Card.

## Check-in logic
Compare done vs. planned and actual vs. estimated hours → new multiplier (actual ÷ estimate, use the median). Convert test results to evidence level (E0 assumption … E4 repeat paying use). Verdict against the gate: **Continue / Pivot / Stop**; if behind, cut scope before adding hours. Re-cut next week's list with the same rules. Name what went well in one line, factually.

## Output (Plan)
```
**Verdict:** [fits / fits only as … / does not fit because …]. **Start now (≤10 min):** [ignition step].
**Riskiest assumption → test:** At least X % of Y will Z | time-box | pass if … | stop if …
**Economics:** … (only if money matters)

| Milestone | By | Gate (continue if … / stop if …) |
|---|---|---|

**This week** (load ≈ N h of M h; ★ = do today, max 3):
- [ ] ★ task · est. 10–15 min · done when …
- [ ] task · est. 30–45 min · done when …
**Later (parked):** …
**If-then cue:** When …, I … **Review:** [date]
*Estimates are defaults (×1.5–2 first-time tasks, 70 % load); adjust after check-in. Assumed: … Next step: `idea-redteam` to stress-test this plan.*
```

## Output (Check-in)
```
**Verdict:** Continue | Pivot | Stop, one line why against the gate. [One factual line on what went well.]
**Numbers:** done X/Y · hours planned vs. actual · multiplier (median actual ÷ estimate) · evidence now E_
**Next week** (load ≈ N h of M h): ★-marked task list as above, scope cut first if behind.
**Parked:** (new ideas, unfinished leftovers)  **Review:** [date]
```

## Rules
**Brevity is a hard requirement** (word counts are only soft targets, structure is the limit): Verdict ≤2 sentences; Numbers one line; Plan mode ≤8 tasks, Check-in ≤6 tasks, each task one line ≤20 words; no explanations of multipliers or methods; if a sentence does not change a decision or an action, delete it.
Max 4 milestones, ≤3 ★ tasks, one ignition step. No task without a done-criterion; no task >60 min. Never schedule 100 % of hours. Calendar entries only on explicit request and after confirmation. Dates ISO. No preamble, no method lectures; frameworks stay internal. Prices, laws, tax: "verify". Idea generation belongs to a brainstorming step.
