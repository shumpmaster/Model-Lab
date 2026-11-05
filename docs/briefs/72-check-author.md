# Brief 72 — check-author — S-001's own locked checks (dispatch (b)): AC1 to AC11 and the join tests J1 to J8

session: session_01QBwHGJ9ZMyT9fK17HjfmCc
model: claude-sonnet-5-5 (the Builder that will build to these checks runs on claude-opus-5-5; D-056). A fresh session, a helper of the Orchestrator's session, as S-001's "Two Check author jobs" names for dispatch (b).
start: Model-Lab@7d6c999594ced79a81bf73a60c6164f4b9c435ce (branch build/check-author/s001-locked, in its own worktree /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/wt-check)
recorded: at hand-out, 2026-11-04 (LL-04, LL-24)

## Pack (the standing `[roles.check-author]` pack, by hand)
- must read: specs/S-001.md (frozen @ f4298cd) and its join sheets; the ruling records decisions/questions/P-001-build-gate.md and decisions/questions/P-001-build-gate-terms.md.
- may read: the library (/home/user/portfolio/library), docs/playbooks/**; and the files the frozen spec itself names as inputs to a check (experiments/E-003.md and experiments/E-003/** apart from output files you do not need, governance/PACKS.toml, governance/checks/session_runner.py for `norm`).
- must not see: src/**, docs/handover/**, docs/reports/**, governance/HOLDOUTS.md (out of every pack, D-054); any held-back check (none exists; the sheets repository is not in this session).

## Brief

You are the Check author (your role file: .claude/agents/check-author.md). Today is 2026-11-04. Work only in your own worktree, /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/wt-check, on the local branch build/check-author/s001-locked (made from commit 7d6c999). Commit as `check-author <check-author@agents.invalid>` (`git -c user.name=check-author -c user.email=check-author@agents.invalid commit`) with the trailers `Agent-Session: session_01QBwHGJ9ZMyT9fK17HjfmCc` and `Spec: S-001`. Do not push. Read nothing under src/**, docs/handover/** or docs/reports/** (your pack above); no work product exists yet for this spec.

The owner passed the Build gate at size A and ruled the plan's terms; S-001 and E-003 are frozen at f4298cd. This is dispatch (b) of "Two Check author jobs": S-001's own locked checks, written before any harness code is built. You never hold a held-back check; those are written later, blind, in another session.

The task:
1. Write the locked checks for AC1 to AC11 in tests/acceptance/** (and checks/** if a check is a rubric rather than a test), each traced to its criterion by name, from the frozen spec's scenarios only.
2. Write one join test for each of J1 to J8, each file containing the marker `join-test: S-001/J<n>` that `v3_checks joins` looks for, testing what the join's own text says its test covers (J3's test repository, J4's stand-in sheet and block parser forms, J5's verdict-line forms, J7's and J8's pack and manifest checks against governance/PACKS.toml, case-folded as session_runner.py's `norm` does). Where a test needs a piece the Builder has not built yet (a script, a parser), name the interface you test against (path, command, input and output) in the test file and in your return, from the spec's own words; where the spec does not fix one, say so in your return as a contradiction or gap, and do not invent more than the test needs.
3. Tests that need the Builder's code will fail until it exists; say which. Tests that can pass now (for example J7's and J8's pack checks, AC1's file checks) should pass, or say why not.
4. Run `bash governance/checks/check_all.sh . origin/main` in your worktree after committing and report its summary; `v3_checks joins` should now pass; `record_checks merges` is a known local false failure on Orchestrator record commits (LL-29). Run `python3 governance/checks/surface_guard.py diff --range 7d6c999..build/check-author/s001-locked --branch build/check-author/s001-locked` and report it.

Return the six-part contract: each file with the criterion or join it checks, how to run the tests and their current result, the interfaces named, any contradiction or gap in the spec, the commit ids and `git log --format='%an %ae' -3`.
