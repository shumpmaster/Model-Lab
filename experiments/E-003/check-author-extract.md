# What the Check author is given for the fair test (S-001, E-003)

*An extract of spec S-001 and registration E-003, written for the Check author and frozen with them.
It is all the Check author is given of either. It leaves out, on purpose, everything about what the
test changes: S-001's design and criteria, E-003's hypothesis and method, and the files
experiments/E-003/C*.md are withheld from the Check author (S-001, AC4; join sheet J8). Nothing below
says what the test varies.*

## Your task
Write one **held-back check** for each of three kinds of work, before that kind's comparison opens:

| Kind | The piece that is judged | Its existing check, to write from |
|---|---|---|
| Plans | a spec draft at round 1, as submitted to its plan review | the project's plan-review role file (`.claude/agents/critic.md` in Model-Lab and the Service Desk) and the playbook for the spec's work type |
| Built work | a built stage's round-1 submission: the commit range it adds, in a copy of the repository | the project's build-review role file (`.claude/agents/reviewer.md`) and the frozen spec the stage builds |
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
- The judge answers in this form (S-001, join sheet J5): first line `Verdict: PASS` or
  `Verdict: FAIL`; then the numbered tests that failed, each with the file and line it rests on.
  A piece passes when no test fails.

## Rules
- Write each check before its kind opens. Once its fingerprint is recorded, it is never edited while
  its kind's comparison runs; it is used for that kind only (E-003, Holdout use).
- Store it outside every repository, as governance/HOLDOUTS.md says; record only its set id and
  fingerprint there. No copy of it may be committed anywhere.
- Writing each check is one run of the test's budget.
- If you need anything not listed here to write a check, ask through the channel; do not read
  specs/S-001.md, experiments/E-003.md or experiments/E-003/C*.md.

## Return
The six-part contract, with, per kind: the set id, its fingerprint, the role files and playbooks
(path and commit) you wrote it from, and its number of tests. Not its text.
