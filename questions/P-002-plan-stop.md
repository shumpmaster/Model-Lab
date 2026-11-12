# Ruling needed: a late fix to the trial plan failed its check after the plan had passed

Milestone: M9

The plan for counting your touches and for the fixed trial passed its independent check at the third and last allowed round. The Critic then listed nine smaller points to tidy before the plan is frozen. One of them asked what happens when a trial piece and a pull request do not match one to one: for example, when two pieces handed out for a trial end up merged as one pull request. The writer's answer was to count such a pull request once, on the first piece's side, and to leave the second piece's place empty. The Critic's check of that answer failed, on two points. First, an empty place leaves a side with fewer than 30 pieces, and the rule for whether the second look runs is written for 30 each way. Second, whoever hands out the work can see which side comes next, so merging two pieces, or entering one piece twice, would let them empty a place they choose, with no limit. The model's stop rule sends a failure after the last allowed round to you. Nothing is frozen and no trial has started, so nothing here is irreversible.

WHY: the plan cannot be frozen, and the hand check of the counting rules uses the rules as the passed plan states them; the trial's fairness rests on no one being able to choose which pieces drop out after the sides are known (docs/projects/P-002.md, section 6).
OPTIONS:
  A. One focused fix, then one check.
     The writer refills an emptied place from the three spare places a trial already holds for dropped pieces, on the same side. A doubled piece or a doubled entry then counts toward the same limit of three as a dropped piece, and a fourth stops the trial and brings it to you. The writer also adds these routes to the plan's stated limits and fixes the seven smaller points from the same check. One check by the Critic covers only the changed lines; if it fails, it comes back to you.
     Gain: every side stays at 30, so the checked figures hold, and no new route lets a piece be dropped by choice.
     Cost: one more change and one more check, which can itself fail.
     Undo: nothing is frozen until the check passes.
  B. Undo the late fix and keep the plan as it passed.
     The late change is taken back, so the plan reads as it passed at round 3. The question of a piece and a pull request that do not match stays open, listed as a known risk for your decision on the plan's scenario card (the card where you approve how the plan behaves).
     Gain: no more checks now; the plan as passed is unchanged.
     Cost: the plan does not say what happens in those cases, so the Reviewer would decide them when judging a trial, after the sides are known. The Critic judged that mostly harmless at round 3, but not settled.
     Undo: the fix can be made later, before the plan is frozen, with a check of its own.
  C. Re-specify the trial's entry rules as a new draft.
     The writer redrafts how pieces enter a trial and how they drop out, and the Critic reviews that part from round one, with three rounds again.
     Gain: a fresh look at the part of the plan that has needed fixing in every round.
     Cost: the most time and checking; the hand check and the cards wait on it.
     Undo: the plan as passed is kept until the new draft passes.
RECOMMENDATION: A, with moderate confidence (the Chief of Staff's judgement): it closes both points with a mechanism the plan already has and checks only what changed. What would change it: wanting no more checks before the scenario card (then B), or judging the entry rules unsound as a whole (then C).
WHO HAS CHECKED IT: the Critic's plan review, rounds 1 to 3, and its re-check after round 3 (reviews/S-002/plan.md).
RISK CLASS: R0, a question only   REVERSIBILITY: reversible   BLAST RADIUS: the screening's trial plan and its counting rules, before any freeze
DEFAULT: none, deliberately: the stop rule leaves the next step to you   TIMEOUT: none

## Context
- The plan review failed at rounds 1 and 2 and passed at round 3, with nine non-blocking findings (source: reviews/S-002/plan.md)
- Round 3's finding 3 asked what happens when an entry and its pull requests do not match one to one (source: reviews/S-002/plan.md, round 3)
- The writer's fix counts such a pull request once on the first entry's side and leaves the later place empty, with no limit (source: docs/briefs/276-definer.md; experiments/E-004.md, Exclusions)
- The re-check failed on two blocking findings: an empty place leaves the second-look rule undefined, and merging or entering twice lets a session that knows the sides empty a place it chooses (source: reviews/S-002/plan.md, "Re-check after round 3", findings 1 and 2)
- A trial already holds three spare places, on the withdrawn piece's side, under a limit of three withdrawals a look (source: experiments/E-004.md, Exclusions)
- After S-001's round 3 pass, a failed later check went to the owner under the plan stop rule (source: reviews/S-001/plan.md; decisions/questions/P-001-plan-stop.md)
- At the stop rule the owner chooses from fixed options: re-specify, re-scope, drop, or one focused confirmation review; accepting work despite a failed check is never an option (source: Personal-Org-Operating-Model OPERATING_MODEL.md §4 "Stop rule")
