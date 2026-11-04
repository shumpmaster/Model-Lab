# Brief 32 — reviewer — PR #39, the blind Check author's per-task pack (S-001-holdout)

session: session_01QBwHGMBo8kZsMCS2EvKNwd
model: claude-fable-5-1 (the work's writer, the Chief of Staff, runs on claude-opus-5-5; D-056)
recorded: at dispatch, 2026-11-04 (LL-04, LL-24)

## Brief

You are the Reviewer (your role file: /home/user/Model-Lab/.claude/agents/reviewer.md). Today is 2026-11-04. Read-only: you edit nothing, commit nothing, push nothing.

Review pull request #39 in /home/user/Model-Lab, branch claude/chief-of-staff-design-u3hdz2: `git diff origin/main...HEAD -- governance/PACKS.toml` (the new `[roles.S-001-holdout]` table) and the PR body's Context and Tasks (saved at /tmp/claude-0/-home-user/ece28257-2441-5b09-947e-f298d6962395/scratchpad/body.md). The change is risk class R3 (governance/**).

The standard: specs/S-001.md, "Two Check author jobs" (the Pack row and the Never row), J8, AC4 and "Needed outside this spec's lane". Try to refute that the table, as the session runner would resolve it (governance/checks/session_runner.py: Config.pack_entry, _fill, norm, _any, always_out, manifest_problems; governance/checks/govlib.py glob_match), gives the blind Check author exactly experiments/E-003/check-author-extract.md, the role files and playbooks that extract names, and nothing S-001 says it must never see, in this repository and in Service-Desk (/home/user/Service-Desk), whose role files sit at the same paths. Judge in particular:
1. Whether the two stated departures from S-001's listing (change texts withheld by name instead of `C*.md`; governance/HOLDOUTS.md left out) are needed and keep S-001's intent, and whether either opens a gap.
2. Whether any path in either repository that S-001 withholds still resolves into the pack, or any path the extract names is missing.
3. Whether the table breaks anything that reads PACKS.toml (the runner, record_checks gate-packs, v3_checks), and whether the full checks pass: `governance/checks/check_all.sh . origin/main`.
4. Whether each Context bullet is true of the cited source, and the ticked task is done.

Return a first line `Verdict: PASS` or `Verdict: FAIL` in column 0, then numbered findings with file and line, each marked blocking or not; then the six-part contract.
