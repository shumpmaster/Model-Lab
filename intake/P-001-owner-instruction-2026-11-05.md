# Intake — P-001: the owner's instructions for Build-2, 2026-11-05

*Recorded by the Chief of Staff (session_01QBwHGNGKXFwvVVdzkei5aT) from the owner's opening message in that session. Only the lines on the fair test's checks and briefs are copied here; the rest of the message restates the handoff (docs/handoff/2026-11-04-chief-of-staff-9.md) and this project's working rules.*

## The owner's words, verbatim (2026-11-05)
"PR #53 records my answer to the checks' stop question, "A: one focused round (Recommended)". The round is done, and the Reviewer passed it by running every case."

"Build-2: brief the Builder for the harness scripts under src/E-003/, to the interfaces in tests/acceptance/e003_support.py. Tell it:
   - analyse.py is a deliverable the checks add: a mechanical reference, not the Reviewer's result.
   - Under the strict F4 reading, a /tmp path is clean only from the line that creates it."

"Every brief that records a pack manifest names the setting its check reads: S001_BLIND_MANIFEST for J8, S001_ANALYSIS_MANIFEST for J7. A wrong or empty setting skips with exit 0, so confirm each run checked the record rather than skipping it."

"Keep the open non-blocking points on the locked checks for a later superseding change; locked checks are not edited."

## What it bears on
- Brief 90 carries the two Build-2 points (docs/briefs/90-builder.md, items 2 and 3).
- The last line is the owner's instruction on the three minor points left open on the locked checks (reviews/51/reviewer.md, round 4; triage/P-001-S-001-checks-round-5.md, finding 2), and the owner's statement that locked checks are not edited.
