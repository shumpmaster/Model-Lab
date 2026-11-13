# Q-018 memo 5 — the hand check re-coded on the owner's rulings 11 and 15 to 19

*Recorded verbatim by the Orchestrator. The Researcher's return on brief 333 (docs/briefs/333-researcher.md), on Model-Lab@761054b, from research/Q-018.md and research/Q-018-extract/ alone. Not yet checked: the Critic's step 5 on the changed items follows.*

Q-018, memo 5: the 74 drawn items re-coded on the owner's rulings 11 and 15 to 19. Dated 2026-11-13. From the extract alone; no web; nothing written.

Plain summary. Nothing failed or was skipped outright, but several results could not be decided from the extract, and some rest on my own reading of the rules, so the Critic should check them. Of the 74 drawn items, 33 are pieces of work and 41 are not: 37 merged pull requests change only records, answers or guidance, 2 were closed unmerged, and 2 are commits with no pull request. Taking the "later work" codes exactly as the extract gives them, 14 of the 33 pieces had at least one owner touch before merging, and 19 had none. Without those codes the figure would be 16 of 33. The codes take 22 touches off the count. They move 2 pieces from needing the owner to not needing the owner, and none the other way. For the first independent check, 16 pieces have a first round that failed, 4 passed, 4 are undecided, and 9 have no check record at all. No piece was reverted or marked as reopened. 13 pieces have their 30 days complete (none reopened) and 20 are still pending. Owner-account comments on Service-Desk and Personal-Org-Operating-Model pull requests all carry the agent footer, so none counts as a touch. Model-Lab's sampled pull requests have no comments. No review exists on any of the three repositories. Nothing here says whether any count or share is large or small.

HOW I READ. I took each `later_work` code from the extract and coded none of my own. I read sample.jsonl with field searches, not line by line. I worked out the K3 line sums by hand from the per-file added and removed lines (arithmetic to be checked). Grading: every result below is a coded reading of records under the rules, not a library fact, and I propose no library entries. Record labels are the extract's 8-hex labels. Commits are the first 8 hex digits. Times are UTC, as commit times. Dispatch is the piece's first commit for every piece except ML #98 (brief record 258, first added 2026-11-11T18:23:13Z, the earlier of its two brief records). No sampled Service-Desk piece has a control file or brief record, so E-K3 is not seen.

Abbreviations: ML = Model-Lab, SD = Service-Desk, POOM = Personal-Org-Operating-Model. NP = not a piece. 30d = 30 days complete at the cut-off. NR = not reopened. Pend = pending.

A. THE 74 ITEMS (sample.jsonl order)

Rules in each line: RP1 (merged PR) and RP2 (a built, plan or research file); kind and the rule (K1 to K3); touches; C1; reopening. K4 is for trials only. RR1(a) found no revert for any item, and the `Reopens:` marks are empty (RR1(b) cannot exist on past pieces). For a non-piece, kind, touches, C1 and reopening do not apply.

