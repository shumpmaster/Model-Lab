# Brief 28 — critic — plan review of the fair test (S-001, E-003)

session: session_01QBwHGLd77YbwCSMSPU26vW
model: claude-sonnet-5-5 (the writer, the Definer, ran on claude-opus-5-5; D-056)
recorded: at dispatch, 2026-11-04 (LL-04, LL-24)

## Brief

You are the Critic (your role file: /home/user/Model-Lab/.claude/agents/critic.md). Today is 2026-11-04. This is the plan review (round 1 of at most 3) of the fair test, milestone M2, before it can be frozen: /home/user/wt/ml-definer-s001/specs/S-001.md and its registration /home/user/wt/ml-definer-s001/experiments/E-003.md, with the change texts and sizing script under experiments/E-003/ (branch build/definer/p001-fair-test, checked out in that worktree; do not switch branches).

Standards: the spec form specs/_TEMPLATE.md; the freeze gate and the Design standard milestones (/home/user/Personal-Org-Operating-Model/OPERATING_MODEL.md §4, "Standard milestones" Design-1 to Design-6, and "Freeze gate"); the experiment playbook (§6) and experiments/_REGISTRATION.md; the project document docs/PROJECT.md (section 3, M2; section 6, V1 and V2 and the starting figures; section 7, U2, U3, R1 to R9; section 8, terms and constraints); and the owner's rulings in decisions/questions/ (P-001-open-unknowns.md, P-001-e002-not-tested.md, P-001-value-target.md, P-001-test-budget.md, P-001-spend-ceiling.md, P-001-worst-work.md, P-001-no-change-result.md). The replay run's analysis is reviews/E-001/reviewer.md; the count of past work is research/Q-008-memo.md.

Judge: whether the test could be run exactly as written by someone who did not write it; whether its thresholds decide each result before any run, leaving nothing to reinterpret; whether each criterion is a scenario the owner can approve and traces to V1 or V2; whether each join sheet covers a real hand-over with its awkward cases; whether every fact relied on has evidence that says what is claimed (re-run experiments/E-003/sizing.py and re-derive any figure you doubt); whether the candidate changes follow from the count's causes; whether the judging under U3's fallback is as sound as it claims and states what it cannot rule out; whether anything conflicts with a ruling or the project document; and whether the open questions put to the owner are complete and fairly stated.

Write no files. Return a record whose first line, in column 0, is exactly `Verdict: PASS` or `Verdict: FAIL`, then numbered findings, each blocking or non-blocking, each with the record and line that supports it.
