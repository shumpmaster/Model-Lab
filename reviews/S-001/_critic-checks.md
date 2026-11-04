Verdict: FAIL

*The Critic on S-001's locked checks (Build-1), against the frozen spec. Brief 73 (docs/briefs/73-critic.md); a fresh session on a different model from the checks' writer. Recorded verbatim by the Orchestrator, 2026-11-04. The first line is the latest round's verdict.*

## Round 1 (commit e0d8104)

Critic's pass on S-001's locked checks (tests/acceptance/test_ac*.py, test_j*.py, e003_support.py), read at the fixed copy of Model-Lab e0d8104 against specs/S-001.md and experiments/E-003.md as frozen at f4298cd, with the change files C1–C3 and E-001's F4.

Overall: coverage is wide. Each AC1–AC11 and each J1–J8 has a test file, and each J test carries its `join-test: S-001/Jn` marker. Most checks are strict, with mutation-style negative cases, so they would catch a wrong implementation and not only a missing one. Four checks contradict the frozen spec or its frozen change files, or would turn the suite red on a correct run. Those four block.

## Findings

1. **Blocking: J7's recorded-manifest test will check the blind dispatch's manifest and fail it.** test_j7_analysis_pack.py:132-133 picks any docs/briefs record whose *whole text* contains `.claude/agents/reviewer.md` or `experiments/E-003.md`. The `S-001-holdout` manifest lists `.claude/agents/reviewer.md` as a file line (it is in that pack's must_read; J8's own GOOD list has it). So from the first blind dispatch on, J7 tests the J8 manifest against the `S-001-analysis` entry. It finds the extract and critic.md not allowed, and E-003.md, verdicts.tsv and the cards file missing. The full suite goes red, and every weekly R1 landing needs the full suite to pass. Fix: pick manifests by their parsed file lines, not the record text. An analysis manifest is one whose file lines include experiments/E-003.md. A blind manifest is one whose file lines include check-author.md or the extract. test_j8_holdout_pack.py:151 has the same weakness and should get the same fix.

2. **Blocking: the transcript-check tests count reads that F4 allows as leaks.** E-003 Exclusions 2 and the sheet's route (step 3) allow "the system paths E-001's F4 allows". F4 (experiments/E-001.md:76) allows reading under /usr, /bin, /lib and /etc (read only), and files the run itself creates in /tmp. Yet test_ac05_judging.py:159 (`/etc/hostname`), :171 (`/etc/a`, `/etc/b`) and :184 (`/etc/hosts`) all require `leak@n`. A correct implementation fails these. Also, no test shows that an allowed system path comes back `clean`, so an over-strict check would pass. Use a path such as /home/user/x or /root for the leak cases, and add clean cases for /usr, /etc and a run-created /tmp file.

3. **Blocking: J1's fill-c2 test needs items that C2's frozen list rules would not give.** test_j1_change_to_arm.py:137 requires `decisions/questions/P-009-ruling.md`. C2 item 3 (experiments/E-003/C2-built-named-inputs.md:28) says "every ruling file under decisions/ that the cited stage or section names". In the fixture (:102), the Stage 2 lines are only "gamma/delta/epsilon" and name no ruling; only the ruling file names itself. The test at :140 also requires `checks/s009_check.py`. C2 item 4 needs a `join-test: S-009/` marker or the spec id in the path. That file has no marker, and its path holds `s009`, not `S-009`. An implementation that follows C2 strictly fails both. Fix the fixture: Stage 2 should name the ruling's path, and the check file should carry the marker or `S-009` in its path.

4. **Blocking: J2's seven-day test calls a record written after the dispatch eligible.** test_j2_dispatch_record.py:114-117 asserts `eligible` for a record reading `recorded: at hand-out, 2026-11-05`, given `--dispatched-at 2026-11-01`. That is a record written four days after the dispatch, which J2's first awkward case says is not eligible. Meanwhile :86-88 requires the same date to be read from that line and compared with the round-1 verdict. An implementation that applies the date both ways fails the test. Fix: give the fixture a recorded date equal to the dispatch date.

5. **Non-blocking: the interface list in e003_support.py:12-55 does not match the tests.** That docstring is the stated contract, so it should describe the calls the tests make.
   - fill_judge_brief.py is listed with `--template FILE`. test_j4 (:167) and test_ac05 (:125) call it without `--template` and with `--label` and `--copy-path`.
   - Calls the tests make that the list leaves out:
     - `pair.py entry --repo/--dispatched-at/--round-1-verdict-at/--memo-commit`
     - `pair.py locked-checks`
     - `judge.py parse-return` and `followup-text`
     - `change.py verify-removal`
     - `analyse.py v2`
     - `export.py make --checker-role/--role-file/--task-statement-text/--task-statement-path/--memo-path`
     - `cards.py draw --set/--answers` and `cards.py file`
   - The `--history` file and its event words for `pair.py rerun-decision` are not described anywhere.

