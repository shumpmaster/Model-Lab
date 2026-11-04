# Handoff — the prompt engine (P-001), 4 November 2026, second session

*Written by the Chief of Staff (session_01QBwHGLd77YbwCSMSPU26vW) at a natural stopping point: the fair test's plan passed its review. It follows docs/handoff/2026-11-04-chief-of-staff.md.*

## Where it stands
- **Phase:** Design, first run. M1 accepted; its reached mark still waits (below).
- **The fair test (M2):** specs/S-001.md and its registration experiments/E-003.md, still `status: draft`. The Critic's plan review passed at round 3 of 3 (reviews/S-001/plan.md); its non-blocking notes are applied. Design: each new piece of work is done (or, for research, checked) twice from the same start, with and without one change; a held-back check, written by a Check author who never learns the changes, judges both blind on a different model (Fable 5.1); up to 8 owner cards per kind confirm the judge. One change per kind: C1 plans, C2 built work, C3 research. Recommended size: 60 pairs per kind, about 732 runs and 132 million tokens, 60 to 121 weeks one kind after another at the Service Desk's pace (32 to 64 collected together). Figures: experiments/E-003/output.txt.
- **The gate-record ruling (LL-43):** the owner chose "A: change the model (Recommended)". The question is PR #36 (cos/p001-ask-gate-record, all checks green), waiting on the owner's merge. The answer record is written on the local branch cos/p001-answer-gate-record (worktree /home/user/wt/ml-answer-gate, commit 5c4e973, based on the question branch) and is lost if this container is reclaimed; its full text is reproduced below. Open its pull request only once PR #36 is merged (rebase it onto main first).
- **Test runs used through Design:** 14 of about 100 (none this session).
- **Lessons:** LL-46 (an option's effects not traced through the code) and LL-47 (a helper's figures lost in a restart).

## Next, in order
1. **File the gate-record answer** once PR #36 merges (text below), in a pull request that also deletes the question file.
2. **The blind Check author's pack:** draft the `S-001-holdout` per-task pack in governance/PACKS.toml (the Chief of Staff's lane) as S-001's "Two Check author jobs" table lists; it is a rule change for the owner (S-001 open question 5) and must be merged before the Build gate. Check first whether the pack format can key a pack to a task.
3. **The join-up review closing Design (Design-5)**, then the Design standard milestones' records.
4. **The Build gate case** (docs/gates/P-001/), carrying S-001's seven open questions: V1's and M2's wording ("on the same past tasks" no longer holds), budget, size and order (options A to D), collecting kinds together against the "incrementally" ruling, recording each brief, start commit and model at dispatch (without it no plan or built piece can enter), judges within the plan, C3's tolerance. Include the Orchestrator's confirmation that the pack is in place (the plan review's round-3 note 4). The owner sets the test's budget there; the spec freezes after.
5. **The gate-record change** in Personal-Org-Operating-Model, under its own rules, as ruled.
6. Then the handoff's earlier items: at the end of the cycle the rule-change rulings and LL-01 to LL-47 into the operating model (M5, M6); LL-16 before the second idea.

## The gate-record answer record (decisions/questions/P-001-gate-record.md)
```
Ruling: A — change the operating model so the checks see the owner's recorded gate ruling, for projects run from a conversation
Question: questions/P-001-gate-record.md

Asked: 2026-11-04, in the Chief of Staff's session session_01QBwHGLd77YbwCSMSPU26vW, by the session's question tool, from questions/P-001-gate-record.md (filed in PR #36; Critic: reviews/P-001-gate-record/critic.md, PASS at round 3). A rule change: the owner's own ruling, never a default.

## The owner's words, verbatim
The owner chose: "A: change the model (Recommended)".

## How it is carried out
- The change is made in the Personal-Org-Operating-Model repository under its own rules: a spec settles the route (the checks read the recorded "proceed" ruling where no status record exists, or the pipeline's script writes the status record from it), then its tools builder builds it, an independent review checks it, and the owner merges it.
- It is then copied into Model-Lab's governance checks; until then no milestone here is marked reached and no status record is written by hand.
- Once the checks see the approval, M1's reached mark is added in a commit whose `Owner-Ruling:` trailer names decisions/questions/P-001-accept-m1.md.
- The related gap (standard milestones and the timeline reading "not recorded" for conversation-run work, LL-35 and LL-40) is not part of this change; it stays with the end-of-cycle model changes.
```

## How work ran this session
- A container restart mid-session lost one helper's reported token figure (LL-47); its hand-back text survived in its transcript.
- Plan-review rounds: the Critic was resumed for rounds 2 and 3, and each Definer round was a fresh session with its own brief (docs/briefs/27 to 31).
- The local `record_checks merges` failure on the orchestrator's record commits is the known false failure (LL-29); run the checks against a test merge signed as the owner, which passes.

## Token checkpoint
This session, by its own status: about 274,000 tokens of context in use and about $16 estimated cost. Helpers reported about 810,000 tokens, not counting the first Definer (lost in the restart). The plan's remaining allowance cannot be read; its weekly limit currently allows use.