Random part, Model-Lab (20 from all):
1. ML #61. Merged. NP (RP2: only records files).
2. ML #43. Piece. Plans (K3: plan 347 changed lines against research 168). Touches 0. C1 FAIL (plan record 0df9522f, spec's plan.md, reading (ii), 5 rounds; three unclassed records in its spec folder not read). Pend.
3. ML #29. Piece. Plans (K3: only plan files). Touches 1. C1 no record, left out. Pend.
4. ML #58. NP.
5. ML #92. Piece. Plans (K3: 10 lines). Touches 0 (the only record in the window is left out by RT5(b)). C1 no record, left out. Pend.
6. ML #64. NP.
7. ML #93. Piece. Plans (K3: 232). Touches 1. C1 undecided, listed (its only own-spec records are a build review, 3 other-kind records and 1 unclassed). Pend.
8. ML #13. Piece. Research (K3: only research files). Touches 0. C1 FAIL. It has a question Q-008 and no memo, so the Critic's check 0f1c0335 is the one that applies (reading (ii), FAIL, 2 rounds). The source-check record f33fac53 also reads FAIL. Pend.
9. ML #25. NP.
10. ML #47. NP.
11. ML #73. Piece. Research (K3). Touches 0 (1 taken off by a "later work" code). C1 FAIL (memo Q-009's source check be10cf2b, (ii), 2 rounds; the Critic's 4241d270 also FAIL). Pend.
12. ML #77. NP.
13. ML #55. NP.
14. ML #59. NP.
15. ML #42. NP.
16. ML #56. NP.
17. ML #81. Piece. Research (K3). Touches 1. C1 FAIL (memos Q-015 and Q-016: cba2f3bb and 41905828, both (ii) FAIL, 3 rounds). Pend.
18. ML #27. NP.
19. ML #78. Piece. Research (K3). Touches 0. C1 no record, left out. Pend.
20. ML #32. NP.

Random part, Service-Desk (10 with 30d complete, 10 without):
21. SD #233. NP (merged by a bot; only records files).
22. SD #230. Piece. Built (K3: built 596 against plan 41). Touches 0 (4 taken off). C1 FAIL (build reviewer.md 8eae195c, (ii), 2 rounds; stage review r1 23917e4b, (i), FAIL; r2 gives none). Pend.
23. SD #105. NP (bot-merged).
24. SD #76. NP.
25. SD #237. NP (RP2, ruled T1: only owner question and answer files and records).
26. SD #150. NP.
27. SD #109. NP.
28. SD #341. Piece. Built (K3: 24 lines). Touches 0 (its record 8e21866a was first added at the dispatch instant, so it is the starting ruling, RT4). C1 PASS (reviewer.md 3ea324e4, reading (iv), PASS; _reviewer-verbatim.md 69809936 gives none). Pend.
29. SD #93. NP.
30. SD #329. NP.
31. SD #22. Piece. Plans (K3: 13). Touches 0 (its two records are read from the dispatch commit; no later add in the window). C1 no record, left out. NR (30d).
32. SD #51. NP.
33. SD #21. NP.
34. SD #61. Piece. Plans (K3: plan 1471 against research 28). Touches 0. C1 no record, left out. NR.
35. SD #26. Piece. Plans (K3: 196). Touches 1. C1 no record, left out. NR.
36. SD #57. NP.
37. SD #25. Piece. Plans (K3: 80). Touches 0. C1 no record, left out. NR.
38. SD #6. NP.
39. SD #31. Piece. Plans (K3: 12). Touches 0 (ad5eedfa first added at the dispatch instant, so starting ruling). C1 no record, left out. NR.
40. SD #47. NP.

