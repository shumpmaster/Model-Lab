# Ruling needed: How much may this project spend on testing instruction changes?

Milestone: Discovery-3
Asked in session: session_01QBwHGJH9m3A4Ray7WpHzBo

WHY: Telling a real improvement from chance needs several runs of the same task, and each agent run costs usage. One reviewer run in Service-Desk used between about 57,000 and 214,000 tokens. Without a limit, the research cannot size its tests; the model leaves the research cost limit open.
OPTIONS:
  A. A run count — up to about 100 agent runs for testing during Discovery and Design, then reset at the Build gate with the evidence.
  B. A money limit — a monthly figure you name, checked against your plan's usage.
  C. No extra spend — use only records that already exist (past reviews and sessions), with no new test runs, until the Design gate.
RECOMMENDATION: A — runs are what you can see on your plan's usage, and 100 is enough to learn whether testing is feasible without committing to more.
RISK CLASS: R3   REVERSIBILITY: irreversible (spending)   BLAST RADIUS: this project's agent usage only
DEFAULT: none (spending never defaults)   TIMEOUT: none

## Context
- Reviewer helper runs ranged from 56,509 to 213,771 tokens; most helper lines hold null usage figures (source: research/Q-001-memo.md, G1)
- The research sub-project cost limit is open in the rulebook (source: Personal-Org-Operating-Model OPERATING_MODEL.md §2, "Delegation grants")
- The owner ranked lower agent usage outside this project's goals: "a combination of all but lower agent usage and less of my time" (source: portfolio ideas/IDEAS.md, 2026-11-01)
