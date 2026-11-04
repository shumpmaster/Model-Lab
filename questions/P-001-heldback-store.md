# Ruling needed: where the fair test's secret marking sheets are kept

Milestone: M2

The fair test judges each piece of work with a secret marking sheet, one for each kind of work, written by a helper who never learns what is being tested. The work being judged must never see those sheets, and they must last as long as the test, which may run for many months. The operating model has never said where such sheets are kept, and this project's plan cannot be finished without an answer (the last fit-together check, finding 2). Both choices below keep the sheets out of every project's own repository, and either can be changed later. One needs a few minutes of your time to create a private repository; the other needs nothing from you but protects the sheets less well.

WHY: the plan's fix needs a named place for the sheets before its confirmation review; without one, the sheets cannot be written or checked, and the test cannot start (reviews/S-001/plan.md, "Round 4", finding 2; decisions/questions/P-001-plan-stop.md).
OPTIONS:
  A. A new private repository only for the sheets — Gain: the sheets last as long as needed, and the sessions that do the work being tested never hold that repository, so the work cannot reach them; only the session that judges is given it. What happens: you create one private repository (a few minutes, your own action), and judging runs in its own session with that repository attached. Cost: one action from you, and judging sessions set up separately from the work's sessions. Rules out: nothing.
  B. A folder in your private portfolio repository — Gain: no new repository; nothing needed from you. What happens: the sheets go in a folder there that no helper's reading list includes. Cost: every session in this environment already holds the portfolio repository, so any helper, including the ones doing the work being tested, could open the folder; the sheets would be kept away from the work by instruction only. Rules out: a test whose secrecy does not rest on instruction.
RECOMMENDATION: A — the test's worth rests on the work never seeing its marking sheets, and only A keeps them out of the work's reach rather than relying on instruction; the cost is one action from you.
RISK CLASS: R0 (questions/**)   REVERSIBILITY: reversible   BLAST RADIUS: the fair test's secret marking sheets and the sessions that judge with them; no other project
DEFAULT: none (A needs your own action, so it cannot be adopted by default)   TIMEOUT: none

## Context
- The last fit-together check found no record names where the secret marking sheets are kept or how a copy is shown unchanged (source: reviews/S-001/plan.md, "Round 4", finding 2)
- The operating model has not decided where hidden check sets are stored (source: Personal-Org-Operating-Model specs/S-009-v3-record-checks.md, AC8, "Known limit")
- This session's environment holds four repositories, the portfolio among them, and every helper it starts can read them (source: the session's own record of its sources, session_01QBwHGMBo8kZsMCS2EvKNwd)
- The portfolio repository is private, and Model-Lab and the Service Desk are public (source: the session's repository listing, 2026-11-04)
- Keeping the sheets only in a session's own storage would lose them when its machine is reclaimed, while the test may run for 60 to 121 weeks at the Service Desk's pace (source: specs/S-001.md, "Budget options by kind and order")
- The owner chose the focused fix, with the changes it needs approved separately (source: decisions/questions/P-001-plan-stop.md)
