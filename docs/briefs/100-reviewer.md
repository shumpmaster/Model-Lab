# Brief 100 — reviewer — the corrected AC2 research test: run every case against the real build and broken copies of it

session: session_01QBwHGNGKXFwvVVdzkei5aT
model: claude-fable-5-1 (the test's writer, the Check author, runs on claude-sonnet-5-5, brief 99; the build it checks was written by the Builder on claude-opus-5-5; D-056). The same Reviewer session as briefs 91, 96 and 98, resumed.
start: Model-Lab@6a958b6174440554656860422fcc1b7637246274 (fixed copy /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/combo: the Check author's commit daa44a3 on the default branch at f517937, with the Builder's branch at 9caff21 merged in locally so the test can run against the build; this merge is not pushed)
manifest: none. This brief records no pack manifest, so neither S001_BLIND_MANIFEST (J8) nor S001_ANALYSIS_MANIFEST (J7) is set for it.
recorded: at hand-out, 2026-11-05 (LL-04, LL-24)

## Brief

The owner ruled A on decisions/questions/P-001-ac2-research-test.md: the Check author corrects only the AC2 research test's comparison, and one review runs every case of it, not only reads it; the change then goes to the owner as a high-risk pull request. You are that review; your return is recorded verbatim in the pull request's reviews/<PR>/reviewer.md.

Read only from /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/combo; nothing changes there while you run. Build any fixture or broken copy in a new folder outside it. Do not read docs/reports/** or docs/briefs/**. The change is `git -C /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/combo diff f517937 daa44a3 -- tests/acceptance`.

1. Run the corrected test, and the whole locked suite, against the real build in the copy.
2. Build broken copies of src/E-003/pair.py outside the copy, one per case, and run the corrected test against each: C3's paragraph missing; two paragraphs added; the C3 text altered in its first words; altered after them; another paragraph changed in the change arm only; changed identically in both arms; the real path left in both briefs; left in one. Say for each whether the corrected test fails, as it must, and which assertion fails it; name any case it passes and whether any other locked test catches it.
3. Confirm the change touches only that one test in tests/acceptance/test_ac02_pair_start.py, matches the ruling (the comparison only, as the same file's built-work test at lines 72-80 does), and is by `check-author <check-author@agents.invalid>` with its trailers. Say whether anything it adds beyond setting the copy paths aside goes past the ruling.
4. Run `bash governance/checks/check_all.sh . f517937` on the copy, and report it.

Return first a column-0 line `Verdict: PASS` or `Verdict: FAIL`, then numbered findings marked blocking or not, each with file:line and the case that reproduces it, then the six-part contract. Write "verdict" with a colon only in that first line.
