# The Critic's second re-check of S-002's corrected counting rules (brief 291)

*Recorded verbatim by the Orchestrator; the verdict is the second section of reviews/Q-018-rules/critic.md. Brief 291 (docs/briefs/291-critic.md), on Model-Lab@93cc8bc, the rules as corrected by brief 290 (commit 53487ce, merged at 022216e). The Critic runs on a different model from S-002's writer (D-056) and apart from the Researcher.*

Verdict: FAIL

**In plain words.** Almost every correction now gives the result the records show. The new "what a record says it reviews" test settles all the first-check cases. Service-Desk #148 is now "undecided", with no other piece's review pulled in. Personal-Org-Operating-Model #25 now reads its upper-case FAIL. The timing rule places every Service-Desk case I named. One fault remains, and it blocks. The new gate test reads file names only, so it now counts a ruling that is part of the value target (trial-gates; two-look-line too) as a touch. RT5 says such rulings stay out until the owner rules on them (Open question 3), so the rule decides that question for these records before the owner has answered. The same test drops a stop-rule choice because its name holds "build-gate", although RT5 says stop-rule rulings are counted. Model-Lab's own records state which rulings are a gate or a value target, so it is a small fix. The rest are wording gaps that do not block. Nothing is irreversible. My earlier fix proposed this gate test, so this finding implicates my own check.

**Self-implication (D-050):** Finding 1 comes straight from the fix I recommended in brief 289, finding 3 ("match a gate by a named gate … and `value-target`"). Findings 3 and 4 come from my 289 fixes 1 and 4. In finding 5 I flag a gloss I missed in 289. Triage should note all four.

## Findings

**1. Blocking. RT5's name-only field (specs/S-002.md:51) goes against RT5's own definition in both directions.**
- **Counted when it should be left out.**
  - P-002-trial-gates says of itself "Part of a value target: the owner's own answer, never a default" (Model-Lab decisions/questions/P-002-trial-gates.md:6).
  - It is part 3 of the value-target ruling (P-002-value-target.md:1, :20).
  - P-002-two-look-line says the same of itself (:6). It is tagged M9, so it is not even listed under question 13.
  - RT5's first sentence keeps a value-target ruling out until the owner rules (Open question 3). The name test counts both, so on ML#92 (trial-gates) the rule settles question 3 for this record before it is answered.
- **Dropped when it should be counted.**
  - P-001-build-gate-stop.md:5 is "A choice under the stop rule after the cards' third failed check".
  - Its name holds `build-gate`, so it is left out.
  - Yet line 51 says "a ruling on a stop rule … is counted under RT1". That clause speaks only of the milestone tag, so the two sentences clash.
- **Fix.**
  - A record is also RT5's when its own text classes it as a phase gate or a value target. Model-Lab's `Asked:` lines say so plainly: "A phase gate" (P-001-design-gate.md:4, P-001-build-gate.md:5), "A value target" (P-001-value-target.md:3, P-002-value-target.md:6), "Part of a value target" (P-002-trial-gates.md:6, P-002-two-look-line.md:6).
  - The name words stay as the test where a record gives no class.
  - A record whose text says it is a stop-rule choice is counted whatever its name.
  - Open question 13's recommendation should then drop trial-gates from its examples.

**2. Non-blocking. Question 13 (:255) mixes Open question 3 with its own subject.** Its title and options are about rulings on a definition of ready. But its recommendation gives as a reason "a ruling given while a piece is under way is you stepping in on it", cites trial-gates (a value-target part) as a case it counts, and so argues question 3. Once finding 1 is fixed, P-002-target alone stays as the example. That one is right to count: it is an unasked ruling on the project's aim (P-002-target.md:5), not one the model requires.

**3. Non-blocking. New ambiguities in "Which records are the piece's" (:59).**
- (a) **Head branches are reused.** In Service-Desk, claude/p004-widget-discovery-gcavd9 is the head of both #300 and #310 (research/Q-018-extract/Service-Desk.list.jsonl:286, :295). claude/chief-of-staff-discovery-yh4eyi heads 8 merged pull requests (:324-334). A statement whose first subject is such a branch fits several pieces. Say which: the latest one merged after the record, or "undecided, listed". No named case hits this; reviews/356 and reviews/360 name the number first.
- (b) **Records with no heading.**
  - S-001-trial-view-2/_build-review-round1-verbatim.md:1-3 and reviews/300/reviewer.md have no heading at all.
  - The rule's own example uses the first of them, so it means "the paragraph alone". The text says "its first heading together with…". Say so.
