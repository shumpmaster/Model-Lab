# Q-016 memo: how the share of AI work, reliance and trust, and whether the work holds up are measured. Researcher, 2026-11-09 (revised after source check round 1)

*The Researcher's memo for Q-016, round 2 (brief 204, docs/briefs/204-researcher.md), revised after the Source checker's round 1 (research/Q-016-source-check.md); round 1 was brief 201, in this file's history. Recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p), 2026-11-09, from the helper's return; only this italic line is the Orchestrator's, replacing round 1's.*

**Answer, as far as the evidence goes.** Published share-of-work figures nearly all count code: characters (F016-1), lines (F016-4, F016-11), functions (F016-8), or a figure with no method given (F016-2, F016-3, F016-5). Of the figures for named organisations, only Anthropic's has had any outside check, and that was one informal estimate from public quotes and conversations with staff (F016-4). Every other figure comes from the company that sells the tool or set the target (F016-2, F016-3, F016-5, and Amodei's "70, 80, 90%" as quoted on Redwood's page). Lines-based tools that tell a person's part from an agent's exist as a draft format and a vendor tool. Neither has been tested for accuracy (F016-9, F016-10). For reliance, the measures found are acceptance rates, merge rates, auto-approve and interrupt rates, and an appropriate-reliance measure. The appropriate-reliance measure compares reliance with whether the advice was right, but it needs the person's own answer before the advice (or simulated answers from people without advice) and was defined for classification tasks only (F016-14 to F016-16, F016-18). The Input reader found no study that checks whether review or override rates of agent work match how often the agents are right (Input reader's gap list). Several single studies show people's trust or felt productivity running ahead of measured quality (F016-19, F016-20; library Q-009-F1-1, Q-009-F10-7). The one study found of the opposite direction, people trusting a better algorithm too little, could not be opened (F016-22). For whether code holds up, three preprints after merge measure different outcomes (survival, churn, and corrective maintenance), and their findings do not point the same way (F016-23, F016-24, F016-25). Outside code, the measures are mainly benchmarks, one of which uses blinded expert graders (F016-35), and one-off trials. The Input reader found no routine organisational measure of whether plans or analyses hold up later (F016-33 to F016-36; Input reader's gap list). On what collecting these measures costs, the record is nearly empty (Input reader's gap list; F016-26). In my opinion, built on these sources, the measures a small organisation could take from its own records are those taken from review and merge logs, not self-report or a model's own classification. None of them has been shown to track what it stands for.

---

## 1. Share of work done by AI

**How it is counted**
- **Fact, B.** Google counts accepted AI-suggested characters divided by typed plus accepted characters. Pasted text is left out, and a suggestion counts only if it was shown for more than 750 ms. Google reported 50% of characters and a 37% acceptance rate. F016-1, https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/. *Stake: Google measures its own tools.*
- **Fact, B.** GitHub's Copilot metrics count lines suggested, added and deleted in the editor, and GitHub calls them "directional". Server telemetry cannot see what happens in the editor, some CLI figures may be inflated, and agent lines can be undercounted. The page does not say whether accepted code survives. F016-11, https://docs.github.com/en/copilot/concepts/copilot-usage-metrics/copilot-metrics. *Stake: GitHub sells Copilot.*
- **Fact, B.** Agent Trace (a draft RFC, v0.1.0) labels each range of code as human, ai, mixed or unknown. It does not judge quality and leaves storage open. F016-9, https://agent-trace.dev/. *Stake: the page names no lead. That Cursor, which sells an AI editor, published it is reported only in search results and is not confirmed.*
- **Fact, B.** Git AI records attribution from the agents' own reports of the hunks they wrote ("no heuristics"). Known gaps are `git mv`, filter-branch and merges made in the web UI, and human edits between agent runs count as human. F016-10, https://usegitai.com/docs/cli/how-git-ai-works. *Stake: tool vendor.*
- **Fact, B.** An outside classifier study estimated that about 29% of US Python functions on GitHub are AI-written, with a 3.6% rise in quarterly output that goes mostly to experienced programmers. The sample sizes differ between versions of the paper. F016-8, https://arxiv.org/abs/2506.08945v2. *No stake seen.* It covers open-source Python only.
- **Fact, B.** Anthropic's own classifier (itself a Claude model) labels 77% of API transcripts as automation. Changing the classifier model moved the Claude.ai automation share from 49% to 45%, and no classifier accuracy is stated. F016-12, https://www.anthropic.com/research/anthropic-economic-index-september-2025-report. *Stake: model vendor classifying its own traffic with its own model.* The library already records that LLM judges favour their own generations (Q-002-F-h, weak C; Q-007-F07, strong A-sc, single-source), and that each of five AI-text detectors flagged some peer reviews that had only been polished by an LLM (Q-011-14, moderate B, peer reviews only).
- **Fact, B (self-report).** Anthropic staff self-reported using Claude in about 60% of their work, with a 50% productivity boost. Most said they could "fully delegate" only 0–20%. The authors themselves flag convenience sampling and non-anonymous answers. F016-13, https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic. *Stake: vendor.*

**Published figures for named organisations**

| Org | Figure | What it counts | Reported by | Stake | Outside check |
|---|---|---|---|---|---|
| Google | 25% (Oct 2024) → 50% (fall 2025) → 75% (Apr 2026) | new code "generated by AI and then reviewed"; method not given; unclear whether it is the same metric as F016-1 | Pichai, via The Decoder (F016-2, B) | sells AI coding tools | none found. One outlet's ~30% for 2025 conflicts with the 50% (search-only) |
| Google | 50% of characters, 37% acceptance | the F016-1 character ratio | Google Research (F016-1, B) | own tools | none |
| Microsoft | "maybe 20 to 30 percent" of the code in Microsoft's repos, "in some of our projects", written by software | a spoken estimate, limited to some projects; no method | Nadella, via The Register (F016-3, B) | sells Copilot | none |
| Coinbase | ~40% of daily code, target >50% | method not given | Armstrong on X, via The Block (F016-5, B) | CEO set a target, which is an incentive to raise the number | none. A later "95%+" is secondary and not opened |
| Anthropic | "90%" on "many teams, you know, not uniformly" | merged lines, by implication | Amodei, as quoted on Redwood's page (F016-7, B) | sells Claude | see Redwood row |
| Anthropic | "70, 80, 90%" (Sept 2025) | not stated | Amodei, as quoted on Redwood's page. The page first cited for this (F016-6) has no spokesperson and no 70–90% figure, so F016-6 as recorded is not confirmed | sells Claude | see Redwood row |
| Anthropic | ~50% of merged lines company-wide | outside estimate from public quotes and private talks with staff; not audited | Redwood Research (F016-4, B) | no stake seen | this is the only outside check found |

- **Opinion (the source's).** The Redwood author says the share "might depend a lot on what exactly you include", that lines are a weak proxy for work, and that the speed-up is likely "less than 2x" (F016-4).
- **Gap.** The Input reader found no method that divides "the work" by time or cost rather than by lines or characters. Neither of the attribution tools has been tested for accuracy (Input reader's gap list).
- **Disagreement.** The Google figures conflict between outlets (F016-2). For Anthropic, Amodei's "70, 80, 90%" and "90%" on many teams differ from the outside ~50%.

## 2. Reliance and trust

- **Fact, B.** In GitHub's 2022 study, the acceptance rate of shown suggestions, rather than whether completions persisted in the code, drove developers' perception of productivity. The outcome measured is perceived productivity, not output. F016-14, https://arxiv.org/abs/2205.06537. *Stake: GitHub.* A 27% acceptance figure is search-only.
- **Fact, B.** Agents' PRs were accepted less often than humans' although agents were faster. The abstract gives no percentages. F016-15, https://arxiv.org/abs/2507.15003. *No stake seen.* Merge figures of about 64% Codex, 49% Devin, 35% Copilot against 79% human are **assumed (search-only)**, and the subsets differ between papers.
- **Library facts on merges.**
  - Of 567 Claude Code PRs, 83.8% were merged, and 45.1% of the merged ones needed further changes (Q-009-F2-8, moderate B).
  - Maintainers would not merge about half of the test-passing SWE-bench Verified agent PRs, in a small sample (Q-009-F2-3, moderate B).
- **Fact, B.** Claude Code users fully auto-approve about 20% of sessions when new (<50 sessions) and over 40% at about 750 sessions. Interrupts rise from about 5% to about 9% of turns. The page says default settings and harder tasks may explain part of this, and it does not measure whether oversight matches correctness. F016-16, https://www.anthropic.com/research/measuring-agent-autonomy. *Stake: vendor telemetry on its own product.*
- **Fact, B.** An appropriate-reliance measure has two parts: relative positive self-reliance (correctly overriding wrong advice) and relative positive AI reliance (correctly following right advice). It needs the person's decision before the advice, or a simulated one from people without advice, as a baseline, and it is defined for classification tasks only. F016-18, https://arxiv.org/abs/2204.06916 (full text). *Stake: the authors propose the measure.*
- **Over-trust (fact, B, single studies).**
  - People with an AI assistant wrote less secure code and were more likely to believe it was secure. F016-19, https://arxiv.org/abs/2211.03622. *No stake seen.*
  - Users missed misinformation in ChatGPT programming answers 39% of the time, while 52% of the answers contained incorrect information. The data are from the GPT-3.5 era. F016-20, https://arxiv.org/abs/2308.02312.
  - Experienced developers took 19% longer with AI while believing they were faster (Q-009-F1-1, Q-009-F10-7, moderate B, one study). METR's page now says these results "no longer reflect the current impact of AI models" (Q-009-F1-1).
- **Different field (fact, B).** A systematic review of clinical decision support found that wrong advice raised the risk of a wrong decision (RR 1.26). Its introduction cites an earlier study (Friedman et al.) in which clinicians overrode their own correct answers in 6% of cases; that figure is not the review's own finding. F016-17, https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751. The library already holds a drug-alert override rate of 49–96% (Q-005-LF-Q005-14, weak C).
- **Under-trust (fact, assumed, different field; the page could not be opened, it returned 403).** After seeing an algorithm err, people chose an inferior human forecaster over it. F016-22, https://repository.upenn.edu/fnce_papers/58.
- **Stated trust (fact, B, self-report).** In Stack Overflow's survey, 46% of developers distrust the accuracy of AI output and 33% trust it. 66% name "almost right, but not quite" as their top frustration. Trust was not checked against correctness. F016-21, https://survey.stackoverflow.co/2025/ai. *Stake: Stack Overflow competes with AI assistants.* DORA 2025 found 30% report little or no trust in AI code (Q-009-F2-6, moderate B; Google stake).
- **Gap.** The Input reader found no study that measures whether review or override rates of agent work match the agents' actual correctness (Input reader's gap list). The evidence that trust and correctness can diverge comes from other tasks (secure coding, Q&A, medicine, and forecasting, the last resting on F016-22, which could not be opened), not from supervision of agents.

## 3. Whether the work holds up

The three code studies below measure different outcomes (survival, churn and corrective maintenance), and their findings do not point the same way, so they cannot be set directly against each other. They are preprints, and F016-24 and F016-25 were read as abstracts only.
- **Fact, B.** Agent-written code survived longer (hazard ratio 0.842 for modification), but the effect was small (Cramér's V 0.116) and differences between agents were larger than the agent–human gap. Corrective changes were slightly higher for agents (26.3% vs 23.0%), and prediction of when code would be modified was poor (macro F1 0.285). F016-23, https://arxiv.org/abs/2601.16809. *No stake seen.*
- **Fact, B.** In about 110,000 PRs, agent contributions were associated with more churn over time than human code. F016-24, https://arxiv.org/abs/2604.00917. *No stake seen.*
- **Fact, B.** Overall maintenance after merge was similar for agent and human code, but agent code needed more corrective fixes. Each 10-point rise in a project's no-review rate came with about 6% more agent maintenance burden. F016-25, https://arxiv.org/abs/2607.09902. *No stake seen.* The one-year window is search-only.
- **Fact, B.** DORA defines change fail rate, deployment rework rate (unplanned deployments caused by a production incident) and recovery time, and cites Goodhart's law as a warning against setting metrics as goals. It names the Quick Check, retrospectives and tools as ways to collect the measures. F016-26, https://dora.dev/guides/dora-metrics/. *Stake: Google.* The library adds DORA's links between AI adoption and stability (Q-009-F1-9, Q-009-F2-6, moderate B) and its AI-throughput link turning from negative in 2024 to positive in 2025 (Q-009-F5-7, moderate B), all from the same publisher.
- **Library facts, code quality.**
  - Static-analysis warnings and code complexity rose after Cursor adoption and stayed up (Q-009-F2-7, B).
  - GitClear found refactoring-linked changed lines fell while cloned lines rose (Q-009-F12-8, B; vendor).
  - Veracode found security vulnerabilities in 45% of cases of AI-generated code (Q-009-F2-4, B; vendor).
  - CodeRabbit found about 1.7x more issues in AI-co-authored PRs (Q-009-F2-5, C; vendor).
- **Non-code failures in use.**
  - Legal AI tools hallucinated 17–33% of the time in a preregistered test. F016-27, https://arxiv.org/abs/2405.20362, B. *No stake seen.*
  - A curated database counts 2,266 court decisions that address AI use or hallucinated material, as of 2026-11-05, including some where AI use was only alleged. Inclusion is partly the curator's judgment. F016-28, https://www.damiencharlotin.com/hallucinations/, B.
- **Gap.** The Input reader found little on how long after delivery defects appear, beyond the code studies' own observation windows.

## 4. Time saved or value, and how it relates to share

- **Fact, B.** Faros AI found that teams with high AI adoption completed 21% more tasks and merged 98% more PRs, but review time rose 91% and bugs per developer rose 9%. There was no significant correlation between AI adoption and improvement at company level. F016-29, https://www.faros.ai/blog/ai-productivity-paradox-report-2025. *Stake: sells engineering analytics.* A Faros FAQ page gives conflicting figures (search-only).
- **Estimate, B.** Anthropic estimates about 80% task speed-up from 100k conversations. Claude estimated how long the tasks take, and those estimates were checked against JIRA tasks. Time spent refining output outside the chat is not counted. F016-30, https://www.anthropic.com/research/estimating-productivity-gains. *Stake: vendor; the model grades its own work.*
- **Opinion, B.** DX frames AI measurement as utilization, impact and cost, warns that code-volume metrics are "particularly susceptible to gaming", and advises counting agent PRs in the throughput of the team that directs the agents. F016-31, https://getdx.com/ai-measurement-framework/. *Stake: sells developer analytics.*
- **Fact, B (self-report).** In Atlassian's survey, the share of developers reporting 10+ hours a week saved fell from 68% to 26% in a year, and 65% spend time correcting AI output. Atlassian notes these findings "reflect self-reported experience and perception, not system-level telemetry". F016-32, https://infoq.com/news/2026/10/atlassian-devex-2026. *Stake: Atlassian sells developer tools.* No fieldwork dates were published.
- **Library, trial results.**
  - Google RCT: about 21% faster task time with AI, wide confidence interval (Q-009-F4-7, B).
  - GitHub RCT: 55% faster on one HTTP-server task (Q-009-F3-8, B).
  - METR: 19% slower (Q-009-F1-1); METR's page now says these results no longer reflect the current impact of AI models. METR's follow-up gave -18% (CI -38% to +9%), which METR calls only very weak evidence (Q-009-F1-2).
- **Fact, weak C (library).** Under an enterprise mandate to double AI use, load per reviewer doubled (Q-009-F10-6, weak C).
- **Gap.** The Input reader found no study that ties a share-of-work figure to measured time saved in the same organisation. The nearest is Anthropic's rough support from a 67% rise in merged PRs per engineer (F016-13, vendor).
- **Opinion (mine).** Taken together, F016-29 and F016-4 suggest that more output or a higher share of output need not mean more value at the level of the whole organisation. That rests on one vendor's telemetry and one informal estimate.

## 5. How measures are collected, and what that costs

- **Self-report:** F016-13, F016-21, F016-32, and the BetterUp "workslop" survey (unnumbered item; self-report, internally inconsistent figures, BetterUp sells coaching). The library shows a gap between perceived and measured time (Q-009-F10-7).
- **Logs and telemetry:** F016-1, F016-11, F016-16, F016-29. These have stated blind spots: editor versus server telemetry, inflated or undercounted figures (F016-11), and default settings (F016-16).
- **Model-run classification:** F016-12 and F016-30. Changing the classifier moved the share by 4 points (F016-12), and these classifications fall under the library's self-preference facts (Q-002-F-h, Q-007-F07).
- **Review of the work by people:** F016-23 to F016-25 (repository mining), and F016-35 (blinded expert graders).
- **Cost.**
  - **Fact, B.** GDPval's authors do not consider their automated grader a full substitute for expert graders (F016-35).
  - **Fact, B.** The benchmark owner reports that a calibrated automated LLM judge "badly overshot" the newest models, and the post states the size of the overshoot (F016-34). *Stake: benchmark owner.*
  - **Fact, B.** DORA says custom integrations for collecting its measures "might not be worth the initial investment" (F016-26). It gives no cost figure.
  - **Gap.** No published cost figures were found for any of these collection methods.

## 6. Work other than code

- **Fact, B (abstract).** On the Remote Labor Index, the best agent's automation rate was 2.5% at launch. F016-33, https://arxiv.org/abs/2510.26787. The abstract does not give the number of projects or say how deliverables were judged. *Stake: the benchmark owner's post (F016-34) says the benchmark was developed with Scale Labs, which sells evaluation services.*
- **Fact, B.** The same benchmark later reached 15.8% for Fable 5. F016-34, https://safe.ai/blog/significant-increase-in-digital-labor-automation. *Stake: benchmark owner.* Another outlet gives 16.1% (not opened).
- **Fact, B.** GDPval compares model deliverables with experts' work in 44 occupations, with graders blinded in reports. F016-35, https://www.transformernews.ai/p/openai-gdpval-ai-jobs-work. *Stake: OpenAI sells models.* The Opus 4.1 47.6% figure and the "100x faster/cheaper" claim are not in the article opened; they come from search extracts only.
- **Fact, B and weak C (library).** Several library entries on AI summaries, citations and search for research work are relevant: Q-012-24, Q-012-25, Q-012-26 on summaries and citations (weak C), and Q-012-22 on Elicit's search sensitivity (moderate B).
- **Gap.** The Input reader found no routine organisational measure of whether plans or analyses hold up later (Input reader's gap list). Benchmarks and one-off RCTs are what exists.

## 7. Comparison with the same work done without AI

- **Fact, B (secondary page).** In a BCG RCT with 758 consultants, those using GPT-4 did "12 percent more work at a 25 percent faster clip" on one set of tasks (shoe-design tasks). Quality was about 40% higher on "certain kinds of tasks"; the page does not tie that figure to the tasks inside the frontier. On "more complex tasks" they were 19 points less likely to be correct, and for the task outside the frontier the page gives drops of 24 and 13 points. F016-36, https://www.library.hbs.edu/working-knowledge/humans-vs-machines-untangling-the-tasks-ai-can-and-cant-handle. *Stake: BCG co-authored.*
- **Fact, B (unnumbered).** In customer support, issues resolved per hour rose 14%, and 34% for novice workers (Brynjolfsson, Li, Raymond, NBER w31161; 5,179 agents). This is an observational rollout.
- **Fact, B (unnumbered, secondary).** In a writing experiment, professionals took 40% less time and peers judged quality 18% higher, but there was no fact-checking (Noy & Zhang via TechXplore).
- **Library.** The coding RCTs in §4 compare work with and without AI. The library also cautions that one study's effect may not transfer (Q-009-F6-4, Q-009-F6-5, Q-010 entries).

## How each measure can be gamed or misread, and how well it tracks

- **Characters or lines share.** It leaves out pasting and depends on the display threshold (F016-1). Telemetry has gaps (F016-11). DX warns that volume metrics are easy to game (F016-31). Lines are a weak proxy for work (F016-4, opinion). Nothing was found that tests whether this share tracks value.
- **Acceptance rate.** Acceptance, rather than whether the code persists, drove felt productivity (F016-14), and perceived speed can diverge from measured speed (Q-009-F10-7). Nothing was found that shows it tracks correctness.
- **Merge rate.** Merged code can still need further changes: 45.1% of merged Claude Code PRs did (Q-009-F2-8). Maintainers would not merge about half of test-passing SWE-bench agent PRs (Q-009-F2-3). The rate also counts only PRs that were opened, so dropped work is invisible; see the library's survivorship pattern, Q-006-P-q006-01 (weak C).
- **Auto-approve and interrupt rates.** They are confounded by default settings and task difficulty (F016-16). Nothing was found that links them to correctness.
- **Survival or churn after merge.** The three studies measure different outcomes and do not point the same way (F016-23 to F016-25), and survival analysis predicts poorly when code will be modified (F016-23).
- **DORA rework or change-fail rates.** They invite gaming once set as goals (F016-26).
- **Self-report.** It diverges from measured time (Q-009-F10-7). Anthropic's own authors say to take their staff self-reports "with a grain of salt" (F016-13).
- **Classification by a model.** The share moved 4 points when the classifier changed (F016-12), and model judges show self-preference (Q-002-F-h).
- **Thin evidence.** The tracking evidence is single studies, often preprints read as abstracts. Much of the reliance evidence comes from other fields: medicine, forecasting (F016-22, not opened), and pre-agent assistants.

## What each possible answer would change (as the question frames it; no choice made)

- **If a measure can be collected from the organisation's own records and is known to track what it stands for, it becomes a measure to use.** The candidates the evidence names that can come from an organisation's own records are review and merge outcomes, changes needed after merge, rework or change-fail counts, and override or interrupt counts (F016-15, F016-16, F016-25, F016-26; library Q-009-F2-8, and the pipeline's own return and first-pass counts in Q-006 and Q-008). None of them was found to be shown to track correctness or value (Input reader's gap list), so on this evidence none clearly meets the "known to track" condition.
- **If a measure is known to be easily gamed or misread, it is paired with a check or left out.**
  - Volume and share measures (F016-1, F016-11, F016-31), self-reported time (F016-32; Q-009-F10-7) and model-run classification (F016-12; Q-002-F-h) all have recorded ways to be gamed or misread.
  - The appropriate-reliance construct (F016-18) is the one recorded design that checks reliance against correctness. It needs each person's answer before the advice (or simulated unaided answers), and it was defined for classification tasks only.
  - **My opinion:** the library's own survivorship pattern (Q-006-P-q006-01) and its minimum-detectable-effect calculation (Q-013-14) bear on whether a small organisation's counts could show a change at all.
- **If a published share figure is used, it is used only with what it counts and its source's stake stated.** Every named figure but one comes from a party with a stake, and most have no published method (F016-2, F016-3, F016-5, and Amodei's figures). The one outside check is informal and puts Anthropic's company-wide figure at about 50% against Amodei's "70, 80, 90%" and "90%" on many teams, not uniformly (F016-4, which quotes both; F016-7).

## Proposed library entries (one line each: statement, type, grade, proposed shelf life)

1. Google counts AI's code share as accepted AI-suggested characters over typed plus accepted characters, leaving out pasted text, and reported 50% with a 37% acceptance rate (2024). Fact, B, vendor on its own tools; 12 months.
2. Pichai's figure for AI-generated new code at Google ("generated by AI and then reviewed") rose from 25% (Oct 2024) to 50% (fall 2025) and 75% (Apr 2026), with no method published and no outside check found. Fact, B, attributed, vendor stake; 6 months.
3. Nadella said "maybe 20 to 30 percent" of the code in Microsoft's repos, "in some of our projects", was written by software; a spoken estimate with no method. Fact, B, attributed, vendor stake; 12 months.
4. Coinbase's CEO said about 40% of daily code was AI-generated and set a target of over 50%; no method was published, and the target is an incentive. Fact, B, attributed; 6 months.
5. An outside informal estimate puts Anthropic's AI-written share of merged lines at about 50% company-wide, against Amodei's "90%", which he said held on many teams, not uniformly. Estimate, B, single informal source, not audited; 6 months.
6. A classifier study estimates that about 29% of US Python functions on GitHub are AI-written. Fact, B, single study, open-source Python only; 12 months.
7. Agent Trace (draft RFC) labels code ranges human, ai, mixed or unknown, and Git AI records attribution from agents' self-reports with known gaps; neither has been tested for accuracy. Fact, B; Git AI is a vendor source, and Agent Trace's page names no lead; 6 months.
8. GitHub calls its Copilot line metrics "directional" and lists telemetry blind spots and possible inflation. Fact, B, vendor; 6 months.
9. Changing the classifier model moved Anthropic's Claude.ai automation share from 49% to 45%, and no classifier accuracy is stated. Fact, B, vendor; 12 months.
10. Acceptance rate, rather than whether code persisted, drove Copilot users' perceived productivity (GitHub, 2022). Fact, B, vendor study; 24 months.
11. Agents' PRs were accepted less often than humans' although agents were faster (Li, Zhang, Hassan). Fact, B, abstract, no figures; 12 months.
12. Claude Code users auto-approve about 20% of sessions when new and over 40% at about 750 sessions, while interrupts rise from about 5% to about 9% of turns; defaults may confound this. Fact, B, vendor telemetry; 6 months.
13. Users of an AI assistant wrote less secure code yet were more confident it was secure (Perry et al.). Fact, B, single study; 24 months.
14. Users overlooked misinformation in ChatGPT programming answers 39% of the time; 52% of the answers were wrong (GPT-3.5 era). Fact, B, single study; 24 months.
15. Incorrect clinical decision-support advice raised the risk of a wrong decision (RR 1.26, systematic review); the review's introduction cites Friedman et al. for clinicians overriding their own correct decisions in 6% of cases. Fact, B, systematic review, different field; 60 months.
16. Three preprints on agent-written code after merge measure different outcomes and do not point the same way (longer survival; more churn; similar overall maintenance but more corrective fixes, rising with the no-review rate). Fact, B, abstracts or single preprints; 6 months.
17. Faros AI telemetry: high-adoption teams merged 98% more PRs, but review time rose 91%, with no company-level gain. Fact, B, vendor; 12 months.
18. Anthropic's 80% task speed-up estimate uses Claude to estimate task time and does not count time spent refining output outside the chat. Estimate, B, vendor; 12 months.
19. Atlassian's survey: developers reporting 10+ hours a week saved fell from 68% to 26% in a year (self-report). Fact, B, vendor survey via press; 12 months.
20. Remote Labor Index best automation rate: 2.5% at launch, 15.8% later; an automated LLM judge "badly overshot" the newest models. Fact, B, benchmark owners with a stake; 6 months.
21. GDPval's authors say their automated grader does not fully replace expert graders. Fact, B, vendor via press; 12 months.
22. BCG RCT (758 consultants): with GPT-4, consultants did 12% more work 25% faster on one set of tasks and had about 40% higher quality on certain kinds of tasks, but were less likely to be correct on more complex tasks (19 points) and on the task outside the frontier (24 and 13 points). Fact, B, secondary page; 36 months.
23. Legal AI research tools hallucinated 17–33% of the time in a preregistered test. Fact, B, single study; 24 months.
24. Pattern: report any AI share-of-work figure with its unit (characters, lines, functions or tasks), what it leaves out, who reported it and their stake, and whether it has been checked from outside. Pattern, opinion built on B sources (F016-1 to F016-5, F016-7, F016-11); 24 months.
25. Pattern: pair any reliance rate (acceptance, merge, auto-approve) with a check of whether the work relied on was correct, because acceptance, rather than persistence, drove felt productivity, and confidence ran ahead of quality in single studies. Pattern, opinion built on B sources (F016-14, F016-18, F016-19, F016-20; Q-009-F10-7); 24 months.

## Finding ids relied on, for the Source checker

F016-1 to F016-36. After round 1 of the source check:
- **Could not be opened:** F016-22 (the page returned 403). It is marked assumed.
- **Not confirmed as recorded:** F016-6. The memo now uses only the Amodei "70, 80, 90%" quote on Redwood's page (F016-4's source), and drops the spokesperson and the ~90% for Claude Code.
- **No longer search-only:** F016-7 (the quote is on Redwood's page), F016-18 (full text opened), F016-34 (opened, so the paraphrase caution is dropped).
- **Search-only sub-claims still marked so:** the ~30% Google outlet (F016-2), "95%+" (F016-5), 27% (F016-14), the 64/49/35/79 merge figures (F016-15), the one-year window (F016-25), the Faros FAQ (F016-29), 16.1% (F016-34), 47.6% and "100x" (F016-35).
- **Reconciling with the Input reader's count (F016-6, 7, 34 search-only):** the Input reader's own gap list also called F016-18 and F016-22 search-only, which is where my earlier list came from. On the check's findings, only F016-22 stays unopened, and F016-6 stays unconfirmed.

Also the three unnumbered non-code items: NBER w31161, TechXplore/Noy & Zhang, and BetterUp.

Library entries cited: Q-002-F-h, Q-005-LF-Q005-14, Q-006-P-q006-01, Q-007-F07, Q-009-F1-1, Q-009-F1-2, Q-009-F1-9, Q-009-F2-3, Q-009-F2-4, Q-009-F2-5, Q-009-F2-6, Q-009-F2-7, Q-009-F2-8, Q-009-F3-8, Q-009-F4-7, Q-009-F5-7, Q-009-F6-4, Q-009-F6-5, Q-009-F10-6, Q-009-F10-7, Q-009-F12-8, Q-011-14, Q-012-22, Q-012-24, Q-012-25, Q-012-26, Q-013-14. Q-006 and Q-008 are cited as the pipeline's own counts.

**Gaps (sources needed that were not gathered):**
- methods or audits behind the Google, Microsoft and Coinbase figures;
- any study testing whether review or override rates of agent work match the agents' correctness;
- the full texts of F016-23 to F016-25, and of F016-33 (project count and how deliverables were judged);
- a primary source for Anthropic's company-wide figures (F016-6 as recorded not found), and an openable copy of F016-22;
- the SSRN paper behind F016-36;
- cost figures for collecting any of these measures;
- any routine organisational measure of whether non-code work holds up later.

Total tokens: I cannot see them.

---

## Change list (item — what changed — correction answered)

1. §2 clinical decision support; entry 15 — 6% override now credited to Friedman et al., cited in the review's introduction, and not called the review's finding — #1.
2. §1 table, Coinbase row — "AI-assisted/AI-generated used interchangeably" deleted — #2.
3. §1 table, Microsoft row; entry 3 — added "in some of our projects" and used the page's "maybe 20 to 30 percent"; took the quotation marks off written by software; dropped "outlets disagree" because it could not be sourced. Also dropped the "I'd say" quote in favour of the page's wording — #3.
4. §1 table, Google row; entry 2 — ">25%" changed to "25%"; added the 50% for fall 2025 that the page gives — #4.
5. §1 table, Anthropic 70–90% row; the Disagreement line; opening answer; "what each answer would change" (third bullet) — the spokesperson and the ~90% for Claude Code are gone, replaced by Amodei's "70, 80, 90%" from Redwood's page. F016-6 as recorded is marked not confirmed — #5.
6. F016-7 (table row) and F016-18 (§2, opening answer, "what would change", entry 25) — dropped "search-only" and raised F016-18 from assumed to B. F016-18 is now worded to the full text: "relative positive" reliance measures, a baseline from the person's pre-advice decision or simulated unaided answers, and classification tasks only. The opening answer's "seen only in a search extract" now gives the classification-only limit instead — #6.
7. §3 DORA; §5 cost; end discrepancy note — "survey" changed to Quick Check, retrospectives and tools. The custom-integrations quote is now a B fact under Cost, and both discrepancy notes are deleted. The opening answer's cost sentence now also cites F016-26 — #7.
8. §3 F016-28 — added "including some where AI use was only alleged"; deleted "counts only failures a court addressed", "lower bound" and "shows up late" — #8.
9. §6 F016-33; §5 "review by people"; opening answer — removed the 240 count and "judged by humans against professionals' deliverables". The Scale stake now rests on the CAIS post (F016-34). F016-33 and F016-34 are out of the expert-grader list, so the opening answer now names only GDPval as using expert graders — #9.
10. §6 F016-35 — the critic is removed; 47.6% and "100x" are marked as not in the article (search extracts only) — #10.
11. §7 F016-36; entry 22 — reworded: 12%/25% on one set of tasks (shoe design), 40% on "certain kinds of tasks" and not tied to inside the frontier, 19 points on "more complex tasks", and 24 and 13 points on the outside-frontier task — #11.
12. §1 F016-9; entry 7 — "led by Cursor" replaced with: the page names no lead, and Cursor's role is reported only in search results — #12.
13. §2 F016-14; gaming section; entries 10 and 25 — "predicted ... better than" changed to "acceptance, rather than persistence, drove perceived productivity" — #13.
14. Library citations — Q-009-F5-7 is now described as the throughput link turning positive, split from the stability entries; Q-012-22 is Elicit search sensitivity; the Q-009-F10-6 label is now "Fact, weak C"; the METR caveat that the results "no longer reflect the current impact of AI models" is added in §2 and §4; Q-011-14 is limited to peer reviews and five detectors; Q-009-F2-4 now says "cases" — #14.
15. Opening answer; §3 intro; gaming section "survival or churn"; entry 16 — "disagree" changed to "measure different outcomes (survival, churn, corrective maintenance) and do not point the same way". The opening answer's "in both directions" is replaced by over-trust evidence only, plus a note that the under-trust study (F016-22) could not be opened. F016-22 in §2 is marked as not opened (403), and forecasting is flagged in the §2 gap and in "thin evidence" — #15.
16. The "Finding ids relied on" section — the search-only list is reconciled with the Input reader's count and the check's findings. The F016-34 "paraphrase" caution is dropped in §5 because the post states the overshoot sizes; I did not add the sizes myself — #16.
17. Entry 24 — the source range now reads F016-1 to F016-5, F016-7, F016-11, leaving out F016-6, which is not confirmed — follows from #5.
18. §7 NBER — dropped "at one firm", which is not on the page, and added the 5,179 agents the check confirmed — the check's findings table (it names this item).
19. Gaps list — updated for F016-6, F016-7, F016-18, F016-22 and F016-33 — follows from #5, #6, #9 and #15.

Not changed: the proposed grades stay B. The Source checker filed several of these at weak (C) (Q-016-2, 3, 4, 5, 16, 19, 21, 22 and both patterns). I left my proposals as they were rather than restate the checker's grades as my own.

## Finding ids for the Source checker to re-check

F016-2, F016-3, F016-5, F016-6 (now only the Amodei quote on Redwood's page), F016-7, F016-9, F016-14, F016-17, F016-18, F016-22 (status only), F016-26, F016-28, F016-33, F016-34, F016-35, F016-36, NBER w31161; library citations Q-009-F1-1, Q-009-F2-4, Q-009-F5-7, Q-009-F10-6, Q-011-14, Q-012-22; and the reworded proposed entries 2, 3, 5, 7, 10, 15, 16, 22, 24, 25.

Total tokens: I cannot see them.
