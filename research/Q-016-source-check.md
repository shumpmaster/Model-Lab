Verdict: FAIL

*The Source checker's check of research/Q-016-memo.md. Each round on a different model from the Researcher; recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p) from the helper's return, 2026-11-09; each round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's.*

## Round 1 (brief 203)

The round's verdict was FAIL.

Several claims the memo does not mark as assumed do not hold as worded. I opened the cited pages, 33 of them in full or as abstracts, and read the Schemmer paper and the Kabir paper as PDFs. A figure from the Input reader's search-only extracts counts as holding if the memo already marks it assumed. Tokens: I cannot see them.

## Findings (mark, then one-line reason)

| id | mark | reason |
|---|---|---|
| F016-1 | confirmed (quotes exact) | Google Research blog, 2024-06-06. The characters ratio, "characters from copy-pastes are not included in the denominator", the 750 ms rule, 50% and 37% all hold. Google's own tools; no second source. |
| F016-2 | confirmed in substance | The Decoder, 2026-04-23. The page says "25 percent in October 2024 and 50 percent by fall 2025", not the memo's ">25%". Press relay of Google's blog post; the primary was not opened. The memo's "~30% outlet" was not opened. |
| F016-3 | partly confirmed | The Register has "maybe 20 to 30 percent of the code that is inside of our repos today in some of our projects". The memo drops "in some of our projects" and puts "written by software" in quotation marks, which I did not find. I did not verify the claim that outlets disagree. |
| F016-4 | confirmed (quote exact) | Redwood, 2025-10-22. "much less than 90%, more like 50%." The post shows no calculation and calls it a "current understanding". The caveats and "less than 2x" hold. |
| F016-5 | partly confirmed | The Block, 2025-09-04. The 40% and "over 50% by October" quotes are exact. The "AI-assisted and AI-generated used interchangeably" claim is false: "AI-assisted" does not appear on the page. The "95%+" claim was not opened. |
| F016-6 | not confirmed | I opened the letsdatascience page. It has no spokesperson, no 70–90% and no ~90% for Claude Code. Redwood's page does have Amodei saying "70, 80, 90%" (Sept 2025), so the attribution is wrong. The memo marks it assumed. |
| F016-7 | confirmed in substance | Redwood's page and the LessWrong mirror give "on many teams, you know, not uniformly" (Benioff interview). The mirror does not name Dreamforce. The memo calls it search-only, but it is checkable. |
| F016-8 | confirmed (quotes exact) | arXiv v2 abstract. 29%, 3.6%, experienced programmers; 30M commits and 170,000 developers. Science 2026 not opened. |
| F016-9 | confirmed (quotes exact) | The labels, the non-goal and "does not define how traces are stored" hold. The page does not name a lead. Search results say Cursor published it; I did not open those. The memo's "led by Cursor" is thus secondary. |
| F016-10 | confirmed (quotes exact) | "no heuristics"; the gaps and human checkpoints hold. The "neither tested" claim is a negative I could not verify. |
| F016-11 | confirmed (quotes exact) | "directional view"; the editor blind spot; CLI inflation; agent lines undercounted. The page says nothing on whether accepted code survives. |
| F016-12 | confirmed in substance | The report has 77% API automation. Footnote 4 says "45% automation versus 49% with Sonnet 4" (a rerun). The footnote does not name the dataset; it sits in the Claude.ai chapter. No accuracy statement found. |
| F016-13 | confirmed (quotes exact) | 60% and 50% ("59%" in the body); "fully delegate" 0–20%; convenience sampling; non-anonymous; "grain of salt"; 67% more merged PRs. Published 2025-12-02. |
| F016-14 | confirmed in substance | The abstract says acceptance rate, "rather than... persistence", "drives developers' perception of productivity". It does not say "predicted better". The 27% was not seen. |
| F016-15 | confirmed (quote exact) | "their PRs are accepted less frequently". No percentages on the abstract. The 64/49/35/79 figures were not seen. |
| F016-16 | confirmed in substance | About 20% for new users, over 40% by 750 sessions, 5% to about 9% of turns. The default-settings and harder-task caveats hold. Correctness is not measured. "<50 sessions" is the Input reader's quote only. |
| F016-17 | partly confirmed | RR 1.26 (95% CI 1.11–1.44) and 74 studies hold. The 6% override is not the review's finding. It is in the introduction, credited to Friedman et al. The memo says the review "found" it. |
| F016-18 | confirmed in substance | I read the full text of arXiv 2204.06916. It defines a relative positive AI reliance measure and a relative positive self-reliance measure, which need the person's decision before the advice (or a simulated one from humans without advice). It covers classification tasks only. The abstract does not use those terms. The memo calls it search-only and it is not. |
| F016-19 | confirmed (quotes exact) | Perry et al. abstract. |
| F016-20 | confirmed (quotes exact) | 52% and 39% hold. The PDF confirms the free version based on GPT-3.5. |
| F016-21 | confirmed (figures exact) | 45.7% distrust, 32.7% trust (n=33,244); 66% "almost right" (n=31,476). The stake note is a judgement. |
| F016-22 | could not open | The page returned 403 and PubMed has a cookie wall. A search extract of the abstract matches, but I did not open the page. Not filed. |
| F016-23 | confirmed (quotes exact) | HR 0.842, V 0.116, 26.3% vs 23.0%, F1 0.285, and "per-agent variation exceeds the agent-human gap" all hold. 201 projects. |
| F016-24 | confirmed (quote exact, abstract) | About 110,000 PRs; "more churn over time". |
| F016-25 | confirmed (abstract) | "overall maintenance rates are similar"; higher corrective maintenance; about 6% per 10 points of no-review rate (an association). The one-year window is not in the abstract. |
| F016-26 | partly confirmed | Definitions, Goodhart's law and the update date (2026-01-05) hold. The page does not mention surveys; it names the Quick Check, retrospectives and tools. It also says custom integrations "might not be worth the initial investment". That is the claim the memo says it could not find. |
| F016-27 | confirmed (quote exact) | "each hallucinate between 17% and 33% of the time"; "first preregistered". |
| F016-28 | partly confirmed | The count of 2,266 (5 Nov 2026), "wider universe" and "judgment call" hold. The database also includes some decisions where AI use was only alleged. "Failures" and "shows up late" go beyond the page. |
| F016-29 | confirmed (quotes exact) | 21%, 98%, 91%, 9%, no company-level correlation; over 10,000 developers, 1,255 teams. |
| F016-30 | confirmed (quotes exact) | 80%; 100,000; Claude estimates; JIRA; refinement time not counted; 2025-11-25. |
| F016-31 | confirmed (quotes exact) | Utilization, impact and cost; "particularly susceptible to gaming"; the agent-PR advice. Undated. |
| F016-32 | confirmed (quotes exact) | 68% to 26%; 65%; self-report caveat; 1,560 respondents; no fieldwork dates. Press relay of the vendor survey. |
| F016-33 | partly confirmed | The 2.5% quote holds. The abstract gives no count (240), no human judging and no Scale AI. The CAIS post says the benchmark was developed with Scale Labs. |
| F016-34 | confirmed in substance | 15.8% for Fable 5 and "badly overshot" hold. The post gives sizes (about 2.9x and 2.3x), so the memo's "paraphrase" caution is more cautious than needed. The Input reader's own count calls this page opened, not search-only. The 16.1% was not opened. |
| F016-35 | partly confirmed | 44 occupations, blinded graders and the "full substitute" quote hold; "it" is the automated grader. The 47.6% and "100x" claims are not in the article, and neither is the critic. |
| F016-36 | partly confirmed | 758 consultants; "12 percent more work at a 25 percent faster clip" (shoe-design tasks). The 40% is "certain kinds of tasks", not tied to inside the frontier. The 19 points is "more complex tasks". For the outside-frontier task the page gives 24 and 13 points. |
| NBER w31161 | confirmed in substance | 14%, 34%, 5,179 agents. "One firm" is not on the page. |
| TechXplore / Noy & Zhang | confirmed (quotes exact) | 40% less time, 18% higher quality, no fact-checking. |
| BetterUp | confirmed in substance | 40%, 1h51, $186, and 1,004 against 1,150 respondents all hold. $9M per 10,000 is stated; $186 × 12 × 10,000 is $22.3M, so it does not follow. |

