# Brief 24 — builder — run E-001 (replay) exactly as registered

session: session_01QBwHGN4kVVA3rfHx2b4FsF
model: claude-opus-5-5 (the run's helpers use the models E-001 names; the Reviewer that analyses it runs on claude-sonnet-5-5)
recorded: at dispatch, 2026-11-03 (LL-04, LL-24)

## Brief

You are the Builder (your role file: /home/user/Model-Lab/.claude/agents/builder.md). Today is 2026-11-03. Run the frozen registration experiments/E-001.md (frozen at 4e2cb12) exactly as written, under the draft spec specs/S-001.md. Read both first, and E-002.md for the judge-brief template E-001's check runs use. Work in the worktree /home/user/wt/ml-builder on branch build/builder/p001-e001 (already created from main; do not switch other checkouts). The full clones are /home/user/Service-Desk, /home/user/Personal-Org-Operating-Model, /home/user/Model-Lab and /home/user/portfolio; Service-Desk and Personal-Org-Operating-Model were unshallowed this session (check with `git rev-parse --is-shallow-repository`; run `git fetch --unshallow origin` if needed). Build every history-limited copy outside the clones, under /home/user/wt/e001/.

Write everything you produce under src/E-001/ in your worktree (your lane): RESULT.md with every measure the registration names, per kind and per stratum, the records-check table with each F1–F3 verdict citing its record lines, each copy's two checks, each run's F4–F7 verdicts with the transcript path, and the runs started; plus any scripts you use. Do not judge the thresholds' outcome yourself beyond reporting the measures: the Reviewer analyses them. Commit only on your branch as `git -c user.name=builder -c user.email=builder@agents.invalid commit`, each message ending with a trailer paragraph `Agent-Session: session_01QBwHGN4kVVA3rfHx2b4FsF` and `Spec: S-001`. Do not push or merge.

Runs: start every helper session yourself, on the model the registration names, and count each as started whatever its outcome; stop at the registration's caps. If you cannot start helper sessions from your own session, stop after step 1 (the records check, which uses no runs), commit it, and say so plainly. Record each helper's reported tokens, tool uses and time in RESULT.md.

Return the six-part contract: changed (by file) · why · verified (command + output) · undone · needed outside your surface · open questions, and the number of runs started.
