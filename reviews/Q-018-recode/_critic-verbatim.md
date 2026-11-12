# The Critic's step 5 again: the re-coding against the records (brief 299)

*Recorded verbatim by the Orchestrator; the verdict file is reviews/Q-018-recode/critic.md. Brief 299 (docs/briefs/299-critic.md), on Model-Lab@69879e2, research/Q-018-memo-2.md (brief 298), with a records pack built by pack.py and pack2.py in this session's scratchpad (real paths, full messages, records as first added and their in-window diffs; not committed, as it holds free text). The Critic runs on a different model from S-002's writer (D-056) and apart from the Researcher.*

Verdict: FAIL

**In plain words.** First, what failed. Most of the corrected rules now give the right result against the records. That covers the first-check rule on every case my first check named, the comment rule, the starting-ruling rule and the gate-ruling rule. One thing still goes wrong: the question rule misses many of the owner's answers given while a piece was under way. It misses them in two ways.
- In Service-Desk, the owner's answers are written inside numbered lines or in plain quotation marks. The rule's test for "the owner's words" does not read that form. One piece shows 15 answer entries as holding no owner words.
- In the operating-model repository, the owner's answers are kept beside the plan reviews, not in the folders the rule reads. Three of its ten pieces are counted as needing no owner touch when the records show the owner answered while each was under way.

This changes the share the target is measured on, so the hand check cannot close yet. Both faults are in the rules, not in the Researcher's coding, and both go to the Definer. Nothing here is irreversible. I am flagging a self-implication: my earlier checks passed the wording of this owner-words test (finding 8).

## Findings

**1. Blocking. RT1(a)'s owner-words test misses Service-Desk's answer form, so Service-Desk #78 is under-counted.**
- Rule: S-002.md:47, "no `Ruling:`, `Answer:` or `Decision:` line, and no quoted line …". The extract reads these labels only at the start of a line, and quotes only as lines starting `>`.
- Record: the piece's own decision record d38d8364 (Service-Desk decisions/questions/P-001-trial-view-notes-2.md). It has 15 commits inside #78's window (11:54:38 to 20:40:27), each adding text. All 15 are coded `owner_word_lines: 0` (pack records2/Service-Desk--d38d8364.md:20 to :688).
- What the text shows: they hold the owner's answers as `1. "<question>" Answer: "<choice>"`. Examples: 17762604 at 17:05:56 (:604-607), 50853e61 at 17:39:03 (:680-682), and 2846118f at 17:56:50 (:699-700, a choice under the plan stop rule). Others are the owner's messages "verbatim" in double quotes, such as 1cf4987a at 17:21:23 (:624-625) and 5f36faa0, 14d854aa and 01221fd4.
- Result: the memo's "1× RT1(a)" for #78 (memo :126) is right under the rule's words and wrong against the records. It should be about 15 touches more.
- #78 still has at least one touch, so its own V1 result is unchanged. But the same test decides every Service-Desk append, and it fails on the repository's usual form.
- Fix (Definer): count a line holding `Answer:`, `Ruling:` or `Decision:` anywhere, and a double-quoted passage under a line naming the owner's words, answer, note or ruling, as well as `>` quotes. The extract then needs re-running for this field only.

**2. Blocking. RT1(a) reads only top-level `questions/` and `decisions/`, but Personal-Org-Operating-Model keeps the owner's answers in `reviews/S-0nn/_owner-answer(s)*.md`. This changes V1 for three of its ten pieces.**
- At the cut-off that repository has no `questions/` or `decisions/` folder (Glob: none). Its answers are filed beside the plan reviews, and C1 already classes them as "of another kind".
- Each of these pieces is coded "none" in memo :100, :105 and :110:
  - **PO#30** (window 2026-10-13 19:24:29 to 10-14 00:22:10). reviews/S-029/_owner-answers-2026-10.md gets owner answers in commits 667e193c (20:24:30), 879f5e3a (20:47:13) and 83cc104b (22:06:38) (pack L47:65-178).
  - **PO#25** (window 10-10 21:56:54 to 10-12 01:25:51). hc/Personal-Org-Operating-Model/reviews/S-022/_owner-answers-2026-10.md:16-20 holds two answers given at approval on 10-11. They were added by 6e37e45e (14:31:36) and 71bff0be (15:42:40) (pack L57:74-81).
  - **PO#27** (window 10-12 01:18:05 to 10-13 15:20:19). reviews/S-025/_owner-answers-2026-10.md:16-38 gets answers D5-1 to D5-6, B1 (a choice under the build stop rule) and B2. They were added by dcc1e652 (03:18:48), 546dbdf3 (03:43:00), 93ed08cd (12:49:18) and 261d78fa (13:28:50) (pack L52:126-320).
  - PO#35 already counts 1, and reviews/S-033/_owner-answers.md adds more (pack L41:241-301).
  - PO#49 and PO#50 are right: their answer records are added in each piece's first commit, so RT4 applies (pack L51:174-180, L50:122-128).
