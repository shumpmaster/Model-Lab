Ruling: option 1 — fix the holdouts check so a merge is judged by what it changes on the line it lands on
Question: none filed (put to the owner in conversation, 2026-11-09, at the first weekly landing; recorded here as an owner's ruling given in session)
Milestone: M4

Asked: 2026-11-09, in the Chief of Staff's session session_01QBwHGNPFytF6t2VG6mnugn, at the first weekly landing (brief 124). The landing merge of the work session's branch, which starts from main before pull request #69, read to `v3_checks holdouts` as changing governance/HOLDOUTS.md, because `--full-history` lists a merge that differs from any parent; the file is unchanged on main, and the same would recur every week. Options put: 1, fix the check; 2, let the work session bring main into its branch once, against brief 113, with one failing landing. Reversible: the check can be changed back.

## The owner's words, verbatim
"Option 1, fix the check"

## How it is carried out
- governance/checks/v3_checks.py, `check_holdouts`: `--full-history` becomes `--first-parent`, so each commit on the first-parent line is compared with its first parent; the comparison of the file at the base and at HEAD stays. Run on four cases: the week-1 landing passes; the #69 merge, recorded by L-0007, passes; a change with no ledger entry fails; the same change made on a side branch and merged fails.
- The check came with the operating model's template; the change is to this repository's copy, and is reported for the operating model's own copy when Model-Lab's results move there.
- A Reviewer checks it, and, the path being R3, the owner's verdict file is needed (governance/risk-paths.toml).
