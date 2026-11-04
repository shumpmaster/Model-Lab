# Held-back checks for S-001: what the Check author is given

*Frozen with spec S-001. This file, and the role files and playbooks it names, are your task.
Files not listed in your pack are not yours to read.*

## Your task
Write one **held-back check** for each of three kinds of work, each by the date the Orchestrator
gives you for that kind:

| Kind | The piece that is judged | Its existing check, to write from |
|---|---|---|
| Plans | a spec draft at round 1, as submitted to its plan review | the project's plan-review role file (`.claude/agents/critic.md` in Model-Lab and the Service Desk) and the playbook for the spec's work type |
| Built work | a built stage's round-1 submission: the commit range it adds, in a copy of the repository | the project's build-review role file (`.claude/agents/reviewer.md`), as a general standard that holds for any stage; no particular spec is given to you, since the judge receives the stage's spec at judging time, as the task it was set |
| Research | a research memo's round-1 submission, with the sources it cites | the project's source-check role file (`.claude/agents/source-checker.md`) and the research playbook |

Use the role files and playbooks as they stand when you are dispatched, in each participating
project; where two projects' standards differ, write the check so it holds for both, and say where.

## What a held-back check is
- A short list of pass/fail tests, numbered. Each names one fault that, if present, sends the piece
  back, and says how a judge decides whether the piece has it, from the piece and the files it cites.
- It judges the piece alone. The judge sees only the piece and the files it cites, never how or by
  whom it was made.
- It is written for a judge on a different AI model from the workers, who has not seen the project
  before. Each test must be decidable from the piece and what it cites, with no other context.
- For research: the judge opens the memo's sources itself.
- For built work: the judge is also given the spec the stage builds, as its task statement. Write the
  check so it judges the piece against whatever spec it is given; name no particular spec.
- The judge answers in this form: first line `Verdict: PASS` or
  `Verdict: FAIL`; then the numbered tests that failed, each with the file and line it rests on.
  A piece passes when no test fails.

## Rules
- Once its fingerprint is recorded, a check is never edited while it is in use; it is used for its
  own kind only.
- Store it outside every repository, as governance/HOLDOUTS.md says. Return its set id and
  fingerprint; the Orchestrator records them there. No copy of it may be committed anywhere.
- Writing each check is one run of the budget.
- If you need anything not listed here to write a check, ask through the channel; read nothing
  outside your pack.

## Return
The six-part contract, with, per kind: the set id, its fingerprint, the role files and playbooks
(path and commit) you wrote it from, and its number of tests. Not its text.
