Verdict: PASS

*The Source checker's deciding check of the Q-016 library entries, as the owner ruled (decisions/questions/P-002-research-stop-3.md): one check of every filed entry against its source, the memo set aside. A fresh session on a different model from the Researcher, brief 215 (docs/briefs/215-source-checker.md). Recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p) from the helper's return, 2026-11-09.*

All 25 entries were checked against their sources. I opened every URL myself, except two: The Block returned 403 to curl, so I read it with WebFetch, and the LessWrong mirror would not connect, so I dropped it. I also opened the Kabir PDF and the Schemmer PDF (arXiv 2204.06916) for the claims that rest on full text. No entry relies on an unopened source, and no entry was removed. I had no wording to change in the entries marked "holds" below.

| id | source opened / record used | result | reason |
|---|---|---|---|
| Q-016-1 | Google Research blog, opened | holds | Ratio, copy-paste exclusion, 750 ms, 37%, 50% and the date all match. |
| Q-016-2 | The Decoder, opened | holds | 25/50/75 percent, "the company says", Pichai only in a separate sentence. |
| Q-016-3 | The Register, opened | reworded | Nadella's word is "software", not AI. The 30-40 percent is the Register's paraphrase, not a separate quote from him, and its unit is not stated. Title and README row changed to match. |
| Q-016-4 | The Block, read with WebFetch (403 to curl) | reworded | Quotes, author, date and the absence of "AI-assisted" all hold. I replaced the note about "the memo's reading" with "an opinion, not stated in the article". |
| Q-016-5 | Redwood Research post, opened | reworded | Quotes, caveats, and the Amodei "70, 80, 90%" and "not uniformly" lines all hold. I removed the "memo's B" note, the LessWrong mirror source (not reachable) and the README phrase "the outside check". |
| Q-016-6 | arXiv 2506.08945v2, opened | holds | 29%, 3.6%, 30 million commits, 170,000 developers. |
| Q-016-7 | agent-trace.dev and Git AI page, opened | holds | Labels, non-goals, storage left open, "no heuristics", known gaps, human checkpoints. The "no accuracy test" point is attributed to the pages and the Input reader. |
| Q-016-8 | GitHub Docs, opened | holds | "Directional view", editor blind spot, CLI inflation, agent lines undercounted. |
| Q-016-9 | Anthropic Economic Index report, opened | holds | Footnote 4 gives 45% vs 49%. It sits in the Claude.ai chapter. No classifier accuracy is stated. |
| Q-016-10 | arXiv 2205.06537, opened | holds | Quote exact; submitted 13 May 2022. |
| Q-016-11 | arXiv 2507.15003, opened | reworded | Quote holds. I removed the "memo's" percentages sentence. |
| Q-016-12 | Anthropic, Measuring agent autonomy, opened | reworded | All figures and caveats hold. The page does say "<50 sessions", so I replaced the note that said it did not. |
| Q-016-13 | arXiv 2211.03622, opened | holds | Both abstract quotes hold; latest version dated 2023-12-18. |
| Q-016-14 | arXiv 2308.02312 abstract, and the PDF | holds | 52%, 39%, and the GPT-3.5 free-version basis confirmed in the PDF. |
| Q-016-15 | PMC3240751, opened | reworded | RR 1.26 (CI 1.11 to 1.44) is from a meta-analysis of four papers. Only 74 studies met inclusion; the Statement had implied the RR covered all 74. The 6% is credited to Friedman in the introduction and is not filed as this review's finding. |
| Q-016-16 | Three arXiv abstracts, opened | holds | All numbers match: 201 projects, HR 0.842, V 0.116, 26.3% vs 23.0%, F1 0.285, about 110,000 PRs, 182 repositories, 6% per 10 points. |
| Q-016-17 | Faros report, opened | reworded | Figures hold. I replaced the "memo's note" about the FAQ page with a statement that it was not opened and is not filed. |
| Q-016-18 | Anthropic productivity page, opened | reworded | 80%, 100,000 conversations, Claude as estimator, refinement time not counted, and the date all hold. The JIRA test is of Claude's time estimation (rho 0.44 vs 0.50 for developers), not a check of the 100,000-conversation estimates. The old line "agreement not quantified" was wrong. |
| Q-016-19 | InfoQ, opened | holds | 68% to 26%, 65%, the self-report quote, 1,155 + 405 = 1,560 respondents, no fieldwork dates. |
| Q-016-20 | arXiv 2510.26787 and CAIS blog, opened | holds | 2.5%; 15.8%; "badly overshot"; 6.25% vs 17.9%; joint development with Scale Labs. |
| Q-016-21 | Transformer and arXiv 2510.04374, opened | reworded | Quotes hold. I removed the "memo's" wording. |
| Q-016-22 | HBS Working Knowledge, opened | reworded | 758 consultants, 12%/25%, 40%, 19 points and the 24/13 points all hold. The page describes 18 tasks inside the frontier (shoe design), so "on one task" in the title and README was wrong. |
| Q-016-23 | arXiv 2405.20362, opened | holds | 17% to 33%; "first preregistered". |
| Q-016-P24 | Facts it cites, and their sources | reworded | Origin now cites facts only and is marked as opinion. I removed the F016-6/F016-7 and memo references and changed "the one outside estimate" to "an outside estimate". |
| Q-016-P25 | Facts it cites, Q-009-F10-7, Schemmer PDF | reworded | The Schemmer description is confirmed: classification only, needs the decision before advice, or a simulated one. Q-009-F10-7 exists and says what the pattern claims. I removed the "memo's own source" sentence. |

The README rows for Q-016-3, 4, 5, 10, 15, 16, 20, 21, 22 were changed to match the entries and drop memo-bound text.

Commit: 21fc723 on build/source-checker/q-016 in /home/user/lib-q-016, library/ only, one commit, not pushed. The last paragraph is exactly the requested trailer. I did not add the Co-Authored-By or Claude-Session lines from the session attribution reminder, because the brief fixes the last paragraph and project rules bar model names in commits.

Still open (none of it affects the verdict):
- The Block gave 403 to curl and was read through WebFetch, and the LessWrong mirror was unreachable. The mirror is no longer cited.
- Q-016-2, 3, 4 and 19 are press relays of company statements, graded C. Their primaries (Pichai's post, the Armstrong post on X, the Atlassian report) were not opened, and the entries say so.
- Q-016-6, 10, 11, 13, 16, 20 and 23 rest on abstracts or the owner's blog.
- The 19, 24 and 13 point figures on the HBS page are not reconciled, and the entry says so.
- The "no accuracy test found" statements in Q-016-7 are negatives I did not search for; they are attributed to the Input reader and the pages.
- The Q-016-5 date shows only "Oct 22" on the page, with the year taken from the earlier record.
- I cannot see my token total.

Paths: /home/user/lib-q-016/library/facts/Q-016-*.md, /home/user/lib-q-016/library/patterns/Q-016-P24.md, /home/user/lib-q-016/library/patterns/Q-016-P25.md, /home/user/lib-q-016/library/README.md.
