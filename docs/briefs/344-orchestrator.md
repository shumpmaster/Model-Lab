# Brief 344 — orchestrator — the research question re-quotes S-002 :46 as brief 342 left it; one stale README line (P-002, M8)

session: session_01QBwHGLKYvyVZk199qdegcJ
model: a fresh helper working the Orchestrator's lane (research/**), apart from the helpers of briefs 323, 332 and 340. Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@1dbff9d9dd15b1d341ec0d537684849dfa8a3073 (branch orch/q018-quote-7, in its own worktree /home/user/wt/ml-orch-344, made from the commit that adds this brief)
manifest: the worktree; specs/S-002.md (step 4; line 46); research/Q-018.md; research/Q-018-extract/README.md; docs/briefs/340-orchestrator.md
recorded: at hand-out, 2026-11-13

## Brief
In research/** only:
1. research/Q-018.md re-quotes S-002's lines as step 4 gives them, at this brief's start commit (the plan as brief 343's check passed it; line 46 lost its hand-check results in brief 342), with its heading's commit updated. Show by script that the quoted rules and the edge-case table are verbatim against S-002 at this commit, less Q-017's three parentheses. Change nothing else in the question.
2. research/Q-018-extract/README.md: the sentence at about line 67 that says step 3's `later_work` is not yet in the extract, brought up to date (it is, since brief 332).
Run Python as `python3 -I -B` (LL-84). Commit as `orchestrator <orchestrator@agents.invalid>` with the trailer `Agent-Session: session_01QBwHGLKYvyVZk199qdegcJ/orchestrator-344` in its own paragraph; do not push or merge. Run `governance/checks/check_all.sh . <the commit that adds this brief>` (`record_checks merges` may be red, LL-29; `review_check lint` is red on main from reviews/87/owner.md, outside this lane: say so) and `python3 -I -B governance/checks/surface_guard.py diff --range <that commit>..orch/q018-quote-7 --branch orch/q018-quote-7`. Return the six-part contract.
