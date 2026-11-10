# Handoff — the screening of cutting-edge practice (P-002), 10 November 2026, fourth stopping point

*Written by the Chief of Staff (session_01QBwHGNSLmSrYQgS6BPjV8p). It follows docs/handoff/2026-11-09-chief-of-staff-p002-3.md.*

## Where it stands
- **The target** is unchanged: how the owner's multi-agent system is run and optimised, with promising methods tried, not only credentialed ones (decisions/questions/P-002-target.md; docs/projects/P-002.md, Part 2).
- **Q-017, the count of the organisation's own records, is done.** Its memo failed its first source-check rounds on one sentence; the owner ruled to replace that sentence with the counts that occur and have one focused check (decisions/questions/P-002-q017-memo-stop.md). The fix is in research/Q-017-memo.md, section 3; the focused check (brief 237) passed (research/Q-017-source-check.md, last section). The extract and its script are in research/Q-017-extract/, with the hand check in research/Q-017-extract-sample.md. Rounds of rework were dropped from the count by the owner's ruling (decisions/questions/P-002-q017-decide.md).
- **Figures it gives as starting points** (research/Q-017-memo.md): 447 merged pull requests across the three repositories; plain commits under an agent identity 94.2% (Service-Desk), 98.9% (Model-Lab), 97.8% (operating model); pull requests holding a commit under the owner's identity 15.4%, 7.1%, 32.0%; the owner's account merged all pull requests except 86 bot merges on Service-Desk; files first added as questions 540, 82, 29; no reverts; later pull requests changing the same files within 14 days 202, 42, 33. Read the memo's limits before using any figure.
- **Discovery done:** research Q-010 to Q-016 (library entries in the portfolio library, PRs #9 to #11), the problem statement and pre-mortem (docs/projects/P-002.md sections 2 and 7), and the Q-017 baseline.

## Next, in order
1. **The value-target question (Discovery-2).** Draft it as questions/P-002-value-target.md from Q-017's figures and the library's Q-016 entries: options for the measure (the share of work agents carry, paired with a check that it holds up, such as owner interventions or later rework), the target level, the stop rule, and the rule for a trial that ends "not shown" (pre-mortem R9). The spend ceiling waits for the Design gate (shortlist answer 8). Critic check (on a different model), pull request, then ask the owner.
2. Then the milestones and the brief, the Critic, and the Design gate. The plan must carry the data-class table and the boundary with the prompt engine.

## Standing conditions (unchanged)
- While P-002 is in Discovery, the prompt engine files no new groundwork request, or checks that any it files is counted to it (decisions/questions/P-002-route.md).
- Each brief sending the Critic a P-002 plan carries the line that a plan review reads docs/projects/P-002.md, until critic.md takes the model's copy after E-003 (L-0008).
- The owner's private details are never written to any file or sent out. The extract script takes the owner's address as an argument only.

## For the prompt engine's session (not acted on here)
- Library entry Q-002-F-m states "17.2x", which the study's arXiv abstract does not carry (research/Q-015-entries-check.md). Worth a check before P-001 relies on it.

## Slips this session
LL-71 recurred; LL-72 (commits under the wrong role), LL-73 (a coding script run without a sample check, recurred), LL-74 (a session line on main edited in place) are in docs/LESSONS.md. Service-Desk PR #338 (portfolio pull requests on the desk, later work W3) is merged.

## Token checkpoint
Helpers' reported tokens are in sessions/chief-of-staff/session_01QBwHGNSLmSrYQgS6BPjV8p.jsonl; some are null where the helper's report gave none. The session's own usage is not read here.
