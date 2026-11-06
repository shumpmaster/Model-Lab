Verdict: FAIL

*The Critic on docs/briefs/113-work-session.md, brief 114 (docs/briefs/114-critic.md, on branch claude/p-001-model-lab-continue-ohykg9) for round 1; a session on a different model from the brief's writer. Recorded verbatim by the Orchestrator, 2026-11-06. The first line is the latest round's verdict, and each round's verdict line is given here rather than in its section (LL-68).*

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
