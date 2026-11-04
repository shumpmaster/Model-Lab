# Held-back checks for S-001: what the Check author is given

*Frozen with spec S-001. This file, and the role files and playbook it names, are your task.
Files not listed in your pack are not yours to read.*

## Your task
Write one **held-back check** for each of three kinds of work, each by the date the Orchestrator
gives you for that kind:

| Kind | The piece that is judged | Its existing check, to write from |
|---|---|---|
| Plans | a spec draft at round 1, as submitted to its plan review | the plan-review role file, `.claude/agents/critic.md`, and the playbook `docs/playbooks/software.md` |
| Built work | a built stage's round-1 submission: the commit range it adds, in a copy of the repository | the build-review role file, `.claude/agents/reviewer.md`, as a general standard that holds for any stage; no particular spec is given to you, since the judge receives the stage's spec at judging time, as the task it was set |
| Research | a research memo's round-1 submission, with the sources it cites | the source-check role file, `.claude/agents/source-checker.md`; there is no research playbook |

Write each check from these files only, as they stand in your pack when you are dispatched. They
are the Model-Lab copies. Your pack cannot hold another repository's files, and no playbook other
than `docs/playbooks/software.md` exists, in Model-Lab or in the other projects whose work will be
judged. Write each check so it holds for work from any of the owner's projects. Where a test rests
on something these files give that another project might not, say so in that test.

## Your agent file and your brief
Your agent file (`.claude/agents/check-author.md`) describes your usual job: writing a frozen
spec's locked checks and committing them. For this task:
- its lines about reading the frozen spec and its join sheets do not apply. You are given no spec;
- its lines about your write lane, committing and handing off committed checks do not apply. You
  write nothing into any repository (see Rules).

If your brief names a spec, or tells you to read one, that line does not apply to this task either.

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
- **Where it goes.** Return each check's full text to the Orchestrator only, in your return. Never
  commit it, and never write it into any repository or into your pack folder. The Orchestrator
  places it in the held-back store, a place outside every repository whose location the owner rules.
- **Its fingerprint.** On receipt, the Orchestrator computes the SHA-256 of the check file's bytes,
  as placed in the held-back store, and records it with the set id. You do not compute it.
- Writing each check is one run of the budget.
- If you need anything not listed here to write a check, ask through the channel; read nothing
  outside your pack.

## Return
The six-part contract. Then, per kind: the set id; the role files and playbook (path and commit) you
wrote it from; its number of tests; and the check's full text, as one fenced block, for the
Orchestrator only.
