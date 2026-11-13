# The Critic's re-check of briefs 318 and 319 (brief 320)

*Recorded verbatim by the Orchestrator; the verdict file is reviews/S-002-rulings-3/critic.md. Brief 320 (docs/briefs/320-critic.md), on Model-Lab@038a89d, S-002 and E-004 as changed by briefs 318 (6df531d) and 319 (d8c9fa7). The Critic runs on a different model from S-002's writer (D-056), apart from the Definers and from the Critics of briefs 315 and 317.*

Verdict: FAIL

Briefs 318 and 319 close every finding from brief 317 that was open: the ones closed in the text are closed there, and the one that needed the owner is now settled by the owner's choice. That choice is written in with the card's exact words, and its one added reading (that "every question" also covers your notes and unasked instructions) is supported by the card. Nothing here blocks the re-count. One thing blocks the freeze, though not the re-count. On trial pieces the "later work" code is now ignored, but the Chief of Staff still keeps the touch log. The Chief of Staff knows the sides, and it alone decides whether a touch given in conversation is logged and which piece it is put against. So the plan's new claim that "no one who knows the sides decides which of them count" goes too far, and that way of steering is not on any of the plan's lists of what a trial cannot catch. Smaller points: the decision record for this choice is not on this branch yet. The records pack the coder must use does not yet hold the ledger entries. The plan says twice that the comparison is "not tilted", which claims more than the card does. And a different ruling whose quoted words happen to match (such as "A" or "Approve") is silently skipped, and no list says so.

## Findings

1. **Blocking for the freeze (not for the re-count), for the Definer, with a gap for the owner. The person keeping the touch log knows the sides, and the plan does not say so.** specs/S-002.md:197 (J9): the Chief of Staff writes every conversation touch's line, including its `piece` field (`"brief <n>" | "pr <n>"`). The live count then counts RT1(c), RT2(b), RT3(c) and RT7 from those lines (:189). experiments/E-004.md:149 says "The agents and the Chief of Staff know which pieces carry the method". Ruling 19 takes the later-work code out of trial pieces, but the choice moves to two places it does not reach: whether a conversation touch is logged at all, and which piece it is logged against. For example, a question about follow-up work can be logged on the trial piece, or on the not-yet-dispatched later work, which is not counted (J9 awkward case "a touch on work not yet dispatched (not counted, RT4)"). Three lines now say more than holds:
   - the plain words (:10), "so no one who knows the sides decides which of them count";
   - Risks (:236), "no code given knowing the side reaches a trial's deciding measure". This is true of codes, but not of what gets logged.
   - Risks (:233), "a missed touch is as likely on either side unless agents ask less on one". This leaves out that the log's keeper knows the sides.

   The monthly cross-check (AC5, :170) compares the records against the log, so it cannot catch a conversation touch that was left out or put against the wrong piece. The Definer should add this to the plain words, J3, J4 and Risks, and to E-004's "What this trial cannot catch" and Steps 1 and 8. Ruling 19 does not reach it, so the owner should then choose:
   - (a) a stated limit;
   - (b) the owner confirms, or adds, each trial look's conversation lines through the desk before the look is judged;
   - (c) a fresh session that is not told the sides checks the log against the session handbacks.

   Self-implication (D-050): brief 315's and brief 317's Critics, my role, did not raise this.

2. **Closed: brief 317 finding 1.** The owner ruled option C. It is written into:
   - the plain words (:10), "What a touch is" (:46), RT4 (:52), J1 (:189), J3 (:191), J4 (:192), J9 (:197), Risks (:236) and Open question 19 (:265);
   - E-004's Step 1 (:39), Step 8 (:101), Measure (:110) and "What this trial cannot catch" (:151).

   The withdrawn piece's and the unmerged piece's touches (E-004:127) fall under Measure's "on a trial piece", so they are covered.

