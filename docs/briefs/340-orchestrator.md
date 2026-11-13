# Brief 340 — orchestrator — #49's two codes under the owner's ruling, and the research question re-quoted at the passed plan (P-002, M8)

session: session_01QBwHGLKYvyVZk199qdegcJ
model: a fresh helper working the Orchestrator's lane (research/**), apart from the helpers of briefs 323 and 332. Model names are kept out of this record by this session's standing instructions (LL-70).
start: the commit that merges brief 341's Definer change into orch/p002-fix-5, named in the dispatch (branch orch/q018-codes-6, in its own worktree /home/user/wt/ml-orch-340, made from that commit), so the re-quote holds the plan's last wording
manifest: the worktree; specs/S-002.md (step 3, *Later work*; step 4; line 46); decisions/questions/P-002-plan-written-by-piece.md (the owner's ruling); reviews/Q-018-later-work/ (the three verbatim records, _critic-reread-verbatim.md last); reviews/S-002/plan.md, section "Focused confirmation review, at the second plan stop" (finding 5); research/Q-018-extract/ (README.md, later_work.py, sample.jsonl); research/Q-018.md; docs/briefs/332-orchestrator.md
recorded: at hand-out, 2026-11-13

## Brief
In research/** only, with brief 294's limits (never `draw`; sample.json byte-identical; the owner's address never written):
1. Set `later_work` for rows 60 and 61 (Personal-Org-Operating-Model #49, de17627b at 568cd6e0 and 0e57b841) to "this piece", under decisions/questions/P-002-plan-written-by-piece.md, as the re-read (_critic-reread-verbatim.md) confirms; keep both Critics' readings on each entry and add the re-read's. Do it in later_work.py, so a re-run gives the same file. Show that only those two entries change.
2. README.md: say why the two codes changed, by label and commit only, no text.
3. research/Q-018.md re-quotes S-002's lines as step 4 gives them, at this brief's start commit (the plan as its focused confirmation review passed it, with brief 341's wording fixes; line 46 changed since brief 332's quote), and adds to the pointer notes the three pointers the review's finding 5 names (J2, step 6 (v), E-004's "Exclusions" and "The sides are known ahead"). Change nothing else in the question.
Run Python as `python3 -I -B` (LL-84). Commit as `orchestrator <orchestrator@agents.invalid>` with the trailer `Agent-Session: session_01QBwHGLKYvyVZk199qdegcJ/orchestrator-340` in its own paragraph; do not push or merge. Run `governance/checks/check_all.sh . <the commit that adds this brief>` (`record_checks merges` may be red, LL-29: say so if it is) and `python3 -I -B governance/checks/surface_guard.py diff --range <that commit>..orch/q018-codes-6 --branch orch/q018-codes-6`. Return the six-part contract with the comparison.
