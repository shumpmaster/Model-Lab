# Brief 44 — definer — S-001's new draft, round 3: the plan review's round-2 findings

session: session_01QBwHGMBo8kZsMCS2EvKNwd
model: claude-opus-5-5 (its checker, the Critic, runs on claude-sonnet-5-5; D-056)
recorded: at dispatch, 2026-11-04 (LL-04, LL-24)

## Brief

You are the Definer (your role file: /home/user/Model-Lab/.claude/agents/definer.md). Today is 2026-11-04. A fresh session; briefs 41 and 43 (docs/briefs/) keep their task, standards and working rules. Work in the worktree /home/user/wt/ml-definer-r3, branch build/definer/p001-rewrite-r3 (at 043eba4). Commit as definer, each message ending with one trailer paragraph holding both `Agent-Session: session_01QBwHGMBo8kZsMCS2EvKNwd` and `Spec: S-001`. Write only specs/** and experiments/**. No push, no merge.

The plan review of the new draft failed at its round 2 on one blocking finding (reviews/S-001/plan.md, "New draft, round 2"). Round 3 is the last before the plan stop rule, so fix exactly the findings and nothing else:
- **A (blocking):** K1's probe against an empty repository proves nothing. Add a canary: the owner places one harmless file in shumpmaster/secret-marking (for example README.md holding one fixed word the owner chooses and gives only to the sheet session's lead), before any probe; parts (i) and (ii) pass only if refused and the canary is not shown; allow that file where the spec says the repository holds holdouts/ and verdicts/ only; and record in the J4/J5 k lines whether the canary was seen.
- **B:** after the first sheet exists, the probes must not fetch: `git ls-remote` and a read of the canary's name only.
- **C:** one sentence in "In plain words" on open questions 8 and 9, and on what it means if K1 part (iii) shows that the Orchestrator's side can read the sheets side's events (secrecy from that side by instruction only).
- **D:** a bound on the wakes' tokens, or say plainly that the budget excludes them.
- **E:** the authority for the weekly landing of the work session's records and exports: what review it gets, or why it is exempt, citing the rule that governs it.
- **F:** J5's served-model field form as J4's; J4's void-form awkward case aligned with the void form; K5 to cover a reclaim of the Orchestrator's own session.

Change no threshold, size, option or criterion meaning; list anything forced. Leave status draft. Run `python3 governance/checks/surface_guard.py diff --range 043eba4..HEAD --branch build/definer/p001-rewrite-r3` and `governance/checks/check_all.sh . 043eba4` before you return. Return the six-part contract, one line per finding.
