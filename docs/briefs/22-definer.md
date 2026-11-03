# Brief 22 — definer — the two Design checks: replay (U2) and judge consistency (U3)

session: session_01QBwHGN4kVVA3rfHx2b4FsF
model: claude-opus-5-5 (its checker, the Critic, will run on claude-sonnet-5-5; D-056)
recorded: at dispatch, 2026-11-03 (LL-04, LL-24)

## Brief

You are the Definer (your role file: /home/user/Model-Lab/.claude/agents/definer.md). Today is 2026-11-03. The owner passed the Design gate for P-001, the prompt engine (decisions/questions/P-001-design-gate.md). Work in the worktree /home/user/wt/ml-definer on branch build/definer/p001-design-checks (already created; do not switch branches elsewhere). Commit there only, as `git -c user.name=definer -c user.email=definer@agents.invalid commit`, each message ending with a trailer paragraph `Agent-Session: session_01QBwHGN4kVVA3rfHx2b4FsF` and `Spec: E-001` (or E-002). Do not push; do not merge.

Task: write two experiment pre-registrations from experiments/_REGISTRATION.md, frozen line left as the placeholder (the Critic checks them first):
- experiments/E-001.md — **replay (U2):** can past tasks be re-run faithfully at the repository state they started from, so a paired test (the same past tasks with and without a change) can run? Read docs/PROJECT.md section 7 (U2, pre-mortem R9), section 8 (terms, "run", the 100-run budget and the 40-run limit for both checks together) and decisions/questions/P-001-open-unknowns.md.
- experiments/E-002.md — **judge consistency (U3):** are the checks that would judge the test consistent and unbiased enough? Same sources, plus R3 and section 8's constraint on judges from a different model or provider within the existing plan.

Each registration names: the hypothesis stated so that either outcome is a result; the method (which past tasks, chosen how, from which records; research/Q-008-memo.md lists the strata and records of past work); the measure; the sample and the runs it uses (E-001 and E-002 together at most 40; say what counts as one run); exclusions; the deciding threshold set now, including what result triggers the brief's fallback; holdout use ("none" unless you need one); and the milestone it serves (M2, and the standard milestone Design-3). Facts about the environment are in docs/reports/2026-11-03-design-environment-check.md: full history is readable after `git fetch --unshallow`, helpers can run on Opus 5.5, Sonnet 5.5, Haiku 5.5 or Fable 5.1 (one provider), and a git worktree at a past commit can be a helper's working directory. State plainly where the one-provider limit weakens E-002. Keep each registration short enough for the owner to follow; plain English, with terms from section 8.

Return the six-part contract: changed (by file) · why · verified (command + output) · undone · needed outside your surface · open questions.
