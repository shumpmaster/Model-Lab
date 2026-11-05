# Brief 88 — check-author — the focused round the owner ruled: J7 and J8 each with its own setting

session: session_01QBwHGJ9ZMyT9fK17HjfmCc
model: claude-sonnet-5-5 (its check, the Reviewer, runs on claude-opus-5-5; D-056). The same Check author session as briefs 72, 74, 76, 79 and 82, resumed.
start: Model-Lab@bef590a72dd027794a3b96f708ef8c1d916dcf11 (branch build/check-author/s001-locked, in its own worktree /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/wt-check)
recorded: at hand-out, 2026-11-05 (LL-04, LL-24)

## Brief

The Critic's round 5 and the Reviewer's round 3 failed J7 and J8 on the same hole, and Triage traced its root cause: both tests read one shared setting, S001_MANIFEST, and guess from a record's contents whether it is theirs; every guess lets some faulty record skip (/tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-records2/triage/P-001-S-001-checks-round-5.md; read it first, with its case table). The owner ruled "A: one focused round (Recommended)": you give each of the two checks its own setting, so each tests the list it is named for whatever that list holds; one review then runs every case in the trace's table, and a failure goes back to the owner (decisions/questions/P-001-checks-stop.md on branch cos/p001-answer-checks-stop).

1. J8 reads only S001_BLIND_MANIFEST and J7 only S001_ANALYSIS_MANIFEST (or names you choose, one per test); when its own setting is set, each checks that record whatever it holds and never skips it; each ignores the other's setting and S001_MANIFEST. When its own setting is unset, the scan of docs/briefs stays as it is.
2. Bring the docstrings, skip messages and e003_support.py's run instructions into line with the two settings. Change nothing else.
3. Before committing, run J7 and J8 each alone, with its own setting naming each of the trace's rows A to E (a record with no file lines; blind marker only; analysis marker only; both; neither), and also with only the other test's setting set; every row must give the trace's required result for a record named for that test (check and fail, or check and pass on its merits), and setting only the other's must leave the test unaffected. Report each run.
4. Commit on top of bef590a as before; do not push. Run the suite, `bash governance/checks/check_all.sh . 7d6c999` and the surface guard's diff range, and report them.

Return the six-part contract: what changed (file and line), the runs, the new commit id, the suite's result, and `git log --format='%an %ae' -3`.
