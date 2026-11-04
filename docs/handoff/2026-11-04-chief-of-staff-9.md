# Handoff — the prompt engine (P-001), 4 November 2026, ninth stopping point

*Written by the Chief of Staff (session_01QBwHGJ9ZMyT9fK17HjfmCc). It follows docs/handoff/2026-11-04-chief-of-staff-8.md.*

## Where it stands
- **Build has begun.** The owner's Build-gate answers are recorded (PR #50: decisions/questions/P-001-build-gate.md and P-001-build-gate-terms.md, ledger L-0006, no hand-written status record by the gate-record ruling). The stop-rule answer is PR #48; the last session's records are PR #49. All three were green and waiting on the owner's merge when this was written.
- **The terms are carried out**, on branch cos/p001-build-terms (its pull request opened from this session, after #50 since it starts from #50's branch):
  - V1, M2's "done when" and the other past-task and run-count lines of docs/PROJECT.md reworded to the plan's texts; the Critic passed them at round 2 (reviews/P-001-build-terms/critic.md).
  - Brief records gain a `start:` field (docs/briefs/README.md); every brief from 66 on carries it.
  - The Definer settled the plan's open questions as ruled and froze S-001 and E-003 at f4298cd; the Critic's check of the settled text failed once on four stale line pointers (LL-58), which were fixed before the freeze landed, and passed at round 2 (reviews/S-001/_critic-settled.md).
  - The Check author wrote S-001's locked checks (tests/acceptance/, AC1 to AC11 and join tests J1 to J8); the Critic passed them at round 3 (reviews/S-001/_critic-checks.md), which is Build-1's record. 43 tests pass today; 183 wait for the Builder's scripts under src/E-003/ (docs/reports/2026-11-04-s001-locked-checks-return.md names every interface).
- **The private sheets repository** shumpmaster/secret-marking exists (intake/P-001-environment-2026-11-04.md). This session never attached it. The owner's set-up for it is below.

## Next, in order
1. Check the live state of #48, #49, #50 and the terms pull request (LL-11); after each merge, check main's questions/ (LL-30).
2. **The owner's set-up** (S-001, "Needed outside"; K1): in shumpmaster/secret-marking, one file only, `README.md`, holding one harmless word the owner chooses and tells no session yet (the `holdouts/` and `verdicts/` folders are added by the sheet lead when it writes the first sheet); then, in the cloud environment's settings (the environment menu in a session's title bar, then Edit, Repositories), confirm secret-marking is not listed, so no new session gets it by default.
3. **Build-2:** brief the Builder (claude-opus-5-5; the Check author ran on claude-sonnet-5-5) for the harness scripts under src/E-003/, to the interfaces the locked checks name (tests/acceptance/e003_support.py's docstring). Tell it: analyse.py is a deliverable the checks add, a mechanical reference and not the Reviewer's result; a Bash redirect target counts as a file the run creates (the strict F4 reading the checks pin); and two non-blocking notes from the Critic's round 3 stand on the locked checks (the J7 and J8 tests share one manifest variable, so run those two files one at a time when it is set; one docstring's wording), which a locked check cannot be edited for: they need a superseding change if they are to change.
4. Then the first kind (built work): the owner starts the three sessions the plan names, and the K1 probe runs before any sheet is written.

## Token checkpoint
This session, by its own status at the stopping point: about 376,000 tokens of context in use and about $26.52 estimated cost. Helpers this session, as reported (resumed helpers' increases only, LL-34): the Critic on the reworded lines 42,563 and 20,690; the Definer 211,572 and 13,472; the Critic on the settled plan 154,762 and 133,127; the Check author 282,603, 23,019 and 10,831; the Critic on the locked checks 191,051, 99,595 and 80,169; in all 1,263,454. No test runs have been used: the fair test's 732 runs start with the first kind.
