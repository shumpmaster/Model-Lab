# The Critic's re-check of brief 326 (brief 327)

*Recorded verbatim by the Orchestrator; the verdict file is reviews/S-002-rulings-6/critic.md. Brief 327 (docs/briefs/327-critic.md), on Model-Lab@d8df6ad, S-002 and E-004 as changed by brief 326 (deb78d1, merged at bb91a8e). The Critic runs on a different model from S-002's writer and from brief 326's Definer (D-056), apart from the Critics of briefs 315, 317, 320, 322 and 325.*

Verdict: FAIL

Brief 326 did what it was asked. All six of brief 325's findings it was given (1, 2, 3, 4, 6 and 7) are closed in the text, and nothing in the text blocks the re-count. Two small things still block the freeze, and both sit inside the new rule that gives the result "both ways". First, that rule is triggered only by a touch the owner adds on a withdrawn piece. A touch the keeper itself logs on that piece after the withdrawal, which the owner then sees and confirms, triggers nothing, is listed nowhere and is in no limits list, so the keeper, who knows the sides, can avoid the safeguard by its own action. Second, the plan does not say what a trial's result is when the two ways differ at the first look and the deciding result was "go on to the second look": it says no new piece is drawn, yet also that the first result still decides, and it does not say whether the owner may then order the second look. Each needs a sentence, not a new ruling. The second also belongs on the owner's scenario card. The Definer's four open questions are otherwise answered "right", with wording notes.

## Findings

1. **Brief 325's findings 1, 2, 3, 4, 6 and 7: all closed in the text (brief item 1).**
   - Finding 1 (the list is checked): /home/user/Model-Lab/specs/S-002.md:197 has the desk's record hold the list as shown, the Reviewer check it against the trial's log and the touch log, and a touch line count only when a confirmed list or the answer holds it. The same is at S-002.md:10, :82, :174, :192, :233, :266 and /home/user/Model-Lab/experiments/E-004.md:20, :86, :101, :113, :132, :153.
   - Finding 2 (look 2): "the look's pieces" is defined once at S-002.md:197 ("here and in E-004 always means ..."), and look 2's list holds the pieces of both looks. E-004.md:84 now says "the look's counted pieces" for the hold-up tests, and S-002.md:175 says "the pieces entered at that look" for the short reads. I found no use in another sense.
   - Finding 3 (a) and (b): the same-commit rule is at S-002.md:82, :197 and E-004.md:86, :132; "all the look's answers together" is at S-002.md:197 and E-004.md:86.
   - Finding 4: "shown without the sides" is in the design half at S-002.md:10, :174, :233 and E-004.md:153; the bracketed lists at S-002.md:197 and E-004.md:86 now name "the rule for lines after the confirm line".
   - Finding 6: the two cases are in the plain words (S-002.md:10), Open question 20 (:266), the limits lists (S-002.md:192, :197, :233; E-004.md:39, :86, :102, :153) and the both-ways working (S-002.md:197; E-004.md:86, :113). The wording at S-002.md:197 now names the two exceptions to "once the log and the answer agree" and says an out-of-window added touch is not written. Left open by it: findings 2, 3 and 4(a) below.
   - Finding 7: the least the record holds, and that the owner makes it, are at S-002.md:197 and :272; the Step 0 condition is at E-004.md:30. Left open by it: finding 4(b) below.

2. **Blocking for the freeze (not the re-count), for the Definer. The both-ways rule for a withdrawn piece is triggered only by a touch the owner adds.**
   - S-002.md:197: "On a withdrawn piece, an added touch ... or a strike changes no count ... the Reviewer also works out the look's result with every withdrawn piece that has one put back". E-004.md:86 says the same ("every withdrawn piece that has an added touch"). J4 lists only "the added and struck lines on its withdrawn pieces" (S-002.md:192; E-004.md:101).
   - Condition (i) of a withdrawal rests on touch-log lines "committed so far" (E-004.md:121). A touch the keeper leaves out until the piece is withdrawn and refilled, then logs, stands on the owner's list as a logged touch on a withdrawn piece (S-002.md:197 shows withdrawn pieces with every touch line). The owner confirms it and has no reason to add it. It counts on nothing, no other-way result is worked, the results card does not list it, and no limits list names it.
   - The count effect is the same as never logging the touch, which is a stated limit, but this route closes the one catch the plan claims for that case. It is capped by the 3 withdrawals a look.
   - E-004.md:121 has the Reviewer "check every withdrawal again", but gives no consequence when condition (i) no longer holds.
   - Fix: key the other-way result, and J4's listing, on every withdrawn piece that has any touch a confirmed list or an answer holds and that is not struck, whoever wrote the line. Say what the Reviewer's re-check of a withdrawal does when (i) fails.
   - Self-implication (D-050): brief 325's finding 6, my role's, framed the case as "the owner then adds the touch" and proposed the fix in those terms.

