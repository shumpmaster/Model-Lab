Verdict: PASS

The Critic's check of the prompt engine's milestone lines (docs/PROJECT.md section 3), on a different model from their writer, verbatim: round 1 (FAIL), round 2 (PASS). Recorded by the orchestrator. Session session_01QBwHGJH9m3A4Ray7WpHzBo, 2026-11-01.

## Round 1
Verdict: FAIL

Scope: section 3 of /home/user/ml-cos/docs/PROJECT.md, checked against OPERATING_MODEL.md §3 "Milestones, sprints and steps", §3 "Why and context", §4 "Standard milestones", the seven P-001 rulings in /home/user/ml-cos/decisions/questions/, the idea log, and the research memos (Q-001 to Q-003 in part). Two lines fail outright (M2, M4). Four more need rewording or a ruling (M1, M3, M5, M6). The standard lines pass, with two small notes.

**Standard lines (Discovery-1 to 8, Design-1 to 6)**
- All 14 are present, in phase order, each with `(standard) · taken on · why:`. None has " · " inside its why.
- Phase and number match the §4 table. The whys are true to the records and plain.
- Discovery-1: matches the idea log. The owner agreed on 2026-11-01 and ordered this idea first.
- Discovery-4 and Discovery-6: supported by the Q-001 memo's design traps and the Q-002 memo. Q-002 says no study splits the variance across all levers, and that inputs and context dominate one failure kind. "May not be the main cause" is correctly hedged.
- Discovery-5, "six research questions": this matches only if Q-001 (the groundwork map) is not counted, since the research folder holds Q-001 to Q-007. Please confirm the count.
- Discovery-2 is true but only restates the milestone. Suggested wording: "the owner wants fewer review rounds and better research, and the project needs a point at which it stops". This is optional.
- Discovery-7 is true. It rests on the test-budget ruling and on the across-the-model ruling for session records.

**M1: "The causes of rework are known"**
- The name is an achievement and has no codes. Its why is true: "minimize the gaps" is the owner's phrase, and "inputs and how work is split" is in the Q-001 and Q-002 memos. The line does not assume instructions are the cause. Good.
- "Known" cannot be told done or not done.
- The "done when" is clumsy ("work being sent back across the model's past work"). Its "starting point to compare later changes against" is the experiment baseline, which is Design work (Q-003 RQ-b). Keep it only if the baseline comes from past records and not from new runs.
- Suggested "done when": "the share of work sent back is counted from past records for each kind of task, each kind has a stated cause, and a starting figure is on record for later comparison".

**M2: "A fair test of instruction changes is ready" (FAIL)**
- The name assumes instructions are what gets changed, which is the thing the research has not settled. The Q-002 memo says wording is a noise source and that inputs, task split and checks are co-equal levers.
- Change the name to "A fair test of the changes is ready".
- In "done when", change "comparing instruction versions" to "comparing each candidate change with leaving things as they are".
- "Registered in advance" and "no-change arm" are jargon. Plainer: "written down before any run" and "a group where nothing changes".
- Why, claim too strong: "only a paired test of this size can tell a real gain from noise". The Q-003 memo says about 100 paired runs detect only large gains, roughly 15 to 20 points or more, and that below that nothing can be told from noise. Replace with: "the owner accepted that no change may be the result, and the research found that about 100 paired runs can only show large gains, so the test must be set up before it is run".

**M3: "Every agent's brief and model on record"**
- The name and "done when" are an achievement and can be checked. The phase is right, and the why is true to the session-records ruling and the idea log.
- The owner's ruling was about conversation-started agents. The line widens it to every session. That is harmless, but say so or keep to the ruling.
- Gap: the owner accepted the proposal to "record each agent brief and role card against how its work went (review rounds, fails, rework) … and improve the weak ones. Ongoing". No milestone covers tying a brief to its outcome, or the ongoing refinement.
- Fix: add to M3's "done when" "…and each brief can be read against how its work went", or add a new milestone for it.
- Overlap: M3 and M5 both cover the recording rule.

