Verdict: FAIL

*The Critic on questions/P-002-design-gate.md, the question for the screening's Design gate (P-002): round 1 (FAIL), brief 253; round 2 (FAIL), brief 255. Each round a fresh session on a different model from the card's writer, started by the Chief of Staff (session_01QBwHGJtTY3gJUPrQDDJkf5), 2026-11-11, on fixed copies Model-Lab@5d26be1 (round 1) and Model-Lab@23c9962 (round 2, the same tree as 07668ce), with the two cards as put given as files. Recorded verbatim by the Orchestrator from the helper's return; the round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's. Round 2's own second-level headings are recorded one level lower, so they nest under their round. After round 2's copy was made, the card's REVERSIBILITY field was put in its one-word form, its exception moved into BLAST RADIUS, at commit c23a311; nothing else changed.*

## Round 1 (brief 253)

The round's verdict was FAIL.

I checked questions/P-002-design-gate.md against questions/_TEMPLATE.md, docs/gates/P-002/trial-terms.md and design-gate-1-case.md. I also checked the two decision records, the two filed cards, docs/projects/P-002.md and reviews/P-002-value-target-odds/reviewer.md.

Most counts and figures hold:
- The 31 ruled, 8 confirm-only and 20 proposed terms match the list.
- The eight confirm terms are T23 to T30.
- The two-look line figure matches P18 and the Reviewer's sweep (0.093 and 0.099, up to about 0.106).
- The FAIL, FAIL, PASS history matches the Reviewer's record.
- The spend text is consistent with P-001-spend-ceiling.

The problems are below.

1. **Blocking: Part 4's recommendation is on the owner's own time.**
   - Part 4's reasoning includes "reads per look let you see the work at each judgement", and option A picks 5 reads per look, which is 10 for a trial with a second look.
   - Part 2 correctly gives no recommendation on time, and the card's own "What would change it" line shows the reads are a time choice.
   - The reads choice (per look or per trial) should be split out with no recommendation.

2. **Blocking: the plain-English opening fails a cold reader.**
   - The card never says what a "piece", "touch", "screening", "prompt engine", "entry card", "starting share", "ceilings" or "open unknowns" is. The definitions exist only in the terms list.
   - The WHY line reads "odds behind your target were reproduced" and "proposals left by your two trial cards".
   - Part 3 lists U1 to U5 as fragments ("U2 the starting share").
   - Part 4's "about 1 in 10 as now, up to about 0.106" needs a sentence on what "as now" is and what the 0.106 is.
   - A smart non-expert could not rule on Parts 3 and 4 from the card alone.

3. **Blocking: Part 4 asks the owner to rule twenty proposals and confirm eight terms that the card does not show.**
   - Only P12, P13, P19 and the two choice items are described. The owner is told to rule "as written" with the writing in another file.
   - The card does not say that 17 come from the owner's earlier cards and 3 (P18, P19, P20) are the Chief of Staff's own designs. The terms list says so.
   - It does not name the P6 difference between the two cards.
   - The eight confirmations are named but not explained.
   - Confirm-only terms are ruled-in-text, not ruled-in-words. They should be summarised with that distinction, not folded into a bulk "A. all as listed".

4. **Blocking: Parts 4 and 5 overlap and can contradict each other, and Part 5 option A misstates P12.**
   - Part 4 option A rules P12, P13 and P19 as written. Part 5 is P13's own ruling and offers B (all of Build waits) and C (hold the screening). An owner who chooses Part 4 A and Part 5 C has ruled both ways.
   - The card should say that Part 5 settles P13 and overrides how P12 and P19 apply.
   - Part 5 A says "each trial waits until its kind of work is clear of the prompt engine". P12 and the brief say only a method that could change first-check pass rates waits.
   - Part 5 A says "Design and the count go ahead now". Under T20 and brief line 244 the log is built only after the gate, and the count runs from the start of Build. This blurs what "now" means.
   - Part 5 B ("all of Build waits") would also delay the count, which contradicts the card's own claim that counting changes nothing the prompt engine does.

