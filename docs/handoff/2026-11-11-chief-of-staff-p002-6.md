# Handoff — the screening of cutting-edge practice (P-002), 11 November 2026, sixth stopping point

*Written by the Chief of Staff (session_01QBwHGJRsdA6DND96m5Z9xE). It follows docs/handoff/2026-11-11-chief-of-staff-p002-5.md.*

## What this means for you

The screening's brief is ready for the Design gate. It failed its check three times, you chose one focused last check, and that passed. The odds behind your target were re-run by someone who did not write them: every figure was reproduced, and three were restated more fairly, with nothing you ruled changed. Your answer, the passing check and this handover are kept back until the open pull request merges, and then go up as a new one. The next session writes the Design-gate case. Nothing here is irreversible.

## Where it stands
- **The brief** (docs/projects/P-002.md, Part 1): every section filled; milestones M7 to M15 and the Discovery and Design standard lines drafted for the owner to approve at the gate. Critic: FAIL at rounds 1 to 3, Triage (triage/P-002-brief-round-3.md), the owner's ruling (decisions/questions/P-002-brief-stop.md, A), PASS at the focused round 4 (reviews/P-002-brief/critic.md).
- **The odds** (M7): the Reviewer's independent run, FAIL, FAIL, PASS (reviews/P-002-value-target-odds/reviewer.md); corrections in intake/P-002-value-target-odds-2026-11-10.md, round 4, and section 6.
- **Pull request #93** holds everything up to the stop question. Local only, waiting on #93's merge (LL-32): the answer record, brief 251, the round 4 record, LL-79's status, the session line for round 4 and this handoff. After #93 merges, push them as a new pull request that also deletes questions/P-002-brief-stop.md (AGENTS.md §5).

## Next, in order
1. Land the local commits as above.
2. **The Design-gate case** (OPERATING_MODEL §4, "Phase gates"; about 350 words before the appendix), with the Critic's gate view on a different model. The owner is the user, so the user representative is not needed. The gate asks the owner to: approve the milestones and standard lines; set the spend and owner-time ceilings (decisions/questions/P-002-groundwork-shortlist.md, answer 8); accept or not each open unknown U1 to U5 (section 7), each acceptance recorded in decisions/; rule each proposal in section 6's last bullet; say whether any part may start before the prompt engine finishes (pre-mortem R15); and accept M7 or not.
3. Before the gate card, write one list of every trial term, each marked ruled or proposed, from the rulings and the cards as put (LL-79; Triage's root cause), and give every checker the cards as files from round 1: /home/user/ml-fixed-249-cards/ is gone in a new container, so rebuild them with `git show 964da47:questions/P-002-value-target.md` and `git show 3ae1268:questions/P-002-trial-gates.md`.
4. Round 4's non-blocking findings to carry into the gate card (not fixed after the pass, so the passed text stands): "two cards per trial" is in the proposed list though the two approvals are ruled; "fixed trial plan" and "the Critic's view" are attributed to the owner's design though the card marked them as added; the intake files hold less of the cards than the brief says; R7 says "proposed" for a check part 4 ruled; the Source checker row does not say how outside text reaches it.

## Standing conditions (unchanged)
- While P-002 is in Discovery, the prompt engine files no new groundwork request, or checks that any it files is counted to it (decisions/questions/P-002-route.md). Do not disturb the prompt engine's running work (PR #87 is its own).
- Each brief sending the Critic a P-002 plan carries the line that a plan review reads docs/projects/P-002.md, until critic.md takes the model's copy after E-003 (L-0008).
- The owner's private details are never written to any file or sent out.

## Mechanics learned this session
- Run the full check on a simulated `--no-ff` merge into main in a separate worktree, and push only in a separate step after reading a pass (LL-29); it caught an extra key on a session line (the sessions check allows none).
- A resumed helper's tokens are its running total (LL-67): the Reviewer's three rounds reported 56,443, 67,025 and 74,097.

## Slips this session
LL-77 (two odds figures stayed wrong after a check flagged one), LL-78 (the boundary with the prompt engine guarded trials only; the screener step had no owner) and LL-79 (three Critic rounds; ruled and proposed never set out in one list) are in docs/LESSONS.md.

## Token checkpoint
Seven helper sessions reported 486,132 tokens in all: the Reviewer 74,097 (its running total over three rounds), the Critic 106,709, 81,742, 86,107 and 75,847, and Triage 61,630, in sessions/chief-of-staff/session_01QBwHGJRsdA6DND96m5Z9xE.jsonl. The session's own usage is not read here.
