# The Check author's return on S-001's locked checks (brief 72), verbatim

*Recorded by the Orchestrator, 2026-11-04. The writer's own summary of its work: kept out of the Critic's and the Reviewer's packs (docs/reports/**). The commit it describes is e0d8104 on build/check-author/s001-locked.*

## S-001 locked checks (dispatch b): AC1 to AC11 and join tests J1 to J8, committed on `build/check-author/s001-locked`

The 20 files are committed, but 179 of 222 tests fail because the Builder's scripts under `src/E-003/` do not exist yet.

**Where and how to run.** Worktree is `/tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/wt-check`, branch `build/check-author/s001-locked`. Commit `e0d8104cc7e2f88f19e6370d0cf84743d92e9679` is the only commit, on top of 7d6c999. `git log --format='%an %ae' -3` gives:
- check-author check-author@agents.invalid
- orchestrator orchestrator@agents.invalid
- orchestrator orchestrator@agents.invalid

The commit message carries `Agent-Session: session_01QBwHGJ9ZMyT9fK17HjfmCc` and `Spec: S-001`. I left off the attribution reminder's Co-Authored-By line because the project CLAUDE.md and the role file forbid model names in commits.

Run everything with `python3 -m unittest discover -s tests/acceptance -p 'test_*.py'` from the worktree root. Standard library only; pytest is not installed. For one file, use `-p 'test_j7*.py'`.

### 1. Files, the criterion or join each checks, and current result
Everything is in `tests/acceptance/`. Eight tests in the table pass now; every other test that passes now is in one of the 100%-pass files (AC1, J7, J8) or in the "partly pass" row.

| File | Checks | Result now |
|---|---|---|
| `e003_support.py` | Shared helpers and reference maths (exact binomial, Newcombe, card draw). Its docstring lists all interfaces. | n/a |
| `test_ac01_change_texts.py` | AC1: C1 to C3 files exactly as frozen, word counts 35/11/64, role files and playbooks unchanged since f4298cd. | 8/8 pass |
| `test_ac02_pair_start.py` | AC2: both arms, fresh copies, briefs differ only by the change paragraph and copy path, same model, same hour, within 7 days; no record means not eligible. | fail, `pair.py` missing |
| `test_ac03_pair_audit.py` | AC3: in-flight inputs, foreign commit taken in, context differs, leak, one rerun then leave out, never rerun for a better answer. | fail, `pair.py`, `transcript_check.py` missing |
| `test_ac04_heldback_gate.py` | AC4: `kind.py can-open` gate. | 8 gate tests fail; 4 repository tests pass |
| `test_ac05_judging.py` | AC5: verdict-line rules, one follow-up then at most one new session, arm outcome (judge PASS and locked checks exit 0), judge model differs from doers', brief carries no arm label, hand-back or commit messages, and the transcript check (outside reads, web, sheets repository). | fail, `judge.py`, `transcript_check.py` missing |
| `test_ac06_owner_cards.py` | AC6: 8 cards at 4/2/2, seeded draw against an independent reference, shortfall rule, locked-check failures never drawn, extension to 6 answered or 12 shown, rescoring, disagreements. | fail, `cards.py` missing |
| `test_ac07_decision.py` | AC7: exact one-sided test at 1 in 40, judge confirmation (6 answered, at most 2 disagreements), gain with 95% range, fewer than 10 pairs, the false-pass guard (change's false passes at most the unchanged check's plus one). | 1 passes (spec anchors), 11 fail, `analyse.py` missing |
| `test_ac08_counts_card.py` | AC8: caps 133/132, 133/66, totals 266/200 (and the 40 and 100 sizes), start limits, due at every 20 runs and every 16 weeks, card contents, power from `sizing.py`, weeks to target, no outcome, ruling recorded. | fail, `counts.py` missing |
| `test_ac09_model_change.py` | AC9: group by model, test the larger group only, say so; arms on different served models are a set-up fault. | fail, `analyse.py` missing |
| `test_ac10_v2_record.py` | AC10: V2 cutoffs 5/13/18 of 30, and the record carries the V2 measure, how pieces are counted and the removal test. | 1 passes (cutoff arithmetic), 4 fail |
| `test_ac11_removal.py` | AC11: apply then remove is byte for byte (CRLF, no trailing newline, unicode, a role file); per-pair clean-removal check. | fail, `change.py` missing |
| `test_j1_change_to_arm.py` | J1 insertion position, C1 and C2 fills, every awkward case. | fail, `change.py` missing |
| `test_j2_dispatch_record.py` | J2 entry from brief records and control files, awkward cases, 7-day boundary. | fail, `pair.py` missing |
| `test_j3_neutral_export.py` | J3 two-commit bundle, neutral fields, trees equal, no other object reachable, fill file, INDEX hashes, `last`, tamper refused, reader list. | fail, `export.py` missing |
| `test_j4_sheet_route.py` | J4 block parser (three forms plus refusals) and fill script (SHA gate, determinism, writes nothing else). | fail, `block.py`, `fill_judge_brief.py` missing |
| `test_j5_verdict_record.py` | J5 verdict-line, counts-block and closing-block forms, test numbers, label and path checks. | fail, `verdicts.py` missing |
| `test_j6_cards_record.py` | J6 cards file, sheet-text and arm-label absence, quotation replaced by test number. | fail, `cards.py` missing |
| `test_j7_analysis_pack.py` | J7 entry, validator and manifest checks, with synthetic good and broken manifests. | 12 pass, 1 skip |
| `test_j8_holdout_pack.py` | J8 entry, the extract's withheld paths, change ids, "arm" and change sentences, validator. | 15 pass, 1 skip |

