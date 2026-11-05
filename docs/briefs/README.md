# Briefs

One file per builder dispatch, `<task-id>.md`, written by the orchestrator when the task is sent,
using the coder brief format in OPERATING_MODEL §12. It's the record of what the agent was told.

Each record opens with these fields, one per line:
- `session:` the session that handed the task out;
- `model:` the model that runs the task, and the model of the work it checks or is checked by (D-056);
- `start:` the starting point, `<repository>@<full commit id>` for each repository the task starts from (its fixed copy, or the commit its branch is made from); for a plan or built piece entering the fair test, the piece's start commit (decisions/questions/P-001-build-gate-terms.md, term 9; specs/S-001.md, AC2). Records written before 2026-11-04's Build-gate ruling have no `start:` line;
- `recorded:` when the record was written: at hand-out, or after it and why.
