Verdict: FAIL

The Critic's check of the rest of the brief (docs/PROJECT.md sections 1, 2 chain, 4, 5, 7 groundwork and unknowns, 8, 9) and the intent (Part 2), on a different model from their writer (brief: docs/briefs/09-critic.md), verbatim. Recorded by the orchestrator. Session session_01QBwHGHrHnEvMNYgKDoaH8w, 2026-11-01.

## Round 1
Verdict: FAIL

Scope: I checked section 1, the chain paragraph in section 2, sections 4, 5, 8 and 9, the Groundwork and Load-bearing unknowns parts of section 7, and Part 2. Sections 3 and 6 and the pre-mortem were read only for consistency. Records read: IDEAS.md, the P-001 decision records, the handoff, SURFACES.md in Model-Lab and the Personal-Org-Operating-Model OPERATING_MODEL.md.

Passes:
- Section 9 is the one-line form, "The owner is the user." It is not contradicted: no one but the owner uses this work.
- Section 4 names an owner for the archiving of Model-Lab (the owner, by their own GitHub action) and for every other deliverable row.
- Tier T1 matches Model-Lab's AGENTS.md.
- Every owner quotation in Part 2 matches its record word for word. This covers the "refined prompt engine" passage, "all but lower agent usage and less of my time", the "6 different repos" line, "done right", the token checkpoints, "everything should be touched", the slip-ups line and the session-move line.
- The phrase "integrated into the operating model completely" matches too.

Findings:

1. BLOCKING, section 4. Several owners do not match what the role may write (SURFACES.md, OPERATING_MODEL.md §5).
   - "The candidate changes, and running the test exactly as registered (M4) | Builder": the Builder's lane is src/**, tests/** and docs/handover/**. Role files and templates sit in .claude/** (orchestrator surface) and AGENTS.md and governance/** (chief-of-staff surface). The kept changes land in another repository with its own roster. No row says who writes a candidate change to a role file or brief.
   - "Researcher; Source checker" for memos, and "Researcher, checked by the Source checker" for the M1 count: the Researcher is reviewer-class with no write tools and no shell. The Orchestrator records its returns. A count from records needs a named role that can read and compute, and the row should say who records it.
   - "The Reviewer analyses the results": the Reviewer is also reviewer-class and writes nothing, so the row should say the Orchestrator records its verdict. The notes column is silent on this.
   - Rewrite the owners so each can write what the row gives it.

2. BLOCKING, sections 1 and 8. The scope and the defined terms disagree.
   - Section 1 says "Every kind of agent work", following the owner's "everything should be touched".
   - Section 8 defines "*Kind of work:* plans, research and built work" only. M1's "each kind of task" and the V1/V2 targets depend on this list.
   - Either the Critic, Definer, Check author and the rest are in scope and need a kind, or the terms narrow the owner's ruling on their own. Narrowing is the owner's call and should go on the card. Section 8's constraint list does not mention this tension.

3. NON-BLOCKING, section 7. A load-bearing unknown is missing.
   - R7 says past records may be unable to assign a cause, especially for conversation-started work, and that records of dropped work, a third of dispatches and anything after 8 October are missing.
   - U1 assumes the count can separate avoidable returns from caught faults. Its fallback is the stop rule, which is the wrong remedy for "the records cannot show causes".
   - Add a "whether the records can show causes at all" unknown with its closing test and fallback. U2 and U3 will also need the owner's recorded acceptance in decisions/ to stay open into Design (definition of ready item 7). The text says "draft", which is fine for now.

4. NON-BLOCKING, sections 3, 6 and 8. The run limits are not reconciled.
   - M2's "done when" says the test size is "within the owner's 100-run limit".
   - Sections 6 and 8 say the test needs about 300 runs, with its budget ruled at the Build gate. The 100 runs cover only Discovery and Design.
   - The replay check in U2 and the judge-consistency repeats in U3 also use those 100 runs. Section 8 only says "no conflict" for the 100-versus-300 pair. It does not say how M2 is satisfied, or what is left of the 100 after U2 and U3.

5. NON-BLOCKING, section 4. Two deliverables have no row or owner.
   - "Adopting the new model version in the Service Desk" appears in no scope item or milestone.
   - The LL-25 session-move notice has two parts. The desk part is Out in section 1. The model part belongs under M6 (P-001-session-move-notice.md says it goes to the operating model under its own rules), but no row owns it. Section 1 says "this project only records the need", which understates what the ruling gives M6.

6. NON-BLOCKING, section 5. "Spend ceiling: not yet ruled; proposed to the owner with the Design gate" gives no proposed figure.
   - Definition of ready item 5 wants the ceiling. It is the owner's to set, but the brief should say what is proposed.
   - "AI usage within the owner's existing plan" cites no record. The test-budget record says only "okay with 100 runs" and token checkpoints.

7. NON-BLOCKING, Part 2. Several lines go further than their records.
   - "Spending tokens is fine": the record says "I'm okay with 100 runs". "Fine" is broader.
   - The "What the owner would hate" bullet includes "separate status pages". The handoff says "No status pages now that the project is on the desk", and LL-17 says the owner asked for a single status page. LL-11 and LL-17 are the Chief of Staff's own lessons log, not the owner's words. "Hate" is an inference. Label these as inferred, or keep only the lines the owner said.
   - "What success means" glosses "all but lower agent usage and less of my time" as "fewer review rounds and better research". That is the Chief of Staff's reading of the options put. It omits "obviously there are trade offs". Say it is a reading, or quote both.

8. NON-BLOCKING, Part 2 and section 8. Both cite decisions/questions/P-001-value-target.md, which is not on branch cos/p001-discovery-2.
   - It exists only at /home/user/wt/ml-ans/decisions/questions/P-001-value-target.md and says option A.
   - Make sure it is merged before the cite is relied on. Separately, the "What success means" bullet cites it only for "ruled as V1 and V2", which is accurate.

9. NON-BLOCKING, section 8. The terms are mostly enough.
   - "AI model" versus "operating model" is clear.
   - "Run" is deferred to "fixed before testing", which is acceptable.
   - Section 8's own constraints (no timeline versus a date-less target, and M5 versus archiving) are consistent.
   - The six-month "too few pieces" rule in section 6 is a calendar limit beside "no fixed timeline". It was owner-adopted in the value-target ruling, so no contradiction.

No other item decides something for the owner. The scope narrowing in finding 2 is the one candidate. The spend ceiling is correctly left to the owner.
