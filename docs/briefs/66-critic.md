# Brief 66 — critic — M2's reworded "done when", and the project document's lines restated to the Build-gate terms

session: session_01QBwHGJ9ZMyT9fK17HjfmCc
model: claude-sonnet-5-5 (the lines' writer, the Chief of Staff, runs on claude-opus-5-5; D-056). A fresh session.
start: Model-Lab@480fb62e61dcca1a9be3ecff35541c18290f6647 (fixed copy /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-terms); Personal-Org-Operating-Model@226f1c5f1bec162cf2ddf36ded1f3fddbbb096a3
recorded: at hand-out, 2026-11-04 (LL-04, LL-24)

## Brief

You are the Critic (your role file: .claude/agents/critic.md). Today is 2026-11-04. A fresh session, read-only; your return is recorded verbatim by the Orchestrator as reviews/P-001-build-terms/critic.md.

Read only from the fixed copy /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-terms (Model-Lab at commit 480fb62); nothing changes there while you run. Its last commit reworded seven lines of docs/PROJECT.md; `git -C /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-terms show HEAD` shows the old and new text. The owner ruled the Build gate's terms "All as recommended": term 1, A, rewords V1 and M2's "done when" to the plan's proposed texts and restates the project document's other "past tasks" lines and its "about 300 runs" line to match (decisions/questions/P-001-build-gate-terms.md; questions/P-001-build-gate-terms.md as it stood is in `git -C /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-terms show 2350130:questions/P-001-build-gate-terms.md`; the proposed texts are in specs/S-001.md, "Open questions for the owner", 1 and 2). The gate's size is in decisions/questions/P-001-build-gate.md.

Check, against Personal-Org-Operating-Model OPERATING_MODEL.md §3 "Milestones, sprints and steps" and "Why and context" (/home/user/Personal-Org-Operating-Model) and the records:
1. M2's reworded line: an achievement, not a task; its "done when" exactly the plan's proposed text; the line's form `<name> (M<id>) · done when <…> · phase: <phase> · why: <reason>`; its why still true now the test uses new work.
2. V1: exactly the plan's proposed text.
3. Each other changed line: true of the record it cites (the gate answer, specs/S-001.md's "Budget options by kind and order" table, reviews/E-001/reviewer.md), and consistent with the rest of docs/PROJECT.md.
4. Any line of docs/PROJECT.md left unchanged that still says the test uses past tasks or about 300 runs, as a statement of the plan (not of what Discovery's research or pre-mortem said at the time): name it.

Return first a column-0 line `Verdict: PASS` or `Verdict: FAIL`, then numbered findings marked blocking or not, then the six-part contract.