5. **Blocking: the owner's time caps in Part 2 do not add up, and their consequences are missing.**
   - 10 reads a month covers only two one-look trials. A trial with a second look takes 10 reads alone, so "about two trials" is wrong for those trials. The brief says 3 to 5 in 10 trials run a second look.
   - The card does not say what happens at a cap.
   - P16 (proposed, unflagged here) says results cards are never held back. A hard cap of 4 cards a month cannot coexist with that, and the card does not say which wins.
   - Option C's "each status update counting them" is P17, which is only proposed, and it is presented as part of the option.
   - Option B's trial equivalent is not given.

6. **Blocking: the two-look choice is not put fairly.**
   - The stricter line is recommended as the one that "keeps the 1 in 10 you chose". Its cost is never stated: a lower line means a useful halving passes less often than the 0.92 and 0.70 quoted. The Reviewer's figures show the line near 0.022 passes a real halving 0.77 and 0.43 of the time.
   - The "as now" alternative is described only as exceeding 1 in 10 by up to 0.006.
   - The sweep shows the current line is under 1 in 10 at most starts. The card gives neither side's gain and cost, as the template's option form needs.

7. **Blocking: Part 1 approves "the brief as it stands" without saying that the case carries five unfixed round-4 findings.**
   - They are listed in the case's appendix: "two cards per trial" wrongly under proposed, the "fixed trial plan" and "Critic's view" attribution, the intake claim, R7's "proposed" wording, and the Source checker row.
   - The owner is asked to approve the brief as it stands without being told of them, so the line "the brief meets every readiness item" is unqualified.
   - The card also omits two things from the case's section 8: "You are the user: no user representative step", and the condition behind the tier question (three or more agents at once, trial-terms line 84).

8. **Non-blocking, but one hand-off item: Part 3 accepts U2's fallback, which is a proposal.**
   - U2's fallback is the stop rule (P5, a starting count under 6 of 60). P5 is only proposed and is ruled in Part 4.
   - The recommendation says "each open unknown has a test and a fallback" without saying one rests on an unruled proposal. If the owner rules Part 3 A and drops P5 in Part 4 B, U2 has no fallback.
   - I did not see the full text of U3 and U5 in the grep output, so I did not check those two.

9. **Non-blocking: Part 6 is one-sided.**
   - The Reviewer's own assumptions section says the target figure leaves out the hold-up half, that the independence assumptions are not tested, and that the 0.80 hold-up figure is a guess.
   - Part 6 says "ran every figure your target and the trial rest on", which overstates what a rerun covers. Option A shows no gain or cost, and B shows none either.
   - "Medium-high confidence" is a term the other parts do not use.
   - "once three were restated" is roughly right: the 0.20 to 0.22 correction, the 4-to-5 to 5-in-10 rounding, and the range.
   - "Nothing you ruled changed" is not checked by any record I read.

10. **Non-blocking: smaller accuracy points.**
    - WHY says the Critic's view "is in the gate document". It is a separate file, reviews/P-002/_design-gate-1-critic.md, and the case holds none of it.
    - "WHO HAS CHECKED IT" states in the past tense that the Critic checked this card. That is true only once this record is filed.
    - "Each proposal guards a risk in the pre-mortem" cites no record, and I could not confirm it for P17, P4 or P20.
    - "Nothing here is irreversible" sits beside option D (kill), and the card gives no reopen path.
    - RISK CLASS is R2, but both source cards were R3 ("part of a value target") and the card rules their leftover proposals. The class is a computed field and should be checked.
    - The template has options with "cost, what it rules out". Parts 1 (B, C, D), 4 (B, C), 5 and 6 give none for most options.
    - The "Order" context line cites "Part 2" of the brief, which is a bullet that itself cites the portfolio IDEAS.md. That is traceable but should name IDEAS.md.

