# Brief 79 — check-author — round 4 of S-001's locked checks, on the Reviewer's findings on pull request #51

session: session_01QBwHGJ9ZMyT9fK17HjfmCc
model: claude-sonnet-5-5 (its checks, the Critic and the Reviewer, run on claude-opus-5-5; the Builder will run on claude-opus-5-5; D-056). The same Check author session as briefs 72, 74 and 76, resumed.
start: Model-Lab@d372707fa947ccc1379bf0cbb0be2863e25791ca (branch build/check-author/s001-locked, in its own worktree /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/wt-check)
recorded: at hand-out, 2026-11-04 (LL-04, LL-24)

## Brief

The Critic passed your checks at round 3, and the required Reviewer then failed pull request #51, which carries them: two locked tests would fail a correct build. Its full return is in /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/tmp/rev51-r1.md (read it first; recorded verbatim as reviews/51/reviewer.md). The checks are not yet locked: they lock when #51 merges, so they are corrected here (feedback routing: checks wrong, back to stage 4).

1. Fix the Reviewer's findings 1 (AC6's re-scoring fixture, against E-003 Step 5) and 2 (J4's string matches, against E-002's template and E-003 Step 4: compare with whitespace collapsed, at every match the Reviewer names and any like it).
2. Fix finding 3 (the shared S001_MANIFEST variable: each test checks a named record only when it is its own kind or malformed, and skips with a plain message otherwise), finding 6 (AC9's docstring says the leave-out applies to a pair still mixed after its rerun), and the Critic's round-3 note 3 (the interface wording "clean on the line that creates it and on any later line", and the stale comment at test_ac05:138-139).
3. Before committing, run each changed test's expectation by hand against the frozen text it rests on, as the Reviewer did, not only against the finding (LL-53); a reference script outside the repository is fine, as before.
4. Commit on top of d372707 as before; do not push. Run the suite, `bash governance/checks/check_all.sh . 7d6c999` and the surface guard's diff range, and report them.

Return the six-part contract: what changed (file and line), how each expectation was checked, the new commit id, the suite's result, and `git log --format='%an %ae' -3`.
