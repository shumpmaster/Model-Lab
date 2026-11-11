## The Critic's independent view

I read the case (docs/gates/P-002/design-gate-1-case.md) against docs/gates/_GATE.md. I read docs/projects/P-002.md, the screening's own brief, in full. I read the two card files, the decision records for the value target, trial gates, groundwork shortlist, aim and brief stop, the Reviewer's odds record, and the brief Critic's four rounds. I confirmed the other decision files the case cites exist. I did not open research/Q-017-memo.md, reviews/P-002-problem-premortem/critic.md beyond its verdict lines, or the intake files. I ran nothing.

**The Critic's recommendation:** proceed — every claim that asks the owner to rule traces to a record that holds it: the brief passed round 4 after three failed rounds, the Reviewer's run of the odds passed at round 3, and the trial-terms list has no blocking finding. The case itself needs the fixes below before the owner reads it, chiefly the unnamed unknowns, the missing ceiling options and two visuals. None of them changes what the records support.

**Citation check:**

Every other line cites a record that says it. The gaps, by section and line of the case:

1. Section 1, lines 11 to 15 (the phase visual). It draws "Discovery: done", and the text alternative says "Discovery is done". The case's own appendix (line 105) says M7, a Discovery milestone, is "not reached until you accept it". It also records Discovery-1 and Discovery-6 as "not recorded by the model". No cited record says Discovery is done, and the owner's ruling at this gate is what closes it. This is an unreached value drawn as reached. It should show Discovery as pending the owner's acceptance of M7.
2. Section 2, lines 26 to 28 (today side of the visual). "Methods found by chance → adopted untested, or not at all" is in no cited record. docs/projects/P-002.md section 2 says only that ways of running the team are untested and often maker-reported, and quotes the owner on waiting for full proof. The picture of today's practice is the Chief of Staff's, uncited.
3. Section 4, lines 47 to 59 (the dependency visual), checked against the Dependencies paragraph in section 3 of the project document.
   - The drawn edge M7 → M8 is in no record; M7 is only said to be confirmed before the gate. The text alternative leaves that edge out, so the drawing and its text alternative differ.
   - The drawn edge M10 → M12 is not in the Dependencies paragraph either. It says only that M10 "can be designed beside" M8 and that M12 "can start with M11".
   - The rest matches: M8 to M9 and M11; M9, M11 and M12 to M13; M13 to M14; M14 to M15.
4. Section 3, line 38. "Re-tested outside claims held less often; copied code carried harm" is stated flat. The project document grades the evidence weak: one secondary citation whose study was not opened, one preprint abstract, and one project page (section 2). The case drops the grades.
5. Section 3, line 39. "A true halving shows on the count about 5 times in 10" is right (0.53 and 0.54, reviewer.md round 3). The project document adds that it shows less often once the work must also hold up, and the Reviewer says that figure is not computed. The case omits this.
6. Section 1, line 9, and section 8, line 83 (M7). The case does not tell the owner that the two cards the owner answered still carry figures the Reviewer found stated too low.
   - The value-target card says a real halving shows "about 4 to 5 times in 10", where the Reviewer's figure is about 5 in 10 (reviewer.md round 1, finding 4).
   - Both cards say the hold-up check turns away a harmless method "up to 1 in 5" with two looks, where the Reviewer's figure is 0.22, about 1 in 4.5 (round 1, finding 2).
   - The case says the odds "were reproduced independently", which is true of the scripts and section 6. The owner ruled on the card figures, so the case should say they were corrected only in the brief and the odds record. The Reviewer never read the cards (rounds 1 and 3, "Undone").
