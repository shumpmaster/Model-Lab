Verdict: PASS

*The Critic's check of P-002's new standard lines Build-1 to Build-5 and Launch-1 to Launch-5 (docs/projects/P-002.md:131 to :135 and :142 to :146), brief 346 (docs/briefs/346-critic.md); a fresh session on a different model from the lines' writer, read from a fixed copy at Model-Lab 809bb44. Recorded verbatim by the orchestrator, 2026-11-22. The lines are kept as checked; the optional wording notes on Build-2, Build-4 and Launch-3 are not taken, so this record quotes them as they stand.*

## Round 1

All ten lines are in the required form, with no " · " inside any reason. Each why gives a project-specific reason that the records support. I found no blocking issues. I read the Build and Launch lines against docs/projects/P-002.md, specs/S-002.md, decisions/questions/P-001-work-repo.md, docs/LESSONS.md LL-73, and the model's table of standard milestones. Two checks I could not do from the model:
- I could not find the model's §3 and §4 text by name. I used the standard-milestone table at OPERATING_MODEL.md lines 166 to 176 instead.
- The Grep tool omitted some long lines, including S-002.md line 197 and the Part 2 and section 6 lines, so I did not read them in full.

`- Build-1 (standard) · taken on · why: the count and the draw decide which of the owner's pieces count and which side each trial piece falls on, so their checks must be written by the Check author from the frozen plan before the Builder writes either`
Non-blocking: none. It matches the table row "Tests written before the work". Section 4 and S-002 name the Check author as writing the locked checks before the count is built.

`- Build-2 (standard) · taken on · why: the count, the draw, the reading-brief check and the empty place for outside items must be built to the frozen plan before any piece is counted, any trial drawn or any outside item run`
Non-blocking: the four items match S-002 "Needed outside this spec's lane" (the Builder bullet). "The empty place" is mild shorthand for section 4's "place it runs, with no project data and no way to send any out". Consider "a sealed place".

`- Build-3 (standard) · taken on · why: a fault in the count or the draw would move the target's figure or a trial's sides without anyone seeing it, and outside code runs only in the empty place, so a reviewer must try to break each before it is trusted`
Non-blocking: none. Section 4 says the Reviewer tries to break the count and checks outside code, and that nothing from outside runs until the place is set. "Each" is slightly loose but clear in context.

`- Build-4 (standard) · taken on · why: every method the owner lets through to a trial must end with a recorded result and the owner's ruling on it, passed or not, before anything enters the operating model`
Non-blocking: "anything" is slightly broader than the records. M14's two proposals (on evidence and on adopting a method its trial did not pass) are not preceded by a trial result. The dependencies paragraph says only "each method ... after its results card". Suggest "before any method enters". Otherwise it matches M13, M14 and P-002-trial-gates.

`- Build-5 (standard) · taken on · why: the count, the touch log, the trial records, the feeds and the owner's two cards must work together on real pieces, not one at a time, before the screening is handed over`
Non-blocking: none. It is consistent with Design-5 (no screens of its own) and with the touch log and reading-round records in S-002.

`- Launch-1 (standard) · taken on · why: the screening only helps the owner while it runs, and it must run in the operating model itself, since Model-Lab is temporary and is archived once both projects are in`
Non-blocking: it overlaps M15's why, but the standard line is allowed to say so. The record P-001-work-repo.md line 1 says Model-Lab is archived "once both are in", which supports it.

`- Launch-2 (standard) · taken on · why: the count, the reading rounds and the trials need keepers among the operating model repository's own roles, named at the hand-over, to keep running after this project leaves the desk`
Non-blocking: none. It matches section 4's rows for M15 ("Named at the hand-over") and M14.

`- Launch-3 (standard) · taken on · why: the owner wants kept methods moved fully into the operating model, never by an automatic update, and the owner approves the launch on a complete handover package`
Non-blocking: its first half repeats M14's why, and its second half is the model's own definition of "handed over". It is true and plain, but the least project-specific of the ten. Consider naming this project's package contents.

`- Launch-4 (standard) · taken on · why: the target is checked 12 months after the first trial starts, likely after the hand-over, so the count, the status updates and each kept method's six-month review must be confirmed running before the project leaves the desk`
Non-blocking: none. S-002 AC20 and AC21 hold the status updates, the six-month review and the 12-month check, and say all of it runs from the operating model repository after the hand-over.

`- Launch-5 (standard) · taken on · why: this project has already had slips for the operating model to learn from, such as the miscounted record coding, so its lessons must be recorded at hand-over, before the project leaves the desk`
Non-blocking: none. LL-73 records a coding script built over varied records without a sample check, and M8's why says the same.

The sentence added at the end of line 106 names specs/S-002.md ("Areas touched" and "Needed outside this spec's lane"), section 4, section 6, P-002-trial-gates.md, P-001-work-repo.md and LL-73. All exist and support the lines. Section 6 was not read in full, so I could not confirm that it supports the lines. The sentence's form is consistent with the other entries. No finding.

Six-part contract:
- Changed: no files. I am read-only.
- Why: the brief asked for a check of the ten new standard lines and the line-106 sentence before they go to the owner at the Build gate (model S-032).
- Verified: I read P-002.md lines 60 to 169, S-002.md (Areas touched and Needed outside), P-001-work-repo.md, LESSONS.md LL-73, PROJECT.md lines 60 to 76 for comparison, and OPERATING_MODEL.md lines 166 to 176 for the milestone table. I also grepped the fixed copy for "six-month", "status update" and "archived". Every line was checked for form, for " · " inside the why, and for agreement with its records.
- Undone: I did not read the long lines Grep omitted, including the Part 2 and section 6 lines. I did not read reviews/P-001-standard-lines/critic.md or any docs/briefs or docs/reports file other than the brief.
- Needed outside its surface: the Orchestrator records this verbatim as reviews/P-002-standard-lines/critic.md. The Chief of Staff may take or leave the optional wording suggestions on Build-2, Build-4 and Launch-3.
- Open questions: none.