6. **Non-blocking: AC4's "locked-checks session" test cannot catch the fault it aims at, and could fail a correct run** (test_ac04_heldback_gate.py:97-114).
   - Nothing on the held-back side records a sheet session's id: the J4 block has no session line. So running dispatch (a) in dispatch (b)'s session would not show here.
   - If dispatch (b)'s Agent-Session trailer is the Orchestrator's session id (b is a helper of it), the Orchestrator's own K1/K5 lines in reviews/E-003/<kind>/sessions.md may name that id and fail the test.
   - Drop it, or say that this part of AC4 is shown by the K2 record and the dispatch records.

7. **Non-blocking: AC1's role-file check goes beyond what AC1 needs and misses part of what it says.**
   - test_ac01_change_texts.py:86-91 fails on *any* change to .claude/agents/** or docs/playbooks/** since the freeze. Over a run of one to two years, an unrelated, legitimate role-file update would turn the suite red. "Since the changes exist only as these texts" needs only the check at :72-84 that no role file holds a change text.
   - The other half of AC1 is not tested: no brief (docs/briefs/**) and no other repository is checked.

8. **Non-blocking: AC4's HOLDOUTS.md check forbids any set line that is not S-001's** (test_ac04:82). The spec does not ask for this, and a later test's set would break it. Check only the `S-001-` lines.

9. **Non-blocking: AC3's rerun test can be read against Reruns (b)** (test_ac03:136). `["completed","set-up-fault"]` must not be rerun. If "completed" means the arms finished but are not yet judged, Reruns (b) says the pair is rerun once. Define "completed" as "judged".

10. **Non-blocking: cases left untested.**
    - AC2: "records the pair" (the test says so itself).
    - "Is listed" for pieces and pairs left out (AC2, AC3, AC5, J2): only `reason` is checked.
    - J2: the two-lane piece.
    - J3: no deliverable means that arm fails and no export is made (also E-003 Exclusions 4); a deliverable that names the change is judged as it is and reported.
    - J7: a kind stopped at a review point has its power worked out with sizing.py in the analysis.
    - J8: the extract edited after the freeze. A `git diff FROZEN HEAD -- experiments/E-003/check-author-extract.md` check, like test_ac01:93-100 does for the change files, is cheap.
    - The case sets are otherwise complete for J1, J4, J5 and J6.

11. **Non-blocking: AC7, AC9 and AC10 are tested through `analyse.py`, a Builder script the spec does not name.** The spec says the Reviewer analyses. As a mechanical reference this is about the least a test needs, and it fits src/E-003/** in the areas touched. But it adds a Builder deliverable, and it does not check the Reviewer's actual result record. The Builder's brief should say so.

12. **Non-blocking: AC2's research fixture is the wrong way round** (test_ac02:31-34, 94-97). The memo commit comes *after* the source check's start commit, so the check's copy cannot hold the memo. An implementation that requires the memo to be an ancestor of the check's start would fail. Put the memo commit before the check's start.

**Check 4 (no held-back check, sheet text or src/**): met.** Only a stand-in sheet is used, marked as no real check. No test reads src/**, docs/handover/** or docs/reports/**. The src/E-003/*.py names are interface paths to be built, not content. The exact change texts in e003_support.py:251-257 are allowed to dispatch (b), J8's test needs them, and tests/acceptance/** is withheld from the blind pack.

**Choices that fill gaps the spec leaves open, all acceptable:**
- the closing-block layout (J5);
- the grammar of the judge's failed-test line;
- extra cards drawn from the first non-empty group in the order G1, G3, G2;
- the in-flight cut taken at the submission's committer date;
- the counts card shape;
- the caps 133/132/266 and 133/66/200, which match the spec's table.

## Six-part contract
- **Changed (by file):** none. I am read-only.
- **Why:** this is the Critic's pass on the locked checks, which the standard milestone "Tests written before the work" requires (OPERATING_MODEL §4).
- **Verified:** by reading the files; I ran nothing. Read: specs/S-001.md (whole), experiments/E-003.md, E-003/C1–C3, E-003/check-author-extract.md (grep), E-003/sizing.py (grep), E-001.md:76 (F4), E-002.md:21-36 (template), governance/PACKS.toml:103-131, governance/HOLDOUTS.md, docs/briefs/README.md:7-10, docs/PROJECT.md:109, and every test_ac*/test_j* file plus e003_support.py. No checks/** files exist.
- **Undone:** I did not run the suite, because I hold no shell. Whether the "should PASS now" tests (AC1, the J7 and J8 entry and extract tests) pass today is not verified.
- **Needed outside its surface:** the Check author (dispatch (b)) should fix findings 1–4, and should fix 5–12 or answer them in its return. The tests are not locked into use until a Critic's pass.
- **Open questions:**
  - (a) Should AC1's freeze cover all role files for the whole test, or only the absence of the change texts (finding 7)?
  - (b) Is a dispatch (b) helper's Agent-Session id its own or the Orchestrator's (finding 6)?
