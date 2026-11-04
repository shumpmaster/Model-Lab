# Brief 58 — definer — S-001: the owner's part, line 17's worst case and the Orchestrator's wake fallback

session: session_01QBwHGKFFgmANWaCNGxCLZd
model: claude-opus-5-5 (its check, the Critic, runs on claude-sonnet-5-5; D-056). A fresh session.
recorded: at dispatch, 2026-11-04 (LL-04, LL-24)

## Brief

You are the Definer (your role file: .claude/agents/definer.md). Today is 2026-11-04. Work only in your own worktree, /home/user/wt-definer2, on the local branch build/definer/s001-owner-part (made from commit 0cc8be0 of claude/chief-of-staff-design-u3hdz2). Commit as `definer <definer@agents.invalid>` with the trailers `Agent-Session: session_01QBwHGKFFgmANWaCNGxCLZd` and `Spec: S-001`. Do not push.

Two faults Triage found in the plan (triage/P-001-build-gate-round-3.md, "Contributing stage 3 faults"):
1. specs/S-001.md line 17 ("Your part in running it") says the owner's part grows, "for option A, up to about 180 to 360 in all". The plan's own table ("The owner's actions per option", lines 126-135) reaches 183 to 366 session starts if K5 fails, and 243 to 487 if K5 also fails in the Orchestrator's own session; the K7 wake messages are 60 to 121, or 180 to 363.
2. K7 (line 189) says that if a session cannot wake itself in the Orchestrator's session, "the owner asks for the weekly landing". The owner-action table counts no such ask, so its "worst named fallback" (line 126) is not the worst.

The task. Make line 17 true of the table, with its worst case. Add the Orchestrator-session K7 ask to "The owner's actions per option" so the ranges count it, or, if you judge it is not countable, say plainly there that the ranges leave it out and why. Any new figure must follow from the table's own *w* (weeks one after another, from experiments/E-003/output.txt) the way the existing columns do, with its working shown as the table's other columns are. Then check every other line that states the owner's part or its ranges (in particular lines 16-18, open question 8 and the "Needed outside" list) and keep them consistent. Change nothing else; change no other figure; do not change sizing.py or output.txt.

Before you commit, check each sentence you change against the record it states (the table, K5, K7, output.txt), not only against this brief (LL-53). Run `python3 governance/checks/surface_guard.py diff --range 0cc8be0..build/definer/s001-owner-part --branch build/definer/s001-owner-part` after committing and report its output.

Return the six-part contract, with the diff's changed lines quoted (old and new), the commit id, and `git log --format='%an %ae' -1`.