I found no second independent source for any share figure. Redwood's mirror is not independent of Redwood's post.

## Recomputations
The memo marks nothing "Calc". I checked the derived numbers it states:
- 49% − 45% = 4 points (F016-12).
- Interrupts 5% to about 9% (F016-16).
- 68% to 26% is a fall of 42 points (F016-32).
- BetterUp: $186 × 12 months × 10,000 workers = $22.3M a year, not $9M.

## Library entries cited
- **Q-009-F5-7** is about DORA's throughput link turning positive, not stability. The memo lists it with the stability entries Q-009-F1-9 and Q-009-F2-6.
- **Q-012-22** is about Elicit search sensitivity, not summaries or citations. The memo lists it among those entries.
- **Q-009-F10-6** is weak (C). The memo's header says "Fact, B (library)".
- **Q-009-F1-1** is a B entry. The memo omits METR's note that the result "no longer reflect[s] the current impact" of AI models.
- **Q-011-14** is limited to peer reviews and five detectors. The memo widens it to AI-text detectors in general.
- **Q-009-F2-4** says "45 percent of cases". The memo says "samples".
- The rest match the memo: Q-002-F-h, Q-005-LF-Q005-14, Q-006-P-q006-01, Q-007-F07, Q-009-F1-2, F1-9, F2-3, F2-5, F2-6, F2-7, F2-8, F3-8, F4-7, F6-4, F6-5, F10-7, F12-8, Q-012-24 to 26 and Q-013-14.

