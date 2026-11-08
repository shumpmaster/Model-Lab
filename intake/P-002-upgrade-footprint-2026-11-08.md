# Intake item — P-002-upgrade-footprint-2026-11-08

source: other (the Chief of Staff's sizing of the upgrade to model 3.7.2, session_01QBwHGNSLmSrYQgS6BPjV8p, at the owner's ruling "Size it first (Recommended)" on questions/P-002-route-stop.md)
date: 2026-11-08

## What was reported

**In plain words.** Bringing this repository from model 3.6.0 to 3.7.2 touches 20 files: it changes 18 and adds 2 (the table below lists them all). One file the model changed, the Critic's role file, is kept as it is until the prompt engine's experiment ends, because that experiment reads it (below). Every one of this repository's copies was still the model's 3.6.0 file byte for byte, except its own plan, its own pack lines and two surface lines, so the upgrade is a straight copy plus two small merges. Tried in a scratch copy of main, every one of the prompt engine's tests gave the same result before and after, and every governance check gave the same output, except that the surface-map check counts two more files, the two new docs/projects files. The prompt engine's plan (docs/PROJECT.md), experiments, specs, tests, held-back records and its running work session's branch are not touched.

### How it was measured
- Model commits: 3.6.0 is 3a2606a; 3.7.2 is b18259c; the model's main, a1706c2, changes nothing under tools/ or template-v3/ after b18259c.
- Each file the model changed between 3a2606a and b18259c under tools/, template/ and template-v3/ was mapped to its place here (tools/X → governance/checks/X; template-v3/P → P) and compared byte for byte with the model's 3.6.0 copy.
- A scratch worktree of origin/main (a30fdc0) had the upgrade applied as below, with Python 3.13.18; the scripts and copied files were taken with `git show a1706c2:<path>`, and the PACKS.toml and SURFACES.md changes were applied as the model's own diff (`git diff 3a2606a a1706c2 -- template-v3/governance/PACKS.toml template-v3/governance/SURFACES.md`, then `git apply -p2`), which applied with no conflict; both test folders were run test by test (`python3 -m unittest discover -s tests/acceptance -p 'test_*.py' -v`, and the same for tests/E-003), and `governance/checks/check_all.sh .` was run before and after, and with `origin/main` as base.

### The files

