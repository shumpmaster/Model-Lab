# Brief 91 — reviewer — Build-2's stage 5 review: try to refute the harness scripts, running every expectation

session: session_01QBwHGNGKXFwvVVdzkei5aT
model: claude-fable-5-1 (the work's writer, the Builder, ran on claude-opus-5-5, brief 90; the locked checks' writer, the Check author, ran on claude-sonnet-5-5; D-056). A fresh session.
start: Model-Lab@3861b3843133588baa1406c617ba9e29193381da (fixed copy /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/fix-build1, the Builder's branch build/builder/e003-harness at its one commit, on the default branch at ed35668)
manifest: none. This brief records no pack manifest, so neither S001_BLIND_MANIFEST (J8) nor S001_ANALYSIS_MANIFEST (J7) is set for it.
recorded: at hand-out, 2026-11-05 (LL-04, LL-24)

## Brief

You are the Reviewer (your role file: .claude/agents/reviewer.md). Today is 2026-11-05. A fresh session; you edit nothing, and your return is recorded verbatim by the Orchestrator in reviews/S-001/_reviewer-build.md as round 1.

Read only from the fixed copy /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/fix-build1; nothing changes there while you run. Build any record or fixture you need in a new folder outside it. Do not read docs/reports/**, docs/briefs/** or docs/handoff/**.

The work is the Builder's one commit 3861b38 on top of ed35668 (`git -C <copy> diff --stat ed35668 3861b38`): the harness scripts under src/E-003/ that S-001's locked checks call (tests/acceptance/e003_support.py names the interfaces), and the Builder's own tests in tests/E-003/. Try to refute it against specs/S-001.md (frozen at f4298cd), experiments/E-003.md and E-001.md (frozen), and the locked checks.

1. Run the locked checks (`python3 -m unittest discover -s tests/acceptance -p 'test_*.py'`) and tests/E-003. For every test that fails or skips, say whether the fault is in the build or in the test, citing the spec line that decides it, and show the case that shows it.
2. Do not rely on the tests passing. For each script, build at least one case of your own from the frozen text that a wrong build would get wrong, and run it; give most weight to transcript_check.py (E-001's F4, read strictly: a /tmp path is clean only from the line that creates it), pair.py (copies, briefs and their paths, the confinement paragraph of E-003 Step 3) and fill_judge_brief.py (E-002's template with E-003 Step 4's changes).
3. analyse.py is a deliverable the checks add, a mechanical reference: confirm it does not present itself as the Reviewer's analysis.
4. Confirm the commit touches only src/E-003/** and tests/E-003/**, is by `builder <builder@agents.invalid>` with `Agent-Session:` and `Spec: S-001` trailers, and that nothing in it holds a sheet's text or reaches the sheets repository.
5. Add the join-up section your role file asks for at the end of Build: the scripts working together on one stand-in pair, from entry to export to judge brief to verdict record to cards.
6. Run `bash governance/checks/check_all.sh . ed35668` and `python3 governance/checks/surface_guard.py diff --range ed35668..3861b38`, and report them.

Return first a column-0 line `Verdict: PASS` or `Verdict: FAIL`, then numbered findings marked blocking or not, each with file:line and the case that reproduces it, then the six-part contract. Write "verdict" with a colon only in that first line.