Random part, Personal-Org-Operating-Model (10 with 30d complete, 10 without):
41. POOM #35. Piece. Built (K3: built about 3,500 against plan 634). Touches 2. C1 FAIL (S-033 build review round 1, 675ec21d, (i), FAIL). Pend.
42. POOM #11. NP.
43. POOM #47. Piece. Plans (K3: 120). Touches 0 (its only question file was first added after the merge). C1 FAIL (plan review 65934264, (i), FAIL; its build records are not of the plan kind). Pend.
44. POOM #19. NP.
45. POOM #32. NP.
46. POOM #52. NP.
47. POOM #30. Piece. Built (K3: built 588 against plan 149). Touches 4 (2 taken off). C1 undecided, listed (its only build record, 63a11d59, gives no round-1 verdict; its plan records are of another kind). Pend.
48. POOM #48. NP.
49. POOM #53. NP.
50. POOM #50. Piece. Built (K3: 175 against 4). Touches 0. C1 PASS (3fed3942 (iv) PASS; f5ba9a62 (i) PASS). Pend.
51. POOM #49. Piece. Built (K3: 547 against 109). Touches 1. C1 PASS (0e5d0a2e (i) PASS, f5ba9a62 (i) PASS; cdb45b88 gives none). Pend.
52. POOM #27. Piece. Built (K3: built 2520 against plan 1066). Touches 4 (6 taken off). C1 FAIL (reviewer.md b835d08f, (iii), FAIL). Pend.
53. POOM #15. NP.
54. POOM #24. Piece. Built (K3: only built, 60). Touches 0. C1 FAIL (063b6a95, (ii), FAIL). NR.
55. POOM #23. NP.
56. POOM #14. NP.
57. POOM #25. Piece. Plans (K3: plan 258 against built 129). Touches 3 (8 taken off). C1 FAIL (plan review 03b9d86d, (i), FAIL). NR.
58. POOM #18. Piece. Built (K3: 20 against 2). Touches 0. C1 FAIL (d019f699, (iii), FAIL). NR.
59. POOM #22. Piece. Built (K3: 455 against 106). Touches 1. C1 PASS (7054833b, (iv), PASS). NR.
60. POOM #20. Piece. Built, by K2 (three trailers briefs s-017, s-018, s-019, role `-tb-` read as tools-builder by K2's short-form table; no brief records exist, so dispatch is the first commit). Touches 4. C1 FAIL (48a85c6f, (iii), FAIL). NR.

Edge-case part (14):
61. SD commit 9e46dd84 (drawn E-RP1). Frame D. 2 parents, no files, agent: a local merge. NP by RP1 (no pull request). This is work the measure cannot see.
62. SD commit 04511022 (E-RP1). Frame D. 1 parent, 4 records files: a direct push. NP by RP1.
63. SD #147 (E-RP2). Closed unmerged by the owner. NP by RP1. 1 commit (an owner question-or-answer file). RT3(b) cannot be tested from this sample: the extract gives `rt3b_matches` only for merged rows. No sampled merged piece lists any closed-unmerged match.
64. SD #174 (E-RP2). Closed unmerged by the owner, no commits. NP by RP1. Same RT3(b) note.
65. SD #316 (E-RP3). NP (RP2: a class-other file and records only).
66. ML #69 (E-RP3). NP (RP2: a class-other file and records only).
67. ML #98 (E-RP4). Piece. Plans, by K2: its trailers name two briefs (258, 263), both Definer, so one piece with one kind. Touches 0 (the only question file, class "part of a value target", was first added after the merge). C1 undecided, listed (only record c50bbebd, unclassed). Pend.
68. SD #78 (E-K1). Piece. Built (K3: built about 12,330 against plan about 5,441 and research 200). Touches 16 (12 under RT1(a), 4 under RT7). C1 FAIL (_build-review-round<n> 9c0ec757, (i), FAIL). Pend.
69. SD #148 (E-K1). Piece. Plans (K3: plan about 2,533 against built 73 and research 42). Touches 1. C1 undecided, listed (its records are build-kind reviews or other kinds). Pend.
70. SD #36 (E-K2). Piece. Plans, by K2's short form `-def-` (a role in K2's list once the short form is read). Touches 0. C1 no record, left out. NR.
71. SD #319 (E-RT2). NP (RP2: a class-other file and records).
72. SD #300 (E-RT2). Piece. Research (K3: only research file). Touches 2. C1 FAIL (the Critic's check, `_critic-r<n>` 9f16cd20, (i), FAIL; others give none). Pend.
73. SD #52 (E-RR2). Piece. Built (K3: only built files). Touches 0. C1 FAIL (reviewer.md 6fc7083c, (iii), FAIL). NR.
74. SD #11 (E-RR2). Piece. Built (K3: only built files). Touches 0. C1 FAIL (2d2438a5, (iii), FAIL). NR.

Counts: 33 pieces. By kind: plans 14, built 14, research 5. By repository: ML 9, SD 13, POOM 11. The random part holds 26 pieces (ML 8, SD 7, POOM 11) and the edge part holds 7.

