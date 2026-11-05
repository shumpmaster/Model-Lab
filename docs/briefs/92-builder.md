# Brief 92 — builder — Build-2, round 2: the Reviewer's findings on the harness scripts

session: session_01QBwHGNGKXFwvVVdzkei5aT
model: claude-opus-5-5 (the work's checks were written by the Check author on claude-sonnet-5-5; the Reviewer that checks this round runs on claude-fable-5-1; D-056). The same Builder session as brief 90, resumed. Build round 2 of 3 (OPERATING_MODEL §4, stop rule).
start: Model-Lab@3861b3843133588baa1406c617ba9e29193381da (branch build/builder/e003-harness, in its own worktree /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/wt-builder)
manifest: none. This brief records no pack manifest, so neither S001_BLIND_MANIFEST (J8) nor S001_ANALYSIS_MANIFEST (J7) is set for it.
recorded: at hand-out, 2026-11-05 (LL-04, LL-24)

## Brief

The Reviewer's stage 5 review of your commit 3861b38 is FAIL at round 1, on one blocking finding, with five more not blocking. Read it first: reviews/S-001/_reviewer-build.md (on branch claude/chief-of-staff-p001-build-5m9j1d; a copy of that file is at /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/round2/_reviewer-build.md). Its own case scripts are under /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/review-cases/; you may read and run them, and change nothing there.

1. **Finding 1 (blocking), transcript_check.py.** A path outside the copy inside a quoted argument (`bash -c`, `sh -c`, `eval`, `python3 -c`, `node -e`, `perl -e`, and the like) must not read as clean.
2. **Findings 2, 3, 4 and 6 (not blocking, but defects against the frozen text): fix them too.** 2: a URL or repository named in any git subcommand, a `$VAR` path with a `..` segment, and a network listener. 3: pair.py audit leaves a pair out when the real work's branch takes in any commit that is neither its own nor an ancestor of the start commit (E-003 Exclusions 1), not only the default branch's. 4: pair.py plan refuses, or replaces, an absolute path in the brief that is not the copy's when the entry has no `real_path`. 6: export.py make takes the task statement's path for built work and research, as J3 lists it.
3. **Before writing any of these classification fixes (1, 2 and 3), write the full table of input cases and the result each must give** (LL-61): for 1, every wrapper form and quoting you handle, with paths inside the copy, outside it, under /tmp before and after creation, and a quoted string that only looks like a path (for example in an echo); for 2, each new form beside the forms already handled; for 3, the merge cases of the AC3 test and of the Reviewer's case 5. Put each table in your tests in tests/E-003/ so every row runs, and include it in your return. Where the strict F4 reading leaves a row open, choose the result that reads as a leak and say so.
4. **Do not change** finding 5 (the `recorded: at hand-out` form; it is the recording form's question, not the build's), the failing AC2 research test (a contradiction between that locked test and the spec, going to the owner), or anything outside src/E-003/** and tests/E-003/**. Change nothing the findings do not need.
5. Before handing back, run, from the worktree's root: the locked suite, tests/E-003, the Reviewer's case scripts that bear on your fixes, `bash governance/checks/check_all.sh . ed35668f0e204698fcb8d15e3176a937ba1d73dc` and `python3 governance/checks/surface_guard.py diff --range ed35668f0e204698fcb8d15e3176a937ba1d73dc..build/builder/e003-harness --branch build/builder/e003-harness`. Report each result.

Commit on top of 3861b38 on build/builder/e003-harness, as before (`builder <builder@agents.invalid>`, trailers `Agent-Session: session_01QBwHGNGKXFwvVVdzkei5aT` and `Spec: S-001`, no model names or co-author lines). Do not push, open a pull request or merge.

Return the six-part contract, the case tables, the new commit id and `git log --format='%an %ae' -3`.
