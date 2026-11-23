Verdict: PASS

*The Critic's check of the two Build gate cards for P-002, questions/P-002-build-gate.md and questions/P-002-build-gate-terms.md. Round 1: brief 347 (docs/briefs/347-critic.md), a fresh session on a different model from the cards' writer, read from a fixed copy at Model-Lab 809bb44; FAIL, two blocking findings on the gate card, none on the terms card. Recorded verbatim by the orchestrator, 2026-11-22. Round 2: brief 348 (docs/briefs/348-critic.md), a fresh session, read from a fixed copy at Model-Lab 4708e7f; PASS, no blocking finding. Its non-blocking findings 1 and 2 (gate card) were then applied as wording only, and the WHO HAS CHECKED IT lines brought up to date; no claim changed otherwise. The header verdict is the latest round's.*

## Round 1
Verdict: FAIL

Both cards were read against the fixed copy at /tmp/claude-0/-home-user/46a16990-6c77-5cf3-ac0a-e9b9f3fdee4e/scratchpad/ml-fixed-346 (Model-Lab at 809bb44). Paths below are relative to it. The gate card has two blocking findings and the terms card has none.

**Gate card: questions/P-002-build-gate.md**

1. BLOCKING, check (1). The opening paragraph says "Nothing failed and nothing was skipped", but the plan's review failed more than once.
   - reviews/S-002/plan.md shows round 1 FAIL (:6), round 2 FAIL (:133), a re-check after round 3 FAIL (:340) and a re-run FAIL (:545).
   - Each failure led to an owner ruling at a plan stop (decisions/questions/P-002-plan-stop-2.md; S-002 open question 21 at specs/S-002.md:267).
   - The rounds ended in PASS, and the same card's Context cites the passing checks. That is the reason the plan can go forward. It does not make "nothing failed" true.
   - The card is meant to lead with anything failed. Fix: add one plain clause saying the plan failed its review several times and the owner ruled at two plan stops. The card can then say it passed on the later checks.

2. BLOCKING, check (3). The list of what approval carries beyond earlier rulings, items (i) to (iv), leaves out limits the plan itself states, and they touch the value target. The sources are specs/S-002.md:233, :234, :236, :190 and :191.
   - **Counts run high.** On a trial piece every question and note counts, and the plan says this leans against the starting figure, toward a miss of V1 rather than a pass (:236). The gate card does not state it.
   - **The touch-log keeper.** The Chief of Staff keeps the log, knows the sides, and decides whether a conversation touch is logged at all and which piece it is put against (:233). The card's (iii) lists only "a touch you too do not recall". The owner's confirmation guards this only in part, which the card does not say.
   - **Not blind.** The agents know the side. Only the short reads are unlabelled (:234). This is also missing.
   - The card does carry the folded-work limits, the unjudged-look limit, the sides-known limit (also on the terms card as term 10) and the withdrawn-piece and settled-piece exceptions.
   - Fix: add these to (iii), or say plainly that they are carried by pointing to the plan.

3. Not blocking, check (1). The cold read is hard in places.
   - The opening paragraph has no paths or ids, which is good.
   - The terms "look", "sides", "desk" and "touches" are never explained on either card. The "sides" are the two arms of a trial, with the method and without it. A "look" is a planned judging point.
   - Option A (i) is one very long sentence-stack. Break it into short items.

4. Not blocking, check (2). These claims hold.
   - 14 of 33 and 11 of 26 match research/Q-018-memo-5.md:137 and :138.
   - Build-1 to Build-5 and Launch-1 to Launch-5 exist in docs/projects/P-002.md (:131 to :135, :142 to :146).
   - The ceilings match decisions/questions/P-002-design-gate.md:10 and :11.
   - The four non-blocking join-up differences match findings 3 to 6 in reviews/S-002/plan.md (:308 to :311).
   - The claims on the desk record match E-004 Step 0 (experiments/E-004.md:29) and S-002 :274.

5. Check (5) is mostly right. Risk class R0, irreversible, no default and no timeout fit a phase gate, with kill as the irreversible option. Nothing wrong there. The card's four options are within the P-001 ruling, which allows "sizes, hold, recycle and kill".

**Terms card: questions/P-002-build-gate-terms.md**

6. Check (4) holds. The eight open questions, 2 to 9 in specs/S-002.md:248 to :255, map to terms 1 to 8 (2→1, 3→2, 6→3, 7→4, 4→5, 5→6, 8→7, 9→8). Nothing open is missing.
   - Terms 9 to 11 are extra points. For term 9, the source open questions are at reviews/Q-018-extract/critic.md:70 and :71. For term 11, decisions/questions/P-002-check-named-by-statement.md is dated 2026-11-14 and says "own files only".
   - The Context line "1 and 10 to 22 answered, 2 to 9 open" is correct.
   - The split follows decisions/questions/P-001-build-gate-stop.md: terms 1 to 4 are argued (touch counting, value target, a model-rule exception, an earlier ruling), and 5 to 11 are listed.

