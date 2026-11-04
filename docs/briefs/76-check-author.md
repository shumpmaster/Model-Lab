# Brief 76 — check-author — round 3 of S-001's locked checks, on the Critic's round-2 findings

session: session_01QBwHGJ9ZMyT9fK17HjfmCc
model: claude-sonnet-5-5 (its check, the Critic, runs on claude-opus-5-5; the Builder will run on claude-opus-5-5; D-056). The same Check author session as briefs 72 and 74, resumed.
start: Model-Lab@742ef89 (branch build/check-author/s001-locked, in its own worktree /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/wt-check)
recorded: at hand-out, 2026-11-04 (LL-04, LL-24)

## Brief

The Critic's round 2 resolved round 1's findings apart from one new blocking contradiction that the fix for round 1's finding 2 brought in; its full return is in /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/tmp/crit-checks-r2.md (read it first). This may be the last round the stop rule allows (whether the rule counts check rounds is open, docs/LESSONS.md LL-55), so make only the changes below and add no new test or claim.

1. Finding 1: take the reading of E-001's F4 that its words give ("files the run itself creates in the system temporary directory"): a /tmp path is clean only when an earlier line of the same transcript creates it. Make test_ac05_judging.py:181's case create the file first, keep the uncreated /tmp reads as leaks, and change e003_support.py's interface note to match. Check every transcript-check case and the docstring against F4's words, and against each other, before committing (LL-53).
2. Finding 2's weakness: when S001_MANIFEST names a record, check that record whatever its kind, so a badly formed manifest fails instead of skipping.
3. Leave the rest of finding 10 and finding 7's note as they are; answer them in your return if you wish.
4. Commit on top of 742ef89 as before; do not push. Run the suite, `bash governance/checks/check_all.sh . 7d6c999` and the surface guard's diff range, and report them.

Return the six-part contract: what changed (file and line), the new commit id, the suite's result, and `git log --format='%an %ae' -3`.
