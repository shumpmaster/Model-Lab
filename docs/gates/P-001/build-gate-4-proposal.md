# P-001 — the Build gate: what a user would see

**Shown to the user representative, a simulation of the target user, not real users.**

## 1. What it is

A fair test of candidate changes to what the operating model's agents are given to work from: their role files, each task's brief, and what each is given to read [docs/PROJECT.md:13].
Each change is kept only if it raises the share of work passing its check first time by so much that chance alone would give it at most 1 time in 40 [docs/PROJECT.md:108].

## 2. What it does for you

More plans, research and built work pass their checks first time, where a change is shown to help [docs/PROJECT.md:109].
If no change helps, no instruction changes; the record of each agent's brief and AI model still goes into the operating model [docs/PROJECT.md:112].

## 3. How you would use it

> AC1 [trace: V1 → AC1] — When the owner opens experiments/E-003/ at the Build gate, they find each of C1, C2 and C3 as the exact text the harness will insert, with its kind, the cause it aims at, how it is applied and its removal test; and every brief and role file in every repository is as it was, since the changes exist only as these texts. [specs/S-001.md:250]
> AC2 [trace: V1 → AC2] — When a new piece of the kind under test is dispatched in a participating project with its record made at dispatch (for plans and built work the worker's brief, start commit and model; for research the memo's submission and the source check's brief, start commit and model), then the harness runs both arms from that start commit in fresh copies, with briefs that differ only by the change paragraph, on the same served model, starting within the same hour and within 7 days of the dispatch, and records the pair; and when a piece has no such record, it does not enter and is listed. [specs/S-001.md:251]
> AC3 [trace: V1 → AC3] — When a piece's named inputs change between its start commit and its real round-1 submission, or an arm leaks, or the arms' starting contexts differ beyond the change text, then the pair is not judged as it stands: it is left out or rerun as E-003 says, listed with its reason, and never run again for a better answer. [specs/S-001.md:252]
> AC4 [trace: V1 → AC4] — When a kind's comparison opens, its held-back check already exists, written by a blind Check author that ran as a helper of a sheet session the owner started with the sheets repository only, from a pack folder matching the manifest recorded from the per-task pack `S-001-holdout` (experiments/E-003/check-author-extract.md and the standards it names, and not this spec, E-003, any experiments/E-003/C?-*.md file or S-001's locked checks), and whose transcript shows no read, search or command outside that folder and no web or network use (unless K4 showed transcripts cannot be read and the owner ruled to go on, which the record states); that session is not the one that wrote S-001's locked checks, and the session that wrote them never held a held-back check; the check is in the sheets repository with its fingerprint recorded in governance/HOLDOUTS.md, and no session that does or starts the work, and no arm's copy, brief or export, has held it. [specs/S-001.md:253]
> AC5 [trace: V1 → AC5] — When a plan or built arm finishes, its deliverable's neutral export is judged in its own judge session, and when both research checks have returned, the memo's export is judged once in its own session; each judge is a helper of the kind's judging session, which holds the sheets repository and no work repository; every judge runs on a model other than the doers', without the arm's label, hand-back, commit messages or the check versions' verdicts, and gets its sheet only after the sheet's SHA-256 matches the recorded fingerprint; for built work the stage's locked checks also run by script; a judge with no verdict line gets the one fixed follow-up and at most one new session, and a judge whose transcript shows a read outside its copy, or the web beyond the memo's sources, leaves its pair out; each pair left out is listed. [specs/S-001.md:254]
> AC6 [trace: V1 → AC6] — When every pair of a kind is judged, the owner receives 8 cards, each one output without arm labels, showing the judge's verdict with the numbers of the failed tests and their cited lines, drawn by the pre-written seed from the three groups E-003 names, each answerable in about five minutes; more are drawn, up to 12, until 6 have a yes or no; the owner's answers replace the judge's verdicts, the pairs are scored again, and the cards answered and the disagreements are recorded. [specs/S-001.md:255]
> AC7 [trace: V1 → AC7] — When the Reviewer analyses a kind, a change is kept only if the judge is confirmed (6 or more cards answered, at most 2 disagreements) and the exact one-sided test on the differing pairs clears 1 in 40 (for C3, also the false-pass guard); otherwise the record says "not shown", with the gain and its 95% range, and "no change helps" stands as an accepted result. [specs/S-001.md:256]
> AC8 [trace: V1 → AC8] — When the test is running, the owner receives, at every 20 runs of each side and 16 weeks after each kind opens, the runs and tokens used on each side, the pairs collected and left out, the power at the pairs collected and the weeks to the target at the pace so far, and no outcome; the owner's "go on" or "stop" is recorded; no side of a kind starts more runs than its planned runs plus its share of the reserve, so no kind starts more than its planned runs plus reserve. [specs/S-001.md:257]
> AC9 [trace: V1 → AC9] — When the served model of the doers or the judge changes during a kind's comparison, pairs are grouped by model, the deciding test is run on the larger group only, and the result says so. [specs/S-001.md:258]
> AC10 [trace: V2 → AC10] — When a change is kept, its result record gives the V2 measure for its kind (first-time pass rate over the first 30 pieces checked under the changed operating model, against the starting figure, at 1 in 25), how those pieces are counted from the review records, and its removal test, so the operating model can carry, monitor and remove it after M5 without Model-Lab. [specs/S-001.md:259]
> AC11 [trace: V2 → AC11] — When a kept change is removed, by its removal test or at the operating model's scheduled review, the brief or role file returns byte for byte to its text without the change. [specs/S-001.md:260]

## 4. What it looks like

No screens: the fair test has no screens or views; the owner sees records and short cards.

## 5. What it asks of you

AI usage within your existing plan, with nothing paid beyond it unless you say so at the time [docs/PROJECT.md:99].
Your time, with no cap set on it; each status update reports the tokens the helpers used [docs/PROJECT.md:116].
