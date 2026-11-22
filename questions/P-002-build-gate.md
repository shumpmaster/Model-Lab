# Ruling needed: move the screening into Build, approving its plan's scenarios?

Milestone: Design-6

The plan failed its review four times before it passed. Each failure was fixed, and after two of them you chose a focused fix at a plan stop. It now stands passed: its last changes passed their check, and its parts fit together. Nothing was skipped. Tried by hand on past work, its counting rules found that 14 of 33 past pieces needed at least one touch from you, meaning a time you stepped in before the work merged. Proceeding approves the plan's twenty-one scenarios as written. That includes the parts that are the plan's own design rather than your earlier rulings, the limits it says it cannot catch, and the milestone lines for Build and Launch. Some of those limits bear on your target: trial counts run a little high, against a pass, and the session that logs what you say in conversation knows which pieces carry the method. The plan then freezes, once the terms card beside this one is answered and your answers are written in and checked. No trial starts until the conditions you already set are met. Once frozen, the plan can change only through a new plan. Killing the project could not be undone.

Words used: a trial's two *sides* are the pieces given the method and the pieces without it; a *look* is a planned point at which a trial is judged, after 30 pieces each way, with one planned second look; the *desk* is the Service Desk, where you answer cards.

WHY: nothing goes past a gate until you rule. At the Build gate you approve the criteria by scenario, and they then freeze (Personal-Org-Operating-Model OPERATING_MODEL.md §4 "Phase gates"; specs/S-002.md, "Acceptance criteria").
OPTIONS:
  The model fixes a gate's four rulings: proceed, hold, recycle or kill.
  A. Proceed: approve AC1 to AC21 as specs/S-002.md gives them ("Acceptance criteria"), and take on the standard lines Build-1 to Build-5 and Launch-1 to Launch-5 (docs/projects/P-002.md, section 3). Beyond your earlier rulings, this approval carries:
     (i) the plan's own design for confirming each look's touches (AC9; J9; "In plain words"):
       - the list is shown to you without the sides, and you may strike a line;
       - you see every logged touch on the look's pieces, and at look 2 all 120 pieces;
       - the desk keeps your answer, as a record you make yourself, and the list and the log are checked against it;
       - a touch counts only if a list you confirmed holds it or you added it;
       - for a withdrawn piece's touch, and for an unmerged piece whose every touch you strike, the result is also worked out the other way; if the two differ, the trial comes to you, and a look 1 that would have gone on stops there;
       - there is no time limit on your confirmation, so the look, and new pieces of its kind, wait for you.
     (ii) the desk's record of your answer is a condition before any trial (AC12; experiments/E-004.md, Step 0). It is Service Desk work, filed there for you to approve.
     (iii) the limits the plan states it cannot catch (specs/S-002.md, "Risks and mitigations"; experiments/E-004.md, "What this trial cannot catch"):
       - on a trial piece every question and note of yours counts, even one asking for later work, so both sides' counts run a little high, and a little high against the starting count, leaning toward a miss of your target rather than a pass;
       - the Chief of Staff keeps the log of your conversation touches and knows the sides, so it decides whether such a touch is logged and which piece it goes on; your confirmation guards this only in part;
       - the trial is not blind: the agents doing the work know the side, and only your short reads are unlabelled (as you ruled);
       - work folded into another brief's pull request is only listed, and work folded into work with no brief, all begun after the entry, is not listed at all;
       - a session that knows the sides can hold a look unjudged, though no result changes;
       - a touch you too do not recall, or one you confirm on the wrong piece, is missed;
       - the sides are known in advance to whoever hands out the work; the terms card asks you to accept this limit.
     (iv) the join-up review's four non-blocking differences, carried as risks (reviews/S-002/plan.md, round 3, "Join-up review").
     Gain: Build starts. The Check author writes the locked checks, then the Builder builds the count and the draw. Cost: no trial runs until the plan is frozen, the starting count of 60 pieces is on record, the ceilings are set (done at the Design gate) and the desk's record is in place. Rules out: changing a scenario without a new plan.
  B. Hold: say what to change in the case or the plan, and it comes back to you. Nothing moves meanwhile.
  C. Recycle into Design: name what to redo and why, and Design runs again.
  D. Kill: the project closes. The prompt engine is not affected.
RECOMMENDATION: A, with medium confidence (the Chief of Staff's judgement). The plan passed its review, its last changes passed their check and the join-up review found no blocking difference. The hand check shows the rules can be applied to the records, with what they cannot catch on record. What would change it: wanting the confirmation made simpler before any trial runs (then B, naming what), or finding the stated limits too wide to trust a trial's result (then C).
WHO HAS CHECKED IT: the Critic, on a different AI model from the writer, checked the plan, the join-up review and the plan's last changes (reviews/S-002/plan.md). It also gives its own independent view of the case beside this card (reviews/P-002/_build-gate-1-critic.md) and checks this card: round 1 failed, on this opening and on limits missing from (iii) (reviews/P-002-build-gate/critic.md).
RISK CLASS: R0 (questions/**; a phase gate, which only you rule)   REVERSIBILITY: irreversible   BLAST RADIUS: the screening's next phase. Option D closes the project, which is why this card is marked irreversible
DEFAULT: none (irreversible; a phase gate is never ruled by default or by proxy)   TIMEOUT: none

## Context
- The case for going on, with the gate Critic's independent view of it (source: docs/gates/P-002/build-gate-1-case.md; reviews/P-002/_build-gate-1-critic.md)
- The plan failed its review at rounds 1 and 2, at the re-check after round 3 and at the re-run before the freeze; the owner chose a focused fix at each of the two plan stops; it passed at round 3 and at both focused reviews, and the check of its last changes passed (source: reviews/S-002/plan.md, header and each round; decisions/questions/P-002-plan-stop.md; decisions/questions/P-002-plan-stop-2.md)
- The join-up review closing Design found no blocking difference and carried four non-blocking ones as risks (source: reviews/S-002/plan.md, round 3, "Join-up review")
- The hand check: 14 of 33 pieces had at least one touch, 11 of 26 in the random part (source: research/Q-018-memo-5.md:137, :138)
- The plan names the parts of its design that are yours to approve at this gate, and the limits it states (source: specs/S-002.md, "In plain words", "Risks and mitigations"; experiments/E-004.md, "What this trial cannot catch")
- A trial waits on the plan's freeze, the starting count, the ceilings and the desk's record of your answer (source: specs/S-002.md, AC12; experiments/E-004.md, Step 0)
- The ceilings were set at the Design gate: your existing AI plan, and no cap on your time (source: decisions/questions/P-002-design-gate.md, Parts 2 and 3)
- Build's and Launch's standard lines were written for this gate (source: docs/projects/P-002.md, section 3)
