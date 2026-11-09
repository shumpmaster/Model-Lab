# Q-012 memo, 2026-11-09: how fast findings about practice lose validity, and how organisations keep their practice up to date

*The Researcher's memo for Q-012, round 4, the focused confirmation round the owner ruled (decisions/questions/P-002-research-stop.md; brief 185, docs/briefs/185-researcher.md), revised after the Source checker's round 3 (research/Q-012-source-check.md); rounds 1 to 3 (briefs before 185) are in this file's history. Recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p), 2026-11-09, from the helper's return; only this italic line is the Orchestrator's, in the place the Researcher left for it.*

**Answer in brief.** Every sentence here names the finding ids or library entries it rests on, and is marked as fact, estimate or opinion.

- **Opinion, from indirect evidence only:** findings tied to particular AI models or prompts can lose validity when the models change (F012-3, F012-4; library Q-009-F5-3). No study found measures how fast findings about *practice* in this field lose validity (section 1 gap; the Input reader's gap note).
- **Facts, the indirect evidence:**
  - In one study, the behaviour of GPT-3.5 and GPT-4 changed substantially between March and June 2023 (F012-3).
  - In another, 58.8% of prompt-and-model combinations lost accuracy over API updates, on GPT-3.5-era models (library Q-009-F5-3).
  - In a third, on one task and from the abstract only, gains from structured prompting shrank or turned negative on newer GPT models, while Qwen models kept gaining from Few-Shot and CCoT prompting (F012-4).
  - Four Anthropic model IDs were retired 12 to 13 months after their snapshot (library Q-004-F-Q004-4).
- **Estimate, low confidence (mine, from those four):** a finding tied to one model or prompt may hold for months to about a year. No source measures this. The 18.8 to 67.3 point rise in scores on three benchmarks within a year (F012-5) shows how fast models improved on those benchmarks, not how fast findings decay, so I do not count it as support.
- **Facts, from a different field (medicine), where the figures are in years:**
  - Half of 17 AHRQ guidelines were outdated by 5.8 years (library Q-005-LF-Q005-15, weak (C)).
  - 100 systematic reviews went a median 5.5 years before a signal that an update was needed (library Q-009-F13-5).
  - 60% of 474 liver-disease conclusions from 1945–1999 were still judged true when updated in 2009 (F012-1).
  - In the same cohort of 100 reviews, 7% already had an update signal when published (Q-009-F13-5).
  - The Stack Overflow study gives shares, not a rate (F012-2). Of the answers that became obsolete, 58.4% were probably obsolete when posted, and only 20.5% were ever updated.

On how organisations keep up:
- **No review.**
  - Opinion (from the three facts below): in the cases found, most items went without an update, even where updating was the norm.
  - Facts: about 80% (100 − 20.5) of obsolete Stack Overflow answers were never updated (F012-2). 88% of the Cochrane reviews first published 1996 to February 2015 had been inactive for 5.5 years or more (F012-7). In one medical area, only 32.7% of Cochrane reviews were updated within the recommended two years (library Q-009-F5-6).
  - No study found measures what going without review costs (section 2).
- **Fixed schedules.**
  - Facts: ISO international standards are reviewed every 5 years and technical specifications every 3, according to one ISO committee's page (F012-10). Shekelle et al. recommend reassessing guidelines every 3 years (library Q-005-LF-Q005-15, weak (C)). The voluntary NIST AI RMF says periodic reviews are planned and leaves their frequency to the organisation (F012-11).
  - Fact: 19 living reviews had a planned update period and at least one update. Of these, 8 had gone more than 3 times that period since their last version, though the median ratio of actual to planned interval was 1.12 (F012-14).
  - No study found measures what a schedule catches or costs (section 4 gap).
  - A report that NICE dropped its fixed 5-year schedule (F012-13) is unconfirmed and not relied on.
- **Event-triggered review.**
  - No cost figures were found (section 5).
  - Fact: the one study found compares two signal methods with each other, in a small unblinded pilot (F012-15). They agreed with kappa 0.64 overall and 0.30 for one review. The study does not compare event-triggered with scheduled review.
  - Fact: one exploratory paper, with no figures, reports that targeted tests in risk areas can uncover regressions that overall metrics miss (F012-6).
  - Re-running a fixed re-check set when a model changes is a library pattern whose effect is unmeasured (Q-004-P-Q004-1).
- **Continuous intake (living reviews).**
  - Fact: there was one test, for a single living review over one year (F012-21). An automated full search found all 4 new trials, 6 to 12 months before the reference standard, using 17.1 h of screening against 12.4 h. Two cheaper alerts each found 1 of the 4. The new trials did not change the review's results.
  - Facts: two evaluations report workload as a challenge. In one pilot (27 participants), author time ranged from 5 minutes to 32 hours a month, and one Cochrane author called it "probably unsustainable" without extra resources (F012-18). The Australian COVID-19 living guidelines reported workload and fatigue as challenges (F012-19).
  - Fact: 34 of 97 COVID-19 living reviews (35%) were updated at least once (F012-20).
  - Fact: the Cochrane Handbook says living reviews need considerable resources (library Q-009-F13-6).
  - Four of these sources carry a stake note, because their authors run, propose or evaluate living reviews (F012-14, F012-18, F012-19, F012-20).
- **Automated reading.**
  - Facts, screening:
    - Cochrane's RCT classifier, set to 99% recall, found 99.5% of 44,007 RCTs and cut manual screening by 40–70% in pilots (F012-24, from the tool's builders).
    - GPT-4o screening in one living review cut simulated workload by 79–86%, with sensitivity ranging from 58% to 100% (F012-27).
    - A statistical stopping rule kept recall reliable but saved a mean of about 17% of the work, at a 95% recall target (F012-25).
    - Two single LLM configurations had 56.2% and 77.5% sensitivity (F012-26).
  - Facts, other steps:
    - LLM summaries of science overgeneralised in 26–73% of cases, across three models (F012-32).
    - Citation accuracy of deep-research and generative-search systems was 40–80% (F012-33).
    - 3–13% of citation URLs from LLMs and deep-research agents were hallucinated (F012-34).
  - Facts, one tool (Elicit), two independent tests:
    - Search sensitivity averaged 39.5% across four evidence syntheses, against 94.5% for the original reviews' traditional searches (F012-29).
    - In a preprint, its extracted values agreed 90%, but its supporting quotes matched only 46% and its reasoning 30% (F012-31).
    - Elicit's own figures (F012-30) were not found on the page opened, and are not used.
  - Opinion: no source found recommends unchecked automated reading.
  - Facts, what those sources say about checking:
    - The joint statement says AI "should be used with human oversight" (F012-35).
    - The authors of F012-26 and F012-27 say manual validation or human oversight remains necessary.
    - The authors of F012-29 recommend Elicit only as a supplementary search tool.
    - The authors of F012-31 say it complements but does not replace human extractors.

