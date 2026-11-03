## The Critic's independent view

I read the case against docs/gates/_GATE.md and opened every record it cites. That includes docs/PROJECT.md in full, the Critic's definition-of-ready and pre-mortem records, research/Q-008-memo.md and Q-008-source-check.md, research/Q-001-memo.md, the first 40 lines of research/Q-002-to-Q-007-corrections-confirmation.md, and the owner's rulings on the open unknowns, the count, the test budget, the value target, the spend ceiling, no-change, worst-work and time-and-limit. I also opened OPERATING_MODEL.md's standard-milestone table.

I have no shell, so I did not run `v3_checks gates`. My hand count of sections 1 to 8 is about 350 to 360 counted words (±10), so the case sits at the limit. Please confirm with the check.

The case is honest and mostly well sourced:
- The figures in section 3 match the sources.
- The three open unknowns, the 40-of-100 run split, V1 and V2, the spend ceiling and the intent all match the rulings.
- Section 3 says plainly that instructions are the primary cause of only 1 return and that 61 of 84 returns name no cause. It does not hide that the project's central premise is weak.

Gaps I would want fixed or set before the owner:
1. The "low pass rates" line carries no uncertainty.
   - PROJECT.md:99 says the figures are pooled across three repositories, come from mostly conversation-started work, and are uncertain where counts are small.
   - Research is 2 of 19, not 5 of 19, if the later-added source check counts. Built work is 27 of 75 without five single-pass PR files.
   - Q-008-memo.md says the same.
   - The point that pass rates are low survives either way, so this is a framing gap, not an error.
2. Section 5 does not give the form's "where it stands now" for any risk.
   - Replay (U2) and judge consistency (U3) are open and untested, and the case should say so against each risk.
   - The "unfaithful replay" line states the fallback, not what would happen.
   - The risk that the changes are aimed at the wrong cause (PROJECT.md R1) is not listed, although section 3 shows the count points away from instructions.
3. The visuals are incomplete. The form's standard visuals are missing for section 2 (today against the change), section 6 (owner-time caps) and the section 9 research and check outcomes.
4. The phase-line drawing in section 1 has five boxes, with "Operate and Review" joined in one. Its text alternative says "six phases". The numbers should agree.
5. The diagram in section 4 is faithful to PROJECT.md line 37, and the text alternative matches it. M1 is drawn "done", which rests on the Q-008 source-check PASS. No `reached` line exists yet, and the case rightly leaves it to the owner's ruling.
6. Nothing in the records contradicts "proceed". I have not seen the Critic's view of design gate 1, because it is outside my pack.

**The Critic's recommendation:** proceed — the definition-of-ready check passed at round 2 (reviews/P-001-ready/critic.md), the problem statement and pre-mortem passed (reviews/P-001-problem-premortem/critic.md), and the Q-008 count passed its source check, round 2. The owner has already ruled "go on" after the count and accepted U2, U3 and U4 as open. The findings below are non-blocking, but the case should be corrected before it goes to the owner: the section 3 uncertainty (point 1 above), the risk standings (point 2), the three citation items, and the M1 sprint note in the Milestones section.

**Citation check:**
- Section 4, line 4: "M1, the count, is done … [docs/PROJECT.md:35]". Line 35 is the italic instruction about adding `reached`. It does not say M1 is done. M1's own line is docs/PROJECT.md:48, and "done" rests on research/Q-008-source-check.md.
- Section 7, line 1: "Back to you if the 100 runs end before the test is ready [decisions/questions/P-001-test-budget.md]". The ruling record says only "up to about 100 runs … with checkpoints". The stop rule is in docs/PROJECT.md:103, which should be cited.
- Section 3, line 1: "plans 2 of 44, research 5 of 19, built work 32 of 80 … [research/Q-008-source-check.md]". The source check does not state these pooled figures. They are sums of the memo's per-source rows (1+1+0+0 of 17+23+3+1; 2+3 of 12+7; 15+17 of 51+29), and PROJECT.md:99 gives them. The sums are right. Cite the memo's bottom line 2 for them.
- Appendix, line 76: "M1 shows no sprint: the count was a research memo recorded in a records pull request with no review record of its own". This is contradicted by research/Q-008-source-check.md (PASS, round 2) and reviews/Q-008/critic.md, so the reason does not hold.
- Appendix, table row Discovery-3: "[research/Q-001-memo.md] [decisions/questions/P-001-worst-work.md]". The model shows this milestone by a source-checked map plus the owner's shortlist answers. Q-001-memo.md is the unchecked memo, and worst-work is one answer of five. Cite Q-001-source-check-2.md and the other four answer records (listed in PROJECT.md §7 "Groundwork").
- Appendix, table rows Discovery-1, -4 and -6: the model's table (OPERATING_MODEL.md lines 151, 154, 156) reads these as "not recorded". The table gives each a record without saying so, which can read as a claim of reached. Say "not recorded" and name what exists.
- Appendix, line 90: U2, U3 and U4 "accepted by you [decisions/questions/P-001-open-unknowns.md]". The record is second-hand, taken from a previous session's handoff. Its asked date is 2026-11-02 under a 2026-11-01 session id. This was already noted as acceptable by the readiness Critic, and I note it as carried.
- All other claims cite a record that supports them. I checked section 1 (reviews/P-001-ready/critic.md, P-001-after-the-count.md, P-001-open-unknowns.md); section 2; section 3 lines 2 to 4; section 4 lines 1 to 3; sections 5, 6 and 8; section 7 lines 2 and 3; and appendix rows Discovery-2, -4, -5, -6, -7 and -8.
- There is no user-profile proposal to check, because §9 reads "The owner is the user." Nothing in the case reports what a user representative said.

**Milestones:**
- All six project milestones read as achievements, not tasks:
  - M1: "How often work is sent back, and what the records show of why, is known"
  - M2: "A fair test of the changes is ready"
  - M3: "Every agent's brief and model on record"
  - M4: "Each tested change has a result"
  - M5: "The operating model runs on what worked"
  - M6: "Every slip in this work corrected"
- Each has a `· why:` that states the reason in plain words, with no ` · ` inside it. The Discovery and Design standard lines are all present and taken on, each with a why (PROJECT.md lines 40 to 57).
- No standard milestone is claimed reached. M1 is called "done" and its `reached` mark is left to the owner's ruling, which is correct.
- Finding on M1: it has no `· sprints:` part and is not "sprint pending". A merged, source-checked research item for it exists (Q-008 memo and Q-008-source-check.md, PASS). So its sprint could exist before this gate, and the case's reason for having none is wrong (see the citation check). Either record the sprint on M1 or give the true reason.
- M2 to M6 are Design or Build milestones, so their sprints cannot exist before this gate. None of them is a finding.
- Standard Discovery-1, -4 and -6 are "not recorded" in the model and must not be claimed reached. See the citation check.
