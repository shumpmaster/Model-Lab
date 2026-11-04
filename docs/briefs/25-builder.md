# Brief 25 — builder — run E-001 step 2 (replays), as a separate cloud session

session: session_01QBwHGN4kVVA3rfHx2b4FsF (starting session); the Builder runs as session_01QBwHGMu36mvZdxN2ssBspJ
model: claude-opus-5-5 (its helpers use the models E-001 names; the Reviewer will run on claude-sonnet-5-5)
recorded: at dispatch, 2026-11-03 (LL-04, LL-24)
why a separate session: a helper session cannot start helpers of its own, and E-001 requires the Builder to start every run (src/E-001/RESULT.md, "why step 2 was not run")

## Brief

The full prompt given to the session, verbatim, starting from branch claude/chief-of-staff-discovery-064xiz, pushing only to build/builder/p001-e001-runs:

You are the Builder for the Model-Lab project P-001 (the prompt engine). Your role file is .claude/agents/builder.md in the Model-Lab repository; read it, then AGENTS.md, then specs/S-001.md, experiments/E-001.md (frozen) and experiments/E-002.md (for the judge-brief template E-001's check runs use), then src/E-001/RESULT.md, which holds step 1 (the records check, done in another session, no runs used) and names the pieces step 2 takes by the registration's rule.

Task: run E-001 step 2 exactly as registered. You are a top-level session so that you can start the helper sessions the registration requires yourself (a helper session cannot start helpers of its own, which is why step 2 was not run before). Start every replay and check run yourself with your Agent tool, on the model the registration names (Opus 5.5 for replays, Fable 5.1 for the check runs), each with its working directory set to its history-limited copy; count every helper as started whatever its outcome, and stop at the registration's caps (at most 20 helper sessions for E-001, reruns only for your own set-up faults, each costing 2).

Set-up: the replays need the Service-Desk and Personal-Org-Operating-Model repositories (shumpmaster/Service-Desk, shumpmaster/Personal-Org-Operating-Model) with full history. Attach them with your add_repo tool (read access), clone them, and run `git fetch --unshallow` where a clone is shallow; unshallow Model-Lab too. Build every history-limited copy outside the clones, as E-001's method says, and record each copy's two checks.

Record: write everything under src/E-001/ (your lane and inside S-001's Areas touched), adding to RESULT.md every step-2 measure the registration names, per kind and stratum, each run's F4–F7 verdict citing its transcript line, and each helper's reported tokens, tool uses and time. Because the Reviewer that analyses the result runs in another session, copy each helper's transcript (your session folder's subagents/agent-<id>.jsonl) into src/E-001/transcripts/. Report the measures only; the Reviewer judges the thresholds.

Commit only as `git -c user.name=builder -c user.email=builder@agents.invalid commit`, each message ending with a trailer paragraph holding `Agent-Session: <your own session id>` and `Spec: S-001`. Never add model names or AI co-author lines to commits. Push only to your outcome branch, build/builder/p001-e001-runs. Do not open a pull request and do not merge. Do not run E-002.

Finish with the six-part contract (changed by file · why · verified with command and output · undone · needed outside your surface · open questions) and the number of runs started, as your final message.
