# Red-team lenses (load for Full mode)

| Lens | Ask |
|---|---|
| Demand | Who exactly pays, for what problem, instead of what they do today? Has anyone paid or committed (E3) or only said nice things (E1)? |
| Substitutes | What is the cheapest alternative, including doing nothing, a spreadsheet, a free tool, a friend? Why switch? |
| Competition | Who sells this already, at what price? What would make a buyer pick this one? Search if possible. |
| Economics | Price - variable cost = margin? Break-even customers vs. customers reachable in 12 months? Acquisition cost vs. lifetime margin? |
| Execution | Which step needs a skill, permission, partner or supplier the user does not have? Which hidden task is biggest? |
| Timing / reversibility | Is there a window? What is irreversible (contract, public disclosure, spend)? Can the first step be undone? |
| Legal / ethical / harm | Which rule, license, claim limit or safety duty might apply (verify locally)? Who could be hurt or misled? |
| Assumption stack | How many independent conditions must all hold? Count them; do not compute a probability. A long stack is fragile even if each step looks likely. |
| Sustainability | Does the plan assume steady energy and uninterrupted weeks? What happens after a missed week? Is there a slack buffer? |
| Single point of failure | One supplier, platform, person, channel, algorithm? What if it disappears? |

Cognitive traps to check in the user's own reasoning: planning fallacy (inside view), survivorship bias (only successes cited), confirmation bias (only friendly feedback), sunk cost (continuing because of past spend), anchoring on an earlier score.

Severity guide: fatal = cannot work or causes harm (→ Stop, or Fix first if a named fix exists); major = changes economics or timeline by a multiple (→ Fix first); minor = fix during execution (→ Proceed).
