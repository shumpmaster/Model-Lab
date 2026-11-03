Verdict: PASS

The Critic's cold read of the two owner questions, questions/P-001-design-gate.md and questions/P-001-accept-m1.md, on a different model from their writer (brief: docs/briefs/20-critic.md), verbatim: round 1 (FAIL), round 2 (PASS). Recorded by the orchestrator. Session session_01QBwHGN4kVVA3rfHx2b4FsF, 2026-11-02.

## Round 1
Verdict: FAIL
Design gate: FAIL
Accept M1: PASS

Both questions are mostly accurate against their records. The Design gate question fails on two blocking points: option D states something no record holds, and the options are not put evenly. The M1 question has no blocking findings.

DESIGN GATE (questions/P-001-design-gate.md)

1. BLOCKING. Option D says "the lessons log still goes to the operating model" if the project is killed. No record says this.
   - decisions/questions/P-001-lessons-log.md says each open entry is corrected "in the result that is integrated into the operating model" at the end of the cycle, as M5 and M6.
   - A kill ends the project before M5 and M6. docs/PROJECT.md says only that a miss on V1 closes the project, and that the record of each agent's brief and model (M3) still goes in.
   - The claim is a promise the records do not hold. Either cite a record or remove it.

2. BLOCKING. The options are not put evenly, and A's cost is hidden.
   - Only A has a stated gain and reversibility ("Reversible: yes; nothing is spent beyond your plan").
   - A's real cost is not named: it uses up to 40 of the 100 test runs in Design, per decisions/questions/P-001-open-unknowns.md and docs/PROJECT.md section 8. Those runs cannot be un-spent, so "reversible" needs that qualifier.
   - B, C and D state no cost and no reversibility. For D, a kill, the owner cannot tell from the card whether it can be undone.
   - The decision-card standard (§2) asks for gain, cost and reversibility on each option. The earlier P-001-open-unknowns card had the same defect, and the Critic ruled it blocking there (reviews/P-001-open-unknowns/critic.md, finding 3).

3. Non-blocking. WHY says "you have ruled on everything it raised". The companion ask, P-001-accept-m1, is still unanswered, and it is the owner's to rule. Say "everything it raised in Discovery except the M1 acceptance below", or drop the clause.

4. Non-blocking. The card never says what happens if the owner does not decide. DEFAULT and TIMEOUT "none" are right for a phase gate (§2 and §4: phase moves are never delegable). One clause saying "nothing moves" would complete the card; option B says it only for the hold.

5. Non-blocking. Some terms are unexplained for a cold reader: "readiness check", "replay and judge-consistency checks", "fair test", "value targets", and "the Discovery and Design lines" (these are the standard-milestone lines in docs/PROJECT.md section 3). The first sentence of WHY, "Discovery is done", is in plain English.

