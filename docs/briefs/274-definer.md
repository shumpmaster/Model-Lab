# Brief 274 — definer — S-002 and E-004 after the plan review's round 2 FAIL (P-002, M8 to M10)

session: session_01QBwHGNPKhVy6fgoUjKtW6q
model: the Definer runs in a fresh session; its change is checked by the Critic on a different model from it (D-056). Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@4617eb3a614215b73de8ca2481143fe61f7b183e (branch build/definer/p002-plan-fix-2, in its own worktree /home/user/wt/ml-definer-274)
manifest: the worktree; the Critic's rounds 1 and 2, reviews/S-002/plan.md; governance/SURFACES.md; governance/PACKS.toml
recorded: at hand-out, 2026-11-12

## Brief
The plan review failed at round 2 with two blocking findings (reviews/S-002/plan.md, round 2). Round 3 is the last of three before the stop rule sends the plan to the owner, so make this change complete and check it end to end. In specs/S-002.md and experiments/E-004.md only:
1. Fix blocking findings 1 (withdrawal condition (ii) against the 60-day rule) and 2 (reserve places' sides) as the Critic states them. For finding 2, a reserve place takes the withdrawn piece's side, which is not in the trial record; give the Reviewer's check for it and reword J2, AC8 and the wait bound to match.
2. Fix non-blocking findings 3 to 11 in the same change, as the Critic states them. For finding 3, fix the seed as a string written in the spec and state the cut-off rule, so the Orchestrator chooses neither. For finding 8, the Reviewer reports each look's result with and without late touch-log lines, and the results card states both. For finding 7, list the withdrawal check's own pack under "Needed outside this spec's lane" (you may not edit PACKS.toml). Finding 12 stays for the freeze. For the sides fixed ahead, word the limit as the Critic's round 2 open point says, in E-004, S-002's risks and the plain-words section, and drop the "none is skipped or chosen" overclaim.
3. Change no figure. Check every changed sentence against the record it states (LL-55), and re-read the withdrawal, reserve and wait rules end to end across both files for any sentence that still contradicts them.
Do not freeze either file. Run Python as `python3 -I -B` (LL-84). Commit as `definer <definer@agents.invalid>` with the trailers `Agent-Session: session_01QBwHGNPKhVy6fgoUjKtW6q/definer-274` and `Spec: S-002` in one paragraph; do not push or merge. Run `governance/checks/check_all.sh . 4617eb3a614215b73de8ca2481143fe61f7b183e` and `python3 -I -B governance/checks/surface_guard.py diff --range 4617eb3a614215b73de8ca2481143fe61f7b183e..build/definer/p002-plan-fix-2 --branch build/definer/p002-plan-fix-2`. Return the six-part contract with a table: finding number, the fix, the file and lines changed.
