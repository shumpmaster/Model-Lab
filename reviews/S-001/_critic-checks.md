Verdict: FAIL

*The Critic on S-001's locked checks (Build-1), against the frozen spec. Brief 73 (docs/briefs/73-critic.md) for round 1, brief 75 for round 2, brief 77 for round 3, brief 80 for round 4 and brief 83 for round 5; each a fresh session on a different model from the checks' writer. Recorded verbatim by the Orchestrator, 2026-11-04. The first line is the latest round's verdict; rounds 1 and 2 were FAIL, round 3 PASS and round 4 FAIL. The Orchestrator's byte diff of the two copies (`git diff --stat e0d8104 742ef89`) shows the files round 2 did not re-read unchanged.*

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

## Round 2 (commit 742ef89)

Critic's round 2 on S-001's locked checks (tests/acceptance/**). I read the new copy at commit 742ef89 (scratchpad/fix-checks2) against round 1's copy at e0d8104 (scratchpad/fix-checks), against specs/S-001.md, experiments/E-003.md, C2, and E-001.md:76 (F4). I ran nothing.

Round 1's findings 1, 3 and 4 are resolved, and finding 2 is only half resolved. The fix for finding 2 adds a new blocking contradiction. Findings 5 to 9, 11 and 12 are resolved, and finding 10 is partly resolved.

## Findings

1. **Blocking (new, from the fix for round-1 finding 2): the transcript-check tests now contradict each other on /tmp, so no correct implementation can pass them all.**
   - F4 (E-001.md:76) allows only "files the run itself creates in the system temporary directory (/tmp)".
   - test_ac05_judging.py:181 requires `clean` for `Read /tmp/s001-file-the-run-made.txt`. No earlier line in that transcript creates the file.
   - test_ac05_judging.py:207 requires `leak@1` for a Read of `<self.tmp>/saved-output.txt.other`. `self.tmp` comes from `tempfile.mkdtemp`, which is under /tmp, and nothing in that transcript creates that file either.
   - :171 (`Glob path=/tmp/other`) and :173 (`cd /tmp && ls`) also require a leak.
   - So the outcome depends on which reading the implementation takes:
     - Read F4 strictly (only files the run created): it fails :181.
     - Allow all of /tmp, as the interface docstring now says (e003_support.py:49-50: "/usr, /bin, /lib, /etc (read only) and /tmp"): it fails :171, :173 and :207.
   - Fix: in :181, put a line before the Read that creates the file (a Write, or a Bash `echo > /tmp/…`). Keep a Read of a /tmp file the run did not create as a leak. Change e003_support.py:50 to "files the run itself created in /tmp". The /usr, /bin, /lib and /etc clean cases are right as they are.

2. **Resolved (round-1 finding 1): J7 and J8 now pick recorded manifests by their parsed file lines** (e003_support.py:481-491 `manifest_kind`; test_j7:131-148; test_j8:159-166). A blind manifest that lists reviewer.md is no longer taken for an analysis manifest.
   - Non-blocking weakness that this change brings in: the filter also applies when S001_MANIFEST names the record. A record whose `## Pack manifest` is badly formed (wrong info string, two blocks, one-space lines) gives no file lines. Its kind is then None, and J8/J7 skip with the message "no blind dispatch has recorded a manifest yet" instead of failing. The spec says the test "parses the dispatch's recorded manifest in the named form and fails unless …".
   - Fix: when S001_MANIFEST is set, check that record whatever its kind.

3. **Resolved (round-1 finding 3).** The Stage 2 lines now name decisions/questions/P-009-ruling.md (test_j1:102). The check file is checks/S-009-check.py, so the spec id is in its path (:110), and test_s009.py carries a `join-test: S-009/` marker. Line numbers check out: Stage 2 at line 7, Stage 3 at line 12. Each expected item now follows from C2 items 1 to 4.

4. **Resolved (round-1 finding 4).** test_j2:116 sets the record's date to the dispatch date (2026-11-01) before the seven-day check.

5. **Resolved (round-1 finding 5).** The interface list (e003_support.py:23-73) now matches the calls the tests make. That covers `--label`/`--copy-path` with no `--template`, and the calls round 1 found missing: entry options, locked-checks, parse-return/followup-text, verify-removal, v2, the make options, cards draw/file, and the `--history` events.

6. **Resolved (round-1 finding 6).** AC4 drops the locked-checks session test and says the K2 record and the dispatch records show it (test_ac04:15-17).

7. **Resolved (round-1 finding 7).** The role-file freeze is gone. AC1 now checks that:
   - brief records that existed at the freeze are not modified or deleted;
   - no brief record holds a change text.

   It says that other repositories are beyond a file test (test_ac01:86-106). I accept this reading, since AC1 is stated "at the Build gate".
   - Non-blocking: the needle at :99 ("A source you cannot open is not by itself a fault in the memo") would also fail a future Builder or Reviewer brief that quotes C3 for reference. No current record matches it.

8. **Resolved (round-1 finding 8).** test_ac04:82 now checks only `S-001-` lines.

9. **Resolved (round-1 finding 9).** "completed" is defined as "judged", with "arms-finished" kept apart (e003_support.py:43-46). test_ac03:134-141 matches Reruns (b).

10. **Partly resolved (round-1 finding 10), non-blocking.**
    - Added:
      - J3, no deliverable: the arm fails and no export is made (test_j3:154-166; this matches E-003 Exclusions 4);
      - J8, the extract changed since the freeze (test_j8:107-115; the spec at :270 says the extract is "as frozen").
    - Still untested, and none contradicts the spec:
      - AC2 "records the pair";
      - "is listed", where only `reason` is checked;
      - J2's two-lane piece, which the tests name as a gap;
      - J3, a deliverable that names the change;
      - J7, the power for a kind stopped at a review point;
      - that a write under /etc is refused.

11. **Resolved (round-1 finding 11).** analyse.py is now declared as an added Builder deliverable in src/E-003/** (e003_support.py:69-71).

12. **Resolved (round-1 finding 12).** The memo commit is now `base`, which comes before the source check's start `parent` (test_ac02:24-34).

**Round 1's four checks:**
- (a) **Coverage of AC1 to AC11 and J1 to J8: holds.** Every criterion and join still has a test file, and each J file keeps its `join-test: S-001/Jn` marker.
- (b) **Nothing beyond the spec: holds**, apart from the declared analyse.py.
- (c) **Each check able to fail: holds**, apart from the skip in finding 2.
- (d) **No held-back check, sheet text or src/** read: holds.** Only the stand-in sheet is used, and no test reads src/**, docs/handover/** or docs/reports/**.

**Not checked by reading:** I found which files changed by comparing line counts. The files I did not re-read in the new copy (AC6 to AC11, J4 to J6) have the same line counts as in round 1, but same-length edits there were not checked.

## Six-part contract
- **Changed (by file):** none. I am read-only.
- **Why:** this is the Critic's round 2 on S-001's locked checks, needed before the checks are locked into use (the standard milestone "Tests written before the work").
- **Verified:** by reading only. In the new copy I read in full:
  - e003_support.py;
  - test_ac01, ac02, ac03, ac04, ac05;
  - test_j1, j2, j3, j7, j8;
  - tests/acceptance/README.md;
  - docs/briefs/README.md.

  In round 1's copy I read test_ac05:100-201, test_ac01:70-105, and the round-1 findings. I also read C2 in full, grepped E-001.md:76 for F4, grepped S-001.md (lines 214, 216, 250 and 270) and E-003.md (Exclusions), and compared line counts across both copies.
- **Undone:** I ran no tests, because I hold no shell. I did not re-read AC6 to AC11 or J4 to J6 (their line counts match round 1).
- **Needed outside its surface:** the Check author must fix finding 1. It should also fix finding 2's S001_MANIFEST skip, and should either fix or answer the remaining gaps in finding 10.
- **Open questions:** (a) Should F4's "files the run itself creates in /tmp" be read strictly, that is, shown by the transcript? The tests need one reading, and the spec's words support the strict one.

## Round 3 (commit d372707)

Critic's round 3 on S-001's locked checks. I compared the new copy (d372707, fix-checks3) with round 2's copy (742ef89, fix-checks2) by reading the four changed files side by side. I also checked them against specs/S-001.md (:214, :216, :269, :270), experiments/E-003.md (:36, Exclusions 2 at :114) and E-001.md:76 (F4). Both of round 2's findings are resolved and nothing blocking is left. F4 now has one reading. Findings 2 and 3 below are new and not blocking.

## Findings

1. **Resolved (round 2 finding 1, blocking): /tmp now has one reading, the strict one, and every transcript-check case applies it.**
   - The old :181 case (a Read of a /tmp file nothing had created) is gone. test_ac05_judging.py:182-185 now creates each /tmp file first, once with a Write and once with a Bash `echo hi > …`, and then reads it. Both are required clean.
   - The new test at :187-194 requires a leak in three cases:
     - a /tmp file the run never created;
     - a Read that comes before the Write that creates the file (leak@1);
     - a different /tmp path from the one created (leak@2).
   - The cases that were already there still fit this reading:
     - :171 (`Glob path=/tmp/other`) and :173 (`cd /tmp && ls`) are leaks;
     - :220 (`<self.tmp>/saved-output.txt.other`, under /tmp and not created) is a leak;
     - :219 is clean only through `--allow-path`, which matches E-003 Exclusions 2.
   - test_ac03_pair_audit.py:146-167 has its copy under /tmp and requires reads inside the copy to be clean. That fits: the copy check comes first, and S-001:214 puts the blind Check author's pack folder under /tmp.
   - The interface note (e003_support.py:50-51) now says "files the run itself created in /tmp (a /tmp path is clean only if an earlier line of the transcript creates it)". That is the same reading as the ac05 docstring (:176-178) and E-001.md:76.
   - Nothing contradicts S-001, E-003 or the change files. A correct implementation can pass every case.

2. **Resolved (round 2 finding 2), with a new non-blocking flaw. Self-implication flag (D-050): the fix is the one my round 2 text proposed, so this finding is about my own earlier check.**
   - What is resolved: when S001_MANIFEST is set, recorded_manifests (e003_support.py:477-478) returns the named record whatever it holds. J7 (:144) and J8 (:161) then check it whatever its kind, so a badly formed record now fails instead of skipping.
   - The new flaw: both tests read the same variable, and each checks the named record against its own entry.
     - With S001_MANIFEST naming a correct blind record (as J8's docstring :17 and its skip text tell you to set it), J7 fails it. critic.md is not in the analysis must_read, and E-003.md, sizing.py, verdicts.tsv and the card file are missing.
     - With it naming a correct analysis record, J8 fails it, because E-003.md and reviews/E-003/** are withheld.
     - So running the whole suite (the first command in e003_support.py:6-7) with the variable set fails a correct manifest. Running one file at a time works.
     - S-001:269 says J7 parses "the recorded manifest", meaning the analysis dispatch's own, not any record that is named.
   - Fix: when the variable is set, each test checks the named record only if `manifest_kind` is its own kind or None (None catches a badly formed record). Otherwise it skips, saying the record is the other kind. Or give each test its own variable.

3. **Non-blocking: the wording and one comment do not quite match what the tests require.**
   - "Clean only if an earlier line … creates it" (e003_support.py:51; ac05:178), read literally, makes the creating line itself a leak. That would cover the Write at :182 and the Bash at :184, which the tests require to be clean.
     - Fix: "clean on the line that creates it and on any later line".
   - The tests also mean the Builder must treat a Bash redirect target as a file the run creates. Only `>` is tested. This sits inside F4 and is not beyond the spec, but the Builder should be told.
   - The comment at ac05:138-139 ("a copy under /tmp could not show the leak cases below") is now stale. Under the strict reading, a copy under /tmp could show them. It is harmless.

4. **Round 1's four checks, for the changed files:**
   - (a) **Coverage: holds.** J7 and J8 keep their `join-test` markers, and every case in ac05 is still there.
   - (b) **Nothing beyond the spec: holds.** The strict /tmp reading is F4's own wording.
   - (c) **Each check able to fail: holds.** The skip in finding 2 is gone. J7 and J8 now skip only when no record of their kind exists and the variable is unset, which matches the spec's "meaningful only once … recorded".
   - (d) **No held-back check, sheet text or src/** read: holds.** The changed files use only the stand-in sheet and read nothing under src/**, docs/handover/** or docs/reports/**.

## Six-part contract
- **Changed (by file):** none. I am read-only.
- **Why:** this is the Critic's round 3 on S-001's locked checks, needed before they are locked for the standard milestone "Tests written before the work".
- **Verified:** by reading only.
  - I read the four changed files in full in both copies: e003_support.py, test_ac05_judging.py, test_j7_analysis_pack.py and test_j8_holdout_pack.py. For J8 I read the round 2 copy's lines 1-40 and 140 to the end; the rest matched.
  - I read test_ac03_pair_audit.py:110-168 in the new copy, because it also calls the transcript check.
  - I read S-001:269 in full, and grepped S-001 (:214, :216, :270), E-003 (:36, :114), E-001:76 and tests/acceptance/README.md (no S001_MANIFEST guidance there).
- **Undone:** I ran no tests (I hold no shell). For the claim that only these four files changed, I relied on the Orchestrator's diff.
- **Needed outside its surface:** the Check author should fix finding 2 (the shared S001_MANIFEST variable) and finding 3 (the wording and the stale comment). Neither blocks locking.
- **Open questions:** (a) Should J7 and J8 each get their own manifest variable, or should one variable be filtered by kind as in finding 2's fix? Either works. The spec names neither.

Files: /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-checks3/tests/acceptance/e003_support.py, /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-checks3/tests/acceptance/test_ac05_judging.py, /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-checks3/tests/acceptance/test_j7_analysis_pack.py, /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-checks3/tests/acceptance/test_j8_holdout_pack.py

## Round 4 (commit 0030fcb)

The Critic's round 4 on S-001's locked checks. I compared the seven changed files in fix-checks4 (0030fcb) with fix-checks3 (d372707) by reading both copies in full. I worked each changed expectation out by hand from E-003 Step 4 and Step 5, E-002's template (experiments/E-002.md:22-36) and S-001 J4, J7 and J8 (:266, :269, :270).

The Reviewer's findings 1, 2 and 6 are resolved. Finding 3, which is also my round 3 note 2, is resolved for the case it named. But the fix opens a new hole in J8, and that hole blocks.

**Self-implication flag (D-050):** the J7/J8 fix is the one my round 3 note 2 proposed ("each test checks the named record only if `manifest_kind` is its own kind or None"). Finding 3 below is a fault in my own earlier proposal.

## Findings

1. **Resolved (Reviewer finding 1, blocking before): AC6's re-scoring now expects the right answer.** test_ac06_owner_cards.py:136-142.
   - The answers are now `{c00: yes, k01: yes}`. By hand, using E-003:78 ("Yes is FAIL"):
     - p00 (change PASS, control FAIL) becomes (FAIL, FAIL), so concordant.
     - p01 (change FAIL, control PASS) becomes (FAIL, FAIL), so concordant.
     - n10 and n01 are both 0, as asserted.
   - The new comment states the rule correctly. That fits E-003:86: each pair's class is worked out again from its two outputs.
   - Nothing else in the file changed.

2. **Resolved (Reviewer finding 2, blocking before): J4's fill test no longer depends on line breaks.** test_j4_sheet_route.py:174-183.
   - The text is now matched with whitespace collapsed. By hand against E-002:27-28 and :34-35, with only E-003 Step 4's seven changes applied:
     - "Judge it\nagainst:" collapses to "Judge it against:", so a ≥ 0.
     - Change 4 puts "Apply this check:", the sheet, then the failing rule after it, so a < b < c. STANDIN-T1 comes after b and STANDIN-T3 before c.
     - Change 6 turns "Then each blocking finding as one\nnumbered line citing file:line." into "Then the numbers of the tests of the check that failed, each citing file:line." The asserted substring is present.
     - Change 7's "Do not start background tasks" is present.
     - "L7" is present, and the template holds no word "arm".
   - A byte-faithful fill now passes, and so does a fill that wraps the added text.
   - Not blocking: "the check in full" (:177) is now also matched collapsed. A fill that re-wraps the sheet would pass, though E-003:65 says "given in full". The byte-for-byte test at :187-190 and the fingerprint gate limit the risk. This weakens the check slightly; it is not a defect.

3. **Blocking: new. J8, run on its own with S001_MANIFEST set, skips a blind manifest that wrongly lists experiments/E-003.md.** It should fail it. (test_j8_holdout_pack.py:160-172; e003_support.py:482-492)
   - `manifest_kind` checks for "analysis" first, so any manifest whose files include experiments/E-003.md is classed "analysis", even when it also holds the extract and check-author.md.
   - J8 now checks a named record only if it is "blind" or None. So for a blind-dispatch manifest that wrongly lists E-003.md, J8 prints "skipped: S001_MANIFEST names a manifest of the other kind (J7's)" and does not fail.
   - J8 is to be run exactly this way: its docstring (:17) and skip text tell you to run it with S001_MANIFEST=<brief record> before each dispatch, and e003_support.py:8-9 gives the one-file command.
   - S-001:270 says the blind pack holds "never … experiments/E-003.md", and that J8 "fails unless … no path matches a withheld path". E-003:33 says the blind dispatch goes ahead once "J8's test passes on it". A skip is not a fail, and the skip message wrongly points at J7.
   - This is the leak the blind pack exists to stop: the registration names the changes. In round 3 the named record was checked whatever it held, so this is a regression.
   - The full suite still goes red, because J7 checks the record as an analysis manifest and fails it on check-author.md and the extract. So the hole is open only for a one-file run. Even so, a locked check cannot be fixed once locked, and a J8 run alone must not skip a leaking blind manifest.
   - Fix (one line in each test): when the variable is set, J8 checks the named record if its files include the extract or check-author.md, or its kind is None. J7 checks it if its files include experiments/E-003.md, or its kind is None. A record carrying both kinds' markers is then checked, and failed, by both. Alternatively, give each test its own variable.
   - The unnamed full-suite path is unaffected: a mixed manifest found by scanning docs/briefs still fails J7.

4. **Resolved (Reviewer finding 3 and my round 3 note 2) for the case they named.**
   - With the variable naming a well-formed blind manifest, J7 now skips it, saying why (test_j7_analysis_pack.py:144-152), and J8 checks it.
   - With it naming a well-formed analysis manifest, J8 skips and J7 checks.
   - A malformed record (kind None) is checked, and failed, by both.
   - Finding 3 is the remaining gap.

5. **Resolved (Reviewer finding 6): AC9's docstring now gives the reading.** test_ac09_model_change.py:3-5 says the analysis leaves out only a pair still mixed after its Reruns (b) rerun, and that the `arm_models` fixture stands for that pair. This fits E-003 Exclusions 7 (:119) and Reruns (b) (:107). The test body is unchanged.

6. **Partly resolved, not blocking: my round 3 note 3.**
   - e003_support.py:51 now reads "clean on the line that creates it and on any later line, and only then", which is right. By hand:
     - the Write at ac05:182 and the echo at :184 are clean;
     - the read before the write at :190-191 is leak@1;
     - the other path at :193-194 is leak@2.
   - The stale comment at ac05:138-139 is replaced with an accurate one.
   - Left over:
     - test_ac05_judging.py:178's docstring still says "clean only when an earlier line of the same transcript creates it", which read literally makes the creating line a leak;
     - the interface note still does not tell the Builder that a Bash `>` redirect target counts as a file the run created.

7. **Round 1's four checks, for the changed files:**
   - (a) **Coverage: holds.** The J4, J7 and J8 `join-test` markers stay, and no case was dropped.
   - (b) **Nothing beyond the spec: holds.**
   - (c) **Each check able to fail: fails for J8**, run alone with the variable set, on a blind manifest that holds experiments/E-003.md (finding 3). It holds elsewhere; J4's collapsed matching still fails a fill that is missing or out of order.
   - (d) **No held-back check, sheet text or src/** read: holds.** Only the stand-in sheet is used, and nothing under src/**, docs/handover/** or docs/reports/** is read.
   - Nothing in the seven files contradicts E-003 or its change files. S-001 is contradicted only as in finding 3. No change fails a correct implementation.

## Six-part contract
- **Changed (by file):** none. I am read-only.
- **Why:** this is the Critic's round 4 on S-001's locked checks. It follows the Reviewer's findings on PR #51 and is needed before the checks are locked for "Tests written before the work".
- **Verified:** by reading only.
  - I read all seven changed files in full in both copies. For round 3's J8 I read lines 1-139 and 140 to the end; only TestJ8Recorded and nothing else changed. In e003_support.py only :51 changed. In AC5 only :138-139 changed.
  - I read E-003.md in full and E-002.md:15-44 (the template).
  - I read S-001:266-270.
  - I read the Reviewer's return (rev51-r1.md) and my rounds 1 and 3 (crit-checks-r1.md, crit-checks-r3.md).
- **Undone:**
  - I ran no tests (I hold no shell).
  - For the claim that only these seven files changed, I relied on the Orchestrator's diff.
  - Round 3's checks record, reviews/S-001/_critic-checks.md, is in neither copy, so I read my earlier rounds from the scratchpad tmp files instead.
- **Needed outside its surface:**
  - The Check author (dispatch (b)) should fix finding 3 (it blocks), and should fix finding 6's two leftovers.
  - A Critic round should then check the change.
- **Open questions:**
  - (a) For finding 3: should each test match on its own markers (my suggestion), or should J7 and J8 get separate variables? Both close the hole; the spec names neither.

Files:
- /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-checks4/tests/acceptance/test_j8_holdout_pack.py
- /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-checks4/tests/acceptance/test_j7_analysis_pack.py
- /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-checks4/tests/acceptance/e003_support.py
- /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-checks4/tests/acceptance/test_ac05_judging.py
- /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-checks4/tests/acceptance/test_ac06_owner_cards.py
- /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-checks4/tests/acceptance/test_j4_sheet_route.py
- /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-checks4/tests/acceptance/test_ac09_model_change.py

## Round 5 (commit bef590a)

The Critic's round 5 on S-001's locked checks. I compared the four changed files in fix-checks5 (bef590a) with fix-checks4 (0030fcb) by reading both copies in full. I worked out by hand what J7 and J8 do when run alone with S001_MANIFEST set, against S-001:202, :269 and :270 and E-001 F4 (E-001.md:76).

What changed, by file:
- **e003_support.py:** the interface note at :51-52 gained a list of what counts as creating a file, and a new `manifest_markers` was added at :496-503.
- **test_j7_analysis_pack.py:** the import, and the record selection at :145-151.
- **test_j8_holdout_pack.py:** the import, and the record selection at :162-169.
- **test_ac05_judging.py:** only the docstring at :178.

## Findings

1. **Resolved (round 4 finding 3, blocking before): a blind manifest that also lists experiments/E-003.md is now checked and failed by both tests.** Worked by hand:
   - `manifest_markers` returns (True, True, True) for this record.
   - J8 checks it, since `mine` is true when blind is true (:165-167). `holdout_problems` fails it because E-003.md is in WITHHELD and outside must_read.
   - J7 checks it, since analysis is true (:147-149). It fails it because the extract and check-author.md are outside the analysis must_read.
   - The unnamed full-suite path is unchanged (`manifest_kind`), so a mixed record in docs/briefs still fails J7.

2. **Blocking, new: a regression from round 4 finding 4.** With S001_MANIFEST set, a record that has file lines but neither kind's marker is now skipped by both J7 and J8. Round 4 checked and failed it in both. (test_j8_holdout_pack.py:165-169; test_j7_analysis_pack.py:147-151)
   - Round 4 checked a named record when its kind was None. Round 5 checks it only when it has no file lines (`not has_files`). My round 4 suggestion said "or its kind is None", so the fix narrowed it.
   - Example by hand: a blind pack whose manifest lists specs/S-001.md in place of the extract and leaves out check-author.md.
     - Its files are critic.md, reviewer.md, source-checker.md, docs/playbooks/software.md and specs/S-001.md.
     - The markers are (True, False, False), so `mine` is false in both tests.
     - J8 skips it, wrongly saying the record is "of the other kind (J7's)". J7 skips it too.
   - The same happens to any blind manifest that lacks both the extract and the agent file. It also happens when the only lines that fail to parse (e.g. an uppercase SHA) are the marker lines.
   - Why this blocks:
     - S-001:270 names "lacks the extract (no dispatch; the manifest is made again)" as an awkward case J8 must fail, and S-001:202 dispatches only "after J8's test passes on the recorded manifest".
     - A skip is not a fail. The skip message is false, and the example also leaks specs/S-001.md.
     - This is the same kind of hole as round 4 finding 3, which was blocking.
   - Fix (one line in each test):
     - J8: `return blind or not analysis`
     - J7: `return analysis or not blind`
     - Worked by hand, this gives: blind-only goes to J8 only, analysis-only to J7 only, both markers to both, and neither marker (including no file lines) to both. That keeps findings 1 and 3 here as they are.

3. **Resolved (round 4 finding 6, leftovers 1 and 2).**
   - AC5's docstring at :178 now reads "clean on the line that creates it and on any later line, and only then". That matches e003_support.py:51 and the cases at ac05:182-194.
   - The interface note at :51-52 now says a Bash `>` or `>>` redirect target counts as a file the run created. That covers the echo case at ac05:184.

4. **Not blocking: the note's new "Write/Edit file_path counts as created" is wider than E-001 F4 for Edit.**
   - E-001:76 allows only "files the run itself creates" in /tmp.
   - An Edit cannot create a file. It acts on an existing one and returns part of its text. So a transcript whose first contact with a /tmp file it did not create is an Edit would be marked clean by a Builder following the note.
   - The same is true, more weakly, of `>>` and `touch` on a file that already exists. Those are defensible, because a transcript check cannot see the file system.
   - No test asserts the Edit case, so a correct implementation is not failed. Suggest dropping "/Edit" from the note.

5. **Not blocking: wording.**
   - J8's docstring at :14-17 and J7's at :15-18 still say the record named by S001_MANIFEST is checked, but each can skip it.
   - No synthetic test exercises `manifest_markers` or the named-record selection. TestJ7Classify tests only `manifest_kind`. A case for a mixed record and one for a record with no marker would make findings 1 and 2 testable without the variable.

6. **The four asked cases, J7 and J8 each run alone with S001_MANIFEST set:**
   - **Well-formed blind manifest** (markers T,T,F): J8 checks it and it passes, given a correct PACKS entry. J7 skips it, giving "J8's" as the reason, which is correct.
   - **Well-formed analysis manifest** (markers T,F,T): J7 checks it and it passes. J8 skips it, giving "J7's", which is correct.
   - **Malformed record:**
     - With no section, no block, or no parsable file line, both tests check it and fail it.
     - With a marker line parsed, the marker's own test checks it and fails it.
     - With file lines but no marker parsed, both skip it. That is finding 2.
   - **Blind manifest that also lists E-003.md:** both tests check it and fail it (finding 1).

7. **Round 1's four checks, for the changed files:**
   - (a) **Coverage holds.** The join-test markers stay, and no case was dropped.
   - (b) **Nothing beyond the spec holds.** `manifest_markers` is a helper on the test side.
   - (c) **Each check able to fail: fails for J8**, run alone with the variable set, on a named blind record with no marker (finding 2). It holds elsewhere.
   - (d) **No held-back check, sheet text or src/** read: holds.**
   - Nothing contradicts experiments/E-003.md. S-001:270 is contradicted as in finding 2, and E-001 F4 only as in finding 4, which is not blocking. No change fails a correct implementation.

## Six-part contract
- **Changed (by file):** none. I am read-only.
- **Why:** this is the Critic's round 5 on S-001's locked checks, needed before they are locked for "Tests written before the work".
- **Verified:** by reading only.
  - I read all four changed files in full in both copies.
  - I read S-001:269-270 and checked :202 and :214 by search.
  - I read E-001 F4 (:70-79) by search.
  - I read round 4's return (crit-checks-r4.md).
- **Undone:**
  - I ran no tests (I hold no shell).
  - For the claim that only these four files changed, I relied on the Orchestrator's diff.
  - I did not re-read E-003.md in this round. The changes touch only the selection logic and the /tmp wording, and I checked the E-003 points behind them in round 4.
- **Needed outside its surface:**
  - The Check author (dispatch (b)) should fix finding 2, which blocks, and preferably findings 4 and 5.
  - A Critic round should then check the change.
- **Open questions:** whether "Edit" should stay in the note's list of what counts as creating a file (finding 4). E-001 F4 suggests not.

Files:
- /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-checks5/tests/acceptance/test_j8_holdout_pack.py
- /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-checks5/tests/acceptance/test_j7_analysis_pack.py
- /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-checks5/tests/acceptance/e003_support.py
- /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-checks5/tests/acceptance/test_ac05_judging.py