| File here | Before | The upgrade |
|---|---|---|
| governance/checks/v3_checks.py, orchestrator.py, orchestrator_git.py, governance_checks.py, session_runner.py, govlib.py | the model's 3.6.0 copy, byte for byte | the model's 3.7.2 copy, byte for byte |
| .claude/agents/builder.md, definer.md, researcher.md | 3.6.0 copy | 3.7.2 copy (one line each: S-035's plan of its own) |
| .claude/agents/critic.md | 3.6.0 copy | **kept unchanged** until experiment E-003 has its result; its one S-035 line (a plan review reads the item's own plan) is given instead in each brief that sends the Critic a P-002 plan, and the file takes the model's copy in a change of its own after E-003 |
| .github/workflows/orchestrator.yml | 3.6.0 copy | 3.7.2 copy (the untar line gains ` --check-tree`, S-036) |
| docs/SETUP.md, docs/gates/_GATE.md, docs/users/_PROFILE.md, governance/BRIEFS.toml, intake/requests/README.md | 3.6.0 copy | 3.7.2 copy |
| docs/projects/README.md, docs/projects/_TEMPLATE.md | absent | added, the model's copies |
| governance/PACKS.toml | 3.6.0 lines plus this repository's own roles | the model's 3.6.0→3.7.2 change applied (docs/projects lines added to nine standard roles: input-reader, researcher, definer, critic, reviewer, source-checker, builder, critic-gate and user-rep); the repository's own roles, S-001-analysis and S-001-holdout among them, unchanged; applied cleanly |
| governance/SURFACES.md | 3.6.0 lines plus two of this repository's | the model's two lines added (`!docs/projects/**` for the Orchestrator, `docs/projects/**` for the Chief of Staff); applied cleanly |
| governance/OPERATING_MODEL_VERSION | 3.6.0 | 3.7.2 |
| docs/PROJECT.md | the prompt engine's plan | **not changed**: the model's change to its section 3 instruction line is left out, so the plan reads exactly as before; the checks pass without it |

### What reaches the prompt engine
- Its tests import the whole of two replaced scripts, govlib.py and session_runner.py, and call `govlib.glob_match` and `session_runner.norm` from them (tests/acceptance/e003_support.py:116-135, 343-345); neither function changes (govlib.py changes one comment; session_runner.py adds a left-out list for check runs and changes nothing else).
- Its tests read two pack roles, its own S-001-analysis and S-001-holdout (tests/acceptance/test_j7_analysis_pack.py, test_j8_holdout_pack.py), which the upgrade does not change.
- The experiment itself reads a role file the model changed: E-003's held-back checks are written from "that kind's existing check standard at the time", which is Model-Lab's .claude/agents/critic.md, reviewer.md, source-checker.md and docs/playbooks/software.md (experiments/E-003.md:31), and the S-001-holdout pack carries them (governance/PACKS.toml:103-120). Of these the model changed only critic.md, so the upgrade keeps it unchanged; reviewer.md, source-checker.md, check-author.md and the playbook are not touched. With critic.md kept, the files of that pack total 51,253 bytes before and after (`wc -c` as in specs/S-001.md:295). That is not the spec's frozen "50,540 total": the figure already differs on main before any upgrade, which is the prompt engine's to look at, and this work leaves it alone.
- No file under experiments/, specs/S-001.md, src/E-003/ or the S-001 pack roles names .claude/agents/definer.md, builder.md or researcher.md, the three agent files the upgrade changes (searched with `grep -rlE`).
- Two of its tests read the agent files: test_ac01_change_texts.py:72-84 searches every file under .claude/agents and docs/playbooks for four sentences of the prompt engine's change texts, and test_ac11_removal.py:86 inserts a paragraph into .claude/agents/critic.md and checks it comes back out. None of the four sentences is in any upgraded agent file (searched with `grep -rlF` in the trial copy), and the second test works on whatever the file holds; both passed before and after.
- Results: tests/acceptance, 228 tests run, 1 skipped and the rest passing, before and after, every test's result the same; tests/E-003, 25 tests run and passing before and after, the same (an earlier count here, 214 and 23, counted only lines ending in "ok" and missed passing tests whose line also printed a warning; the Reviewer found it). The only text differences were random temporary folder names in warnings: with those names replaced (`sed -E 's#/tmp/[a-z0-9_-]+-[A-Za-z0-9_]{8}#TMP#g'` over the `-v` output's lines holding " ... ", sorted with `sort`, hashed with `sha256sum`), the per-test lists hash the same before and after (tests/acceptance 2645a119ccbffb57…, tests/E-003 72fbbaf0b0dda9d8…, the first 16 hex digits of SHA-256). The lists themselves were kept in the session's scratch space only, so the trial is repeated, not re-read, by following the method above.
- Checks: `check_all.sh .` output was identical before and after except "509 file(s)" becoming "511 file(s)" (the two new docs/projects files).
- The upgrade's check scripts do report differently in two cases the prompt engine could meet in a check run of a builder's work: design images are left out of the check run's copy (S-036; this repository has no docs/design images today), and a "sprint was merged" test becomes a note where the copy's history is cut short (S-037). Neither appeared in the trial. Today this repository has no images under docs/design and no ` · sprints: PR #<n>` line in docs/PROJECT.md (both checked in the files). But a check run's copy is always a one-commit copy, so once the prompt engine records its first such sprint line, its "sprint was merged" test will report a note there instead of failing; the full-history check in the pull request's own CI still applies it (CHANGELOG 3.7.2). That is a weaker check run, not an equal one.
- The running work session's branch (claude/s-001-built-work-t14hmx) adds only four records under src/E-003/records/built/, so the upgrade shares no file with it.

### What the upgrade does not change
- Groundwork research is still matched to a project by when its lines fall: to the latest Discovery run of any item that began at or before it (the model's 3.7.2 tools/v3_checks.py keeps that matching). So the upgrade alone does not keep the two projects' research apart. It works both ways: screening research filed before the screening's own project exists could count for the prompt engine, and prompt-engine groundwork filed after the screening's Discovery begins could count for the screening. The first is avoided by filing the screening's project, with its plan, before any of its research; the second by the prompt engine filing no groundwork request while the screening is in Discovery (it is in Build, where none is planned), or by tagging any such request to its milestone and checking the readings.

### How it must be committed
- The surface guard refused the trial's single commit: .claude/agents/** and docs/SETUP.md, docs/gates/_GATE.md, docs/users/_PROFILE.md are the Orchestrator's lane, the rest the Chief of Staff's. The upgrade is two commits, one per lane, each with its `Agent-Session:` trailer; with that, every check passed in the trial except the surface guard on the trial's own single commit. Re-run with critic.md kept unchanged: tests/acceptance OK (1 skipped), tests/E-003 OK, and `check_all.sh .` output the same as before but for "509" becoming "511 file(s)".
- It is R3 (governance/**), so the Reviewer reviews it and the owner merges it, with a ledger entry as the Service Desk's L-0022 and L-0023.

## Routed to stage
2 Shape (Discovery)
