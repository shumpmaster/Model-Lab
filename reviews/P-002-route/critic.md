Verdict: FAIL

*The Critic on the route card for the screening's start (questions/P-002-route.md, never committed; its round-3 wording is kept in intake/P-002-route-card-r3-2026-11-08.md), three rounds on 2026-11-08, each a fresh session on a different model from the card's writer, started by the Chief of Staff (session_01QBwHGNSLmSrYQgS6BPjV8p). Each round's return is recorded verbatim. The card reached the three-round limit without a pass (OPERATING_MODEL §4 "Stop rule"); the cause is in docs/LESSONS.md (LL-69) and the stop card is questions/P-002-route-stop.md. Each round's own verdict line is recorded as "The round's verdict was …", so the file keeps one verdict line (LL-68).*

## Round 1 (uncommitted draft)

The round's verdict was FAIL. The card is well formed, but three factual claims that carry the recommendation do not hold against the records. I opened every Context source and checked the opening paragraph and options against them.

Findings (blocking unless marked):

1. BLOCKING. Opening paragraph and option B: "a map ... reads and writes nothing the checks look at" and "the upgrade and the map touch nothing of each other's".
   - The records say otherwise. In this repository's checks, a groundwork request is a research question file, research/Q-nnn.md, which is on the orchestrator's allowed-paths list (governance/checks/record_checks.py:88 and 508).
   - The question's dispatch and log lines make it a "groundwork" item (governance/checks/v3_checks.py:853).
   - Those items feed the "Discovery-3" milestone, the expert's-questions-answered one (v3_checks.py:975-1010, 1116).
   - The card also cites no record for the "touches nothing" claim. Option B rests on it, and so does the "map is needed whichever way" reasoning.
   - Why it matters to the owner: B's safety argument is unsupported. The map is the exact piece of work that would start under the old checks.

2. BLOCKING. Opening paragraph and Context line 21: "Bringing this repository up to it changes the checks only", and "a repository with one project sees no change in any check's output" (also the BLAST RADIUS line "prompt engine's plan reads unchanged").
   - The CHANGELOG 3.7.0 sentence is real: "A project with no later item sees no change in any check's output". But the upgrade is to 3.7.2, and Context line 21 cites only 3.7.0.
   - 3.7.1 changes the check run's packed copy. Design images are left out, large text files go in, and a new "Left out of the check run's copy" section appears in the check record. 3.7.1 also needs a change to the workflow line, which is under .github/**. (CHANGELOG.md 3.7.1 and 3.7.2.)
   - The Service Desk's sync, which the card cites as precedent, also changed PACKS.toml, BRIEFS.toml, SURFACES.md, the builder, critic, definer and researcher cards, docs/SETUP.md, the gate and profile templates, and the workflow (Service-Desk docs/LEDGER.md L-0022 and L-0023). That is more than "the checks only".
   - Why it matters to the owner: the owner is asked to merge an R3 change and is told its footprint is smaller than the records show. The "nothing changes beside the prompt engine" comfort is overstated, and it is what separates B from C.

3. BLOCKING. Recommendation, second sentence: "In every option the upgrade merges only after the prompt engine's first weekly landing if that landing is open at the same time".
   - This is a new condition that appears in none of the options.
   - It conflicts with A's stated cost ("likely a day or more"), because it can lengthen A's wait.
   - It also removes C's only stated gain ("no check changes under the prompt engine before its first landing"), because that gain would then hold in every option. So C is weakened by the recommendation's own rule, and the options are not fairly put.
   - Why it matters to the owner: the options are not independent and their costs are not what they read as.

4. Non-blocking. Option C and the handoff.
   - The handoff (docs/handoff/2026-11-08-chief-of-staff-14.md) says the Orchestrator's weekly task is not yet created. Briefs 124 and 125 are not yet on main, and "one pull request a week" is only "the Orchestrator's reading".
   - The first landing therefore has no date, and C's "a week or more later" may understate the wait.
   - Context line 25 says the landing's "next step" is simply the landing. The handoff lists creating the scheduled task first.

