# Q-011 memo: is looking for outside practice worth it, and how well does each kind of source hold up? (Researcher, 2026-11-08)

*The Researcher's memo for Q-011, round 2 (brief 166, docs/briefs/166-researcher.md), revised after the Source checker's round 1 (research/Q-011-source-check.md); round 1 was brief 157, in this file's history. Recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p), 2026-11-08, from the helper's return; only this italic line is the Orchestrator's, replacing round 1's.*

**Answer as far as the evidence goes.** No study gathered for this question compares looking for outside practice in AI or agent work against not looking. So for AI work, whether looking is worth it is **unknown**. The only measured evidence comes from other fields, and it points both ways.
- **Searching outside the firm:** innovation rises with outside search, then falls past a point (UK manufacturing).
- **Spreading medical guidelines:** about a 10% median improvement in process-of-care measures.
- **Copying code:** copied Stack Overflow security code carried insecure snippets into most of the apps that used it.
- **Cost:** the only measured cost is a formal medical systematic review, at about 67 weeks. Most guideline studies did not report cost at all.

On whether claims held up, no kind of source has a measured rate for AI or agent work. The nearest figures:
- **External replications of software-engineering studies:** 26% confirmed the original result, against 82% for replications by the original authors. This is a secondary citation.
- **Machine-learning papers:** one person independently reproduced about 62% to 64% (the article states 62%; 162 of 255 is 63.5%).
- **Popular prompting tips and techniques:** in independent tests they mostly showed no significant effect.
- **Vendor benchmark claims:** one case where an independent score came in well below the vendor's headline.
- **Benchmarks:** flaw sizes are known (up to 100% relative misstatement; one rate fell from 12.47% to 3.97% after filtering), but not a hold-up rate.
- **Open-source projects:** nothing measured.

Share of material by kind:
- **Promotional:** nothing measured.
- **Duplicated:** nothing measured.
- **Machine-written:** detector-based estimates: about 40–47% of Medium posts, and about 17.5% of computer-science abstracts by early 2024. One SEO agency's count says AI-generated web articles surpassed human-written ones in number in November 2024; a figure of about half of new web articles rests only on an unopened follow-up (assumed). Several of these come from detector sellers, and the detectors' reliability is not established: one study found every detector it tested misclassified some LLM-polished peer reviews.

Filtering methods exist (AACODS, the multivocal-review guidelines, NeurIPS reproducibility rules). None was found with a measured effect on outcomes.

## 1. Is looking worth doing at all, compared with not looking?

