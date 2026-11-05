# Triage — S-001's locked checks, at the stop after the Critic's round 5 and the Reviewer's round 3

*Triage's return (brief: docs/briefs/85-critic-triage.md), a fresh Critic session on claude-opus-5-5, verbatim. Recorded by the orchestrator. Session session_01QBwHGJ9ZMyT9fK17HjfmCc, 2026-11-05.*

Triage on P-001 / S-001: the locked checks after round 5 (fixed copy fix-stop, Model-Lab at 04edf28, PR #51 head)

## Findings

**1. The failure chain and its root cause**

There were eight rounds. Each one moved J7's and J8's record selection, and each fix made the next hole:
- **Critic round 1 (e0d8104):** J7 chose records by their whole text, so it took the blind manifest (which lists reviewer.md) for its own and failed it. The fix was to classify by parsed file lines.
- **Critic round 2 (742ef89):** a named record that was malformed (kind None) was skipped by both tests. The Critic proposed checking the named record whatever it holds.
- **Critic round 3 (d372707):** checking whatever is named means one shared `S001_MANIFEST` fails a correct blind manifest in J7, and a correct analysis manifest in J8. This was not blocking. The proposal was "own kind or None", or "give each test its own variable" (open question (a)).
- **Reviewer round 1 (b991248):** the same shared-variable point, not blocking. Open question (b) asked for separate variables.
- **Check author, 0030fcb:** chose "own kind or None".
- **Reviewer round 2:** PASS on four fixtures. No mixed record was tried.
- **Critic round 4 (0030fcb):** `manifest_kind` tests for "analysis" first, so a blind manifest that also lists E-003.md is skipped by J8. Blocking. The proposal was "markers, or kind is None". The Critic flagged this against its own round-3 proposal.
- **Check author, bef590a:** wrote "or not has_files" instead of "kind is None".
- **Critic round 5 and Reviewer round 3 (2555c21), independently:** a record with file lines but neither marker is skipped by both tests. Blocking.

**Root cause.** The checks use one shared `S001_MANIFEST` variable, so each test has to work out from the record's contents whether the named record belongs to its own dispatch. That cannot be right for every record:
- Round 3's "check everything" fails correct manifests in the other test.
- Every filter since then skips some faulty record. A skip exits 0, so it reads as a pass at E-003:33's gate ("J8's test passes on it").

**Originating stage: 4 (the checks).** The spec is not wrong, so this is not "criteria were wrong". Two other causes contributed:
- **Stage 3 left a gap.** S-001:269-270 say "the dispatch's recorded manifest" but not how a test is told which record that is. Brief records have no field naming the dispatch (docs/briefs/README.md:6-10).
- **The reviews (my role's own earlier checks).** Separate variables were raised three times (Critic round 3 (a), Reviewer round 1 (b), Critic round 4 (a)) and never decided. Every round proposed a one-line patch and checked it only against the case it named (LL-61). Two of the holes came from the Critic's own proposals: round 3's led to round 4's hole, and round 4's, narrowed, led to round 5's.

**Self-implication flag (D-050):** this trace finds fault with the Critic's rounds 3 to 5, which are checks by my own role. It also finds a gap in the fix round 5 proposed (finding 3).

**2. Is the blocking finding confined to J7 and J8?**

Yes. Every other blocking finding is resolved:
- Critic round 1, findings 1 to 4;
- Critic round 2, finding 1;
- Reviewer round 1, findings 1 and 2;
- Critic round 4, finding 3.

Nothing else blocking remains, going by the records. I re-read only J7, J8 and e003_support.py.

Non-blocking findings still open:
- **The /tmp interface note (e003_support.py:51-52):** "Edit" counts as creating a file, which is wider than F4; and `cp`, `tee` and `mktemp` are left out, which is narrower. It should say "for example" and drop Edit (Critic round 5 finding 4; Reviewer round 3 finding 4).
- **Docstrings:** J7:15-18 and J8:14-17 say the named record is checked, but either test can skip it. No synthetic test exercises `manifest_markers` or the named-record selection (Critic round 5 finding 5).
- **Scan mode** (variable unset): a mixed record is checked by J7 only, and a record with no marker by neither (Reviewer round 3 finding 3).
- **AC1's needle at :99** could fail a future brief that quotes C3 (Critic round 2).
- **J4's "the check in full"** is now matched with whitespace collapsed. This is slightly weaker; it was accepted.
- **Cases not tested** (Critic round 2 finding 10):
  - AC2 "records the pair";
  - "is listed", where only `reason` is checked;
  - J2's two-lane piece;
  - J3, a deliverable that names the change;
  - J7, the power of a kind stopped at a review point;
  - a write under /etc being refused.
- **The skipTest flags** need the owner's ruling.
- **`record_checks merges`** fails for a local-only reason (LL-29). Not caused by this change.

**3. The one-line fix leaves a hole**

The fix both reviewers propose (J8 `blind or not analysis`, J7 `analysis or not blind`) meets every row except two cells (see the table). Those two cells cannot be settled from the parsed state at all.

The one that blocks: a blind manifest, named for the blind dispatch, that holds experiments/E-003.md in place of the extract and leaves out check-author.md. Its markers are (T,F,T), so J8 run alone skips it with "of the other kind (J7's)".
- S-001:270 requires a fail: it "lacks the extract", and the blind pack holds "never … experiments/E-003.md".
- The sheet lead builds the folder from the manifest, so the transcript check would not catch the read.
- This is the round-5 example with E-003.md in place of specs/S-001.md. It is the same class that rounds 4 and 5 called blocking, and the worst leak, because the registration names the changes.
- No version since round 1 has closed it.

The twin cell (B, J7) is milder. J8 fails such a record in the full suite, and J7 is not a stated dispatch gate.

A design that meets every cell is one variable per test, for example `S001_BLIND_MANIFEST` and `S001_ANALYSIS_MANIFEST`:
- Each test checks its own named record whatever it holds.
- Each test ignores the other's variable.

## Case table (S001_MANIFEST set; markers from parsed file lines only: blind = the extract or check-author.md, analysis = experiments/E-003.md)

| Named record's parsed state | J8 must | J7 must | Now, at bef590a (J8 / J7) | Proposed fix (J8 / J7) |
|---|---|---|---|---|
| A. No file lines (no section, no block or two blocks, no line parses) | check and fail | check and fail | check-fail / check-fail | check-fail / check-fail: meets |
| B. File lines, blind marker only | check: pass if every path is allowed and the extract is present, otherwise fail | skip (J8's record). But if it is the analysis dispatch's record: check and fail (no E-003.md) | check / skip | check / skip: meets, **except when the record is the analysis dispatch's** |
| C. File lines, analysis marker only | skip (J7's record). But if it is the blind dispatch's record: **check and fail** (lacks the extract; holds E-003.md) | check: pass or fail on its merits | skip / check | skip / check: **fails the requirement when the record is the blind dispatch's** |
| D. File lines, both markers | check and fail (E-003.md withheld) | check and fail (the extract or check-author.md is not allowed) | check-fail / check-fail | check-fail / check-fail: meets |
| E. File lines, neither marker | check and fail (no extract) | check and fail (no E-003.md) | **skip / skip** (the open finding) | check-fail / check-fail: meets |

Code basis: J8:165-169, J7:147-151, e003_support.py:496-503 (`manifest_markers`), :464-480 (`recorded_manifests`), :295-331 (`parse_manifest`), J8:36-45 (`holdout_problems`), J7:35-47 (`analysis_problems`).

## Summary for the owner (149 words)

What failed: two of S-001's locked checks, J7 and J8, cannot pick which recorded pack list to test. Both read one shared setting and guess a list's kind from its contents, and every guess lets some faulty list be skipped, which reads as a pass. Even the fix both reviewers propose would skip a blind list holding E-003.md in place of the extract: a leak. Nothing else blocks.
Re-specify: S-001's J7 and J8 are revised to say how each test is told which dispatch's list it checks (one setting each), with the case table; the checks are rewritten once.
Re-scope: J7 and J8 stop testing named lists; the sheet lead checks each list by hand, a weaker gate.
Drop: S-001 stops; E-003 is not run.
One focused confirmation review: the Check author gives each test its own setting, and one review runs every table row; a failure returns here.

## Six-part contract
- **Changed (by file):** none. I am read-only.
- **Why:** the stop was reached on S-001's locked checks after eight rounds. Triage traces the chain and its root cause, and gives the owner one summary (OPERATING_MODEL §4, "Stop rule" and "Feedback routing").
- **Verified:** by reading only, in fix-stop:
  - reviews/S-001/_critic-checks.md (all rounds) and reviews/51/reviewer.md (all rounds);
  - test_j7_analysis_pack.py and test_j8_holdout_pack.py in full;
  - e003_support.py:1-75 and :290-511;
  - specs/S-001.md:200-206 and :268-270;
  - experiments/E-003.md:28-37;
  - docs/briefs/README.md;
  - docs/LESSONS.md LL-55 and LL-59 to LL-61;
  - OPERATING_MODEL.md §4, in Personal-Org-Operating-Model.

  I worked the case table by hand from the code.
- **Undone:**
  - I ran nothing, because I hold no shell. The cell (C, J8) under the proposed fix comes from reading the code, not from running it.
  - I did not re-read the non-J7/J8 test files. "Nothing else blocking" rests on the review records.
  - I did not read docs/reports/**, docs/handoff/** or sessions/**.
- **Needed outside its surface:**
  - The owner picks a stop-rule route.
  - Whatever the route, a fix should be checked against every row of the table above, and a review should run them, not only read them (LL-60, LL-61).
  - The Orchestrator records this return as triage/P-001-S-001-checks-round-5.md.
- **Open questions:**
  - (a) Is a skip whose message names the other kind acceptable for cell (B, J7)? It is not acceptable for (C, J8), by the standard rounds 4 and 5 applied.
  - (b) Does LL-55's open rule on counting check rounds now cover locked checks (LL-61)?

Files:
- /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-stop/tests/acceptance/test_j8_holdout_pack.py
- /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-stop/tests/acceptance/test_j7_analysis_pack.py
- /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-stop/tests/acceptance/e003_support.py
- /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-stop/specs/S-001.md
