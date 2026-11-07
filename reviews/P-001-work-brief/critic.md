Verdict: PASS

*The Critic on docs/briefs/113-work-session.md, brief 114 (docs/briefs/114-critic.md, on branch claude/p-001-model-lab-continue-ohykg9) for round 1, brief 115 for round 2 and brief 116 for round 3; a session on a different model from the brief's writer, resumed for rounds 2 and 3. Recorded verbatim by the Orchestrator, 2026-11-06. The first line is the latest round's verdict; rounds 1 and 2 were FAIL, and each round's verdict line is given here rather than in its section (LL-68).*

## Round 1 (commit 78cdfec)

I read the brief (/tmp/claude-0/-home-user/9a06fe22-60e0-580d-8926-30c8a46558b9/scratchpad/fix-work/docs/briefs/113-work-session.md) against S-001, E-003, the src/E-003 scripts, AGENTS.md, the CLAUDE.md files, and briefs 109 and 110. I ran no scripts. Three findings block it: one lets pieces enter that the spec excludes, and two make a step impossible to carry out as written or put arm output at risk. The rest is mostly sound.

Step order matches the spec: K1 listing and probe, seed, wake, every-turn K5/K6/K7, scan, pair, export, records. The commands I checked match the scripts' flags: kind.py can-open, counts.py may-start and record-ruling, pair.py entry/plan/audit/locked-checks, export.py make/verify/finish, and transcript_check.py with repeated `--sheets-repo`. The commit, trailer and no-co-author rules match Model-Lab's CLAUDE.md. The wake message is word for word S-001's. The model line for builders (claude-opus-5-5) is supported by briefs 90, 92, 97 and 103. counts.json's four keys match counts.py `card` exactly. LL-66 exists.

### Blocking

1. **Nothing excludes pieces dispatched before the kind opened.**
   - E-003 Step 2 (first bullet) and AC2 admit only pieces dispatched after the comparison opens.
   - The brief's step 6 only says to start no pair before the kind is open. Step 7's first scan covers all history, and `pair.py entry` has no opening-time check.
   - Model-Lab records 90, 92, 97 and 103 already carry `start:` and `recorded: at hand-out`, dated 2026-11-05 and 06. They would pass `entry` and sit inside the 7 days. Only the unmarked "names S-001/E-003" rule stops them, and it would not stop any other pre-open record.
   - Fix: add an explicit rule. A record whose dispatch is before the kind's recorded opening time is `not-eligible: dispatched before the kind opened`, and a piece listed eligible before opening is not started afterwards.
   - The brief also never says where the opening time is recorded (see non-blocking 10).

2. **The `plan` step cannot run for briefs that name an absolute path, and its fallback loops.**
   - `pair.py plan` refuses with a set-up fault when a brief names an absolute path outside the copy. The only fix is a `real_path` in the saved entry, and `pair.py entry` never adds one.
   - Model-Lab builder briefs do name such paths (90 and 103 name /tmp/claude-0/... worktrees).
   - Step 8 says to save the `entry` object as it is, and to treat a refusal as a set-up fault under Reruns (b). A rerun cannot cure a missing `real_path`.
   - Fix: say when to add `real_path` (the real clone's path, `/home/user/<repo>` or the path the brief names; J2 allows replacing it with the copy's path). Say that a refusal still unsolved by that is listed, not rerun.

3. **A held pair keeps its arms' only output on a reclaimable machine.**
   - Two holds are written: the audit hold, until the round-1 submission is on record, and the "task names no spec" hold, until the Orchestrator's weekly landing.
   - A held pair's final trees exist only in `/home/user/e003-copies`. S-001 K5 and the brief's own last sentence of "Commits" say the machine may be reclaimed between turns and nothing may rest on it.
   - A reclaim during a hold loses the deliverables, and the lost arms could not be told apart from "no deliverable = FAIL" (Exclusions 4).
   - Fix: say what is saved and pushed before the turn ends for a held pair (for example the committed final-tree commit ids and a private bundle). Say that a lost copy is a set-up fault listed as such, never an arm FAIL.

