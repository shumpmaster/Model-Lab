# The Critic's step 5 on memo 3 (brief 304)

*Recorded verbatim by the Orchestrator; the verdict file is reviews/Q-018-recode-2/critic.md. Brief 304 (docs/briefs/304-critic.md), on Model-Lab@4ead565, research/Q-018-memo-3.md (brief 303), with a records pack built by pack.py and pack2.py in this session's scratchpad (not committed, as it holds free text). The Critic runs on a different model from S-002's writer (D-056) and apart from the Researcher.*

Verdict: FAIL

The corrected question rule now gives the right result on every piece brief 304 names. The one thing that fails is not that rule. One randomly drawn Service-Desk pull request (#237) counts as a piece of work only because the rule that sorts files by path puts the owner's own answer records in the research class. Under the owner's ruled definition of a piece, a pull request that only files questions, records answers and adds records is not a piece. Take it out and the share becomes 11 of 26, not 12 of 27. That is a fault in the counting rules, so it goes back to the Definer. The extract then needs re-coding for that one rule only.

On the question you asked: the three operating-model pieces that the "drop quoted-form answers" reading would zero out each hold the owner's own choices, given while the piece was under way. So that reading is wrong against the records, and the "at least one touch" result stands for all three. The pairing case on Personal-Org-Operating-Model #35 is settled by the records: two touches, not three. The owner filing a reviewer's verdict through the web editor does not stop it being an independent check. The memo has two small arithmetic slips. Nothing here is irreversible.

Self-implication (D-050): my step 5 checks on memo 2 (brief 299) and on brief 300's rules (brief 301) passed Service-Desk #237 as a piece without testing it against the ruled definition.

## Findings

**1. Blocking: Service-Desk #237 is a piece only through K1, against ruled T1. The random share is 11 of 26, not 12 of 27.**
- Rules: S-002.md:20 (K1 classes paths by Q-017's rules), :24 (RP2), and :48 ("they change no file's class by K1"). Ruled T1, quoted at :16: "one that only files or answers a question, or only adds records, is not a piece".
- Records (pack L25-Service-Desk-237.md:4-17, :20-47):
  - 5 question files.
  - 7 PNG pictures (records).
  - docs/design/references/owner-answers-2026-10-25-g8c-review.md, the owner's answers (records2/Service-Desk--5ae5d612.md:4-34). Rule :48 names this as an owner-answer path.
  - docs/design/references/owner-request-2026-10-25-questions-and-order.md, the owner's answers to questions put in a session (brief 301 finding 3).
  - K1 classes the last two as research, which makes the pull request a piece. Every file is a question, an answer or a record.
- Memo 3:39 codes it as a piece with 6 touches. Memo 3:124 counts it in "SD 3 of 8". Memo 3:204 notices the problem but does not judge it.
- Result: random part 11 of 26 (42.3%), and 14 of 33 over all pieces. The form-filter reading becomes 8 of 26.
- Fix (Definer): K1 classes files at the owner-answer paths of :48, and Service-Desk's other `docs/design/references/owner-<kind>-` files, as owner question or answer. Then re-code RP2 on the drawn sample (no new draw). Service-Desk #148 (2,533 plan lines) and #61 (1,471 plan lines) stay pieces either way.

**2. Non-blocking: Service-Desk #78 is 16 touches, not 17 (memo 3:82, :116).**
- The extract lists 15 in-window appends to d38d8364, then 7d757252 at 20:29:14 (research/Q-018-extract/sample.jsonl line 68). The memo's own list of times adds up to 15, not the "16 appends" it states.
- This matches brief 301's "1 to 16". The form-filtered figure of 6 is right: 5 appends with a form (1) label, plus 7d757252.

**3. Non-blocking: the Open question 11 estimate should be 6 of 27, not 5 (memo 3:131).**
- Six random pieces fall to 0: ML #29, #73 and #81, and SD #230, #237 and #26. SD #78 is an edge case.
- Six stay: ML #93 (31505fb6 names it by number), and POM #35, #30, #49, #27 and #25.

**4. Brief item 1, RT1(a) against the records, piece by piece.**
- **Service-Desk #78:** each counted append adds the owner's words, given between dispatch (11:54:38) and merge (20:40:27) (records2/Service-Desk--d38d8364.md:20-700). 7d757252 holds a real `Answer:` given in the session (records/Service-Desk--7d757252.md:7). None is missed: owner.md is an approving review (RT4), and the 20:32:34 comment carries the footer.
  - Several appends (14d854aa, 01221fd4 and the 16:42:39 group) are the owner's unasked notes, not answers. RT1(a) counts them as questions; see finding 7(b).
- **Service-Desk #26:** b2697809's `Ruling: yes` (16:11:10) is a real in-window answer (records2/Service-Desk--b2697809.md:2-3). 4977c952 on 233211a9 is rightly not an append, and 21334cb2 adds no owner words. 1 is right.
- **Service-Desk #237:**
  - 7234f058 holds two real owner answers (records2/Service-Desk--5ae5d612.md:28-34). Form (3) also counts its 4 agent "Asked:" and "Options offered:" lines, but the count is per commit, so it is still 1.
  - The 5 question files are filed in the window, and their decisions come after the merge.
  - Every one of these touches is about other work (M3G, G8d).
  - Right under the rules, but moot if finding 1 holds.
- **Personal-Org-Operating-Model #25:** yes, the owner's own answer.
  - 6e37e45e (10-11 14:31:36) adds the owner's verbatim choice on the ruling's scope.
  - 71bff0be (15:42:40) adds the owner's verbatim approval to freeze.
  - Both are inside the window, 10-10 21:56:54 to 10-12 01:25:51 (records2/…--ad6df430.md:56, :71).
  - "At least one" stands.
- **Personal-Org-Operating-Model #27:** yes. dcc1e652 (10-13 03:18:48) adds four of the owner's choices (D5-1, D5-2, D5-3, D5-6). 546dbdf3 adds D5-4 and D5-5, and 93ed08cd adds the build stop-rule choice (records2/…--c4fc482f.md:29-73). All are in the window, which ends 10-13 15:20:19. "At least one" stands.
- **Personal-Org-Operating-Model #30:** yes. 667e193c, 879f5e3a and 83cc104b each add the owner's chosen option to a question put about S-029, the spec #30 builds (records2/…--455192c4.md:6, :38, :55-57). "At least one" stands.
- **Personal-Org-Operating-Model #35:** 2 touches, not 3 (see 6(a)). Both count:
  - cac877e8 at 16:13:32, a stop-rule choice (RT5(a)).
  - The Q-024 question first added at 16:19:03, answered by 59c359a1 at 17:59:31.
- **Form (3) on these three pieces:** each counted line puts the agent's "Asked" text and the owner's quoted choice on one line. So the flag only_form_2_or_3 marks a recording style, not agent-only text.
- **Duplicates:** e219aae3 (S-023) and 2cb87e77 (S-024) are byte-for-byte copies of one answer file (records2/…--e219aae3.md:4). On #25 each answer is counted twice. This does not change any yes-or-no.

**5. Brief item 2, the share and which reading the records support.**
- 12 of 27 is right arithmetic under the rules as written: ML 4 of 8, SD 3 of 8, POM 5 of 11.
- The records support today's reading over the form-(2)/(3) filter. The filter's 9 of 27 removes three pieces whose counted commits hold the owner's real in-window choices (finding 4). Personal-Org-Operating-Model writes its answers only in that form.
- The spec-only filter changes no piece's yes-or-no, as the memo says.
- Corrected for finding 1, the figure the records support is 11 of 26. It is still subject to Open question 11, whose upper-bound effect is finding 3.

**6. Brief item 4, the undecided cases.**
- **(a) The Q-024 pairing on #35: an extract gap, not a rule fault or an owner question.**
  - 14b7aecb is questions/Q-024-approve-s033.md (records2/…--14b7aecb.md:1), and 59c359a1's answer 3 names Q-024 (records2/…--0d5230c0.md:35). By RT1(a) they are one question, so the count is 2.
  - The extract gives the question file's id only as a hash (memo 3:130). Carry the `Q-<nnn>` of each question file in clear.
- **(b) The owner's web-editor commits of build-review records: none of the three; the records settle it.**
  - Service-Desk reviews/11/reviewer.md:2, reviews/52/reviewer.md:2 and Personal-Org-Operating-Model reviews/18/reviewer.md:2 each read "Reviewer: reviewer (read-only subagent, fresh context)" and give that Reviewer's rounds. The owner only filed the verdict.
  - So C1's "whoever wrote it" (:59) gives the right result.
  - The filing is not a touch: it is a records file, and RT2(a) needs built, plan or research.
  - It need not go to the owner unless the owner wants clerical filing counted as stepping in, which ruled T2 does not include.

**7. Brief item 3, spot checks.**
- Read in full, each right under the rules:
  - ML #93: 1 touch. 31505fb6's in-window answer, the stop-rule choice, pairs with 22147854.
  - ML #29: 9acdfce2 is in the window. The answer was recorded from the handoff update committed at 00:03:15, after the dispatch at 23:56:17.
  - SD #230: 4 question files filed in the window. They ask for later changes, which is the Open question 11 case.
  - SD #341: 0. The decision is in the first commit (RT4), and the question file is only deleted.
  - POM #49: 1. Q-031 is filed at 16:38:01, and its answer comes at 23:35:08, after the 23:32:42 merge.
  - POM #25, #27, #30 and #35, and SD #78, #26 and #237: as finding 4.
- Every case my step 5 on memo 2 passed keeps its result. The C1 results match brief 299 finding 9: SD #11, #78, #52 and #300 FAIL; POM #18, #27, #20, #24, #47 and #25 FAIL; POM #50 PASS; ML #73 and #81 FAIL; ML #78 left out; SD #148 and ML #93 undecided. The 12 owner-account comments are all the agent's. The E-RP, E-K and E-RT2 edge results are unchanged.
- **Pack note (no effect on results):** records2/Service-Desk--d38d8364.md shows each of the four 16:42:39 commits four times (:128-528). The extract has each once.

**8. Brief item 5, for step 6's list (new).**
- **(a)** Owner answer records kept under a research path make an answers-only pull request a piece (finding 1), until K1 is fixed.
- **(b)** The owner's unasked notes, written into a decision record, are counted under RT1(a) as questions, not under RT7's own code. So a ruling on Open question 2 could not drop them (SD #78, 14d854aa and the notes 10 to 27 appends).
- **(c)** An answer given before the dispatch but first written down inside the window counts in the window, since RT1(a) times by commit.
  - POM ad6df430 says its words were "first written down in the spec draft".
  - ML 9acdfce2 was "Recorded from the previous session's handoff".
- **(d)** Byte-for-byte copies of one answer file (POM S-023 and S-024) count each answer twice.
- **(e)** Batch commits squeeze touch times together: eight SD #78 commits fall between 16:42:38 and 16:42:40. A touch's commit time may then be far from when it was given, which matters for a trial look's cut-off.
- **(f)** Form (3) counts agent lines ("Asked:", "Options offered:") in Service-Desk's owner-answers files as owner words. No yes-or-no changes, but the line count is a flag, not a measure.

**9. Self-implication (D-050).** In brief 299 (finding 9, E-RP and E-K spot checks) and brief 301 (finding 3, which read #237's owner-request file and said "nothing in the sample changes"), I treated SD #237 as a piece and never tested RP2 against ruled T1 there. Triage should count finding 1 as an issue my earlier checks missed.

## Six-part contract
- **Changed:** nothing. I hold no write tool.
- **Why:** brief 304, S-002 hand check step 5 on memo 3 (P-002, M8).
- **Verified:** with Read, Grep and Glob only.
  - Model-Lab: AGENTS.md; docs/briefs/304-critic.md; specs/S-002.md:1-136; research/Q-018-memo-3.md in full; reviews/Q-018-recode/_critic-verbatim.md and reviews/Q-018-rules-2/_critic-verbatim.md; greps of research/Q-018-extract/sample.jsonl for in-window commit fields (lines 41, 47, 52, 57 and 68).
  - Pack: INDEX; L68, L35, L25, L57, L52 (headers and commits), L28, L07, L03, L22 and L51 (sections cited).
  - Pack records2: d38d8364, 233211a9, b2697809, 5ae5d612, ad6df430, e219aae3, c4fc482f, 455192c4, 4efc6a60, 14b7aecb, 0d5230c0, 31505fb6, 9acdfce2 and e469c207. Pack records: 7d757252.
  - Clones: Service-Desk reviews/11/reviewer.md and reviews/52/reviewer.md; Personal-Org-Operating-Model reviews/18/reviewer.md.
- **Undone:**
  - No git log, so author times and the exact moment answers were given come from commit times and record text only.
  - E-RR candidates were not re-opened: the RR rules are unchanged since brief 299.
  - c4fc482f's two omitted long lines (546dbdf3's D5-4, 93ed08cd's stop-rule choice) were judged from the commit headers and the surrounding lines.
- **Needed outside my surface:**
  - The Definer: finding 1 (K1 class for owner-answer paths), and wording for 8(b) if taken.
  - The Orchestrator: the extract field for clear question ids (6(a)); re-code RP2 after the fix; the pack2 duplicate output (finding 7 note).
  - The Researcher: correct memo 3:82, :116 and :131 (findings 2 and 3).
  - Triage: finding 9.
- **Open questions:**
  - Whether the owner's unasked notes recorded in decision records should count under RT7's code rather than RT1(a). This could go beside Open question 2.

Key paths:
- /home/user/Model-Lab/research/Q-018-memo-3.md
- /home/user/Model-Lab/specs/S-002.md
- /tmp/claude-0/-home-user/b9b3c098-5ac2-5fab-85c9-5ae65240ab9c/scratchpad/q018-pack3/L25-Service-Desk-237.md
- /tmp/claude-0/-home-user/b9b3c098-5ac2-5fab-85c9-5ae65240ab9c/scratchpad/q018-pack3/records2/Service-Desk--d38d8364.md
- /tmp/claude-0/-home-user/b9b3c098-5ac2-5fab-85c9-5ae65240ab9c/scratchpad/q018-pack3/records2/Personal-Org-Operating-Model--ad6df430.md
- /tmp/claude-0/-home-user/b9b3c098-5ac2-5fab-85c9-5ae65240ab9c/scratchpad/q018-pack3/records2/Personal-Org-Operating-Model--c4fc482f.md
- /tmp/claude-0/-home-user/b9b3c098-5ac2-5fab-85c9-5ae65240ab9c/scratchpad/q018-pack3/records2/Personal-Org-Operating-Model--455192c4.md
- /tmp/claude-0/-home-user/b9b3c098-5ac2-5fab-85c9-5ae65240ab9c/scratchpad/q018-pack3/records2/Personal-Org-Operating-Model--14b7aecb.md
- /tmp/claude-0/-home-user/b9b3c098-5ac2-5fab-85c9-5ae65240ab9c/scratchpad/q018-pack3/records2/Personal-Org-Operating-Model--0d5230c0.md