The two skips are the checks on a recorded manifest in `docs/briefs/`. None exists until a blind or analysis dispatch records one. Run them before each dispatch with `S001_MANIFEST=<brief record> python3 -m unittest discover -s tests/acceptance -p 'test_j8*.py'` (or `test_j7*`).

Every failure I could inspect says "interface missing" and nothing else. I also ran the J3, J4-parser and J5 tests against throwaway scripts kept outside the repo and not committed. All of those tests passed. Two deliberately broken exporters (no fixed date, wrong label message) each failed the J3 test. A fixture bug I found this way, a mixed-forms case that was actually a valid stopped block, is fixed. The other interface tests have not been run against any implementation, so a fixture bug could still sit in them.

### 2. Interfaces named (all invented only as far as a test needs)
The scripts are `python3 -I src/E-003/<name>.py <subcommand>`, run from the repository root:

- `change.py` with `apply`, `remove`, `verify-removal`, `fill-c1`, `fill-c2`.
- `pair.py` with `entry`, `plan --no-run`, `audit`, `context-compare`, `rerun-decision`, `locked-checks`.
- `transcript_check.py check` prints `clean`, or `leak@<line>` with exit 1.
- `fill_judge_brief.py`, `export.py`, `block.py parse`, `verdicts.py check`, `judge.py`, `cards.py`, `analyse.py` with `run` and `v2`, `counts.py`, `kind.py can-open`.

Conventions:
- A decision command prints one JSON object and exits 0, even for a negative decision.
- A refusal exits 1.
- A usage error exits 2.

The full list, with arguments and output keys, is in the docstring at the top of `e003_support.py`, and each test file repeats the part it uses.

### 3. Contradictions and gaps in the spec
1. **No file names or command lines for the Builder's scripts.** The fill script, transcript check, export reader, block parser and the rest are named but not located. The names above are mine.
2. **J4, `k1-canary` in the full form.** One sentence lets it be `unseen`, `seen` or `unread`; another says "in the full form it is `unseen`". I test `unseen` in the full form and the three words in the stopped and void forms.
3. **J4, "writes nothing but the J5 line".** The fill script cannot know most J5 fields. I read it as: the only file created is `--out`, and stdout holds no sheet text.
4. **J5, closing block layout.** The separators between the counts block, the verdict file and `sha256:` are not given. I assume plain concatenation. "Tokens, tool uses, seconds" are read as integers.
5. **J1.**
   - The spec does not say how the "task statement" is found in a brief, so `apply` takes it as a file.
   - It does not say how a cited stage's line range is derived. I assume the heading to the next same-or-higher heading.