11. **Checked and fine.**
    - Ruled and proposed are kept apart in Part 4 with T-numbers and P-numbers, apart from the overlaps in findings 4 and 8.
    - T22 (ceilings set at this gate) is honoured by Part 2.
    - The Part 1 option A description matches the case's section 4 and section 8.
    - DEFAULT and TIMEOUT "none" fit a phase gate.
    - The Context list's sources exist, and the Part 3 test-and-fallback claim holds for U1, U2 and U4.

**Contract**
- **Changed:** nothing. I have no write tool.
- **Why:** a cold read of the card as the owner would meet it, plus a check of every claim against its records.
- **Verified:** I read the card, the template, trial-terms, the case, both decision records, both filed cards, the Reviewer's record in full, and the relevant lines of docs/projects/P-002.md. I did this by reading and grepping, with no shell.
- **Undone:** I did not read the full text of the brief's U3 and U5 (long lines were omitted from the grep output). I did not check P-001-spend-ceiling or reviews/P-002-brief beyond the quoted lines. I did not check the pre-mortem claim for each of the 20 proposals. I did not read docs/briefs, reports, handoff or sessions, as ordered.
- **Needed outside my surface:** the Chief of Staff must fix findings 1 to 7. Findings 8 to 10 should be fixed in the same pass.
- **Open questions:** does the owner want the twenty proposals shown on the card itself or only by reference? Is R2 or R3 the right class? Should the reads choice become its own part?

## Round 2 (brief 255)

The round's verdict was FAIL.

*The Critic on questions/P-002-design-gate.md, the question for the screening's Design gate (P-002): round 2, read cold as a smart non-expert, on the fixed copy /home/user/ml-fixed-254 with the two cards as put read from /home/user/ml-cards/. The Parts 1-10 below are those of the redraft.*

I checked the redraft against questions/_TEMPLATE.md, docs/gates/P-002/trial-terms.md, the case (docs/gates/P-002/design-gate-2-case.md), both decision records, both filed cards, docs/projects/P-002.md (sections 5-8, U1-U5) and the Reviewer and brief-Critic records. The redraft is much better than round 1. Four blocking problems remain, plus one smaller blocker on the wording of P15 and P16.

### Round 1 findings, one by one

1. Part 4 recommended on the owner's time: **answered for the reads.** Part 6 is now its own part with no recommendation. The same fault has moved into Part 5 (new finding 1 below).
2. Plain-English opening: **mostly answered.** The Words block defines piece, touch, trial, second look, look, entry card, results card and prompt engine. The WHY is now plain. Part 9 gives each unknown in full. Part 7 now says what the two starting shares are. Some jargon is left (finding 9).
3. Proposals and confirmations not shown: **partly answered.**
   - All fourteen proposals and all twelve confirmations are now written out, and the ruled-in-text versus ruled-in-words distinction is stated.
   - The P6 difference between the cards is named, and so is the P14 difference.
   - Still open: the origin of P18, P19 and P20 (finding 2), and clauses dropped from P15 and P16 (finding 5).
4. Parts 4 and 5 overlap and P12 is misstated: **mostly answered.**
   - P12, P13, P19 and P20 now live only in Part 8.
   - The "only a method that could change first-check pass rates waits" wording now matches P12.
   - "Count from the start of Build" matches T20 and the brief.
   - Part 8 C, "hold the screening", still contradicts Part 1 A (finding 3).
5. Time caps do not add up: **mostly answered.**
   - The card now says what happens at a cap: the entry card waits, the look waits.
   - It names the P16 conflict, and says a results card counts against the next month.
   - P17 is out of the option.
   - The arithmetic holds: 2 entry cards and 10 reads is two trials at 5 reads each, and 4 cards and 20 reads is four. A second look takes 10 reads alone, and the card covers that by letting the look wait.
   - It never states the "two trials a month" reading (finding 8).
6. Two-look choice not fairly put: **partly answered.**
   - The cost of the stricter line is now stated ("how much less has not been computed"), and the figures are right.
   - Gain and cost are still uneven (finding 4).
