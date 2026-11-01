# Ruling needed: how we will know the prompt engine worked, and when we stop

Milestone: Discovery-2

WHY: Every project must say from the start what it must improve, by how much, by when, and when it stops (the model's "Success defined" milestone). Setting this target is yours alone and cannot be delegated or defaulted. Until it is set, the fair test (M2) has no measure to aim at, and the brief cannot go to the Design gate.

What you told us you want: fewer review rounds and better research, and to close the gaps in how work passes between agents; lower agent usage and less of your time are not the aim. You ruled there is no fixed timeline, and that finding "changing the instructions doesn't help" is an acceptable result.

The measure in every option below is the **first-time pass rate**: of the pieces of work that go to a check (a plan to its review, a research memo to its source check, built work to its reviewer), the share that pass at the first try. Each failed try is a review round. Today, from the Service Desk's records: about 1 in 17 plans passed every checker first time, 2 in 12 research memos, and about 3 in 10 pieces of built work.

OPTIONS:
  A. **Two targets, sized to what our test can see.** (1) In the fair test, a change is kept only if it raises the first-time pass rate of the work it targets by at least 20 points over leaving things as they are, on the same past tasks. With about 100 runs, a gain much smaller than 20 points cannot be told apart from chance. Checked at the end of testing, before the changes go into the model. (2) In real use, once the kept changes are in the model: over the first 30 pieces of each kind (plans, research, built work) checked under it, in any project, the first-time pass rate is at least 20 points above today's figure for that kind. Checked when the 30 pieces of each kind are done, at the model's next rule review; no calendar date, as you ruled. Gain: one measure for both of your aims, sized so the test can actually see it. Cost: smaller real gains (say 10 points) would be missed and the change dropped. Reversible: you can change the target later.
  B. **The same two targets, measured as rounds per piece of work** (the typical number of tries before a pass falls by at least one round) instead of the first-time pass rate. Gain: closer to how you described it ("fewer review rounds"). Cost: with about 100 runs, a fall of one round is harder to tell from chance than a 20-point pass-rate gain, because most work would need to be taken to a pass, which costs more runs per task. Reversible.
  C. **Wait for the full starting figures before setting any number.** The milestone "The causes of rework are known" (M1) recounts today's figures per kind of task before the Design gate; set the target once it is done. Gain: the target rests on the finished count. Cost: the fair test (M2) cannot be designed until then, and the 20-point limit of a 100-run test does not change with the count. Reversible.

  **Under every option, the miss and the stop rule are:**
  - **Miss on target 1:** no change clears 20 points. We record "no change helps" (your accepted result), keep only the record of each agent's brief and model (M3), put that into the model, and close the project.
  - **Miss on target 2:** a change that passed the test does not hold up in real use. It is retired at that rule review, not tuned (the model's "killed, not tuned").
  - **Stop and come back to you** if the count of past work (M1) shows the instructions are not a meaningful cause of rework for any kind of task: you rule whether to re-aim the project or close it.
  - **Stop and come back to you** if the 100 test runs you allowed through Design are used up before the fair test is ready.
  - **Your time:** no cap, as you ruled. Each status update gives the tokens used so far and the number of questions put to you.

RECOMMENDATION: A, because it measures both of your aims (fewer rounds and better research) with one figure, and it is sized to what a 100-run test can detect, so a "kept" result is believable.
RISK CLASS: R3 (a value target, the owner's own ruling)   REVERSIBILITY: reversible (the owner can change it later)   BLAST RADIUS: this project's test design, its keep-or-drop decisions, and which changes reach the operating model
DEFAULT: none — value targets are never delegated or defaulted   TIMEOUT: none

## Context
- Every project states a value target and stop rule in its project document's section 6: its measure, target, date and miss, including the cost to the owner's time; value targets are never delegable (source: Personal-Org-Operating-Model OPERATING_MODEL.md §1 item 13, §2, §4 definition of ready item 6).
- Asked how they would judge the work, the owner chose fewer review rounds and better research, not lower agent usage or less of their time, with the core goal "to minimize the gaps that might arise from traditional orchestrasted workflows" (source: portfolio ideas/IDEAS.md, 2026-11-01 entry).
- The owner ruled no fixed length for Discovery and no cap on their time (source: decisions/questions/P-001-time-and-limit.md).
- The owner ruled that finding that changing the instructions doesn't help is an acceptable result (source: decisions/questions/P-001-no-change-result.md).
- The owner allowed up to about 100 test runs through Discovery and Design, with token checkpoints (source: decisions/questions/P-001-test-budget.md).
- With about 100 runs, a paired test on the same tasks has about 70–77% power for a 20-point gain and about 25% for a 10-point gain (source: research/Q-003-memo.md, §0 item 3 and §4, calculations).
- In the Service Desk's records, 1 of 17 plan items passed every checker at round 1, 2 of 12 research items passed the source check first time, and build stages passed first time in about 15 of 50 cases (source: research/Q-006-memo.md, §0 item 2).
- The conversational path did not record each agent's brief or model, so past records cannot say whether the instructions caused a finding (source: research/Q-006-memo.md, §0 item 1).
