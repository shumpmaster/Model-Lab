# Brief 269 — definer — the owner's line at two looks written into the plan

session: session_01QBwHGJm2otqFdQxgZQ1fyx
model: the Definer runs in a fresh session; the change is checked by a Reviewer on a different model from it (D-056). Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@6295a868c81bdbd2c9f95468b00b8ee1381f33c7 (branch build/definer/p002-line-chosen, in its own worktree /home/user/wt/ml-definer-269)
manifest: the worktree; the owner's ruling, decisions/questions/P-002-two-look-line.md
recorded: at hand-out, 2026-11-12

## Brief
The owner ruled A, "A: line of 0.097" (decisions/questions/P-002-two-look-line.md). In experiments/E-004.md and specs/S-002.md only, and in no other file:
1. E-004.md, "Deciding threshold": fill the `line:` field as `line: 0.097`, citing the ruling record; keep both versions' figures as they stand, marking (a) as the one ruled and (b) as the one not chosen. Change no figure.
2. S-002.md: where the plan says the line is the owner's choice still to come (the "In plain words" paragraph, "This plan does not choose", and open question 1, "The line at two looks (P18)"), say instead that the owner chose 0.097 on 2026-11-11, citing the ruling; mark open question 1 answered, and keep its number. Keep the figures the owner chose on.
3. As the ruling's "How it is carried out" says: the trial record copies the line, not a starting share; and the results card states the line and, where the counted starting share falls in one of (a)'s two bands (about 0.31 to 0.43 and about 0.57 to 0.69), says a method that does nothing would pass a little more than 1 in 10 of the time there. Put each where E-004 or S-002 already says what the trial record and results card carry.
Do not freeze either file; S-002 stays draft. Check each changed sentence against line-output.txt and the ruling (LL-53). Run Python as `python3 -I -B` (LL-84). Commit on your branch as `definer <definer@agents.invalid>` with trailers `Agent-Session: session_01QBwHGJm2otqFdQxgZQ1fyx/definer-269` and `Spec: S-002`; do not push or merge. Run `governance/checks/check_all.sh . 6295a868c81bdbd2c9f95468b00b8ee1381f33c7` and `python3 -I -B governance/checks/surface_guard.py diff --range 6295a868c81bdbd2c9f95468b00b8ee1381f33c7..build/definer/p002-line-chosen --branch build/definer/p002-line-chosen`. Return the six-part contract, quoting each changed passage old and new.

## Addendum, after the Definer's first return (2026-11-12)
The Definer's open questions name passages that still read as if the line were undecided. In the same two files, on the same branch, in a second commit with the same trailers: E-004 line 10 ("One choice is left to the owner ..."), say the owner chose 0.097, citing the ruling; S-002's M9 paragraph "The line at two looks (P18)", say the owner ruled 0.097 on its card after the independent run passed; S-002's AC9, name 0.097 as the line the owner ruled (S-002 is a draft, so no superseding entry is needed); S-002's "Needed outside this spec's lane", mark the card on the line done. Leave E-004 line 3 and S-002's "Facts relied on" bullet as they are. Change no figure. Re-run both checks and return the six-part contract, quoting each passage old and new.
