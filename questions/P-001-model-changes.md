# Ruling needed: When the AI model behind an agent changes, should its instructions be expected to keep working?

Milestone: Discovery-3
Asked in session: session_01QBwHGJH9m3A4Ray7WpHzBo

WHY: Published research reports that instructions tuned for one model can do worse on another. New models arrive every few months. This decides whether the project keeps a fixed set of test tasks to re-check instructions whenever a model changes, which costs runs each time.
OPTIONS:
  A. Yes, check on every model change — keep a small fixed set of past tasks and re-run them when a role's model changes; costs some runs per change.
  B. Re-tune when needed — no standing check; fix instructions if problems show up after a change.
  C. Decide later — the research on this question comes back first.
RECOMMENDATION: C — the research shortlist already asks how well instructions carry across models; its answer sets whether A is worth the runs.
RISK CLASS: R1   REVERSIBILITY: reversible   BLAST RADIUS: this project's scope only
DEFAULT: C   TIMEOUT: 168

## Context
- Prompts tuned for one model reported to do worse on another; not yet confirmed from the source (source: research/Q-001-memo.md, F1, marked assumed)
- Every checker must run on a different model from what it checks, so one role's model change can affect others (source: Personal-Org-Operating-Model OPERATING_MODEL.md §5, "Model diversity")
