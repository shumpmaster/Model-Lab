# Handoff — the prompt engine (P-001), 4 November 2026, sixth stopping point

*Written by the Chief of Staff (session_01QBwHGMBo8kZsMCS2EvKNwd). It follows docs/handoff/2026-11-04-chief-of-staff-5.md.*

## Where it stands
- **PR #44 (open, draft)** holds: the per-task reading lists in governance/PACKS.toml (Reviewer PASS, reviews/44/reviewer.md; R3, needs the owner's verdict reviews/44/owner.md and merge); the Build gate case's first draft (docs/gates/P-001/build-gate-1-case.md); the two gate questions (questions/P-001-build-gate.md and P-001-build-gate-terms.md, round-2 drafts, not yet re-checked); the gate Critic's view (reviews/P-001/_build-gate-1-critic.md: recommendation hold); the questions' Critic round 1 (reviews/P-001-build-gate/critic.md: FAIL).
- **The case's blocker (LL-49):** the gate Critic's main findings are that the case shows the owner none of the criteria to approve, the budget options or the open questions, and carries too few risks. The first two cannot be cited from the case: `v3_checks gates` accepts only records the gate Critic's pack holds, and with no status record the plan (specs/S-001.md) is not among them. The gate-record ruling bars writing a status record by hand.
- **Standard lines:** Build-1, Build-3 and Launch-5 in docs/PROJECT.md need rewording (reviews/P-001/_build-gate-1-critic.md, "Standard lines"), then a Critic check.

## Next, in order
1. **Put the LL-49 choice to the owner as a filed question** (one card): A, the case cites the plan directly and the gate check stays red on that one point, recorded as the known gap (fastest; a red check the owner merges past); B, the case carries the criteria in a citable record in docs/gates/P-001/ (for example the gate's proposal file, which the model reserves for what a user would see, including the scenarios; the owner is the user here, so no user representative reads it), so the check stays green (some duplication of the plan's text); C, first make the gate-record change in Personal-Org-Operating-Model so the checks read the item's spec (the right fix; slowest). Trace each option through `v3_checks.py` check_gates and citable_paths before stating its effect (LL-46, LL-50).
2. **Rework the case** on the owner's answer: the scenarios, the budget options beside the earlier "about 300 runs", the open questions (or a pointer to the terms card), the power limit and the plan review's carried risks with what we would do and where each stands, every citation the gate Critic named, "Discovery: done / Design: done" cited to the Design gate ruling, the spend line restated ("the ceiling is your plan; whether 732 runs fit is not known"), the project's stop-and-go-to-the-owner rule in section 7, and the Reviewer's note on the analysis list's comment as a risk.
3. **Reword Build-1, Build-3 and Launch-5**; Critic check.
4. **The questions' Critic, round 2** on the two gate cards (they were redrafted for round 1's findings 1 to 11; send them with the reworked case).
5. **Then put the gate**: the owner's verdict on PR #44's reading lists, the gate card and the terms card together.

## Token checkpoint
This session, by its own status at this point: about 574,000 tokens of context in use and about $52.21 estimated cost. Helpers since the fifth stopping point: Reviewer 109,826; gate Critic 64,654; questions' Critic 58,609.
