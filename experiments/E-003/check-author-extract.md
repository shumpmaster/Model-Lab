# Held-back checks for S-001: what the Check author is given

*Frozen with spec S-001. This file, and the role files and playbook it names, are your task.
They are in your pack folder, which is your working directory. Files not in your pack folder are
not yours to read.*

## Your task
Write one **held-back check** for the one kind of work your brief names:

| Kind | The piece that is judged | Its existing check, to write from |
|---|---|---|
| Plans | a spec draft at round 1, as submitted to its plan review | the plan-review role file, `.claude/agents/critic.md`, and the playbook `docs/playbooks/software.md` |
| Built work | a built stage's round-1 submission: the commit range it adds, in a copy of the repository | the build-review role file, `.claude/agents/reviewer.md`, as a general standard that holds for any stage; no particular spec is given to you, since the judge receives the stage's spec at judging time, as the task it was set |
| Research | a research memo's round-1 submission, with the sources it cites | the source-check role file, `.claude/agents/source-checker.md`; there is no research playbook |

Write the check from these files only, as they stand in your pack folder. They are the Model-Lab
copies. Your pack cannot hold another repository's files, and no playbook other than
`docs/playbooks/software.md` exists, in Model-Lab or in the other projects whose work will be
judged. Write the check so it holds for work from any of the owner's projects. Where a test rests
on something these files give that another project might not, say so in that test.

## Your agent file and your brief
Your agent file (`.claude/agents/check-author.md`, in your pack folder) describes your usual job:
writing a frozen spec's locked checks and committing them. For this task:
- its lines about reading the frozen spec and its join sheets do not apply. You are given no spec;
- its lines about your write lane, committing and handing off committed checks do not apply. You
  write no file and commit nothing (see Rules).

If your brief names a spec, or tells you to read one, that line does not apply to this task either.

## What a held-back check is
- A short list of pass/fail tests, numbered from 1. Each names one fault that, if present, sends
  the piece back, and says how a judge decides whether the piece has it, from the piece and the
  files it cites.
- It judges the piece alone. The judge sees only the piece and the files it cites, never how or by
  whom it was made.
- It is written for a judge on a different AI model from the workers, who has not seen the project
  before. Each test must be decidable from the piece and what it cites, with no other context.
- For research: the judge opens the memo's sources itself.
- For built work: the judge is also given the spec the stage builds, as its task statement. Write the
  check so it judges the piece against whatever spec it is given; name no particular spec.
- The judge answers in this form: first line `Verdict: PASS` or `Verdict: FAIL`; then the numbers of
  the tests that failed, each with the file and line it rests on. A piece passes when no test fails.
  Only the test numbers and the cited lines are kept with the verdict, so each test must be
  understood by its number and the check's text, which the judge and the owner can read.

## Rules
- **Where you work.** Read only the files in your pack folder. Do not read, search or run commands
  on any path outside it, do not use the web, and do not fetch from any repository. The session you
  run in checks your transcript for this, and a read outside your pack folder voids the check.
- **Where it goes.** Return the check's full text to the agent that started you, in your return,
  and nowhere else. Write no file, commit nothing, and do not write it into any repository. That
  agent places it in the private store for these checks and computes its fingerprint (the SHA-256
  of the file's bytes); you do not compute it.
- Once its fingerprint is recorded, the check is never edited while it is in use; it is used for
  its own kind only.
- Writing the check is one run of the budget.
- If you need anything not listed here to write the check, say so in your return and stop; read
  nothing outside your pack folder.

## Return
The six-part contract. Then: the set id your brief gives; the role files and playbook (path, and
the SHA-256 your brief lists for each) you wrote it from; its number of tests; and the check's full
text, as one fenced block, for the agent that started you only.
