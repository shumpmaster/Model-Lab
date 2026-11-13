# The Critic's re-check of brief 329 (brief 331)

*Recorded verbatim by the Orchestrator; the verdict file is reviews/S-002-rulings-7/critic.md. Brief 331 (docs/briefs/331-critic.md), on Model-Lab@597112a, S-002 and E-004 as changed by brief 329 (d2f0543, merged at 4a8df07). The Critic runs on a different model from S-002's writer and from brief 329's Definer (D-056), apart from the Critics of briefs 315, 317, 320, 322, 325 and 327. The Orchestrator's git check the Critic asked for: from 7bdf340 (main before brief 321) to 4a8df07, the hand check's lines changed only at S-002 :112 (step 6 (r), brief 321) and :114 (step (5)'s reported figures, briefs 321 and 324).*

Verdict: PASS

Nothing in brief 329's change blocks the freeze, but I did not read all of the plan and could not see the change itself, only the text as it stands (see Undone). Both things that blocked last time are now closed in the text: the "result worked the other way" now runs for any confirmed, unstruck touch on a withdrawn piece, whoever logged it, and the plan now says the trial is reported as stopped, with no second look, when the two results differ at a first look that would have gone on. The smaller fixes of brief 327 are all in. The Definer's four open questions are answered "right", each with a limit worth stating. Four small things are left, none of which makes the plan say something false or leaves a branch without a result. The closest call is the new line for undoing a strike: the plan applies it whenever it is written and gives as the reason that it only restores what the owner answered, but no check is named for it between the two looks. I rate that non-blocking because the same-look case is caught by the existing rule that the log and the answer must agree, and the rest can be closed by one clause or stated as a limit. If the caller reads the acceptance criterion strictly ("the owner's own answers to that look"), it is the one item that could be argued the other way. Nothing here is irreversible. The owner's scenario card must carry the stop at look 1 as a choice of this plan's, not of the ruling.

## Findings

1. **Brief 327 finding 2: closed (brief item 1).**
   - The key is now "a touch line a confirmed list or the answer holds and that is not struck, whoever wrote it": /home/user/Model-Lab/specs/S-002.md:197 ("the owner adding it or the Chief of Staff logging it"), :174 (AC9), :192 (J4); /home/user/Model-Lab/experiments/E-004.md:20, :86, :101 (Step 8), :113.
   - The re-check's consequence is at E-004.md:121: the withdrawal stands, the piece is listed with its side and the touch, and it is put back in the other-way result. S-002.md:197 and :192 carry the same.

2. **Brief 327 finding 3: closed.**
   - E-004.md:79 (Step 5, item 4), :86, :145 ("Reported as"); S-002.md:192 (`Result: stopped`, "as under ruled P7"), :197, :174, and the plain words at :10.
   - It is marked "by this plan's design, for the owner's scenario card" at each place, and the bracketed design lists at S-002.md:197 and E-004.md:86 name it.
   - I checked the other branches. Deciding result "passed" or "not passed" at look 1, and any difference at look 2: the deciding result stands and both go on the card. Deciding result "go on" and the other way differs: stopped. No branch is left without a result.

3. **Brief 327 finding 4 (a) to (g) and finding 5: closed.**
   - (a) J3 now carries the two cases, the other-way result and the stop: S-002.md:191.
   - (b) The fourth start condition is in AC12 (S-002.md:177) and the last sentence of the plain words (:10).
   - (c) The settled case is "judged on the pieces the look then has ... and not also with the place filled in every way"; the two ways are worked "apart and, when a look has pieces of both kinds, together as well"; the chain is "worked from the first": S-002.md:197; E-004.md:86.
   - (d) "that no confirmed list holds": S-002.md:197; E-004.md:86. No use of the old wording is left (Grep).
   - (e) J1's strike is conditioned on a later confirm line of a look whose pieces include the struck line's piece (S-002.md:189), and the unstrike form is at :197. A strike on a piece outside any look is therefore never applied, which is right. See finding 5.
   - (f) Monthly files are read in month order: S-002.md:82, :197; E-004.md:86, :132.
   - (g) Settled by a sentence, no new field: J2's `brief` takes the form the trailers are read in (S-002.md:190), and a trial piece whose trailers give no brief is listed and taken as a trial piece by the Reviewer (:189).
   - Finding 5: "counting on nothing" is gone; S-002.md:10 reads "not counting at all" (Grep finds no "on nothing" in either file).

4. **The Definer's open questions (brief item 2).**
   - (1) The settled case worked only on the pieces the look has: right. A comparison needs one result, and E-004.md:130's "every way" working gives a set, not one. The limit: the true other case is a refill by an unknown piece, so this one result can miss a difference that a refill needing the owner would have shown. It is marked as this plan's design. It can go on the scenario card in a clause; it does not block.
   - (2) Putting the first withdrawn piece back takes out every reserve place its withdrawal led to: right. Had the touch been logged, no reserve place would have opened, and each side returns to 30. One wording gap in finding 6.
   - (3) The failed re-check counting a touch the records show: right. Condition (i) reads "in the records or in touch-log lines" (E-004.md:121), records touches are not subject to the owner's confirmation, and a records touch timed before the withdrawal line means the withdrawal should not have been made. No gap.
   - (4) "Reported as" naming only some stops (E-004.md:145): right enough. The fourth withdrawal or void entry (E-004.md:121) and the empty place with no deciding result (:130) are each worded "as under P7", so P7 covers them by reference. The new stop is also "as under P7" yet is named apart, so the list reads uneven. A wording note, not a gap in results; J4's awkward cases name each (S-002.md:192).

5. **Non-blocking, the closest call. The unstrike line has no named check between the looks.** S-002.md:197: the unstrike "is applied whenever it is committed, since it only brings the log back to the answer".
   - Within one look this is covered: an unstrike of a strike the answer holds leaves the log and the answer disagreeing, and "the look is judged only once the log and the answer agree" (S-002.md:197; E-004.md:86).
   - Between look 1's judging and look 2 it is not clearly covered. A look-1 line the owner struck, then unstruck in the log, is not shown again at look 2 (only lines and strikes committed after look 1's confirm line are, S-002.md:197), and it counts at look 2 because look 1's list held it. AC9 has the Reviewer check "the owner's own answers to that look" (S-002.md:174); E-004.md:20 says "the owner's answers", which could reach look 1's.
   - Why not blocking: the plan states the Reviewer's check of the log against the answer as the safeguard, with its limits; this is a refinement of that check for one new line type. The route is limited to lines the owner struck at look 1, in trials that take the second look. No sentence is false on the plan's own premise ("undoes a strike the answer does not hold"), and the branch has a result.
   - Fix, one clause: the Reviewer checks every unstrike line against the answers, at look 2 those of both looks, and one that undoes a strike an answer holds is listed and not applied. Or state it as a limit.
   - Self-implication (D-050): brief 327's finding 4(e), my role's, asked for "a form for undoing a strike" and did not ask that the form be checked.

