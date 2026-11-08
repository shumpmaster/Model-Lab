Verdict: FAIL

*The Source checker's check of research/Q-012-memo.md. Each round on a different model from the Researcher; recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p) from the helper's return, 2026-11-08; each round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's.*

## Round 1 (brief 165)

The round's verdict was FAIL.

The memo's main numbers hold, but several claims are worded more strongly than their sources, and one table in section 6 has two labels swapped. The unopened search-only items (F012-13, 16, 17, 28, 30) are marked assumed in the memo, which is allowed. The FAIL rests on the corrections listed at the end.

Dates: all pages were opened on 2026-11-08. Pages were read with WebFetch, which returns a model summary of each page, so quotes are as returned by it. Tokens: I cannot see my token count.

## Findings table

Second source: "none" means I opened no independent second source. For the memo's AI-drift facts, the library entries Q-009-F5-3 (Ma et al.), Q-004-F-Q004-3/8 and Q-009-F8-4 point the same way and count as independent supporting studies.

| Id | Mark | Reason |
|---|---|---|
| F012-1 | confirmed | Quote exact (RePEc listing of Poynard 2010, PLOS ONE). The abstract says "updated in 2009", not "re-rated". The 45-year half-life stays unopened. No second source. |
| F012-2 | confirmed | Quotes exact (arXiv, Zhang 2019). 100 − 20.5 = 79.5%, so "about 80% uncorrected" holds. No second source. |
| F012-3 | confirmed | Both phrases were returned as separate fragments; not seen as one sentence. It is not a duplicate of Q-009-F5-3 (Chen/Zaharia/Zou against Ma et al.). Q-009-F5-3 supports it independently. |
| F012-4 | confirmed in substance | Qwen "continue to benefit substantially from Few-Shot and CCoT", not from all structured prompting. Abstract only, one task (Python functions). Weak support from Q-009-F5-3 and F8-4. |
| F012-5 | confirmed | Exact: "scores rose by 18.8, 48.9, and 67.3 percentage points…"; "In 2023, researchers introduced…" The page has no date and no exact span for "a year later". It measures benchmark saturation, not decay of findings. No second source. |
| F012-6 | partly confirmed | The page says silent updates "can introduce behavioral drift"; the memo says "cause". The targeted-testing quote is exact. It is exploratory with no figures. Q-004-F-Q004-3 supports drift. |
| F012-7 | confirmed | "88% of these" refers to the roughly 55% of 7,931 CDSR reviews first published 1996 to Feb 2015, not to all reviews. |
| F012-8 | confirmed in substance | Mean 67.3 is a mean (Table 1: median 65.8, SD 31.0, IQR 41.6). The mean of 5 authors holds. It is a convenience sample of 195 (n=192 for time). The abstract says "mean=42 vs 26 weeks" funded against unfunded, which cannot be reconciled with a 67.3 mean; the paper does not explain it. |
| F012-9 | partly confirmed | Primary opened via Europe PMC (Michelson & Reuter 2019): "each SLR costs approximately $141,194.80", from an economic formula, so it is an estimate. 1.72 person-years appears only on the ResearchGold blog, not in the primary abstract. |
| F012-10 | confirmed | Quotes exact. It is the ISO/TC 211 committee page, maintained by a third party, last entry 2022-07-27. The ISO Directives were not opened. |
| F012-11 | partly confirmed | GOVERN 1.5 says periodic review "are planned" and roles are defined "including determining the frequency of periodic review". It does not say "required". The page calls the Playbook and framework voluntary. |
| F012-12 | confirmed | 17 guidelines; about half outdated at 5.8 years (95% CI 5.0–6.6). The point at which no more than 90% were still valid was 3.6 years. Surveys (71% response) plus a literature search through March 2000. "Reassessed for validity every 3 years" is exact. |
| F012-13 | could not open | NICE returned 403. Stays assumed (search-only). |
| F012-14 | confirmed in substance | The 42% is 8 of 19 (reviews with a planned period and at least one update), not of 76. The median actual-to-planned ratio was 1.12, so most complied. "No LSR included a retirement notice"; the abstract gives no denominator, 76 is likely. The phrase is "greater than 3 times". |
| F012-15 | confirmed | Kappa 0.64 is overall (3 reports, 4 reviews, 77 conclusions); 0.30 is the fish-oil review. Unblinded, no predictive validity, "largely subjective" all exact. The page does not show that the authors developed both methods. It has no competing-interests statement. |
| F012-16 | could not open | NICE returned 403. Stays assumed. |
| F012-17 | could not open | OpenAI returned 403. Stays assumed. |
| F012-18 | confirmed in substance | The figures are exact. "Probably unsustainable" is one Cochrane author's quote, not "participants judged". One team went from monthly to 3-monthly; others reverted to manual work or declined screening technology. |
| F012-19 | confirmed in substance | 20 weekly updates in the first 5 months, 11 FTE, 7 panels, over 200 contributors, checks as stated. The source calls workload and fatigue "challenges", not failures. Satisfaction is ">90%" in the abstract against ">85%" in the results; Table 2 shows about 86–97%. |
| F012-20 | partly confirmed | Opened via Europe PMC: 97 reviews, "n = 34, 35%" exact. Neither the tie to workload nor the advice on a core team plus automation was seen in the abstract text read. Stays out of filing. |
| F012-21 | partly confirmed | See correction 1: the memo swaps two labels. Everything else holds. |
| F012-22 | confirmed in substance | 71% sensitivity (CI 0.36–0.92), 73% specificity, 14% PPV (CI 0.06–0.3). "Most items did not matter" is the memo's reading. All five authors are listed at the University of Birmingham; the page does not show that this is the centre evaluated. |
| F012-23 | confirmed in substance | "average overlap of only 2.5% to 4.0% between the indicator feeds"; "22 specific threat actors"; "delay of, on average, a month". It is not shown whether the overlap is limited to the 22 actors. |
| F012-24 | confirmed | 99.5% (43,783 of 44,007) exact; 93.8% is Table 3 (54,683 of 58,283), not the abstract; precision 0.08 and the 40–70% pilot figure exact. The builders deploy the tool; no conflicts declared. |
| F012-25 | confirmed | "inconsistent recall" exact. The 17% is a mean at a 95% recall target. The memo omits that target. |
| F012-26 | partly confirmed | 56.2% is GPT-4o mini configuration CHAT_2; 77.5% is Llama 3 (70B) configuration LLA_2. These are single configurations, not model-wide figures. "Manual validation remains necessary" is exact. |
| F012-27 | partly confirmed | The memo's "excluded no finally-included study" holds for the baseline and update runs. The repeated-run check also reports "only one erroneous exclusion… 1/730". The paper's record counts (73 against 63 included studies) are not reconciled. Sensitivity 58–100%, precision 4–20% and 79% / 86% are exact. The 10 runs were on 50 records. Authors declare pharma and digital-health interests. |
| F012-28 | could not open | medRxiv returned 403 on both URLs. Stays assumed. Not filed. |
| F012-29 | confirmed | Quote exact. Four evidence syntheses; the 94.5% is the original reviews' traditional searches. "Recommended as a supplementary search tool". No conflicts declared. |
| F012-30 | not confirmed | The page opened, but the 94% and 94–99% figures are not in the content returned. It is dated "Nov 8, 2026", the build date. Stays assumed. |
| F012-31 | confirmed | 90%, 46%, 30%, 10%, 0% exact. High-accuracy value matches were 77%. Preprint, not peer reviewed. "Across accounts" was not seen on the page. |
| F012-32 | confirmed in substance | The 26–73% is for DeepSeek, ChatGPT-4o and LLaMA 3.3 70B. "Nearly five times" is an odds ratio (OR 4.85, CI 3.06–7.70). "Most LLMs" and "newer models tended to" are the page's words; the memo is firmer. |
| F012-33 | confirmed in substance | "40--80% across systems" exact. "Large fractions of unsupported statements" is said of deep-research configurations. No affiliations on the page, so the stake is unconfirmed. |
| F012-34 | confirmed | 3–13% hallucinated, 5–18% non-resolving, and "6–79× to under 1%" with urlhealth (the authors' open-source tool). |
| F012-35 | confirmed in substance | The statement says "should", not "requires"; "must" appears only for tool developers. The four requirements as listed are otherwise present. |

## Recomputations

The memo marks no item "Calc". I recomputed every derived number it uses.

- **F012-1:** 284/474 = 59.9%, 90/474 = 19.0%, 100/474 = 21.1%; 284 + 90 + 100 = 474. Holds.
- **F012-2:** 100 − 20.5 = 79.5%, "about 80%" holds. 100 − 58.4 = 41.6%.
- **F012-5:** "19 to 67 points" is 18.8 to 67.3 rounded; holds.
- **F012-8:** 67.3 weeks × 7 / 365.25 = 1.29 years.
- **F012-14:** 8/19 = 42.1%, so the 42% is of 19, not 76.
- **F012-20:** 34/97 = 35.05%, holds.
- **F012-21:** 17.1 − 12.4 = 4.7 h more than the reference standard (ratio 1.38). 4 − 1 = 3 of 4 trials missed by the alerts. Holds.
- **F012-24:** 43,783/44,007 = 99.49%; 54,683/58,283 = 93.82%; missed 224/44,007 = 0.51%. Holds.
- **F012-22:** 100 − 14 = 86% of flagged items were not true positives. The memo does not state this, but "most flagged items did not matter" rests on it.

## Library entries cited

Read from /home/user/portfolio/library on its current branch. The Q-009 entries are not on main, and the new worktree is cut from main.

- Q-005-LF-Q005-15: says what the memo says (5.8 years, 3-year reassessment, grade weak (C)).
- Q-009-F13-5: holds (median 5.5 years, 23% within 2 years, 7% at publication).
- Q-009-F5-6: holds.
- Q-009-F5-3: holds (GPT-3.5-era models).
- Q-009-F13-6: holds.
- Q-009-F1-1: holds (METR's page says the result is out of date).
- Q-009-F8-4: holds. The entry notes the 32% is a fall in issue counts, and the memo says "32% reduction".
- Q-009-F10-3: holds.
- Q-004-F-Q004-3: holds.
- Q-004-F-Q004-8: holds.
- Q-004-F-Q004-4: partly. Four IDs retired 12–13 months after their snapshot, and one (Sonnet 4.5) is not due until 2026-11-30, about 14 months. The memo's "IDs were retired 12 to 14 months" overstates that one.
- Q-009-F5-8: the memo's "tied to a fixed publishing cycle" is not supported. The entry says the page does not state the Radar cadence.
- Q-005-LP-Q005-09, Q-004-P-Q004-1: say what the memo says.

## Filed

Worktree /home/user/lib-q-012, branch build/source-checker/q-012, one commit, not pushed. Author is source-checker. The last paragraph is exactly the two lines required: `Agent-Session: session_01QBwHGNSLmSrYQgS6BPjV8p/source-checker-165` and `Spec: none (library filing from research Q-012, P-002)`. I did not add the Co-Authored-By or Claude-Session trailers from the attribution reminder, because the task fixed the last paragraph and the project bans model names in commits.

- 27 facts, /home/user/lib-q-012/library/facts/Q-012-1.md through Q-012-27.md, numbered as the memo's proposals 1–27. Each is reworded to what its source supports. Grades are moderate (B) for entries 1–3, 5, 7–8, 10–20, 22 and 27, and weak (C) for entries 4, 6, 9, 21, 23–26.
- 2 patterns: /home/user/lib-q-012/library/patterns/Q-012-P1.md (the memo's proposal 29) and Q-012-P2.md (proposal 30).
- 29 index rows appended to /home/user/lib-q-012/library/README.md. Nothing outside library/ was written.
- Not filed: proposal 28 (NICE). The NICE pages returned 403 and the claim is unconfirmed. There is no Q-012-28 file.
- Rewordings in the entries:
  - Entry 8 drops the funded 42 against 26 weeks result as unreconciled.
  - Entry 10 changes "requires" to the page's "are planned" and notes the framework is voluntary.
  - Entry 11 gives "8 of 19".
  - Entry 13 attributes "probably unsustainable" to one author.
  - Entry 15 corrects the swapped labels.
  - Entry 20 names the single configurations.
  - Entry 21 adds the 1/730 erroneous exclusion.
  - Entry 27 changes "requires" to "should".
- P1 drops F012-22 as an origin, because that study measures forecast accuracy, not what an alert misses. It also drops "finds little of what matters", because the four new trials did not change the review's results.
- P2 leaves out F012-28 and F012-30, which were not opened.

## What the memo must correct

1. **F012-21 table (section 6 and proposed entry 15):** swap the labels. PubMed Similar Articles took 9.4 h and Scopus Citing References (citation alerts) took 5.2 h. The memo has citation alerts at 9.4 h and similar-article alerts at 5.2 h.
2. **F012-11 (NIST) and F012-35 (joint statement):** replace "requires". NIST describes planned periodic review in a voluntary framework. The joint statement says "should".
3. **F012-6:** replace "silent updates cause drift" with "can introduce drift".
4. **F012-14 (entry 11):** state the 42% as 8 of 19, not as a share of the 76. Replace "often lag" with the figures. Note the abstract gives no denominator for "no retirement notice".
5. **F012-18 and F012-19:** "participants judged it probably unsustainable" is one author's quote. Replace "failures" with "challenges".
6. **F012-26:** the 56.2% and 77.5% are single configurations (CHAT_2, LLA_2), not model-wide.
7. **F012-27:** add the 1/730 erroneous exclusion and the unreconciled 73 against 63 counts. "Excluded no finally-included study" is true only for the single-pass runs.
8. **F012-8:**
   - Say "convenience sample of 195 registered reviews".
   - Note the median is 65.8.
   - Note the funded and unfunded figures cannot be reconciled with the mean and are left unresolved in the paper.
9. **F012-32:** name the three models behind the 26–73% range. "Nearly five times" is an odds ratio. Soften "did not fix it" and "newer models did worse" to the page's "most LLMs" and "tended to".
10. **F012-15:** drop "the authors include the developers of both methods". It is not shown on the page. The same applies to the stake note on F012-22.
11. **F012-9:** the primary (Michelson & Reuter) confirms $141,194.80 as a formula estimate. 1.72 person-years is blog-only. F012-20: only the 97, 34 and 35% figures were seen; the tie to workload and the advice on a core team plus automation are unconfirmed.
12. **Library citations:** Q-009-F5-8 does not support "tied to a fixed publishing cycle". Q-004-F-Q004-4's "retired 12 to 14 months" includes one ID not yet retired.
13. **Still unopened (403 or no content):** F012-13, 16, 17, 28 and 30. They must stay assumed and out of the library. Proposal 28 stays out until someone opens the NICE page.
14. **F012-3:** the quote is two fragments; mark it so, or have it re-read.

## Round 2 (brief 176)

The round's verdict was FAIL.

All 14 round 1 corrections and all 17 listed findings now hold. The FAIL is for outside claims in the memo's "Answer in brief" bullets that go beyond what the sources support. Pages were re-opened only for F012-5 and F012-7, where round 1's record left a doubt. Everything else was checked against round 1's record.

## Re-checked ids

| Id | Result | Reason |
|---|---|---|
| F012-3 | holds | Marked as two separate fragments. Not a duplicate of Q-009-F5-3. |
| F012-6 | holds | Now "can introduce behavioural drift". Exploratory, own framework noted. |
| F012-8 | holds | Convenience sample of 195, mean 67.3, median 65.8. The 42 against 26 weeks is marked unreconciled and not relied on. |
| F012-9 | holds | $141,194.80 is marked as the source's own estimate. The 1.72 person-years stays assumed. |
| F012-11 | holds | "are planned", frequency left to roles, voluntary framework. |
| F012-14 | holds | 8 of 19 (42%), median ratio 1.12, "greater than 3 times", no denominator for the retirement notice. |
| F012-15 | holds | The developer-stake note is dropped. |
| F012-18 | holds | "Probably unsustainable" is attributed to one Cochrane author. |
| F012-19 | holds | "Challenges" replaces "failures". Satisfaction disagreement noted. |
| F012-20 | holds | Only the 97, 34 and 35% figures are relied on. The workload tie and core-team advice stay assumed. Removed from the "stall" line. |
| F012-21 | holds | Labels fixed: Similar Articles 9.4 h, Scopus Citing References 5.2 h. |
| F012-22 | holds | The authorship stake note is dropped. The sentence "Most items it flagged did not matter" is still stated as part of the fact. See correction 6 below. |
| F012-26 | holds | CHAT_2 and LLA_2 are named as single configurations. |
| F012-27 | holds | Limited to single-pass runs. 1 of 730 and the 73 against 63 counts added. |
| F012-30 | holds | Stays assumed. Page opened, figures not found. Not relied on. The Elicit bullets are restated. |
| F012-32 | holds | Three models named, odds ratio 4.85, "most LLMs" and "tended to". |
| F012-35 | holds | "Should", with "must" only for tool developers. |
| Q-009-F5-8 | holds | Memo now notes the page does not state the Radar cadence. |
| Q-004-F-Q004-4 | holds | Four retired at 12–13 months, one not due until 2026-11-30. |

Items round 1 marked not confirmed (F012-13, 16, 17, 28, 30, and the blog-only parts of F012-9 and F012-20) are labelled assumed in the memo. Entry 28 is not to be filed, and none of them feeds a library entry or pattern. The exception is the "Answer in brief" bullet that still leans on the F012-20 workload tie (see correction 1).

Two re-opened pages:
- **F012-5:** the AI Index page says "Just a year later … scores rose by 18.8, 48.9, and 67.3 percentage points". So "within a year" holds.
- **F012-7:** the Hoffmeyer abstract says "Fifty-five percent were published for the first time between 1996 and February 2015" and "88% of these had been inactive for 5.5 years or more". The memo's wording matches this.

## Library entries changed

One commit, `fda24e1`, author source-checker, in the worktree /home/user/lib-q-012 on branch build/source-checker/q-012, not pushed. It carries the required last paragraph with `Agent-Session: session_01QBwHGNSLmSrYQgS6BPjV8p/source-checker-176`.

The commit changes 9 files: `Q-012-6`, `-10`, `-11`, `-14`, `-15`, `-16`, `-20`, `-24` and `-27`, all under `library/facts/`. Facts, grades and filings are unchanged. I removed notes that described the memo's round 1 wording, such as "memo's 'requires'", "cause drift", "often lag", "failures" and the swapped labels. Those notes were false once the memo was corrected. In `Q-012-16` I also removed "possible self-evaluation", which the memo dropped. The page does not show whether the authors are at the centre evaluated, and that is now stated that way.

I checked the other entries against the memo and left them as they were. The patterns P1 and P2 are consistent with the memo.

## What the memo must still correct

1. **"Answer in brief", continuous intake bullet:** "every evaluation found reports heavy workload and drop-off" is too strong.
   - F012-14 found most living reviews kept close to their planned period.
   - The F012-20 workload tie is unconfirmed.
   - F012-21 and F012-22 are not workload evaluations.
   - Restate it to F012-18 and F012-19, and the 35% update rate.
2. **"Answer in brief", automated reading bullet:** "Every standards body and study author found keeps people checking" is only supported for F012-26, 27, 29, 31 and 35. Page-level support was not shown for F012-24, 25, 33 and 34. Name the sources, or weaken to the section 7 opinion ("no source found recommends unchecked automated reading").
3. **"Answer in brief", event-triggered bullet:** "Event-triggered review is cheaper" has no source, and section 5 says there are no cost figures. F012-15 compares two signal methods, not event-triggered against scheduled review. Drop "cheaper".
4. **"Answer in brief", continuous intake bullet:** "catches new evidence earliest" rests on one review (F012-21). Qualify it.
5. **"No review" bullet:** "common default, and decay goes unnoticed" is an inference. F012-2 and F012-7 give uncorrected or inactive shares, not "unnoticed". Mark it as opinion or reword.
6. **F012-22:** "Most items it flagged did not matter" is the memo's reading of a 14% positive predictive value. Reword to "86% of positive predictions were not borne out", or label it as opinion.
7. **F012-31:** "across accounts" was never seen on the page. Drop it from the F012-31 line and entry 23, or mark it unconfirmed. The library entry already flags it.
8. **F012-1 and entry 1:** the page says "updated in 2009", not "re-rated". The library entry already uses "updated".
9. **F012-23:** it is not shown that the 2.5–4.0% overlap is limited to the 22 shared actors. Soften "for 22 shared actors".
10. **"What each answer would change":**
    - "Living efforts stall without dedicated resources" is stronger than F012-18, where some teams slowed or dropped, and Q-009-F13-6, which says "considerable resources". Reword.
    - "Tools screen with high recall" cites F012-27, whose title and abstract sensitivity ranged 58–100%. Qualify it.
11. **F012-9:** the memo says "opened by the Source checker" but gives only the blog URL. Cite the primary (Michelson & Reuter 2019, opened via Europe PMC).

I cannot see my token count.
