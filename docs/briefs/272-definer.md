# Brief 272 — definer — S-002 and E-004 after the plan review's round 1 FAIL (P-002, M8 to M10)

session: session_01QBwHGNPKhVy6fgoUjKtW6q
model: the Definer runs in a fresh session; its change is checked by the Critic on a different model from it (D-056). Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@67010c1702f607c7cae45f68a3dd42e153f68c4f (branch build/definer/p002-plan-fix, in its own worktree /home/user/wt/ml-definer-272)
manifest: the worktree; the Critic's round 1, reviews/S-002/plan.md; governance/SURFACES.md
recorded: at hand-out, 2026-11-12

## Brief
The Critic's plan review of specs/S-002.md and experiments/E-004.md failed at round 1 with eight blocking findings (reviews/S-002/plan.md, round 1). Round 2 is the second of three allowed before the stop rule. In specs/S-002.md, experiments/E-004.md and, only if a fix needs it, experiments/E-004/line.py, and in no other file:
1. Fix blocking findings 1 to 8 as the Critic states them. Where a finding offers two fixes, choose one and say why. In particular:
   - Finding 5: keep rule T5 (gate and value-target rulings as touches) out of the count, J1 and the hand check until the owner rules S-002's open question 3, unless you can say exactly which pieces a ruling lands on from a field in the extract.
   - Finding 6: the draw must be fixed in the frozen trial record before any entry exists, and the Reviewer re-derives every draw.
   - Finding 7: name who decides a withdrawal. A decider that is neither the Chief of Staff nor any session that knows the arms is preferred (ruled T29). Cap withdrawals, and give a rule for a piece still unmerged after a set number of days.
   - Finding 8: put the trial logs and the count in a lane a named writer owns in governance/SURFACES.md (you may not edit SURFACES.md), or name the script and the role that commits them, and list it under "Needed outside this spec's lane".
2. Fix non-blocking findings 9 to 16 and the four rated leftovers in the same change, unless one conflicts with a blocking fix; then say so.
3. Change no figure. Where a sentence states a figure, check it against line-output.txt (LL-53). Before committing, check every changed sentence against the record it states, not only against the finding it answers (LL-55's correction).
Do not freeze either file; S-002 stays draft. Run Python as `python3 -I -B` (LL-84). Commit on your branch as `definer <definer@agents.invalid>` with the trailers `Agent-Session: session_01QBwHGNPKhVy6fgoUjKtW6q/definer-272` and `Spec: S-002`; do not push or merge. Run `governance/checks/check_all.sh . 67010c1702f607c7cae45f68a3dd42e153f68c4f` and `python3 -I -B governance/checks/surface_guard.py diff --range 67010c1702f607c7cae45f68a3dd42e153f68c4f..build/definer/p002-plan-fix --branch build/definer/p002-plan-fix`. Return the six-part contract with a table: finding number, the fix, the file and lines changed.
