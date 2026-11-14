# Brief 345 — critic — a check of P-002's Build and Launch standard lines, before the Build gate

session: session_01QBwHGJyHFoAkyeCseVWzup
model: the Critic runs in a fresh session, on a different model from the lines' writer where the environment allows (D-056). Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@69892823273a4569c47568b90221f4c9f6ba9f15
manifest: docs/projects/P-002.md (the ten new lines at :131 to :135 and :142 to :146, and the note at :96, with the rest of the document for their facts); specs/S-002.md and experiments/E-004.md; AGENTS.md; decisions/questions/P-001-work-repo.md; research/Q-018-memo-5.md; reviews/S-002/plan.md; docs/handoff/2026-11-12-chief-of-staff-p002-14.md ("What this means for you"); governance/checks/v3_checks.py :549 to :565 (the model's names for the standard milestones)
recorded: at hand-out, 2026-11-14

## Brief
You are the Critic, checking standard milestone lines (your charter, last duty; model S-032). Read only; write nothing. Your return is recorded verbatim in reviews/P-002-standard-lines/critic.md. The Chief of Staff wrote P-002's Build-1 to Build-5 and Launch-1 to Launch-5 lines before the Build gate, where the owner rules them; until then each needs your check. For each of the ten lines, quote it whole and say: whether it is in the right form; whether its why says in plain words why this project needs that standard milestone, for this project, not in general; and whether every fact in the why is true of the records in your manifest. Rate a finding blocking only if a why is false, missing, not about this project, or not plain. Flag any self-implication (D-050).
Return first a column-0 line `Verdict: PASS` or `Verdict: FAIL`, then a paragraph in plain words, then numbered findings each marked blocking or not, each with file, line and a fix, then the six-part contract.
