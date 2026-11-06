# Intake — P-001: the surface guard run on each way the harness could land, 2026-11-05

*Recorded by the Chief of Staff (session_01QBwHGNGKXFwvVVdzkei5aT) from runs on scratch clones of Model-Lab, none pushed. The base is the default branch at 0148e34 (pull request #57 merged). The command each time is `python3 governance/checks/surface_guard.py diff --range <base>..HEAD`.*

## Landing the Builder's three commits (3861b38, a42c2df, 9caff21) as they are
- With a merge commit onto the base: `spec S-001: session session_01QBwHGNGKXFwvVVdzkei5aT wrote both checks (check-author) and code (builder)` · `FAIL: 1 violation(s)`.

## Option B: the three commits listed in governance/SURFACES.md's exempt block (a stand-in ledger id, for the run only)
- The landing range: `OK: 5 commit(s) … checked (1 merge(s) skipped, 3 exempt, 0 human)`.
- Then one more commit by `builder`, `Spec: S-001`, from a different session id (`session_other`), its range alone: `spec S-001: session session_01QBwHGNGKXFwvVVdzkei5aT wrote both checks (check-author) and code (builder)` · `FAIL: 1 violation(s)`. The exempt commits are still in the history the check reads.

## Option A: the three commits made again with `Agent-Session: session_01QBwHGNGKXFwvVVdzkei5aT/builder-90`, the same author, message otherwise unchanged
- `git diff --quiet 9caff21 HEAD`: the tree is the same as the reviewed 9caff21.
- The landing range: `OK: 4 commit(s) … checked (1 merge(s) skipped, 0 exempt, 0 human)`.
- Then one more `builder` commit with `Spec: S-001` from `session_other`, its range alone: `OK: 1 commit(s) … checked`.
- The full governance check on the landing (`bash governance/checks/check_all.sh . 0148e34`): every step passes but `record_checks merges`, which fails locally on any orchestrator merge commit without an `Item:` trailer (docs/LESSONS.md LL-29; CI passed it on pull request #57's merge).