3. **Blocking for the freeze, for the Definer, then the scenario card. The Definer's question (3): the result when the two ways differ is not defined at look 1's branch.**
   - S-002.md:197 and E-004.md:86: if a result worked the other way differs "in whether the look passes or, at look 1, whether it goes on", "no new piece is drawn and the results card brings both results to the owner". E-004.md:113 says the other-way result "does not decide".
   - At look 2, or at look 1 on pass against not pass, this hangs together: the deciding result stands, and the owner sees both and rules on the method as on any result (T13). No further rule is needed there.
   - Where look 1's deciding result is "go on", the text does not hang together. The deciding result says draw 30 more each way; the rule says draw none. J4's `Result:` line (S-002.md:192) and "Reported as" (E-004.md:145) have no value for it. Nothing says whether the owner may order the second look. A second look taken by the owner's choice after seeing both results is not the planned look the line's figures assume (E-004.md:78, T16).
   - Fix, one sentence, in the form of E-004.md:130: say the look then has no deciding result, or that the trial is reported as stopped as under P7, and that the second look is not taken. Or say the owner may rule it taken, and put that on the scenario card as a choice.
   - Self-implication (D-050): brief 325's finding 6 proposed "the trial coming to the owner if the two differ" without asking what the trial's result then is.

4. **Non-blocking, to fix in the same pass, before the scenario card.**
   - (a) J3's limits list (S-002.md:191) leaves out the two cases and the both-ways result, while the entry card's own item carries them (E-004.md:39). The join test for J3 would be written from J3.
   - (b) AC12 (S-002.md:177) and the last sentence of the plain words (S-002.md:10) still give three conditions for starting a trial. Step 0 now has a fourth, the desk's record (E-004.md:30), and no acceptance criterion covers it.
   - (c) "Its place worked as a place left empty" (S-002.md:197; E-004.md:86): E-004.md:130 judges such a look on the pieces it has and also with the place filled in every way. Say which of these is the other-way result. Say also whether the two other ways are worked apart only or together as well when a look has both kinds of piece, and what "in place of the reserve place its withdrawal opened" means when that reserve piece was itself withdrawn and refilled.
   - (d) The Reviewer's check sentence reads "a touch line ... that the list does not hold" (S-002.md:197; E-004.md:86). Read to the letter at look 2, that flags every look-1 line confirmed at look 1; the next sentence's bracket ("look 1's list or look 2's") gives the meaning. Write the check as "that no confirmed list holds".
   - (e) J1 says a struck line "is not recorded", without condition (S-002.md:189). J9 says a strike after the confirm line, or one the answer does not hold, is not applied (S-002.md:197). The log has no form for undoing a strike, though "the Chief of Staff correcting the log" is the remedy. Between looks, a strike the owner never gave takes a touch out of the count's figures unchecked.
   - (f) The same-commit rule ("above it in the log") assumes one file; the log is one file a month (S-002.md:197). A commit that spans two months' files is not settled.
   - (g) Carried from brief 325 finding 5, still open: J2's `brief` field has no form (S-002.md:190), and count.jsonl holds an entry with no brief in its trailers as `trial: null` (S-002.md:189).

5. **The Definer's open questions (brief item 2).**
   - (1) Both cases as "the correction does not do what it would on a piece still open": right for the withdrawn piece; loose for the settled one, where a strike on an open piece also leaves it not needing the owner and the real difference is that it would later have been withdrawn. Each case is spelled out straight after the phrase, so no reader is misled. For the scenario card, "counting on nothing" (S-002.md:10) wants plainer words, such as "does not count".
   - (2) A withdrawn piece put back in place of its reserve place: right. Had the touch been logged, the piece would have stayed on its side as needing the owner and no reserve place would have opened. Gaps: finding 2, and the chain case in finding 4(c).
   - (3) "A difference brings the trial to the owner", with no rule for what the owner rules: right at look 2 and on pass against not pass; a gap at look 1's "go on" branch (finding 3).
   - (4) At look 2, a first-look piece's lines from before look 1's confirm line are not shown again: right. Every such line stood on look 1's confirmed list or went back to the owner before look 1 was judged, and strikes are log lines that stand at both looks. The one cost is that the owner cannot strike at look 2 a first-look line they are no longer shown. That can be carried on the scenario card as a limit; it does not block. Wording: finding 4(d).