## Filed
The branch is build/source-checker/q-016 in /home/user/lib-q-016. I made one commit as source-checker with the required trailers, and did not push.
- Facts: /home/user/lib-q-016/library/facts/Q-016-1.md to Q-016-23.md. All twenty-three are filed. Entries 2, 3, 4, 10, 15, 16 and 22 are reworded to what the sources support.
- Patterns: /home/user/lib-q-016/library/patterns/Q-016-P24.md and Q-016-P25.md.
- Index: 25 rows appended to /home/user/lib-q-016/library/README.md.
- Grades differ from the memo's B:
  - Press relays and unaudited or unopened-primary items are weak (C): Q-016-2, 3, 4, 5, 19, 21 and 22.
  - The three abstract-only preprints in Q-016-16 and both patterns are weak (C).
- F016-6 and F016-22 are not filed. F016-7 is used only through Redwood's page.

## What the memo must correct
1. F016-17: the 6% override is Friedman et al. as cited in the review's introduction, not the review's finding (§2, proposed entry 15).
2. F016-5: delete the claim that "AI-assisted" and "AI-generated" are used interchangeably (§1 table).
3. F016-3: add "in some of our projects", remove the quotation marks on "written by software", and either source or drop "outlets disagree".
4. F016-2: use "25%", not ">25%".
5. F016-6: the attribution to a spokesperson is not supported by the page opened. Redwood's page has Amodei saying "70, 80, 90%". Fix the table row and the line "vendor's 70–90%".
6. F016-7 and F016-18 are checkable. Drop "search-only" for F016-18 (the full text was opened), and for F016-7 (Redwood's page has the quote; the mirror does not name the event).
7. F016-26: the DORA page does say custom integrations "might not be worth the initial investment". Delete the discrepancy note. Change "collection may be by survey" to Quick Check, retrospectives and tools.
8. F016-28: the database includes some decisions where AI use was only alleged. "Counts only failures a court addressed" and "shows up late" go beyond the page.
9. F016-33: the 240 count, "judged by humans against professionals' deliverables" and the Scale AI stake are not in the abstract. The stake is supported by the CAIS post.
10. F016-35: remove the critic's attribution on the "100x" claim; it is not in the article.
11. F016-36: the 19 points is the page's "more complex tasks" figure. The outside-frontier drops are 24 and 13 points. The 40% quality gain is not tied to the inside-frontier tasks.
12. F016-9: "led by Cursor" is not on the page.
13. F016-14: use "drove ... rather than persistence", not "predicted ... better than".
14. The library citations above: Q-009-F5-7, Q-012-22, the Q-009-F10-6 grade label, the Q-009-F1-1 caveat, the Q-011-14 scope, and Q-009-F2-4 "cases".
15. The opening answer's "three preprints... disagree" should say they measure different outcomes: survival, churn, and corrective maintenance. The both-directions trust claim rests on F016-22, which I could not open.
16. The Input reader's count of search-only findings (F016-6, 7, 34) does not match the memo's list (F016-6, 7, 18, 22, 34's paraphrase). Reconcile it.