3. **Ruling 19's text (brief item 2).**
   - **The quote:** J1 (:189) gives option C word for word against questions/P-002-live-later-work-check.md:15. The owner's words match the handoff, docs/handoff/2026-11-12-chief-of-staff-p002-16.md:46. I could not read the card at d0f290b without git; the copy on this branch matches.
   - **Additions beyond option C:**
     - (i) every figure toward V1 gives how many of its pieces are trial pieces: a disclosure, no issue;
     - (ii) the Chief of Staff "need not know which pieces are trial pieces" (:197): no issue;
     - (iii) "the comparison a look decides on is not tilted" (Risks :236; E-004:151), and "leans toward a miss of V1, never a pass" (:236): see finding 5 for (iii).
   - **The reading of "every question" as RT1a, RT1c and RT7:** supported, not a gap for the owner. The card's gain is "no judgement at all on trial pieces, so nothing to steer" (card :16). RT7 already reads a note for later work "as a question is" (:55). Read narrowly, RT7 notes and logged instructions on trial pieces would keep the coder who knows the sides, which is the very thing the card removes. The plain words already tell the owner "every question or note of yours counts".
   - **Is `trial` codable?** Yes, from the J2 entry line's `repository` and `brief` matched to the brief numbers in the pull request's `Agent-Session:` trailers. That is the same match K2 and the extract use.
     - Non-blocking: J2 does not fix the form of the `brief` field. A trial pull request whose commits carry no trailer naming its brief (only bare `Agent-Session:` trailers, as Personal-Org-Operating-Model #49's do, L51 pack file) would get `trial: null` and have its codes read.
     - Fix: J1 should name the match, and list any J2 entry that no J1 line carries.
   - **The notes on the starting figure:** right as to which way the rule leans. On a trial piece, treating every question as "not said" can only add touches, and the starting 60 come before any trial (AC12, :177), so they hold no trial piece. Wording: "can only read high" (E-004:151) is the rule's lean, not a bound on the figure, which chance still moves.

4. **Non-blocking, needed before the coding step. The records pack does not hold ledger entries.** Step 3 *Later work* (:109) has the Critic code every entry the *Ledger entries* fields list, "from the records pack… (research/Q-018-extract/pack.py and pack2.py), which holds each listed record". Neither script reads `docs/LEDGER.md` (no match for "ledger" in pack2.py). In the current pack, #49's L-0156 (447cf875) is only "listed in window", and there is no records2 file for it. The pack must be widened to hold each entry as first added before step (2) of :114.
   - Self-implication (D-050): my brief 317 finding 13 proposed the pack as the coder's source without checking this.

5. **Non-blocking. "Not tilted" says more than the card.** Risks :236 and E-004:151 say "both sides are counted alike, so the comparison… is not tilted". The card says only "both sides are counted the same way" (:16); "the comparison stays fair" is the Chief of Staff's recommendation (:18), not the option. On trial pieces the deciding measure now includes questions about later work and about other work, among them question files a trial piece itself files about unrelated items (named by being its own file, :46). A method that changes how often those happen moves its side's count. Suggested wording: "counted by one rule with no judgement; a method that changes how often you ask for later or other work moves its own side's count". The re-count could also report how many touches the sample's "later work" codes take off, so that "a little high" has a size before the freeze.

6. **Brief 318's open questions (brief item 3).**
   - **(a) An entry that is itself the starting ruling skips a later copy: right.** Ruling 18 is "Also skip an entry when the piece's starting ruling holds the same words: the entry is that ruling" (decisions/questions/P-002-ledger-copy-of-start.md:1). It names the starting ruling whatever record holds it, and ruling 15 makes an entry "a decision record of its own". Checked on the records:
     - pack L51: 3681644a, #49's first commit, adds L-0155;
     - LEDGER.md:2234: L-0155's `decided_by:` holds "Merged, I want to go with your reccomendations on all of them";
     - LEDGER.md:2249: L-0156, added by 0862650a at 16:00:06, inside the window, holds the same passage, which also stands in 558fd054, first added in 3681644a.

     So the spec's "the same either way" (:48) holds.
   - **(b) For a piece dispatched by its brief record, the starting ruling is a record first added in the dispatch commit: right against the words.** Ruling 18 does not restrict "the piece's starting ruling" to pieces dispatched by their first commit, so it needs a definition for the other case. The definition chosen mirrors Q-018/U1. It is narrower than the plain meaning: an approval recorded before the dispatch that in fact started the piece is not covered, so its ledger copy counts. That is disclosed in step 6 (t) (:112). No sampled piece whose ledger is read is affected.

7. **Non-blocking. A different ruling with the same words is skipped, and no list says so.** The character-for-character skip (:48), from an answer record (ruling 15) and now also from a starting-ruling entry, also skips a later, different ruling whose passages are short and common. Many Personal-Org-Operating-Model entries quote only "A", "Approve" or "Approved" (LEDGER.md:1050–1604, 1740, 1768). Step 6 (r) lists the opposite cases (a reworded copy counts twice; two entries never skip each other) but not this under-count. Add it to (r).
   - Self-implication (D-050): brief 317 finding 9 saw this collapse for entry against entry only.

8. **Non-blocking, needed before the plan review passes. Ruling 19's decision record is not on this branch.** decisions/questions/P-002-live-later-work-check.md is cited at :10, :46, :52, :189, :197, :236 and :265, and at E-004:110 and :151, but is absent. The handoff (:44–47) gives it as not yet recorded, and the brief places it in PR #110.

9. **Brief 317's findings 5 to 13 (brief item 1).**
   - **5:** closed. A code the second Critic does not confirm is "not said, counts, listed with both readings" (:109); "until the owner rules" is gone from step 3.
   - **6:** closed. Both records now exist with the owner's exact words.
   - **7:** closed. J1 now reads "the script makes no judgement of a record's meaning" (:189). The old premise survives only as a Context bullet in decisions/questions/P-002-later-work-coder.md:21, which is true of when it was written.
   - **8:** closed. Step 6 (q) names L-0122 and L-0123 (:112), and the pack gives brief numbers and spec ids (:109). I could not compare with the Definer's table of expected changes, which is outside my pack.
   - **9:** closed (:48, step 6 (r)), with finding 7 above.
   - **10:** closed (RT1(a) :47, RT4 :52, step 6 (t)).
   - **11:** closed (:46, :109, the L-0124 case).
   - **12(3):** closed. J1 now says a log line with a record is never itself a touch (:189).
   - **13:** closed as written, but see finding 4.

10. **What blocks (brief item 4).**
    - The re-count: nothing in the text. In order, it needs findings 4 (the pack) and 8 (the record).
    - The freeze: finding 1, then the owner's choice on it, and the plan review re-run on the changed lines.

## Six-part contract
- **Changed:** nothing; I am read only.
- **Why:** brief 320, a re-check of briefs 318 and 319 before the re-count.
- **Verified:** Read, Grep and Glob only, with no shell and no git.
  - specs/S-002.md: lines 1–157, 172–178, 186–197 and 232–280.
  - experiments/E-004.md: lines 36–41, 99–153, and a grep for later work.
  - Brief 317's findings.
  - The card questions/P-002-live-later-work-check.md, on the branch.
  - The two decision records, and the handoff's lines 44–47.
  - research/Q-018-extract: the list of scripts, pack.py and pack2.py (grep), and sample.jsonl line 51.
  - Records pack q018-pack-307: L51-Personal-Org-Operating-Model-49.md, and a check that no records2 file exists for 447cf875.
  - The Personal-Org-Operating-Model clone's docs/LEDGER.md: L-0121 to L-0124, L-0155 to L-0157, and every `decided_by: owner (` line.
- **Undone:**
  - The diffs of 6df531d and d8c9fa7, and the card as at d0f290b (no git).
  - Spec lines 158–171 and 198–231 (the sections that do not bear on this check).
  - The Definer's table of expected changes, which my pack keeps out.
- **Needed outside its surface:**
  - The Definer: finding 1's disclosure, and findings 3 (`trial` match), 5 and 7.
  - The owner: finding 1's choice.
  - The Orchestrator: widen the pack (finding 4).
  - The Chief of Staff: ruling 19's decision record (finding 8).
  - Triage: my D-050 flags on findings 1, 4 and 7.
- **Open questions:**
  - Finding 1: how should the touch log's conversation lines on trial pieces be guarded, if at all?
  - Finding 5: should the re-count report how much the "later work" codes remove?

Files:
- /home/user/Model-Lab/specs/S-002.md
- /home/user/Model-Lab/experiments/E-004.md
- /home/user/Model-Lab/questions/P-002-live-later-work-check.md
- /home/user/Model-Lab/decisions/questions/P-002-later-work-coder.md
- /home/user/Model-Lab/decisions/questions/P-002-ledger-copy-of-start.md
- /home/user/Model-Lab/docs/handoff/2026-11-12-chief-of-staff-p002-16.md
- /home/user/Model-Lab/reviews/S-002-rulings-2/_critic-verbatim.md
- /home/user/Model-Lab/research/Q-018-extract/pack2.py
- /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/q018-pack-307/L51-Personal-Org-Operating-Model-49.md
- /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/hc/Personal-Org-Operating-Model/docs/LEDGER.md
