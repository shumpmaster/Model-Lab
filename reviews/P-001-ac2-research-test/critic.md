Verdict: FAIL

*The Critic on questions/P-001-ac2-research-test.md, brief 93 (docs/briefs/93-critic.md, on branch claude/chief-of-staff-p001-build-5m9j1d) for round 1; a fresh session on a different model from the card's writer. Recorded verbatim by the Orchestrator, 2026-11-05. The first line is the latest round's verdict. One quotation in round 1, finding 1, is shown as [its verdict line, PASS], since the review check accepts that line's label only at the start of a line.*

## Round 1 (commit 4b34d74)

Two findings block the card. Findings 3 to 6 do not.

1. BLOCKING. The recommendation says "the three minor points stay set aside, as you asked." No cited record holds that instruction.
   - decisions/questions/P-001-checks-stop.md has the owner choosing "A: one focused round". It says nothing about setting these points aside.
   - decisions/questions/P-001-build-gate-stop.md is about cutting cards down.
   - reviews/51/owner.md holds only [its verdict line, PASS].
   - So the card states an owner judgement that is not on record, inside the Chief of Staff's recommendation. That blurs whose judgement is whose, and it leans the card towards A over B.
   - Fix: cite the owner's words, or drop the clause and say the Chief of Staff set them aside.

2. BLOCKING. The card misstates what the options rule out, and it misses a written rule.
   - The WHY says "no rule says how a locked check is corrected." tests/acceptance/README.md:4-5 does say it: "If a test here contradicts its spec, report the contradiction as a question; never edit the test." The Reviewer cites this line (reviews/S-001/_reviewer-build.md, section 1 and the contract), and the card does not.
   - The card also quotes the note at e003_support.py:4 ("Never edited once locked; a new spec supersedes it"). That note is the written route, and only option C follows it.
   - A and B edit a locked check without a superseding plan, so they depart from both written statements and set a precedent. Both are marked "Rules out: nothing", which is not fair. C is the only option that rules out nothing. D is the only one that ends the work.
   - Fix: say that the README rule is satisfied by filing this question, but that "never edit" is what A and B set aside by the owner's ruling. Put the departure in A's and B's cost or "rules out".

3. Not blocking. Several claims rest on records that do not say them.
   - "The Builder found this" has no cited record. The cited review only says the fault is in the test.
   - "On branch claude/chief-of-staff-p001-build-5m9j1d" is not in the record. The record names commit 3861b38 on build/builder/e003-harness.
   - The cited review is the Build-2 harness review, while the card says Build-1 (docs/PROJECT.md:60-61). The link is plausible but not explained.
   - The card says "Leaving it unruled holds the Build's review from passing." The same review is already FAIL for another blocking build defect, in transcript_check.py. It states "The FAIL rests on finding 1 alone". The owner should be told this check is not the only thing holding the review.

4. Not blocking. Context bullet 5 says "no record answers" whether a locked test can be corrected. reviews/51/reviewer.md round 2 says open question (a) "was answered by brief 79: they lock when #51 merges." That answers only the question of whether PR #51 was still before the lock. It does not answer the question after the lock. The card should say so rather than "no record answers".

5. Not blocking. The options lean a little towards A.
   - C's cost carries an argument: "a fault in a test… which the Builder and the Reviewer both found right".
   - LL-61 (each fix opened a new hole) is set against B only. The recommendation then calls A's risk "low" without saying what makes A's edit safe beyond the copied pattern.
   - The card has four options against the form's two or three. That is defensible, because D is the kill route the stop rule allows. It should still be said.
   - Citations checked and true:
     - The test lines 18-19, 46-48 and 94-100, and the sibling test at 74-80.
     - J2, E-001:102 and E-003:115.
     - The OPERATING_MODEL §4 quotes ("criteria or checks wrong → 3 or 4"; never accepting work despite a failed check).
     - M4 in docs/PROJECT.md:66.
     - B's three points, which sit in reviews/51/reviewer.md round 4 finding 4 and in triage finding 2.
     - AGENTS.md §1, line 34, for C's superseding entry.

6. Not blocking. Plainness and length.
   - The opening paragraph has no paths or ids and starts with what failed. That is good. It is about 190 words, longer than the five-line background the form asks for. It also leans on terms the owner may not carry in mind: "fair test", "the checks' writer", "source check's brief", "locked". It says what the owner decides only at its end.
   - The WHY and OPTIONS lines carry about 15 inline citations. The owner asked for cards cut to their decisions (decisions/questions/P-001-build-gate-stop.md). The citations could move to Context.
   - Whose judgement is whose is clear for the recommendation, which is labelled the Chief of Staff's.

Six-part contract
- Changed (by file): none. I have no write tool.
- Why: this is the cold read of questions/P-001-ac2-research-test.md against the decision-card standard (OPERATING_MODEL §2, Model-Lab AGENTS.md §4-5). It checks that each claim is true of its record, that the options are fair, and that the opening is plain and the card short.
- Verified (command + output): I read only. I opened the card and these records:
  - the cited lines of tests/acceptance/test_ac02_pair_start.py, tests/acceptance/e003_support.py:1-15 and tests/acceptance/README.md;
  - specs/S-001.md:264, experiments/E-001.md:102 and experiments/E-003.md:115;
  - reviews/S-001/_reviewer-build.md, reviews/51/reviewer.md (rounds 1-4) and reviews/51/owner.md;
  - triage/P-001-S-001-checks-round-5.md, docs/LESSONS.md LL-61 and docs/PROJECT.md, M4 and Build-1/2;
  - decisions/questions/P-001-checks-stop.md and P-001-build-gate-stop.md;
  - OPERATING_MODEL §2 and §4, and Model-Lab AGENTS.md §1, §4 and §5.
  I did not read docs/reports/**.
- Undone: I ran nothing. The Reviewer's reproduction of the failing test is taken from its record, not rerun. I could not see the branch claude/chief-of-staff-p001-build-5m9j1d. I did not check the card against the questions/_TEMPLATE.md form.
- Needed outside my surface: the Chief of Staff redrafts the card to fix findings 1 and 2, and ideally 3 to 6. A fresh Critic round then reads the new card.
- Open questions: should the owner be asked directly whether "never edit a locked test" yields to a correction with the owner's verdict? That is the real decision behind A, B and C, and the card does not state it.