### Non-blocking

4. **`context-compare` has inputs the brief does not supply.**
   - The `--change-text` file must hold the filled change paragraph. `plan` output gives only `fill` and the two briefs, and the brief names no file.
   - `--path-a` and `--path-b` are also unsaid. A wrong paragraph makes every pair read "differs" and spends the reserve.
   - Fix: give the recipe, for example the paragraph from `change.py apply` or the diff of the two briefs.

5. **`rerun-decision --history` has no stated form.**
   - It wants a JSON list of `{"event": ...}` using the names in the code (`set-up-fault`, `context-differs`, `in-flight-inputs`, `leak`, `arms-finished`, `completed`). The docstring does not list them.
   - The brief also never says how a rerun is run or counted: new copies by `plan`, two more runs from the reserve, and the first runs' tokens still counted.
   - A "model has no alias" case is called a set-up fault, but a rerun cannot cure it. It should be listed, not run.

6. **Unmarked readings that should carry "the Orchestrator's reading".**
   - Excluding any record that names S-001, E-003 or this test is broader than E-003 Step 2's "part of this test". It is the stricter reading, so keep it, but mark it.
   - Holding a pair until the audit is a reading of "before judging", also stricter.
   - The model rule is a second unmarked reading. E-003 Step 3 says "the model the operating model uses for that role when the kind opens", while the brief and `pair.py` use the entry's recorded model. J2 and AC2 support the entry's model, so this one is fine if marked.
   - The "unrun" handling for non-Python locked files is already marked.

7. **`create_trigger` justification.**
   - The parenthetical "(the owner's brief asks for it)" for `initiation: human_request` is not true of the owner's message.
   - The intake record (:39) does not mention that parameter either.
   - The "13:00 to 17:00 UTC" window rests on no record I found.
   - Fix: drop or source both.

