# Brief 103 — builder — re-sign Build-2's three commits, on the owner's ruling A

session: session_01QBwHGNGKXFwvVVdzkei5aT
model: claude-opus-5-5 (the work's checks were written by the Check author on claude-sonnet-5-5; the Reviewer that confirms this runs on claude-fable-5-1; D-056). The same Builder session as briefs 90, 92 and 97, resumed. No new build round: the content does not change.
start: Model-Lab@ed35668f0e204698fcb8d15e3176a937ba1d73dc (a new branch build/builder/e003-harness-signed, in the Builder's worktree /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/wt-builder; the commits to remake are 3861b38, a42c2df and 9caff21 on build/builder/e003-harness)
manifest: none. This brief records no pack manifest, so neither S001_BLIND_MANIFEST (J8) nor S001_ANALYSIS_MANIFEST (J7) is set for it.
recorded: at hand-out, 2026-11-06 (LL-04, LL-24)

## Brief

The owner ruled A on decisions/questions/P-001-harness-landing.md (on branch cos/p001-answer-harness-landing): the surface guard reads your commits and the Check author's as one session, because both signed `Agent-Session: session_01QBwHGNGKXFwvVVdzkei5aT`; you remake your three commits with the same content, each signed with a label naming you as this session's builder.

1. In your worktree, create build/builder/e003-harness-signed from ed35668 and remake 3861b38, a42c2df and 9caff21 in that order, each with exactly the same tree as the commit it replaces, the same author and author date, and the same message except that its `Agent-Session:` line reads `Agent-Session: session_01QBwHGNGKXFwvVVdzkei5aT/builder-90`. Keep `Spec: S-001`. Change no file.
2. Show, for each pair, `git rev-parse <old>^{tree} <new>^{tree}` (the two must match) and `git diff --stat <old> <new>` (empty).
3. Run `python3 governance/checks/surface_guard.py diff --range ed35668f0e204698fcb8d15e3176a937ba1d73dc..build/builder/e003-harness-signed --branch build/builder/e003-harness-signed` and report it. Leave build/builder/e003-harness as it is.

Commit as `git -c user.name=builder -c user.email=builder@agents.invalid commit`, no model names or co-author lines, even if a hook asks. Do not push, open a pull request or merge. Return the six-part contract, the three new commit ids with the tree pairs, and `git log --format='%an %ae %s%n%b' -3`.
