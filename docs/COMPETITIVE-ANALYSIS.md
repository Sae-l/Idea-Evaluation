# Competitive analysis (2026-10-02)

**Method and limits.** I read the public README/overview pages of six related open-source skill collections (via a summarizing web fetch, not the full SKILL.md files) and did **not run** any of them. Star counts and feature lists are as reported by those pages and may be incomplete or outdated. Strengths/weaknesses below are my reading, partly inferred; treat as a map for improvement, not as a verdict on others' work. This analysis should have been done before building; it is added afterwards and drove the v3.1 changes.

## The field
| Project | Scope | Strengths | Weaknesses / gaps |
|---|---|---|---|
| [business-idea-validator](https://github.com/allexp1/business-idea-validator-AI-skill) (MIT) | One startup idea → scored verdict (0–100), HTML/PDF brief + `verdict.json` | hard gates that cap the verdict; evidence hierarchy (paying > verbal > behavior > stated); base-rate penalty; separate scoring for bootstrap / venture / service paths; zero-trust handling of user claims with a "verified facts" footer; kill criteria; salvage/uplift plan; dated reference data with refresh; 6 regression cases incl. one that must flip verdict by path | heavy (research, HTML/PDF, Chromium for PDF); one idea at a time; startup/AI-era focus; rubric weights not externally validated; no accuracy data; no planning, no ADHD design |
| [EmanuelVogt/skills `grill-my-idea`](https://github.com/EmanuelVogt/skills) (MIT) | One business idea → dossier with GO / VALIDATE-FIRST / PIVOT / KILL | assumption-tree grilling; claims tagged `[fact] [belief] [assumption] [unknown]`, numbers tagged `[data] [benchmark] [estimate] [guess]` with sources; "fatal weaknesses cannot be averaged away"; negative verdicts must name 2–4 re-costed escape routes; asks only what it cannot look up, or runs "don't ask me anything" | 25–40+ searches per run (token-heavy); locale defaults to Brazil; no tests/evals documented; single idea |
| [claude-skills-founder](https://github.com/emotixco/claude-skills-founder) (MIT) | 13 founder skills (validate, brief, competitors, MVP scope, pricing, GTM, pitch, fundraise…) | "no walls of text", word limits per skill; state saved in a `founder/` folder and reused; never fabricates (placeholders instead); evals README that admits cases where it made no difference | scoring weights and verdict logic undocumented; fundraising/startup-centric; many skills, no capacity or ADHD design |
| [idea-validation-agents](https://github.com/MaxKmet/idea-validation-agents) (MIT) | 15 skills / 4 workflows: generate, validate, market deep dive, pivot | riskiest-assumption test with explicit constraints; multiplicative-floor score ("one catastrophic weakness kills the score"); persistent `memory/` per idea; cross-tool (Claude Code, Codex, Cursor) | fixed example budget/time constraints baked in; app/creator-economy bias (TikTok, ASO); no tests or accuracy data |
| [pm-skills](https://github.com/phuryn/pm-skills) (MIT, reported 26.7k stars) | 69 PM skills, 42 workflows, 9 plugins | breadth (assumption prioritization Impact × Risk, 9 prioritization frameworks, strategy red team, roadmap, sprint plan, SWOT, retros); CI tests and plugin validator; big ecosystem | large surface to learn and load; Claude-optimized commands; generic scoring, no evidence adjustment, no capacity check, no ADHD design |
| [startup-skill](https://github.com/ferdinandobons/startup-skill) (MIT) | Startup design, competitors, positioning, pitch | "30+ structured deliverables"; positioning (April Dunford); real reviews/forums as input | states it can consume many tokens; go/no-go logic undefined; no tests |

## Where this suite is different (honest claim)
1. **Portfolio prioritization with capacity**: ranks several ideas against stated hours and a work-in-progress limit. In the pages I read, the validators score one idea at a time (the larger collections contain many skills, but their validation skill is single-idea).
2. **Evidence-adjusted scoring** (E0–E4), plus sensitivity and order-bias checks. In one eval an idea with deposits (E3) outranked an assumption-only idea; whether this changes ranks in practice is not measured. Closest rival feature: the validator's evidence hierarchy.
3. **Evaluate → plan → red-team as separate, independent, small skills** with a shared Idea Card; red team ignores prior scores.
4. **Small instruction files** (SKILL.md about 700–1,000 words, references on demand; no mandatory web research). Token use was not measured against the other tools.
5. **Neutral and portable** (no fixed budget/locale; ChatGPT instructions per skill; any goal type incl. non-profit, research, inventions).
6. **ADHD-oriented output design** (a hypothesis, untested with users).

## Where others are stronger (and what v3.1 does about it)
| Gap in this suite | Seen in | Change in v3.1 |
|---|---|---|
| Additive score can average away a fatal weakness | EmanuelVogt, idea-validation-agents, validator hard gates | **Knockout floor:** Demand, Feasibility or Cost rated 1 caps priority at C and names the reason (`scoring.py`, Excel, tests) |
| One success bar for all ventures | validator capital paths | **Path** (bootstrap / venture / side-project / non-profit / research) sets the Upside bar (`methods.md`); a lifestyle business may be A as bootstrap and D as venture (eval 13: not yet demonstrated, see `evals/RESULTS.md`) |
| Claims and numbers not clearly tagged | EmanuelVogt | Light tags: user claims are hypotheses; numbers carry `fact (source)` / `assumption` / `unchecked` (evaluation); red team already did |
| Negative verdicts without a way forward | EmanuelVogt, validator salvage plan | Recycle/Stop must name **one escape route**; B ideas get a one-line "lift to A" |
| No memory across sessions | founder skills, idea-validation-agents | Optional **state file**: Idea Cards kept in `ideas.md` when files can be written and the user agrees (in `idea-card.md`) |
| Questions can create friction | EmanuelVogt ("don't ask me anything") | Explicit **no-questions mode**: if the user says assume, never ask, list assumptions |
| No market check at all | validator, startup-skill, founder skills | **Optional market check** for the top idea (3 competitors/substitutes with source) when search is available and the user wants it; never mandatory |
| MVP scoping vocabulary | pm-skills, founder skills (Must/Should/Won't) | MoSCoW-style cut list in `idea-to-plan/references/planning.md` |
| Evals only show wins | founder skills' honest "no difference" notes | `evals/RESULTS.md` now states where baselines were already good; new eval requires different verdict by path |

## Not adopted (on purpose)
Mandatory deep web research (cost, freshness risk), HTML/PDF dossiers, pitch/fundraising/GTM generation, dated market-data files that need upkeep. They fit a "validate one startup" product; this suite optimizes cheap decisions across many ideas.

## Still unknown
Whether this suite is *better* than any of the above on real ideas. A small head-to-head (3 cases, blind LLM judges) is in [COMPARISON.md](COMPARISON.md): no sign of superiority, and no better results from the baseline either beyond noise. A test with real ideas and human judges is still missing.
