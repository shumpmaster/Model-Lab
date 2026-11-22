Verdict: FAIL

*The Critic's check of the two Build gate cards for P-002, questions/P-002-build-gate.md and questions/P-002-build-gate-terms.md. Round 1: brief 347 (docs/briefs/347-critic.md), a fresh session on a different model from the cards' writer, read from a fixed copy at Model-Lab 809bb44; FAIL, two blocking findings on the gate card, none on the terms card. Recorded verbatim by the orchestrator, 2026-11-22. The header verdict is the latest round's.*

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