6. **What blocks (brief item 3).**
   - The re-count: nothing in the text. Step (5)'s figure is at S-002.md:114. On brief 325's pack item, /home/user/Model-Lab/research/Q-018-extract/pack2.py now matches "ledger" 9 times (pack.py has no match); I did not read what it packs.
   - The freeze: findings 2 and 3. Neither can be stated as a limit as it stands: finding 2 is a safeguard the text claims and the keeper can avoid, and finding 3 is a branch with no result. Finding 2 could become a limit only if every limits list said the both-ways working can be avoided this way, which is worse than the one-clause fix.
   - Text fixes in the same pass, not blocking on their own: finding 4 (a) to (f).
   - For the owner's scenario card, as this plan's design: strikes; the list without sides; look 2's list of both looks, with first-look lines not shown again; the desk's record; counting only confirmed lines; the two both-ways cases and what happens when they differ (finding 3); no time limit.
   - Before the first trial, not the freeze: the Service Desk work (S-002.md:272), which Step 0 now makes a condition; and the plan review re-run on the changed lines.

## Six-part contract
- **Changed:** nothing; I am read only.
- **Why:** brief 327, a re-check of brief 326 before the re-count and the freeze.
- **Verified:** Read and Grep only; no shell, no git.
  - Read in full: /home/user/Model-Lab/AGENTS.md, my charter, docs/briefs/327-critic.md, 326-definer.md and 322-critic.md; reviews/S-002-rulings-5/_critic-verbatim.md; decisions/questions/P-002-touch-log-check.md; experiments/E-004.md.
  - Read of specs/S-002.md: lines 1 to 95, 112 to 114, 170 to 197 and 228 to 281.
  - Grep of both files for "look's pieces", "the look's counted" and "added touch": the lines cited above.
  - Grep of research/Q-018-extract/*.py for "ledger": extract.py 21, pack2.py 9, pack.py none.
- **Undone:**
  - specs/S-002.md lines 96 to 111, 115 to 169 and 198 to 227 were not read; brief 326 was to leave the hand check's rules alone, and I could not confirm that without git.
  - The diff of deb78d1 and the Definer's table were not seen, so I checked the text as it stands.
  - The card at 55e645e was not read; I relied on the note in brief 322.
  - Not read: docs/projects/P-002.md, the trial terms, the Service Desk's records, docs/DIGEST.md and the open sprint. pack2.py's content was not read.
  - The first-message line naming the model is left out, by the instruction to keep model names out of this return.
- **Needed outside its surface:**
  - The Definer: findings 2 and 3, then 4 (a) to (f).
  - The Chief of Staff: the scenario card carrying finding 3's choice and the items in finding 6, in plainer words than S-002.md:10.
  - The Orchestrator: the Researcher's brief asking for step (5)'s figures; the plan review re-run on the changed lines.
  - Triage: my D-050 flags on findings 2 and 3.
- **Open questions:**
  - Finding 2: should the other-way result run for any confirmed, unstruck touch on a withdrawn piece, and what does the Reviewer's re-check of a withdrawal do when condition (i) no longer holds?
  - Finding 3: when the two ways differ at look 1 and the deciding result is "go on", is the trial stopped with no deciding result, or may the owner order the second look?
  - Finding 4(c): is the other-way result for a settled piece the look judged on the pieces it has, or also filled in every way?

Files:
- /home/user/Model-Lab/specs/S-002.md
- /home/user/Model-Lab/experiments/E-004.md
- /home/user/Model-Lab/docs/briefs/327-critic.md
- /home/user/Model-Lab/docs/briefs/326-definer.md
- /home/user/Model-Lab/docs/briefs/322-critic.md
- /home/user/Model-Lab/reviews/S-002-rulings-5/_critic-verbatim.md
- /home/user/Model-Lab/decisions/questions/P-002-touch-log-check.md
- /home/user/Model-Lab/research/Q-018-extract/pack2.py
