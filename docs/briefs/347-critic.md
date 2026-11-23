# Brief 347 — critic — the two Build gate cards for P-002, round 1

session: session_01QBwHGLMjQEZefR9gzXbPS8
model: claude-sonnet-5-5 (the cards' writer, the Chief of Staff, runs on claude-opus-5-5; D-056). A fresh session.
recorded: at dispatch, 2026-11-22 (LL-04, LL-24)

## Brief

You are the Critic (your role file: .claude/agents/critic.md), reading decision cards cold as a smart non-expert (D-019). Today is 2026-11-22. Read-only; your return is recorded verbatim by the Orchestrator as reviews/P-002-build-gate/critic.md, round 1. Read only from the fixed copy /tmp/claude-0/-home-user/46a16990-6c77-5cf3-ac0a-e9b9f3fdee4e/scratchpad/ml-fixed-346 (Model-Lab at 809bb44).

The cards: questions/P-002-build-gate.md (the gate: proceed, hold, recycle or kill, approving specs/S-002.md's scenarios AC1 to AC21 and Build's and Launch's standard lines) and questions/P-002-build-gate-terms.md (the plan's open questions 2 to 9 and three further points, before the freeze). Their form: questions/_TEMPLATE.md and AGENTS.md §4 "Plain English first" and §5; the decision-card form of Personal-Org-Operating-Model OPERATING_MODEL.md §2. As the precedent the owner ruled for the prompt engine's Build gate, the cards are cut down to the decisions, pointing to the plan instead of copying it, arguing only the terms that touch the owner's earlier rulings, the value target, a rule change or anything irreversible, and listing the rest with the plan's proposed answer (decisions/questions/P-001-build-gate-stop.md; the passed cards at git history are not in your copy, so judge against that ruling's words).

Check: (1) each card opens with a plain-English paragraph leading with anything failed or skipped, with no paths, code or ids; (2) every claim, option, gain, cost and recommendation is true of the records it names (specs/S-002.md, especially "In plain words", "Acceptance criteria", "Risks and mitigations" and "Open questions for the owner"; experiments/E-004.md; reviews/S-002/plan.md; research/Q-018-memo-5.md; docs/projects/P-002.md; decisions/questions/P-002-*.md; reviews/Q-018-extract/critic.md); (3) the gate card's list of what approval carries beyond earlier rulings is complete and fair against the plan's own statements of its design and limits; (4) each term on the terms card states the plan's open question fairly, nothing open in specs/S-002.md "Open questions for the owner" is missing, and the split between argued and listed terms follows the ruling above; (5) the risk class, reversibility, default and timeout are right. Do not read docs/briefs/** other than this file, or docs/reports/**, or any -notes.md file.

Return first `Verdict: PASS` or `Verdict: FAIL` on its own line (FAIL if either card has a blocking finding), then numbered findings by card, each marked blocking or not, with evidence by file and line; then the six-part contract.
