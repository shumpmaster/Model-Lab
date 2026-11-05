# Brief 96 — reviewer — Build-2's stage 5 review, round 2: the Builder's round 2 on the harness scripts

session: session_01QBwHGNGKXFwvVVdzkei5aT
model: claude-fable-5-1 (the work's writer, the Builder, runs on claude-opus-5-5, briefs 90 and 92; the locked checks' writer, the Check author, ran on claude-sonnet-5-5; D-056). The same Reviewer session as brief 91, resumed.
start: Model-Lab@a42c2dfcc53bdc98e0e14c8388a8bfdb8367cbad (fixed copy /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/fix-build2, the Builder's branch build/builder/e003-harness at its second commit, on the default branch at ed35668)
manifest: none. This brief records no pack manifest, so neither S001_BLIND_MANIFEST (J8) nor S001_ANALYSIS_MANIFEST (J7) is set for it.
recorded: at hand-out, 2026-11-05 (LL-04, LL-24)

## Brief

Round 2 of your stage 5 review; your return is recorded verbatim as round 2 in reviews/S-001/_reviewer-build.md. The Builder was sent back on your round 1 to fix findings 1 (blocking), 2, 3, 4 and 6, and to leave finding 5 and the AC2 research test alone (the AC2 test is a question for the owner). Its new commit is a42c2df on top of 3861b38 (`git -C <copy> diff 3861b38 a42c2df`).

Read only from /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/fix-build2; nothing changes there while you run. Build any fixture in a new folder outside it; your round 1 case scripts are in /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/review-cases/. Do not read docs/reports/**, docs/briefs/** or docs/handoff/**.

1. Rerun your round 1 cases and the locked suite on the new commit, and say for each of findings 1 to 4 and 6 whether it is fixed.
2. The Builder's own tests now hold tables of input cases with required results (tests/E-003/test_round2_cases.py). Run them, and judge each row against the frozen text (E-001's F4, E-003 Exclusions 1 and 2, J2, J3): is the required result the one the text gives? For rows where the text leaves the result open, say whether reading it as a leak, or as left out, is the strict reading or goes beyond it, and what each such row costs the test (a pair lost, a run lost, or nothing). Build cases of your own beside the tables, aimed at what a wrong fix would get wrong: a leak that still reads clean, and a clean command in E-001's own transcripts (src/E-001/transcripts/) that now reads as a leak.
3. Confirm nothing that passed in round 1 now fails, and that the commit touches only src/E-003/** and tests/E-003/**, under the builder identity with its trailers.
4. Update your join-up section if any join changed.
5. Run `bash governance/checks/check_all.sh . ed35668` and `python3 governance/checks/surface_guard.py diff --range ed35668..a42c2df`, and report them.

Return first a column-0 line `Verdict: PASS` or `Verdict: FAIL`, then numbered findings marked blocking or not, each with file:line and the case that reproduces it, then the six-part contract. Write "verdict" with a colon only in that first line. The AC2 research test is not a finding against the build if its fault is still in the test.