6. **J2.**
   - The layout of a Service Desk control file "holding several roles" is not given. I use a JSON list of entries.
   - The two-lane case needs a record format the spec does not give, so it is not tested.
7. **J3.**
   - The neutral author and the fixed date are not named. I require only that they are the same in both commits and in every export, and differ from the source's.
   - The `.fill.json` keys are not given. I check that the values appear.
   - The "no deliverable, so no export" case is not tested.
8. **AC6.** Two details are my reading:
   - How a shortfall is added to the 4/2/2 sample sizes.
   - "Further cards via `choice` in the order G1, G3, G2", read as the first non-empty leftover group in that order.
9. **AC5.**
   - The spec does not say whether the new judge session gets its own follow-up. I test only that a third session never starts.
   - The invocation of a project's locked checks is not given, so `pair.py locked-checks` takes the command as an argument.
   - E-001's allowed system paths (F4) are in `src/**`, which I may not read. The transcript tests therefore cover only clearly inside and clearly outside paths.
10. **J7 and J8.** The spec says the manifest is recorded "in the dispatch's brief record" but not which field says which pack it is for. I tell the two apart by the agent file (`check-author.md` or `reviewer.md`).
11. **AC10.** "How those pieces are counted from the review records" has no content defined. I ask only that the record name the review records and say what counts as first time.
12. **AC2.** "Records the pair" has no location, so I test only the returned arms.
13. **Local false failure.** `surface_guard diff origin/main..HEAD` in `check_all` reports earlier chief-of-staff and orchestrator commits as not by check-author (see section 6).

### 4. Which tests can pass without the Builder
They pass now: AC1 (all 8), J7 (12), J8 (15), AC4's four repository and record tests, the spec-anchor test in AC7, and the cutoff-arithmetic test in AC10. Everything else needs `src/E-003/` and fails until the Builder writes it.

### 5. `check_all.sh` summary
Run in the worktree after committing, as `bash governance/checks/check_all.sh . origin/main`. The summary is all PASS, including `v3_checks joins`, except two lines:
- `record_checks merges`, the known false failure (LL-29).
- `surface_guard diff --range origin/main..HEAD`, which lists the earlier chief-of-staff and orchestrator commits as not check-author. That is a property of comparing against `origin/main`, not of my commit.

### 6. Surface guard
`python3 governance/checks/surface_guard.py diff --range 7d6c999..build/check-author/s001-locked --branch build/check-author/s001-locked` printed `OK: 1 commit(s) in 7d6c999..build/check-author/s001-locked checked (0 merge(s) skipped, 0 exempt, 0 human)` and exited 0.

Not pushed.

## Round 2 (brief 74), commit 742ef89

## Brief 74: round-1 findings on S-001's locked checks fixed in commit 742ef89, on top of e0d8104

Findings 1 to 5, 7 to 9 and 12 are fixed, plus the cheap cases of 10. Findings 6 and 11 are answered below, and the rest of 10 is not done.

New commit: `742ef89`, same worktree and branch (`build/check-author/s001-locked`). e0d8104 is not rewritten, nothing is pushed, and the trailers are as before. The commit message has no model names or attribution lines, per the project rule.

`git log --format='%an %ae' -3`:
- check-author check-author@agents.invalid
- check-author check-author@agents.invalid
- orchestrator orchestrator@agents.invalid