**Thin, absent or from a different field.**
- Fact (the cited sources): all the cost figures found come from evidence synthesis in medicine (F012-8, F012-9, F012-18, F012-19, F012-21; library Q-009-F13-6).
- Fact (the cited sources): most of the evidence on what was caught and missed is from the same field. The exceptions are F012-2 (Stack Overflow), F012-23 (threat-intelligence feeds), F012-6 (LLM drift, no figures) and the AI-tool tests in section 7.
- My count of this memo's URLs:
  - Most AI-specific findings are cited to arXiv or preprint pages from 2023–2026 (F012-3, 4, 6, 31, 32, 33, 34).
  - F012-26, 27 and 29 are journal pages.
- Absent (section gaps):
  - Any measure of how fast AI or agent practice findings decay.
  - What never reviewing costs.
  - The yield of a one-off review.
  - The cost or yield of scheduled or event-triggered review.
  - Anything measured on keeping up with outside practice in software or AI.
- Unopened or unconfirmed, and not relied on: F012-13, F012-16, F012-17, F012-28, F012-30.

Grades: **B** means the Input reader reports it from a page it opened. These are unconfirmed until the Source checker opens them. **B, opened by the Source checker** means the Source checker opened the page and found the stated part there. **assumed (search-only)** means seen only in a search extract, or on a page that was opened without the claimed content. Library facts carry their own grade.

## 1. Do findings lose validity, and how fast?

