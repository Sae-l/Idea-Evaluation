# Idea Card (shared handoff format)

Plain `key: value` lines, all fields optional. Skills read a card if present; otherwise they ask for the minimum (max 3 questions) or mark assumptions. Each skill ships an identical copy at `references/idea-card.md` (checked by `tests/test_cards_in_sync.py`).

```
## Idea Card
idea: <short name>
problem: <who> has <problem>; today solved by <alternative>
goal: profit | impact | learning | other
scores: upside 4 · demand 4 · feasibility 4 · cost 4 · speed 3 · fit 4   (1-5, cost/speed: 5 = cheap/fast)
evidence: E2 · <what the evidence is>   (E0 assumption, E1 stated interest, E2 observed behavior, E3 commitment, E4 repeat paying use)
adjusted: 3.5 · priority A   (weighted score x evidence factor)
riskiest_assumption: <type>: <statement>   (user | problem | solution | business | feasibility | adoption)
test: At least X% of Y will Z · time-box <n days> · pass if <threshold>
kill_if: <stop criterion agreed in advance>
constraints: hours/week <n> · money ceiling <n> <currency> · deadline <date>
status: start | recycle | park | stop · revisit <YYYY-MM-DD>
next_step: <one action, <=30 min>
```
Rules: never invent a field value; write `unknown`. Update `evidence`, `adjusted`, `status`, `revisit` whenever new results arrive. Dates ISO (YYYY-MM-DD).
