# Ruling needed: when to fix six gaps found in the desk

Milestone: M6

WHY: Six gaps in the desk turned up during this work. The desk has graduated, so changes to it come back only as new work whose route you approve. Until you rule, the gaps and the workarounds below stay.

The six gaps:
  1. A new project with no milestones yet shows "no milestone left to reach", as if it were finished. Workaround: milestones are drafted before a project goes on the desk.
  2. The desk does not tell you when a conversation must move to a new session. You asked for this.
  3. Portfolio pull requests waiting on you do not show on the desk, and library patterns are not counted, only facts. Workaround: the Chief of Staff sends the link with every request.
  4. When GitHub's notice of a waiting deploy does not reach you, the desk's operating notes do not say where to find it. Workaround: the Chief of Staff sends the waiting run's link with every merge that starts a deploy.
  5. A project the desk cannot read because its access token does not cover it is described as "the configured default branch was not found", which is misleading.
  6. An open question for you inside this work: should "only the Service Desk needs your approval for deploys" be enforced, as its test's title and the spec read, or should any project be able to take up owner-approved deploys? Today the check allows either.

OPTIONS:
  A. **One piece of new work for the desk, started after this project's Design gate.** All six go into one new desk project item, with a short Discovery of its own sized to the work, then Design and Build under the desk's rules. *Gain:* one route and one set of reviews for all six; this project's Discovery is not slowed. *Cost:* the gaps and workarounds last until then. *Reversible:* yes.
  B. **The same new work, started now, alongside this project.** *Gain:* the gaps close sooner, including the session-move notice you asked for. *Cost:* two projects run at once, so more questions reach you at the same time and more helper tokens are used. *Reversible:* yes.
  C. **Split them:** the session-move notice (2) and the waiting-items gaps (3, 4) now, as in B, and the wording and rule gaps (1, 5, 6) later, as in A. *Gain:* what you asked for and what hides waiting items close first. *Cost:* two desk projects instead of one, so more reviews and asks in all. *Reversible:* yes.
  In every option, the operating-model side of the session-move notice stays in this project, with the other lessons (milestone "Every slip in this work corrected"). If this question defaults to A, nothing starts before the Design gate, and the route is put to you again then; a default is never your ruling.

RECOMMENDATION: A, with medium confidence: the workarounds already cover the gaps that could hide work waiting on you, and one route costs fewer questions and reviews than two. What would change it: if you want the session-move notice sooner, C.
WHO HAS CHECKED IT: the Critic, on a different AI model from the writer (record: reviews/P-001-desk-follow-ups/critic.md).
RISK CLASS: R1 (where new work starts; no code changes by this ruling)   REVERSIBILITY: reversible   BLAST RADIUS: the desk's next piece of work, and how many questions reach the owner at once
DEFAULT: A   TIMEOUT: 72

## Context
- A graduated product comes back only when the owner says a fix or addition is needed; the Chief of Staff files new work and proposes its route, and the owner approves (source: Personal-Org-Operating-Model OPERATING_MODEL.md §3 "Graduation and re-entry")
- A new v3 project with no milestone lines read "no milestone left to reach" on Home (source: Service-Desk reviews/263/design-reviewer.md B1; Model-Lab docs/LESSONS.md LL-21)
- The owner asked to be notified when a conversation must move to a new session (source: decisions/questions/P-001-session-move-notice.md)
- The desk reads the portfolio's records but not its pull requests, and counts library facts only (source: Service-Desk src/config/projects.json; src/public/lib/portfolio.js, RARE_DIRS; Model-Lab docs/LESSONS.md LL-28)
- A waiting deploy reached the owner with no notice (source: Model-Lab docs/LESSONS.md LL-23)
- An unreadable repository is described as "the configured default branch was not found", and the reviewer asked whether the deploy-approval rule should be enforced as its test title reads (source: Service-Desk reviews/263/design-reviewer.md F1; reviews/263/reviewer.md N1, Q2)