7. Not blocking, check (2). Term 4's cost line, "both tests collect pieces more slowly from the same work", is not in specs/S-002.md open question 7 or in any record I could find. It is the Chief of Staff's inference. Mark it as such or cite a source.

8. Not blocking, check (4). Term 8 (open question 9) leaves out the plan's own warning at :255 that whoever hands out the work could merge two pieces or hand one out twice to move later pieces' sides, which the refill and limit cap but do not catch. Term 10 covers sides-known in general. One clause would make term 8 fair.

9. Not blocking, check (2). Term 9 is introduced as the plan's proposed answer, but the plan makes no proposal for those two points. They were left "with the Definer and the owner" (reviews/Q-018-extract/critic.md:113). "Keep as written" is the Chief of Staff's answer, and the card should say so.

10. Check (5) holds. R0, reversible, default none and timeout none are right, since answers are written into the plan before the freeze. The terms card does bear on the value target in terms 1 and 2, and it says so.

**Six-part contract**
- **Changed (by file):** nothing. I am read-only and wrote no file.
- **Why:** brief 347 asks for a cold critic round 1 of the two Build gate cards for P-002.
- **Verified:** by reading only. I read both cards in full and specs/S-002.md :1-85, :163-193 and :232-270. I read specs/S-002.md :274, :157-160, experiments/E-004.md :29 to :36, and decisions/questions/P-001-build-gate-stop.md. I also read decisions/questions/P-002-check-named-by-statement.md, parts of reviews/S-002/plan.md (the round verdicts), research/Q-018-memo-5.md :137 and :138, docs/projects/P-002.md :125 to :146, decisions/questions/P-002-design-gate.md :10 and :11, and reviews/Q-018-extract/critic.md :66 to :73. From the operating model I read OPERATING_MODEL.md :242 and the heading list.
- **Undone:**
  - Most of specs/S-002.md :86-162 and :194-231.
  - experiments/E-004.md beyond Step 0, so I could not trace every limit in "What this trial cannot catch".
  - Most of experiments/E-004.md and docs/projects/P-002.md, including the section 6 definition of a touch.
  - reviews/P-002/_build-gate-1-critic.md and docs/gates/P-002/build-gate-1-case.md, which I only searched.
  - questions/_TEMPLATE.md and AGENTS.md §4 and §5 for exact form, which I judged from the P-001 precedent.
  - The operating model's §2 and §5 citations, which I only matched by heading.
  - The passed P-001 cards, which are not in the copy.
- **Needed outside my surface:** the Chief of Staff redrafts the gate card for findings 1 and 2, and optionally the points in findings 3, 7, 8 and 9. The Orchestrator then sends a round 2.
- **Open questions:** whether the plan's earlier failures belong in the opening or only in Context. I think the opening, because the form leads with failures. Also, is "look" and "sides" jargon acceptable to the owner? The owner has seen it throughout the plan's cards.

## Round 2
Verdict: PASS

Round 2 of the Critic's check of questions/P-002-build-gate.md and questions/P-002-build-gate-terms.md. I read both from the fixed copy at /tmp/claude-0/-home-user/46a16990-6c77-5cf3-ac0a-e9b9f3fdee4e/scratchpad/ml-fixed-348. Paths below are relative to it. Neither card has a blocking finding.

**Round 1's findings**
- **Finding 1 (opening said nothing failed): fixed.**
  - The gate card now says "The plan failed its review four times before it passed", and that you chose a focused fix at a plan stop after two of them.
  - reviews/S-002/plan.md has four FAILs: round 1 (:6), round 2 (:133), the re-check after round 3 (:340) and the re-run (:545).
  - The owner's rulings are decisions/questions/P-002-plan-stop.md and P-002-plan-stop-2.md, each "A: focused fix (Recommended)". The re-check and the re-run are the two failures that led to them.
  - The opening has no paths or ids.
- **Finding 2 (limits missing from option A (iii)): fixed.** All three omissions are now in (iii), and each matches the spec.
  - Counts run high, leaning toward a miss: specs/S-002.md:236.
  - The Chief of Staff's log decides whether a touch is logged and which piece it goes on, and your confirmation guards this only in part: :233.
  - The trial is not blind, and only short reads are unlabelled: :234.
  - The folded-work limit holds. A fold into work with no brief, all begun after the entry, is not listed (experiments/E-004.md:151).
