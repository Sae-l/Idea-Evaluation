# Idea Card (shared handoff format)

Plain `key: value` lines, all fields optional. Skills read a card if present; otherwise they ask for the minimum (max 3 questions; a skill may ask fewer) or mark assumptions. Each skill ships an identical copy at `references/idea-card.md`.

```
## Idea Card
idea: <short name>
problem: <who> has <problem>; today solved by <alternative>
goal: profit | impact | learning | other
path: bootstrap | venture | side-project | non-profit | research   (sets the bar for Upside)
scores: upside 4 · demand 4 · feasibility 4 · cost 4 · speed 3 · fit 4   (1-5, cost/speed: 5 = cheap/fast)
evidence: E2 · <what the evidence is>   (E0 assumption, E1 stated interest, E2 observed behavior, E3 commitment, E4 repeat paying use)
adjusted: 3.5 · priority A   (weighted score x evidence factor)
riskiest_assumption: <type>: <statement>   (user | problem | solution | business | feasibility | adoption)
test: At least X% of Y will Z · time-box <n days> · pass if <threshold>
kill_if: <stop criterion agreed in advance>
constraints: hours/week <n> · money ceiling <n> <currency> · deadline <date>
status: start | recycle | park | stop · revisit <YYYY-MM-DD>
escape_route: <for recycle/stop: one pivot or fix that could change the verdict>
next_step: <one action, <=30 min>
```
Rules: never invent a field value; write `unknown`. Claims by the user are hypotheses until evidence says otherwise; tag numbers `fact (source)`, `assumption`, or `unchecked`.

Storing cards (optional): if files can be written and the user agrees, keep all cards in one `ideas.md` (one `## Idea Card` block per idea), read it first in every session and update it after results. Never store personal data beyond what the user typed, and keep `ideas.md` out of public repositories (add it to `.gitignore`). If files cannot be written, print the updated card for the user to paste next time. Update `evidence`, `adjusted`, `status`, `revisit` whenever new results arrive. Dates ISO (YYYY-MM-DD).