C1 results over the 33: PASS 4 (SD #341, POOM #50, #49, #22); FAIL 16 (ML #43, #13, #73, #81; SD #230, #78, #300, #52, #11; POOM #35, #47, #27, #24, #25, #18, #20); undecided 4 (ML #93, ML #98, SD #148, POOM #30); no record and left out of this measure 9 (ML #29, #92, #78; SD #22, #61, #26, #25, #31, #36).

Reopening: 13 NR (the 30d column), 20 pending, 0 reopened. Pieces with 30d complete: SD #22, #61, #26, #25, #31, #36, #52, #11; POOM #24, #25, #18, #22, #20.

B. TOUCHES PER PIECE
Window = after dispatch and before merge. Every touch below is RT1(a) or RT7 unless stated.

RT1(b): the owner-account comments I found are POOM #35 (1), POOM #30 (2), POOM #18 (1, and a session record shows it posted), SD #78 (1) and SD #11 (3, session record shows posted). All carry the agent footer, so they are the agent's, not touches. There are none on the Model-Lab pieces. RT2: the owner-identity web-editor commits on pieces change only records files, so none is a fix. RT3(a): no review exists on any of the three repositories. RT3(b): no match. RT5(b)/(d): the only record in a piece's window that RT5 leaves out is ML #29's 3ae73360 (class "A phase gate") and ML #92's b3609d4c ("Part of a value target"). RT6: no record is counted on two sampled pieces.

Model-Lab
- #29: 1. Decision 9acdfce2 (class "Accepting an unknown as open", RT5(c)), first add 11-02 00:38:22 (d7f8549a), 1 owner line, code "this piece". Its question 8628e3d2's file does not name #29. Tagged Discovery-8, so listed under Open question 13. Not counted: 5e700c74, a question file first added 00:43:43 (coded later work); 3ae73360 (RT5(b) phase gate; first add and 5 appends); decisions b6081c5a and 66512cad (first added after the merge).
- #93: 1. Question 0d05d5f2, timed at its question file 22147854's first add 11-11 03:08:30. Decision 31505fb6 (first add 03:50:31, 2 owner lines) is the same question. Both "this piece". Tagged Discovery-8, so listed. Not in window: 4973eb45 and 56004034 (class "A phase gate, its ceilings, a value target's terms, the acceptance of open unknowns and of a milestone", left out whole under RT5(b)).
- #81: 1. Question 813d3838, file 30491519, first add 11-09 05:32:16, no owner words (a question file counts at its first add), "this piece". Its decision is after the merge.
- #92, #43, #13, #78, #98, #73: 0.

Service-Desk
- #26: 1. Decision b2697809 (question 64fbc9af), first add 10-04 16:11:10 (4977c952), 1 owner line. Not counted: 233211a9 at 4977c952 (not an append: adds 1, removes 3, a ruling's words changed; listed) and 21334cb2 (no owner words); 4782268e and 1d370480 (files ending -notes.md).
- #148: 1. Question 692b8dc7, file 552be005, first add 10-19 21:43:10.
- #300: 2. Question 4bc380fd (file 76fc6d56, first add 11-04 22:17:16) and question 96ef8dad (file c2476643, first add 11-05 16:24:30). Their decisions are first added after the merge. Appends to the question files add no owner words.
- #78: 16.
  RT1(a), 12 (commit times on 10-16, record d38d8364 unless stated): 12:11:02 (5f36faa0), 13:35:07 (fd5d7a8e), 16:42:39 (5f6d7303), 16:42:39 (b8ca4c9c), 16:42:40 (7e3e6071), 16:42:53 (680797bd), 17:05:56 (17762604), 17:21:23 (1cf4987a), 17:35:13 (3719ea74), 17:39:03 (50853e61), 17:56:50 (2846118f), and decision 7d757252's first add at 20:29:14 (1382e156).
  RT7 code, 4 (listed for the Critic): 13:28:21 (14d854aa), 16:42:38 (01221fd4), 16:42:39 (79afa01b), 16:42:39 (c0ab80c5). All coded "this piece". d38d8364's first add is the dispatch instant, so it is the starting ruling.
- #230, #341, #22, #61, #25, #31, #36, #52, #11: 0. SD #341, #22, #31 and #26 hold decisions first added at their dispatch instants (starting rulings, RT4), and none of those has a later add in the window.

Personal-Org-Operating-Model
- #35: 2. Append to answer record 0d5230c0 at 10-17 16:13:32 (cac877e8), naming no question id. Question Q-024: its file 14b7aecb first added 16:19:03 and the append at 17:59:31 (59c359a1) naming Q-024 are one question, timed 16:19:03. 0d5230c0's first add is the dispatch instant (starting ruling). Ledger entry 5be98217 (17:59:31, asks Q-024) is skipped (record whose words skipped it: 0d5230c0 at 17:59:31).
- #30: 4. Answer record 455192c4: first add 10-13 20:24:30 (667e193c), appends 20:47:13 (879f5e3a) and 22:06:38 (83cc104b). Ledger entry aa4bb0c6 (20:47:28): counted. Its three passages are in no single counted record (its second passage is nowhere in the extract). Skipped: ledger f3a6b509 (words in 455192c4's 22:06:38 append). Coded later work (not touches): 4efc6a60 first add 22:13:25 and append 23:15:11; ledger 9754623d (also a later-work code). Ledger 56c65486 names no piece.
- #49: 1. Question Q-031 (file de17627b, first add 11-05 16:38:01, 568cd6e0), coded "not said" (first Critic "later work", second "this piece"), so it counts and is listed. The 17:03:38 append (0e57b841) is a question file with no owner words. Ledger 447cf875 skipped (starting rulings 08ba8ef8, 558fd054, 959abcab).
- #27: 4. Answer record c4fc482f appends at 10-13 03:18:48 (dcc1e652), 03:43:00 (546dbdf3), 12:49:18 (93ed08cd), 13:28:50 (261d78fa). Its first add is the dispatch instant (starting ruling). Ledger 71ba6fcf skipped (c4fc482f 03:43:00). Ledger 4c0ded4f skipped (c4fc482f 12:49:18 and 13:28:50). Ledgers 71c48d9c and 3058ae12 name no piece. All of e219aae3, 2cb87e77 and 5f201b8e are coded later work (section D).
- #25: 3. Answer record ad6df430: first add 10-11 01:00:35 (e3086031), appends 14:31:36 (6e37e45e) and 15:42:40 (71bff0be). Ledgers 8c0b9957 and cf45170a skipped (words in ad6df430). Records e219aae3 and 2cb87e77 coded later work.
- #22: 1. Ledger entry 20cf0bd6 (10-08 17:20:58, c1373c42), counted.
- #20: 4. Ledger entries d4f9e0fe (10-05 17:07:42), 0ccd2fd5 (17:26:38), 689b54b0 (17:54:04, whose passage stands in 0ccd2fd5's, but one entry never skips another, so both count) and 878518f1 (19:50:39).
- #50: 0. df986385 is first added at the dispatch instant (starting ruling); ledger 3b79e454 skipped (words in df986385). Owner instruction file 104f5eb5 is listed only.
- #47, #24, #18: 0.

C. SHARES (pieces with at least one owner touch before merging)
- All: 14 of 33 (42.4%). Model-Lab 3 of 9, Service-Desk 4 of 13, Personal-Org-Operating-Model 7 of 11.
- Random part: 11 of 26 (42.3%). Model-Lab 3 of 8, Service-Desk 1 of 7, Personal-Org-Operating-Model 7 of 11. Edge part: 3 of 7.
- Touch totals: 42 (ML 3, SD 20, POOM 19).
- Without the "later work" codes, so every question counts on the piece under way: 16 of 33 (ML 4 of 9, SD 5 of 13, POOM 7 of 11); random part 13 of 26. Touch totals 64 (ML 5, SD 24, POOM 35).

D. THE TWO FIGURES
1. Touches the "later work" codes take off: 22 in all. Model-Lab 2 (#73: 1; #29: 1, question file 5e700c74). Service-Desk 4 (#230: 4 question files). POOM 16 (#30: 2; #27: 6; #25: 8). I counted a touch as taken off if it would count, with skipping applied, when no code is read. On #30 the later-work code on ledger 9754623d takes nothing off, because with no codes 4efc6a60 would count and would skip it.
2. Pieces changed from needing the owner to not needing: 2 (ML #73 and SD #230). From not needing to needing: 0. I found no question coded "later work" on one sampled piece that counts on another. Records shared between sampled pieces (e219aae3, 2cb87e77, 4efc6a60) carry the same code on each.

E. LISTS THE RULES ASK FOR

Questions or notes coded "later work" or "not said" (row, commit; no text). Rows marked (NP) are on non-pieces.
- ML #29: 5e700c74, rows 2 (12454c30), 3 (45d2bfd4).
- ML #58 (NP): b1d4ead4, rows 10 (387af768), 11 (207c8ba6).
- ML #47 (NP): 3ba984e1, rows 15 (85e8c0ae), 16 (1d8ddc41), 17 (1fdbf479), 18 (e0543be0), 19 (7884bb78); 5a41a066, row 20 (4a446274).
- ML #73: 9ea16fdb, row 21 (78f74919).
- SD #230: b793d0d9, 6ab2fa98, 446c689a, rows 23 to 25 (all 543527d2); e469c207, row 26 (21060101).
- SD #237 (NP): 5ae5d612, row 27 (7234f058); b0dc8e16, d184bc0b, f24d03df, 9e91287e and 2780ba86, rows 28 to 32 (all 97429c02).
- SD #26: 4782268e, row 35 (4977c952), "not said" (a -notes.md file, so not a touch anyway).
- SD #300: e24f55f9, row 124 (e67251eb), no owner words either way.
- POOM #11 (NP): ledger 730a2fac, row 43 (e049ddde). POOM #32 (NP): 74b08fff, row 44 (89fe4da1).
- POOM #30: 4efc6a60, rows 48 (439db48a), 49 (72b51377); ledgers 56c65486, row 50 (6b348bac), and 9754623d, row 53 (c402fefa).
- POOM #53 (NP): c4c7c231, rows 54 (d5da01cb), 55 (ccfce1ca); 5b41d98e, rows 56 (f06a6378), 57 (d5da01cb), 58 (ccfce1ca).
- POOM #49: de17627b, rows 60 (568cd6e0), 61 (0e57b841), "not said", both readings shown above.
- POOM #27: e219aae3, rows 63 to 69 (ebbc97b7, 25901b57, 6c7f76f5, 72175182, 59d7e26a, d9ca7ec0, 8485c986; read before the record names #27, so not read for it), 70 (ab8b0471), 71 (c2169dd0); 2cb87e77, rows 72 (a3c2b6e0) and 73 (7a7b5588; not read for #27), 74 (b69270eb), 75 (fc359f9c; adds no owner words), 76 (925d8be9); 5f201b8e, rows 81 (1a18e855), 82 (e98bd1da), 83 (5b4e82a7), 84 (a0e2585f); ledgers 71c48d9c, row 85 (0ea97377), and 3058ae12, row 86 (6ba7f05f).
- POOM #25: e219aae3, rows 92 (221a9cb4), 93 (b1ce9f0b), 94 (a4c068bb), 95 (9a7bd056), 96 (ebbc97b7); 2cb87e77, rows 97 (8ae9dc9e), 98 (26408956), 99 (be28fa52).
Totals agree with the extract: 61 "later work" (ML 11, SD 11, POOM 39) and 3 "not said".

RT7-coded: the 4 SD #78 notes listed under B.

Ledger entries: counted are POOM #30 aa4bb0c6; #22 20cf0bd6; #20 d4f9e0fe, 0ccd2fd5, 689b54b0, 878518f1. Skipped are #35 5be98217 (0d5230c0); #30 f3a6b509 (455192c4); #50 3b79e454 (df986385, the starting ruling); #49 447cf875 (08ba8ef8, 558fd054, 959abcab, starting rulings); #27 71ba6fcf and 4c0ded4f (c4fc482f); #25 8c0b9957 and cf45170a (ad6df430). Not counted (names no piece, or coded later work): #30 56c65486 and 9754623d; #27 71c48d9c and 3058ae12.

RT5: counted rulings tagged with a gate or value-target milestone are ML #29's 9acdfce2 (Discovery-8) and ML #93's 22147854 and 31505fb6 (Discovery-8). Left out in a window: ML #29 3ae73360 and ML #92 b3609d4c (their classes are exactly "A phase gate" and "Part of a value target"). Left out whole, class not exactly one of those, listed: ML #43 58cc6884 and 7196c3a9 ("Touches the value target (term 1) and a rule change (term 4)") and ML #93 4973eb45 and 56004034 (class as above). None falls in a piece's window. Stop-rule records read under RT5(a) (ML #43's, class "A choice under the plan stop rule…") also fall outside its window.

Owner items listed only, added in a piece's window: ML #92 intake copy of an answer b97ada67 (11-11 02:32:58); ML #98 intake item a62f6a50 (11-11 19:11:42); POOM #50 instruction file 104f5eb5 (11-06 00:21:35, names #50 by number and spec); SD #148 four reference files 1c669f9a, 96e547ef, bcc111f8 (10-19 21:02:09), 0695bbf6 (10-20 13:56:12).

Commits listed as not appends (adds no owner words, or its words are matched): SD #26 4977c952 (on 233211a9); POOM #27 5b4e82a7 (11-12 21:52:44) and a0e2585f (21:54:24), both on 5f201b8e. Changed-text pairs matched away: those three, plus POOM #25's be28fa52 (a counted append; one line remains unmatched).

E-RT2 (a tool's default identity; not a touch; listed): SD #319, 57d1b19e; SD #300, 11 commits (bbb63009, 82c7e1e8, 68148cb8, 68e2bccb, a79c3071, 174f3164, 4ea80e84, 4fe15960, 5ca92119, 2cb0a663, 79fba275); POOM #25, e49d0946; POOM #20, b5f0dfdc, d4f8a111, 8abb34e5. All carry an agent session trailer and no files.

E-RR2 candidates (later merged pull requests sharing a file, and later commits naming the number; none is a revert):
- ML: #43 #44, #51; #29 #31, #39, #44, #51 and commit b6d588c8; #92 #93, #97, #98; #93 #94, #97, #98 and 4 commits (5aefa062, e9f1f2f5, 130e78ac, 75ccb647); #13 commit 1bfb69e9; #73 #74; #81 #82; #98 #99; #78 none.
- SD: #341 #342 and commits edfdc13a, d2c8a200, 461b9f72; #61 #66, #69, #72; #300 #310, #316, #320 and commits ef83ea7b, 340bdca7; #11 #14, #18, #27, #48, #65, #148; long lists (counts) #230 21, #22 28, #26 24, #25 25, #31 22, #78 75, #148 10, #36 46, #52 49, with numbers in `after_merge.later_prs_sharing_a_file`.
- POOM: #35 #38, #46, #49, #50; #47 #49; #30 #34, #35, #38, #46, #49, #50 and commit d34a7fd4; #49 #50; #22 #26, #27, #30, #49; #27 10, #24 8, #18 10, #20 10 (long lists in the extract); #50 and #25 none.

F. CASES I COULD NOT DECIDE FROM THE EXTRACT, AND WHY
1. C1 undecided: ML #93 (build review only), ML #98 (unclassed only), SD #148 (build-kind only), POOM #30 (own-kind record gives no round-1 verdict). Listed under the owner's rulings 12 and Q-018/U3.
2. SD #300's check kind. It has no memo and no research-question file, so I took its research file as an experiment registration (the Critic's check applies; FAIL). Read as a memo piece it would be undecided. The extract's piece_by says "experiment or question id".
3. Unit of a touch for an answer record's first add that holds several answers (one touch) and for appends in the same second (one each). That is my reading of RT1(a); the rule does not say.
4. "Not said" codes: POOM #49 de17627b counts and is listed with both readings. SD #26 4782268e is a notes file, so it does not count under RT1(a) in any case.
5. Model-Lab owner comments: none exist on the sampled pull requests, and Model-Lab's agent marks have not been read, so RT1(b) there is untested beyond "none found".
6. My kind sums (K3) are by-hand; the narrowest margins are POOM #25 (258 against 129) and ML #43 (347 against 168).
7. RT3(b) for the closed-unmerged items cannot be read from the extract (see 63 and 64 above).

G. AWKWARD CASES
Seen: E-RP1 (2 commits), E-RP2 (SD #147, #174), E-RP3 (SD #316, ML #69), E-RP4 (ML #98), E-K1 (SD #78, #148), E-RT2 (SD #319, #300), E-RR2 (SD #52, #11). E-K2 was drawn on SD #36, but with the short forms its role is in K2's list, so E-K2's own case is not seen; the short-form table is exercised on SD #36 and POOM #20. Not seen (no match in the frame at the draw): E-RP5, E-RP6, E-K3, E-RT1, E-RT3. Not sampled (for the Critic): E-RT4, E-RT5, E-RT6, E-RR1, E-RR3.
Untested on past records, as the question says: RT1(c), RT2(b), RT3(c), RT7's touch-log part, RR1(b) and (c), and K4 (trials only). RT7 from files is listed only (owner instructions, intake items, reference files).

H. FIELDS ABSENT OR NOT READ
- Records' text, path text, comment text and ledger text are not in the extract (by design); `later_work` is the only text reading.
- Model-Lab and Service-Desk ledgers are not read (null). Reviews do not exist on any of the three repositories.
- Closed-unmerged matches (`rt3b_matches`) appear only on merged rows; frame U rows lack `c1`, `after_merge` and `ledger_entries`.
- `question_id` is non-null only for POOM; first-added times for starting-ruling checks are read as equality with the dispatch time, because the extract gives no per-record first-commit flag in the lines I searched.

I. CONTRACT
- changed: nothing. I wrote no file; this return is the memo.
- why: brief 333, Q-018 re-coded on the owner's rulings 11 and 15 to 19.
- verified: read research/Q-018.md, research/Q-018-extract/README.md, sample.json and sample.jsonl by field searches, plus the repository's AGENTS.md, my charter and brief 333 as instructed. I did not recompute the 33-piece list a second way, and the K3 sums are by hand.
- undone: no second reading of every record; no check of sample.jsonl against frame files. The take-off figure rests on my skip logic for ledger entries (section D).
- needed outside your surface: the Critic's step-5 check of this coding against the records, especially the sections B and D counts, the C1 readings in A, and cases F1 to F3.
- open questions: (1) Is an answer record's first add with several answers one touch? (2) For a piece with no memo and no question file, does the Critic's check apply (SD #300)? (3) Should POOM #20's and ML #98's dispatch times be re-checked against their brief records, since the extract reads earlier of two?

Files: /home/user/Model-Lab/research/Q-018.md, /home/user/Model-Lab/research/Q-018-extract/README.md, /home/user/Model-Lab/research/Q-018-extract/sample.json, /home/user/Model-Lab/research/Q-018-extract/sample.jsonl.
