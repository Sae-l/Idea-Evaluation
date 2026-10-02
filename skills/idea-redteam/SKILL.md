---
name: idea-redteam
description: Use when the user wants an idea, plan or decision stress-tested before committing time or money, e.g. "red team this", "what could go wrong", "pre-mortem", "devil's advocate", "poke holes", "is my plan solid". Not for choosing between ideas or building a plan.
---

# Idea Red Team (v1.0)

**Find what would kill it, cheaply testable. Max 3 findings. Protective, not discouraging.** Works for any user, domain and currency. Reply in the user's language. Neutral, factual tone: no hype, no doom, no sarcasm even if asked to be "brutal" (be direct instead).

## Independence rules (the point of this skill)
- Earlier scores, priorities, "evidence levels" or the user's certainty are **claims, not facts**. Do not adopt them; ask what they rest on (E0 opinion … E4 repeat paying use) and judge from the facts given.
- Do not soften because the user is sure or invested. Do not inflate to look tough.
- **No invented statistics.** Mark every number as `fact (source)`, or `assumption (range, verify)`. If unsure, reason qualitatively. Laws, prices, tax: "verify locally".
- Web search only if available and only for facts that change a finding (competitors/substitutes, regulation). Name what was found; otherwise label "unchecked".

## Inputs
Idea Card if present (`references/idea-card.md`), else the idea/plan as written. Also: **what is at stake** (time, money, reputation) and **the decision** (start / continue / scale). Ask ≤2 short questions only if the answer changes the verdict (never if the user says to assume); else assume and list assumptions.

## Modes
- **Quick** (default): aim for ≤500 words, each finding ≤70 words (Why ≤2 sentences). · **Full**: ≤600 words, adds watchlist and lens details (`references/lenses.md`).

## Process (internal, do not narrate)
1. Restate idea + decision in one line.
2. **Pre-mortem:** "12 months later this failed. Most likely reasons?" Generate candidates across lenses: demand · substitutes/competition (what they do today, who else) · economics (margin, acquisition cost, reachable customers) · execution (skills, time, hidden steps, dependencies) · timing/reversibility · legal/ethical/harm · assumption stack (does it need many things to all go right?) · sustainability (does the plan survive a bad week?).
3. **Rank** by severity × likelihood, tie-break by how cheap the test is. Keep the **top 3** (Full: plus up to 3 one-line watchlist items). Separate **fixable** from **fatal**.
4. **Per finding:** what goes wrong (1 line) · why plausible (fact/source or labeled assumption) · **cheapest test** written as "At least X % of Y will Z" with time-box and threshold (`references/tests.md`) · fix if true.
5. **Steelman:** the strongest case *for* the idea, one sentence. **What would change my mind:** the evidence that would lift the verdict.
6. **Verdict:** **Proceed** (risks testable cheaply) · **Fix first** (named fix before spending) · **Stop** (fatal flaw or harm). Confidence low/medium/high with one reason.

## Output
```
**Verdict:** Proceed | Fix first | Stop (confidence: …, because …)
**If you only do one thing:** [the single cheapest test, 30 min to start]

**1. [Weakness]** (fixable|fatal)
- Why: … [fact (source) | assumption (range, verify)]
- Test: At least X % of Y will Z | time-box | pass if …
- If true: …
**2. …**  **3. …**

**Strongest case for the idea:** …  **Would change my mind:** …
*Prior rating/claims not verified: [what they rest on]. Assumed: … Next step: `idea-to-plan` to build the test into a plan, `idea-evaluation` to re-rank after results.*
```

## Style (ADHD-friendly)
**Brevity is a hard requirement** (word counts are soft targets, structure is the limit): restatement ≤1 line; per finding: title ≤10 words, Why ≤2 sentences, Test 1 line, If-true 1 line; steelman and mind-changer 1 line each; if a sentence does not change the verdict or a test, delete it.
Verdict first, one list, no tables, no more than 3 findings, one starting action. If the user seems overwhelmed, give only finding #1 and the single test. State risks as testable questions, not as judgments of the person. Dates ISO. No preamble, no repetition, frameworks stay internal.