6. Non-blocking. RISK CLASS "R2 (a phase gate; reversible)" is not computed from paths, as the template says. governance/risk-paths.toml puts docs/**, decisions/** and questions/** in R0. The label is a judgement. The same applies to "R1" on the M1 card.

7. Claims that hold:
   - The brief passed the Critic's readiness check, round 2 PASS (reviews/P-001-ready/critic.md).
   - The three open unknowns each have a test and a fallback, and the owner accepted them (decisions/questions/P-001-open-unknowns.md).
   - The owner ruled to go on (decisions/questions/P-001-after-the-count.md).
   - "Within 40 of your 100 test runs" matches the open-unknowns ruling and PROJECT section 8.
   - The Build gate and test-budget steps, and the milestones M1 to M6, match docs/PROJECT.md and the case.
   - Nothing is presented as the owner's view without a record; the recommendation is labelled the Chief of Staff's judgement.
   - The "WHO HAS CHECKED IT" mention of the gate Critic view is excluded from this judgement, as instructed.

ACCEPT M1 (questions/P-001-accept-m1.md)

8. Pass: option A fits the milestones check. In governance/checks/v3_checks.py, `reached_licence` requires the question's option for the owner's letter to begin `<letter>. accept` after its indent and to name the milestone id whole. The line `  A. accept M1 as reached — …` matches (OPTION_LINE_RE, then `accept\b` and `_whole("M1", …)`). The file's name, `P-001-accept-m1`, matches the record name the check requires, and the check reads the question from the tree before the record was added.

9. Pass: DEFAULT none and TIMEOUT none are right. §3 says only the owner's ruling, never a default, adds or removes a reached mark. The check treats a "(defaulted)" ruling as never counting.

10. Pass: the figures match their records.
   - The question's figures match PROJECT section 6, and the memo's first-try table gives the same totals:
     - plans 2 of 44 (1 of 17, 1 of 23, 0 of 3, 0 of 1);
     - research 5 of 19;
     - built work 32 of 80;
     - Critic 1 of 20.
   - 61 of 84 matches memo bottom line 3 and PROJECT U5.
   - The Source checker's round 2 is PASS (research/Q-008-source-check.md).
   - The Critic passed M1's wording in both rounds (reviews/P-001-open-unknowns/critic.md).
   - The §3 context ("only once the milestones are approved") and the reopen route for reversibility both hold.

11. Non-blocking. The delivered figures are given as headline numbers only, but PROJECT section 6 carries alternates:
   - research is 2 of 19 if a later-added check counts;
   - built work is 27 of 75 without the five single-pass pull-request files.
   Because the card says "high confidence", one clause noting that some counts are small and have alternates would keep it candid. The card does say what the records cannot show (61 of 84 name no cause), but not the further 41 returns with no record of findings.

12. Non-blocking. Options A and B are even in form, but B states no cost and no timing. A clause such as "the project waits on the extended count" would balance them.

13. Non-blocking. The Source checker's round-2 remaining slips (the memo's "unchanged" wording and the S-002 note) were handled in the memo. At line 27 the memo discloses that §1.3 and §1.4 were edited, so "all source-checked" stands.

## Round 2
Verdict: PASS
Design gate: PASS
Accept M1: PASS

I re-read both question files cold, and the current case (docs/gates/P-001/design-gate-3-case.md) beside them. Every round-1 blocking finding is fixed. What remains is non-blocking.

DESIGN GATE (questions/P-001-design-gate.md)

1. Resolved (was blocking 1, the lessons-log claim). Option D now says nothing of the project reaches the operating model, "since its results move there only at the end of the cycle". That follows from M5's "done when" in docs/PROJECT.md section 3. No lessons-log promise remains. Non-blocking: PROJECT section 6 says a no-change miss still sends the brief-and-model record (M3) into the model. That is a different path from a kill at this gate, and the card's "nothing" is correct for a kill now.

2. Resolved (was blocking 2, uneven options). A, B, C and D each state gain, cost and reversibility.
   - A names its cost: up to 40 test runs and their tokens, which cannot be taken back. That matches decisions/questions/P-001-open-unknowns.md and PROJECT section 8.
   - D is marked not reversible as this project.
   - Non-blocking: A's gain, "the work goes on now", is thin beside the other options. The REVERSIBILITY header says "A, B and C reversible", while A's runs are not; the option line itself says so, so the header only needs "(except the runs used)".

3. Resolved (was 3). WHY now names the M1 question beside it, and says that if you do not decide, nothing moves.

4. Resolved (was 4 and 5). The terms are explained in line: the readiness check, "value targets (the gains it must show)", the fair test, and the replay and consistency checks. The standard Discovery and Design lines are now "the lines saying which of the model's standard Discovery and Design milestones it takes on".

5. Resolved (was 6). RISK CLASS R0 matches governance/risk-paths.toml (docs, decisions and questions paths are R0). The note that a phase gate is the owner's ruling whatever its class is correct.

6. Claims check against records.
   - The case pointer, the ready Critic PASS, the owner rulings and the 40 of 100 runs all hold.
   - The case's own cites resolve: PROJECT lines 48, 99, 103 and 105, and reviews/Q-008/critic.md exists.
   - DEFAULT none and TIMEOUT none are right for a phase gate.
   - The recommendation is labelled as the Chief of Staff's judgement.
   - Nothing is presented as the owner's view without a record.

ACCEPT M1 (questions/P-001-accept-m1.md)

7. Option A still begins "A. accept M1 as reached", which satisfies reached_licence in governance/checks/v3_checks.py (the option begins "<letter>. accept" and names M1 whole). The question file name is unchanged, so the check's record-name match still holds.

8. Resolved (was 11 and 12). The delivered text now gives both alternates and the 41 returns with no record of findings. Option B now states its cost: the milestone stays unreached and the project waits on the extended count.
   - 2 of 19 matches PROJECT section 6.
   - 27 of 75 without the five single-pass records matches the Q-008 memo's "12 of 24" built-work row and PROJECT section 6.
   - 41 matches memo bottom line 3.
   - The headline figures all match the memo.

9. DEFAULT none and TIMEOUT none are right: §3 says only the owner's ruling adds a reached mark. R0 is computed. The reversibility line (a reopen ruling removes the mark) is supported by the check.

10. Non-blocking: the question says the mark is added after the Design gate. That matches §3.
