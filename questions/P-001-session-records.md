# Ruling needed: Should work done by agents inside a conversation keep the same record as the automatic pipeline?

Milestone: Discovery-3
Asked in session: session_01QBwHGJH9m3A4Ray7WpHzBo

WHY: When the automatic pipeline starts an agent, it records exactly what the agent was told and which model ran it. When an agent is started from a conversation like this one, which is how most of Service-Desk's later work ran, neither is recorded. Without that record nobody can tell later which instructions led to clean first passes. Recording it adds a few minutes per dispatch for the Chief of Staff and, as a rule change, goes through the model's process.
OPTIONS:
  A. Yes, from now on — every brief and the model are recorded for conversation-started agents too, starting in this project; a model rule change follows.
  B. Only inside this project — record them here as the project's own test data; decide the model-wide rule from the results.
  C. No — keep conversation work light; measure only the automatic pipeline.
RECOMMENDATION: B — it gives this project the data it needs now, and the model-wide rule is then decided on evidence.
RISK CLASS: R1   REVERSIBILITY: reversible   BLAST RADIUS: the Chief of Staff's dispatches in this project (A: all projects)
DEFAULT: B   TIMEOUT: 168

## Context
- Script-started sessions record the brief text, the agent file's hash and the model (source: Service-Desk reviews/Q-001/_control/0-62b8dda7dcf2.json, cited at research/Q-001-memo.md C1)
- Service-Desk's brief folder holds only its README, and the Chief of Staff's session file records no brief or model (source: research/Q-001-memo.md, C2)
- The owner's earlier account: briefs are written by hand per dispatch and nothing records which led to clean first passes (source: portfolio ideas/IDEAS.md, 2026-11-01 evidence list)
