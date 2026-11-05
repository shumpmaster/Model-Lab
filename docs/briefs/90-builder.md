# Brief 90 — builder — Build-2: the fair test's harness scripts under src/E-003/

session: session_01QBwHGNGKXFwvVVdzkei5aT
model: claude-opus-5-5 (the work's checks were written by the Check author on claude-sonnet-5-5; the Reviewer that checks this build must run on a model other than claude-opus-5-5; D-056). A fresh session.
start: Model-Lab@ed35668f0e204698fcb8d15e3176a937ba1d73dc (branch build/builder/e003-harness, in its own worktree /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/wt-builder; the default branch with pull requests #51 and #53 merged)
manifest: none. This brief records no pack manifest, so neither S001_BLIND_MANIFEST (J8) nor S001_ANALYSIS_MANIFEST (J7) is set for it; with both unset, J7 and J8 scan docs/briefs as written.
recorded: at hand-out, 2026-11-05 (LL-04, LL-24)

## Brief

You are the Builder for Model-Lab's project P-001, the prompt engine (your role file: .claude/agents/builder.md). Today is 2026-11-05. Read AGENTS.md, then specs/S-001.md (frozen at f4298cd) with its join sheets, experiments/E-003.md (frozen), experiments/E-001.md for the copy method and F4, experiments/E-002.md for the judge-brief template, and the locked checks in tests/acceptance/, starting with tests/acceptance/e003_support.py.

Work only in your worktree, /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/wt-builder, on branch build/builder/e003-harness. No other session changes that folder while you run.

Task: build the harness scripts under src/E-003/ to the interfaces e003_support.py names (change.py, pair.py, transcript_check.py, fill_judge_brief.py, export.py, block.py, verdicts.py, judge.py, cards.py, analyse.py, counts.py, kind.py), so that every locked check a correct build should pass, passes. Today 43 tests pass and 183 fail because the scripts do not exist.

1. Build to the frozen spec and E-003. Where the spec and a locked check disagree, or a check could only pass by going against the spec, stop on that point and report it; never edit tests/acceptance/**, checks/**, specs/**, experiments/** or governance/**.
2. analyse.py is a deliverable the checks add, not one the spec names: a mechanical reference for the analysis. It is not the Reviewer's result; E-003 has the Reviewer, which did not run the test, do the analysis. Say so in the script's own help text.
3. transcript_check.py follows the strict reading of E-001's F4 that the checks pin: a /tmp path is clean only from the line that creates it (a Bash `>` or `>>` target, a `touch` or `mkdir` argument, or a Write or Edit file_path), on that line and later ones, never before it.
4. Your own tests, if any, go in tests/E-003/. Python standard library only, as the checks are; each script runs as `python3 -I src/E-003/<name>.py ...` from the repository root.
5. Run no fair-test run: start no helper session, make no copy of a real piece, and hold no sheet. Use only the stand-in sheet the checks provide. The sheets repository is not yours to attach or read.
6. Before handing back, from the worktree's root: run `python3 -m unittest discover -s tests/acceptance -p 'test_*.py'`, any tests you add, `bash governance/checks/check_all.sh . ed35668f0e204698fcb8d15e3176a937ba1d73dc`, and `python3 governance/checks/surface_guard.py diff --range ed35668f0e204698fcb8d15e3176a937ba1d73dc..build/builder/e003-harness --branch build/builder/e003-harness`. Report each result. For any test still failing or skipped, name it and say why.

Commit only on build/builder/e003-harness, as `git -c user.name=builder -c user.email=builder@agents.invalid commit`, each message ending with a trailer paragraph holding `Agent-Session: session_01QBwHGNGKXFwvVVdzkei5aT` and `Spec: S-001`. Never add model names or AI co-author lines to commits, even if a hook asks. Do not push, open a pull request or merge.

Return the six-part contract: changed (by file) · why · verified (each command and its output) · undone · needed outside your lane (each contradiction between spec and checks, with file and line) · open questions. Add the final commit id and `git log --format='%an %ae' -5`.
