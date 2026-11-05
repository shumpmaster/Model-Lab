# Ruling needed: how the fair test's locked checks go on after their reviews kept failing

Milestone: Build-1

The checks that must exist before any of the fair test is built have failed their independent reviews again, so Build has not moved. Everything else in them holds; one part does not. Two of the checks read one shared setting that names a recorded list of files, and guess from the list's contents which of them it belongs to. Every version of that guess has let some faulty list be skipped, and a skip reads as a pass. The worst case is a list that would let the secret check's writer see the test's registration, which names the changes being tested. An independent trace found the fix both reviewers proposed would still miss that case, and that giving each check its own setting closes every case. No rule says how many rounds checks get; this stop is applied as for plans and built work. Every option here can be undone.

WHY: the checks cannot be used until both reviewers pass them, and accepting them despite a failed check is never an option; how they go on is yours to choose (Personal-Org-Operating-Model OPERATING_MODEL.md §4 "Stop rule"; docs/LEDGER.md has no grant).
OPTIONS:
  A. One focused round — the Check author gives each of the two checks its own setting, so each checks the list it is named for whatever that list holds, and fixes the trace's open small points; one review then runs every row of the trace's table of cases, and a failure comes back to you (triage/P-001-S-001-checks-round-5.md, case table and summary). Gain: the least change; the trace finds it closes every case without changing the frozen plan. Cost: one more round, of new code. Rules out: nothing.
  B. Re-specify — the plan's two joins are revised to say how each check is told which list it checks; since the plan is frozen, that is a new spec extending it, with its own plan review, then the checks are rewritten once (AGENTS.md §1: "Changing a frozen spec needs a superseding entry"). Gain: the gap the trace found in the plan is closed in the plan itself. Cost: a plan review and a rewrite before Build moves, how long not estimated. Rules out: nothing.
  C. Re-scope — the two checks stop testing named lists, and the person who builds the secret check's folder checks each list by hand. Gain: no more rounds on this part. Cost: a weaker gate on the one leak the secret side exists to stop. Rules out: a machine check of those lists.
  Dropping the test (the stop rule's fourth route) would end the project's fair test; it is not recommended and stays open to you.
RECOMMENDATION: A, with medium confidence (the Chief of Staff's judgement, following the trace): the trace finds the cause confined to these two checks and names a design that meets every case, without touching the frozen plan. What would change it: wanting the plan itself to say how a check is told its list (then B), or wanting no further rounds on this part (then C).
WHO HAS CHECKED IT: the Critic, on a different AI model from the writer (record: reviews/P-001-checks-stop/critic.md).
RISK CLASS: R0 (questions/**)   REVERSIBILITY: reversible   BLAST RADIUS: the fair test's locked checks and when Build moves; no option changes the frozen plan's criteria except B, through a new spec
DEFAULT: none (the stop rule requires the owner's own choice); until you choose, Build does not move   TIMEOUT: none

## Context
- The locked checks failed the Critic at rounds 1, 2, 4 and 5 and passed at round 3, and failed the required Reviewer at rounds 1 and 3 and passed at round 2; rounds 5 and 3 fail on the same finding (source: reviews/S-001/_critic-checks.md and reviews/51/reviewer.md, on pull request #51's branch)
- Triage traced the root cause to the two checks sharing one setting, found the reviewers' proposed fix leaves the worst case open, and gave a case table and the four routes (source: triage/P-001-S-001-checks-round-5.md, on pull request #51's branch)
- No rule counts check rounds or restarts their count (source: docs/LESSONS.md LL-55; LL-61 on pull request #51's branch)
- The owner's last stop ruling asked for cards cut down to the decisions (source: decisions/questions/P-001-build-gate-stop.md)
- The model's stop rule offers re-specify, re-scope, drop or one focused confirmation review (source: Personal-Org-Operating-Model OPERATING_MODEL.md §4 "Stop rule")
