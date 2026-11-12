# Ruling needed: a late fix to the trial plan failed its check after the plan had passed

Milestone: M9

A trial tests one method on new work. Each piece of work is handed out as an entry (one brief) and counts once it is merged as a pull request. A look is one round of 30 pieces done with the method and 30 without it; a second look may add 30 more each way. Each entry takes a numbered place, and each place's side, with or without, is fixed in advance by a shuffle. Under set conditions (you did not step in, and its work did not merge) a piece can be dropped ("withdrawn": left out, and its place refilled from one of three spare places each look holds, on the same side); a fourth drop in one look stops the trial and brings it to you.

The plan for these trials, and for counting your touches, passed its independent check (by the Critic, a reviewer that did not write it) at the third and last allowed round. The Critic then listed nine smaller points to tidy before the plan is frozen. One asked what happens when an entry and a pull request do not match one to one: for example, when two entries end up merged as one pull request. The writer of the plan's answer was to count such a pull request once, on the first piece's side, and to leave the second piece's place empty, with no limit. The Critic's check of that answer failed, on two points. First, an empty place leaves a side with fewer than 30 pieces, and the rule for whether the second look runs is written for 30 each way. Second, whoever hands out the work can see which side comes next, so merging two pieces into one pull request, or entering one piece twice, would let them empty a place they choose. The model's stop rule (its limit of three checks on a plan) sends a failure after the last allowed round to you, to choose from fixed options; accepting the change despite its failed check is not one of them. Nothing is frozen (fixed so it can no longer be changed) and no trial has started, so nothing here is irreversible. The late change left the counting rules alone, but it also changed one line of how the hand check (a check by hand of the counting rules on a sample of past pieces) draws its sample, and the notes its researcher is given; those go with the change under each option.

WHY: the plan cannot be frozen until this is settled; a trial is fair only if no one can choose which pieces drop out once the sides are known (reviews/S-002/plan.md, round 1 finding 7 and the re-check's finding 2).
OPTIONS:
  A. One focused confirmation review: a focused fix, then one check.
     The writer refills an emptied place from the same three spare places, on the same side. A doubled piece or a doubled entry counts toward the same limit of three a look as a dropped piece. The writer adds these routes to the plan's stated limits, and fixes the seven smaller points from the same check. One check by the Critic covers only the changed lines; if it fails, it comes back to you.
     Gain: every side stays at 30 while the limit of three is not passed, so the checked figures hold; there is no new route without a limit: at most three pieces a look can be dropped by any route, and the plan states that as a limit.
     Cost: one more change and one more check, which can itself fail (in the first project, a focused fix failed and was then redrafted, reviews/S-001/plan.md). Doubled pieces now share the limit of three with real drops, so a trial can stop sooner and come back to you, and each refill adds a wait while the spare piece is done.
     Undo: nothing is frozen until the check passes.
  B. Re-scope: take the late change back and carry its question to the scenario card.
     The late change is taken back, so the plan reads as it passed at round 3. This removes the failed change from the plan's scope; it does not accept it. The question of a piece and a pull request that do not match stays open, not settled: it is listed for your decision on the plan's scenario card (the card where you approve how the plan behaves), and settled before the plan is frozen.
     Gain: no more checks now; the plan as passed is unchanged, and the hand check can go ahead on it.
     Cost: until you rule it, the plan does not say what happens in those cases. The Critic called the effect "mostly conservative" at round 3, but its later check found that a merge can favour the method. A ruling on the card still needs a change and a check of its own.
     Undo: any choice can be written in later, before the plan is frozen.
  C. Re-specify the trial's entry rules as a new draft.
     The writer redrafts how pieces enter a trial and drop out, and the Critic reviews that part from round one, with three rounds again.
     Gain: a fresh look at the part of the plan that has needed fixing in every round.
     Cost: the most time and checking; the cards wait on it.
     Undo: the plan as passed is kept until the new draft passes.
  D. Drop the trial plan.
     The screening keeps its counting rules and sources but runs no fair trials.
     Gain: no more work on trial entry.
     Cost: methods could not be judged against your value target, which is set in trial terms; the project's purpose would need re-ruling.
     Undo: a trial plan can be drafted again later.
RECOMMENDATION: A, with moderate confidence (the Chief of Staff's judgement): it closes both points with a mechanism the plan already has and checks only what changed; the confidence is moderate because a focused fix failed once before in the first project. What would change it: wanting no more checks before the scenario card (then B), judging the entry rules unsound as a whole (then C), or the check failing again, which brings it back to you.
WHO HAS CHECKED IT: the Critic's plan review, rounds 1 to 3, and its re-check after round 3 (reviews/S-002/plan.md); this card, the Critic's cold read, round 2 (round 1 failed and the card was rewritten; reviews/P-002-plan-stop/critic.md). The recommendation is the Chief of Staff's and has no other check.
RISK CLASS: R0 (the lowest), a question only   REVERSIBILITY: reversible   BLAST RADIUS: the screening's trial plan before any freeze
DEFAULT: none, deliberately: a choice under the stop rule is the owner's own, never a default, as for the first project's plan stops; this departs from AGENTS.md section 5's rule that a reversible question takes its recommendation at timeout, because the stop rule makes the choice the owner's own   TIMEOUT: none

## Context
- The plan review failed at rounds 1 and 2 and passed at round 3, with nine non-blocking findings (source: reviews/S-002/plan.md)
- Round 3's finding 3 asked what happens when an entry and its pull requests do not match one to one, and called the effect "mostly conservative" (source: reviews/S-002/plan.md, round 3)
- The writer's fix counts such a pull request once on the first entry's side and leaves the later place empty, with no limit (source: docs/briefs/276-definer.md; experiments/E-004.md, Exclusions)
- The re-check failed on two blocking findings: an empty place leaves the second-look rule undefined, and merging or entering twice lets a session that knows the sides empty a place it chooses, which can favour the method (source: reviews/S-002/plan.md, "Re-check after round 3", findings 1 and 2)
- Each look holds three spare places, on the withdrawn piece's side, under a limit of three withdrawals a look (source: experiments/E-004.md, Exclusions)
- After S-001's round 3 pass, a failed later check went to the owner under the plan stop rule; the owner chose a focused fix, which failed, and then a redraft (source: reviews/S-001/plan.md; decisions/questions/P-001-plan-stop.md and P-001-plan-stop-2.md)
- A choice under the plan stop rule was recorded as "the owner's own choice, never a default" (source: decisions/questions/P-001-plan-stop.md)
- At the stop rule the owner chooses from fixed options: re-specify, re-scope, drop, or one focused confirmation review; accepting work despite a failed check is never an option (source: Personal-Org-Operating-Model OPERATING_MODEL.md §4 "Stop rule")
- The value target is set in trial terms (source: decisions/questions/P-002-value-target.md)