8. **Locked-check command.**
   - `python3 -m unittest discover` assumes unittest-style files. On Python 3.12 or later, zero tests run exits 5 (my recollection of Python's behaviour; not checked here), which would read as a failure for both arms.
   - Fix: treat "no tests ran" as `locked: unrun`, not a pass or fail.
   - Check that C2's list items under tests/ or checks/ carry no `:a-b` range. `fill_c2` adds only whole paths for locked files, so this holds. Strip the range from the spec item only.

9. **Records you listed are incomplete or collide.**
   - The K1 listing's line form is unspecified. Brief 110 step 6 requires every `k1-` part line to read `refused`. A listing line named `k1-…` would make the sheet lead stop. Give it a form that does not start `k1-` (for example `listing:`).
   - Measure in E-003 reports each pair's real round-1 verdict. `pairs/<n>.json` has no field for it, and nobody is named to supply it.

10. **Gaps in where things come from.**
    - **Opening time:** "recorded once" names no file. Put it in `session-<id>.md` or `seed.md`.
    - **Default-branch files:** `can-open` and `may-start` run "on the default branch's files", but the branch must not be merged into. Say how to read them, for example `git show origin/<default>:path` into a scratch folder.
    - **rulings.md:** `reviews/E-003/built/rulings.md` is named nowhere else in the repo. Say the Orchestrator creates it in `counts.py record-ruling`'s tab-separated form `date<TAB>kind<TAB>ruling`.
    - **may-start:** say that `--started` is runs already started, so the pair's second run is checked with `started+1`.
    - **Audit arguments:** give `--repo` (the real clone). `--default-branch` defaults to `main`, so check each repo's actual default. Say where the "round-1 check's record" is found for Service-Desk and Model-Lab pieces.
    - **Early check:** run `change.py verify-removal` before starting the arms. It catches a brief that differs beyond the change text, a set-up fault, at zero run cost.
    - **Record time:** `entry` is never passed `--round-1-verdict-at` or `--dispatched-at`. A record that reaches the default branch after its round-1 verdict is not detected. Say whether to apply such a check from the record's commit date.
    - **Hook:** it is "once per session", but a reclaimed machine may lose it. Re-add it if absent at each turn.

11. **"Never name secret-marking except in K1's probe"** conflicts with step 8's `transcript_check --sheets-repo secret-marking`, and with the K1 record lines. Add the exception.

12. **K1 extra runs.** S-001 also requires the probe "before every analysis dispatch". The brief has no way to receive that ask. Say the owner or Orchestrator may request it and it runs the after-form.

13. **Checkpoint and `list_events` readings.** The checkpoint reading ("only the judging lead pauses") is consistent with `counts.py may-start`, which stops only on a recorded "stop". It is needed, and it is the milder reading, so the owner should know. The `k1-iii: refused … not held` reading is needed because brief 110 requires "refused", and is marked.

### Six-part contract

- **changed:** none (read-only critique; no files written).
- **why:** check brief 113 against S-001, E-003, the harness scripts, AGENTS.md, CLAUDE.md, and briefs 109 and 110.
- **verified:** read the brief, the spec (sessions, K1 to K7, AC2, AC3, J1 to J5), E-003 Steps 2 and 3, Sample and Exclusions, the docstrings and code of pair.py, change.py, kind.py, counts.py, export.py and transcript_check.py, briefs 90, 92, 97, 103 and 110, and the E-001 hook text. I ran no scripts.
- **undone:** no script run (Orchestrator's runs trusted). I did not read judge.py, block.py or the rest of export.py and transcript_check.py. I did not check Service-Desk control-file contents beyond their location, and did not confirm the default-branch names.
- **needed outside my surface:** Orchestrator to fix blocking items 1 to 3 in the brief and answer 10's file and branch questions.
- **open questions:** (a) Should a held pair's arm output be bundled and pushed before the audit, or held unpushed and treated as a set-up fault if lost? (b) Is the Orchestrator's hand-out the intended source of `real_path`?

## Round 2 (commit 7cc5c73)

Round 2 on docs/briefs/113-work-session.md (fix-work2). Most round 1 findings are answered. Three new or changed sentences are wrong or unrunnable as written, and I mark them blocking. I ran no scripts. I judged the Orchestrator's runs against the code: the export clone/re-make against export.py (the bundle holds tag `start` and branch `<label>`, so `--start start --final <label>` resolves in a clone), `entry --round-1-verdict-at` against pair.py lines 183-186, `change.filled` against change.py, and exit 5 against the Orchestrator's report.

### Round 1 findings: status
1. **Pieces dispatched before the kind opened:** answered. Step 7 gives `not-eligible: dispatched before the kind opened`, and `opened.md` gives the opening time. See findings 4 and 5 for flaws in how the opening time is fixed and compared.
2. **`real_path`:** answered in step 8, with "listed, not rerun" for a refusal it does not cure.
3. **Held pair's output on a reclaimable machine:** answered by held exports pushed in `records/built/held/<n>`, with "a held export lost is a set-up fault, never an arm's FAIL". It has a hole (finding 3).
4. **Context-compare inputs:** answered. The change-paragraph recipe is correct for `context-compare` (it strips `\r\n`), and the two copy paths are given.
5. **Rerun history events and how a rerun is run and counted:** answered. A "no alias for the model" case is now listed, not rerun.
6. **Unmarked readings:** now marked (the S-001/E-003 name rule, the model rule, the hold).
7. **Unsupported wake time and "owner's brief asks":** removed. `initiation: human_request` is kept without a source (finding 7).
8. **Locked-check command:** answered. `NO TESTS RAN` (exit 5) is now `locked: unrun`, which matches the Orchestrator's run; in a `&&` chain exit 5 stops the chain, which reads as unrun.
9. **Listing line and real round-1 verdict:** answered. The `listing:` line avoids the `k1-` prefix, so brief 110 step 6 will not trip on it. The `pairs/<n>.json` list now holds the real round-1 submission and verdict and their record.
10. **Gaps in where things come from:** answered, except the `--default-branch` argument (finding 1) and the `--now` reuse (finding 2).
11. **Naming secret-marking:** answered by the added exception.
12. **K1 on request:** answered ("whenever the owner asks").
13. n/a.

### Blocking
1. **The audit reads a stale branch.**
   - Step 9 passes `--default-branch main` to `pair.py audit`, but the whole brief reads `origin/main` and says never to merge into the branch.
   - `audit` resolves `main` in `/home/user/<repo>`. That is the local branch. In Service-Desk it is the clone-time checkout, and `git fetch` does not advance it. In Model-Lab it may be absent.
   - Round-1 verdicts arrive after the clone, so the in-flight check (Exclusions 1) would read old history and wrongly include pairs.
   - Fix: pass `--default-branch origin/main`. `rev-list` accepts it.
   - The scan's "each repository's main" should also read `origin/main`.
2. **"Run `entry` again" with the wrong time silently drops valid pairs.**
   - Step 9 runs `entry` again with `--round-1-verdict-at`, but does not say which `--now`.
   - `cmd_entry` still applies `now - dispatched_at > 7 days` (pair.py line 187). A round-1 verdict usually lands days after dispatch, so using the current time gives `first found more than 7 days after its dispatch (late)` for a pair that started in time.
   - Fix: say to reuse the `--now` of the scan that found the record (found-at in `scan.tsv`).
3. **A pair whose task names no spec cannot be held.**
   - Step 9 makes the held export first, with `--task-statement-path <the spec C2's list names first>`. export.py requires that flag for built work.
   - With no spec there is no value, so `make` cannot run. The brief says "The copies may then go", and Release says "the pair stays held".
   - The eligible piece's deliverable would be gone before the Orchestrator rules.
   - Fix: state what path the held export takes for a no-spec task (for example the first path of C2's list, recorded as provisional), or keep the copies' committed trees pushed another way. Also say that a pair left out (leak, or `rerun-decision` says leave-out) gets no export at all.

### Non-blocking
4. **The opening time is looser than round 1's.**
   - Step 6 now uses the first commit that holds `reviews/E-003/built/sheet.md`. A void or stopped block recorded earlier, then replaced by a full block, would give too early an opening and admit pieces dispatched while no check existed.
   - It should also be the commit where HOLDOUTS.md holds the line, since `can-open` needs both.
   - Fix: use the first commit at which `can-open` returns eligible, found by testing along `git log --reverse`, as round 1's wording did. Or use the last commit that changed sheet.md or HOLDOUTS.md before eligibility.
5. **Dispatch-versus-opening comparison is undefined.**
   - Model-Lab records carry a date only. The opening time has a time.
   - Say to compare dates and treat the opening day itself as not eligible (the stricter reading), and mark it.
6. **The never-list lost two prohibitions.** "Never merge, push to or open a pull request in any repository other than your push branch" is now only "never push to any branch but...". Restore the no-merge and no-pull-request words.
7. **`initiation: human_request` has no source in the records I found.** The intake (:39) does not mention it. It is acceptable if the tool's own description requires it. Say so.
8. **Fill in a shell argument.** The one-line `change.filled` command passes `'<the plan's fill>'` in single quotes. A fill containing an apostrophe breaks it. Read the fill from `plan`'s output file instead.
9. **Service-Desk round-1 record.** "The round-1 verdict file under reviews/<item>/" is vague; I saw `reviews/Q-016/critic.md`. Name the builder's review file (probably `reviewer.md`) once known.

### Six-part contract
- **changed:** none (read-only critique).
- **why:** check round 2 of brief 113 against round 1's findings, the spec, and the script code and the Orchestrator's reported runs.
- **verified:** read both briefs and my round 1 record, export.py (lines 1-47, 91-136, 206), pair.py `entry`/`plan`/`audit`, change.py, and the Service-Desk review layout; judged the reported unittest exit 5, `entry --round-1-verdict-at`, and the export/clone/re-make results against the code.
- **undone:** no script run by me; I did not read export.py `cmd_make` past line 136; I did not check whether `git clone` of a bundle keeps tag `start` beyond the Orchestrator's report; I did not confirm the builder review filename in Service-Desk.
- **needed outside my surface:** Orchestrator to fix findings 1 to 3 in the brief and decide on 4 to 9.
- **open questions:** (a) For a no-spec task, which path should the held export use, and who rules? (b) Should the opening time use the first or last sheet.md/HOLDOUTS commit?

## Round 3 (commit 3260c00)

Round 3 on docs/briefs/113-work-session.md (fix-work3 against fix-work2). All three round 2 blocking findings are answered. The two sentences I could not source are marked below. I ran no scripts; I judged the Orchestrator's runs against the code.

### Round 2 findings: status
1. **Audit read a stale branch (blocking):** answered. Step 9 now passes `--default-branch origin/main`, after a `git fetch` in that clone. `cmd_audit` hands the name to `git rev-list ... --before=<t> <branch>` and `git log`, so `origin/main` resolves; the Orchestrator's run agrees. The scan also now reads `origin/main`.
2. **`entry` re-run used the wrong time (blocking):** answered. Step 9 says to use `--now` as the found-at time from the pair's `scan.tsv` line, so the 7-day test (pair.py line 187) is applied at scan time. `--round-1-verdict-at` is the committer date of the verdict record's first commit on `origin/main`, which pair.py lines 183-186 use as written.
3. **A no-spec task could not be held (blocking):** answered. The held export takes the first path of C2's list, recorded as provisional. At release the Orchestrator rules the task statement's path and the export is re-made with it. The bundle is unchanged and only the fill file's path differs, which fits export.py (`--task-statement-path` goes only into `<label>.fill.json`). A pair left out by a leak or by `rerun-decision` now gets no export at all.
4. **Opening time looser than round 1 (non-blocking):** answered. Step 6 now finds the first commit of `git log --reverse ... origin/main -- reviews/E-003/built/sheet.md governance/HOLDOUTS.md` at which `can-open` is eligible, testing each commit's two files in turn. This is the same definition as kind.py's.
5. **Date-only dispatch against opening time:** answered. A date-only record counts as dispatched at its day's start, so a record of the opening day is not eligible. It is marked as the stricter Orchestrator's reading.
6. **The never-list lost two prohibitions:** answered ("never merge, push to or open a pull request on any branch but your Model-Lab push branch").
7. **`initiation: human_request` had no source:** partly answered. It now carries a reason ("since the owner started this session with this brief to set it up"). See non-blocking 1.
8. **Apostrophe in the fill:** answered. The `change.filled` command reads the fill from the saved plan file as JSON, and the `$(...)` form passes the fill to `verify-removal` whole. The Orchestrator ran both on an apostrophe-bearing fill. `$(...)` does not re-expand its output, so quotes, `$` and backticks in the fill stay literal.
9. **Service-Desk review file:** answered. Step 9 names `reviews/<pull request>/reviewer.md` for both repositories, which the coordinator confirmed.

### Non-blocking
1. `initiation: human_request` is justified by "its description asks for", which I cannot check against any record; the intake (:39) does not mention the parameter. It is acceptable if the tool's own description requires it, and the lead can see that description.
2. The nested double quotes in the `verify-removal` command work in bash only. The brief assumes bash, so this is fine, but the lead should run it as written and not in another shell.
3. Step 6's opening time calls `can-open` at each commit "on that commit's two files". At an early commit where one file does not exist, use a path that does not exist, as step 3 does.
4. Labels are drawn "as soon as the arms are checked", even for a pair later left out. That wastes no run, but the drawn labels of a left-out pair should be recorded or the pair number kept, so the draw order stays stable.

### Six-part contract
- **changed:** none (read-only critique).
- **why:** check round 3 of brief 113 against my round 2 findings, the spec, the cited records and the scripts' code.
- **verified:** read the round 3 brief and my earlier records; compared them with round 2; checked audit/entry/export/kind logic in the code I read in rounds 1 and 2; took the Orchestrator's reported runs (audit with `origin/main`, the apostrophe fill) as consistent with the code.
- **undone:** I ran no script. I did not re-read the code paths for commands the brief did not change. I did not check the tool descriptions for `initiation`.
- **needed outside my surface:** none required to start; non-blocking items 1 to 4 are for the Orchestrator's judgement.
- **open questions:** none.