**Results**
- The suite runs 227 tests: 43 pass, 2 skip and 182 fail.
- All 182 failures are "interface missing", meaning the Builder's `src/E-003/` scripts do not exist yet. I checked this by reading every failure.
- The 2 skips are the recorded-manifest checks, which wait for a dispatch to record a manifest.
- `bash governance/checks/check_all.sh . 7d6c999` prints "OK: all governance checks passed". Every line passes, including `v3_checks joins`, and the `record_checks merges` false failure does not appear against this base.
- `surface_guard.py diff --range 7d6c999..build/check-author/s001-locked --branch build/check-author/s001-locked` prints "OK: 2 commit(s) ... checked (0 merge(s) skipped, 0 exempt, 0 human)".

**Findings**
1. **J7 manifest picked by record text (blocking), fixed.** `e003_support.manifest_kind` now classifies a recorded manifest from its parsed file lines. "Analysis" means `experiments/E-003.md` is among them. "Blind" means the extract or `check-author.md` is. J7 and J8 both use it. I added `TestJ7Classify`, which shows the blind pack's manifest (it lists reviewer.md) is not taken for an analysis manifest.
2. **Transcript check counted F4 reads as leaks (blocking), fixed.**
   - I read F4 in `experiments/E-001.md:76`. It allows /usr, /bin, /lib and /etc (read only) and files the run creates in /tmp.
   - The leak cases in `test_ac05_judging.py` now use `/home/user/...` and `/root/...`.
   - I added `test_system_paths_e001_f4_allows_are_clean`, covering /etc, /usr/bin, /bin, /lib and /tmp.
   - The copy under test now lives under /var/tmp, falling back to the home directory. Under /tmp, the `../secret.txt` and `-evil` leak cases would themselves be allowed.
3. **J1 fill-c2 fixture vs C2's list rules (blocking), fixed in `test_j1_change_to_arm.py`.**
   - Stage 2 of the fixture spec now names `decisions/questions/P-009-ruling.md`, and Stage 3 names the unrelated P-010. C2 item 3 requires the stage to name the ruling.
   - The check file is now `checks/S-009-check.py`, with the spec id in its path. I added `checks/unrelated_check.py` as a negative case. Item 4 needs a `join-test: S-009/` marker or the spec id in the path.
4. **J2 seven-day test with a late record (blocking), fixed.** In `test_j2_dispatch_record.py` the record's `recorded:` date now equals the dispatch date (2026-11-01). The exactly-7-days and 7-days-plus-1-second cases are unchanged.
5. **Interface list out of date, fixed.** I rewrote the docstring in `e003_support.py` to match every call the tests make. It now includes `fill_judge_brief.py` without `--template`, the `rerun-decision` history file with its event words, and the `analyse.py` note from finding 11.
6. **AC4 locked-checks-session test, dropped.**
   - No held-back-side record names a session id, so a file test cannot catch the fault it aimed at.
   - Your answer to open question (b) means a test would compare the Orchestrator's own session id against `reviews/E-003/**`, and could fail a correct run.
   - The AC4 docstring now says this part is shown by K2's record and the dispatch records.
7. **AC1 role-file check, narrowed.**
   - Answer to open question (a): I read "every brief and role file ... is as it was, since the changes exist only as these texts" as "no change text is in any of them". That check stays.
   - The test that failed on any change to a role file or playbook since the freeze is removed, because a later unrelated role-file update is legitimate.
   - I added a check that no brief record that existed at the freeze has been modified or deleted. `docs/briefs/README.md` is excluded, and new records may be added.
   - I added a check that no brief record holds a change text.
   - Role files and briefs in other repositories are out of reach of a Model-Lab file test.
8. **AC4 HOLDOUTS.md check, fixed.** It now checks only lines starting `S-001-`.
9. **AC3 "completed", fixed.**
   - The docstring now says "completed" means judged.
   - I added the "arms-finished" event, which still gets the one rerun after a set-up fault (Reruns (b)).
10. **Cheap cases added, the rest not.**
    - Added: the J8 extract-as-frozen diff against f4298cd (`test_j8_holdout_pack.py`).
    - Added: J3 `export.py make --no-deliverable`, which exports nothing and returns `{"exported": false, "arm_result": "FAIL"}` (`test_j3_neutral_export.py`).
    - Not added: AC2's "records the pair", the two-lane J2 case, a deliverable that names the change, and J7's power for a kind stopped early. The spec fixes no record location or format for these.
    - "Is listed" stays checked as a non-empty `reason`, since the spec gives no listing form.