- (c) **Letter case of `Verdict:` in this clause.** The "any letter case" clause is in the next bullet ("here and below"), so this clause's "a `Verdict:` line" is still case-sensitive. A record whose first paragraph is `VERDICT: FAIL` would take that line as its statement.
- (d) **"As a whole word" for branch names is not defined:**
  - an `origin/` prefix (S-001-desk-v2/_plan-review-round1-verbatim.md:3, "origin/build/definer/s001-desk-v2");
  - a hyphen running on after the name (`orch/desk-v2` inside `…desk-v2-1a`).
- (e) **The new kind-by-path sentence (:57) clashes with the two-kind clause (:60).** A path-classed build review that also gives plan-review lines (PO reviews/20/reviewer.md:4; SD reviews/77/reviewer.md:3 "as a plan check") can be read as giving a plan piece's verdict, or as never giving it. On PO#20, a built piece, the result is the same either way.

**4. Non-blocking (self-implication). RT4's first-commit clause (:47, :50) applies when dispatch comes from a brief record, too.**
- There the first commit can come hours after the dispatch, so an owner ruling given in between and recorded in that commit is called the starting ruling.
- In the sample only line 67 (ML#98, after the cut-off) is dispatched from a brief record, so no case changes.
- Fix: limit the clause to pieces dispatched by their first commit.

**5. Non-blocking. Steps 3 to 5 match the rules, with three gaps.**
- (a) Step 4's glosses (:108) do not gloss "(step 6)" in RT1(b) (:47), which the quoted lines carry. This gap has been there since brief 288, and I missed it in 289.
- (b) Step 3 (:107) gives only "the piece's head branch name". The statement test needs to know whether a named branch or hash belongs to any merged pull request, at any time, so it needs every merged pull request's head branch and own commits.
- (c) Extract, for the Orchestrator. Service-Desk.list.jsonl holds `head_ref` names in clear (for example :73, "orch/trial-view-2"). Step 3 says the branch name is "not written".

**6. Non-blocking. RT1(b)'s "all 8 comments under the owner's account on the sampled pull requests" (:47) says more than the reading did.**
- github_reads.json:5-7 lists 10 comments on drawn merged pull requests (SD#6 and PO#11 as well), plus frame U's.
- The 8 my brief 287 reading covered are the ones counted before merging (reviews/Q-018/_critic-verbatim.md:53-60).
- Say "all 8 counted before merging".

**7. Non-blocking. "Names a piece" when only an append names it (:46).** A record is "read as the commit that first adds it … left it, and each later commit's added lines as that commit adds them". The rule does not say whether a later append that names the piece makes the record name the piece.

## 1. Each finding against its cases

1. **Fixed; every named case is right.**
   - **SD#148: undecided, right.**
     - Its records are design-reviewer-setup/_review-round1..3 (heading ":1 Pull request #148"), all build reviews by path.
     - It also has reviews/148/reviewer.md, a build review by path.
     - Its `_confirmation*` records are of another kind.
     - The desk-v2 records no longer belong to it. Their statement names build/definer/s001-desk-v2, which is no merged pull request's head, and then ceaf9a2, an own commit of #176 (Service-Desk.M.jsonl:164).
   - **SD#52: FAIL, right** (reviews/52/reviewer.md:5). Other pieces' records are no longer taken in:
     - 287/_reviewer-r1 has the heading "PR #287";
     - 300/reviewer.md:3 says "PR #300";
     - trial-view-2's statement points to #78.
   - **SD#54: PASS, right** by (iv) (reviews/54/reviewer.md:1, :3). The "PR #54" in 52's record comes after its subject.
   - **SD#11: FAIL, right** (reviewer.md:3). reviews/245's statement is "QW2 (PR #245)". M3G/_stage-qw2-review-r1's statement names build/builder/qw2 at 8e530a5.
   - **SD#78: FAIL, right.**
     - build/builder/trial-view-2 heads no merged pull request (list.jsonl, no match), so the subject is orch/trial-view-2, which is #78's head (list.jsonl:73).
     - I could not recompute the SHA-1 label 03490570 (no shell). The name is in list.jsonl directly.
   - **SD#300: FAIL, right** (EXP-007/_critic-r1, the folder clause).
   - **PO#25: FAIL, right** by (i) (S-022/_plan-review-s022-round1-verbatim.md:5).
   - **PO#27, PO#47 and PO#50: unchanged, right.**
   - **ML#93: undecided, right.**
2. **Fixed** (:60).
3. **(a) and (b) fixed.** gate-card, gate-buttons, glance-waits-gates and brief-stop are counted, and SD m3c-launch-gate is left out ("M3C is your launch approval", m3c-launch-gate.md:8), which is right. **But the fix gives new wrong results** (finding 1).
4. **Fixed.**
   - **SD#341: right.** The record is first added in the first commit, at 13:52:33, the dispatch (sample.jsonl:28).
   - **SD#26: right by the rule.** 233211a9 is first added at 15:46:35, which is both the dispatch and the first commit, so it is the starting ruling. o3-define counts at 16:11:10, and the notes file is out.
   - **SD#78's appends: right in kind.** Counting them needs the widened extract.
5. **Fixed as a listing under question 11** (SD#237, ML#29 accept-m1, SD#230).
6. **Fixed.** PO#24 is FAIL by (ii) (reviews/24/reviewer.md:77).
7. **Fixed.**
8. **Fixed.**
9. **Fixed.** No bare Q-018 U label is left.
10. **Fixed,** but see finding 7.
11. **Mostly fixed** (finding 5).
12. **Fixed.**
13. **Fixed,** but see finding 6.
- **3(a): sound,** with its reason stated (:46).

## 2. Can the changed rules be coded from records alone?
- Yes for C1's verdict reading, the round-1 name test, the folder list, RT1's timing and the marks.
- The statement test can be coded and makes no wrong match on any case I checked. I also scanned every `Reviewed`/`Read:` line in Service-Desk's and Personal-Org-Operating-Model's reviews/. The ambiguities are in finding 3.
- RT5 can be coded but gives wrong results (finding 1).

## 3. The Definer's question
- **P-002-target: right to count it, and to list it.** It is not a ruling the model requires.
- **P-002-trial-gates: wrong to count it.** It is a value-target ruling by its own record (:6). P-002-two-look-line is the same and is not listed.
- So the name-only field does not meet RT5's definition (finding 1).

## 4. Open questions 12 to 14
- **12 and 14 are fair.** Each has my options and a recommendation, and neither changes a rule.
- **13's options are fair, but not its reasoning or examples** (finding 2). Through RT5's field, the rules count value-target parts before Open question 3 is answered (finding 1).

## 5. Nothing else changed
- **Untouched:** both diffs leave the draw, the seed, the cut-off and the window (:84) alone, and the edge-case table (:86-105), filters included.
- **The step 3 sentence on E-K2:** it changes no filter text.
- **The Definer's line list:** it matches the brief-290 diff's hunks.
- **Not confirmed:**
  - that commit 53487ce touches S-002 alone;
  - that the governance checks passed.

**On the Definer's script** (data, not trusted). Its results match mine on the named cases, but it differs from the rule:
- It reads level-1 headings only (`l.startswith('# ')`).
- Its branch pattern knows only build/, orch/ and claude/, not cos/.
- It reads the clones as they stand now, not as at the cut-off.
- A short hash prefix may match several pull requests.

## Six-part contract
- **Changed:** nothing; I hold no write tool.
- **Why:** brief 291, the re-check of brief 290's corrections on their cases (P-002, M8).
- **Verified:** with Read, Grep and Glob, I read:
  - the two diffs, specs/S-002.md:1-120, reviews/Q-018-rules/_critic-verbatim.md, reviews/Q-018/_critic-verbatim.md:48-63, docs/briefs/290-definer.md and c1check2.py;
  - from the extract: sample.jsonl (dispatch fields, line 68, questions_decisions), Service-Desk.list.jsonl (head refs), Service-Desk.M.jsonl:164 and github_reads.json;
  - in Service-Desk: reviews 11, 52, 54, 245, 287, 300, 356, 360, design-reviewer-setup, S-001-desk-v2, S-001-trial-view-2, M3G, and every `Reviewed`/`Read:` line; decisions o3-define, o6-define, m3c-launch-gate and the gate files;
  - in Personal-Org-Operating-Model: S-022 round 1, reviews 20 and 24, the #25/#27/#47/#50 matches, and every `Reviewed` line;
  - in Model-Lab: decisions P-002-target, trial-gates, value-target, two-look-line, brief-stop, build-gate-stop, build-gate-terms, the "never a default" lines, and reviews/ matches for #93.
- **Undone:**
  - No git, so I checked no commit times, the SHA-1 label, the files commit 53487ce changes, or the governance checks.
  - I did not re-read the GitHub comments.
  - I did not count the SD#78 appends.
  - I could not see the deleted question files.
- **Needed outside my surface:**
  - The Definer: finding 1 (blocking) and findings 2 to 7.
  - The Orchestrator: extract fields for every merged pull request's head branch and own commits, and for each record's class statement; list.jsonl's clear branch names against step 3.
  - Triage: the self-implication flags.
- **Open questions:** for the owner, unchanged: 11 to 14, with question 13 reworded once finding 1 is fixed.

Key paths: /home/user/Model-Lab/specs/S-002.md, /home/user/Model-Lab/decisions/questions/P-002-trial-gates.md, /home/user/Model-Lab/decisions/questions/P-002-two-look-line.md, /home/user/Model-Lab/decisions/questions/P-001-build-gate-stop.md, /home/user/Model-Lab/research/Q-018-extract/Service-Desk.list.jsonl, /home/user/Model-Lab/research/Q-018-extract/github_reads.json