**M4: "Instruction changes proven or ruled out" (FAIL)**
- The name assumes instructions again. Suggested: "Each tested change has a result".
- "Done when the registered test has run" is an activity. Suggested: "every tested change has a recorded result: kept, dropped, or no difference found".
- The why is true to the owner's words ("not redundant with the flow of the operating model").
- Budget conflict: the test-budget ruling allows about 100 runs through Discovery and Design only. A test that runs in Build falls outside it. Either a new owner ruling on a Build budget is needed, or the line must say that the runs are inside the 100. Nothing in section 3 or its why says which.

**M5: "The operating model runs on what worked"**
- "Service-Desk has adopted that version" was not asked for. The owner's words are "integrated into the operating model completely" and "not 6 different repos". Remove it, or the why must cite where the owner asked for it.
- Missing: the work-repo ruling, that each result moves fully into the model repository. Suggested "done when": "…are part of the operating model under its own rules, and nothing of the result is left only in the work repository".
- "Rules for … testing" were not asked for. Keep only the recording rules, or drop "testing".
- Phase question: §3 says nothing is built in Launch, yet this milestone is model-change work that needs reviewed sprints. Consider Build. A phase change is the owner's ruling once approved, but it is free to change now while the line is a draft.

**M6: "Every slip in this work corrected"**
- The name is an achievement, and the "done when" and why match the lessons-log ruling exactly.
- Same phase question as M5: corrections to the model are built work, so Launch is doubtful. Confirm the phase or move it to Build.

**Across the set**
- The screening idea (2026-10-15) is a separate project that follows this one. No P-001 milestone is needed for it. The only link is the shared work repo being archived once both ideas are in. Make sure M5 or section 4 says who archives it, so the owner's "one repo" ruling is carried out.
- Not milestones, but they must show up elsewhere in the brief:
  - the owner's token checkpoints (test-budget ruling) belong in sections 5 and 6;
  - "no timeline" (time-and-limit ruling) also belongs there.
- Nothing is in section 3 that the owner did not ask for or the research did not require, apart from the Service-Desk adoption in M5.
- The standard-milestone "taken on" lines are all fine, and no milestone has a code in its name.

Wording to change, in summary: M2 name, "done when" and why; M4 name and "done when", plus the budget question; M1 "done when"; M3 "done when" (outcome link); M5 "done when" (drop Service-Desk adoption, add the work-repo move, trim "testing"); the phase of M5 and M6 (confirm or move).

## Round 2
Verdict: PASS

Every round-1 finding is resolved. I found nothing new that blocks.

**Resolved**
- **M1:** the new "done when" can be told done or not. It counts the share of work sent back from past records, gives a stated cause for each kind of task, and records a starting figure. It does not assume instructions are the cause.
- **M2:** the name, "done when" and why no longer assume instructions. The why now matches the Q-003 memo: about 100 paired runs show only large gains. "Written down before any run" and "a group where nothing changes" are plain.
- **M3:** the outcome link is added. The new why is true: the Q-001 source check (C1) confirms the script-dispatched control record holds the brief and the model, so "the automatic pipeline already records it" stands. No " · " inside the why.
- **M4:** the name and "done when" now read as a state. The budget question is handled: runs fall within the testing budget the owner sets at the Build gate, which fits the budget ruling covering Discovery and Design only.
- **M5:** the Service-Desk adoption and "testing" are gone. The work-repo move is in "done when", and the why cites the owner's ruling. Build is the right phase.
- **M6:** the line is unchanged and still matches the lessons-log ruling. Build is acceptable. The corrections are model changes that need reviewed sprints.
- **Discovery-2 and Discovery-5:** the rewordings are true. Seven questions with the groundwork map among them matches Q-001 to Q-007.

**No Launch milestone of the project's own:** this is not a problem. The model requires at least one own milestone per project, not per phase, and Launch has no built work. Launch's standard lines are due before the Build gate, so remember them then.

**Minor, not blocking**
- /home/user/ml-cos/docs/PROJECT.md line 42 is a blank line that splits the Build list before M5. Remove it.
- Design-3's why still says "whether instruction changes help is unknown". Consider "whether the candidate changes help is unknown and must be tested, not assumed", to match M2 and M4. The same goes for Design-5's "the agents' instructions" if you want the set consistent. This is optional.
- Section 4 must name the archiving of the work repo (second project) and the token checkpoints belong in sections 5 and 6. Neither is a milestone matter.

