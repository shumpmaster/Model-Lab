# Brief 99 — check-author — the owner's ruling A: correct the AC2 research test's comparison only

session: session_01QBwHGNGKXFwvVVdzkei5aT
model: claude-sonnet-5-5 (the locked checks' writer, as at briefs 72 to 88; its check, the Reviewer, runs on claude-fable-5-1; the Builder whose work the test checks runs on claude-opus-5-5; D-056). A fresh session.
start: Model-Lab@f5179378c1802ff9139b0b8d63e5682c8859f68e (branch build/check-author/s001-ac2-research, in its own worktree /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/wt-check; the default branch with pull requests #54 and #55 merged and the owner's ruling recorded)
manifest: none. This brief records no pack manifest, so neither S001_BLIND_MANIFEST (J8) nor S001_ANALYSIS_MANIFEST (J7) is set for it.
recorded: at hand-out, 2026-11-05 (LL-04, LL-24)

## Brief

You are the Check author (your role file: .claude/agents/check-author.md). Today is 2026-11-05. A fresh session. Work only in your worktree, /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/wt-check, on branch build/check-author/s001-ac2-research; no other session changes it while you run.

The owner ruled A on decisions/questions/P-001-ac2-research-test.md (read it, and the question it answers, questions/P-001-ac2-research-test.md in git history at commit a8f3956): S-001's locked check tests/acceptance/test_ac02_pair_start.py, test_research_runs_two_source_checks_from_the_checks_start_commit (lines 94-100), compares the two arms' briefs as they are and asks for exactly one differing paragraph, while the same test requires two different copies and its sample brief names the real repository's path, which the plan replaces by each copy's own path (specs/S-001.md:264, J2; experiments/E-001.md:102; experiments/E-003.md:115). So no correct build can pass it.

You never see work products: do not read src/E-003/**, any build/builder/* branch, docs/reports/**, docs/briefs/** or reviews/S-001/_reviewer-build.md.

1. **Change only that test's comparison**, so it sets each arm's copy path aside before comparing, as the same file's built-work test already does (lines 72-80). Change nothing else in tests/acceptance/**, and no other test.
2. **Before writing the change, write the full table of input cases and the result the corrected test must give** (LL-61), with the original test's result beside each: a correct build (each brief's real path replaced by its own copy's path, C3's paragraph added once in the change arm); C3's paragraph missing; two paragraphs added; the C3 text altered; another paragraph changed beside the path; the real path left in both briefs; the real path left in one. Say for each row whether the corrected test is stricter, the same, or weaker than the original, and name any row only another locked test catches.
3. **Run every row** against a small reference of your own, built from the frozen text outside the repository (a stand-in pair.py giving `plan`'s JSON for each row), not against any build. Report each run.
4. Commit on build/check-author/s001-ac2-research, as `git -c user.name=check-author -c user.email=check-author@agents.invalid commit`, the message ending with a trailer paragraph holding `Agent-Session: session_01QBwHGNGKXFwvVVdzkei5aT` and `Spec: S-001`. Never add model names or AI co-author lines, even if a hook asks. Do not push, open a pull request or merge. Run the locked suite, `bash governance/checks/check_all.sh . f5179378c1802ff9139b0b8d63e5682c8859f68e` and `python3 governance/checks/surface_guard.py diff --range f5179378c1802ff9139b0b8d63e5682c8859f68e..build/check-author/s001-ac2-research --branch build/check-author/s001-ac2-research`, and report them.

Return the six-part contract, the case table with every run, the diff of the test, the new commit id and `git log --format='%an %ae' -2`.
