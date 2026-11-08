# Q-012 memo, 2026-11-08: how fast findings about practice lose validity, and how organisations keep their practice up to date

*The Researcher's memo for Q-012, round 3 (brief 179, docs/briefs/179-researcher.md), revised after the Source checker's round 2 (research/Q-012-source-check.md); rounds 1 (brief 163) and 2 (brief 172) are in this file's history. Recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p), 2026-11-08, from the helper's return; only this italic line is the Orchestrator's.*

**Answer in brief.** Findings about building with AI models do lose validity. No study measures how fast for *practice* findings in this field, though. The nearest evidence is indirect: hosted model behaviour changed within three months (F012-3), benchmarks introduced in 2023 rose 19 to 67 points within a year (F012-5), and gains from prompting techniques depend on the model generation (F012-4; library Q-009-F5-3). Together these point to a shelf life measured in months, not years. That is an estimate. Fields that measure decay directly (medicine, Stack Overflow) find much slower rates, but also that a sizeable share of findings is already outdated when published (F012-2; library Q-009-F13-5). On how organisations keep up:
- **No review** is, in my reading, the common default (opinion). The sources give shares left alone: about 80% of obsolete Stack Overflow answers are never updated (F012-2), and 88% of one cohort of Cochrane reviews had been inactive for 5.5 years or more (F012-7).
- **Fixed schedules** exist (ISO every 5 years, Shekelle's advice of every 3) but have no measured yield. NICE reportedly dropped its fixed 5-year schedule for priority-based watching (search-only).
- **Event-triggered review** has no cost figures. The only comparison found is a small pilot of two signal methods (F012-15), not a comparison with scheduled review. One AI incident was caught only after release, by the public (search-only).
- **Continuous intake (living reviews)** found new evidence earliest in the one test found, for a single review (F012-21). Two evaluations report heavy workload (F012-18, F012-19), and only 35% of COVID-19 living reviews were updated at least once (F012-20). Its sources are mostly its own advocates.
- **Automated reading** cuts screening work a lot, but recall varies widely by tool and setting. Summaries and citations made by AI are unreliable. The tool-maker's own figures could not be confirmed, and the only independent tests are much less favourable. No source found recommends unchecked automated reading. The joint statement of the review bodies (F012-35) and the authors of F012-26, F012-27, F012-29 and F012-31 keep people checking the output.

The evidence on cost, and on what each way catches and misses, comes almost entirely from evidence synthesis in medicine. The AI-specific sources are mostly 2025–2026 preprints.

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
- **Fact, B (F012-4, Rudyk et al. 2026, https://arxiv.org/abs/2608.24641, abstract):** Gains from structured prompting shrink or turn negative on newer GPT models but hold on Qwen. The authors say strategies must be adapted per model family and generation.
- **Fact, B (F012-5, Stanford HAI AI Index 2025, https://hai.stanford.edu/ai-index/2025-ai-index-report):** Scores on MMMU, GPQA and SWE-bench rose 18.8, 48.9 and 67.3 points in one year. Stake: low.
- **Fact, B (F012-6, Chishti et al. 2026, https://arxiv.org/abs/2604.27789):** Silent provider-side updates can introduce behavioural drift, and targeted tests in risk areas catch regressions that overall metrics miss. It is exploratory with no figures, and the authors propose their own framework (stake).

**Other library facts that bear on decay (not re-researched)**
- Q-004-F-Q004-3, moderate (B): vendor model IDs are pinned snapshots, but infrastructure updates can still change behaviour slightly.
- Q-004-F-Q004-4, moderate (B): four IDs were retired 12 to 13 months after their snapshot. One more (Sonnet 4.5) is not due to retire until 2026-11-30, about 14 months after its snapshot. The dates are tentative.
- Q-004-F-Q004-8, weak (C*): updates that raise average accuracy still cause negative flips.
- Q-009-F8-4, moderate (B), single vendor: a 32% reduction became a further 4% on a newer model.
- Q-009-F1-1, moderate (B): METR's own page says its 2025 result is out of date.

**Estimates and gaps**
- **Estimate, low confidence (mine, from F012-3 to F012-6 and the library facts above):** Findings tied to a particular model or prompt likely lose validity within months to about a year. Findings about methods (how to measure, how to check) likely last longer. No source measures either.
- **Gap:** No study measures the decay of findings about AI or agent practice. The decay rates found are from medicine (years) and Stack Overflow. They transfer at most as a lower bound on the share that is wrong at publication, not as a rate.

## 2. No deliberate review

**Cost:** nothing direct. There are no figures on what is lost.

**What it caught and missed**
- **Fact, B (F012-7, Hoffmeyer et al. 2021, https://research.regionh.dk/en/publications/most-cochrane-reviews-have-not-been-updated-for-more-than-5-years/, abstract):** 88% of Cochrane reviews first published 1996 to February 2015 had been inactive for 5.5 years or more. This happens even under an organisation whose norm is updating.
- **Fact, library moderate (B), Q-009-F5-6:** Cochrane pregnancy and childbirth reviews had a median 3.3 years to first update, and only 32.7% were updated within the recommended two years.
- **Fact, B (F012-2):** Without a review, about 80% of obsolete answers stay uncorrected.
- **Opinion:** These show that the default drifts towards "no review" even where review is the norm. They do not show what that cost the users.

**How output was checked, what worked:** not applicable, and no evidence.

**Gap:** No study of what organisations doing AI work lose by never reviewing (Input reader's gap note).

## 3. One-off review

**Cost**
- **Fact, B (F012-8, Borah et al. 2017, https://pmc.ncbi.nlm.nih.gov/articles/PMC5337708):** In a convenience sample of 195 registered reviews (192 with time data), a systematic review took a mean of 67.3 weeks (median 65.8, IQR 41.6), with a mean of about 5 authors. The abstract also gives 42 weeks for funded reviews against 26 for unfunded. These cannot be reconciled with the 67.3-week mean, and the paper leaves them unresolved, so this memo does not rely on them.
- **Estimate (the source's own), B, opened by the Source checker (F012-9, Michelson & Reuter 2019, primary paper opened by the Source checker via Europe PMC; its URL is not recorded in the check):** Each systematic review costs about $141,194.80. The primary paper reaches this figure from an economic formula, so it is an estimate, not a measured cost. The figure of about 1.72 person-years appears only on a blog relaying the paper (https://researchgold.org/blog/systematic-review-statistics): **assumed (search-only)**.
- **Opinion:** These are the costs of a full medical systematic review. A one-off scan of AI practice reading would be far smaller in scope, so the figures transfer as an upper bound only.

**What it caught and missed**
- **Fact, library moderate (B), Q-009-F13-5:** 7% of reviews were already outdated at publication, and 23% within 2 years.
- **Fact, B (F012-2):** 58.4% of obsolete answers were obsolete when posted.
- **Opinion:** A one-off review starts to decay at once.

**Gap:** No evaluation of a one-off review's yield.

## 4. Reviews on a schedule

**Practice**
- **Fact, B (F012-10, ISO/TC 211 good-practice page, https://committee.iso.org/sites/tc211/home/resolutions/isotc-211-good-practices/--systematic-review.html):** ISO international standards are reviewed every 5 years and technical specifications every 3. The committee votes to confirm, revise or withdraw, and withdrawal needs a separate ballot. The page says a third party maintains it, and its last dated entry is 2022.
- **Fact, B (F012-11, NIST AI RMF, https://airc.nist.gov/airmf-resources/airmf/5-sec-core/):** Under GOVERN 1.5, periodic reviews "are planned", and roles are defined "including determining the frequency of periodic review". The frequency is thus left to the organisation. The framework is voluntary, so this describes practice; it does not require it.
- **Fact, library weak (C), Q-005-LF-Q005-15:** Shekelle et al. recommend reassessment every 3 years.
- **Opinion, library weak (C) / opinion (M), pattern Q-005-LP-Q005-09:** Review rules on a schedule set from data.
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
- **Opinion:** A schedule fixes when review happens but not whether it is done. F012-7, library Q-009-F5-6 and, for a minority (8 of 19), F012-14 show planned cadences missed.

## 5. Reviews started by events (signals)

**What it caught and missed**
- **Fact, B (F012-15, Chung et al. 2012, https://pmc.ncbi.nlm.nih.gov/articles/PMC4141462):** An expert-plus-search method (RAND) and a literature-signal method (modified Ottawa) gave broadly similar update signals: kappa 0.64 overall, but 0.30 for one review.
  - The pilot was small and unblinded, and could not test predictive validity.
  - The authors call the judgements "largely subjective".
- **assumed (search-only) (F012-16, NICE PH13 2019 exceptional surveillance, https://www.nice.org.uk/guidance/ph13/resources/2019-exceptional-surveillance-of-physical-activity-in-the-workplace-nice-guideline-ph13-6661547533/chapter/How-we-made-the-decision):** NICE runs "exceptional surveillance" between scheduled checks when significant new evidence appears. It does not consult when it decides not to update, which leaves that decision unchecked from outside. NICE is describing itself.
- **assumed (search-only) (F012-17, OpenAI, https://openai.com/index/expanding-on-sycophancy/):** In the GPT-4o sycophancy incident, public reaction after release caught the problem. Expert testers said it "felt" off, and there was no sycophancy-specific evaluation. This is the vendor's self-report on its own failure.
- **Opinion:** An event trigger catches only what someone is watching for. F012-17 is a miss by pre-release checks, caught by an outside event.
- **Fact, B (F012-6):** Targeted risk-area tests catch what overall metrics miss. One kind of event trigger is model or provider change. Library pattern Q-004-P-Q004-1 (moderate (B), effect unmeasured) is to re-run a fixed re-check set when a role's model changes.

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

  The new trials did not change the review's results. This is the clearest cost-against-catch evidence in the record, for one review.
- **Fact, B (F012-22, Simpson et al. 2004, https://www.cambridge.org/core/journals/international-journal-of-technology-assessment-in-health-care/article/assessing-the-accuracy-of-forecasting-applying-standard-diagnostic-assessment-tools-to-a-health-technology-early-warning-system/70CDD85E14DDBF0DEE69A99B43FCF92A, abstract):** The UK horizon-scanning early-warning system had 71% sensitivity, 73% specificity and 14% positive predictive value, so 86% of its positive predictions were not borne out. The gold standard was imperfect.
- **Fact, B (F012-23, Bouwman et al. 2020, https://www.usenix.org/conference/usenixsecurity20/presentation/bouwman):** Two commercial threat-intelligence feeds had an average overlap of only 2.5–4.0% in their indicators. The study examined 22 threat actors; the page does not show whether the overlap figure is limited to them. Shared indicators appeared about a month later in the other feed. Customers judge feeds by informal heuristics, not measured coverage.
- **Opinion:** Any one outside feed covers only part of what exists.

**Gap:** No figures for the cost of producing a living review or guideline. Packer 2012 (10 years of horizon scanning) gave no results in its abstract.

## 7. How the reading, choosing and summarising is done: people, tools, or both

**Choosing: screening and search**
- **Fact, B (F012-24, Thomas et al. 2021, https://pmc.ncbi.nlm.nih.gov/articles/PMC8168828):** Cochrane's RCT classifier, set to 99% recall, found 99.5% of 44,007 RCTs. Counting records with too little text, it found 93.8%. Precision was about 8%, and it cut manual screening by 40–70% in pilots. Stake: the authors built and deploy the tool.
- **Fact, B (F012-25, Callaghan & Müller-Hansen 2020, https://pmc.ncbi.nlm.nih.gov/articles/7700715):** Earlier stopping rules for machine-prioritised screening gave inconsistent recall. A statistical stopping rule kept recall reliable but saved only about 17% of work. Stake: the authors propose the rule.
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
- **Elicit: the tool-maker's own figures are unconfirmed, and independent tests are much less favourable.**
  - **Fact, B (F012-29, Lau & Golder 2025, https://pmc.ncbi.nlm.nih.gov/articles/PMC12483133/):** Elicit's search sensitivity averaged 39.5% (25.5–69.2%), against 94.5% for traditional searching. The authors recommend it only as a supplement. No conflicts declared.
  - **assumed (search-only) (F012-30, Elicit's own blog, https://elicit.com/blog/how-we-evaluated-elicit-systematic-review):** Search extracts attribute to Elicit claims of 94% correct screening and 94–99% extraction accuracy. The Source checker opened the page but did not find these figures in it, so they are not confirmed. Stake: Elicit sells the product.
  - Even if confirmed, these figures measure different tasks (screening and extraction accuracy, not search sensitivity), so they would not be a head-to-head contradiction. The only independent tests found are much less favourable.

**Extracting and summarising**
- **Fact, B (F012-31, Lagisz et al. 2025, preprint, https://ecoevorxiv.org/repository/view/9909/):** Elicit's extracted values agreed 90%, but its supporting quotes matched only 46% and its reasoning 30%. In high-accuracy mode these fell to 10% and 0%. The authors say it complements but does not replace human extractors.
- **Fact, B (F012-32, Peters & Chin-Yee 2025, https://arxiv.org/abs/2504.00025v1, abstract):** LLM summaries of science overgeneralised in 26–73% of cases; this range covers DeepSeek, ChatGPT-4o and LLaMA 3.3 70B. The odds of broad generalisation were nearly 5 times those of human summaries (odds ratio 4.85, CI 3.06–7.70). The page says this held for most LLMs, that prompting for accuracy did not remove it, and that newer models "tended to" do worse.
- **Fact, B (F012-33, DeepTRACE 2025, https://arxiv.org/abs/2509.04499):** Deep-research and generative-search systems made many statements their listed sources do not support, with citation accuracy of 40–80% across systems. The authors' affiliation (possibly Salesforce, a stake) is unconfirmed.
- **Fact, B (F012-34, Rao et al. 2026, https://arxiv.org/abs/2604.03173):** 3–13% of citation URLs from LLMs and deep-research agents were hallucinated, and 5–18% did not resolve. A URL checker cut non-resolving links to under 1%. Stake: the authors release the checker.

**How output is checked**
- **Fact, B (F012-35, Cochrane / Campbell / JBI / CEE joint statement 2025, https://pmc.ncbi.nlm.nih.gov/articles/PMC12594113/):** The statement says reviewers should keep human oversight and author accountability, demonstrate that tools are sound, and report AI use in full. It uses "must" only for tool developers. The bodies set norms for their own field.
- **Fact, library moderate (B), Q-009-F10-3 (single vendor):** Human evaluation caught agents choosing content farms over authoritative sources.

**Opinion:** Across F012-24 to F012-35, no source found recommends unchecked automated reading. The common design in the record has a tool rank or screen for recall, and people verify inclusion and any claim that changes a conclusion. Summaries and citations are the weakest automated steps.

**Gaps**
- No head-to-head comparison of people, tools and both for keeping up, beyond F012-21 and the screening studies.
- Nothing measured on keeping up with outside practice in software or AI.
- Practitioner accounts (Husain and others) were seen only secondhand.

**Transfer.** Opinion. The screening tools were tested on biomedical abstracts with structured study designs. Outside AI practice comes mostly from vendor posts, preprints and blogs, without such structure. Recall figures (F012-24, F012-27) are therefore unlikely to hold as given. The failures in summaries and citations (F012-32 to F012-34) are general to LLMs and transfer more directly.

## What each answer would change (as the question frames it; no choice made here)

- **Shelf life.** Which kind of review fits depends on how long findings last. No source settles it.
  - If model- and prompt-tied findings last months, as the indirect AI evidence suggests (estimate), that favours frequent review, or review triggered by model and provider changes.
  - If findings last years, as the medical evidence from a different field suggests, that favours infrequent review or none.
  - If the two classes of finding differ, different shelf lives per class may be needed.
- **Who or what does each step.**
  - Evidence that tools can screen with high recall and cut work supports tools at the ranking and screening step. That evidence is F012-24, at a 99% recall setting, and F012-27, whose sensitivity ranged 58–100% across runs; F012-28 is search-only.
  - Evidence that tools search poorly (F012-29), extract unsupported quotes (F012-31), overgeneralise (F012-32) and mis-cite (F012-33, F012-34) supports people at the search, summary and claim-checking steps, or a check placed after each of those steps.
  - Independent tests of Elicit (F012-29, F012-31) are much less favourable than the tool-maker's own figures, which are unconfirmed (F012-30). This bears on whether vendor figures can set where checks sit.
- **Where checks sit.** The failures found are concentrated in summarising, citation and partial coverage by any one feed (F012-23). The joint statement (F012-35) says human oversight should run across all steps.
- **What is affordable.**
  - A full one-off review takes a mean of about 67 weeks with about 5 authors, an upper bound (F012-8).
  - Continuous intake costs 5 minutes to 32 hours a month per review (F012-18), up to 11 FTE in a crisis (F012-19).
  - Cheap alerts cost 5–9 hours a year but miss 3 of 4 new trials (F012-21).
  - Living reviews need considerable resources (library Q-009-F13-6). In one pilot, some teams slowed their cadence or dropped the automation (F012-18).
  - Scheduled and event-triggered review have no cost evidence at all.

## Questions I add (not closed)

1. What is the measured rate at which the portfolio library's own entries are overturned or found stale on re-check, by type of entry (model-tied against method)? This is the local shelf-life evidence the outside record lacks.
2. What do Newberry 2013 (AHRQ surveillance cost and yield) and NICE PMG20/PMG49 report on the cost and yield of scheduled against priority-based surveillance? They were blocked this time.
3. Is there any measured evaluation of how software or AI practitioners or firms (Radar-style boards, engineering blogs, evaluation teams) keep their practice current, with cost and misses?

## Sources needed that were not gathered (gaps for the Input reader)

- Newberry 2013.
- NICE PMG20 and PMG49 full text.
- Garner 2016 (BMJ update checklist).
- The FAA airworthiness-directive rules.
- The OpenAI sycophancy postmortem (opened).
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
4. Gains from structured prompting shrink or turn negative on newer GPT models but persist on Qwen, so strategies must be adapted per model family and generation (Rudyk 2026) | fact | B | 12 months
5. MMMU, GPQA and SWE-bench scores rose 18.8, 48.9 and 67.3 points within a year of introduction (AI Index 2025) | fact | B | 2 years
6. Silent LLM updates can introduce drift, and targeted risk-area tests catch regressions that overall metrics miss (Chishti 2026; exploratory; the authors' own framework) | fact | B | 12 months
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
19. Earlier stopping rules for prioritised screening gave inconsistent recall, and a statistical rule kept recall reliable while saving about 17% (Callaghan 2020) | fact | B | 5 years
20. LLM screening sensitivity varied by model and configuration (a GPT-4o mini configuration 56.2%, a Llama 3 70B configuration 77.5%), and manual validation remains necessary (López-Pineda 2025) | fact | B | 12 months
21. GPT-4o screening in a living review excluded no finally-included study in single-pass runs, with one erroneous exclusion in 730 repeated-run decisions; it cut simulated workload 79–86% and needs human oversight (Homiar 2025) | fact | B | 12 months
22. Independently tested, Elicit's search sensitivity averaged 39.5% against 94.5% for traditional searching (Lau & Golder 2025) | fact | B | 12 months
23. Elicit's supporting quotes and reasoning matched only 46% and 30%, falling to 10% and 0% in high-accuracy mode (Lagisz 2025, preprint) | fact | B | 12 months
24. Summaries of science by DeepSeek, ChatGPT-4o and LLaMA 3.3 70B overgeneralised in 26–73% of cases, with nearly 5 times the odds of human summaries (OR 4.85); per the page this held for most LLMs, and newer models tended to do worse (Peters & Chin-Yee 2025) | fact | B | 2 years
25. Citation accuracy of deep-research and generative-search systems ranged 40–80% (DeepTRACE 2025) | fact | B | 12 months
26. 3–13% of citation URLs from LLMs and deep-research agents were hallucinated, and URL checking cut non-resolving links to under 1% (Rao 2026; the authors' own tool) | fact | B | 12 months
27. The Cochrane, Campbell, JBI and CEE joint statement says reviewers should keep human oversight and accountability, demonstrate tool soundness and fully report AI use | fact | B | 3 years
28. NICE replaced fixed 5-year surveillance with priority-based surveillance and exceptional reviews on significant new evidence | fact | assumed (search-only) | 3 years. Not to be filed until someone opens the NICE page.
29. A cheap alert found 1 of 4 new trials in the one test found, and any one outside feed covers only part of what exists; pair a cheap alert with a periodic fuller search and measure what each finds (origin F012-21, F012-23) | pattern | opinion built on B sources | 3 years
30. Let tools rank and screen for recall; have people verify each summary, quote and citation that a decision rests on (origin F012-24 to F012-35, excluding the unopened F012-28 and F012-30) | pattern | opinion built on B sources | 12 months

## Finding ids relied on

F012-1 to F012-35. Search-only or unconfirmed, staying assumed and out of the library: F012-13, F012-16, F012-17, F012-28, F012-30, the blog-only 1.72 person-years in F012-9, and the workload tie and advice in F012-20. Library entries cited: Q-005-LF-Q005-15, Q-005-LP-Q005-09, Q-009-F5-3, Q-009-F5-6, Q-009-F5-8, Q-009-F13-5, Q-009-F13-6, Q-004-F-Q004-3, Q-004-F-Q004-4, Q-004-F-Q004-8, Q-004-P-Q004-1, Q-009-F1-1, Q-009-F8-4, Q-009-F10-3.

Points for the Source checker:
- "Answer in brief": the no-review, event-triggered, continuous-intake and automated-reading bullets are restated to the sources named in round 2's corrections 1–5.
- F012-22: "most items did not matter" is replaced by the arithmetic from the 14% positive predictive value (86% not borne out).
- F012-23 and entry 17: the overlap is no longer tied to the 22 actors.
- F012-31 and entry 23: "across accounts" is dropped.
- F012-1 and entry 1: "updated in 2009".
- F012-9: the cost is now cited to the primary (opened via Europe PMC), and the blog only for the 1.72 person-years. The primary's URL is not in the check record, so I could not give it.
- Pattern 29: reworded and F012-22 dropped as an origin, in line with the filed P1.

## Tokens

My token count is not visible to me.

---

## Change list (item: what changed, and the correction it answers)

1. **"Answer in brief", continuous intake bullet:** I replaced "every evaluation found reports heavy workload and drop-off" with the two workload evaluations (F012-18, F012-19) and the 35% update rate (F012-20, figures only). I replaced "catches new evidence earliest" with "found new evidence earliest in the one test found, for a single review (F012-21)". Round 2 corrections 1 and 4.
2. **"Answer in brief", automated reading bullet:** I replaced "Every standards body and study author found keeps people checking" with the section 7 opinion ("no source found recommends unchecked automated reading"), and named only the supported sources: F012-35 and the authors of F012-26, 27, 29 and 31. Round 2 correction 2.
3. **"Answer in brief", event-triggered bullet:** I dropped "cheaper" and added "has no cost figures". F012-15 is now described as a pilot of two signal methods, not a comparison with scheduled review. Round 2 correction 3.
4. **"Answer in brief", no-review bullet:** it is now marked as opinion, and "decay goes unnoticed" is dropped. It now cites the shares the sources give (about 80% never updated, F012-2; 88% inactive, F012-7). Round 2 correction 5.
5. **F012-22 (section 6):** "Most items it flagged did not matter" became "86% of its positive predictions were not borne out" (100 − 14). Round 2 correction 6.
6. **Pattern 29 (knock-on from item 5):** "A cheap alert finds little of what matters" became "found 1 of 4 new trials in the one test found", plus the partial-coverage point. F012-22 is dropped as an origin, because after item 5 it no longer supports "what matters". This also matches the filed P1. Mark unchanged (opinion built on B sources). Follows from round 2 correction 6.
7. **F012-31 and entry 23:** "across accounts" is dropped. Round 2 correction 7.
8. **F012-1 and entry 1:** "re-rated" became "updated". Round 2 correction 8.
9. **F012-23 and entry 17:** "for 22 shared actors" / "on shared actors" became an average overlap "in their indicators". The line now notes that the study examined 22 actors, and that it is not shown whether the overlap is limited to them. Round 2 correction 9.
10. **"What each answer would change", affordability:** "Living efforts stall without dedicated resources" became "need considerable resources (Q-009-F13-6)", with the F012-18 note that some teams slowed their cadence or dropped the automation. Round 2 correction 10.
11. **"What each answer would change", who does each step:** "tools screen with high recall" became "can screen with high recall". It is now qualified by F012-24's 99% recall setting and F012-27's 58–100% sensitivity range. Round 2 correction 10.
12. **F012-9:** this is now cited to the Michelson & Reuter 2019 primary, opened by the Source checker via Europe PMC. The blog URL is kept only for the blog-only 1.72 person-years. The "Sources needed" line for Michelson & Reuter now asks only for the primary's URL, which is not recorded in the check. Round 2 correction 11.
13. **Header italic line, "Points for the Source checker" and this change list:** these replace round 2's versions. The previous round's change list is in the file's history.

No mark changed apart from those above. The opening answer changed only as listed in items 1–4.

## Finding ids for the Source checker to re-check

- **Findings:** F012-1, F012-9, F012-22, F012-23, F012-31. Also the "Answer in brief" bullets, as they rely on F012-2, 7, 15, 18, 19, 20, 21, 26, 27, 29, 31 and 35.
- **"What each answer would change":** the affordability and who-does-each-step lines, which rely on F012-18, F012-24, F012-27 and library Q-009-F13-6.
- **Proposed entries 1, 17 and 23, and pattern 29:** check them against the filed Q-012-1, Q-012-17, Q-012-23 and P1 in /home/user/lib-q-012.

## Tokens

I cannot see my token count.
