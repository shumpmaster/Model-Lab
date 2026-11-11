# Brief 263 — definer — E-004's statement of the line at two looks, after the Reviewer's run

session: session_01QBwHGN6YeYid8ERiP8HY5Z
model: the Definer runs in a fresh session; its Reviewer runs on a different model from it (D-056). Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@c158b8e14b71c5f7cf7c56f5164e085cb821ab84 (branch build/definer/p002-two-look-wording, in its own worktree /home/user/wt/ml-definer-263)
manifest: the worktree; the Reviewer's return, reviews/P-002-two-look-line/reviewer.md, round 1
recorded: at hand-out, 2026-11-11

## Brief
The Reviewer reproduced every figure of both versions of the line at two looks and failed one sentence (reviews/P-002-two-look-line/reviewer.md, round 1). In experiments/E-004.md and specs/S-002.md only, and in no other file:
1. Finding 1 (blocking): state version (a)'s excess over 1 in 10 as the two bands it is, about 0.31 to 0.43 and about 0.57 to 0.69, with 0.0933 at 1 in 2 below 1 in 10. Reword line.py's print line the same way and re-record line-output.txt by running it; change no figure or computation.
2. Finding 2: name each worst case with its mirror share.
3. Finding 3: add the chance of a second look under each version, for a method that does nothing and for a true halving, from line-output.txt.
4. Finding 4: state assumptions A1, A3, A5 and A6 in plain words in E-004, where it gives the figures.
5. Finding 5: give version (a)'s range of lines that decide the same (0.09616 up to, not including, 0.09725), as for (b), after checking it with line.py or your own sum; fix line.py's header run time.
Recommend neither line. Check each changed sentence against line-output.txt (LL-53). Commit on your branch as `definer <definer@agents.invalid>` with trailers `Agent-Session: session_01QBwHGN6YeYid8ERiP8HY5Z/definer-263` and `Spec: S-002`; do not push or merge. Run `governance/checks/check_all.sh . c158b8e14b71c5f7cf7c56f5164e085cb821ab84` and the surface guard's diff for your range. Return the six-part contract, quoting each changed passage old and new.
