# Ruling needed: move the prompt engine into Build, and how big a test to run?

Milestone: Design-6

Two checks were not done, and you should weigh them first. Past work could not be re-run faithfully, so the test uses new work as it arrives, which is slow. The check of how accurate the judges are was skipped by your ruling, so their accuracy is unknown: if a judge is wrong one time in ten, the chance of seeing a real gain roughly halves. With that said, Design is done: the fair test's plan passed its review, and its parts were checked and fit together. Only you can move the project past this gate. Proceeding approves the plan's criteria, sets the test's size and budget, and lets the plan freeze, together with your answers to the terms asked beside this. Nothing here is irreversible except closing the project.

WHY: nothing goes past a gate until you rule; the test's budget is yours to set here, since your earlier allowance of about 100 runs covered only Discovery and Design (decisions/questions/P-001-test-budget.md; Personal-Org-Operating-Model OPERATING_MODEL.md §4 "Phase gates").
OPTIONS:
  A. proceed with the full test — 60 pieces of each kind, built work first, then plans, then research: 732 runs, about 132 million tokens, about 60 to 121 weeks one kind after another at the Service Desk's pace (32 to 64 if the kinds collect side by side). Your part: 9 sessions to start and about 24 to 27 short records to pass, if the sessions wake themselves as planned; if they cannot be resumed after their machines are reclaimed, up to about 183 to 366 session starts. Gain: an answer for all three kinds at the size the plan was built for. Cost: the most runs and the longest wait. Rules out: nothing; any kind can be stopped at its review points on counts alone.
  B. proceed with built work only first (the plan's option C; this goes against your ruling "no single kind first; every kind, incrementally") — 60 pieces of built work: 266 runs, about 48 million tokens, about 7 to 15 weeks; you decide the other two kinds on its result. Your part: 3 sessions and about 8 records, up to about 22 to 46 session starts if sessions cannot be resumed. Gain: about a third of the spend before you see the result and how the running worked. Cost: plans and research wait, and may not be tested. Rules out: nothing.
  C. proceed at another size — 40 pieces a kind: 490 runs, about 88 million tokens, 40 to 81 weeks; or 100 pieces for research and built work and 60 for plans: 1,040 runs, about 188 million tokens, 87 to 173 weeks (the plan's options B and D). Say which.
  D. hold — the case is updated with what you ask and comes back to you. Nothing moves meanwhile.
  E. recycle into Design — say what to redo and why; Design runs again as its second iteration.
  F. kill — the project closes; the lessons log still goes to the operating model.
  For any size: the budget counts the test's runs only. The sessions' own wake-ups (about 540 to 1,090 under A) and the weekly reviews of the work's records (60 to 121) are outside it and not estimated. And the chance of seeing a real 20-point gain at 60 pieces is about 4 in 5 under the library's middle assumption, but about 1 in 2 for built work and research if the two versions disagree as often as chance allows, and lower again if the judges err. Two of the three changes aim at causes worth at most about 11 to 19 points, so "not shown" is the likely result for them even if they help.
RECOMMENDATION: A, with medium confidence (the plan's recommendation, and the Chief of Staff's): 60 pieces is the smallest size that gives about 4 in 5 under the library's assumption for every kind, it follows your "every kind, incrementally" ruling, and built work, which comes first, tries the untested running on the fastest kind; a failed first check there comes to you before more is spent. What would change it: wanting to cap the spend until the running is shown to work, accepting a single kind first (then B).
WHO HAS CHECKED IT: the Critic, on a different AI model from the writer: the plan's review and the join-up review; its independent view of the case beside it; and its check of this card.
RISK CLASS: R2 (a phase gate; reversible except F)   REVERSIBILITY: irreversible   BLAST RADIUS: this project's next phase and the test's spend; option F closes the project, which is why this is marked irreversible
DEFAULT: none (irreversible; a phase gate is never ruled by default or by proxy)   TIMEOUT: none

## Context
- The case for going on, with the Critic's independent view (source: docs/gates/P-001/build-gate-1-case.md)
- Past tasks could not be replayed, and the judge-consistency check was not run, by the owner's ruling (source: decisions/questions/P-001-e002-not-tested.md; specs/S-001.md, "In plain words")
- The plan passed its review at round 3 with the join-up review, and its run, token and week sums were re-checked (source: reviews/S-001/plan.md, "New draft, round 1" and "round 3")
- The plan's budget options, power figures and smaller-gains warning, with the plan recommending A (source: specs/S-001.md, "In plain words" and "Budget options by kind and order")
- The owner's part per option, and the wake-ups outside the budget (source: specs/S-001.md, "What the separate sessions add" and "In plain words")
- The owner ruled the earlier allowance of about 100 runs for Discovery and Design only (source: decisions/questions/P-001-test-budget.md)
- The owner ruled "every kind, incrementally", with no single kind first (source: decisions/questions/P-001-worst-work.md)
- The owner rules each phase gate, never by default or proxy (source: Personal-Org-Operating-Model OPERATING_MODEL.md §2 and §4 "Phase gates")
- The first draft of this card failed its check: it did not lead with the skipped checks, stated the power as fact, and left out the wake-ups and the owner's part (source: reviews/P-001-build-gate/critic.md)