5. Non-blocking. Form.
   - The template and D-019 ask each option to state gain, cost and reversibility. A and B give no gain, and none of the three gives its own reversibility. They all say only "Rules out: nothing".
   - The card says "WHO HAS CHECKED IT: the Critic checks this card" and names no one else.
   - The recommendation says "medium confidence", which is fine.

6. Non-blocking. Plain English (S-026).
   - The opening paragraph is about eight sentences, against the limit of five lines of background.
   - Jargon is left unexplained: "locked checks", "held-back sheets", "groundwork map", "R3", "R0", "LL-16", "Discovery", "plan of its own", "Monday landing pull request".
   - The milestone line is acceptable: "Milestone: none (…)" matches the template form. The template's DEFAULT field wants a letter. "none" with a reason is acceptable because starting a project is the owner's to rule.

7. Non-blocking. Unfair wording in B's cost.
   - The cost reads "the map waits on it, unused", which is vague. It does not say whether the map is lost or merely idle.

Claims confirmed against the records:
- The owner ruled one shared repository, with Model-Lab archived once both ideas are in (decisions/questions/P-001-work-repo.md).
- The owner's order (prompt engine first, then the screening) and the 2026-11-08 kick-off request are in the portfolio's ideas/IDEAS.md.
- Model-Lab runs 3.6.0 (governance/OPERATING_MODEL_VERSION), and the model is at 3.7.2 (VERSION).
- LL-16 is open in docs/LESSONS.md.
- governance/** is R3 in governance/risk-paths.toml, and questions/** is R0.
- The Service Desk adopted 3.7.0 and 3.7.2 by byte-for-byte copying of the checks, keeping its own lines, in pull requests the owner merges (LEDGER L-0022 and L-0023).
- The prompt engine's built-work comparison and work session match the handoff.
- The groundwork-before-research-questions step is in OPERATING_MODEL.md §4. The long lines in §3 and §4 were truncated in my tool output, but the CHANGELOG supports the "one plan per project item" claim.

Could not verify: Context line 26 ("no open pull requests on 2026-11-08") comes from the GitHub pull-request list, which I cannot open. I did not fail it. The handoff does mention PR #69, with the owner's PASS recorded.

Tokens used: not visible to me.

## Round 2 (uncommitted draft)

The round's verdict was FAIL (round 2). One blocking finding. The card's footprint wording is much better than before, but the recommendation's evidence and option A's "no change in any check's result" claim are not supported by the records.

I opened every Context source except the GitHub pull-request list, which I cannot open. I did not fail the card on that line alone.

**Sources that say what is claimed:**
- The owner's ruling in P-001-work-repo.
- The IDEAS entries for 2026-11-01 and 2026-11-08.
- The versions: Model-Lab 3.6.0, model 3.7.2.
- The 3.7.0 change note and OPERATING_MODEL §3: "A second idea always has a plan of its own."
- The v3_checks.py groundwork and Discovery-3 lines: lines 849-854 and 975-1010 do match groundwork research to a project and count it toward Discovery-3.
- LL-16 is open.
- The risk-paths entry for governance/** as R3.
- The handoff: a daily wake, and the weekly landing task still to be created once briefs 124 and 125 are on main.
- The 3.7.1 and 3.7.2 change notes as summarised in the context line.

**Findings**

1. **RECOMMENDATION line, "the Service Desk's two upgrades show no change in check results for a single project". Blocking.**
   - The desk was not a single-project repository when it took 3.7.0 and 3.7.2.
   - Its ledger entry L-0022 records that P-003's and P-004's "Discovery-2 and Discovery-7 now read not recorded". That is a change in check results.
   - L-0023 was done so the card fix's first check run would not "fail on nine lines that are not the builder's". That is also a changed check result.
   - So the desk's records neither show nor contradict "no change for a single project". The recommendation cites evidence that does not say that.
   - The owner is relying on this reason for medium confidence in A.

2. **Option A, Cost: "whose change notes say a one-project repository sees no change in any check's result, while the check run's copy and the pipeline's workflow do change". Blocking.**
   - The "no change" sentence is only in the 3.7.0 note, not in 3.7.1 or 3.7.2.
   - 3.7.1 changes what the checks are given to read: design images are left out and large text files are let in.
   - 3.7.2 turns one check from a failure into a note wherever a copy's history is cut short. The check run's copy is such a copy, per the note itself.
   - Both are changes to what checks report in the prompt engine's first landing. The card's own Context line 21 says so, but option A's cost, which the owner will weigh, says the opposite.
   - This is the same kind of understatement as the earlier round, now in the cost line.

3. **Footprint claim in the opening paragraph and BLAST RADIUS: "the prompt engine's plan, experiments and tests are not changed". Non-blocking.**
   - The prompt-engine acceptance tests load governance/checks/session_runner.py and govlib.py as their reference code (tests/acceptance/e003_support.py, lines 114-135).
   - The upgrade replaces those files; L-0023 shows session_runner.py is among them.
   - The test files stay the same, but what they run against changes. One clause saying so would make the claim fair.

4. **Plain English (S-026, D-019). Non-blocking.**
   - The opening paragraph runs to about six dense lines.
   - It uses terms a non-expert cannot read cold: "check run's copy", "pipeline's workflow", "pack lists", "the files its agents are given", "weekly landing" (never explained), and "Discovery".
   - The WHY line carries a bare record id, "LL-16".
   - The paragraph says what changes but not, in one plain sentence, what the owner will see (a pull request to merge).

5. **Option A, Gain: "the screening starts within days". Non-blocking.** No record gives a timescale. The "days" figure is an estimate and should be marked as one.

6. **Option B, Cost. Non-blocking.** The wait having no date is supported by the handoff. The "week or more" figure is the Chief of Staff's guess and should be marked as one. Fairness is otherwise acceptable: both options carry a gain, a cost and reversibility, and A is not presented as the only reasonable choice.

7. **DEFAULT: none / TIMEOUT: none. Non-blocking.**
   - AGENTS.md §5 says reversible questions adopt the recommendation at timeout.
   - The card is entered as reversible but sets no default, with the reason "starting a project is yours to rule".
   - The reason is sensible. But the card does not say plainly that, if the owner does not decide, nothing starts and the idea stays held. The WHY line only partly covers this.

8. **Context last line, source "the GitHub pull-request list, read in session_01QBwHGNSLmSrYQgS6BPjV8p". Non-blocking.** I cannot verify it. The source named is a session, not a record, so the owner cannot check it either. Note it as an unrecorded observation.

**Form check:** the template's fields and the D-019 parts are all present. The "Milestone: none" line has a reason. The risk class R0 for questions/** matches risk-paths.toml.

## Round 3 (the wording kept in intake/P-002-route-card-r3-2026-11-08.md)

The round's verdict was FAIL. There are two blocking findings (1 and 2). Both are about how much of the work the tests actually guard and how large the upgrade is. Everything else is non-blocking.

**What I confirmed**
- Every Context source opens and says what the card claims. This covers:
  - the owner's ruling (P-001-work-repo)
  - the IDEAS entries for 2026-11-01 and 2026-11-08
  - the versions (3.6.0 in Model-Lab, 3.7.2 in the model)
  - CHANGELOG 3.7.0, 3.7.1 and 3.7.2
  - v3_checks.py lines 849-854 and 975-1010
  - e003_support.py lines 116-131
  - LL-16
  - the R3 rule for governance/** (risk-paths.toml)
  - the handoff's "Next, in order" (weekly landing task still to be created, daily wake running)
  - Service Desk L-0022 and L-0023 (as now worded, the card no longer claims "no change in any check's result")
- The byte comparison could not be repeated with cmp, because I have no shell.
  - The nearest checks agree with the card. Five of the six scripts differ in line count (e.g. v3_checks 2763 against 3156, orchestrator_git 4029 against 4069).
  - govlib.py has the same line count (1191) but lacks the "S-035" marker the model's copy carries, so it differs too.
  - The card should still keep "not yet in a record".
- I did not check the "no open pull requests" line. The handoff mentions a pull request #69, so it should be confirmed against GitHub.

**Findings**

1. **Line 11 (RECOMMENDATION reason and "what would change it"). Blocking.**
   - The card says the before-and-after test condition "protects the prompt engine's running work directly". It also speaks of a change "its tests show changes nothing".
   - The only prompt-engine tests that touch the replaced scripts are in test_j7_analysis_pack.py and test_j8_holdout_pack.py. They reach govlib.glob_match and session_runner.norm through e003_support.py (lines 130-135, 343-345). The other acceptance tests and the tests/E-003 tests never load governance/checks.
   - Nothing tests v3_checks, orchestrator_git, orchestrator or governance_checks. Those are the scripts behind the costs the card names: images left out, large files let in, the history-cut-short note.
   - So a pass on the test condition says almost nothing about how the first landing will be checked. The owner is told the condition is the main protection when it covers only the pack-matching helpers.
   - The recommendation rests on that condition and on B having no date. The first half is overstated, and the recommendation reads stronger than the evidence allows.

2. **Line 5 (opening paragraph; also line 13 BLAST RADIUS) and the "two of its tests" claim. Blocking on the footprint, non-blocking on the count.**
   - On the count: "two of its tests" is true only if it means two test files. j7 and j8 hold roughly 6 and 11 checks that use the helpers, so "two test files" or "tests in two files" would be accurate. Read as two single tests, it understates.
   - On the scripts: the claim itself is fair. Two scripts, session_runner.py and govlib.py, are loaded by the tests, and both are replaced.
   - On the footprint: the opening says the upgrade replaces "rule-checking scripts and some agents' instruction files". Line 26 (the Service Desk precedent) shows the same upgrade also carried template changes into the packs, briefs, surface map, setup, gate and profile forms, and the workflow.
   - The packs file, governance/PACKS.toml, is read by the same tests (e003_support.pack_entry, line 337, and the j8 holdout-pack test). That makes it a second path by which the upgrade could change those tests' results.
   - The opening should say the upgrade may also change the pack and brief definitions the tests read. As written it implies the footprint is only scripts and agent files, and a round-1 failure on this point is only half fixed.

3. **Lines 9-10 (the timing estimates). Non-blocking.**
   - "Within a few days" for A and "a week or more" for B are given as estimates, but no basis is shown. Only B's undated schedule is evidenced (the handoff).
   - How long the upgrade takes to build and review is not stated anywhere in the records.

4. **Line 9 (A's cost) against line 24. Non-blocking.**
   - A's cost lists three behaviour changes, but says the pass condition is "every prompt-engine test the same". The owner may take that to mean all the changes are guarded.
   - Add one clause saying the condition does not cover the check scripts. This follows from finding 1.

5. **Lines 3, 5, 9 (jargon). Non-blocking.**
   - "The model", "Discovery", "R0/R3", "landing" and "main line" are only partly explained for a non-expert.
   - "The model's newest version" in the opening should say it is the operating model.
   - "Its Discovery begins" is never explained.

6. **Lines 12-14 (form). Non-blocking.**
   - "WHO HAS CHECKED IT" is not in _TEMPLATE.md.
   - DEFAULT and TIMEOUT read "none", while AGENTS.md §5 says a reversible question adopts the recommendation at timeout. The reason given (starting a project is the owner's call) is sound, but the departure from the form should be stated as deliberate.

7. **Fairness of options. Non-blocking.**
   - Apart from findings 1 and 4, A and B are put even-handedly. The recommendation is labelled medium-low confidence, the judgement is attributed to the Chief of Staff, and a condition that would flip it is given.
   - The earlier merge-timing skew is gone.

Files: /home/user/Model-Lab/questions/P-002-route.md and /home/user/Model-Lab/tests/acceptance/e003_support.py.
