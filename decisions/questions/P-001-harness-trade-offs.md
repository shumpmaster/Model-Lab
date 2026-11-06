Ruling: A and C — keep the leak check's stricter readings, and record the routes it misses as known limits; the harness is unchanged
Question: questions/P-001-harness-trade-offs.md
Milestone: M4, Build-3

Asked: 2026-11-06, in the Chief of Staff's session session_01QBwHGKmmzB2PF2wo11LAAC, by the session's question tool, from questions/P-001-harness-trade-offs.md (filed in PR #63; Critic: reviews/P-001-harness-trade-offs/critic.md, PASS at round 3). No default. Reversible for the choice, not for pairs already lost.

## The owner's words, verbatim
On part 1, the stricter readings, the owner chose: "A: Keep them (Recommended)".
On part 2, the routes it misses, the owner chose: "C: Record as limits (Recommended)".

## How it is carried out
- Nothing in src/E-003/** or tests/** changes; no further build round.
- Each kind's result lists the stricter readings and the missed routes as known limits of the check, from intake/P-001-harness-trade-offs-runs-2026-11-06.md sections 1 to 3 and the Reviewer's list (reviews/S-001/_reviewer-build.md, round 2 open question a, round 3 findings 1 to 3).
- Every brief record of a plan or built piece keeps `recorded: at hand-out, <date>`, the form the harness reads (src/E-003/pair.py:122).
- The fair test's set-up before built work goes on with the harness at the default branch's commit.