**Medicine and software (measured decay, other fields)**
- **Fact, B (F012-1, Poynard et al. 2010, https://ideas.repec.org/a/plo/pone00/0012044.html, abstract only):** Of 474 liver-disease conclusions from 1945–1999, updated in 2009, 60% were still judged true, 19% obsolete and 21% false. The 45-year half-life in the authors' 2002 paper is search-only: **assumed (search-only)**.
- **Fact, library weak (C), Q-005-LF-Q005-15 (repeated by F012-12, Shekelle et al. 2001):** Half of 17 AHRQ guidelines were outdated by 5.8 years, and reassessment every 3 years was recommended. F012-12 adds that 90% were still valid only up to 3.6 years, and that the method combined panel surveys with a literature search. Those additions are **B** (https://www.rti.org/publication/validity-agency-healthcare-research-and-quality-clinical-practice-guidelines-how-quickly-do). Stake: minor, the authors are guideline methodologists.
- **Fact, library moderate (B), Q-009-F13-5 (Shojania et al. 2007):** Systematic reviews went a median 5.5 years before a signal that an update was needed. 23% had a signal within 2 years, and 7% already at publication.
- **Fact, B (F012-2, Zhang et al. 2019, https://arxiv.org/abs/1903.12282):** 58.4% of obsolete Stack Overflow answers were probably obsolete when posted, and only 20.5% of obsolete answers are ever updated. This is the nearest field to software practice in the record, and it is about answers, not practice guidance.

**AI models (drift, not practice findings)**
- **Fact, B (F012-3, Chen, Zaharia, Zou, https://arxiv.org/abs/2307.09009v3):** The behaviour of GPT-3.5 and GPT-4 changed substantially between March and June 2023, and the authors call for continuous monitoring. The quote is two separate fragments, the change and the call for monitoring. They were not seen as one sentence and should not be quoted as one. This is not a duplicate of library Q-009-F5-3, which is Ma et al., a different study. The Input reader's possible overlap does not hold on the authors.
- **Fact, library moderate (B), Q-009-F5-3:** 58.8% of prompt-and-model combinations lost accuracy over API updates (GPT-3.5-era models).
- **Fact, B (F012-4, Rudyk et al. 2026, https://arxiv.org/abs/2608.24641, abstract):** Gains from structured prompting shrink or turn negative on newer GPT models. Qwen models continue to benefit substantially from Few-Shot and CCoT, not from all structured prompting. This is one task (Python functions), from the abstract only. The authors say strategies must be adapted per model family and generation.
- **Fact, B (F012-5, Stanford HAI AI Index 2025, https://hai.stanford.edu/ai-index/2025-ai-index-report):** Scores on MMMU, GPQA and SWE-bench rose 18.8, 48.9 and 67.3 points in one year. This measures benchmark saturation, not the decay of findings. Stake: low.
- **Fact, B (F012-6, Chishti et al. 2026, https://arxiv.org/abs/2604.27789):** Silent provider-side updates can introduce behavioural drift, and targeted tests in risk areas can uncover regressions that overall metrics miss. It is exploratory with no figures, and the authors propose their own framework (stake).

**Other library facts that bear on decay (not re-researched)**
- Q-004-F-Q004-3, moderate (B): vendor model IDs are pinned snapshots, but infrastructure updates can still change behaviour slightly.
- Q-004-F-Q004-4, moderate (B): four IDs were retired 12 to 13 months after their snapshot. One more (Sonnet 4.5) is not due to retire until 2026-11-30, about 14 months after its snapshot. The dates are tentative.
- Q-004-F-Q004-8, weak (C*): updates that raise average accuracy still cause negative flips.
- Q-009-F8-4, moderate (B), single vendor: a 32% reduction in issues became a further 4% on a newer model.
- Q-009-F1-1, moderate (B): METR's own page says its 2025 result is out of date.

**Estimates and gaps**
- **Estimate, low confidence (mine):** findings tied to a particular model or prompt may lose validity within months to about a year. No source measures this. It rests on:
  - F012-3: one study, two models, a change within three months.
  - Library Q-009-F5-3: GPT-3.5-era models.
  - F012-4: one task.
  - Library Q-004-F-Q004-4: IDs retired 12 to 13 months after their snapshot.
  - Q-009-F8-4 and Q-009-F1-1, single cases.
  - F012-6, which has no figures.
  - F012-5 is not counted, because it measures benchmark saturation.
- **Opinion, no source:** findings about methods (how to measure, how to check) may last longer. No finding in the record measures this.
- **Gap:** no study measures the decay of findings about AI or agent practice (the Input reader's gap note).
  - The figures found are from medicine, in years (F012-1, Q-005-LF-Q005-15, Q-009-F13-5), and from Stack Overflow (F012-2). F012-2 gives shares of the answers that became obsolete, not a rate.
  - Opinion: neither transfers to AI practice as a rate. What they show is that some findings have problems from the start, as with the 7% of 100 reviews that had an update signal at publication (Q-009-F13-5).

## 2. No deliberate review

**Cost:** nothing direct. There are no figures on what is lost.

**What it caught and missed**
- **Fact, B (F012-7, Hoffmeyer et al. 2021, https://research.regionh.dk/en/publications/most-cochrane-reviews-have-not-been-updated-for-more-than-5-years/, abstract):** 88% of Cochrane reviews first published 1996 to February 2015 had been inactive for 5.5 years or more. This happens even under an organisation whose norm is updating.
- **Fact, library moderate (B), Q-009-F5-6:** Cochrane pregnancy and childbirth reviews had a median 3.3 years to first update, and only 32.7% were updated within the recommended two years.
- **Fact, B (F012-2):** About 80% (100 − 20.5) of obsolete answers are never updated.
- **Opinion (from F012-7, Q-009-F5-6 and F012-2):** in these cases most items went without an update, including in Cochrane, which recommends updating. They do not show what that cost the users.

**How output was checked, what worked:** not applicable, and no evidence.

**Gap:** No study of what organisations doing AI work lose by never reviewing (Input reader's gap note).

## 3. One-off review

**Cost**
- **Fact, B (F012-8, Borah et al. 2017, https://pmc.ncbi.nlm.nih.gov/articles/PMC5337708):** In a convenience sample of 195 registered reviews (192 with time data), a systematic review took a mean of 67.3 weeks (median 65.8, IQR 41.6), with a mean of about 5 authors. The abstract also gives 42 weeks for funded reviews against 26 for unfunded. These cannot be reconciled with the 67.3-week mean, and the paper leaves them unresolved, so this memo does not rely on them.
- **Estimate (the source's own), B, opened by the Source checker (F012-9, Michelson & Reuter 2019, primary paper opened by the Source checker via Europe PMC; its URL is not recorded in the check):** Each systematic review costs about $141,194.80. The primary paper reaches this figure from an economic formula, so it is an estimate, not a measured cost. The figure of about 1.72 person-years appears only on a blog relaying the paper (https://researchgold.org/blog/systematic-review-statistics): **assumed (search-only)**.
- **Opinion (on F012-8 and F012-9):** these are the costs of a full medical systematic review. In my opinion, with no source, a one-off scan of AI practice reading would likely be smaller in scope, so the figures would serve as an upper bound only.

**What it caught and missed**
- **Fact, library moderate (B), Q-009-F13-5:** in one cohort of 100 reviews, 7% already had a signal that an update may be needed at publication, and 23% within 2 years. These are signals, not measured obsolescence.
- **Fact, B (F012-2):** 58.4% of the answers that became obsolete were obsolete when posted. This is a share of the obsolete answers, not of all answers.
- **Opinion (on Q-009-F13-5):** a one-off review can already be partly out of date when finished.

**Gap:** No evaluation of a one-off review's yield.

## 4. Reviews on a schedule

**Practice**
- **Fact, B (F012-10, ISO/TC 211 good-practice page, https://committee.iso.org/sites/tc211/home/resolutions/isotc-211-good-practices/--systematic-review.html):** ISO international standards are reviewed every 5 years and technical specifications every 3. The committee votes to confirm, revise or withdraw, and withdrawal needs a separate ballot. The page says a third party maintains it, and its last dated entry is 2022.
- **Fact, B (F012-11, NIST AI RMF, https://airc.nist.gov/airmf-resources/airmf/5-sec-core/):** Under GOVERN 1.5, periodic reviews "are planned", and roles are defined "including determining the frequency of periodic review". The frequency is thus left to the organisation. The framework is voluntary, so this describes practice; it does not require it.
- **Fact, library weak (C), Q-005-LF-Q005-15:** Shekelle et al. recommend reassessment every 3 years.
- **Opinion, library weak (C) / opinion (M), pattern Q-005-LP-Q005-09:** Review rules on a schedule set from data. The pattern's only origin is clinical guidelines (LF-Q005-15), and its transfer is opinion (M).
- **Fact, library weak (C), Q-009-F5-8:** Thoughtworks fades a Radar entry after two Radars with no change. This is a pruning rule. The entry notes that the page does not state the Radar's publishing cadence. Stake: consultancy.

**Sources disagree on direction**
- **assumed (search-only) (F012-13, NICE PMG20 update information, https://www.nice.org.uk/process/pmg20/chapter/update-information):** NICE removed fixed 5-year routine surveillance in favour of priority-based surveillance, with continuous searching for some key areas. NICE is describing its own process (stake). This is the one reported case of an organisation moving away from a fixed schedule, and it is unconfirmed (the page returned 403 to the Source checker).

**Fixed schedules in living reviews**
- **Fact, B (F012-14, Akl et al. 2023, https://experts.mcmaster.ca/display/publication2951274, abstract listing):**
  - 19 living reviews had both a planned update period and at least one update. Of these, 8 (42%) had gone "greater than 3 times" their planned period since the last version.
  - The median ratio of actual to planned interval was 1.12, so most kept close to their plan.
  - No living review carried a retirement notice. The abstract gives no denominator for this; 76, the total reviewed, is likely but not stated.
  - Stake: the authors are living-review methodologists.

**Cost, catch and miss**
- **Gap:** No cost or yield figures. Newberry 2013 (the cost and yield of the AHRQ surveillance programme) and NICE PMG49 were blocked. No study compares fixed intervals outside medicine.
- **Opinion:** a schedule fixes when review is due, but not whether it is done. Planned cadences were missed in some cases:
  - Library Q-009-F5-6: 32.7% updated within the recommended two years, in one medical area.
  - F012-14: 8 of 19 living reviews had gone more than 3 times their planned period, though the median ratio was 1.12.
  - F012-7 shows 88% of one Cochrane cohort inactive for 5.5 years or more, but it states no planned cadence.

## 5. Reviews started by events (signals)

**What it caught and missed**
- **Fact, B (F012-15, Chung et al. 2012, https://pmc.ncbi.nlm.nih.gov/articles/PMC4141462):** An expert-plus-search method (RAND) and a literature-signal method (modified Ottawa) gave broadly similar update signals: kappa 0.64 overall, but 0.30 for one review.
  - The pilot was small and unblinded, and could not test predictive validity.
  - The authors call the judgements "largely subjective".
- **assumed (search-only) (F012-16, NICE PH13 2019 exceptional surveillance, https://www.nice.org.uk/guidance/ph13/resources/2019-exceptional-surveillance-of-physical-activity-in-the-workplace-nice-guideline-ph13-6661547533/chapter/How-we-made-the-decision):** NICE runs "exceptional surveillance" between scheduled checks when significant new evidence appears. It does not consult when it decides not to update, which leaves that decision unchecked from outside. NICE is describing itself.
- **assumed (search-only) (F012-17, OpenAI, https://openai.com/index/expanding-on-sycophancy/):** In the GPT-4o sycophancy incident, public reaction after release caught the problem. Expert testers said it "felt" off, and there was no sycophancy-specific evaluation. This is the vendor's self-report on its own failure.
- **Opinion, no finding measures this:** an event trigger catches only what someone is watching for. F012-17 is unconfirmed and not used to support this.
- **Fact, B (F012-6):** Targeted tests in risk areas can uncover regressions that overall metrics miss (exploratory, no figures).
- **Opinion:** one kind of event trigger is a model or provider change. Library pattern Q-004-P-Q004-1 (moderate (B), effect unmeasured) is to re-run a fixed re-check set when a role's model changes.

**Cost:** no figures (Garner 2016 and the FAA airworthiness-directive rules were not opened).

## 6. Continuous intake: living reviews, horizon scanning, feeds

**Cost and workload**
- **Fact, library moderate (B), Q-009-F13-6:** The Cochrane Handbook says living reviews need considerable resources.
- **Fact, B (F012-18, Millard et al. 2019, https://pmc.ncbi.nlm.nih.gov/articles/PMC6911272, 27 participants):** In the pilot living reviews, searches ran monthly to three-monthly.
  - Author time ranged from 5 minutes to 32 hours a month, with 3 to 300 citations a month.
  - One Cochrane author called it "probably unsustainable" without extra resources.
  - Some teams dropped the automation or slowed their cadence.
  - Stake: Cochrane Australia evaluating a Cochrane pilot, and Elliott is a leading proponent of living reviews.
- **Fact, B (F012-19, Turner, Elliott et al. 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC8741039/):** The Australian COVID-19 living guidelines published 20 weekly updates in about 5 months, with 11 FTE staff, 7 panels and more than 200 contributors.
  - Output was checked by weekly panels, a leadership group and a steering committee.
  - The challenges reported were workload, fatigue and a "relentless" pace.
  - The source disagrees with itself on satisfaction: more than 90% in the abstract, more than 85% in the results.
  - Stake: the Taskforce evaluating itself.
- **Fact, B, opened by the Source checker (F012-20, Heron et al. 2023, https://pubmed.ncbi.nlm.nih.gov/37660117/):** Only 34 of 97 COVID-19 living reviews (35%) were updated at least once. **assumed (search-only):** the authors tie this to workload and advise a core team plus automation; this was not seen in the abstract text. Stake: the authors run living reviews.

**What different intake methods caught and missed**
- **Fact, B (F012-21, Gates et al. 2021, https://pmc.ncbi.nlm.nih.gov/articles/PMC8056603/):** A prospective one-year test of search methods for a living review compared screening time against new trials found:

  | Method | Screening time | New trials found (of 4) |
  |---|---|---|
  | Automated full search | 17.1 h | 4, 6 to 12 months early |
  | Reference standard | 12.4 h | (the comparison) |
  | Similar-article alerts (PubMed Similar Articles) | 9.4 h | 1 |
  | Citation alerts (Scopus Citing References) | 5.2 h | 1 |

  The new trials did not change the review's results. Opinion: this is the only finding here that sets cost against catch, and it covers one review.
- **Fact, B (F012-22, Simpson et al. 2004, https://www.cambridge.org/core/journals/international-journal-of-technology-assessment-in-health-care/article/assessing-the-accuracy-of-forecasting-applying-standard-diagnostic-assessment-tools-to-a-health-technology-early-warning-system/70CDD85E14DDBF0DEE69A99B43FCF92A, abstract):** The UK horizon-scanning early-warning system had 71% sensitivity, 73% specificity and 14% positive predictive value, so 86% of its positive predictions were not borne out. The gold standard was imperfect.
- **Fact, B (F012-23, Bouwman et al. 2020, https://www.usenix.org/conference/usenixsecurity20/presentation/bouwman):** Two commercial threat-intelligence feeds had an average overlap of only 2.5–4.0% in their indicators. The study examined 22 threat actors; the page does not show whether the overlap figure is limited to them. Shared indicators appeared about a month later in the other feed. Customers judge feeds by informal heuristics, not measured coverage.
- **Opinion, from two cases:** a single outside feed or alert may cover only part of what exists. In F012-23, two threat-intelligence feeds overlapped 2.5–4.0%. In F012-21, two alerts each found 1 of 4 new trials, for one review.

**Gap:** No figures for the cost of producing a living review or guideline. Packer 2012 (10 years of horizon scanning) gave no results in its abstract.

## 7. How the reading, choosing and summarising is done: people, tools, or both

**Choosing: screening and search**
- **Fact, B (F012-24, Thomas et al. 2021, https://pmc.ncbi.nlm.nih.gov/articles/PMC8168828):** Cochrane's RCT classifier, set to 99% recall, found 99.5% of 44,007 RCTs. Counting records with too little text, it found 93.8%. Precision was about 8%, and it cut manual screening by 40–70% in pilots. Stake: the authors built and deploy the tool.
- **Fact, B (F012-25, Callaghan & Müller-Hansen 2020, https://pmc.ncbi.nlm.nih.gov/articles/7700715):** Earlier stopping rules for machine-prioritised screening gave inconsistent recall. A statistical stopping rule kept recall reliable but saved only about 17% of the work (a mean, at a 95% recall target). Stake: the authors propose the rule.
- **Fact, B (F012-26, López-Pineda et al. 2025, https://www.cambridge.org/core/product/EDE7C95374C7FF6200B7280D5742D906/core-reader):** LLM title and abstract screening varied by model and configuration. One GPT-4o mini configuration (CHAT_2) had 56.2% sensitivity, and one Llama 3 (70B) configuration (LLA_2) had 77.5%. These are single configurations, not model-wide figures. The authors say manual validation remains necessary.
- **Fact, B (F012-27, Homiar, Thomas et al. 2025, https://pmc.ncbi.nlm.nih.gov/articles/PMC12306261/):** In a living review, GPT-4o prompts were developed on one set and validated on two updates.
  - In the single-pass baseline and update runs, they excluded no finally-included study.
  - The repeated-run check reports one erroneous exclusion (1 of 730 decisions).
  - The paper's record counts (73 against 63 included studies) are not reconciled.
  - Sensitivity ranged 58–100% and precision 4–20%.
  - Decisions were stable over 10 runs.
  - Simulated workload fell 79–86%.
  - The authors require human oversight. Stake: a co-author develops screening tools.
- **assumed (search-only) (F012-28, Cao et al. 2025, preprint, https://www.medrxiv.org/content/10.1101/2025.06.13.25329541.full.pdf):** The end-to-end otto-SR system reportedly reproduced 12 Cochrane reviews in two days, with 96.7% screening sensitivity against 81.7% for humans. Outputs that changed conclusions were verified by two human reviewers. Abstract versions word the missed-studies result differently. Not peer reviewed, and competing interests were not checked.
- **Elicit: two independent tests, and the tool-maker's own figures, which are unconfirmed.**
  - **Fact, B (F012-29, Lau & Golder 2025, https://pmc.ncbi.nlm.nih.gov/articles/PMC12483133/):** Across four evidence syntheses, Elicit's search sensitivity averaged 39.5% (25.5–69.2%), against 94.5% for the original reviews' traditional searches. The authors recommend it only as a supplementary search tool. No conflicts declared.
  - **assumed (search-only) (F012-30, Elicit's own blog, https://elicit.com/blog/how-we-evaluated-elicit-systematic-review):** Search extracts attribute to Elicit claims of 94% correct screening and 94–99% extraction accuracy. The Source checker opened the page but did not find these figures in it, so they are not confirmed. Stake: Elicit sells the product.
  - These figures are unconfirmed, so no comparison is drawn between them and F012-29 or F012-31. Even if they were confirmed:
    - They measure different tasks from F012-29 (screening and extraction accuracy, against search sensitivity).
    - F012-31's 90% value agreement is not clearly lower than the claimed 94–99% extraction accuracy.

**Extracting and summarising**
- **Fact, B (F012-31, Lagisz et al. 2025, preprint, https://ecoevorxiv.org/repository/view/9909/):** Elicit's extracted values agreed 90%, but its supporting quotes matched only 46% and its reasoning 30%. In high-accuracy mode these fell to 10% and 0%. The authors say it complements but does not replace human extractors.
- **Fact, B (F012-32, Peters & Chin-Yee 2025, https://arxiv.org/abs/2504.00025v1, abstract):** LLM summaries of science overgeneralised in 26–73% of cases; this range covers DeepSeek, ChatGPT-4o and LLaMA 3.3 70B. The odds of broad generalisation were nearly 5 times those of human summaries (odds ratio 4.85, CI 3.06–7.70). The page says this held for most LLMs, that prompting for accuracy did not remove it, and that newer models "tended to" do worse.
- **Fact, B (F012-33, DeepTRACE 2025, https://arxiv.org/abs/2509.04499):** In deep-research configurations, large fractions of statements were not supported by the listed sources. Citation accuracy was 40–80% across systems. The authors' affiliation (possibly Salesforce, a stake) is unconfirmed.
- **Fact, B (F012-34, Rao et al. 2026, https://arxiv.org/abs/2604.03173):** 3–13% of citation URLs from LLMs and deep-research agents were hallucinated, and 5–18% did not resolve. A URL checker cut non-resolving links to under 1%. Stake: the authors release the checker.

**How output is checked**
- **Fact, B (F012-35, Cochrane / Campbell / JBI / CEE joint statement 2025, https://pmc.ncbi.nlm.nih.gov/articles/PMC12594113/):** The statement says reviewers should keep human oversight and author accountability, demonstrate that tools are sound, and report AI use in full. It uses "must" only for tool developers. The bodies set norms for their own field.
- **Fact, library moderate (B), Q-009-F10-3 (single vendor):** Human evaluation caught agents choosing content farms over authoritative sources.

**Opinion, across F012-24 to F012-35 (excluding the unconfirmed F012-28 and F012-30):**
- No source found recommends unchecked automated reading.
- In the tests found, tools rank or screen for recall and people still check inclusion (F012-24, F012-26, F012-27).
- Among the steps tested, the lowest figures were for:
  - one tool's search (F012-29: 39.5%)
  - supporting quotes and reasoning (F012-31: 46% and 30%)
  - summaries (F012-32: overgeneralised in 26–73%)
  - citations (F012-33: 40–80% accuracy; F012-34: 3–13% hallucinated URLs)
- These are different measures, so this is not a like-for-like ranking.

**Gaps**
- No head-to-head comparison of people, tools and both for keeping up, beyond F012-21 and the screening studies.
- Nothing measured on keeping up with outside practice in software or AI.
- Practitioner accounts (Husain and others) were seen only secondhand.

**Transfer.** Opinion.
- The screening tests found (F012-24 to F012-27) were run on records for systematic reviews.
- Outside AI practice comes largely from vendor posts, preprints and blogs. This memo's own AI sources are mostly arXiv or vendor pages.
- So, in my opinion, the screening recall figures (F012-24, F012-27) are unlikely to hold as given.
- The summary and citation failures (F012-32 to F012-34) were measured on general LLMs and deep-research systems, not on review tools. In my opinion they transfer more directly.

## What each answer would change (as the question frames it; no choice made here)

- **Shelf life.** The question's framing is that the kind of review that fits depends on how long findings last (research/Q-012.md). No source settles it (section 1 gap).
  - Suppose model- and prompt-tied findings last months to about a year. That is my low-confidence estimate, from F012-3, F012-4, library Q-009-F5-3 and Q-004-F-Q004-4. By the question's framing, that favours more frequent review. My opinion is that it also favours review triggered by model and provider changes: library pattern Q-004-P-Q004-1, whose effect is unmeasured.
  - Suppose findings last years, as the medical figures from a different field show (F012-1; library Q-005-LF-Q005-15, Q-009-F13-5). By the question's framing, that favours less frequent review, or none.
  - Opinion, no source: if model-tied findings and method findings differ, each class may need its own shelf life.
- **Who or what does each step.**
  - Screening evidence that favours tools:
    - F012-24: 99.5% found at a 99% recall setting, from the tool's builders.
    - F012-27: one living review, 58–100% sensitivity across runs, 79–86% simulated workload cut.
  - Screening evidence that does not:
    - F012-26: single configurations at 56.2% and 77.5%.
    - F012-25: the statistical stopping rule saved a mean of about 17%, at a 95% recall target.
  - F012-28 is unconfirmed and not used.
  - Evidence of tools doing poorly at other steps:
    - One tool's search sensitivity averaged 39.5% (F012-29).
    - One tool's supporting quotes matched 46% (F012-31, preprint).
    - Summaries overgeneralised in 26–73% of cases (F012-32, three models).
    - Citation accuracy was 40–80% (F012-33), and 3–13% of URLs were hallucinated (F012-34).
    - By the question's framing, this evidence bears on having people do the search, summary and claim-checking steps, or on placing a check after each.
  - The tool-maker's own Elicit figures (F012-30) could not be confirmed. So this memo has no confirmed vendor figure to set against F012-29 and F012-31.
- **Where checks sit.**
  - Fact: the joint statement says AI and automation in evidence synthesis "should be used with human oversight". It does not list stages (F012-35).
  - Opinion: the lowest figures found were in five places, which points to checks after search, extraction, summarising and citing, and to not relying on a single feed:
    - search (F012-29)
    - supporting quotes and reasoning (F012-31)
    - summaries (F012-32)
    - citations (F012-33, F012-34)
    - the overlap between two threat-intelligence feeds (F012-23)
- **What is affordable.**
  - Fact: in a convenience sample of 192 registered medical reviews with time data, a review took a mean of 67.3 weeks with a mean of about 5 authors (F012-8).
  - Estimate (the source's own): about $141,195 per review, from a formula (F012-9). Opinion: for a narrower scan these figures are an upper bound.
  - Fact: in one pilot of living reviews (27 participants), author time was 5 minutes to 32 hours a month (F012-18).
  - Fact: in one case, the Australian COVID-19 living guidelines, 20 weekly updates in about 5 months used 11 FTE staff, 7 panels and over 200 contributors (F012-19).
  - Fact: in one test, for one review over one year (F012-21):
    - similar-article alerts took 9.4 h and citation alerts 5.2 h of screening, and each found 1 of the 4 new trials
    - the automated full search took 17.1 h and found all 4
    - the new trials did not change the review's results
  - Fact: living reviews need considerable resources (library Q-009-F13-6). In one pilot, some teams slowed their cadence or dropped the automation (F012-18).
  - No cost figures were found for scheduled or event-triggered review (sections 4 and 5; Newberry 2013 and NICE PMG49 were blocked).

## Questions I add (not closed)

1. What is the measured rate at which the portfolio library's own entries are overturned or found stale on re-check, by type of entry (model-tied against method)? This is the local shelf-life evidence the outside record lacks.
2. What do Newberry 2013 (AHRQ surveillance cost and yield) and NICE PMG20/PMG49 report on the cost and yield of scheduled against priority-based surveillance? They were blocked this time.
3. Is there any measured evaluation of how software or AI practitioners or firms (Radar-style boards, engineering blogs, evaluation teams) keep their practice current, with cost and misses?

## Sources needed that were not gathered (gaps for the Input reader)

- Newberry 2013.
- NICE PMG20 and PMG49 full text.
- Garner 2016 (BMJ update checklist).
- The FAA airworthiness-directive rules.
- The OpenAI sycophancy postmortem (it returned 403 and was not opened).
- Michelson & Reuter 2019: the Source checker opened the primary via Europe PMC, but its URL is not yet recorded.
- Heron 2023 full text.
- otto-SR full text, with its competing interests.
- Poynard 2002 (the half-life).
- The content of Elicit's evaluation.
- Packer 2012 results.
- Any figures on the cost of producing a living review.
- Any software or AI study of how fast practice findings decay.
- Primary practitioner accounts of cadence.

## Proposed library entries (statement | type | grade | shelf life proposed)

1. Of 474 liver-disease conclusions (1945–1999) updated in 2009, 60% were judged true, 19% obsolete and 21% false (Poynard 2010) | fact | B | 10 years
2. 58.4% of obsolete Stack Overflow answers were probably obsolete when posted, and 20.5% of obsolete answers are ever updated (Zhang 2019) | fact | B | 5 years
3. GPT-3.5 and GPT-4 behaviour changed substantially between March and June 2023, and the authors call for continuous monitoring (Chen, Zaharia, Zou), quoted as two separate fragments | fact | B | 2 years
4. On one task (Python functions; abstract), gains from structured prompting shrink or turn negative on newer GPT models, while Qwen models continue to benefit from Few-Shot and CCoT; the authors say strategies must be adapted per model family and generation (Rudyk 2026) | fact | B | 12 months
5. MMMU, GPQA and SWE-bench scores rose 18.8, 48.9 and 67.3 points within a year of introduction (AI Index 2025); this measures benchmark saturation, not the decay of findings | fact | B | 2 years
6. Silent LLM updates can introduce drift, and targeted risk-area tests can uncover regressions that overall metrics miss (Chishti 2026; exploratory; the authors' own framework) | fact | B | 12 months
7. 88% of Cochrane reviews first published 1996 to February 2015 had been inactive for 5.5 years or more (Hoffmeyer 2021) | fact | B | 5 years
8. In a convenience sample of 195 registered reviews, a systematic review took a mean of 67.3 weeks (median 65.8) with about 5 authors; the paper's funded and unfunded figures cannot be reconciled with the mean (Borah 2017) | fact | B | 5 years
9. ISO international standards get a systematic review every 5 years and technical specifications every 3, with a vote to confirm, revise or withdraw | fact | B | 3 years
10. The voluntary NIST AI RMF describes planned periodic review and leaves determining its frequency to roles in the organisation | fact | B | 3 years
11. Of 19 living reviews with a planned update period and at least one update, 8 (42%) had gone more than 3 times that period since the last version, though the median actual-to-planned ratio was 1.12; no living review carried a retirement notice, with no denominator given in the abstract (Akl 2023) | fact | B | 3 years
12. RAND and modified-Ottawa update signals agreed with kappa 0.64 in a small unblinded pilot, and the judgements were "largely subjective" (Chung 2012) | fact | B | 5 years
13. Pilot living reviews took 5 minutes to 32 hours of author time a month, and one Cochrane author called them probably unsustainable without extra resources (Millard 2019; proponents' evaluation) | fact | B | 3 years
14. The Australian COVID-19 living guidelines published 20 weekly updates in about 5 months with 11 FTE, and workload and fatigue were the main challenges (Turner 2022; self-evaluation; abstract and results disagree on satisfaction) | fact | B | 5 years
15. In a one-year test, only an automated full search found all 4 new trials, 6–12 months early, at 17.1 h against 12.4 h for the reference standard; similar-article alerts (9.4 h) and citation alerts (5.2 h) each found 1 of 4 (Gates 2021) | fact | B | 5 years
16. A UK health-technology early-warning system had 71% sensitivity, 73% specificity and 14% positive predictive value (Simpson 2004) | fact | B | 10 years
17. Two commercial threat-intelligence feeds had an average overlap of only 2.5–4.0% in their indicators (Bouwman 2020) | fact | B | 5 years
18. Cochrane's RCT classifier found 99.5% of 44,007 RCTs (93.8% counting thin records), with precision about 8% and a 40–70% cut in screening (Thomas 2021; the tool's builders) | fact | B | 3 years
19. Earlier stopping rules for prioritised screening gave inconsistent recall, and a statistical rule kept recall reliable while saving a mean of about 17% at a 95% recall target (Callaghan 2020) | fact | B | 5 years
20. LLM screening sensitivity varied by model and configuration (a GPT-4o mini configuration 56.2%, a Llama 3 70B configuration 77.5%), and manual validation remains necessary (López-Pineda 2025) | fact | B | 12 months
21. GPT-4o screening in a living review excluded no finally-included study in single-pass runs, with one erroneous exclusion in 730 repeated-run decisions; it cut simulated workload 79–86% and needs human oversight (Homiar 2025) | fact | B | 12 months
22. Independently tested across four evidence syntheses, Elicit's search sensitivity averaged 39.5% against 94.5% for the original reviews' traditional searches (Lau & Golder 2025) | fact | B | 12 months
23. Elicit's supporting quotes and reasoning matched only 46% and 30%, falling to 10% and 0% in high-accuracy mode (Lagisz 2025, preprint) | fact | B | 12 months
24. Summaries of science by DeepSeek, ChatGPT-4o and LLaMA 3.3 70B overgeneralised in 26–73% of cases, with nearly 5 times the odds of human summaries (OR 4.85); per the page this held for most LLMs, and newer models tended to do worse (Peters & Chin-Yee 2025) | fact | B | 2 years
25. Citation accuracy of deep-research and generative-search systems ranged 40–80% (DeepTRACE 2025) | fact | B | 12 months
26. 3–13% of citation URLs from LLMs and deep-research agents were hallucinated, and URL checking cut non-resolving links to under 1% (Rao 2026; the authors' own tool) | fact | B | 12 months
27. The Cochrane, Campbell, JBI and CEE joint statement says reviewers should keep human oversight and accountability, demonstrate tool soundness and fully report AI use | fact | B | 3 years
28. NICE replaced fixed 5-year surveillance with priority-based surveillance and exceptional reviews on significant new evidence | fact | assumed (search-only) | 3 years. Not to be filed until someone opens the NICE page.
29. In the one test found, for one review, a cheap alert found 1 of 4 new trials, and two threat-intelligence feeds overlapped only 2.5–4.0%; pair a cheap alert with a periodic fuller search and measure what each finds (origin F012-21, F012-23) | pattern | opinion built on B sources | 3 years
30. Let tools rank and screen for recall; have people verify each summary, quote and citation that a decision rests on (origin F012-24 to F012-35, excluding the unopened F012-28 and F012-30) | pattern | opinion built on B sources | 12 months

## Finding ids relied on

F012-1 to F012-35, except those below. Search-only or unconfirmed, staying assumed, not used to support any sentence, and out of the library: F012-13, F012-16, F012-17, F012-28, F012-30, the blog-only 1.72 person-years in F012-9, and the workload tie and advice in F012-20. F012-5 is cited but not counted as support for the shelf-life estimate. Library entries cited: Q-005-LF-Q005-15, Q-005-LP-Q005-09, Q-009-F5-3, Q-009-F5-6, Q-009-F5-8, Q-009-F13-5, Q-009-F13-6, Q-004-F-Q004-3, Q-004-F-Q004-4, Q-004-F-Q004-8, Q-004-P-Q004-1, Q-009-F1-1, Q-009-F8-4, Q-009-F10-3.

Points for the Source checker:
- The summary parts were rewritten so that each sentence names its ids, with the base for each figure and a fact, estimate or opinion mark. These are the Answer in brief, the new "Thin, absent or from a different field" paragraph, "What each answer would change", and every Opinion and Estimate line.
- Round 3 corrections:
  - Correction 1 (Elicit): "much less favourable" is gone everywhere.
  - Correction 2 ("outdated when published"): gone. 7% is now an update signal, and 58.4% is a share of the obsolete answers.
  - Correction 3 (joint statement): now quoted, with no stages listed.
  - Correction 4 (smaller wordings): all three applied.

## Tokens

I cannot see my token count.

---

## Change list (item: what changed, and what it answers)

1. **Answer in brief, opening sentence:** "Findings about building with AI models do lose validity" is now an opinion from indirect evidence only, citing F012-3, F012-4 and Q-009-F5-3. *Summary-sentence check.*
2. **Answer in brief, indirect evidence:**
   - Each item is now a single-case fact with its base (one study, two models; GPT-3.5-era; one task, abstract).
   - Q-004-F-Q004-4 is added.
   - F012-5 is removed as support and noted as benchmark saturation (round 1's F012-5 note).
   - Q-009-F5-3 is no longer cited for "depend on model generation". *Summary-sentence check.*
3. **Answer in brief, shelf-life estimate:** "months, not years" is now "months to about a year", to match section 1. It is marked as my low-confidence estimate, with its ids. *Summary-sentence check.*
4. **Answer in brief, "Fields that measure decay directly … much slower rates":**
   - Replaced with the medical figures and their bases (Q-005-LF-Q005-15, Q-009-F13-5, F012-1).
   - Stated that F012-2 gives shares, not a rate. *Round 3 correction 4, third point.*
5. **Answer in brief, "a sizeable share … already outdated when published":**
   - Replaced with "7% of 100 reviews already had an update signal at publication" (Q-009-F13-5).
   - F012-2's 58.4% is now stated as a share of the obsolete answers. *Round 3 correction 2.*
6. **Answer in brief, F012-4:** limited to Few-Shot and CCoT, on one task, from the abstract (also in section 1 and entry 4). *Round 3 correction 4, second point.*
7. **Answer in brief, no-review bullet:** the opinion is restated with its three ids, adding Q-009-F5-6. "Common default" is replaced by "in the cases found, most items went without an update". *Summary-sentence check.*
8. **Answer in brief, fixed-schedules bullet:**
   - The ISO figure is now attributed to one committee's page.
   - NIST (F012-11) and F012-14 (8 of 19; median ratio 1.12) are added.
   - "No measured yield" now cites the section 4 gap.
   - NICE is marked unconfirmed and not relied on. *Summary-sentence check.*
9. **Answer in brief, event-triggered bullet:**
   - The search-only OpenAI incident (F012-17) is removed, because an unconfirmed claim may not support anything.
   - F012-15 now gives its kappa base.
   - F012-6 ("can uncover", exploratory) and Q-004-P-Q004-1 (effect unmeasured) are added. *Summary-sentence check.*
10. **Answer in brief, continuous-intake bullet:**
    - F012-21 is now stated with its figures, as a test of search methods within one living review. It is no longer "continuous intake found new evidence earliest", which implied a comparison across ways.
    - "Heavy workload" becomes "workload as a challenge", with F012-18's range and quote and F012-19's challenges.
    - Q-009-F13-6 is added.
    - "Mostly its own advocates" becomes four named sources with stake notes. *Summary-sentence check.*
11. **Answer in brief, automated-reading bullet:**
    - "Cuts screening work a lot" becomes figures with their bases (F012-24, 27, 25).
    - "Recall varies widely" now gives its ids (F012-26, 27).
    - "Summaries and citations … unreliable" becomes the F012-32, 33 and 34 figures.
    - "Only independent tests are much less favourable" becomes what F012-29 and F012-31 measured, with F012-30 not used. *Round 3 correction 1; summary-sentence check.*
    - Each source's own words on checking are now given (F012-29 recommends a supplement; it does not "keep people checking"). *Summary-sentence check.*
12. **New "Thin, absent or from a different field" paragraph:** this replaces the balance sentence. That sentence had restated the Input reader's note: "almost entirely from medicine" and "mostly 2025–2026 preprints". It now names the cost findings, the non-medical exceptions and my URL count, lists the gaps by section, and lists the unconfirmed ids. *Summary-sentence check.*
13. **Section 1, estimate:** the ids and their single-case bases are named, and F012-5 is excluded. "Methods last longer" is split out as my opinion, with no source. *Summary-sentence check.*
14. **Section 1, gap:** "lower bound on the share that is wrong at publication" is replaced by the shares and signals with their bases, plus an opinion that the figures do not transfer as a rate. *Round 3 correction 2.*
15. **Section 1, F012-4 and F012-5 lines:** F012-4 is limited to Few-Shot and CCoT on one task. F012-5 is noted as measuring benchmark saturation. F012-6 now reads "can uncover" (the page's wording). *Round 3 correction 4; round 1 table notes on F012-4, F012-5 and F012-6, which the summary now relies on.*
16. **Section 2:** the F012-2 line changes from "Without a review, about 80% … stay uncorrected" to "about 80% (100 − 20.5) … are never updated". The opinion "the default drifts towards no review" is restated to the three ids. *Summary-sentence check.*
17. **Section 3:**
    - Q-009-F13-5 changes from "7% already outdated at publication" to "had a signal that an update may be needed", which is the library entry's wording.
    - F012-2 is stated as a share of the obsolete answers.
    - "Starts to decay at once" becomes "can already be partly out of date", resting on Q-009-F13-5.
    - "Far smaller in scope" is marked as my opinion, with no source. *Round 3 correction 2; summary-sentence check.*
18. **Section 4:**
    - The Q-005-LP-Q005-09 line notes its only origin (clinical guidelines).
    - In the opinion "planned cadences missed", F012-7 is no longer said to show a missed planned cadence, because it states none.
    - Q-009-F5-6's 32.7% and F012-14's 1.12 ratio are given. *Summary-sentence check.*
19. **Section 5:**
    - The opinion no longer uses the unconfirmed F012-17 as support.
    - F012-6 now reads "can uncover".
    - "One kind of event trigger is model change" is marked as opinion. *Summary-sentence check.*
20. **Section 6:**
    - "Clearest cost-against-catch evidence" is marked as opinion and narrowed to "the only finding here that sets cost against catch".
    - "Any one outside feed covers only part" is restated as an opinion from two cases (F012-23, F012-21). *Summary-sentence check.*
21. **Section 7, Elicit:**
    - The heading and closing line no longer say "much less favourable". They now say that no comparison is drawn.
    - Also recorded: F012-31's 90% is not clearly below the claimed 94–99%. *Round 3 correction 1.*
22. **Section 7, F012-25, F012-29 and F012-33 lines:**
    - F012-25: "a mean, at a 95% recall target" (round 1 table note).
    - F012-29: four evidence syntheses, and the 94.5% belongs to the original reviews' traditional searches (round 1 table note).
    - F012-33: unsupported statements limited to deep-research configurations (round 1 table note).
    - The summary now cites these figures, so their bases are stated. *Summary-sentence check ("a figure with its base").*
23. **Section 7, opinion:**
    - "People verify … any claim that changes a conclusion" is removed, because it came only from the unconfirmed F012-28.
    - "Summaries and citations are the weakest automated steps" is replaced by the lowest figures with their ids, noted as different measures. *Summary-sentence check.*
24. **Transfer opinion:**
    - "Biomedical abstracts with structured study designs" becomes "records for systematic reviews", because F012-31 is not biomedical and the topics of F012-26 are not recorded.
    - "General to LLMs" becomes "measured on general LLMs and deep-research systems". *Summary-sentence check.*
25. **"What each answer would change":**
    - Shelf life: each branch names its ids, separates the question's framing from my opinion, and marks the per-class idea as my opinion.
    - Who does each step: F012-25 and F012-26 are added to the screening evidence, figures are given with their bases, and F012-28 is marked not used. The Elicit "much less favourable" line is replaced.
    - Where checks sit: the joint statement is now quoted ("should be used with human oversight", with no stages), and "concentrated in" is relabelled as opinion, with F012-29 included as a search failure.
    - Affordable: F012-8 now carries its sample base. "An upper bound" is marked as my opinion. F012-9 is added as the source's estimate. "Up to 11 FTE in a crisis" becomes one case with its figures. Cheap alerts now read "in one test, for one review, over one year", with the exact hours. "No cost evidence at all" becomes "no cost figures were found", with the blocked sources named.
    - *Round 3 corrections 1, 3 and 4 (first point); summary-sentence check.*
26. **Proposed entries:**
    - Entry 4 is limited to Few-Shot/CCoT and one task (correction 4).
    - Entry 5 adds the saturation note.
    - Entry 6 now reads "can uncover".
    - Entry 19 adds the 95% recall target.
    - Entry 22 adds the four syntheses and the original reviews' searches.
    - Pattern 29: "any one outside feed covers only part of what exists" becomes the two measured cases.
    - These follow from items 6, 15 and 22. The filed entries in /home/user/lib-q-012 need matching only for entry 4 (and 19 and 22 if the filed text lacks these bases); I could not read them.
27. **Sources needed:** "The OpenAI sycophancy postmortem (opened)" was wrong, because the page returned 403. It now reads "not opened". *Consistency with the round 1 record for F012-17.*
28. **Header italic line, "Finding ids relied on" and "Points for the Source checker":** updated for this round. The header line is left for the Orchestrator to fill.

No grade mark changed. All other findings lines are as in round 3.

## Finding ids for the Source checker to re-check

- **Summary sentences, against the ids each now names:** the Answer in brief (all bullets), "Thin, absent or from a different field", "What each answer would change", and the Opinion and Estimate lines in sections 1–7 and Transfer. Together these rely on:
  - F012-1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 29, 31, 32, 33, 34, 35
  - library Q-005-LF-Q005-15, Q-005-LP-Q005-09, Q-009-F5-3, Q-009-F5-6, Q-009-F13-5, Q-009-F13-6, Q-004-F-Q004-4, Q-004-P-Q004-1
- **Findings lines changed:**
  - F012-4: Few-Shot/CCoT, one task.
  - F012-5: the saturation note.
  - F012-6: "can uncover".
  - F012-2 in sections 2 and 3.
  - Q-009-F13-5 in section 3: "signal", not "outdated".
  - F012-25: the 95% target.
  - F012-29: four syntheses, the original reviews' searches.
  - F012-33: deep-research configurations.
  - The Elicit block (F012-29/30/31).
- **Proposed entries 4, 5, 6, 19 and 22, and pattern 29:** check against the filed Q-012-4, -5, -6, -19, -22 and P1 in /home/user/lib-q-012.
- **Not to be used anywhere as support:** F012-13, 16, 17, 28, 30, the blog-only part of F012-9, and the workload tie in F012-20. Please confirm that no summary sentence leans on them.

## Tokens

I cannot see my token count.

Files read: /home/user/Model-Lab/research/Q-012-memo.md, /home/user/Model-Lab/research/Q-012-source-check.md, /home/user/Model-Lab/research/Q-012.md, /home/user/Model-Lab/research/Q-012-input.md, and library entries under /home/user/portfolio/library/ (README.md, facts Q-009-F13-5, F13-6, F5-3, F5-6, F5-8, F8-4, F10-3, Q-004-F-Q004-4, Q-004-F-Q004-8; patterns Q-005-LP-Q005-09, Q-004-P-Q004-1). No web use.
