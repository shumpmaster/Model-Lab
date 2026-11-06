# The Check author's return on the AC2 research test (brief 99), verbatim

*Recorded by the Orchestrator, 2026-11-05. The writer's own summary of its work: kept out of the Reviewer's pack (docs/reports/**). The commit it describes is daa44a3577316e1394f23147bfef91e17db153ed on build/check-author/s001-ac2-research, kept local.*

## Six-part contract

**1. Changed (by file)**
- /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/wt-check/tests/acceptance/test_ac02_pair_start.py: only `test_research_runs_two_source_checks_from_the_checks_start_commit`, one hunk, +11/-2 lines. No other file or test changed. The comparison now sets each arm's copy path aside first.
- The change copies lines 72-80 of the built-work test (path not in the brief, copy path in the brief, both paths set aside, control equals the sample brief with `<COPY>`, briefs differ). The test then keeps its original "exactly one differing paragraph" count and its original `startswith("A source you cannot open is not by itself a fault")` check.
- I did not add the full-C3-text equality or the built test's final join-equality (line 82). Those are not in lines 72-80, and you asked for the comparison only.

**2. Why**
- Owner ruled A on decisions/questions/P-001-ac2-research-test.md. No correct build could pass the old test, because each brief names its own copy's path (specs/S-001.md:264, J2; experiments/E-001.md:102; experiments/E-003.md:115).

**3. Verified (command and output)**
- The table was written before the edit, at /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/ref/table-before.md. The stand-in is /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/ref/pair.py and the runner is /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/ref/run.sh. All are outside the repository.
- The stand-in is built from the frozen text only: `plan` prints the arms JSON for the mode in `STANDIN_MODE`, and makes two real git clones holding the start commit and its ancestors only. The runner copies tests/acceptance beside the stand-in and runs the research test with `python3 -m unittest ... -k research`. No build, no src/E-003, no builder branch and no reports were read.
- `bash governance/checks/check_all.sh . f5179378c1802ff9139b0b8d63e5682c8859f68e`: every line PASS, ending "OK: all governance checks passed." (exit 0).
- `python3 governance/checks/surface_guard.py diff --range f5179378c1802ff9139b0b8d63e5682c8859f68e..build/check-author/s001-ac2-research --branch build/check-author/s001-ac2-research`: "OK: 1 commit(s) ... checked (0 merge(s) skipped, 0 exempt, 0 human)" (exit 0).
- I did not run the whole acceptance suite, because the build is not in my pack. The reference runs cover only the one changed test.

**4. Undone / not done**
- Not pushed, no pull request, not merged.
- The three open points the owner kept for later are untouched.
- The C3 text is still checked only by its first words (see row R4b). This is the same limit as before, and I left it.

**5. Needed outside my surface**
- Nothing needed. One thing is for the owner to know: no locked test checks that the C3 paragraph in the pair's change-arm brief is the whole frozen text. test_ac01 covers `change.py apply`, not the brief `pair.py plan` returns. Closing that needs a later superseding change.

**6. Open questions**
- None needed to finish this task. For the owner's review: should R4b above be closed in the later change that holds the three open points?

## Case table

Each row was written before the edit. "Original" is the old test and "Corrected" is the new one. Every result below is from a run against the stand-in.

| Row | Input | Original | Corrected | Corrected vs original |
|---|---|---|---|---|
| R1 | Correct build: each brief's real path replaced by its own copy's path, C3 paragraph added once in the change arm | FAIL (2 differing paragraphs) | PASS | The defect fixed. The original fails every correct build. |
| R2 | C3 paragraph missing | FAIL | FAIL (briefs equal after the path is set aside) | Same |
| R3 | Two paragraphs added | FAIL | FAIL ("2 != 1 : exactly one paragraph differs") | Same |
| R4a | C3 text altered in its first words | FAIL | FAIL (`startswith` fails) | Same |
| R4b | C3 text altered after its first words | FAIL (only because of the path defect) | PASS | Weaker in verdict. Neither test looks past the first words. No other locked test catches it. |
| R5a | Another paragraph changed beside the path, in the change arm only | FAIL | FAIL ("2 != 1") | Same |
| R5b | Another paragraph changed beside the path, identically in both arms | FAIL (path defect only) | FAIL (control no longer equals the recorded brief with `<COPY>`) | Same verdict. The corrected test now fails it for its own reason. |
| R6 | Real path left in both briefs | PASS (wrongly: the old test has no path check) | FAIL (`assertNotIn` on the real path) | Stricter |
| R7 | Real path left in one brief | FAIL | FAIL (`assertNotIn` on the real path) | Same |

Only R4b is caught by no locked test. The old test passed R6 and now fails it.

The runs also confirmed that each corrected row fails for the intended assertion, as the failure messages in the table show.

Runs of the original test against the stand-in:
```
correct: FAILED (failures=1)
missing: FAILED (failures=1)
two: FAILED (failures=1)
altered_early: FAILED (failures=1)
altered_late: FAILED (failures=1)
other_one: FAILED (failures=1)
other_both: FAILED (failures=1)
real_both: OK
real_one: FAILED (failures=1)
```
Runs of the corrected test against the stand-in:
```
correct: OK
missing: FAILED (failures=1)
two: FAILED (failures=1)
altered_early: FAILED (failures=1)
altered_late: OK
other_one: FAILED (failures=1)
other_both: FAILED (failures=1)
real_both: FAILED (failures=1)
real_one: FAILED (failures=1)
```
Both sets match the predictions I wrote down before the edit.

## Diff of the test
```
@@ -95,8 +95,17 @@ class TestAC2(Base):
         self.make_entry("research")
         arms = self.plan("C3")
         self.check_copies(arms)
-        paras = [p for p in arms["change"]["brief"].split("\n\n") if p not in arms["control"]["brief"].split("\n\n")]
-        self.assertEqual(len(paras), 1)
+        ctl, chg = arms["control"]["brief"], arms["change"]["brief"]
+        for a, b in ((ctl, arms["control"]["copy"]), (chg, arms["change"]["copy"])):
+            self.assertNotIn(self.real, a, "the real repository's absolute path is replaced by the copy's")
+            self.assertIn(b, a)
+        ctl_c = ctl.replace(arms["control"]["copy"], "<COPY>")
+        chg_c = chg.replace(arms["change"]["copy"], "<COPY>")
+        expected_ctl = self.brief.replace(self.real, "<COPY>")
+        self.assertEqual(ctl_c, expected_ctl, "nothing but the path changed in the no-change brief")
+        self.assertNotEqual(chg_c, ctl_c)
+        paras = [p for p in chg_c.split("\n\n") if p not in ctl_c.split("\n\n")]
+        self.assertEqual(len(paras), 1, "exactly one paragraph differs")
         self.assertTrue(paras[0].startswith("A source you cannot open is not by itself a fault"), paras[0])
```

## Commit
- New commit id: `daa44a3577316e1394f23147bfef91e17db153ed`, on build/check-author/s001-ac2-research.
- The message ends with a trailer paragraph holding `Agent-Session: session_01QBwHGNGKXFwvVVdzkei5aT` and `Spec: S-001`. It has no model names and no co-author lines.
- `git log --format='%an %ae' -2`:
```
check-author check-author@agents.invalid
shumpmaster furchken@gmail.com
```
The second line is the base commit f5179378, which I did not author.
