Verdict: PASS

*The Source checker's check of research/Q-009-memo.md, round 1, in two parts run side by side: part 1 (areas 1 to 7, brief 141) and part 2 (areas 8 to 13, brief 142), each on a different model from the Researcher. Recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p), 2026-11-08, from each helper's return; part 2's return was read from its transcript after the session restarted. Each part's own verdict line is recorded as "The part's verdict was …" (LL-68). Round 1 failed because part 1 failed; round 2 (brief 147), on the revised memo, passes. The entries each part filed are on branches build/source-checker/q009-a and q009-b of the portfolio repository, not yet merged.*

## Round 1, part 1 (areas 1 to 7)

The part's verdict was FAIL.

Reason: F6-2 does not hold as the memo uses it. The memo relies on it as [B] in item F1 ("The same reviewer calls the method 'a bit hit-or-miss'"). Two further [B] items hold only in part (F3-3, and the stake note on F3-5). Details are under "What the memo must correct".

Method: I opened every URL in my share except four (F1-4, F1-5, F2-2's standard text, F5-5). F1-4, F1-5 and F5-5 failed to open, and I used search for them. The Input reader's quotes passed through a summarising fetch, and so did mine, so every quote below is from a summarised page. Where a quote is marked "exact" it appeared in the page text I was given. Where it differs, I give the page's words. Second-source column: only F4-7 and F6-4 are the same study as each other. No finding in my share has a second independent source, so none is two-source fact. Each filed entry says "single source, attributed" or similar. Same-publisher pairs (METR, DORA, Gloaguen, Arize, Paradis) are noted as non-independent.

| Id | Mark | Reason |
|---|---|---|
| F1-1 | confirmed in substance | The page says "they take 19% longer than without" (reader's "to complete issues" is not the page's wording). The 24% and 20% figures and the "no longer reflect" notice are exact. |
| F1-2 | confirmed (exact) | "only very weak evidence" and -18% with CI -38% to +9% are exact. Developer refusals and the pay cut from $150 to $50 an hour are confirmed. |
| F1-3 | confirmed (exact) | Elsevier press release, 22 Jul 2013, Mayo Clin Proc: "146 (40.2%) found these practices to be ineffective". The journal paper was not opened. |
| F1-4 | could not open | Page returned 403. A search excerpt supports the abstract's "proinnovation biases" but I did not open the page. Not filed. |
| F1-5 | could not open | The PDF returned 503, and the 2012 deck returned 503. Search results say the 1/3 figure appears in Kohavi's slides and the 2012 paper, but I opened none. Not filed. |
| F1-6 | confirmed (exact, secondhand) | Arize page: Cherny told YC "the gain is wiped out with the next model". The YC interview was not opened. Search found only mirrors and summaries that repeat the wording. |
| F1-7 | confirmed | "trailed the harnessed version by 8 points" and "aren't going to shrink to nothing" are exact. The 3.4x ARC-AGI-3 gap is confirmed. |
| F1-8 | confirmed (exact) | arXiv 2609.15919, Tewari, 2026-09-14. Closing phrase exact. It is a theory model, not peer reviewed. |
| F1-9 | confirmed (exact) | 1.5% throughput, 7.2% stability, "not a panacea", 2024-10-22. |
| F2-1 | confirmed (exact) | SRE Book ch. 32, copyright 2017. All three quotes exact. |
| F2-2 | confirmed in substance | The ISO page was opened. It gives "nine characteristics", edition 2, 2023-11-15. The list of nine and the standard text were not seen. The memo marks this item assumed. |
| F2-3 | confirmed (exact) | METR note, 2026-03-10. About 68% human merge rate. Sample is 4 maintainers, 3 repos, 296 PRs. |
| F2-4 | confirmed in substance | The page says "45 percent of cases", not "OWASP Top 10 flaws in 45% of tasks" (OWASP wording not seen). The two CTO quotes are exact. |
| F2-5 | confirmed (exact, secondhand) | The Register's wording matches. The CodeRabbit report was not opened. |
| F2-6 | confirmed (exact) | Quotes exact. The page says "nearly 5,000", not "~5,000". |
| F2-7 | confirmed (exact) | MSR '26 paper. "Persistent" is exact. Adoption inferred from config files is the reader's note, not rechecked. |
| F2-8 | confirmed in substance | 83.8% is exact. 45.1% is the complement of 54.9%. The 91.0% human figure was not seen, and the memo does not use it. |
| F3-1 | confirmed in substance | Abstract only. My page text cut the sentence after "search process". The checklist (§5.3) is unread. |
| F3-2 | confirmed in substance | Both quotes exact. The page says "difficult to determine how technologies will behave once deployed". The memo's "lab results predict deployed behaviour poorly" is stronger than that. |
| F3-3 | partly confirmed | The page says "nearly half (39%)" and "plateaued". It is "superseded by" a newer study, with a share about 3.3 points lower. The "about half" in the memo is supported only by press (Axios) and search, not by the cited page. The GPT-4o-only sentence is exact. Not filed. |
| F3-4 | confirmed (exact) | Quotes exact. The 6 million figure is in the title, not the abstract. |
| F3-5 | confirmed (exact) | Quotes and the 27 Meta variants are exact. The page lists no affiliations, so the memo's stake note (competing vendor among the authors) is not confirmed. |
| F3-6 | confirmed (exact) | 76% against 53%. Two Microsoft authors confirmed. |
| F3-7 | confirmed in substance | Quote exact. Stenberg frames the problem as low-quality reports "AI generated or not". The page says "including AI-generated ones", not "many". |
| F3-8 | confirmed (exact) | 55%, CI 21% to 89%, n=95, one HTTP-server task. |
| F4-2 | confirmed (exact) | "vary by 2.2 to 6.0 percentage points depending on which run is selected". |
| F4-3 | confirmed (exact) | Both quotes exact. Dated 2026-01-09. |
| F4-5 | confirmed (exact) | 4 of 115 (3.48%). The "at least 3 independent demonstrations" requirement is confirmed. |
| F4-6 | confirmed (exact) | Quote exact. The surveys put the share at 30% to 50% of developers. Reader's "work quality differed" was not rechecked. |
| F4-7 | confirmed (exact) | 96 engineers, "about 21%, although our confidence interval is large". |
| F4-8 | confirmed in substance | The page says "should be rigorously evaluated before deployment", not "carefully tested". |
| F5-1 | confirmed (exact) | "doubling approximately every 7 months" and the out-of-date notice. Memo's body does not use it. Not filed. |
| F5-2 | confirmed in substance | The page says "only marginal benefits despite substantial time costs (20-80% increase)". The memo's "lost most of its value" is its paraphrase. |
| F5-3 | confirmed (exact) | 58.8% and 8.7% exact. Five GPT-3.5-family models, so old. |
| F5-5 | could not open | core.ac.uk returned 403. A search shows the 5.5-year median is reported as time without an update signal. The 23% and 7% figures conflict across sources (another gives 11% within 2 years). Not filed. |
| F5-6 | confirmed (exact) | Median 3.3 years (CI 2.7 to 3.8). 32.7% updated within 2 years. |
| F5-7 | confirmed (exact) | Quote exact. |
| F5-8 | confirmed in substance | The page says "If our opinion on a blip hasn't changed for two successive Radars, we 'fade' it". The page gives no publication cadence, so the twice-yearly cadence stays assumed. |
| F6-1 | confirmed (exact) | Quote exact. It is a blog review of Cartwright and Hardie, secondhand. |
| F6-2 | not confirmed | The post says "I found the rest of the book a bit hit-or-miss – lots of use of metaphors". That phrase is about the book overall, not the support-factors method. "No discussion of mechanism experiments, or treatment heterogeneity" also refers to the book. |
| F6-3 | confirmed in substance | Both quotes exact. The page is a preprint listing and gives no journal or author affiliations. The memo's "Microsoft authors" is unconfirmed from the page. |
| F6-4 | confirmed (exact) | In the abstract. |
| F6-5 | confirmed (exact) | Exact. |
| F6-6 | confirmed in substance | The page says "context files are useful for specifying non-standard coding practices" (reader's version was a paraphrase). |
| F6-7 | partly confirmed | I opened arXiv 2604.03196. The quoted sentence is not in it. The nearest line is "human involvement substantially improves merge outcomes, even when CRAs are present". Table 1 is not monotonic. Authors are named (Chowdhury et al.), not "unknown". Not filed. |
| F7-3 | confirmed (exact) | All quotes exact. Dated 2025-09-29. |
| F7-4 | confirmed in substance | "does not generally improve task success rates" and "over 20%" are exact. The reader's "agents followed them well" and "overviews did not help" were not verified. It is the same study as library Q-004-F-Q004-10. |
| F7-5 | confirmed in substance | I opened the abstract. The wording is "frequent, small additions" (not "small, frequent"). 14.8% and 14.5% are exact. The memo marks this item assumed. |
| F7-6 | confirmed (exact) | Exact. |
| F7-7 | confirmed (exact) | Updated 2025-10-30. Data come from the 2019 report. |
| F7-8 | confirmed (exact) | Chapter 16. Both quotes exact. |
| F7-9 | confirmed in substance | The reader's quote ("fundamental changes to traditional testing approaches") is exact, but the versioning claim comes from another sentence: "tracking both LLM and prompt versions is essential for LLM regression tests". |
| F7-10 | confirmed (secondhand) | Arize says "Unconstrained automatic harness evolution overfits" and attributes it to Google's RRSI paper. The Google paper was not opened. |
| F7-11 | confirmed in substance | Same page and fade rule as F5-8. Using it as a pruning model is the Researcher's application. |

Files filed (47 entries): worktree /home/user/lib-a, branch build/source-checker/q009-a, one commit. It has the required trailer paragraph (Agent-Session: session_01QBwHGNSLmSrYQgS6BPjV8p/source-checker-141 and Spec: none (library filing from research Q-009, P-002)). It is not pushed.
- Entries: /home/user/lib-a/library/facts/Q-009-F<area>-<n>.md for F1-1, F1-2, F1-3, F1-6, F1-7, F1-8, F1-9; F2-1 to F2-8; F3-1, F3-2, F3-4 to F3-8; F4-2, F4-3, F4-5 to F4-8; F5-2, F5-3, F5-6, F5-7, F5-8; F6-1, F6-3 to F6-6; F7-3 to F7-11.
- Index: 47 rows added at the end of the table in /home/user/lib-a/library/README.md.
- Grades: no entry is graded A. Most are moderate (B), opened pages stated as attributed single-source. Weak (C) is used for F1-3 (press release), F1-6, F1-7, F1-8, F2-5, F5-8, F6-1, F7-10 and F7-11 (secondhand, theory, press or consultancy self-description).
- Types: opinion for F1-6, F1-8, F4-3, F4-8, F7-3, F7-6, F7-10 and F7-11, fact for the rest.
- Shelf lives: 12 months proposed for AI-tool and model-practice findings; 3 years for method, medical and SRE sources.
- Not filed: F1-4, F1-5, F5-5 (could not open), F3-3 and F6-7 (partly confirmed), F5-1 (confirmed, but the memo's body does not use it), F6-2 (not confirmed).
- Judgement calls for the caller to review:
  - F1-6 and F7-10 are filed as attributed secondhand reports ("Arize says X"), not as the underlying claims.
  - F7-4 duplicates the study behind library facts/Q-004-F-Q004-10.
  - F2-2 and F7-5 are filed although the memo marks them assumed, because I opened the pages.

What the memo must correct:
1. Item F1: delete "The same reviewer calls the method 'a bit hit-or-miss' (F6-2)". The phrase refers to the rest of Cartwright and Hardie's book (heavy use of metaphors). The mechanism-experiments omission also refers to the book. Restate F6-2 as not confirmed.
2. Item C4: F3-3. The cited Graphite page says 39% ("nearly half (39%)") and is superseded by a later study. "About half" rests on press and search, not on the page. Cite the newer study or say 39%.
3. Item C2: F3-5. The page lists no affiliations. Either source the competing-vendor stake or drop it.
4. Item F2: F6-7. The quoted sentence is not in the paper. The paper's own wording is "human involvement substantially improves merge outcomes, even when CRAs are present", and the trend is not strictly monotonic. Its authors are named, not "unknown".
5. Item F2: F6-3. "Microsoft authors" and "Management Science" are not shown on the page. It is a preprint listing hosted by Microsoft Research, and one of three experiments was run at Microsoft.
6. Item D2: F4-8. The wording is "rigorously evaluated before deployment". The memo's "wording may be paraphrase" flag is right, but the page's words can now replace it.
7. Item C5: F3-2. "Lab results predict deployed behaviour poorly" is stronger than the page's "difficult to determine how technologies will behave once deployed".
8. Item E1: F5-2. "Lost most of its value" should read "gained only marginal benefits despite 20-80% more time". Also state that F5-3 covers GPT-3.5-era models only (the memo says "old models", which holds).
9. Item B4: F2-4. Veracode's page says "45 percent of cases". "OWASP-class" and "tasks" were not seen in the page text.
10. Item C6: F3-7. Stenberg frames the problem as low-quality reports "AI generated or not". "Many AI-generated" is not on the page.
11. Items that still lack a source I could open: F1-4, F1-5 and F5-5 stay assumed (pages did not open). F2-2 and F7-5 can move from assumed to opened.

Total tokens: not visible to me.

## Round 1, part 2 (areas 8 to 13)

The part's verdict was PASS.

Every item the memo relies on as [B] in areas 8 to 13 holds, with the wording fixes listed under "What the memo must correct". Four items marked assumed (search-only) do not hold as the memo words them: F10-5, F13-4 and F11-9, and the reader's search-extract quotes for F11-10 and F13-12. One assumed item could not be opened: F13-7. The memo already marks all of these assumed, so none turns the verdict to FAIL.

Marks: "exact" = confirmed (quote exact); "substance" = confirmed in substance; "partly" = partly confirmed; "no" = not confirmed; "closed" = could not open. All 42 findings were opened; the substitutes for F9-6, F11-9 and F13-5 are named in the notes. All sources are 2026-11-08 opens.

| Finding | Mark | One-line reason |
|---|---|---|
| F8-1 | exact | "agent developers naturally pair improvements together" and "So you never isolate individual effects" are both on the page (2026-03-14). The footer reads "Built by Bob with gptme", so it is probably agent-written. |
| F8-4 | substance | The "directional diagnostics" quote is exact. The page says "Behavioral quality issues: down 32%" and "a further 4%", which are falls in issue counts, not a quality gain. |
| F8-5 | exact | Statsig, Tim Chan, 2021-10-08. A vendor writing about high-traffic web tests. |
| F8-6 | substance | The page says "If your primary goal is to figure out the validity of a single test, ... then you might want to avoid tests with overlapping traffic." Dated 2020-05-07, updated 2023-01-29. |
| F8-7 | exact | Abstract quote exact (Buchholz et al., 2022-10-15; Shapley values). Only the abstract was read. |
| F8-8 | exact | SRE Workbook, "Choosing a Canary Population and Duration". Only the initial capital differs. |
| F9-2 | exact | The page says "In Google's experience, a majority of incidents are triggered by binary or configuration pushes". The "in Google's experience" is part of the claim. |
| F9-4 | exact | Hodgson on martinfowler.com, page dated 2017-10-09. Both quotes are on the page. |
| F9-5 | exact | The law reads "With a sufficient number of users of an API, ... all observable behaviors of your system will be depended on by somebody." It is conditioned on the number of users. |
| F9-6 | substance | The cited specbranch page returned HTTP 523 twice. I used the SEC order 34-70694 (2013-10-16) instead. It confirms the repurposed flag, the missed eighth server, about 45 minutes and "more than $460 million". The reader's "$440-460M" is not in it. |
| F10-1 | exact | 4x and 15x token quotes are both on the Anthropic page (2025-06-13). |
| F10-3 | exact | "Human evaluation catches what automation misses" is a heading. The SEO content-farms example is on the page. |
| F10-4 | exact | arXiv 2406.07791 v9, 2025-11-11. The last 4,442 characters of the page were not read. |
| F10-5 | partly | The cited ACL PDF is a different paper (Chae et al., KAIST) that repeats the 90% figure secondhand. The original (Roytburg et al., arXiv 2601.22548) says only that examples losing significance hold "89.6% of total self-preference probability mass", and offers evaluator uncertainty as a plausible reason. It does not measure a 90% share. |
| F10-6 | exact | arXiv 2607.01904, v2 2026-10-27. The abstract says the assignment was not randomised. |
| F10-7 | exact | Becker et al. abstract: forecast 24%, estimate 20%, measured 19% slower. Same study as F1-1, so one origin. |
| F10-8 | substance | I read the PDF text. The paper says the designer "still leaves the operator to do the tasks which the designer cannot think how to automate", and that a supervisor cannot take over "if he has not been reviewing his relevant knowledge, or practising a crucial manual skill". "Hardest tasks" is the reader's gloss. |
| F11-1 | exact | OWASP LLM01:2025. I found no 2026 edition. |
| F11-2 | exact | "Enforce restrictions server-side..." and "Maintain an allowlist of approved MCP servers." are on the page. It says the payload arrives in tool responses, so the reader's "or metadata" is unconfirmed. The page has no date (copyright 2026). |
| F11-3 | exact | Willison, 2025-06-16. The 95% sentence and the three legs are on the page. |
| F11-4 | exact | Wiz states the "weaponized installed AI CLI tools" sentence. It names Claude, Gemini and Q ("including"). Wiz sells security products. |
| F11-5 | exact | "over 5500" is the 29 August interim count. Search results (not opened) show later counts of 6,700 to 7,200 repositories and 2,180 accounts, so "counts differ" holds. |
| F11-6 | exact | Spracklen et al., v3 2025-03-02. The USENIX Security 2025 venue rests on the authors' own comment. |
| F11-9 | partly | The cited Register page supports the source-code leak only. It does not contain the ban quote, and it says an earlier ChatGPT ban was lifted on March 11. The ban is confirmed by a substitute, The Star (Bloomberg, 2023-05-02): a ban on company-owned computers, tablets and phones. |
| F11-10 | substance | I read the order as PDF text. The order is dated 2024-01-03, Judge Tigar. "Defendants do not move to dismiss Plaintiffs' claims for breach of contract for open-source license violations" is in it, and other claims are dismissed. The reader's "left intact" wording is not in the order. The appeal status was not checked. |
| F11-11 | not in my share | Not in my share; not checked. |
| F12-1 | exact | arXiv v1 (2024-12-18): "4.53 million fake stars across 22,915 repositories", before a post-processing step, and "two orders of magnitude" is exact. Same paper as F3-4. |
| F12-3 | exact | "unreliable signal" and "only very weak evidence" are exact. −18% with CI −38% to +9% is exact. The "very weak evidence" wording is about the speedup increase since early 2025, not the −18% figure. |
| F12-7 | exact | SpecBench (Weco AI authors, 2026-05-20). Held-out scores are lower. |
| F12-8 | substance | The page's abstract has the 25% to under 10% refactoring fall and the 8.3% to 12.3% cloned-lines rise. The reader's quote joins two parts of it. GitClear sells analytics. |
| F13-1 | substance | "It is based on our experiences working for clients" is exact. It is a four-day meeting, and the Technology Advisory Board votes with coloured cards. The Trial ring requires production use. The page gives no Radar cadence. |
| F13-2 | exact | "more than 3000 randomized controlled trials" and 396 reversals are in the results. The results also say 7,036 articles were reviewed, of which 3,017 were RCTs. |
| F13-3 | exact | Both quotes are exact. |
| F13-4 | partly | The Ioannidis quote is exact (Milbank Q 94(3), Sept 2016). The commentary "Mass Production of Systematic Reviews and Meta-analyses: An Exercise in Mega-silliness?" (Page and Moher, 94(3):515-519) exists, but I did not read its text. A search summary suggests it partly agrees with Ioannidis, so "Disagree" is not shown. |
| F13-5 | substance | The cited core.ac.uk page returned 403, so I used the Europe PMC record of Shojania et al., Ann Intern Med 2007. It gives a median of 5.5 years free of a signal, 23% within 2 years and 7% at publication. This is time to a signal for updating, not to an actual update. |
| F13-6 | exact | Cochrane Handbook IV.1 reads "Considerable resources are required to support such an ongoing process." The URL has moved to cochrane.org. |
| F13-7 | closed | Four NICE pages returned 403. Search snippets are not an opened page. The item stays assumed and is not filed. |
| F13-8 | substance | "Lack of disagreement is more important than agreement" is a section 2 heading. Counting heads is in section 4, and "running code ... trump theoretical designs" is in section 1. |
| F13-9 | exact | DORA, updated 2025-10-30. The Octopus dispute was not checked. |
| F13-10 | exact | The CSB staff document (2013) cites a 2002 survey; the sentence is exact. The survey itself was not opened. |
| F13-11 | substance | The Wikipedia sentence is exact but cites a 2016 LinkedIn post, not The Economist. The Economist (2024) is cited separately ("the cycle is a rarity"). It is a tertiary page. |
| F13-12 | substance | The glossary defines pro-innovation bias as "the assumption that an innovation ought to spread widely and quickly". It cites Rogers (1983), not 2003. The reader's quote is not on the page. |
| F13-13 | exact | The EBSE infrastructure quote is exact. The reader's "pressure to adopt immature technology" is not on the page. |

Counts: exact 28 · substance 10 · partly 3 (F10-5, F11-9, F13-4) · closed 1 (F13-7). F11-11 is in the input but not in my assigned list, so it was not checked.

Second sources: none of my share has two independent sources opened. Pairs such as F10-7 with F1-1, F12-1 with F3-4, and F9-2 with F8-8 are the same origin. Each entry is therefore filed single-source, attributed and not load-bearing, and I rated none above moderate except the primary records.

**Filed.** 39 entries in the worktree /home/user/lib-b, branch build/source-checker/q009-b. One commit, author source-checker; nothing outside library/ was touched, and nothing was pushed. The commit message ends with the two required trailer lines. I did not add the harness's Co-Authored-By or Claude-Session lines, because the brief fixed the last paragraph and CLAUDE.md bars model names in commits.
- Entries: /home/user/lib-b/library/facts/Q-009-F<area>-<n>.md for these ids: F8-1, F8-4, F8-5, F8-6, F8-7, F8-8, F9-2, F9-4, F9-5, F9-6, F10-1, F10-3, F10-4, F10-6, F10-7, F10-8, F11-1, F11-2, F11-3, F11-4, F11-5, F11-6, F11-9, F11-10, F12-1, F12-3, F12-7, F12-8, F13-1, F13-2, F13-3, F13-5, F13-6, F13-8, F13-9, F13-10, F13-11, F13-12, F13-13.
- Index: 39 rows appended to /home/user/lib-b/library/README.md.
- Not filed: F10-5 and F13-4 (partly confirmed) and F13-7 (could not open).
- F11-9 is filed from a substitute source with the gap stated, though I marked it "partly". Drop it if you want only confirmed items.
- Grades: the README has no A/B/C key, so I followed the convention in existing entries. Strong (A) is a primary record (F9-6 and F11-10). Moderate (B) is a vendor or standards page or a peer-reviewed study. Weak (C) is a blog, preprint or tertiary page.
- Proposed shelf lives are 6 months, 12 months or 3 years.

**What the memo must correct.**
1. J2 / F10-5: remove "one 2026 paper attributes ~90% of it to evaluator uncertainty". The source (Roytburg et al., arXiv 2601.22548) says 89.6% of self-preference mass sits in examples that lose significance, with uncertainty only a plausible explanation. The cited ACL URL is a different paper that repeats the figure secondhand.
2. M2 / F13-4: "Disagree ... a commentary replies 'mega-silliness?'" is unsupported. The commentary text was not read, and the one summary I saw suggests it partly agrees with Ioannidis. Cite its title and authors only.
3. K6 / F11-9: the Register page does not carry the ban. Cite The Star (Bloomberg, 2023-05-02) for the ban, and say the Register covers only the leak.
4. I3 / F9-6: the SEC order (34-70694) is now opened. It confirms the facts, and the loss is "more than $460 million". "Assumed, SEC order not opened" can be upgraded. The Gaps bullet "the SEC Knight Capital order" is now covered.
5. F4 / F8-4: "a 32% gain" should read "32% fewer behavioural quality issues", then "a further 4%" on the newer model. D3's wording is fine.
6. I3 / F9-2: add "in Google's experience". F9-5: keep "with a sufficient number of users".
7. C1: "very weak evidence" refers to the speedup increase since early 2025, not to the −18% result.
8. C3: the 4.5M figure is the v1 count before post-processing. F12-1 and F3-4 are the same paper, not two sources.
9. L1 / F13-11: the "weak support" claim rests on a tertiary Wikipedia page citing a 2016 blog post. The Economist figure is "perhaps a fifth". F13-12 cites Rogers 1983, not 2003.
10. E2 / F13-5: "5.5 years before needing an update" is median time free of a signal for updating. M6 / F13-13: only the infrastructure quote holds; the "pressure to adopt" claim is not on the page.
11. M3 / F13-7: still unopened (403); keep it assumed.
12. K3 / F11-2: the OWASP page puts the payload in tool responses. Drop any "or metadata" reading.
13. E2 / F13-1 and F5-8: the page is silent on a twice-yearly cadence, so keep that assumed.

Total tokens: not visible to me.

## Round 2 (brief 147, on the revised memo)

The round's verdict was PASS.

I re-checked every id the memo lists, plus all 13 corrections round 1 asked for. All hold. I re-opened six pages where round 1's record was thin (Graphite, DORA, Thoughtworks, EurekAlert, and arXiv 2604.03196 in its abstract and html forms). Both Chowdhury fetches were summarising fetches, as in round 1. Everything else rests on round 1's record.

| Id | Result | Reason |
|---|---|---|
| F6-2 | holds | The memo states it as not confirmed and no longer relies on it. The "hit-or-miss" sentence is deleted from F1. |
| F3-3 | holds | Re-opened. The page says "nearly half (39%)", "plateaued" and "superseded by" a newer study. That study is "on average, 3.3 points lower". "About half" is attributed to press and search only. |
| F3-5 | holds | The stake note is dropped, and the page lists no affiliations. |
| F6-3 | holds | Worded as a preprint listing hosted by Microsoft Research, with one of three experiments run at Microsoft. "Management Science" is gone. |
| F6-7 | holds | Re-opened the html. "This pattern suggests that human involvement substantially improves merge outcomes, even when CRAs are present." Table 1 is not strictly monotonic (Mixed(CRA) 63.25% above Mixed 61.09%). The authors are Chowdhury et al. The memo keeps it assumed and not filed. |
| F4-8 | holds | The memo now uses "should be rigorously evaluated before deployment". |
| F3-2 | holds | The memo uses "difficult to determine how technologies will behave once deployed". |
| F5-2 | holds | The memo uses "only marginal benefits despite substantial time costs (20-80% increase)". |
| F5-3 | holds | The memo says "GPT-3.5-era models only". |
| F2-4 | holds | The memo uses "45 percent of cases". The OWASP and "tasks" wording is removed. |
| F3-7 | holds | The memo uses "including AI-generated ones" and Stenberg's "AI generated or not". It says the case is about low-quality volume. |
| F2-2 | holds | Moved to [B, source-checked]. It claims only the ISO catalogue page (edition 2, 2023-11-15, "nine characteristics"). The list of nine and the standard text stay unread, and the Gaps entry stays. |
| F7-5 | holds | Moved to [B, source-checked] on "frequent, small additions", abstract only. |
| F10-5 | holds (removal) | The sentence and its "Disagree" are gone from J2. No other use of it in the memo. |
| F13-4 | holds | The Ioannidis claim is kept as assumed. The commentary is cited by title and authors only, with its text unread. |
| F11-9 | holds | The Register is cited for the leak only. The ban comes from The Star (Bloomberg, 2023-05-02), marked as a substitute source. |
| F9-6 | holds | The SEC order 34-70694 is cited, with "more than $460 million". |
| F9-2 | holds | The memo has "In Google's experience". |
| F9-5 | holds | The memo has "With a sufficient number of users of an API". |
| F8-4 | holds | The memo reads "32% fewer behavioural quality issues … a further 4% fewer". |
| F1-2 / F12-3 | holds | The memo says "only very weak evidence" is about the speed-up having grown since early 2025, not the −18% result. |
| F12-1 | holds | The memo says it is the same paper's first-version count (4.53M), before post-processing, so one source, not two. |
| F13-11 | holds | The memo says the claim rests on a tertiary Wikipedia page citing a 2016 LinkedIn post, and gives the Economist figure "perhaps a fifth". |
| F13-12 | holds | The memo gives the glossary definition and cites Rogers (1983). It stays assumed. |
| F13-5 | holds | The memo says median time free of a signal, not time to an actual update. |
| F5-8 | holds | The fade rule is quoted correctly. The twice-yearly cadence stays assumed. |

Items round 1 marked not confirmed: F6-2 and F10-5 are not relied on. F1-4, F1-5, F5-5, F13-7 and F6-7 stay assumed or search-only, and none is filed. F13-7 appears in no memo item (NICE appears only in M3, as F13-7).

Scan of the rest of the memo for wording stronger than confirmed. Nothing found. Spot checks against the pages:
- **F13-1 "senior board":** Thoughtworks describes the TAB as "some of Thoughtworks' senior technologists", and the meeting runs four days.
- **L3 / G6 batch claim (F7-7):** DORA says heavyweight approval slows delivery, "leading to the release of larger batches less frequently", with "higher levels of risk and thus higher change fail rates".
- **A4 / F1-3 "146 of 363":** EurekAlert says "27% (363/1344) of articles … tested an established one", and 146 (40.2%) of those were ineffective. The memo says "tests", where the page says "articles". This is a trivial difference and I did not require a fix.
- **F2-3 "about half":** the METR quote is "roughly half".
- **F5-7 "flipped sign":** this agrees with the exact DORA quote.

Library entries changed: one commit in /home/user/lib-a on build/source-checker/q009-a. It touches library/facts/Q-009-F2-2.md and library/facts/Q-009-F7-5.md. Both said "the memo marks this item assumed", which is now false. They now say round 1 marked them assumed and round 2 carries them as [B, source-checked]. The commit message ends with the required last paragraph (the Agent-Session and Spec lines). I added no Co-Authored-By line, because the brief fixed the last paragraph. Nothing was pushed.

/home/user/lib-b needed no change and I committed nothing there. Its entries for F9-6, F9-2, F9-5, F8-4, F12-1, F12-3, F13-5, F13-11, F13-12 and F11-9 already match the corrected memo. The other entries I read in lib-a (F3-5, F6-3, F4-8, F3-2, F5-2, F5-3, F2-4, F3-7, F5-8, F1-2, F6-1) are consistent with the memo. Some say "the memo's wording was stronger" about round 1 text. That is a historical note, not a conflict, so I left them.

Memo must still correct: nothing is required. Two optional notes:
- The Orchestrator's italic recording line under the title is unchanged, and the Researcher says the Orchestrator may want to update it.
- Neither tokens line (the memo's or mine) reports a figure. I cannot see my total tokens.
