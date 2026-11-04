# Brief 56 — definer — S-001: the "together" weeks tied to the wrong order

session: session_01QBwHGKFFgmANWaCNGxCLZd
model: claude-opus-5-5 (its check, the Critic, runs on claude-sonnet-5-5; D-056). A fresh session.
recorded: at dispatch, 2026-11-04 (LL-04, LL-24)

## Brief

You are the Definer (your role file: .claude/agents/definer.md). Today is 2026-11-04. Work in your own worktree, /home/user/wt-definer, on the local branch build/definer/s001-together (made from commit a21cbd0 of claude/chief-of-staff-design-u3hdz2). Commit as `definer <definer@agents.invalid>` with the trailers `Agent-Session: session_01QBwHGKFFgmANWaCNGxCLZd` and `Spec: S-001`. Do not push.

The fault. experiments/E-003/sizing.py (lines 145-149) computes "weeks together" as the longest single kind's weeks, which is true only if all three kinds collect from the start. specs/S-001.md ties that figure to a different order: line 90, "'together' if the owner allows the next kind to collect while the previous is judged", and open question 4 (line 337), which sets 32 to 64 against the question "May the next kind's pieces start collecting while the previous kind is being judged and analysed?". Under that order each kind's collection still follows the previous one's, so collection takes the one-after-another weeks (60 to 121 for option A); only the judging and analysis time overlaps, and no record estimates it. The Critic noted this (reviews/P-001-build-gate/critic.md, round 3, finding 4).

The task. Correct S-001 so every "together" figure is tied to the order the script computes. Line 90's note and the table's column heading (around line 94); open question 4, restated so each order it offers carries the weeks that are true of it: one kind after another; the next kind collecting while the previous is judged (collection weeks as one after another, less the judging time, which is not estimated); all three collecting from the start, analysed one after another (the "together" figure); and all three collected and analysed at once, if you keep it. Say for each whether it reads the owner's ruling "every kind, incrementally" literally or goes beyond it (decisions/questions/P-001-worst-work.md), as the plan already does for the others. Then check every other line that uses "together", "side by side" or the together figures (in particular lines 15 and 317, the Risks section, and experiments/E-003.md) and keep them consistent. Change no figure: every number must stay a line of experiments/E-003/output.txt. Do not change sizing.py or output.txt. Change nothing else in the plan.

Before you commit, check each sentence you change against the record it states (the script and its output, the ruling), not only against this brief (LL-53).

Return the six-part contract, with the diff's changed lines quoted, the commit id, and `git log --format='%an %ae' -1`.
