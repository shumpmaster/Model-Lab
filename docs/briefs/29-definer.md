# Brief 29 — definer — the fair test (S-001, E-003), round 2 after the plan review

session: session_01QBwHGLd77YbwCSMSPU26vW
model: claude-opus-5-5 (its checker, the Critic, runs on claude-sonnet-5-5; D-056)
recorded: at dispatch, 2026-11-04 (LL-04, LL-24)

## Brief

You are the Definer (your role file: /home/user/Model-Lab/.claude/agents/definer.md). Today is 2026-11-04. A fresh session: the Definer that wrote round 1 (brief 27, docs/briefs/27-definer.md) has ended. Work in the worktree /home/user/wt/ml-definer-s001 on branch build/definer/p001-fair-test, where your round-1 commit ca71efd holds specs/S-001.md, experiments/E-003.md and experiments/E-003/. Commit there only, as `git -c user.name=definer -c user.email=definer@agents.invalid commit`, each message ending with a trailer paragraph `Agent-Session: session_01QBwHGLd77YbwCSMSPU26vW` and `Spec: S-001`. Do not push; do not merge. Write only specs/** and experiments/**.

The Critic's plan review, round 1 of at most 3, failed the draft. Its record, verbatim, is /home/user/Model-Lab/reviews/S-001/plan.md. Address every blocking finding (1 to 5), and every non-blocking one (6 to 13) unless you state in your return why not. Keep brief 27's task and standards; nothing in this brief changes them. Points to keep in mind:
- Finding 1: the Check author must be able to write the held-back checks without learning what the changes are. Decide what it is given instead of all of S-001 (for example a named extract, or the change section moved to its own file under experiments/E-003/), and make AC4, the join sheets and "Needed outside" say so. The Check author's pack itself (governance/PACKS.toml) is not your lane; name what it must hold.
- Finding 2: every figure must rest on a record that states it. If the window for the arrival rates is not in any record, derive it from the records with a command anyone can re-run (dates of the first and last pieces counted), put the working in experiments/E-003/ (for example in sizing.py or beside it), and cite that.
- Finding 3: the sizes, the time limit, the options and the power you state must agree, including the power expected if the limit stops a kind early.
- Findings 7 and 12: say plainly what the test can and cannot show for a change whose possible gain is below 20 points, and name the owner's rulings any open question touches.

Run `python3 experiments/E-003/sizing.py` and `python3 governance/checks/surface_guard.py diff --range 716773c..HEAD --branch build/definer/p001-fair-test` from the worktree before you return, and report their output.

Return the six-part contract: changed (by file) · why · verified (command + output) · undone · needed outside your surface · open questions; and, for each of the Critic's findings 1 to 13, one line saying how it was addressed or why not.