- **Finding 3 (jargon, long option): fixed.** The card now has a "Words used" line defining sides, look and desk. "Touches" is defined in the opening as "a time you stepped in before the work merged". Option A (i) is now six short items.
- **Finding 7 (term 4's cost): fixed.** The cost is now marked "in the Chief of Staff's judgement (no record measures it)".
- **Finding 8 (term 8's warning): fixed.** Term 8 now carries the plan's warning about merging two pieces or handing one out twice, and that the refill and limit cap it but do not catch it (specs/S-002.md:255).
- **Finding 9 (term 9's source): fixed.** The terms card says the plan has no proposed answer of its own and that the Chief of Staff proposes keeping it as written. That matches reviews/Q-018-extract/critic.md.

**Gate card: questions/P-002-build-gate.md**

1. Not blocking, check (2). In (iii), "leaning toward a miss of your target rather than a pass" drops the plan's own qualifier. The plan says "that is the rule's lean, not a bound, since chance and other differences … can still move such a share either way" (specs/S-002.md:236). Adding "this is a lean, not a bound" would make it exact. The statement is not false as written.
2. Not blocking, check (3). The card's list of misses leaves out one the plan states: "a touch put on a piece outside the look's list" (specs/S-002.md:233 and open question 20 at :266). The card does have the wrong-piece-you-confirm case. One clause would complete it.
3. Not blocking, check (1). The opening is one long paragraph of about 230 words. It leads with the failures and has no paths or ids. Splitting the last four sentences into a second short paragraph would help a cold reader. It is readable as it stands.
4. Check (2) holds. These claims are all true of the records:
   - The 14 of 33 figure matches research/Q-018-memo-5.md:137.
   - The ceilings, the Build and Launch standard lines, and the four join-up differences are carried over from round 1, where I checked them.
   - The desk-record claims match specs/S-002.md:274.
   - The Context line on the four failures matches reviews/S-002/plan.md, header and rounds.
   - The Locked checks line (specs/S-002.md:281) supports "The Check author writes the locked checks, then the Builder builds".
   - I could not find the sentence "Once frozen, the plan can change only through a new plan" in the files I searched. It is the standard meaning of a freeze and was present, unflagged, in round 1.
5. Check (5) holds. The risk class is R0, reversibility irreversible (kill is option D), and default and timeout are none, which fits a phase gate. The four options fit the P-001 ruling.

**Terms card: questions/P-002-build-gate-terms.md**

6. Check (4) holds.
   - Terms 1 to 8 still map one-to-one to open questions 2 to 9 (specs/S-002.md:248 to :255), so nothing open is missing.
   - Terms 9 to 11 are the extra points.
   - The Context line "1 and 10 to 22 answered, 2 to 9 open" is correct (:247, :256 to :268).
   - The split follows P-001-build-gate-stop.md: terms 1 to 4 are argued and 5 to 11 are listed.
7. Not blocking, check (2). The new wording on term 8 holds. "A place still empty is judged filled every way, and decides only if every way agrees" matches :255. Term 7's shared limit of 3, the 60 days and the 7 days match :254.
8. Check (5) holds. R0, reversible, no default and no timeout are right, because answers are written into the plan before the freeze. The card says terms 1 and 2 bear on the value target.
9. The WHO HAS CHECKED IT line says round 1 found nothing blocking on this card. That is true. It is a round-1 record, so the line stays current only if the orchestrator updates it after this round. This is a note, not a finding.

**Six-part contract**
- **Changed (by file):** nothing. I am read-only and wrote no file.
- **Why:** brief 348 asks for a cold round 2 of the two cards. It checks round 1's blocking findings 1 and 2 and its non-blocking findings 3, 7, 8 and 9, and runs the five checks again on the redrafted cards.
- **Verified:** by reading only.
  - I read both cards in full, the round 1 record, and briefs 347 and 348.
  - I read specs/S-002.md :1-10, :46 to :56 (skimmed for the rule text), :225 to :274 and :281.
  - I read reviews/S-002/plan.md :1-8 and its heading list, decisions/questions/P-002-plan-stop.md and P-002-plan-stop-2.md in full, and experiments/E-004.md :151 by search.
  - Round 1's checks of the memo figures, the ceilings and the standard lines are carried over, not re-read.
- **Undone:**
  - I did not compare the pre-redraft copy in ml-fixed-346 line by line. I judged the redraft against round 1's findings.
  - I did not re-read experiments/E-004.md beyond the searched lines, or docs/projects/P-002.md.
  - I did not find where "Once frozen, the plan can change only through a new plan" is stated.
  - I did not re-check AC18 or AC14 beyond the 26-week lines.
- **Needed outside this surface:** optionally, the Chief of Staff makes the small edits in gate card findings 1, 2 and 3, and updates the terms card's checked line to cite this round. Neither is required for the PASS.
- **Open questions:** whether the one-paragraph opening is short enough for the owner. I think it is acceptable now that the words are defined. Also whether the "lean, not a bound" qualifier matters to the owner. It bears on how far to trust a trial count against the 60-piece starting figure, so I would add it.
