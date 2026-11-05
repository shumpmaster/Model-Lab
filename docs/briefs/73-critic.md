# Brief 73 — critic — S-001's locked checks (Build-1), against the frozen spec

session: session_01QBwHGJ9ZMyT9fK17HjfmCc
model: claude-opus-5-5 (the checks' writer, the Check author, runs on claude-sonnet-5-5; D-056). A fresh session.
start: Model-Lab@e0d8104cc7e2f88f19e6370d0cf84743d92e9679 (fixed copy /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-checks)
recorded: at hand-out, 2026-11-04 (LL-04, LL-24)

## Brief

You are the Critic (your role file: .claude/agents/critic.md). Today is 2026-11-04. A fresh session, read-only; your return is recorded verbatim by the Orchestrator as reviews/S-001/_critic-checks.md.

Read only from the fixed copy /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-checks (Model-Lab at commit e0d8104); nothing changes there while you run. Do not read src/**, docs/handover/** or docs/reports/**. specs/S-001.md is frozen (experiments/E-003.md with it). The Check author has written S-001's locked checks, before any harness code exists, in tests/acceptance/ (the files named test_ac*.py and test_j*.py, and e003_support.py); most of them fail today because the scripts they call are not yet built, which is expected.

Check, as the standard milestone "Tests written before the work" requires (Personal-Org-Operating-Model OPERATING_MODEL.md §4, "Shown reached by: the Critic's pass on the locked checks"):
1. Every acceptance criterion AC1 to AC11 and every join J1 to J8 has a check that tests what the criterion or join says, from the frozen spec's words; name any criterion, join or awkward case left untested.
2. No check asks for more than the spec says, or contradicts it; where a check fixes something the spec leaves open (a script's name, a command, a format), say whether the choice is the least the test needs and consistent with the spec.
3. Each check could fail: it would catch a wrong implementation, not only a missing one.
4. No check holds or names a held-back check, a sheet's text, or anything from src/**.

Return first a column-0 line `Verdict: PASS` or `Verdict: FAIL`, then numbered findings marked blocking or not, then the six-part contract. Write "verdict" with a colon only in that first line.
