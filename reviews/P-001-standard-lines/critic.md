# The Critic on the reworded standard lines Build-1, Build-3 and Launch-5, verbatim

*Brief 49 (docs/briefs/49-critic.md); a fresh session on a different model from the lines' writer. Recorded verbatim by the Orchestrator, 2026-11-04.*

Verdict: PASS

Findings (none blocking). I had no shell, so I could not run `git diff`. I identified the three new lines (Build-1, Build-3, Launch-5, docs/PROJECT.md:60, :62, :76) from the finding text and the file as it stands now. I cannot show the old wording beside the new.

1. Build-1 (PROJECT.md:60), finding 1 resolved. Not blocking.
   - Line: "the plan's own locked checks, and the held-back checks written by a Check author who never sees the changes being tested, must exist before any run".
   - The object is now "the changes being tested", not "the work". That matches S-001 AC4 (line 253), which keeps from the Check author the spec, E-003 and the C?-*.md change files. It also matches S-001 line 201 ("Never: holds this spec, E-003, the change texts") and plan.md round 1 finding 1 (line 22).
   - "Before any run" holds. S-001 line 48 admits only pieces "dispatched after its kind's comparison opens", and AC4 requires the held-back check to exist when the comparison opens.
   - It is specific to this project, because only this test has held-back checks.
   - It is a little jargon-heavy for the owner ("locked checks", "held-back checks", "Check author"). The earlier review did not fail this, and I do not either.

2. Build-3 (PROJECT.md:62), finding 2 resolved. Not blocking.
   - Line: "the test's scripts run and record every comparison, and the brief-and-model record will change how every project's agents are started, so a reviewer must try to break both before either is trusted".
   - The "touches every project" claim is now tied to the record only, which was the fix asked for.
   - The scripts clause is true of PROJECT.md:89 (the Builder runs the test and holds the scripts in src/** and tests/**), and nothing live changes (:88).
   - The record clause is true of M3 (:65) and :90: the record lands in the operating model's own rules and tools and covers every session.
   - "Changes how agents are started" is a slight stretch, since the record changes what is written down when an agent starts, not how it starts. A purist would say "recorded". I accept it, because section 1 and the "Where it must work" paragraph speak of "both ways agents are started".
   - "Scripts" is plainer than the earlier "harness". Build-2 and Build-5 still say "harness", so the vocabulary is uneven. That is cosmetic.
   - Reading Build-3's reviewer as one reviewer for both is fine. M3 is reviewed under the operating model repository's own process (:90), and the scripts by the Reviewer here.

3. Launch-5 (PROJECT.md:76), finding 6 resolved. Not blocking.
   - Line: "this project keeps a log of every slip for the operating model to correct, so those lessons must be recorded at handover, before the project leaves the desk".
   - It now leads with the real reason instead of "the owner passes the Launch gate".
   - It is true of the records: M6 and the lessons log (:13, :69, :92), and OPERATING_MODEL §4 "Graduated" says "the lessons for the operating model are recorded at handover".
   - It is plain, uses the owner's word "slip", and is specific to this project.

4. Form. All three keep `- <Phase>-<n> (standard) · taken on · why: <reason>`. None has " · " inside the reason; they use only commas. This matches OPERATING_MODEL §3 "Why and context" and §4 "Standard milestones" (a why is changed, never removed; a why-only change needs only the Critic's check, so no owner ruling is needed). The other seven Build and Launch lines are as the previous review found them, since I have no diff to say otherwise. Their vocabulary, such as "harness" in Build-2 and Build-5, is unchanged.

5. No new error found. No new claim appears that the records do not hold. The Build-3 and Launch-5 reasons do not contradict M3, M4 or M6, or section 4.

The six-part contract
1. What I changed: nothing. I am read-only and wrote no file.
2. Why: the brief asked for a check of the reworded standard lines Build-1, Build-3 and Launch-5, against the gate Critic's findings 1, 2 and 6 and the records.
3. What I verified:
   - docs/PROJECT.md in full, sections 3, 4, 6 and 8 included.
   - OPERATING_MODEL.md §3 "Why and context" (line 120) and §4 "Standard milestones" with its table (lines 147-174).
   - S-001.md AC4 and AC5 (lines 253-254), the line 201 table row, and lines 48 and 319.
   - reviews/S-001/plan.md round 1 finding 1 (line 22).
   - reviews/P-001/_build-gate-1-critic.md "Standard lines", findings 1, 2 and 6.
   - The form of all three lines.
4. What is undone:
   - I could not run `git diff`, so I did not compare old and new text. I identified the changed lines from the findings.
   - I did not read experiments/E-003.md closely. Its matching lines were mostly over-long and omitted, and S-001 held the same facts.
   - I did not re-check the other seven Build and Launch lines or the Discovery and Design lines.
5. Needed outside my lane: nothing. The reasons need no owner ruling, since a why-only change needs only the Critic's check.
6. Open questions: optional wording for the Orchestrator, which I would not hold the verdict on. Build-3 could say "recorded" instead of "started". Build-2 and Build-5 could say "scripts" instead of "harness", to match.