7. Part 1 hid the unfixed faults: **answered.** The six faults are listed and match the case's appendix. The tier condition and "you are the plan's user" are included.
8. U2's fallback rests on P5: **answered.** Part 9 says so.
9. Part 6 (now Part 10) one-sided: **answered.** The assumptions are named, "medium-high" is gone, and the unverified "nothing you ruled changed" line is gone.
10. Smaller points: **answered.** Each of these is fixed:
    - the WHO HAS CHECKED tense;
    - the pre-mortem claim;
    - the reopen path after a kill;
    - RISK CLASS, now R3;
    - the IDEAS.md citation;
    - the wording about the Critic's view.

### New and remaining findings

1. **Blocking: Part 5 recommends on the owner's own time.**
   - P15 (at most 3 entry cards wait on you) and P16 (results cards reach you within two weeks) are choices about the owner's time and load.
   - P4 (a summary after five trials, on which you rule) and P17 (reports counting your touches and cards) bear on it too.
   - Part 5 recommends A, "all fourteen as written", with low confidence, which recommends on them.
   - Part 3 already treats P16 as bearing on the time caps.
   - Fix: move the time proposals (at least P15 and P16) into a part with no recommendation, or give Part 5 no recommendation. Say plainly that the owner may rule those two differently.

2. **Blocking: the origin of P18, P19 and P20 is not shown.**
   - Part 8 puts P12 and P13 (on your cards) together with P19 and P20 in single options. Option A is one block that mixes card proposals with the Chief of Staff's own.
   - Part 7 does not say that P18 is the Chief of Staff's own either.
   - Part 5 says "the cards put these as proposals". Parts 7 and 8 never say P18, P19 and P20 were on neither card. trial-terms says they are the Chief of Staff's own.
   - Round 1 asked for this, and the owner cannot tell from the card which of the twenty were theirs.
   - Fix: say in Parts 7 and 8 which proposals come from the cards and which were designed by the Chief of Staff. Then the owner can rule each knowing its source.

3. **Blocking: Part 8 C contradicts Part 1 A, and the card does not say how they combine.**
   - Part 1 A has Design start now. Part 8 C holds the screening until the prompt engine finishes, "nothing moves".
   - An owner who rules Part 1 A and Part 8 C has ruled both ways.
   - Fix: say that Part 8 C means Part 1 B (hold), or that Part 8 is settled first. Do the same for B's "no trial until" against Part 1.

4. **Blocking: gain and cost are missing or uneven where the choice is the owner's time or a figure.**
   - Part 3 A, B and C have no gain or cost. They state the consequences at a cap but not who gains or loses.
   - Part 6 A, B and C have none either. Part 6 C ("none") drops P14's rule that a read the owner would not have accepted counts as reopened, which is half of the sample guard the VT card put in its "holds up" definition. The card does not say that cost.
   - Part 6 B ("5 per trial, at its first look") adds a timing that neither card has, and leaves a second look with no unlabelled sample.
   - Part 7 A shows a cost but no gain. At low starting shares the line is well under 1 in 10 (the Reviewer: 0.0677 at a 10% start), so A has more power there, and the card does not say so. Part 7 C shows no cost: the later ruling, and the stricter line staying uncomputed.
   - Part 5 A and B, Part 2 A and B, and Part 1 C and D also show no gain or cost.
   - Fix: give each option a gain and a cost in the template's form, so the options are even.

5. **Blocking, narrow: P15 and P16 are not "as written".**
   - P15 omits "the next waits in a queue the desk shows". Part 3 then treats the queue as a given although it is only proposed.
   - P16 omits "never outnumber the entry cards approved". This bears directly on the Part 3 caps.
   - Part 5 A rules "as written" on a paraphrase. State the full wording.

6. **Non-blocking: the Context line "round 4 passed with five non-blocking findings" is wrong.**
   - reviews/P-002-brief/critic.md round 4 has eight non-blocking findings, five of them on the ruled and proposed labels.
   - Part 1 lists six faults, and the case says six. The sixth, the Source checker, is round 4's Item 2, finding 3.

