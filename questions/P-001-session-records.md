# Ruling needed: Should recording each brief and model for agents started from a conversation begin in this project only, or across the model now?

Milestone: Discovery-3
Asked in session: session_01QBwHGJH9m3A4Ray7WpHzBo

WHY: When the automatic pipeline starts an agent, it records exactly what the agent was told and which model ran it. When an agent is started from a conversation like this one, which is how much of Service-Desk's later work ran (how much is not yet known), neither is recorded. You have already said briefs should be recorded against how the work went; this asks where that starts. It adds some work per dispatch for the Chief of Staff (not yet measured), and a model-wide rule goes through the model's own process.
OPTIONS:
  A. Across the model now — a model rule change, so every project's conversation-started agents keep the record. Cost: the model's process (a spec, a review, your ruling) before it applies anywhere.
  B. This project first — record them here as the project's own test data; decide the model-wide rule from the results. Cost: other projects keep no such record meanwhile.
RECOMMENDATION: B — it gives this project the data it needs now, and the model-wide rule is then decided on evidence.
RISK CLASS: R1   REVERSIBILITY: reversible   BLAST RADIUS: the Chief of Staff's dispatches in this project (A: all projects)
DEFAULT: B   TIMEOUT: 168

## Context
- Proposal put to the owner: "Record each agent brief and role card against how its work went (review rounds, fails, rework), find which prompts work, and improve the weak ones. Ongoing." The owner: "I think that should probably be in there too." (source: portfolio ideas/IDEAS.md, 2026-11-01)
- Script-started sessions record the brief text, the agent file's hash and the model (source: research/Q-001-memo.md, C1, confirmed in research/Q-001-source-check.md)
- Service-Desk's brief folder holds only its README, and the Chief of Staff's session file records no brief or model (source: research/Q-001-memo.md, C2)
- The Chief of Staff's own account (2026-10-30): briefs are written by hand for each dispatch and nothing records which led to clean first passes (source: portfolio ideas/IDEAS.md, "Evidence from the Service Desk's launch")
