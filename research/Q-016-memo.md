# Q-016 memo: how the share of AI work, reliance and trust, and whether the work holds up are measured. Researcher, 2026-11-09

*The Researcher's memo for Q-016 on brief 201 (docs/briefs/201-researcher.md), 2026-11-09, recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p) from the helper's return; only this italic line is the Orchestrator's. Its B items stay unconfirmed until the Source checker has opened them (research/Q-016-source-check.md).*

**Answer, as far as the evidence goes.** Published share-of-work figures nearly all count code: characters (F016-1), lines (F016-4, F016-11), functions (F016-8), or a figure with no method given (F016-2, F016-3, F016-5). Of the figures for named organisations, only Anthropic's has had any outside check, and that was one informal estimate from public quotes and conversations with staff (F016-4). Every other figure comes from the company that sells the tool or set the target (F016-2, F016-3, F016-5, F016-6). Lines-based tools that tell a person's part from an agent's exist as a vendor draft format and a vendor tool. Neither has been tested for accuracy (F016-9, F016-10). For reliance, the measures found are acceptance rates, merge rates, auto-approve and interrupt rates, and an appropriate-reliance measure. The appropriate-reliance measure compares reliance with whether the advice was right, but it needs a baseline of unaided answers and was seen only in a search extract (F016-14 to F016-16, F016-18). The Input reader found no study that checks whether review or override rates of agent work match how often the agents are right (Input reader's gap list). Several single studies show that people's trust or felt productivity can differ from measured quality, in both directions (F016-19, F016-20, F016-22 search-only; library Q-009-F1-1, Q-009-F10-7). For whether code holds up, three preprints on survival and maintenance after merge disagree with each other (F016-23, F016-24, F016-25). Outside code, the measures are mainly benchmarks and one-off trials judged by expert graders, and the Input reader found no routine organisational measure of whether plans or analyses hold up later (F016-33 to F016-36; Input reader's gap list). On what collecting these measures costs, the record is nearly empty (Input reader's gap list). In my opinion, built on these sources, the measures a small organisation could take from its own records are those taken from review and merge logs, not self-report or a model's own classification. None of them has been shown to track what it stands for.

---

## 1. Share of work done by AI

**How it is counted**
- **Fact, B.** Google counts accepted AI-suggested characters divided by typed plus accepted characters. Pasted text is left out, and a suggestion counts only if it was shown for more than 750 ms. Google reported 50% of characters and a 37% acceptance rate. F016-1, https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/. *Stake: Google measures its own tools.*
- **Fact, B.** GitHub's Copilot metrics count lines suggested, added and deleted in the editor, and GitHub calls them "directional". Server telemetry cannot see what happens in the editor, some CLI figures may be inflated, and agent lines can be undercounted. The page does not say whether accepted code survives. F016-11, https://docs.github.com/en/copilot/concepts/copilot-usage-metrics/copilot-metrics. *Stake: GitHub sells Copilot.*
- **Fact, B.** Agent Trace (a draft RFC, v0.1.0) labels each range of code as human, ai, mixed or unknown. It does not judge quality and leaves storage open. F016-9, https://agent-trace.dev/. *Stake: led by Cursor, which sells an AI editor.*
- **Fact, B.** Git AI records attribution from the agents' own reports of the hunks they wrote ("no heuristics"). Known gaps are `git mv`, filter-branch and merges made in the web UI, and human edits between agent runs count as human. F016-10, https://usegitai.com/docs/cli/how-git-ai-works. *Stake: tool vendor.*
- **Fact, B.** An outside classifier study estimated that about 29% of US Python functions on GitHub are AI-written, with a 3.6% rise in quarterly output that goes mostly to experienced programmers. The sample sizes differ between versions of the paper. F016-8, https://arxiv.org/abs/2506.08945v2. *No stake seen.* It covers open-source Python only.
- **Fact, B.** Anthropic's own classifier (itself a Claude model) labels 77% of API transcripts as automation. Changing the classifier model moved the Claude.ai automation share from 49% to 45%, and no classifier accuracy is stated. F016-12, https://www.anthropic.com/research/anthropic-economic-index-september-2025-report. *Stake: model vendor classifying its own traffic with its own model.* The library already records that LLM judges favour their own generations (Q-002-F-h, weak C; Q-007-F07, strong A-sc, single-source) and that AI-text detectors flag text that was only polished by an LLM (Q-011-14, moderate B).
- **Fact, B (self-report).** Anthropic staff self-reported using Claude in about 60% of their work, with a 50% productivity boost. Most said they could "fully delegate" only 0–20%. The authors themselves flag convenience sampling and non-anonymous answers. F016-13, https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic. *Stake: vendor.*

**Published figures for named organisations**

| Org | Figure | What it counts | Reported by | Stake | Outside check |
|---|---|---|---|---|---|
| Google | >25% (Oct 2024) → 50% (fall 2025) → 75% (Apr 2026) | new code "generated by AI and then reviewed"; method not given; unclear whether it is the same metric as F016-1 | Pichai, via The Decoder (F016-2, B) | sells AI coding tools | none found. One outlet's ~30% for 2025 conflicts with the 50% (search-only) |
| Google | 50% of characters, 37% acceptance | the F016-1 character ratio | Google Research (F016-1, B) | own tools | none |
| Microsoft | 20–30% "written by software" | a spoken "I'd say" estimate; outlets disagree on whether it covers all code or new code | Nadella, via The Register (F016-3, B) | sells Copilot | none |
| Coinbase | ~40% of daily code, target >50% | method not given; "AI-assisted" and "AI-generated" used interchangeably | Armstrong on X, via The Block (F016-5, B) | CEO set a target, which is an incentive to raise the number | none. A later "95%+" is secondary and not opened |
| Anthropic | "90%" on "many teams, not uniformly" | merged lines, by implication | Amodei (F016-7, assumed, search-only) | sells Claude | see next row |
| Anthropic | 70–90% company-wide, ~90% for Claude Code's own code | not stated | spokesperson, via secondary press (F016-6, assumed, search-only) | sells Claude | — |
| Anthropic | ~50% of merged lines company-wide | outside estimate from public quotes and private talks with staff; not audited | Redwood Research (F016-4, B) | no stake seen | this is the only outside check found |

- **Opinion (the source's).** The Redwood author says the share "might depend a lot on what exactly you include", that lines are a weak proxy for work, and that the speed-up is likely "less than 2x" (F016-4).
- **Gap.** The Input reader found no method that divides "the work" by time or cost rather than by lines or characters. Neither of the attribution tools has been tested for accuracy (Input reader's gap list).
- **Disagreement.** The Google figures conflict between outlets (F016-2). For Anthropic, the vendor's 70–90% (search-only) differs from the outside ~50%.

## 2. Reliance and trust

- **Fact, B.** In GitHub's 2022 study, the acceptance rate of shown suggestions predicted how productive developers felt better than whether their completions persisted in the code. The outcome measured is perceived productivity, not output. F016-14, https://arxiv.org/abs/2205.06537. *Stake: GitHub.* A 27% acceptance figure is search-only.
- **Fact, B.** Agents' PRs were accepted less often than humans' although agents were faster. The abstract gives no percentages. F016-15, https://arxiv.org/abs/2507.15003. *No stake seen.* Merge figures of about 64% Codex, 49% Devin, 35% Copilot against 79% human are **assumed (search-only)**, and the subsets differ between papers.
- **Library facts on merges.**
  - Of 567 Claude Code PRs, 83.8% were merged, and 45.1% of the merged ones needed further changes (Q-009-F2-8, moderate B).
  - Maintainers would not merge about half of the test-passing SWE-bench Verified agent PRs, in a small sample (Q-009-F2-3, moderate B).
- **Fact, B.** Claude Code users fully auto-approve about 20% of sessions when new (<50 sessions) and over 40% at about 750 sessions. Interrupts rise from about 5% to about 9% of turns. The page says default settings and harder tasks may explain part of this, and it does not measure whether oversight matches correctness. F016-16, https://www.anthropic.com/research/measuring-agent-autonomy. *Stake: vendor telemetry on its own product.*
- **Fact, assumed (search-only).** An appropriate-reliance measure has two parts: relative self-reliance (correctly overriding wrong advice) and relative AI reliance (correctly following right advice). It needs unaided human answers as a baseline. F016-18, https://arxiv.org/abs/2204.06916. *Stake: the authors propose the measure.*
- **Over-trust (fact, B, single studies).**
  - People with an AI assistant wrote less secure code and were more likely to believe it was secure. F016-19, https://arxiv.org/abs/2211.03622. *No stake seen.*
  - Users missed misinformation in ChatGPT programming answers 39% of the time, while 52% of the answers contained incorrect information. The data are from the GPT-3.5 era. F016-20, https://arxiv.org/abs/2308.02312.
  - Experienced developers took 19% longer with AI while believing they were faster (Q-009-F1-1, Q-009-F10-7, moderate B, one study).
- **Different field (fact, B).** A systematic review of clinical decision support found that wrong advice raised the risk of a wrong decision (RR 1.26), and that clinicians overrode their own correct answers in 6% of cases. F016-17, https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751. The library already holds a drug-alert override rate of 49–96% (Q-005-LF-Q005-14, weak C).
- **Under-trust (fact, assumed, search-only, different field).** After seeing an algorithm err, people chose an inferior human forecaster over it. F016-22, https://repository.upenn.edu/fnce_papers/58.
- **Stated trust (fact, B, self-report).** In Stack Overflow's survey, 46% of developers distrust the accuracy of AI output and 33% trust it. 66% name "almost right, but not quite" as their top frustration. Trust was not checked against correctness. F016-21, https://survey.stackoverflow.co/2025/ai. *Stake: Stack Overflow competes with AI assistants.* DORA 2025 found 30% report little or no trust in AI code (Q-009-F2-6, moderate B; Google stake).
- **Gap.** The Input reader found no study that measures whether review or override rates of agent work match the agents' actual correctness (Input reader's gap list). The evidence that trust and correctness can diverge comes from other tasks (secure coding, Q&A, forecasting, medicine), not from supervision of agents.

## 3. Whether the work holds up

The three code studies below disagree with each other. They are preprints, and F016-24 and F016-25 were read as abstracts only.
- **Fact, B.** Agent-written code survived longer (hazard ratio 0.842 for modification), but the effect was small (Cramér's V 0.116) and differences between agents were larger than the agent–human gap. Corrective changes were slightly higher for agents (26.3% vs 23.0%), and prediction of when code would be modified was poor (macro F1 0.285). F016-23, https://arxiv.org/abs/2601.16809. *No stake seen.*
- **Fact, B.** In about 110,000 PRs, agent contributions were associated with more churn over time than human code. F016-24, https://arxiv.org/abs/2604.00917. *No stake seen.*
- **Fact, B.** Overall maintenance after merge was similar for agent and human code, but agent code needed more corrective fixes. Each 10-point rise in a project's no-review rate came with about 6% more agent maintenance burden. F016-25, https://arxiv.org/abs/2607.09902. *No stake seen.* The one-year window is search-only.
- **Fact, B.** DORA defines change fail rate, deployment rework rate (unplanned deployments caused by a production incident) and recovery time, and cites Goodhart's law as a warning against setting metrics as goals. Collection may be by survey or by system tools. F016-26, https://dora.dev/guides/dora-metrics/. *Stake: Google.* The library adds DORA's links between AI adoption and stability (Q-009-F1-9, Q-009-F2-6, Q-009-F5-7, moderate B, same publisher).
- **Library facts, code quality.**
  - Static-analysis warnings and code complexity rose after Cursor adoption and stayed up (Q-009-F2-7, B).
  - GitClear found refactoring-linked changed lines fell while cloned lines rose (Q-009-F12-8, B; vendor).
  - Veracode found security vulnerabilities in 45% of AI-generated code samples (Q-009-F2-4, B; vendor).
  - CodeRabbit found about 1.7x more issues in AI-co-authored PRs (Q-009-F2-5, C; vendor).
- **Non-code failures in use.**
  - Legal AI tools hallucinated 17–33% of the time in a preregistered test. F016-27, https://arxiv.org/abs/2405.20362, B. *No stake seen.*
  - A curated database counts 2,266 court decisions that address AI use or hallucinated material, as of 2026-11-05. F016-28, https://www.damiencharlotin.com/hallucinations/, B. It counts only failures a court addressed, so it is a lower bound that shows up late, and inclusion is partly the curator's judgment.
- **Gap.** The Input reader found little on how long after delivery defects appear, beyond the code studies' own observation windows.

## 4. Time saved or value, and how it relates to share

- **Fact, B.** Faros AI found that teams with high AI adoption completed 21% more tasks and merged 98% more PRs, but review time rose 91% and bugs per developer rose 9%. There was no significant correlation between AI adoption and improvement at company level. F016-29, https://www.faros.ai/blog/ai-productivity-paradox-report-2025. *Stake: sells engineering analytics.* A Faros FAQ page gives conflicting figures (search-only).
- **Estimate, B.** Anthropic estimates about 80% task speed-up from 100k conversations. Claude estimated how long the tasks take, and those estimates were checked against JIRA tasks. Time spent refining output outside the chat is not counted. F016-30, https://www.anthropic.com/research/estimating-productivity-gains. *Stake: vendor; the model grades its own work.*
- **Opinion, B.** DX frames AI measurement as utilization, impact and cost, warns that code-volume metrics are "particularly susceptible to gaming", and advises counting agent PRs in the throughput of the team that directs the agents. F016-31, https://getdx.com/ai-measurement-framework/. *Stake: sells developer analytics.*
- **Fact, B (self-report).** In Atlassian's survey, the share of developers reporting 10+ hours a week saved fell from 68% to 26% in a year, and 65% spend time correcting AI output. Atlassian notes these findings "reflect self-reported experience and perception, not system-level telemetry". F016-32, https://infoq.com/news/2026/10/atlassian-devex-2026. *Stake: Atlassian sells developer tools.* No fieldwork dates were published.
- **Library, trial results.**
  - Google RCT: about 21% faster task time with AI, wide confidence interval (Q-009-F4-7, B).
  - GitHub RCT: 55% faster on one HTTP-server task (Q-009-F3-8, B).
  - METR: 19% slower (Q-009-F1-1). METR's follow-up gave -18% (CI -38% to +9%), which METR calls only very weak evidence (Q-009-F1-2).
- **Fact, B (library).** Under an enterprise mandate to double AI use, load per reviewer doubled (Q-009-F10-6, weak C).
- **Gap.** The Input reader found no study that ties a share-of-work figure to measured time saved in the same organisation. The nearest is Anthropic's rough support from a 67% rise in merged PRs per engineer (F016-13, vendor).
- **Opinion (mine).** Taken together, F016-29 and F016-4 suggest that more output or a higher share of output need not mean more value at the level of the whole organisation. That rests on one vendor's telemetry and one informal estimate.

## 5. How measures are collected, and what that costs

- **Self-report:** F016-13, F016-21, F016-32, and the BetterUp "workslop" survey (unnumbered item; self-report, internally inconsistent figures, BetterUp sells coaching). The library shows a gap between perceived and measured time (Q-009-F10-7).
- **Logs and telemetry:** F016-1, F016-11, F016-16, F016-29. These have stated blind spots: editor versus server telemetry, inflated or undercounted figures (F016-11), and default settings (F016-16).
- **Model-run classification:** F016-12 and F016-30. Changing the classifier moved the share by 4 points (F016-12), and these classifications fall under the library's self-preference facts (Q-002-F-h, Q-007-F07).
- **Review of the work by people:** F016-23 to F016-25 (repository mining), and F016-33 to F016-35 (expert graders).
- **Cost.**
  - **Fact, B.** GDPval's authors do not consider their automated grader a full substitute for expert graders (F016-35).
  - **Fact, B.** The benchmark owner reports that a calibrated automated LLM judge "badly overshot" the newest models (F016-34). The size of the overshoot is the fetch tool's paraphrase. *Stake: benchmark owner.*
  - According to the Input reader, DORA warns that custom integrations may not be worth building. I did not find that in F016-26 as recorded.
  - **Gap.** No published cost figures were found for any of these collection methods.

## 6. Work other than code

- **Fact, B.** On the Remote Labor Index (freelance projects judged by humans against professionals' deliverables), the best agent's automation rate was 2.5% at launch. F016-33, https://arxiv.org/abs/2510.26787. *Stake: Scale AI co-authors and sells evaluation services.* The 240-project count is search-only.
- **Fact, B.** The same benchmark later reached 15.8% for Fable 5. F016-34, https://safe.ai/blog/significant-increase-in-digital-labor-automation. *Stake: benchmark owner.* Another outlet gives 16.1%.
- **Fact, B.** GDPval compares model deliverables with experts' work in 44 occupations, with graders blinded in reports. F016-35, https://www.transformernews.ai/p/openai-gdpval-ai-jobs-work. *Stake: OpenAI sells models.* The Opus 4.1 47.6% figure and the "100x faster/cheaper" claim are search-only, and a critic says the latter leaves out supervision and revision costs.
- **Fact, B (library).** Several library entries on AI summaries and citations for research work are relevant: Q-012-24, Q-012-25, Q-012-26 (weak C) and Q-012-22 (moderate B).
- **Gap.** The Input reader found no routine organisational measure of whether plans or analyses hold up later (Input reader's gap list). Benchmarks and one-off RCTs are what exists.

## 7. Comparison with the same work done without AI

- **Fact, B (secondary page).** In a BCG RCT with 758 consultants, those using GPT-4 on tasks inside the "frontier" did 12% more tasks, 25% faster, at about 40% higher quality. On a task outside the frontier they were 19 points less likely to be correct; that figure is uncertain as relayed, and the sub-arm figures are unsure. F016-36, https://www.library.hbs.edu/working-knowledge/humans-vs-machines-untangling-the-tasks-ai-can-and-cant-handle. *Stake: BCG co-authored.*
- **Fact, B (unnumbered).** In customer support at one firm, issues resolved per hour rose 14%, and 34% for novice workers (Brynjolfsson, Li, Raymond, NBER w31161). This is an observational rollout.
- **Fact, B (unnumbered, secondary).** In a writing experiment, professionals took 40% less time and peers judged quality 18% higher, but there was no fact-checking (Noy & Zhang via TechXplore).
- **Library.** The coding RCTs in §4 compare work with and without AI. The library also cautions that one study's effect may not transfer (Q-009-F6-4, Q-009-F6-5, Q-010 entries).

## How each measure can be gamed or misread, and how well it tracks

- **Characters or lines share.** It leaves out pasting and depends on the display threshold (F016-1). Telemetry has gaps (F016-11). DX warns that volume metrics are easy to game (F016-31). Lines are a weak proxy for work (F016-4, opinion). Nothing was found that tests whether this share tracks value.
- **Acceptance rate.** It tracks felt productivity better than whether the code persists (F016-14), and perceived speed can diverge from measured speed (Q-009-F10-7). Nothing was found that shows it tracks correctness.
- **Merge rate.** Merged code can still need further changes: 45.1% of merged Claude Code PRs did (Q-009-F2-8). Maintainers would not merge about half of test-passing SWE-bench agent PRs (Q-009-F2-3). The rate also counts only PRs that were opened, so dropped work is invisible; see the library's survivorship pattern, Q-006-P-q006-01 (weak C).
- **Auto-approve and interrupt rates.** They are confounded by default settings and task difficulty (F016-16). Nothing was found that links them to correctness.
- **Survival or churn after merge.** The three studies disagree (F016-23 to F016-25), and survival does not predict well when code will be modified (F016-23).
- **DORA rework or change-fail rates.** They invite gaming once set as goals (F016-26).
- **Self-report.** It diverges from measured time (Q-009-F10-7). Anthropic's own authors say to take their staff self-reports "with a grain of salt" (F016-13).
- **Classification by a model.** The share moved 4 points when the classifier changed (F016-12), and model judges show self-preference (Q-002-F-h).
- **Thin evidence.** The tracking evidence is single studies, often preprints read as abstracts. Much of the reliance evidence comes from other fields: medicine, forecasting, and pre-agent assistants.

## What each possible answer would change (as the question frames it; no choice made)

- **If a measure can be collected from the organisation's own records and is known to track what it stands for, it becomes a measure to use.** The candidates the evidence names that can come from an organisation's own records are review and merge outcomes, changes needed after merge, rework or change-fail counts, and override or interrupt counts (F016-15, F016-16, F016-25, F016-26; library Q-009-F2-8, and the pipeline's own return and first-pass counts in Q-006 and Q-008). None of them was found to be shown to track correctness or value (Input reader's gap list), so on this evidence none clearly meets the "known to track" condition.
- **If a measure is known to be easily gamed or misread, it is paired with a check or left out.**
  - Volume and share measures (F016-1, F016-11, F016-31), self-reported time (F016-32; Q-009-F10-7) and model-run classification (F016-12; Q-002-F-h) all have recorded ways to be gamed or misread.
  - The appropriate-reliance construct (F016-18, search-only) is the one recorded design that checks reliance against correctness. It needs unaided baseline answers.
  - **My opinion:** the library's own survivorship pattern (Q-006-P-q006-01) and its minimum-detectable-effect calculation (Q-013-14) bear on whether a small organisation's counts could show a change at all.
- **If a published share figure is used, it is used only with what it counts and its source's stake stated.** Every named figure but one comes from a party with a stake, and most have no published method (F016-2, F016-3, F016-5, F016-6). The one outside check is informal and puts Anthropic's company-wide figure at about 50% against claims of 70–90% (F016-4 vs F016-6, F016-7, both search-only).

## Proposed library entries (one line each: statement, type, grade, proposed shelf life)

1. Google counts AI's code share as accepted AI-suggested characters over typed plus accepted characters, leaving out pasted text, and reported 50% with a 37% acceptance rate (2024). Fact, B, vendor on its own tools; 12 months.
2. Pichai's figure for AI-generated new code at Google ("generated by AI and then reviewed") rose from over 25% (Oct 2024) to 75% (Apr 2026), with no method published and no outside check found. Fact, B, attributed, vendor stake; 6 months.
3. Nadella's 20–30% of Microsoft repo code "written by software" was a spoken estimate with no method. Fact, B, attributed, vendor stake; 12 months.
4. Coinbase's CEO said about 40% of daily code was AI-generated and set a target of over 50%; no method was published, and the target is an incentive. Fact, B, attributed; 6 months.
5. An outside informal estimate puts Anthropic's AI-written share of merged lines at about 50% company-wide, against a "90%" claim that holds on some teams. Estimate, B, single informal source, not audited; 6 months.
6. A classifier study estimates that about 29% of US Python functions on GitHub are AI-written. Fact, B, single study, open-source Python only; 12 months.
7. Agent Trace (draft RFC) labels code ranges human, ai, mixed or unknown, and Git AI records attribution from agents' self-reports with known gaps; neither has been tested for accuracy. Fact, B, vendor sources; 6 months.
8. GitHub calls its Copilot line metrics "directional" and lists telemetry blind spots and possible inflation. Fact, B, vendor; 6 months.
9. Changing the classifier model moved Anthropic's Claude.ai automation share from 49% to 45%, and no classifier accuracy is stated. Fact, B, vendor; 12 months.
10. Acceptance rate predicted Copilot users' perceived productivity better than whether their code persisted (GitHub, 2022). Fact, B, vendor study; 24 months.
11. Agents' PRs were accepted less often than humans' although agents were faster (Li, Zhang, Hassan). Fact, B, abstract, no figures; 12 months.
12. Claude Code users auto-approve about 20% of sessions when new and over 40% at about 750 sessions, while interrupts rise from about 5% to about 9% of turns; defaults may confound this. Fact, B, vendor telemetry; 6 months.
13. Users of an AI assistant wrote less secure code yet were more confident it was secure (Perry et al.). Fact, B, single study; 24 months.
14. Users overlooked misinformation in ChatGPT programming answers 39% of the time; 52% of the answers were wrong (GPT-3.5 era). Fact, B, single study; 24 months.
15. Incorrect clinical decision-support advice raised the risk of a wrong decision (RR 1.26); 6% of clinicians' correct decisions were overridden in favour of the wrong advice. Fact, B, systematic review, different field; 60 months.
16. Three preprints disagree on whether agent-written code holds up after merge (longer survival; more churn; similar overall maintenance but more corrective fixes, rising with the no-review rate). Fact, B, disagreement stated; 6 months.
17. Faros AI telemetry: high-adoption teams merged 98% more PRs, but review time rose 91%, with no company-level gain. Fact, B, vendor; 12 months.
18. Anthropic's 80% task speed-up estimate uses Claude to estimate task time and does not count time spent refining output outside the chat. Estimate, B, vendor; 12 months.
19. Atlassian's survey: developers reporting 10+ hours a week saved fell from 68% to 26% in a year (self-report). Fact, B, vendor survey via press; 12 months.
20. Remote Labor Index best automation rate: 2.5% at launch, 15.8% later; an automated LLM judge overestimated the newest models. Fact, B, benchmark owners with a stake; 6 months.
21. GDPval's authors say their automated grader does not fully replace expert graders. Fact, B, vendor via press; 12 months.
22. BCG RCT: inside the frontier, consultants with GPT-4 did 12% more tasks, 25% faster, at about 40% higher quality; on a task outside it they were less likely to be right (19 points, uncertain as relayed). Fact, B, secondary page; 36 months.
23. Legal AI research tools hallucinated 17–33% of the time in a preregistered test. Fact, B, single study; 24 months.
24. Pattern: report any AI share-of-work figure with its unit (characters, lines, functions or tasks), what it leaves out, who reported it and their stake, and whether it has been checked from outside. Pattern, opinion built on B sources (F016-1 to F016-7, F016-11); 24 months.
25. Pattern: pair any reliance rate (acceptance, merge, auto-approve) with a check of whether the work relied on was correct, because acceptance and felt productivity can diverge from persistence and quality. Pattern, opinion built on B sources (F016-14, F016-18 search-only, F016-19, F016-20; Q-009-F10-7); 24 months.

## Finding ids relied on, for the Source checker

F016-1 to F016-36, all of them. F016-6, F016-7, F016-18, F016-22 and F016-34's paraphrase are search-only. Also the three unnumbered non-code items: NBER w31161, TechXplore/Noy & Zhang, and BetterUp.

Library entries cited: Q-002-F-h, Q-005-LF-Q005-14, Q-006-P-q006-01, Q-007-F07, Q-009-F1-1, Q-009-F1-2, Q-009-F1-9, Q-009-F2-3, Q-009-F2-4, Q-009-F2-5, Q-009-F2-6, Q-009-F2-7, Q-009-F2-8, Q-009-F3-8, Q-009-F4-7, Q-009-F5-7, Q-009-F6-4, Q-009-F6-5, Q-009-F10-6, Q-009-F10-7, Q-009-F12-8, Q-011-14, Q-012-22, Q-012-24, Q-012-25, Q-012-26, Q-013-14. Q-006 and Q-008 are cited as the pipeline's own counts.

**Gaps (sources needed that were not gathered):**
- methods or audits behind the Google, Microsoft and Coinbase figures;
- any study testing whether review or override rates of agent work match the agents' correctness;
- the full texts of F016-23 to F016-25;
- the primary sources for F016-6, F016-7, F016-18 and F016-22;
- the SSRN paper behind F016-36;
- cost figures for collecting any of these measures;
- any routine organisational measure of whether non-code work holds up later.

**A discrepancy:** the Input reader's gap list says DORA warns that custom integrations may not be worth building, but F016-26 as recorded does not carry that claim. Re-check it before using it.

Total tokens: I cannot see them.
