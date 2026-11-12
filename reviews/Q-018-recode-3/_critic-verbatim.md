# The Critic's step 5 on memo 4, and a re-check of brief 309's step 6 list (brief 310)

*Recorded verbatim by the Orchestrator; the verdict file is reviews/Q-018-recode-3/critic.md. Brief 310 (docs/briefs/310-critic.md), on Model-Lab@aa879d1 (brief 310's start line names the commit before it), research/Q-018-memo-4.md (brief 308) and S-002 as changed by brief 309 (commit 19dcd2e), with the records pack built by brief 307. The Critic runs on a different model from S-002's writer (D-056) and apart from the Researcher and the Definer.*

Verdict: FAIL

The re-coding is right on every changed item I checked against the records. Service-Desk #237 is no longer a piece. The share is 14 of 33 pieces, and 11 of 26 in the random part. The Q-024 pairing gives two touches on the operating-model pull request #35. The Q-013 append on #25 is rightly left unpaired. The two slips my brief 304 check found are gone. One thing stops this check from closing, and it is in my own step, not in the memo or the rules. Taking #237 out changes which ten pieces the check of milestone-only questions (E-RT4) has to open. Under the hash-order reading of open question 10, which is my role's own reading, the new tenth piece is not known without a shell, so it has not been opened. The fix is small: the Orchestrator gives the hash order and the Critic opens that one piece. The other findings are non-blocking:
- one wrong count in the memo, which changes no result;
- one wrong reason in step 6's item (m), whose conclusion still holds;
- two loose rule wordings that change no count;
- two new items for step 6's list.

Nothing here is irreversible. Three findings implicate my role's earlier checks (D-050; finding 10).

## Findings

**1. Blocking: E-RT4's ten pieces under reading (a) of open question 10 now include a non-piece.**
- E-RT4 opens "the first 10 sampled pieces in the sample's order" (specs/S-002.md:102).
- Under reading (a), the hash order across the three repositories, the ten were SD #230, #237, #341, ML #29, SD #22, ML #92, SD #78, #148, POOM #35 and ML #43 (reviews/Q-018-recode/_critic-verbatim.md:49-59).
- #237 is now not a piece (memo 4 :51; pack L25 :4-17, every file a question, an answer or a record). So the 11th piece in hash order replaces it. Nothing in the manifest records that order (sample.json gives only per-repository lists), and I could not compute SHA-256.
- Under reading (b), sample.jsonl line order, SD #341 (line 28) replaces #237. Its only record is its starting ruling 8e21866a (RT4), so it adds no milestone-only case.
- So the spec's line "the Critic checked both sets" (:253) is true today only for (b).
- Fix:
  - Orchestrator: give the 11th piece in hash order.
  - Critic: open that piece's in-window question and decision files. This is one fresh-session check of that case only.

**2. Non-blocking: memo 4 :28 says ML #43 has "16 records" that name it only by spec. The extract has 18.**
- sample.jsonl line 2 lists 18 entries with `names_only_by_spec: true`, c5e5b2d8 to 0f6c1920, as pack L02 :242-259 shows. Memo 3 :16 had 18.
- None of the 18 is in the window, so the result (0 touches) stands.

**3. Non-blocking: memo 4 :29 and :169 list 66512cad as left out by RT5(b) without saying it falls after the merge.**
- It was first added at 12:27:10, after #29's merge at 12:25:33 (pack L03 :333, :357). So the window rules it out before RT5 is reached.
- Its partner b6081c5a (accept-m1's decision, also after the merge) is not mentioned.
- No count changes.

**4. Non-blocking: memo 4 :211's figures by repository are over all 33 pieces, but the line is not labelled that way.**
- ML 4 of 9, SD 5 of 13 and POOM 5 of 11 are right over all pieces, edge cases included.
- The random part by repository is ML 4 of 8, SD 2 of 7 and POOM 5 of 11, which is 11 of 26.
- The form-filter variant over the random part is 8 of 26 (memo :212 gives only 11 of 33).

**5. Brief item 1: the changed items against the records.**
- **SD #237, not a piece:** right. Its 14 files are 5 question files, 7 PNG files classed records, and 5ae5d612 and e719ce00, both owner question or answer by K1 change (iii) (pack L25 :4-17).
- **The share:** right. 14 of 33 overall; random 11 of 26; edge cases 3 of 7 (#78, #148, #300). I recounted every row of memo :26-100.
- **POOM #35 pairing:** right. sample.jsonl line 41 now holds `"question_id": "Q-024"` in clear, and the 17:59:31 append's `question_ids_in_owner_word_lines: ["Q-024"]`. That makes one question, timed at the question file's first add, 16:19:03, the first such commit (RT1(a), :47). With the 16:13:32 stop-rule append, the total is 2.
- **The Q-013 append on #25:** right that no question file pairs with it, though not for the reason the memo can see.
  - The append at 00:35:38 on 10-12 reads "Asked whether the design research Q-013 is the sprint of …" (pack records2/Personal-Org-Operating-Model--e219aae3.md:328, :342). That is Service-Desk's research item Q-013.
  - Personal-Org-Operating-Model also had its own question Q-013, the approval of S-003, whose file was removed when answered (clone docs/LEDGER.md:325).
  - Read literally, RT1(a) pairs any question file with an append naming its id. No count changes: that question file lies outside every sampled window, and no other record of #25 belongs to it. See 9(a).

**6. Brief item 2: memo 4 against my step 5 on memo 3 (brief 304).**

What differs, each judged against the records:
- SD #237: it was a piece with 6 touches, classed research, first check left out. It is now not a piece. Right.
- SD #78: 17 touches is now 16. Right: 15 in-window appends to d38d8364, plus 7d757252 (pack records2 d38d8364 :20).
- POOM #35: "3 (or 2)" is now 2. Right.
- SD #148: K3 research lines fall from 163 to 42, and the kind stays plans. Right (brief 306).
- The first-check "left out" list drops #237, going from 10 to 9. Counts: 4 PASS, 16 FAIL, 4 undecided, 9 left out. 13 pieces are past their 30 days and not reopened; 20 are pending. All recounted and right.
- Notes files on SD #52 and #11 are no longer listed. Right: 7de704c9, be649c32 and a1d1c4c9 were first added before those windows. #52's window is 10-08 17:15:15 to 17:51:19, and #11's is 10-01 15:01:27 to 15:15:32.
- The E-RT2 commits now say "no files changed". Right: all 20 are merge commits with empty file lists (pack L71, L60, L72, L57, L65).
- RT6 now gives e219aae3's 01:20:59 commit as an example. Right: it falls in #27's window (from 10-12 01:18:05), but e219aae3 names #27 only from its 20:17:26 append, so it is not read for #27 (:46).
- Unchanged and right: kinds, the other C1 results, the RR candidates, the 12 comments under the owner's account (all carry the agent footer, and 5 have a session record), the RT5 lists, and the four undecided first checks (ML #93, #98, SD #148, POOM #30).
- The ML #43 count (finding 2) and the 66512cad wording (finding 3) are slips new in memo 4.

Brief 304's two slips:
- **Finding 2 (#78 at 17):** gone (memo :94, :193).
- **Finding 3 (the open question 11 estimate):** memo 4 no longer states an estimate, so the wrong figure is gone. Corrected for #237, the figure is 6 of 26 in the random part: ML #93 and POOM #35, #30, #49, #27 and #25 stay. Overall it is 8 of 33, since SD #148 and #300 also stay.

**7. Brief item 3: memo 4's two open questions. Both are rule wording gaps for the Definer, not extract gaps and not owner questions.**
- **(a) K3's "changed lines" (:41).**
  - The extract carries added and removed lines (step 3, :109), so the data is there.
  - "Changed" is undefined. I spot-checked POOM #25 (plan 258 against built 129, or 196 against 127 with added lines alone), #49 (built 547 against plan 109) and ML #43 (plan 347 against research 168, or 240 against 95). Each gives the same kind under either reading, as the memo says.
  - Fix: one clause saying "added plus removed lines".
- **(b) ML #29: when to time question 8628e3d2.**
  - Its question file 197dd190 was first added at 23:58:10 by ML #25's own commit, inside #29's window, which opens at 23:56:17 (sample.jsonl line 9).
  - #29's commits only delete that file, and its text names nothing of #29 (pack records Model-Lab--197dd190.md: no number, brief or spec). So the file does not name #29 (:46, the deleted-file clause, which cites #29 by name).
  - RT1(a) (:47) says the question counts when "its record names the piece and, inside the piece's window, its question file is first added or the owner's words are added …; its time is … the first such commit in the window". Read that way, the time is 23:58:10.
  - "What a touch is" says a record that does not name the piece is not read for it. Read that way, the time is 00:38:22, which is the memo's choice.
  - The count is 1 either way. Only the time moves, by 40 minutes, which matters only at a trial look's cut-off.
  - Fix: one clause saying a paired record's event times the question only when that record itself names the piece. I recommend the memo's reading.

**8. Brief item 4: brief 309's step 6 list (a) to (o), and its note on open question 16.**

Each was checked against the record it cites, and each holds except (m)'s reason:
- (a): comments-2026-10.md:1; references/README.md (#61's own commits, 7827ee96; pack L34 :10, :29-50).
- (b), (c), (d) and (e): as brief 306 checked them.
- (f): 7234f058, plus 680797bd, where form (2) reads four agent option lines under "Answer (all four options picked): … The option texts, as offered:" (records2 d38d8364 :254-270).
- (g): de012573 is #237's first commit, which is its dispatch (pack L25 :41-47, :63). The GitHub-plan file holds two answers, at :5 and :13.
- (i), (j), (l): their cited findings exist (reviews/Q-018/_critic-verbatim.md:136-142).
- (k): owner-request-2026-10-20-home.md is 0695bbf6, added by #148's own commits (pack L69 :23). reviews/S-037/_owner-instruction-2026-11-05.md exists (104f5eb5).
- (n): there is no `Reopens:` line anywhere in the three clones.
- (o): P-001-design-reviewer-verdict.md:3 reads "Milestone: none (a governance change the owner asked for)". 8a208b94 has author and commit time 2026-10-20 14:18:53, inside #148's window of 10-19 20:50:27 to 10-20 14:43:21.
- Every item of brief 287 finding 10, brief 297 finding 6(b) and brief 299 finding 10 is now on the list.

The one error is in (m): "neither piece's result changes, since both are plan pieces whose plan review round 1 is FAIL" is wrong for POOM #49.
- #49 is built work by K3, with built 547 against plan 109 (pack L51 :4-27; memo 4 :77).
- Its result is PASS, from S-036's and S-037's round-1 build reviews (0e5d0a2e and f5ba9a62, reading (i); pack L51 :209, :214).
- reviews/49/reviewer.md (cdb45b88), a single-round PASS (clone :1), gives none under reading (iv).
- So the conclusion holds: #49's result does not change. Only the reason is wrong.
- The error comes from my brief 297 finding 6(b) (reviews/Q-018-extract-widened/_critic-verbatim.md:42). Fix (Definer): "#47 is a plan piece whose plan review round 1 is FAIL; #49 is built work whose other build reviews give PASS at round 1".

The note on open question 16 (:259) holds against the record:
- 5f6d7303's heading line, "Notes 15 to 18 … which also answers the question put in chat", names "answers" (records2 d38d8364 :141).
- b8ca4c9c's, "Notes 25 to 27 … after the orchestrator's answer to note 22", names "answer" (:194).
- #78's answers in the window are the fd5d7a8e append (four `Answer:` lines, :86-90) and 7d757252.

The Definer's open question: which count of ML #43's rounds did brief 299 finding 10 mean?
- Brief 299 wrote "6 rounds over two drafts" (reviews/Q-018-recode/_critic-verbatim.md:139). That fits no reading of the record:
  - At #43's merge, f73effd (the Q-017 extract gives f73effd as PR 43's merge-pr commit), the record held "## Round 1" to "## Round 5" of the first draft and three rounds of the new draft. Those three were added by #43's own commits a1b92283, 17b66931 and 083071e7 (pack L02 :38-147). That is 8.
  - At the cut-off it holds 5 plus 5 (clone reviews/S-001/plan.md:5-1000). That is 10.
  - The extract's `rounds` field is 5, the highest n.
- The only way to get 6 is to count the first draft's three plan-review rounds and leave out round 4 (the join-up) and round 5 (the confirmation), which the record itself calls "plan round 5" (:418). That makes "6" a miscount by my role.
- Step 6(m)'s count, "five rounds of the first draft and three of a new draft" at f73effd, is right and should stay.

**9. Brief item 5: new items for step 6's list, or rule fixes.**
- **(a) Pairing by the bare id `Q-<nnn>` can cross repositories.**
  - POOM #25's 00:35:38 append names Service-Desk's research item Q-013. Personal-Org-Operating-Model had its own question file Q-013 (docs/LEDGER.md:325), and RT1(a) would pair the two.
  - If such a pairing fell inside a window, two touches would merge into one. The rules cannot tell which repository's item an answer means without reading its text.
  - No count changes in the sample (finding 5).
- **(b) RT1(a) pairs a question file only with an append to an answer record, not with an answer record's first add that names the question's id (:47).**
  - So an `_owner-answers*.md` file first added inside a window to answer a question filed in the same window would count twice.
  - There is no case in the sample: only lines 41 and 57 of sample.jsonl carry question ids, both on appends.
  - Fix (Definer): "a first add or an append". If it is not fixed, put it on the list.
- **(c)** If finding 7(b) is not settled by a clause, put on the list: a question's time can depend on which of its paired records names the piece (ML #29: 23:58:10 or 00:38:22).

**10. Self-implication (D-050). Triage should count these as misses by my role's earlier checks.**
- My brief 297 finding 6(b) called POOM #49 a plan piece. That reason went into step 6(m) (finding 8).
- My brief 299 finding 10 counted ML #43's record as "6 rounds", which fits no reading of it (finding 8).
- My brief 304 finding 1 proposed taking #237 out, and my brief 306 check passed that change ("none of the draw's edge-case filters now picks a different item"). Neither noted that it changes E-RT4's ten pieces (finding 1).

## Six-part contract
- **Changed:** nothing. I hold no write tool.
- **Why:** brief 310, S-002 hand check step 5 on memo 4, and the re-check of brief 309's step 6 list (P-002, M8).
- **Verified:** with Read, Grep and Glob only.
  - Model-Lab: AGENTS.md; .claude/agents/critic.md; docs/briefs/310 and 309; specs/S-002.md in full; research/Q-018-memo-4.md and memo-3.md in full.
  - Model-Lab reviews: reviews/Q-018-recode-2, Q-018-rules-3 and Q-018-recode `_critic-verbatim.md` in full; Q-018 finding 10 and finding 7; Q-018-extract-widened finding 6(b).
  - Model-Lab extract: research/Q-018-extract/sample.json and README.md (E-RT4 row). sample.jsonl greps: names_only_by_spec, question_id and question_ids, 197dd190, owner_items_listed_in_window, notes-file times. research/Q-017-extract/Service-Desk.commits.jsonl and Model-Lab.commits.jsonl, for 8a208b94 and f73effd.
  - Pack (q018-pack-307): L02, L03, L07, L25, L28, L34, L51, L69, L73 and L74 (sections cited); records2 d38d8364 :20-275 and e219aae3; records 197dd190, 31505fb6 and 22147854.
  - Clones: Model-Lab reviews/S-001/plan.md headings. Service-Desk: reviews/341/_reviewer-verbatim.md headings; decisions/questions/P-001-design-reviewer-verdict.md:3; docs/design/references/comments-2026-10.md and README.md; R3-B1 to R5-B1 in specs/S-001.md; a search of all three clones for `^Reopens:`. Personal-Org-Operating-Model: reviews/49/reviewer.md:1-20; Q-013 references.
- **Undone:**
  - E-RT4's 11th piece in hash order (finding 1).
  - Without git, the state of plan.md at f73effd is worked out from #43's own commit messages and the record's headings at the cut-off.
  - K3's "no kind changes" claim was spot-checked on three pieces only.
  - E-RT5, E-RR1 and E-RR3 are carried over from briefs 299 and 304. The comments, the RR candidates and the RR rules are unchanged, and #237 had no comment and was pending.
  - RT3(b) from the closed-unmerged side was not checked.
- **Needed outside my surface:**
  - Orchestrator: finding 1 (the hash order).
  - Researcher: findings 2 to 4.
  - Definer: finding 8's (m) wording; finding 7's two clauses; finding 9.
  - Triage: finding 10.
- **Open questions:** nothing new for the owner. Open question 10's line "the Critic checked both sets" holds again only once finding 1 is done.

Key paths:
- /home/user/Model-Lab/research/Q-018-memo-4.md
- /home/user/Model-Lab/specs/S-002.md
- /home/user/Model-Lab/research/Q-018-extract/sample.jsonl
- /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/q018-pack-307/L02-Model-Lab-43.md
- /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/q018-pack-307/L03-Model-Lab-29.md
- /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/q018-pack-307/L51-Personal-Org-Operating-Model-49.md
- /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/q018-pack-307/records2/Personal-Org-Operating-Model--e219aae3.md
- /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/q018-pack-307/records2/Service-Desk--d38d8364.md
- /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/hc/Model-Lab/reviews/S-001/plan.md
- /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/hc/Personal-Org-Operating-Model/reviews/49/reviewer.md