- Fix (Definer): name each repository's owner-answer paths for RT1(a), as C1 now names its check-record paths. For Personal-Org-Operating-Model that is `reviews/<folder>/_owner-answer*.md`, and possibly ledger entries that quote the owner. For appends to those files, time each one by its commit.

**3. Non-blocking. An edited `Ruling:` line counts as new owner words (Service-Desk #26).**
- Record: 233211a9's in-window "append" 4977c952 at 16:11:10 changes `Ruling: yes` to `Ruling: yes, phone; yes`. It only reshapes text already given at dispatch, and the owner's quoted words do not change (records2/Service-Desk--233211a9.md:14-36).
- So #26 should count 1, not 2. The result "at least one" is unchanged.
- Fix: an append counts only for owner-word lines that the same commit does not remove in another form.

**4. Non-blocking. Memo :157 says "16 comments on 11 pull requests". The sample has 12 on 9.**
- The 12 are SD#6, SD#11 ×3, SD#78, SD#147, SD#174, PO#11, PO#18, PO#30 ×2 and PO#35 (github_reads.json:9-126; pack owner_account_comments). The memo's own list at :174-176 also adds up to 12.

**5. E-RT5 (brief item 2).**
- All 12 comments under the owner's account on sampled pull requests carry the footer. None has a session link.
- A session's records show 5 of them were posted by a session: SD#6 (1), SD#11 (3) and PO#18 (1) ("reviewer comment(s) on PR #n" lines, pack L38:53, L74:71, L58:77).
- On pieces, the old rule would have counted 8: SD#11 ×3, SD#78, PO#18, PO#30 ×2 and PO#35. None of the 8 was the owner stepping in. The corrected RT1(b) counts 0, which is right.
- The other 4 are on non-pieces (SD#6, PO#11) or on pull requests closed unmerged (SD#147, SD#174). SD#147's comment comes 9 seconds after the board-scope answer was recorded (21:07:26 against 21:07:35), and carries the footer.
- Comment text is not in this pack, so I read marks, not words. Model-Lab stays untested (none of its sampled pull requests has a comment).

**6. E-RT4, E-RR1 and E-RR3 (brief item 3).**
- **Option A's ten (hash order across the three repositories, my reading).** These are taken from my earlier finding 7. I could not recompute the SHA-256 order without a shell.
  - SD#230: 4 questions name only M3E and the spec. They are now counted as the piece's own files, filed for later work (Open question 11).
  - SD#237: 5 questions name only M3G. They are counted as own files but are not about #237 (Open question 11).
  - SD#341: none (its starting ruling, RT4, right).
  - ML#29: open-unknowns (Discovery-8) is counted and listed (Open question 13), which is right. accept-m1 is counted as an own file (Open question 11). design-gate is left out by RT5, which is right.
  - SD#22: none (RT4).
  - ML#92: trial-gates is left out by RT5(b), which is right.
  - SD#78: no milestone-only record, but finding 1's appends are missed.
  - SD#148: board-scope names only MD2 and was answered in the window. It is missed (Open question 14). decisions/questions/P-001-design-reviewer-verdict.md names neither the piece nor a milestone (:3 "Milestone: none") and is dated 2026-10-20 in its text. It is also missed; I could not time its commit without git.
  - PO#35: none milestone-only, but finding 2 applies.
  - ML#43: none.
- **Option B's ten (sample.jsonl line order):** ML#43, #29, #92, #93, #13, #73, #81, #78, SD#230 and #237.
  - Option B swaps 5 items: ML#93, #13, #73, #81 and #78 come in for SD#341, SD#22, SD#78, SD#148 and PO#35.
  - ML#93's brief-stop is Discovery-8, counted as an own file and listed. It was asked about the piece.
  - ML#13: 0, which is right now that matching by path is dropped.
  - ML#73 and ML#81's research-stop-3: counted as own files, which is right.
  - ML#78: none.
  - So option B would not find findings 1 and 2's misses, which sit in SD#78 and PO#35.
- **E-RR1 and E-RR3.** The RR rules are unchanged since my first check (finding 8, none found).
  - A fresh search of Service-Desk reviews for #11 and #52 finds only #54's review checking against #52's code, which builds on it (reviews/54/reviewer.md:3, :8), and #78's review using PR #52 as test data.
  - Neither reverts or fixes either piece. A fix that names nothing (E-RR3) cannot be found by search.

**7. Brief item 4: the memo's undecided cases.**
- **(a) ML#98, unclassed-only: a rule fault.**
  - c50bbebd (reviews/P-002-two-look-line/reviewer.md) is the Reviewer's run of the experiment's line script. That is a check of another kind of work than the plan, and it fits no Model-Lab path form. C1 says nothing about a piece whose only record is unclassed.
  - Treat it like "another kind": undecided, listed. Note that under Open question 12(b) it would become FAIL: its round 1 is FAIL at hc/Model-Lab/reviews/P-002-two-look-line/reviewer.md:5-7, before the merge.
  - The plan review reviews/S-002/plan.md is first recorded after the cut-off (brief 271, recorded 2026-11-12), so it is rightly not read.
- **(b) PO#20, the K2 short form: an extract gap.**
  - K2's table now maps `-tb-`, and the trailer reads `-tb-s018` (my earlier finding 9). The extract still writes role null.
  - Carry the short form as a role in the extract. The result, built, is right either way.
- **(c) Research pieces, memo or no memo: an extract gap.**
  - The pack's real paths settle each one:
    - ML#73 has research/Q-009-memo.md, so its source check governs.
    - ML#81 has Q-015-memo.md and Q-016-memo.md.
    - ML#13 has no memo (research/Q-008.md only), so the Critic's check reviews/Q-008/critic.md governs. The extract also took Q-008-source-check.md, which checks a memo this piece does not carry.
    - SD#300 is an experiment registration, so its Critic r1 governs.
  - All are FAIL either way. Add a "piece has a memo" field.
- **None of (a) to (c) is a question for the owner.**

**8. Self-implication (D-050).**
- In my rules check (reviews/Q-018-rules/_critic-verbatim.md:137-139) I called SD#78's appends "right in kind", taking its in-line `Answer:` lines and double-quoted words as owner words.
- I then passed the narrower wording in later rounds, and the extract's quoted-line test in brief 297 (reviews/Q-018-extract-widened/_critic-verbatim.md:68).
- I never checked where Personal-Org-Operating-Model keeps its answers.
- Triage should count findings 1 and 2 as issues my checks missed.

**9. The other cases, against the records (brief item 1).**
- **My first finding 1 (C1 reading the top verdict):** now right for each case.
  - SD#11: FAIL (iii) (pack L74:69).
  - SD#78: FAIL, from 9c0ec757 (i) (L68:928).
  - SD#52, PO#18, PO#27 and PO#20: FAIL, as in brief 297's item 2.
- **My first finding 2 (C1 paths):** now right for each case.
  - ML#73 and ML#81: FAIL.
  - PO#24: FAIL (ii).
  - PO#50: PASS (iv) and (i) (L50:150-151).
  - ML#78: left out.
  - PO#47: FAIL.
  - SD#148: undecided (Open question 12).
  - SD#300: FAIL.
  - ML#93: undecided.
  - PO#25: FAIL.
- **My first finding 3:** right, 0 counted.
- **My first finding 4:**
  - (a) wrong, as finding 1 above shows.
  - (b) the notes file and the Critic's verdict record are out, which is right.
  - (c) matching by path is dropped, which is right (ML#13 is 0).
  - (d) RT5's class test is right on ML#29 and ML#92.
  - (e) ML#29 now counts its question and answer as one.
- **My first finding 5 (starting rulings):** right for SD#341, SD#26 and SD#78 (L28:41, L68:922).
- **My first finding 9 (the other edge cases):** right.
  - E-RP1: 2 commits.
  - E-RP2: #147 and #174.
  - E-RP3: SD#316 and ML#69, whose only non-records file is governance (L65:12, L66:11).
  - E-RP4: ML#98 is plans by K2.
  - E-RT2: SD#319 (records only) and SD#300.
  - E-K1: SD#78 is built and SD#148 is plan.
  - E-K2: SD#36 is plans.
- **Random-part spot checks (13 items):** each has the right kind and first check, and touches right except where findings 1 to 3 say otherwise.
  - Model-Lab: #43, #13, #73, #81 and #93.
  - Service-Desk: #230, #341, #26 and #61.
  - Personal-Org-Operating-Model: #25, #27, #30, #49 and #50.
  - SD#230's 4 own question files at 09:40:32 and 09:48:17 are inside its window, and their decisions come after the merge (L22:279-288). That is right.

**10. Brief item 5: for step 6, what the rules cannot catch, as this check shows.**
- Owner answers written in forms the owner-words test does not read (finding 1), until the test is fixed.
- Owner answers kept outside `questions/` and `decisions/`, until each repository's paths are named (finding 2). Also owner directions kept as reference files the K1 rule classes as research, such as Service-Desk docs/design/references/README.md in #61's window (pack L34:25-36), and Model-Lab intake/ files. These are unasked instructions, so they belong to RT7 and the touch log.
- Questions naming only a milestone (SD#148's board-scope), or naming nothing (design-reviewer-verdict).
- Comment authorship in Model-Lab, where no comment has been read (RT1(b) comes from the touch log there).
- Check rounds recorded only in spec text or commit messages. SD#36's Reviewer rounds R3 to R5 have no record file (hc/Service-Desk/specs/S-001.md only), so #36 is "left out" although it was checked.
- A single-round record whose verdict is not its first line and that has no round heading gives none: SD#341's _reviewer-verbatim.md:7.
- **Brief-297 finding 6(b):** PO#47's and PO#49's single-round build reviews have a top-line PASS but mention other checks' rounds, so (iv) gives "none found", not their true PASS.
- A spec-keyed plan review holds every piece's rounds for that spec (ML#43's reviews/S-001/plan.md has 6 rounds over two drafts). Its "Round 1" is the spec's first, not necessarily this piece's.
- Reverts worded otherwise (E-RR1) and fixes that name nothing (E-RR3).
- Unclassed check records in Model-Lab topic folders, such as ML#98's.

## Six-part contract
- **Changed:** nothing. I hold no write tool.
- **Why:** brief 299, S-002 hand check step 5 again, on memo 2 (P-002, M8).
- **Verified:** with Read, Grep and Glob only.
  - Model-Lab specs/S-002.md :1-126 and :238-270; research/Q-018-memo-2.md in full; research/Q-018-extract/sample.json and github_reads.json; and reviews/Q-018/_critic-verbatim.md, Q-018-rules/_critic-verbatim.md and Q-018-extract-widened/_critic-verbatim.md.
  - Pack INDEX and the L files 02, 08, 11, 17, 19, 22, 28, 34, 41, 43, 47, 50-52, 54, 57-60, 65-72 and 74 (sections as cited). Pack records2 for d38d8364, b2697809 and 233211a9, plus every records2 in-window header.
  - Clones: Service-Desk decisions P-001-design-reviewer-stop and -verdict, reviews/341, and the reviews search for #11 and #52. Personal-Org-Operating-Model reviews/S-022, S-025 and S-037 owner-answer files, plus a Glob for `questions/` and `decisions/`. Model-Lab reviews/S-001/plan.md, S-002/plan.md and P-002-two-look-line/reviewer.md headings, and the docs/briefs 270-273 dates.
- **Undone:**
  - The SHA-256 order was not recomputed: option A's set is taken from my earlier finding 7.
  - Not every in-window record was opened for E-RT4, since there is no git log; I used each piece's lists of the records that name it and my earlier reading.
  - The commit time of SD#148's design-reviewer-verdict.
  - Comment text, which is not in this pack.
  - E-RR2 candidates beyond the Service-Desk search.
  - The Personal-Org-Operating-Model ledger as an answer source.
- **Needed outside my surface:**
  - The Definer: findings 1 to 3 and 7(a).
  - The Orchestrator: re-extract the owner-words field and the answer paths. Also extract fields for the short form as role and for "has a memo".
  - Triage: finding 8.
- **Open questions:**
  - Whether Personal-Org-Operating-Model ledger lines that quote the owner count as answer records.
  - Whether Open question 10 should be settled before the re-check. The two orders cover different pieces, and only option A's set reaches the faults in findings 1 and 2.

Key paths:
- /home/user/Model-Lab/research/Q-018-memo-2.md
- /home/user/Model-Lab/specs/S-002.md
- /tmp/claude-0/-home-user/b9b3c098-5ac2-5fab-85c9-5ae65240ab9c/scratchpad/q018-pack2/records2/Service-Desk--d38d8364.md
- /tmp/claude-0/-home-user/b9b3c098-5ac2-5fab-85c9-5ae65240ab9c/scratchpad/q018-pack2/L47-Personal-Org-Operating-Model-30.md
- /tmp/claude-0/-home-user/b9b3c098-5ac2-5fab-85c9-5ae65240ab9c/scratchpad/q018-pack2/L52-Personal-Org-Operating-Model-27.md
- /tmp/claude-0/-home-user/b9b3c098-5ac2-5fab-85c9-5ae65240ab9c/scratchpad/hc/Personal-Org-Operating-Model/reviews/S-022/_owner-answers-2026-10.md
- /tmp/claude-0/-home-user/b9b3c098-5ac2-5fab-85c9-5ae65240ab9c/scratchpad/hc/Personal-Org-Operating-Model/reviews/S-025/_owner-answers-2026-10.md