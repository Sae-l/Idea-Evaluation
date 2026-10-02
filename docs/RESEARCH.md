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
| Base rates / outside view | Kahneman & Lovallo; BLS Business Employment Dynamics: about 78 % of new employer establishments survive year 1, about 51 % reach year 5 (BLS data through 2025, via secondary summaries) | high for the idea; quote numbers only with their source and country |
| Weights 25/20/15/15/15/10, thresholds A ≥ 3.4 / B ≥ 2.8 / C ≥ 2.2 | **author's choice, uncalibrated**; fragility checked with `scoring.py --sensitivity` | low until tested on real cases |
| Rate one criterion across all ideas; reverse-order re-read | LLM-as-judge literature: position bias and self-preference bias are documented (e.g. ACL/IJCNLP 2025 systematic study; "consistency–bias paradox": reproducible scores can still be biased) | medium (mitigation reduces, does not remove) |
| ADHD-friendly output: bottom line first, one small next action, time-boxes, external memory, parking list, short feedback loops | Executive-function model of ADHD (Barkley) and dual-pathway model with delay aversion (Sonuga-Barke) support externalizing working memory and short reward loops; practitioner sources on time-boxing and activation energy | **medium-low: derived from theory and practitioner advice; the skill itself has not been tested with ADHD users** |
| WIP limit of one or two active ideas | general work-in-progress principle; plausible for attention constraints | medium |

## Known limitations
- Scores come from an LLM's judgment of text the user supplies; they are structured opinions, not forecasts.
- No outcome data: the skill has not been checked against how ideas actually performed.
- ADHD benefit is a design hypothesis. Ask users with ADHD for feedback and adjust (length, wording, number of choices).
- Sources were read as web summaries, not always the primary books or papers.

## Next research steps
Collect real evaluation cases and outcomes to calibrate weights; test the output with ADHD users; read primary sources (Cooper 2008 *Perspective: Stage-Gate*, Bland & Osterwalder 2019, Savoia 2019, Fitzpatrick 2013).

## Sources
- Agent Skills format and VS Code/Copilot locations: agentskills.io; Visual Studio Magazine and Microsoft Learn skill guides
- Assumption mapping: Strategyzer library; Google Design Sprint Kit
- Pretotyping / XYZ hypothesis: albertosavoia.com materials, *The Right It*
- Stage-Gate decisions: Cooper (Wiley Encyclopedia of Management entry), secondary guides
- Effectuation: Sarasvathy 2001; systematic review of the affordable-loss principle (redalyc)
- ADHD: Barkley executive-function theory; Sonuga-Barke dual-pathway model (via Frontiers in Psychology and PMC articles); practitioner sources on task initiation and externalizing memory
- LLM judges: Systematic Study of Position Bias in LLM-as-a-Judge (ACL Anthology 2025); Measuring Self-Preference in LLM Judgments (arXiv 2506.02592); Reliability without Validity (arXiv)
- BLS Business Employment Dynamics survival data
