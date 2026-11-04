Verdict: FAIL

*The Reviewer on pull request #51 (R3), brief 78 (docs/briefs/78-reviewer.md); a fresh session on a different model from the locked checks' writer. Recorded verbatim by the Orchestrator, 2026-11-04. The first line is the latest round's verdict.*

## Round 1 (commit b991248)

The locked checks cover AC1 to AC11 and J1 to J8, and they are strict. But two of them would fail a correct implementation. The defects are hidden for now, because the code those tests call doesn't exist yet. Once the Builder builds it, a correct build would fail a locked check that can't be edited. The freeze and the PROJECT.md rewording pass.

**Findings**

1. **Blocking: AC6's re-scoring test expects the wrong answer.** test_ac06_owner_cards.py:132-141. The fixture pair p01 is (change FAIL, control PASS), so it scores n01. The owner's "no" on k01 sets k01 to PASS, which it already is. So p01 stays n01, and the count of n01 pairs is 1. The test requires p01 to be "concordant" and n01 to be 0. That contradicts E-003 Step 5 ("yes is FAIL, no is PASS"; the pair's class is worked out again from its two outputs). I reproduced it with an independent reference: `{c00: yes, k01: no}` gives `p01: n01`. Fix: answer "no" on c01, or "yes" on k01. The Critic's rounds missed this: round 2 did not re-read AC6, and no round ran anything.

2. **Blocking: J4's fill test needs a line break the template does not have.** test_j4_sheet_route.py:176-177 looks for the exact string "Judge it against". E-002's template breaks that phrase across two lines, "Judge it\nagainst:" (experiments/E-002.md:27-28). E-003 Step 4 says "Nothing else in the template changes". So a fill that keeps the template byte for byte gives `find("Judge it against") == -1`, and the test fails. I reproduced this by filling the template with E-003's seven changes only. Lines :180-181 have the same weakness for added text the Builder may wrap ("Do not start background tasks", "the numbers of the tests of the check that failed, each citing file:line"). Fix: collapse whitespace before matching.

3. **Not blocking: the Critic's round-3 finding 2 is unfixed.** J7 and J8 both read the same `S001_MANIFEST` variable (test_j7_analysis_pack.py:144, test_j8_holdout_pack.py:161). Reproduced: with the variable naming a well-formed blind manifest (the step J8's docstring and skip message ask for before each blind dispatch), J8 passes it and J7 fails it. So the full suite run before a blind dispatch goes red on a correct manifest. Running one file at a time works.

4. **Not blocking: the skips are legitimate.** review_check flags the `skipTest` lines in J7 and J8 as test weakening. Each skips only while no manifest of its own kind is recorded and the variable is unset. That matches S-001 J8 ("meaningful only once … the manifest is recorded"). The owner still needs to give a verdict on this flag.

5. **Not blocking: the merges check fails for a known, local-only reason.** `record_checks merges` reports 28 violations: orchestrator record commits with no `Item:` trailer. This is the local false failure LL-29 describes; CI judges only the merge commit. It is not caused by this change.

6. **Not blocking: AC9's mixed-model case reads E-003 one way.** test_ac09_model_change.py:230-235 has the analysis leave out a pair whose arms report different served models. E-003 Exclusions 7 calls that a set-up fault, which Reruns (b) reruns once before judging. The test's reading holds only for a pair still mixed after its rerun; the docstring should say so.

**What I confirmed (the four items you asked for)**
- **Item 1, the suite:** 228 tests ran: 43 pass, 2 skip, 183 fail, 0 errors. Every one of the 183 failures says "interface missing: src/E-003/<script> is not built yet". Ten of the eleven scripts the docstring names are the ones that fail: analyse 20, block 12, cards 17, change 19, counts 13, export 15, judge 12, kind 8, pair 32, transcript_check 14, verdicts 21. fill_judge_brief.py is the eleventh; its tests stop first at export.py. The 43 tests that need no Builder code all pass (AC1, the AC4 repository checks, the AC7 and AC10 reference figures, J7/J8 entries, extract and validation). The tests have not changed since the Critic's round 3 (`git diff d372707 HEAD -- tests` is empty).
- **Item 2, the freeze:** the only change since f4298cd is setting the freeze lines. They agree at S-001:3, S-001:365 and E-003:132, each with the full f4298cd id. The nine rulings match the two answer records and the terms card at 2350130. The PROJECT.md pointers that failed the Critic's round 1 are corrected (:108, :111, :99, :159).
- **Item 3, PROJECT.md:** V1 at :108 is byte-identical to the plan's proposal (S-001 at 2350130, :334). M2 at :57 carries the proposed "done when" exactly. The "about 300 runs" line is restated. The lines still saying "past tasks" are statements made at the time (31, 129, 134, 141, 146), as the Critic's round 2 found.
- **Item 4, `bash governance/checks/check_all.sh . 2350130 51`:** 23 checks pass and 2 fail, and it ends "Governance checks FAILED". `review_check pr 51` fails because the R3 class needs reviews/51/owner.md and reviews/51/reviewer.md, which don't exist yet; that is expected. `record_checks merges` fails as in finding 5.

**Six-part contract**
- **Changed:** none. I edited nothing; my only scripts and fixtures are in /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/rev51/.
- **Why:** PR #51 touches tests/acceptance/**, class R3, which needs the Reviewer's verdict and the owner's.
- **Verified:**
  - Ran the acceptance suite and tallied every failure message.
  - Ran check_all and read both failing sections.
  - Read every test file and e003_support.py.
  - Read S-001 in full; E-003; E-002's template; both answer records; the terms card at 2350130; the three Critic records; the PROJECT.md diff.
  - Reproduced findings 1 to 3 with these scratchpad files:
    - /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/rev51/rescore_ref.py
    - /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/rev51/faithful_fill.py
    - /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/rev51/blind-brief.md
  - Compared V1 and M2 byte for byte with /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/rev51/cmp.py.
  - Did not read docs/reports/**.
- **Undone:**
  - The PR's Tasks section is not in the fixed copy, so I could not check its ticks against the work.
  - I did not verify the facts S-001 cites from the portfolio library, which is not in the copy.
  - No join-up review section: this is the Build-1 checks review, not the end-of-Build review, and the project has no screens or views.
- **Needed outside my surface:**
  - The Check author (dispatch (b)) fixes findings 1 and 2, and should fix 3, then a Critic round checks them.
  - The owner gives a verdict on PR #51, including the skip flag in finding 4.
- **Open questions:**
  - (a) A locked test can't be edited once locked. Is PR #51 still before the lock, so the Check author can correct these tests here, or does correcting them need a superseding spec?
  - (b) Should J7 and J8 each get their own manifest variable (finding 3)?