7. **Non-blocking: Part 7 timing and wording.**
   - "As set now" is unclear, because the line is not set anywhere. Per the VT card Part 3 A it is "fixed once the starting share is counted", which the card does not say. That bears on B's "at most 1 in 10 at every starting share".
   - Option C says "you rule it with the next gate". The brief freezes the trial design (M9) in Design, and P20 bars any trial before it is frozen. The card does not say which gate that is, or how it squares with a frozen plan.

8. **Non-blocking: Part 3 leaves the arithmetic unstated.**
   - It never says that 10 reads is two one-look trials (or one trial with a second look).
   - "Short reads" is first used in Part 3 and only explained in Part 6.
   - Part 4's "the second look: 30 more pieces only if the first look leaned the right way" omits TG's "but did not pass".
   - T28 is marked "(added by the Chief of Staff)", yet the Critic's view on the results card is in the trial-gates record. It is minor.

9. **Non-blocking: jargon left for a cold reader.**
   - The Part 1 A line "approves the plan as it stands: the target, the milestones, the standard steps, the trust level and the intent" leaves "standard steps", "trust level" and "intent" unexplained.
   - Part 1 and the case mention the "Source checker" without saying who it is.
   - "Ceilings" and "M7" appear before they are explained.
   - The Part 1 recommendation "the six faults change no term (Parts 4 and 5 rule those)" is muddled.
   - The WHY says Discovery "is done", while the case says it closes at this ruling with M7 awaiting acceptance.

10. **Non-blocking: Part 5's confidence claim cites no record.**
    - "No check since has questioned one" has no source.
    - P6 and P14 are known to differ across the two cards.
    - P16 conflicts with the Part 3 caps, as the card itself says.

### Checked and holding
- The twelve confirmations are T16, T23-T30 and T32-T34, and all match trial-terms.
- The fourteen proposals are P1-P11 and P15-P17. With P12, P13, P19 and P20 in Part 8, P14 in Part 6 and P18 in Part 7, all twenty are covered once.
- The ruled and proposed split matches the decision records and both cards.
- The figures match the records:
  - 0.093 and 0.099, and up to about 0.106 (max 0.1062 at starts of 36% and 64%; 0.1043 at 4 and 6 in 10).
  - 0.92 and 0.70 at the two starting shares.
  - 0.22 for the held-up checks, and 5 in 10 for a true halving on the count (0.53 and 0.54).
  - FAIL, FAIL, PASS, and "agreed a second way".
- The unknowns U1-U5 match brief section 7 as to tests and fallbacks.
- The spend text matches P-001-spend-ceiling.
- The R3 class, "DEFAULT none", the reopen path after a kill, and the WHO HAS CHECKED tense are right.
- No lean towards the recommendation in the options of Parts 2, 4 and 9. No recommendation on time in Parts 3 and 6.
- The pass-through of the case's section 8 is complete: milestones and ceilings (Parts 1-3), unknowns (Part 9), proposals and confirmations (Parts 4-8), M7 (Part 10), and no user representative (Part 1). No part the gate needs is missing.

**Contract**
- **Changed:** nothing. I have no write tool.
- **Why:** a cold read of the redraft as the owner would meet it, plus a check of each claim and figure against its record.
- **Verified:** I read the card, the template, trial-terms, the case, both decision records, both filed cards and round 1 of this record. I also read the brief's U1-U5 text, the brief Critic's round 4, and the Reviewer's record by grep, and compared the counts and figures above.
- **Undone:** I did not check the PR 93 and merge-commit 9513e98 claim, because I have no git. I did not check P-001-spend-ceiling beyond the card's wording. I did not read the Reviewer's "three restated" text in full. I did not read docs/briefs, reports, handoff or sessions, as ordered. I did not count the absent gate Critic record against the card.
- **Needed outside my surface:** the Chief of Staff must fix findings 1-5 and should fix 6-10 in the same pass. A round 3 check is then needed.
- **Open questions:** should P15 and P16 and the other time proposals sit in the time part (Part 3) with the caps and the reads? Should Part 8 be ruled before Part 1, so that 8 C maps to 1 B?
