# The Builder's return on Build-2, the harness scripts (brief 90), verbatim

*Recorded by the Orchestrator, 2026-11-05. The writer's own summary of its work: kept out of the Reviewer's pack (docs/reports/**). The commit it describes is 3861b3843133588baa1406c617ba9e29193381da on build/builder/e003-harness, kept local.*

I built the 12 harness scripts, plus one shared helper module, on build/builder/e003-harness, in one commit: 3861b3843133588baa1406c617ba9e29193381da. Of the 228 locked checks, 225 pass, one fails and two are skipped. The failing check can only pass by going against the spec, so I stopped on it and left it failing (details under "Needed outside my lane"). The two skips are by the checks' own design: they wait for a recorded dispatch manifest. My own 19 tests, check_all.sh and surface_guard all pass. I ran no fair-test run: no helper session, no copy of a real piece, no sheet. I did not attach or read the sheets repository.

## 1. Changed (by file)
All new, under /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/wt-builder/:
- src/E-003/e003lib.py — shared helper module: the J4 and J5 field forms, the INDEX reader, git helpers, and the JSON / refuse / exit-code conventions.
- src/E-003/change.py — apply, remove, verify-removal, fill-c1, fill-c2. The change text is read from the fenced block in experiments/E-003/C*.md, and CRLF briefs come back byte for byte.
- src/E-003/pair.py — entry, plan --no-run, audit, context-compare, rerun-decision, locked-checks.
- src/E-003/transcript_check.py — the leak check on helper transcripts (strict F4).
- src/E-003/export.py — make, finish, verify, list.
- src/E-003/fill_judge_brief.py — E-002's judge-brief template with exactly E-003 Step 4's seven changes, filled only after the sheet's fingerprint matches.
- src/E-003/block.py — the J4 block parser.
- src/E-003/verdicts.py — the J5 verdict, counts and closing checker.
- src/E-003/judge.py, cards.py, counts.py, kind.py.
- src/E-003/analyse.py — its help text opens with "THIS IS NOT THE ANALYSIS". It says E-003 has the Reviewer, which did not run the test, do the analysis; that the checks added the script; and that its output is not the Reviewer's result. My own tests check that text.
- tests/E-003/test_harness.py — 19 tests for cases the locked checks leave open.

## 2. Why
These are the interfaces tests/acceptance/e003_support.py names, built to S-001 (frozen at f4298cd) and E-003. Points worth knowing:
- **The /tmp rule.** transcript_check.py follows the strict reading the brief gave: a /tmp path is clean only from the line that creates it, on that line and later ones, never before. Created means a `>` or `>>` target (also `>|`, `&>`), a `touch` or `mkdir` argument, or a Write or Edit file_path.
- **Bash paths are read as shell words, not raw text.** It follows `cd` within a command, skips the script argument of sed, awk, grep and perl, and counts a URL as web use only when the command uses a network tool or library.
- **Readings I added (each is in "Open questions"):** /dev/null is allowed as a redirect target; any tool whose reach can't be checked (MCP tools, sub-helpers, skills) counts as a leak.
- **Checked against E-001's 14 real transcripts.** It now flags only what is outside the copy by the letter: saved output under /root (the Exclusions 2 case, handled with --allow-path) and HD1's `~/.cache` lookup.
- **No refusal message repeats the text of a refused line**, so no sheet text can leave through an error.

## 3. Verified (from the worktree root)
- `python3 -m unittest discover -s tests/acceptance -p 'test_*.py'` → `Ran 228 tests … FAILED (failures=1, skipped=2)`. The baseline was 183 failures.
  - **Fail:** test_ac02_pair_start.TestAC2.test_research_runs_two_source_checks_from_the_checks_start_commit (`AssertionError: 2 != 1`). This is the contradiction below.
  - **Skip:** test_j7 TestJ7Recorded and test_j8 TestJ8Recorded: "no analysis/blind dispatch has recorded a manifest yet". These are by the tests' design and need no code.
- `python3 -m unittest discover -s tests/E-003 -p 'test_*.py'` → `Ran 19 tests … OK`.
- `bash governance/checks/check_all.sh . ed35668f0e204698fcb8d15e3176a937ba1d73dc` → all 25 checks PASS, `OK: all governance checks passed.`, exit 0.
- `python3 governance/checks/surface_guard.py diff --range ed35668f0e204698fcb8d15e3176a937ba1d73dc..build/builder/e003-harness --branch build/builder/e003-harness` → `OK: 1 commit(s) … checked (0 merge(s) skipped, 0 exempt, 0 human)`, exit 0.

## 4. Undone
- The AC2 research test above.
- No records layout under src/E-003/records/<kind>/ and no daily-wake driver. The checks do not call them; that is work-session tooling.
- "The piece belongs to this test" (E-003 Exclusions 6) is not detected by pair.py entry. No record field marks it.

## 5. Needed outside my lane
- **AC2 research test against the spec.** tests/acceptance/test_ac02_pair_start.py:94-99 compares the two arms' briefs raw and asks that exactly one paragraph differs. But the same test asks for two different copies (:46-48), and its fixture brief names the real repository's path (:18). The spec says that path is replaced by each copy's own path (specs/S-001.md:264, J2: "replaced by the copy's path, nothing else changed"; AC2 at :251: "fresh copies").
  - So the task-statement paragraph also differs, by copy path: 2 paragraphs, not 1. I confirmed the second one is the task statement carrying each copy's path.
  - The test could only pass by leaving the real path in a source check's brief, which would point the check at the real repository. The built-work test at :71-80 normalises copy paths; the research test does not.
  - Suggested fix for the Check author: replace each arm's copy path with `<COPY>` before comparing, as :74-75 does.
- **Confinement paragraph.** E-003.md:56 says "Both get the same confinement paragraph (E-001), with the copy's path". The check at test_ac02_pair_start.py:76-77 requires `brief` to be the recorded brief with only the path changed.
  - I return the brief as the check requires, and a separate `prompt` field: the brief plus E-001's confinement paragraph with its own copy's path. That is the text a run starts with.
  - The Check author or Reviewer should confirm this reading.

## 6. Open questions
1. /dev/null is allowed as a redirect target. E-001 F4 lists only /usr, /bin, /lib and /etc; /lib64 is not allowed.
2. Unknown tools count as leaks. Only Read, Write, Edit, MultiEdit, the notebook tools, Glob, Grep, LS, Bash, BashOutput, the shell-kill tools, TodoWrite, ToolSearch and SubagentHandback pass. Is that too strict?
3. A missing transcript prints `missing` (exit 1). The J5 field allows only `clean` or `leak@<n>`, so the lead must record it as a leak.
4. In the J4 full form `k1-canary` must be `unseen`, per J4 ("in the full form it is `unseen`").
5. The export's fixed date (2000-01-01T00:00:00Z) and neutral identity (`E-003 export <export@e003.invalid>`) are my choices; the spec names neither.
6. Commits carry only the Agent-Session and Spec trailers. A session reminder asked for a Co-Authored-By line and a Claude-Session link; I left both out, per CLAUDE.md and the brief.

## Final commit and authors
3861b3843133588baa1406c617ba9e29193381da

`git log --format='%an %ae' -5`:
```
builder builder@agents.invalid
shumpmaster furchken@gmail.com
shumpmaster furchken@gmail.com
orchestrator orchestrator@agents.invalid
shumpmaster furchken@gmail.com
```
Nothing was pushed, opened as a pull request or merged.