6. **Non-blocking wording, statable as limits.**
   - (a) The chain bracket at S-002.md:197 names only a reserve piece "withdrawn too". A reserve piece that became a void entry also opens the next reserve place (E-004.md:129). The governing words "the reserve places its withdrawal led to" (S-002.md:197; E-004.md:86) cover it; the bracket should say "withdrawn or void".
   - (b) The first key has no time condition, while the re-check's has ("timed before its withdrawal line", E-004.md:121). A confirmed touch timed after the withdrawal puts the piece back though the withdrawal was right. The effect is only that the other-way result is worked, and at worst a trial stops or comes to the owner; it cannot pass a method. Self-implication (D-050): brief 327's finding 2, my role's, proposed the key in those words.
   - (c) E-004.md:86 leaves out "out of the hold-up measures" for a piece put back; S-002.md:197 has it, and E-004 cites J9.

7. **What blocks (brief item 3).**
   - The freeze: nothing I found. Findings 5 and 6 can be fixed in a clause each or stated as limits. If any text is touched before the freeze, finding 5's clause is the one worth adding.
   - For the owner's scenario card, as this plan's design: the stop at look 1 when the two results differ (finding 2); the settled case's single other-way result and its limit (finding 4 (1)); strikes and their undoing; and the items brief 327's finding 6 listed.
   - Carried, not new and not from brief 329: cases worded "the trial comes to the owner" with no `Result:` value named (for example E-004.md:70). I did not re-open them.

## Six-part contract
- **Changed:** nothing; I am read only.
- **Why:** brief 331, a re-check of brief 329 before the design goes to the owner's scenario card.
- **Verified:** Read and Grep only; no shell, no git.
  - Read in full: /home/user/Model-Lab/AGENTS.md, my charter, docs/briefs/331-critic.md, 329-definer.md and 322-critic.md; reviews/S-002-rulings-6/_critic-verbatim.md; decisions/questions/P-002-touch-log-check.md; experiments/E-004.md.
  - Read of specs/S-002.md: lines 1 to 92, 170 to 197 and 228 to 281.
  - Grep of both files for "on nothing", "unstrike", "has an added touch", "that has one put back" and "the list does not hold": only "unstrike" matches, at S-002.md:189 and :197 and E-004.md:86.
- **Undone:**
  - specs/S-002.md lines 93 to 169 and 198 to 227 were not read. Brief 329 was to leave the hand check's rules alone; I could not confirm that without git.
  - The diff of d2f0543 and the Definer's table were not seen; I checked the text as it stands.
  - The card at 55e645e was not read; I relied on the note in brief 322.
  - Not read: docs/DIGEST.md, the open sprint, docs/projects/P-002.md, the trial terms, the Service Desk's records. reviews/Q-018-later-work/ and the scratchpad were not opened, as instructed.
  - The first-message line naming the model is left out, by the instruction to keep model names out of this return.
- **Needed outside its surface:**
  - The Definer, only if the text is touched again before the freeze: finding 5's clause, then 6 (a) to (c).
  - The Chief of Staff: the scenario card carrying the items in finding 7, and finding 5 as a limit if its clause is not added.
  - The Orchestrator: the plan review re-run on the changed lines, and a check by git that the hand check's rules are untouched.
  - Triage: my D-050 flags on findings 5 and 6 (b).
- **Open questions:**
  - Finding 5: does the look-2 Reviewer check look 1's answers too (E-004.md:20's "answers") or only look 2's (AC9's "to that look")? If only look 2's, should the caller treat finding 5 as blocking?
  - Finding 6 (b): should the first key take the same time condition as the re-check?

Files:
- /home/user/Model-Lab/specs/S-002.md
- /home/user/Model-Lab/experiments/E-004.md
- /home/user/Model-Lab/docs/briefs/331-critic.md
- /home/user/Model-Lab/docs/briefs/329-definer.md
- /home/user/Model-Lab/docs/briefs/322-critic.md
- /home/user/Model-Lab/reviews/S-002-rulings-6/_critic-verbatim.md
- /home/user/Model-Lab/decisions/questions/P-002-touch-log-check.md
