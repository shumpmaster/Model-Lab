# Handoff — the prompt engine (P-001), end of 1 November 2026

*Written by the Chief of Staff (session_01QBwHGJH9m3A4Ray7WpHzBo) at a natural stopping point, so a fresh session can carry on without this conversation.*

## Where it stands
- **Phase:** Discovery, first run. Model-Lab is live on the desk (Service-Desk #263, deployed to production 2026-11-01).
- **Done:** work repository (decisions/questions/P-001-work-repo.md); groundwork map Q-001 and its checks; the owner's five shortlist answers (decisions/questions/P-001-*.md); research Q-002 to Q-007, each memo source-checked and corrected, final confirmation in research/Q-002-to-Q-007-corrections-confirmation.md; the six milestones drafted and Critic-passed (docs/PROJECT.md section 3; reviews/P-001-milestones/critic.md); the lessons log (docs/LESSONS.md, LL-01 to LL-24).

## Next, in order
1. **File the checked facts in the library.** The confirmation lists which entries may be filed, per memo. The library lives in the portfolio repository (library/**), filed by the Source checker (OPERATING_MODEL.md §5, §6).
2. **Value target and stop rule** (docs/PROJECT.md section 6), with the owner's token checkpoints and "no timeline" (decisions/questions/P-001-test-budget.md, P-001-time-and-limit.md). Discovery-2.
3. **Problem statement**, industry-free, checked against how other fields solved it (Q-005). Discovery-4.
4. **Pre-mortem** (what could make this fail), its risks shaping any further research. Discovery-6.
5. **The rest of the brief:** sections 1, 2, 4, 5, 7, 8, 9 ("The owner is the user."), and Part 2 the intent. Section 4 names who archives Model-Lab once both ideas are in.
6. **Questions for the Design gate** (filed first, Critic-checked on a different model): whether researchers may read the web directly (L-0005, LL-07); who approves role-file changes and whether instructions are re-checked on model changes (both withdrawn earlier, to come with evidence); the desk follow-ups (a project with no milestones reads as finished, LL-21; deploysNeedOwner on one project only; the "default branch not found" wording, reviews/263 in Service-Desk).
7. **Before the second idea starts:** the tools assume one project per repository (LL-16); bring the owner options.

## Standing preferences of the owner (also for the intent, Part 2)
- No status pages now that the project is on the desk (2026-11-01).
- No fixed timeline; "done right"; several researchers at once is fine.
- Up to about 100 test runs through Design, with token checkpoints in each status update; the owner's remaining plan usage cannot be read from a session.
- Every slip goes in the lessons log the session it is found.

## Working rules learned the hard way (see docs/LESSONS.md)
- Start every checker on a different model from the work it checks (LL-03).
- Log each helper and save its brief and model at dispatch (LL-04, LL-24).
- Check the live state of every pull request and deploy before reporting it (LL-11, LL-23).
- Keep helpers reading a fixed branch; edit other branches in their own worktrees (LL-19).
- Commit by lane with explicit identities; run the surface guard's diff check before every push (LL-13, LL-18, LL-20).
- Test that the environment reaches the sources before dispatching research (LL-12, LL-22).
