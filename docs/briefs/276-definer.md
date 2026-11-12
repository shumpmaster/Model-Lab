# Brief 276 — definer — S-002 and E-004: the plan review's round 3 non-blocking findings (P-002, M8 to M10)

session: session_01QBwHGNPKhVy6fgoUjKtW6q
model: the Definer runs in a fresh session; its change is checked by the Critic on a different model from it (D-056). Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@c418de4455d6c71a089c9dc2b526f0e59ce1ea64 (branch build/definer/p002-plan-fix-3, in its own worktree /home/user/wt/ml-definer-276)
manifest: the worktree; the Critic's round 3, reviews/S-002/plan.md; governance/SURFACES.md
recorded: at hand-out, 2026-11-12

## Brief
The plan review passed at round 3 with nine non-blocking findings (reviews/S-002/plan.md, round 3). In specs/S-002.md and experiments/E-004.md only:
1. Fix findings 1 to 8 as the Critic states them. Keep changes to S-002's rules (lines 18 to 54) and the edge-case table (lines 76 to 95) to the fewest needed, and list every changed rule and case id, because the Critic re-checks those cases only (round 3, finding 9). For finding 3, choose for each case whether it is left out and listed, or counted once on the first entry's side, and say why; mark the choice "this plan's design" for the owner's scenario card. For finding 8, pick the number of days and mark it "this plan's figure", for the owner's card.
2. Leave finding 9's placeholders for the freeze. Do not freeze either file. Change no figure from line-output.txt.
3. Check every changed sentence against the record it states (LL-55), and re-read the entry, withdrawal and count rules end to end for any sentence the change makes false.
Run Python as `python3 -I -B` (LL-84). Commit as `definer <definer@agents.invalid>` with the trailers `Agent-Session: session_01QBwHGNPKhVy6fgoUjKtW6q/definer-276` and `Spec: S-002` in one paragraph; do not push or merge. Run `governance/checks/check_all.sh . c418de4455d6c71a089c9dc2b526f0e59ce1ea64` and `python3 -I -B governance/checks/surface_guard.py diff --range c418de4455d6c71a089c9dc2b526f0e59ce1ea64..build/definer/p002-plan-fix-3 --branch build/definer/p002-plan-fix-3`. Return the six-part contract with a table: finding number, the fix, the file and lines changed, and the rule and case ids changed.
