## The Critic's independent view

I read docs/gates/P-001/design-gate-3-case.md against docs/gates/_GATE.md. I opened the cited records: docs/PROJECT.md in full, reviews/P-001-ready/critic.md, reviews/P-001-problem-premortem/critic.md (head), reviews/Q-008/critic.md, research/Q-008-memo.md, research/Q-008-source-check.md, the Q-001-source-check-2 and corrections-confirmation heads, and the owner's rulings. The rulings were after-the-count, open-unknowns, test-budget, value-target, spend-ceiling, no-change-result, session-records, time-and-limit and worst-work.

Two process notes:
- I have no shell and did not run `v3_checks gates`. My hand count of sections 1 to 8 is about 345 counted words, under 350. It is close, so please confirm with the check.
- I opened reviews/P-001/_design-gate-2-critic.md by mistake. It is outside my pack. I did not use it. Every finding below was checked against the records themselves.

The case is honest and mostly sound:
- Section 3 shows the weak premise plainly: the instructions are the primary cause of 1 return, and 61 of 84 returns name no cause beyond the fault.
- The pooled first-time pass figures (plans 2 of 44, research 5 of 19, built work 32 of 80) equal the sums of the memo's per-source rows, in the table at research/Q-008-memo.md:71-82. They are stated as small, pooled counts with alternates.
- The 40-of-100 run split, V1, V2, the spend ceiling, tier T1 and the open unknowns U2, U3 and U4 all match the owner's rulings and PROJECT.md.
- The risks in section 5 match the pre-mortem rows R1, R2, R3 and R9, and U2/U3 are marked untested.

Faults that are not citation errors:
1. The visuals are incomplete. The form's standard visuals are missing for section 2 (today against the change), section 3 (fit against limits), section 6 (owner-time caps) and the appendix (research and check outcomes). Only the section 1 and section 4 drawings are present.
2. The section 4 drawing shows "M1 count: done", and its text alternative says "M1, the count, is done". The same section says only the owner's ruling marks M1 reached. The drawing states a status the records do not hold.
3. Section 5 gives the risk and its fallback but not "where it stands now" for the wrong-cause risk. For that risk it says only that candidates cover other causes, with no standing against the count's own result.

None of these blocks the owner from ruling.

**The Critic's recommendation:** proceed — the definition-of-ready check passed at round 2 (reviews/P-001-ready/critic.md). The Q-008 count passed its source check at round 2 (research/Q-008-source-check.md). The owner has already ruled "go on" after the count and accepted U2, U3 and U4 as open. The faults above are non-blocking and are for the proposer to fix before the case goes to the owner. They are the missing visuals, the "done" drawing of M1, the section 4 citation, and the M1 sprint reason.

**Citation check:**
- Section 4, line 4: "only your ruling marks it reached [docs/PROJECT.md:48]". Line 48 is M1's own milestone line and says nothing about reached. The ruling rule is in the italic instruction at PROJECT.md:35. "Source-checked" is supported by research/Q-008-source-check.md.
- Appendix, line 76: "a sprint needs a reviewer's record under its pull request's number, and the count's pull request has none [research/Q-008-source-check.md] [reviews/Q-008/critic.md]".
  - reviews/Q-008/critic.md checks the question research/Q-008.md. It does not check the count or any pull request, so it does not support "the count's pull request has none".
  - No cited record shows anything about a count pull request. The Q-008 source check says nothing of the kind.
  - The reason is also narrower than the rule. A sprint can be a reviewed and merged pull request, or a merged research item. The Q-008 memo has a PASS source check (round 2).
- Section 4, flowchart and its text alternative: M1 drawn and described as "done". See fault 2 above.
- Section 2, line 2: "fewer review rounds, better research" cites PROJECT.md. PROJECT.md:166 labels this the Chief of Staff's reading of the owner's words. Section 22 of PROJECT.md calls them "the owner's two aims". The case does not say it is a reading.
- Section 1, ask line: the cited records support "the brief passed its readiness check and you already ruled to go on with three unknowns open". The first record is reviews/P-001-ready/critic.md, round 2 PASS. The others are P-001-after-the-count.md and P-001-open-unknowns.md.
- Section 6, line 2: "100 test runs through Design; about 300 ... ruled at the Build gate". The test-budget ruling holds the 100. The 300 and the Build-gate ruling are in PROJECT.md:105, which is cited.
- Section 7, line 1: "Back to you if the 100 runs end before the test is ready". PROJECT.md:103 is cited and holds it.
- Appendix, line 90: the open-unknowns record is second-hand. It is taken from the previous session's handoff, and its asked date is 2026-11-02 under a 2026-11-01 session id. The case says the record copies the answer, so this is disclosed and carried, not a fault.
- Sections 1 to 8 are otherwise supported by the records I opened.
- Section 3: the 2 of 44, 5 of 19 and 32 of 80 sums, 61 of 84, and instructions as the main cause of one all hold against the Q-008 memo.
- Appendix rows Discovery-2, -3, -5, -7 and -8: each cited record supports its row.
- Appendix rows Discovery-1, -4 and -6: each says "Not recorded by the model" and names the record that exists. None claims reached.
- No user-profile proposal exists, since section 9 of PROJECT.md says "The owner is the user." Nothing in the case reports what a user representative said.

**Milestones:**
- The case gives a table, not the printed block. The empty `milestones` block is explained, as you said.
- The six project milestones in PROJECT.md read as achievements, not tasks, and each has a `· why:` stating the reason in plain words.
  - M1: "How often work is sent back, and what the records show of why, is known (M1)"
  - M2: "A fair test of the changes is ready (M2)"
  - M3: "Every agent's brief and model on record (M3)"
  - M4: "Each tested change has a result (M4)"
  - M5: "The operating model runs on what worked (M5)"
  - M6: "Every slip in this work corrected (M6)"
- No `· why:` has a ` · ` inside it, and each of the 14 Discovery and Design standard lines is present as "taken on" with a why.
- M1 is a finding. It has no sprint and is not "sprint pending". Its work is a research item that passed its source check (round 2). The case's reason for having no sprint concerns pull requests only, and its citation to reviews/Q-008/critic.md does not hold. If the Q-008 item is merged, M1 should show it as its sprint. If it is not merged, the case should say so and cite the record that shows it.
- M2 to M6 are Design or Build milestones, so their sprints cannot exist before this gate. None of them is a finding.
- The table claims no standard milestone as reached. Discovery-1, -4 and -6 are shown as not recorded, which is allowed and is not a finding.
- M1 is drawn "done" in section 4 though not reached. Fix the drawing, as in fault 2.

Files read (all under /home/user/Model-Lab unless stated):
- docs/gates/P-001/design-gate-3-case.md
- docs/gates/_GATE.md
- docs/PROJECT.md
- research/Q-008-memo.md
- research/Q-008-source-check.md
- reviews/P-001-ready/critic.md
- reviews/Q-008/critic.md
- reviews/P-001-problem-premortem/critic.md
- decisions/questions/P-001-after-the-count.md, P-001-open-unknowns.md, P-001-test-budget.md, P-001-value-target.md, P-001-spend-ceiling.md, P-001-no-change-result.md, P-001-session-records.md, P-001-time-and-limit.md and P-001-worst-work.md
- /home/user/Personal-Org-Operating-Model/OPERATING_MODEL.md (sprint passages only)