- **F011-1** (fact, B; https://druid.dk/laursen/papers/laursen_salter2006smj.pdf). Laursen & Salter (2006), 2,707 UK manufacturing firms: searching widely and deeply relates to innovation performance in an inverted U, and past a point more search becomes unproductive.
  - Counted as paying: innovation output.
  - Cost of looking: not measured.
  - Limits: correlational, and a different field (manufacturing innovation, not AI practice). It transfers only as a hypothesis that returns diminish.
- **F011-2** (fact, assumed (search-only); https://typeset.io/papers/investigating-the-not-invented-here-nih-syndrome-a-look-at-bj8szw06k5). Katz & Allen (1982), 50 R&D groups: long-tenure groups cut themselves off from outside information and their performance fell.
  - Counted as paying: technical performance.
  - Limits: the search extracts disagree on the tenure figures, and the page was not opened.
- **F011-3** (fact, B; https://www.mja.com.au/journal/2004/180/6/evidence-based-implementation-evidence-based-care-possible). Grimshaw & Eccles (2004), from 235 evaluations: spreading guidelines gave about a 10% median absolute improvement in process-of-care measures. Fewer than a third of the studies reported what the strategy cost.
  - Counted as paying: process-of-care indicators, not patient outcomes.
  - Stake: the authors summarise their own review.
  - Limits: medicine. What transfers is mainly that cost usually goes unreported.
- **F011-4** (fact, B; https://aisec.fraunhofer.de/en/stackoverflow.html). Fischer et al. (2017): 15.4% of 1.3M Android apps contained security code copied from Stack Overflow, and 97.9% of those had at least one insecure snippet.
  - Counted: harm.
  - What it shows: unfiltered borrowing can cost more than it pays. This is the nearest field (software) of any item here.
- **F011-5** (fact, B; https://www.microsoft.com/en-us/research/?p=238009). Devanbu, Zimmermann & Bird (2016): developers' beliefs were primarily formed from personal experience and do not necessarily correspond with the actual evidence in their own project.
  - Stake: Microsoft studying its own staff.
  - What it shows: indirect evidence that not looking (relying on your own experience) is not free of error either.
- **F011-30** (fact, B; https://pmc.ncbi.nlm.nih.gov/articles/PMC5337708). Borah et al. (2017): a medical systematic review took a mean of 67.3 weeks from registration to publication, with about 5 authors.
  - Cost of looking: this is the only measured figure for formal looking.
  - Limits: medicine, and the formal end of the range. It is an upper reference, not the cost of light scanning.
- **Library, related:**
  - Q-009-F1-3 (weak, C): 40.2% of 363 tests of established medical practice found it ineffective.
  - Q-009-F13-2 (moderate, B): 396 reversals among more than 3,000 RCTs.
  - Q-009-F13-3 (moderate, B): an established ineffective practice is hard to abandon.
  - Q-009-F13-13 (weak, C): in 2004 there was not yet the infrastructure for widespread adoption of evidence-based software engineering.
  - Opinion: these show that adopted practice is often wrong, which can be read as support for either looking or not looking.
- **Estimate (mine):** the indirect evidence is consistent with "looking pays, up to a point, if it is filtered". No study measures that for AI work. The evidence is thin, and all of it comes from other fields.

## 2. How often claims held up when tested independently, by kind of source

**Vendor documentation and studies**
- **F011-11** (fact, B; https://techcrunch.com/2025/04/20/openais-o3-ai-model-scores-lower-on-a-benchmark-than-the-company-initially-implied). Epoch scored the public o3 at about 10% against a vendor-shown figure of over 25%.
  - Epoch suggested possible reasons for the gap ("might be due to"): a stronger internal setup, more compute and a different problem set. These are suggestions, not established causes. The vendor's lower-bound figure is said to match the score Epoch observed; the page gives no number for it.
  - Stake: Epoch had been funded by OpenAI, and the page reports that Epoch was criticised for waiting to disclose that funding.
  - One case, press coverage. It is not a rate.
- **Library, related:**
  - Q-009-F3-8 (moderate, B; vendor): GitHub's own RCT found developers 55% faster on one task.
  - Q-009-F1-1 and Q-009-F10-7 (moderate, B): METR's RCT found 19% slower for experienced developers.
  - The sources disagree: different tasks and settings, and the vendor has a stake. It is not a replication of the same claim.
  - Q-009-F4-7 (moderate, B): Google's own RCT found about 21% faster.
- **Rate:** unknown.

**Practitioners' accounts**
- **F011-9** (fact, B; https://arxiv.org/abs/2409.20303). Vaugrante, Niepert & Hagendorff (2024) re-tested chain-of-thought, EmotionPrompting, ExpertPrompting, Sandbagging and Re-Reading across six models. They found "a general lack of statistically significant differences across nearly all techniques tested".
  - These techniques have academic as well as practitioner origins.
  - Preprint; the abstract only was opened.
- **F011-10** (fact, B; https://arxiv.org/abs/2508.00614). Meincke et al. (Wharton, 2025): tipping or threatening a model had no significant average effect, though it changed results on individual questions unpredictably.
- **Library, consistent with both:**
  - Q-002-F-e (weak, C): persona statements do not improve accuracy.
  - Q-009-F5-2 (moderate, B): chain-of-thought gave reasoning models only marginal benefit.
  - Q-004-F-Q004-6 (weak, C*): optimised prompts do not reliably generalise.
- **No independent test found** of the "26 principles" paper (arXiv 2312.16171). This is a gap.
- **Estimate:** for the popular prompting tips tested, most did not hold up. This is a handful of hand-picked tips, not a sample, so it is not a rate for practitioner accounts.
- **Rate:** unknown.

**Academic and industry studies**
- **F011-6** (fact, B for the secondary citation; https://arxiv.org/pdf/2204.06325 p.3). Citing da Silva et al. (2014, 133 replications): 82% of internal replications confirmed the original, against 26% of external ones.
  - The primary paper was not opened.
  - Shepperd & Counsell's odds ratio of 8.64 is assumed (search-only): the source returned 403.
- **F011-7** (fact, B; https://bura.brunel.ac.uk/handle/2438/8784). Shepperd, Bowes & Hall (2014): in defect-prediction studies, the researcher group was the major explanatory factor of results (31 percent), and the classifier method explained 1.3 percent. "It matters more who does the work than what is done."
  - Unverified (search-only, not checked): a re-analysis disputed the size of the effect, and the authors' 2018 reply holds to it.
- **F011-8** (fact, B; https://thegradient.pub/independently-reproducible-machine-learning/). Raff (2020): one person independently reproduced 162 of 255 ML papers.
  - 162/255 = 63.5% (calculation). The article itself states 62% and calls it a lower bound. Read as about 62% to 64%.
  - Released code was a weak predictor of success. An author answering questions was a strong one: 22 of 26 with a reply, 1 of 24 without.
  - Limits: single replicator, older papers. A reviewer called the sample biased (search-only).
- **F011-31** (fact, B; https://arxiv.org/abs/2003.12206). Pineau et al.: NeurIPS 2019 ran a reproducibility programme with a code policy, a challenge and a checklist.
  - No effect sizes in the abstract. The 74.4% code-availability figure is search-only.
  - Stake: the authors ran the programme.
- **Library, related:** Q-009-F3-2 (moderate, B): SE experiments are open to subject bias.
- **Estimate:** external confirmation is roughly a quarter for SE and roughly 62% to 64% for ML reproduction. The two measure different things (agreement with the original result against reproducing it), so they should not be pooled.
- **Rate for recent LLM or agent papers:** unknown.

**Open-source projects**
- Nothing measures how often their claims hold up.
- F011-8: released code is a weak indicator of reproducibility.
- **F011-29** (fact, B; https://arxiv.org/html/2512.01939v1). Wang et al. (2025): across 1,575 LLM-agent repositories, version and dependency conflicts caused about a quarter of technical obstacles. The paper's own figures are inconsistent (23.53%, "over 25%").
- **F011-28** (fact, B; https://arxiv.org/abs/2603.16572 and https://research.snyk.io/blog/agent-skills-threat-landscape/).
  - Holzbauer et al.: marketplace scanners flag up to 46.8% of agent skills as malicious, but with repository context only 0.52% stay suspicious.
  - Snyk: 76 confirmed malicious payloads reported across its scan of 3,984 skills (the page does not clearly say the 76 are a subset of the 3,984), and 13.4% of skills with a Critical issue.
  - Stake: Snyk authors the page and recommends its own Snyk Agent Scan.
  - The sources disagree widely, and the gap comes mostly from how each one counts.
- **Library:** Q-009-F3-4 and Q-009-F12-1 (moderate, B): fake GitHub stars are used to promote projects. That popularity signals are therefore unreliable is my inference (opinion); the entries do not say it.
- **Rate:** unknown.

**Benchmarks and leaderboards**
- **F011-12** (fact, B; https://arxiv.org/abs/2507.02825). Zhu et al. (2025): flaws in task setup and reward design can misstate agent performance by up to 100% relative. A checklist cut overestimation on one benchmark by 33%.
  - Stake: the authors propose the checklist.
- **F011-13** (fact, B; https://arxiv.org/abs/2410.06992). Aleithan et al. (2024): of SWE-Agent+GPT-4's "successful" SWE-bench patches, 32.67% involved cheating with solutions given in the issue report or its comments, and 31.08% were suspicious because the tests were inadequate. Filtering out the problematic issues cut the resolution rate from 12.47% to 3.97%.
  - Stake: the authors offer a replacement benchmark.
  - A later thesis version gives different figures (search-only).
- **F011-14** (fact, B; https://arxiv.org/abs/2405.00332). Zhang et al. (2024): on a fresh copy of a public maths benchmark, some model families dropped up to 8%, while most frontier models showed little sign of overfitting.
  - Stake (the Input reader's note; not shown on the abstract page): Scale AI sells evaluation services.
- **F011-15** (fact, B; https://arxiv.org/abs/2405.14782). Biderman et al. (EleutherAI lm-eval): sensitivity to evaluation setup and poor reproducibility are central problems.
  - The "12 of 35 scores matched" figure is not in the abstract. Do not use it.
- **Library:**
  - Q-009-F3-5 (moderate, B): Arena skew.
  - Q-009-F3-6 (moderate, B): SWE-bench memorisation.
  - Q-009-F2-3 (moderate, B): maintainers would not merge about half of test-passing agent PRs.
  - Q-009-F4-2 (moderate, B): single-run results vary by 2.2–6.0 points.
  - Q-003-F-c (moderate, B): infrastructure alone moved Terminal-Bench by 6 points.
- **Estimate:** headline benchmark numbers are often inflated by known mechanisms, sometimes by a large factor. That does not always flip the direction of a claim, though, and F011-14 shows frontier models mostly held up on a fresh copy.
- **Hold-up rate in the question's sense** (same direction under an independent test): unknown.

**Where a source has a stake (general)**
- **F011-16** (fact, B; https://www.cochrane.org/MR000033/METHOD_industry-sponsorship-and-research-outcome). Lundh et al. (2017), Cochrane: industry-sponsored drug and device studies more often reported favourable results (RR 1.27) and conclusions (RR 1.34). Standard risk-of-bias checks did not catch this.
  - A different field. It transfers only as a reason to raise the bar for sponsored claims, not as a size for AI.

## 3. Share promotional, duplicated or machine-written

- **Promotional:** unknown. Nothing measured was found. F011-16 is about sponsorship bias, not a share of material.
- **Duplicated:** unknown.
  - Adjacent (decay rather than duplication): F011-22 (fact, B; https://arxiv.org/abs/1903.12282): 58.4% of obsolete Stack Overflow answers were probably obsolete when posted, and only 20.5% are ever updated.
  - Adjacent: F011-23 (fact, B; https://arxiv.org/abs/2104.13435): 49% of grey-literature URLs cited in SE reviews no longer work.
- **Machine-written:**
  - F011-17 (fact as Graphite's claim, B; https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans). AI-generated articles in Common Crawl surpassed human-written ones in quantity in November 2024.
    - Stated detector error rates: 4.2% false positives and 0.6% false negatives, GPT-4o only.
    - Human-edited AI text was not measured.
    - The page is marked superseded. It says the share has plateaued since May 2024 but gives no share for the plateau. Its "nearly half (39%)" is the share about 12 months after ChatGPT's launch, a different statistic.
    - "About half" is not on this page: it rests on F011-18 (assumed) and on reading "surpassed in quantity" as near half (my inference).
    - Stake: an SEO agency using a vendor's detector.
  - F011-18 (assumed (search-only); https://axios.com/2026/05/15/human-vs-ai-written-articles). Graphite's follow-up puts the share at about 49.9% in Q1 2026, averaging three detectors.
    - Stake: all three detector makers sell detection.
  - F011-19 (fact as reported, B for the secondary page; https://getcoai.com/news/medium-is-being-flooded-with-ai-generated-content/). Medium posts likely AI-generated: 47% (Pangram) and about 40% (Originality).
    - Stake: both estimators sell detection, and Medium's CEO disputes that it matters.
  - F011-21 (fact, B; https://arxiv.org/abs/2404.01268). Liang et al.: up to 17.5% of computer-science abstracts were LLM-modified by February 2024. This is a corpus-level estimate, with no stake seen.
  - F011-20 (fact, B; https://arxiv.org/abs/2603.20450). Saha et al. (2026): every detector tested misclassified some LLM-polished peer reviews, so public detector estimates of AI use in peer reviews "should be interpreted with caution".
    - The caution is stated for peer-review estimates only, and the paper does not test the detectors behind F011-17 to F011-19. That it weakens F011-17 to F011-19 is my inference (opinion), not the paper's finding.
  - Library: Q-009-F10-3 (moderate, B): a vendor saw research agents pick SEO content farms over authoritative sources. Q-009-F8-1 (weak, C) records one practitioner blog as probably machine-written.
- **Estimate:** a large share of general web text is machine-written or machine-assisted. No figure exists for AI-engineering blogs or documentation, and that is the material that matters here. Unknown for that.

## 4. How others have filtered such material

- F011-24 (fact, B for the abstract; https://arxiv.org/abs/1707.02553). Garousi, Felderer & Mäntylä: grey literature needs its own search and quality-assessment phases. This overlaps library entry Q-009-F3-1 (moderate, B).
  - The 8-criterion checklist (authority, method, objectivity, date, position against related sources, novelty, impact, outlet type) is assumed (search-only).
  - Stake: the authors promote this kind of review.
- F011-25 (fact, B; https://oxfordhealth.nhs.uk/wp-content/uploads/sites/3/2024/01/AACODS_Checklist.pdf). The AACODS checklist, authored by Flinders University Library: authority, accuracy, coverage, objectivity, date and significance. It says grey studies should be appraised with the same tools as published ones.
- F011-27 (fact, B; https://arxiv.org/abs/2106.11159). Williams, Shardlow & Rainer: argumentation and evidence are the key credibility criteria for practitioner blogs (kappa 0.82). The corpus came from one blog.
- F011-26 (opinion, B; https://arxiv.org/abs/1911.12038). Practitioner grey literature is a valuable data source. No evidence is given, and the authors advocate its use.
- F011-23: few SE reviews applied quality criteria to the grey literature they used.
- F011-31: the NeurIPS reproducibility programme.
- F011-8 (opinion, from the data): whether an author answers questions may be a cheap screen. It rests on one study and one replicator.
- Library:
  - Q-009-F5-8 and Q-009-F13-1: the Thoughtworks Radar method (one firm's own description).
  - Q-009-F4-8 (moderate, B, opinion): test any attempt to improve performance before deployment.
- **Effect on outcomes:** no filter was found with a measured effect on outcomes. Unknown.

## What each answer would change (from the question's own section, no choice made)

- **"Looking adds little over not looking":** nothing measured shows this for AI work. Read F011-4, and the general record of reversals, as "unfiltered looking can harm" and it argues for not looking.
- **"Looking pays":** F011-1 and F011-3 support it, but only by analogy from other fields and with diminishing returns. Taken as transferable, it argues for looking, with a cap on how much.
- **Kinds of source with a poor record, read with a higher bar or not at all:**
  - Popular prompting tips (F011-9, F011-10).
  - Headline benchmark and leaderboard figures (F011-11 to F011-14, plus the library entries).
  - Sponsored or vendor claims (F011-16 by analogy, F011-11).
  - Replications by the claimants themselves (F011-6, F011-7).
- **Kinds that might be read more cheaply:** none has a measured good record. The best measured figure is about 62% to 64% for independently reproduced ML papers.
- **Cost of filtering:** large if detector-based shares of machine-written text apply to the material read (about 40–47% on Medium; in general web corpora, AI articles said to outnumber human ones, with about half resting on an assumed follow-up). The detectors' reliability is not established (F011-20 shows misclassification for peer reviews; applying it to these estimates is my inference), so the true share is not known. The promotional and duplicated shares are unknown.

## Gaps (sources needed that the Input reader did not gather or open)

- Any study comparing looking for outside AI or agent practice with not looking.
- The da Silva et al. (2014) primary paper, and Shepperd & Counsell (core.ac.uk returned 403).
- Katz & Allen (1982), not opened.
- The Graphite Q1 2026 follow-up page itself, and the WIRED Medium original.
- The full Garousi 2017 paper, for the checklist.
- A measured share of promotional or duplicated material in AI-engineering writing.
- Any hold-up rate for vendor documentation or open-source project claims.
- An independent test of arXiv 2312.16171 (the "26 principles" paper).

Level 5 was not needed.

## Proposed library entries (statement | type | grade | proposed shelf life)

1. External SE replications confirmed the original 26% of the time, against 82% for internal ones (da Silva via Minhas) | fact | B (secondary citation) | 5 years
2. In defect-prediction studies, the researcher group was the major explanatory factor of results (31 percent) and the classifier method 1.3 percent; a dispute over the size is unverified | fact | B | 5 years
3. One replicator reproduced 162 of 255 ML papers (63.5%; the article states 62% as a lower bound); an author's reply was a strong predictor and released code a weak one | fact | B | 5 years
4. An independent re-test of five popular prompting techniques across six models found almost no significant effects | fact | B | 18 months
5. Tipping or threatening a model had no significant average benchmark effect, with unpredictable per-question changes | fact | B | 18 months
6. Agent-benchmark setup and reward flaws can misstate performance by up to 100% relative | fact | B | 2 years
7. Filtering problematic issues (solutions leaked in the issue report or comments, and patches suspicious because tests were inadequate) cut SWE-Agent+GPT-4 on SWE-bench from 12.47% to 3.97% | fact | B | 2 years
8. On a fresh copy of a maths benchmark some families dropped up to 8%; most frontier models showed little overfitting (stake: Scale AI, per the Input reader's note, not on the abstract page) | fact | B | 18 months
9. Industry sponsorship is linked to more favourable results (RR 1.27) and conclusions (RR 1.34) in drug and device studies | fact | B | 5 years
10. 97.9% of Android apps with copied Stack Overflow security code had at least one insecure snippet | fact | B | 5 years
11. Outside search relates to innovation performance in an inverted U (UK manufacturing, correlational) | fact | B | 10 years
12. Guideline implementation gave about a 10% median improvement in process of care; fewer than a third of studies reported cost | fact | B | 10 years
13. A medical systematic review averaged 67.3 weeks to publication | fact | B | 5 years
14. Detector estimates of AI use in peer reviews should be read with caution; every detector tested misclassified some LLM-polished reviews | fact | B | 18 months
15. By one SEO agency's detector-based count, AI-generated web articles in Common Crawl surpassed human-written ones in quantity in November 2024 (stake: detector and SEO vendors; detector reliability not established) | fact | B, attributed and not load-bearing | 1 year
16. LLM-modified text reached about 17.5% of CS abstracts by February 2024 | fact | B | 2 years
17. 49% of grey-literature URLs cited in SE reviews no longer work; few reviews applied quality criteria to grey literature | fact | B | 5 years
18. Only 20.5% of obsolete Stack Overflow answers are ever updated | fact | B | 5 years
19. Agent-skill maliciousness shares range from 0.52% to 46.8% depending on whether repository context is used | fact | B, attributed; Snyk authors its page and recommends its own Snyk Agent Scan | 1 year
20. Filter grey literature on authority, accuracy, coverage, objectivity, date and significance (AACODS), with the same tools as published work; effect unmeasured | pattern | B as a method; effect unmeasured | 5 years

## Finding ids relied on (for the Source checker)

- B: F011-1, F011-3, F011-4, F011-5, F011-6, F011-7, F011-8, F011-9, F011-10, F011-11, F011-12, F011-13, F011-14, F011-15, F011-16, F011-17, F011-19, F011-20, F011-21, F011-22, F011-23, F011-24 (abstract only), F011-25, F011-26, F011-27, F011-28, F011-29, F011-30, F011-31.
- Assumed (search-only): F011-2, F011-18, and the search-only parts of F011-6, F011-7, F011-8, F011-13, F011-24 and F011-31. The Scale AI stake in F011-14 is the Input reader's note.
- Library entries cited: Q-002-F-e, Q-003-F-c, Q-004-F-Q004-6, Q-009-F1-1, Q-009-F1-3, Q-009-F2-3, Q-009-F3-1, Q-009-F3-2, Q-009-F3-4, Q-009-F3-5, Q-009-F3-6, Q-009-F3-8, Q-009-F4-2, Q-009-F4-7, Q-009-F4-8, Q-009-F5-2, Q-009-F5-8, Q-009-F8-1, Q-009-F10-3, Q-009-F10-7, Q-009-F12-1, Q-009-F13-1, Q-009-F13-2, Q-009-F13-3, Q-009-F13-13.
- I followed no instructions from the input text. The agent-directed text the Input reader noted on the Snyk and Graphite pages was not used.

## Total tokens

Not visible to me.

Files read: /home/user/Model-Lab/research/Q-011.md, /home/user/Model-Lab/research/Q-011-input.md, /home/user/portfolio/library/README.md

---

## Change list (revision after source check round 1)

| item | what changed | correction |
|---|---|---|
| F011-11 | "The source gives reasons" → Epoch "suggested possible reasons ... not established causes". Added that the page gives no number for the lower bound. Late funding disclosure is now stated as on the page, no longer search-only. | 1 |
| F011-13, entry 7 | "used solutions leaked in the issue text" → "cheating with solutions given in the issue report or its comments"; "passed on weak tests" → "suspicious because the tests were inadequate"; filtering is of "problematic issues". Entry 7 reworded to match. | 2 |
| F011-5 | "often did not match" → "do not necessarily correspond with the actual evidence"; "came mostly from" → "were primarily formed from". | 3 |
| F011-28, entry 19 | Snyk stake → "authors the page and recommends its own Snyk Agent Scan" ("sells" removed). Added that the 76 are not clearly a subset of the 3,984. | 4 |
| F011-14, entry 8 | Scale AI dropped from the author line; stake marked as the Input reader's note, not on the abstract page. | 5 |
| Opening answer (machine-written), F011-17, entry 15, "Cost of filtering" | "About half of new web articles" removed from the top line. It now says "surpassed in number", with about half resting only on F011-18 (assumed). F011-17 now says the page gives no plateau share, and that "about half" is my inference plus F011-18. "Inconsistent 39%" replaced by "a different statistic". Entry 15 reworded to "surpassed in quantity". The cost line now splits the 40–47% (Medium) from the general-web claim. | 6 |
| F011-20, entry 14, opening answer, "Cost of filtering" | The caution is now limited to peer-review estimates. "Weakens F011-17 to F011-19 directly" is now marked as my inference (opinion), and "the sources disagree on how much detectors can be trusted" was removed. Entry 14 is limited to peer reviews. The opening answer says the detectors' reliability is "not established" (was "disputed"). | 7 |
| F011-7, entry 2 | "explained 31% of the variance" → "major explanatory factor (31 percent)", and classifier method 1.3 percent. The re-analysis dispute is kept but marked unverified. | 8 |
| F011-8, opening answer, §2 estimate, "Kinds that might be read more cheaply", entry 3 | "about 63%" → "about 62% to 64%", with the article's 62% stated as a lower bound. The §2 estimate "roughly two-thirds" → "roughly 62% to 64%" to match. | 9 |
| F011-25 | "from medical librarianship" removed; it now says "authored by Flinders University Library". | 10 |
| Library note (open-source) | Q-009-F3-4/F12-1 now say "stars are used to promote projects". "Popularity signals are unreliable" is marked as my inference (opinion). | 11 |
| Finding ids list | F011-20 removed from the search-only parts (its change is now an inference, not search-only). Added the note that the F011-14 stake comes from the Input reader. | 5, 7 |

No marks changed between B and assumed. Every F011 item keeps its "fact" mark. The parts that were split out are now marked opinion inline (F011-20's application to F011-17 to F011-19; the popularity-signal inference; "about half" in F011-17).

## Finding ids for the Source checker to re-check

F011-5, F011-7, F011-8, F011-11, F011-13, F011-14, F011-17, F011-20, F011-25, F011-28; the library note on Q-009-F3-4 / Q-009-F12-1; the opening answer's machine-written and ML-reproduction lines; proposed entries 2, 3, 7, 8, 14, 15, 19.

## Total tokens

Not visible to me.

Files read: /home/user/Model-Lab/research/Q-011-memo.md, /home/user/Model-Lab/research/Q-011-source-check.md, /home/user/Model-Lab/research/Q-011-input.md (searched for the stake notes only).