7. Section 6, line 71. "Usage so far: not recorded [docs/projects/P-002.md]". The project document says only that the owner's hours are not recorded (section 6, "Cost to the owner's time"). It holds nothing on spend or usage either way.
8. Section 1, line 5. "Your focused last check passed it" credits the owner with a check the Critic ran. The owner ruled that it be run (P-002-brief-stop.md). This is a wording slip only.
9. Section 9, line 93. "The timeline prints no milestone lines for this project, whose Discovery ran from a conversation". No cited record says what the timeline prints. I cannot run `v3_checks gates`, and I was told the form check passed. The empty ```milestones block cannot be checked by me.

Form and plainness, non-blocking:

- Section 8 asks the owner to accept "U1 to U5" without saying what they are. Only U1 and U3 appear in section 5. U2 (the starting share), U4 (checking outside code safely) and U5 (a method must be switchable piece by piece) are named nowhere in the case. A non-expert cannot accept what is not shown.
- Section 8 asks the owner to set both ceilings now. The case gives no options, though the brief (section 5) says "the gate card will put the ceilings as options, each with the number of entry cards, results cards and short reads a month it allows". Either the case or the ruling card must carry them.
- Section 6 has no owner-time-caps visual. The caps are unset, so they would be drawn hatched and labelled "not set yet".
- Section 5 lists three risks of the pre-mortem's eighteen, with no "what would happen" for any of them. The form asks for each risk.
- Section 8: "twenty proposals ruled … and whether trials may start before the prompt engine finishes" counts P13 twice. P13 is itself one of the twenty.
- Word count: I estimate about 320 counted words in sections 1 to 8, under the 350 limit.

**Milestones:**

- The appendix table lists Discovery-1 to 8 and M7, and claims none reached. Discovery-1 and Discovery-6 are "not recorded by the model", which is not a finding. M7 is shown as not reached until the owner accepts it, which agrees with reviewer.md (FAIL, FAIL, PASS) and with the project line.
- Discovery-7 ("Scope, limits and owners agreed") is only partly met, because the ceilings are not set. The case says the ceilings are the owner's at this gate. That is the case saying why the owner is asked to proceed, so I make no finding.
- M7 has no ` · sprints:` part in docs/projects/P-002.md line 117, though its work (the Reviewer's run and record) is done. If that record landed by a merged pull request, a sprint could exist before this gate and M7 is a finding. I cannot see pull-request history. The Orchestrator should say whether it merged.
- M8 to M15 have no sprints and none could exist before this gate, so there is no finding. The table does not list them; they appear only in sections 4 and 8.
- Each of M7 to M15, as written in the project document (lines 117, 126 to 128, 131 to 134 and 137), reads as an achievement within its phase and carries a plain ` · why:`. The Discovery-1 to 8 and Design-1 to 6 standard lines are all present, taken on, with a why. I find no action-or-task wording.
- The table's rows give records, not states. Nothing in it claims a "not recorded" milestone reached.

**D-050 flag:** my findings 1 to 3 on the trial-terms list below (T4, T16 and T20 marked ruled on card words) implicate the brief's round 4 label check. It called the sizes "accurately labelled" and said the labels hold.

## The trial-terms list (docs/gates/P-002/trial-terms.md)

**Counts.**
- Ruled terms: T1 to T31 is 31.
- Ruled, confirm: T23 to T30 is 8, and the case's "eight terms confirmed" matches.
- Proposed: P1 to P20 is 20, with 17 from the cards (P1 to P17) and 3 the Chief of Staff's own (P18 to P20).
- The closing paragraph's mapping to the brief's last bullet is right. The bullet holds P1, P4 to P12, P14 to P16, T31, P18 and P19. P13 sits in the brief's R15 and section 8, P2, P3 and P17 are not in the brief, and P20 is in its section 3.
- The two "places the cards differ" are real, and I found no third.

**Marks.** I checked each term against its record. T1 to T3, T5 to T15, T17 to T19, T21, T22 and T31 are as their records support. P1 to P17 are each on a card under its "Proposed" heading, which the value-target record says were "not yet ruled one by one". P18 to P20 are on neither card.

**Findings:**

1. **Non-blocking. T4 is marked Ruled where its own definition of "holding up" is marked "confirm" at T25.**
   - T4's parenthesis (the two checks, passing the first independent check and not reopened within 30 days) rests on the part 1 introduction and the card's "Words used below".
   - Option A's own line says only "with the work holding up". The value-target record's ruling line does not name the two checks or the 30 days.
   - T25 marks the same words "Ruled, confirm". The owner should see them in one place, as ruled-confirm, or T4 should say which half is the owner's words.
2. **Non-blocking. T16 repeats a card claim, "so that a useless method passes no more often", as part of a ruled term.**
   - The Reviewer found the two-look line gives 0.104 at starts of 4 in 10 and 6 in 10, up to about 0.106. So it is "about 1 in 10", not "no more often".
   - P18 proposes the fix, but T16 does not point to it.
   - T16 also draws the detail of the second look from card text under "How often a trial passes", not from the ruling line. The details are card words, so they should be marked "confirm". The ruling line has only "two looks planned".
3. **Non-blocking. T20 is marked Ruled, but half of it is card text outside any option.**
   - The record holds "specced in Design, built only after the Design gate; no trial before".
   - "Counts a starting figure over 60 pieces" and "changes nothing in the prompt engine's work" are from the card's "What must be built" only. They are card words under no option, so they are "Ruled, confirm" by the list's own definition.
4. **Non-blocking. The marking of "Added by the Chief of Staff" lines is uneven.**
   - T27 and T28 are "Ruled, confirm".
   - P6 is "Proposed", although the same TG card marks the identical clause "Added" and puts it under "Under every option". The list's difference 1 gives the reason, that the VT card lists P6 as a proposal.
   - The list's own rule, that "under every option" lines are "confirm", is not stated as having this exception. A cold reader will see two rules.
5. **Non-blocking. Terms on the cards that are missing.**
   - The starting figure counts "all kinds together" (VT part 1 introduction). T4 omits this, though trials are per kind and the owner should see the mixing.
   - Part 1 is "reversible until the first trial starts; after that a change discards the starting count and is a new target". It is not in the list.
   - The VT card has the Chief of Staff logging conversation questions by hand ("Not blind"). T29 holds only the draw record and the Reviewer's analysis.
   - I found no other omission across the two cards' "Words", "Limits", options, "Under every option" and "Proposed" lists.
6. **Non-blocking. T25's "Where" omits that the same VT "Words" paragraph holds the five-piece unlabelled sample** (P14, a proposal), though P14's own row cites it.
7. **The five brief round 4 carry-overs in the case's appendix are carried fairly, with one omission.** I checked the unchanged brief text for each.

   | Carried finding | Case line | Brief text still present | Fairness |
   |---|---|---|---|
   | Finding 1, "two cards per trial" | 110 | line 187 | Fair |
   | Finding 2, "fixed trial plan" and "Critic's view" | 111 | line 183 | Fair. It does not add that the TG record holds the Critic's view, though T28 does. |
   | Finding 4, intake files | 112 | line 187 | Fair |
   | Finding 5, R7 "proposed" | 113 | line 202 | Fair |
   | Source checker row | 114 | line 151 | Fair; it is a residual inside round 4's item 2, not a numbered finding |

   - The omission is finding 3, the ambiguity of "proposals; your ruling makes them so". The list's mark definitions carry it in substance and the gate settles it, but the appendix does not name it as carried.
   - The case's "five findings" therefore leaves out one of round 4's non-blocking findings. Round 4 says eight in all, of which findings 6 to 8 only record that nothing is wrong.

**Six-part contract.**
- **Changed:** nothing. I wrote no file.
- **Why:** to check the Design gate case, and the trial-terms list against both decision records, the shortlist record and both card files.
- **Verified:** I read the case against the gate form and the project document in full. I read both card files and the two decision records in full. I read the shortlist record, the aim record, the brief-stop record, the brief Critic's four rounds, and the Reviewer's odds record, rounds 1 to 3. I checked the counts of the list, the closing mapping, and the five carried findings against the brief text. I confirmed the cited decision files exist.
- **Undone:**
  - I could not run `v3_checks gates` or the form check, and could not see git or pull-request history.
  - I did not open Q-017, the pre-mortem Critic record past its verdict lines, the intake files, or docs/LESSONS.md.
  - I took the case's word count by estimate, not by tool.
- **Needed outside my surface:** the case needs the fixes above:
  - name U1 to U5, or cite where each is shown;
  - give the ceiling options, or say the ruling card carries them;
  - correct visual 1, visual 2 and the dependency edges;
  - tell the owner the card figures were corrected only in the brief and the odds record;
  - carry round 4's finding 3.

  The list needs the cross-reference and mark fixes in findings 1 to 6. The Orchestrator should say whether M7's records landed by a merged pull request.
- **Open questions:** should the owner confirm T4's definition of "holding up" and T16's second-look detail with the eight confirmations, which would make ten? Should the ceilings come as options on the case or on the ruling card?
