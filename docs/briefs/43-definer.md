# Brief 43 — definer — S-001's new draft, round 2: the plan review's round-1 findings

session: session_01QBwHGMBo8kZsMCS2EvKNwd
model: claude-opus-5-5 (its checker, the Critic, runs on claude-sonnet-5-5; D-056)
recorded: at dispatch, 2026-11-04 (LL-04, LL-24)

## Brief

You are the Definer (your role file: /home/user/Model-Lab/.claude/agents/definer.md). Today is 2026-11-04. A fresh session; brief 41 (docs/briefs/41-definer.md) keeps its task, standards and working rules. Work in the worktree /home/user/wt/ml-definer-r2, branch build/definer/p001-rewrite-r2 (at eb8fe9d). Commit as definer, each message ending with one trailer paragraph holding both `Agent-Session: session_01QBwHGMBo8kZsMCS2EvKNwd` and `Spec: S-001`. Write only specs/** and experiments/**. No push, no merge.

The plan review of the new draft failed at its round 1 (reviews/S-001/plan.md, "New draft, round 1"). Fix:
- **Blocking 1 to 4**: K1's probe of what a session's GitHub tools and git can reach, run before the first sheet and in the Orchestrator's and every work session, with what happens if it succeeds; what triggers a pair and what wakes the long-lived sessions, with the owner's actions per kind as a range that expects reclaims (or a named cadence, costed in the options); fixed-form lines for the first-use check results and the judging side's counts, with J4's and J5's tests extended; the milestones header (name M2 and M4, or say which criteria serve which).
- **Not blocking 6 to 9, 11 and 12**: where the pack folder sits and what the sheet session may hold of earlier kinds; the K3 fallback (the three scripts too, and no second repository that breaks K2 and AC5); J5's path check, length and character limit; which tip of governance/PACKS.toml is the starting state (the default branch at eb8fe9d: `[roles.S-001-holdout]` holds the earlier text, and `[roles.S-001-analysis]` does not exist); a lost sheet session (a new sheet, set id n = 2, one run, counted); the extract's sentence on what a judge is given.
- **Findings 5 and 10 are the owner's**: keep open question 8 (one judging session per kind, against one per judging) and add open question 9 (whether exports holding whole start trees of private repositories' work may go into public Model-Lab, or entry is restricted to public repositories), each with the consequence of each answer; say both are ruled at the Build gate, before the freeze.

New recorded facts: intake/P-001-environment-2026-11-04.md, the section "Tools this session holds for starting and waking sessions" (`create_session` takes a `source_url`; `send_later` and `create_trigger` schedule wakes that survive container restarts; `list_events` reads another session's transcript). They are the tools' own descriptions, not tested; where the design rests on one, make it a first-use check. Revise the "no record shows" lines they answer.

Change no threshold, size, option or criterion meaning unless a fix forces it, and list each in your return. Leave status draft. Run `python3 governance/checks/surface_guard.py diff --range eb8fe9d..HEAD --branch build/definer/p001-rewrite-r2` and `governance/checks/check_all.sh . eb8fe9d` in the worktree before you return. Return the six-part contract, with one line per finding.
