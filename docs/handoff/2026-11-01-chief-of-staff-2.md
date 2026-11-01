# Handoff — the prompt engine (P-001), second session of 1 November 2026

*Written by the Chief of Staff (session_01QBwHGHrHnEvMNYgKDoaH8w) at a natural stopping point, so a fresh session can carry on without this conversation. It follows docs/handoff/2026-11-01-chief-of-staff.md.*

## Where it stands
- **Phase:** Discovery, first run.
- **Done this session:**
  - The checked facts are filed: 88 entries in the portfolio library (portfolio PR #3, waiting for the owner's merge; library/README.md indexes them). Held back: F-Q004-5 and everything the confirmations hold.
  - **Success defined (Discovery-2):** the owner ruled option A (decisions/questions/P-001-value-target.md, in PR #10): first-time pass rate up 20 points; V1 in the paired test, V2 over the first 30 real pieces of each kind; no calendar date; the miss and stop rule adopted with it. Written into docs/PROJECT.md section 6. Critic: reviews/P-001-value-target/critic.md (PASS at round 4).
  - **The right problem chosen (Discovery-4)** and **the risks known (Discovery-6):** problem statement in section 2, pre-mortem R1–R9 in section 7. Critic: reviews/P-001-problem-premortem/critic.md (PASS at round 3).
  - **The rest of the brief** (sections 1, 2 chain, 4, 5, 7 groundwork and unknowns U1–U5, 8, 9 "The owner is the user.") and **Part 2, the intent.** Critic: reviews/P-001-brief/critic.md (PASS at round 2). M2's done-when reworded (decisions/questions/P-001-milestones-m2-runs-critic.md).
  - **The owner's unasked ruling:** the desk notifies the owner when a conversation must move to a new session, in the model and the desk (decisions/questions/P-001-session-move-notice.md; lessons log LL-25).
  - Lessons log LL-25 to LL-27.
  - Research question Q-008 (the count of past rework, M1) drafted and sent to the Critic (brief 10); see "Open at handoff".
- **Branches** (all pushed): cos/p001-discovery-2 (the brief, two decision records), orch/p001-discovery-2 (briefs 06–10, review records, lessons, Q-008, this handoff), cos/session-01QBwHGHrHnEvMNYgKDoaH8w (session lines). Their pull requests are listed in the owner's closing message.

## Next, in order
1. **The count of past rework (M1, closes U1 and U5).** Once Q-008 passes the Critic, dispatch a Researcher on it (records only, no web: no network check needed, LL-22), then a Source checker on a different model. Its figures replace section 6's starting figures, and the real-use odds are restated. If it shows the instructions are not a meaningful cause of avoidable rework for any kind, the stop rule sends the project to the owner.
2. **Questions for the Design gate** (filed first, Critic-checked on a different model):
   - the spend ceiling (section 5 carries the Chief of Staff's proposal);
   - accepting U2, U3 and U4 as open into Design and Build (definition of ready item 7);
   - whether researchers may read the web directly (LL-07);
   - who approves role-file changes, and whether instructions are re-checked on model changes (withdrawn earlier, to come with evidence);
   - the library's open choices from the Source checker: shelf lives (OPERATING_MODEL §6 [open]), mapping the memos' letter grades to strong/moderate/weak (Q-007's "A" means opened, not strong), and fields the pattern form lacks;
   - the desk follow-ups (LL-21; deploysNeedOwner on one project only; the "default branch not found" wording, Service-Desk reviews/263) and the route for the desk's part of the session-move notice (LL-25; the desk is graduated, so the owner approves the route).
3. **The brief's last pieces and the definition-of-ready check:** the Discovery-1 to -8 and Design lines in section 3 stand; after M1, the Critic checks the whole brief against the definition of ready, then the Design gate case (docs/gates/, the gate form) goes to the owner.
4. **Before the second idea starts:** the tools assume one project per repository (LL-16); bring the owner options.

## Open at handoff
- Q-008's Critic check (brief 10) was running when this was written; its verdict goes in reviews/Q-008/critic.md.
- PR #10 (the value-target answer) had all checks green and was waiting for the asks-merge workflow.
- Portfolio PR #3 (the library) waits for the owner: the portfolio repository has no asks-merge workflow.

## Token checkpoint
Helpers this session reported about 851,000 tokens in all before the Q-008 check (the session lines hold each figure). This session's own tokens and the owner's remaining plan allowance cannot be read; the plan's weekly limit allowed use at the time of writing.

## Working rules carried forward
Those in the first handoff, plus: run `governance_checks.py pr-body` on a drafted body before opening a pull request (LL-27); before citing research, look up the entry's filing status in the confirmation or the library (LL-26).