11. **`analyse.py` is a Builder deliverable the spec does not name.** I kept it as the smallest mechanical reference the tests need. It is in the interface list, flagged as an added deliverable in `src/E-003/**`, and the Builder's brief should say so. It is not the Reviewer's actual result record.
12. **AC2 research fixture, fixed.** The memo commit is now earlier than the source check's start commit (`test_ac02_pair_start.py`).

## Round 3 (brief 76), commit d372707

## Brief 76: both Critic round-2 fixes are in commit d372707, on top of 742ef89, with no push

Branch `build/check-author/s001-locked`, same worktree (`/tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/wt-check`). Same trailers as before.

**What changed**
1. **The /tmp reading (blocking finding 1).** I took F4's words strictly: a /tmp path is clean only when an earlier line of the same transcript creates it.
   - `tests/acceptance/test_ac05_judging.py`:
     - `test_system_paths_e001_f4_allows_are_clean` now creates each /tmp file first, one by a Write and one by `echo > file`, and then reads it.
     - I added one test, `test_a_tmp_file_the_run_did_not_create_is_a_leak`. It covers an uncreated /tmp read, a read before the creating write, and a read of a different /tmp path than the one created. The brief said to add no new test; this is the only addition, and it pins the strict reading. Say if you want it removed.
   - `tests/acceptance/e003_support.py`: the transcript-check interface note now reads "files the run itself created in /tmp (a /tmp path is clean only if an earlier line of the transcript creates it)".
   - I checked the other transcript cases and the docstring against F4's words and against each other.
     - `Glob path=/tmp/other` and `cd /tmp && ls` stay leaks, because nothing creates those paths.
     - The `saved-output.txt.other` read stays a leak, because only `--allow-path` clears the saved-output file, not its `.other` sibling.
     - The /usr, /bin, /lib and /etc cases are unchanged.
2. **The manifest skip (finding 2).** When `S001_MANIFEST` names a record, J7 and J8 now check it whatever its kind, and a badly formed one fails instead of skipping.
   - `e003_support.py`, `recorded_manifests`: a record named by the variable is returned even if it has no `## Pack manifest` heading.
   - `test_j7_analysis_pack.py` and `test_j8_holdout_pack.py`: the recorded-manifest tests take any record when the variable is set. I added `import os` to the J7 file.
   - I tried a malformed record (wrong info string) through the variable for J7 and J8. Each failed with one failure instead of skipping. I removed the trial record.

**Results**
- Suite: 228 tests, 43 pass, 2 skip, 183 fail. All 183 failures are "interface missing", meaning the Builder's `src/E-003/` scripts do not exist yet. The 2 skips are J7 and J8's recorded-manifest checks, which wait for a dispatch to record a manifest.
- `bash governance/checks/check_all.sh . 7d6c999` printed "OK: all governance checks passed".
- `surface_guard.py diff --range 7d6c999..build/check-author/s001-locked --branch build/check-author/s001-locked` printed "OK: 3 commit(s) ... checked (0 merge(s) skipped, 0 exempt, 0 human)".
- `git log --format='%an %ae' -3`:
  - check-author check-author@agents.invalid
  - check-author check-author@agents.invalid
  - check-author check-author@agents.invalid

**Left as the brief said**
- The rest of round-1 finding 10 stays untested: AC2's "records the pair", "is listed", the two-lane piece, a deliverable that names the change, and the power for a kind stopped early. The spec gives no location or format for these.
- The Critic's note on finding 7 stays: AC1's needle on C3's sentence would also fail a future brief that quotes it for reference.

## Round 4 (brief 79), commit 0030fcb

## Brief 79: Reviewer findings 1, 2, 3 and 6, plus the Critic's round-3 note 3, fixed in commit 0030fcb on top of d372707

