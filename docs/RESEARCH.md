# Research notes and confidence

Maintainer document (not loaded by the skill). It records which design decisions rest on what, and how strong the support is. Last updated 2026-10-02.

| Design decision | Basis | Confidence |
|---|---|---|
| Gate on desirability / feasibility / viability | IDEO framework; used in Bland & Osterwalder, *Testing Business Ideas* | high (established practice) |
| Go / Kill / Hold / Recycle verdicts, must-meet knock-out criteria | Cooper, Stage-Gate (secondary summaries read, not the books) | medium-high |
| Riskiest-assumption-first, importance × evidence map | Bland/Osterwalder assumption mapping (Strategyzer, Google Design Sprint kit) | high |
| Tests as "At least X % of Y will Z" with skin in the game | Savoia, *The Right It* / pretotyping (secondary summaries) | medium-high |
| Evidence ladder opinion < behavior < commitment | Lean Startup, *The Mom Test*, Savoia | high for the ordering; **the numeric factors 0.80–1.00 are the author's choice** |
| Affordable loss, start from means | Sarasvathy, effectuation (systematic review of the affordable-loss principle exists) | medium |
| Pre-mortem | Klein (HBR 2007) | high |
| Base rates / outside view | Kahneman & Lovallo; BLS Business Employment Dynamics survival figures were read only via secondary summaries (unverified) and are no longer quoted in the skills | high for the idea; quote numbers only with their source and country |
| Estimates as ranges, outside view, buffers (default x1.5 known tasks, x2 first-time tasks) | Planning fallacy (Kahneman & Tversky 1979; Buehler, Griffin & Ross 1994: students finished theses on average 22 days later than predicted); reference-class forecasting (Lovallo & Kahneman 2003). The multipliers are **the author's defaults**; practitioner sources suggest ADHD adults sometimes need x2 to x3 | idea: high; multipliers: low until calibrated with the user's own actual times |
| Fixed time, variable scope; cancel by default instead of extending ("circuit breaker") | Shape Up (Basecamp): appetite, circuit breaker | medium (practitioner method, not controlled studies) |
| If-then start cues ("When X happens, I do Y") | Gollwitzer & Sheeran 2006 meta-analysis (Advances in Experimental Social Psychology 38; figures read via secondary summaries): 94 studies, d = .65 for goal attainment, d = .61 for getting started; only 3 clinical-population studies in that analysis | high in general populations, **low-medium for ADHD specifically** |
| Task chunking (15-60 min), time-boxed blocks, estimating generously | ADHD time-perception and time-estimation difficulties (reviews of time perception in adult ADHD; practitioner sources, one survey of ~1,860 adults reports estimation difficulty for about a third) | medium-low |
| Red team centered on a pre-mortem, not a lone devil's advocate | Mitchell, Russo & Pennington 1989 (prospective hindsight: reported ~30 % more reasons identified); pre-mortem reduced plan over-confidence more than comparison conditions (Veinott, Klein & Wiggins 2010, ISCRAM proceedings; via secondary summary); devil's advocacy evidence is mixed; red teams work only with independence and support | medium (the 30 % figure is quoted via secondary sources) |
| Weights 25/20/15/15/15/10, thresholds A ≥ 3.4 / B ≥ 2.8 / C ≥ 2.2 | **author's choice, uncalibrated**; fragility checked with `scoring.py --sensitivity` | low until tested on real cases |
| Rate one criterion across all ideas; reverse-order re-read | LLM-as-judge literature: position bias and self-preference bias are documented (e.g. ACL/IJCNLP 2025 systematic study; "consistency–bias paradox": reproducible scores can still be biased) | medium (mitigation reduces, does not remove) |
| ADHD-friendly output: bottom line first, one small next action, time-boxes, external memory, parking list, short feedback loops | Executive-function model of ADHD (Barkley) and dual-pathway model with delay aversion (Sonuga-Barke) support externalizing working memory and short reward loops; practitioner sources on time-boxing and activation energy | **medium-low: derived from theory and practitioner advice; the skill itself has not been tested with ADHD users** |
| WIP limit of one or two active ideas | general work-in-progress principle; plausible for attention constraints | medium |
| Knockout floor (Demand/Feasibility/Cost = 1 caps at C), path-specific Upside bar, escape routes | gaps found in the competitive analysis (`docs/COMPETITIVE-ANALYSIS.md`): fatal weaknesses must not be averaged away, success bars differ by capital path | medium (practice in comparable tools; the exact cap rule is the author's design) |

## Known limitations
- Scores come from an LLM's judgment of text the user supplies; they are structured opinions, not forecasts.
- No outcome data: the skill has not been checked against how ideas actually performed.
- ADHD benefit is a design hypothesis. Ask users with ADHD for feedback and adjust (length, wording, number of choices).
- Sources were read as web summaries, not always the primary books or papers.
- Planning/red-team skills: the multipliers, the 70 % usable load and the caps (max 3 findings, ≤3 starred tasks) are design defaults, not research results.

## Next research steps
Collect real evaluation cases and outcomes to calibrate weights; test the output with ADHD users; read primary sources (Cooper 2008 *Perspective: Stage-Gate*, Bland & Osterwalder 2019, Savoia 2019, Fitzpatrick 2013).

## Sources (accessed 2026-10-02; read mostly via secondary summaries)
- Agent Skills format and VS Code/Copilot locations: agentskills.io; Visual Studio Magazine and Microsoft Learn skill guides
- Assumption mapping: Strategyzer library; Google Design Sprint Kit
- Pretotyping / XYZ hypothesis: albertosavoia.com materials, *The Right It*
- Stage-Gate decisions: Cooper (Wiley Encyclopedia of Management entry), secondary guides
- Effectuation: Sarasvathy 2001; systematic review of the affordable-loss principle (redalyc)
- ADHD: Barkley executive-function theory; Sonuga-Barke dual-pathway model (via Frontiers in Psychology and PMC articles); practitioner sources on task initiation and externalizing memory
- LLM judges: Systematic Study of Position Bias in LLM-as-a-Judge (ACL Anthology 2025); Measuring Self-Preference in LLM Judgments (arXiv 2506.02592); Reliability without Validity (arXiv)
- BLS Business Employment Dynamics survival data
- Planning fallacy and reference-class forecasting: Buehler/Griffin/Ross; Lovallo & Kahneman; PMI article on reference class forecasting
- Implementation intentions: Gollwitzer & Sheeran 2006 and follow-up reviews (Taylor & Francis, Whiterose)
- Shape Up: basecamp.com/shapeup (Set Boundaries, The Betting Table, Glossary)
- Pre-mortem and devil's advocacy: Mitchell/Russo/Pennington 1989; Klein; AOM and ScienceDirect studies on devil's advocacy and dialectical inquiry
- ADHD time perception and task management: PMC review on time perception in adult ADHD; Guilford ADHD Hub; practitioner sources
