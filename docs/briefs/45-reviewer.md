# Brief 45 — reviewer — PR #44, the fair test's per-task reading lists

session: session_01QBwHGMBo8kZsMCS2EvKNwd
model: claude-fable-5-1 (the work's writer, the Chief of Staff, runs on claude-opus-5-5; D-056)
recorded: at dispatch, 2026-11-04 (LL-04, LL-24)

## Brief

You are the Reviewer (your role file: /home/user/Model-Lab/.claude/agents/reviewer.md). Today is 2026-11-04. Read-only: you edit nothing, commit nothing, push nothing.

Review pull request #44 in /home/user/Model-Lab at commit 09dfa20: `git diff origin/main...HEAD -- governance/PACKS.toml` (`[roles.S-001-holdout]` edited, `[roles.S-001-analysis]` added). Risk class R3 (governance/**).

The standard: specs/S-001.md, "Needed outside this spec's lane", the bullet "The per-task packs" and its two sub-bullets, which specify each table's must_read, must_not_see and comment exactly; also "Two Check author jobs", "The Reviewer's reach", J7 and J8. Try to refute that each table, as governance/checks/session_runner.py would resolve it (norm, _fill, _any, always_out; govlib glob_match), matches the specification exactly, withholds every path S-001 says it must, and holds every path S-001 says it must, in this repository; and that nothing else reading PACKS.toml breaks (`governance/checks/check_all.sh . origin/main`; the only expected local failure is `record_checks merges` on the orchestrator's record commits, LL-29). Also check that each comment says what S-001 asks it to say, and that the Context bullets and the ticked task in the PR body (/tmp/claude-0/-home-user/ece28257-2441-5b09-947e-f298d6962395/scratchpad/body10.md) are true.

Return a first line `Verdict: PASS` or `Verdict: FAIL` in column 0, then numbered findings with file and line, each marked blocking or not; then the six-part contract.