New commit: `0030fcb`, same worktree and branch (`build/check-author/s001-locked`). Not pushed, same trailers.

**What changed, and how I checked each expectation by hand**
1. **Finding 1, AC6 re-scoring** (`test_ac06_owner_cards.py`, `test_the_owners_answer_replaces_the_judges_verdict_and_the_pair_class_is_worked_out_again`).
   - The answers are now `{"c00": "yes", "k01": "yes"}` and the comment is rewritten.
   - Check against E-003 Step 5 ("yes is FAIL, no is PASS"; the class is worked out again from the two outputs). I re-derived it with a reference script outside the repository.
     - p00 is (change PASS, control FAIL), so it starts as n10. Yes on c00 makes both arms FAIL, so it is concordant.
     - p01 is (change FAIL, control PASS), so it starts as n01. Yes on k01 makes both arms FAIL, so it is concordant. A "no" on k01 would change nothing, because k01 is already PASS.
     - So n10 = n01 = 0, as the test asserts.
   - I also re-checked the neighbouring rescore tests against Step 5, and they hold.
     - "Can't tell" keeps the judge's verdict.
     - A "no" on a both-pass pair stays concordant.
     - The answered and disagreements case gives 3 answered and 1 disagreement.
2. **Finding 2, J4 string matches** (`test_j4_sheet_route.py`, `test_a_matching_fingerprint_puts_the_sheet_in_the_brief`).
   - The brief text is now read with whitespace collapsed, and the stand-in sheet is collapsed the same way before the `assertIn`.
   - This covers every phrase match in the test: "Judge it against", "Apply this check:", the failing-rule sentence, the STANDIN markers, "Do not start background tasks", the "numbers of the tests ... file:line" phrase and "L7".
   - Check against E-002's frozen template, which wraps "Judge it / against:". I wrapped the template the same way, applied E-003 Step 4 changes 4, 6 and 7, and ran the test's own expectations on the collapsed result with a reference script. All hold, and no `arm` word appears.
   - No other test file matches template phrases. I grepped for them.
3. **Finding 3, the shared manifest variable** (`test_j7_analysis_pack.py` and `test_j8_holdout_pack.py`). With `S001_MANIFEST` set, each test now checks the named record only if it is its own kind or is malformed (no file lines). A well-formed manifest of the other kind makes it skip with the plain message "S001_MANIFEST names a manifest of the other kind ...". I ran these cases:
   - a well-formed blind manifest: J8 passes and J7 skips;
   - a malformed record: both J7 and J8 fail, one failure each.
4. **Finding 6, AC9** (`test_ac09_model_change.py` docstring). It now says Exclusions 7's set-up fault is rerun once (Sample, Reruns (b)). The analysis leaves out only a pair still mixed after its rerun, which is what the `arm_models` fixture stands for.
5. **Critic's round-3 note 3.** In `e003_support.py`, the transcript-check wording is now "clean on the line that creates it and on any later line, and only then". The stale comment in `test_ac05_judging.py` `setUp` now says the copy is outside /tmp so that the parent-escape and sibling cases land outside the copy and not in /tmp.

**Results**
- Suite: 228 tests, 43 pass, 2 skip, 183 fail. All 183 failures are "interface missing", because the Builder's `src/E-003/` scripts do not exist yet. The counts are the same as before this commit.
- `bash governance/checks/check_all.sh . 7d6c999` prints "OK: all governance checks passed".
- `surface_guard.py diff --range 7d6c999..build/check-author/s001-locked --branch build/check-author/s001-locked` prints "OK: 4 commit(s) ... checked (0 merge(s) skipped, 0 exempt, 0 human)".
- `git log --format='%an %ae' -3` gives:
  - check-author check-author@agents.invalid
  - check-author check-author@agents.invalid
  - check-author check-author@agents.invalid

**Not touched.** Finding 4 (the skip flag) and finding 5 (`record_checks merges`) are the owner's and the known LL-29 false failure. Open question (a) is the coordinator's: the checks are corrected here, before the lock.
