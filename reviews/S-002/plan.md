Verdict: PASS

The Critic's plan review of specs/S-002.md and experiments/E-004.md (P-002, M8 to M10), in a fresh session on a different model from the writer, the Definer. Round 1 (brief: docs/briefs/271-critic.md, at Model-Lab 51bc87c, read from a fixed copy): FAIL, eight blocking findings. Recorded verbatim by the orchestrator, session session_01QBwHGNPKhVy6fgoUjKtW6q, 2026-11-12. Correction to the brief: it said a FAIL stops work before another round; the stop rule's limit for plan rounds is three (docs/LESSONS.md LL-55; reviews/S-001/plan.md, FAIL at rounds 1 and 2 and PASS at round 3), so round 1's findings go back to the Definer, and round 2 counts as the second of three. Round 2 (brief: docs/briefs/273-critic.md, at Model-Lab 1316988, after the Definer's change on brief 272, commit 015ba8f): FAIL, two blocking findings; the Critic flags its own round 1 for missing findings 3 and 4 and part of 6 (D-050). Round 3 (brief: docs/briefs/275-critic.md, at Model-Lab 23d27c1, after the Definer's change on brief 274, commit 749c3c9): PASS, nine non-blocking findings; the Critic flags rounds 1 and 2 for missing its findings 3 to 5 (D-050). Re-check after round 3 (brief: docs/briefs/277-critic.md, at Model-Lab 05a71c3 plus a session-lines commit, after the Definer's change on brief 276, commit f833d70): FAIL, two blocking findings, both in that change's new rule for an entry and its pull requests; the plan stands as round 3 passed it until the owner rules under the stop rule (as reviews/S-001/plan.md, round 4). The header verdict stays round 3's PASS for the plan as it stood at round 3. The owner chose option A, a focused fix (intake/P-002-owner-plan-stop-answer-2026-11-12.md); the focused confirmation review (brief: docs/briefs/281-critic.md, at the Definer's commit 4a03208 on brief 280): PASS, three non-blocking findings. The header verdict is PASS for the plan as it now stands. The orchestrator confirmed with `git diff 4bfc6e0 4a03208 -- specs/S-002.md` that the change has no hunk in S-002 lines 18 to 54 or 76 to 95, which the Critic could not diff. Re-run on the lines changed by briefs 321 to 335, before the freeze (brief: docs/briefs/336-critic.md, at Model-Lab bcac71f, with the files as at 7bdf340 and the diff given as a fixed copy): FAIL, one blocking finding, in brief 335's new dispatch clause as it bears on trial pieces; the header verdict stays the focused confirmation review's PASS for the plan as it stood then. The orchestrator confirmed with `git diff -U0 7bdf340 8f0ca72` and `git diff -U0 8f0ca72 f95d0f7` on specs/S-002.md that lines 82 and 114 changed before memo 5's commit and only lines 46 and 112 of the hand check's section after it. The owner chose option A at the second plan stop, "A: focused fix (Recommended)" (questions/P-002-plan-stop-2.md; saved on receipt in intake/P-002-owner-answers-2026-11-13.md); the focused confirmation review at the second plan stop (brief: docs/briefs/338-critic.md, at Model-Lab 50de6a7, after the Definer's change on brief 337, commit da1fce4): PASS, six non-blocking findings. The header verdict is PASS for the plan as it now stands. Check of the lines changed since then by briefs 341 and 342 (brief: docs/briefs/343-critic.md, at Model-Lab 87b7a9e, with the files as at 50de6a7 and the diff given as a fixed copy): PASS, three non-blocking findings. The orchestrator confirmed the Critic's finding 3 with `git show 9c9a855:questions/P-002-plan-stop-2.md` and `git show d231a51:questions/P-002-plan-written-by-piece.md` (each holds option A in the quoted words), and by a word diff of S-002 lines 110 and 112 against 50de6a7 that those two lines changed only by additions, in the passages briefs 341 and 342 name. The header verdict is PASS for the plan as it now stands.

## Round 1
Verdict: FAIL

Brief 271, plan review round 1 of S-002 and E-004, read only from /home/user/ml-fixed-271 and the two cards in /home/user/ml-cards/. I wrote nothing. This is my first check of these documents, so no finding implicates an earlier check of mine (D-050).

What holds, so the fix list stays narrow:
- S-002's header `milestones: M8, M9, M10` matches P-002.md section 3, lines 126 to 128.
- The quoted terms T1, T2, T23, T25, T27 and P1, P6, P7, P8, P12, P14 and P19 match trial-terms.md and P-002.md section 6. T16 is quoted with its ellipsis intact. The "reopening" and "kind of work" quotes match section 8.
- Every figure in E-004 lines 123 to 125 and S-002 line 87 matches line-output.txt:
  - (a) at 0.097, with its range 0.09616 to 0.09725.
  - (b) at 0.093, with its range 0.09227 to 0.09359.
  - The nine-share rows for passing a method that does nothing, for passing a true halving, and for taking the second look.
  - The worst case 0.1063 at 0.368 and 0.632.
  - The bands 0.307 to 0.429 and 0.571 to 0.693.
  - The gaps 0.0131 at 0.5734 and 0.0367 at 0.5482, and the nine-share gaps 0.0124 and 0.0314.
- The owner's words "A: line of 0.097" and the date 2026-11-11 match decisions/questions/P-002-two-look-line.md.
- line.py's second-look and pass logic matches E-004 Step 5. The test is one-sided Fisher at p ≤ line. The second look needs x<y. Look 2 is judged on all 60 each way at the same line.
- The Q-017 citations check: the 434 and 73 plain commits and local merges, 175/50/38 flagged, 124/150/55 by kind, the §5 list (memo lines 296 to 304), and "no Revert" (memo line 226).
- The "Facts relied on" line numbers I could open are right. I could not open reviews/P-002-value-target-odds/ or research/Q-013-memo.md, which are outside the manifest.
- E-004 is not a re-run. It is a new general registration and no earlier experiment in experiments/ matches it. S-002 has `lineage: []`.

## Findings

1. BLOCKING. S-002:16-45, 49, 66 (rule ids). The rules reuse ids that the ruled terms already hold, so a reader cannot tell which is meant.
   - Rules T1 to T7 (touch rules) collide with ruled terms T1 to T7. T1 is the term "piece", T3 the measure, T5 the 12-month check.
   - Rules P1 and P2 (a piece is a merged PR) collide with ruled P1 (judged 30 days after the last piece) and P2.
   - The same sentence mixes the two senses. E-P2 says "(T3)" meaning the send-back rule. Line 42 says "(T2's words)" meaning the term. Lines 49 and 66 cite "P14", "T25" and "T29" as terms.
   - The Researcher gets these rules verbatim (step 4). Results "under each rule" and J1's `rule: T1a|T1b|T1c|T2|T3` would then be ambiguous.
   - Fix: give the counting rules their own prefix (for example `RP1`, `RT1` to `RT7`, `RR1`) and write ruled terms only as "ruled T25". Apply it in J1, J9 and the ACs.

2. BLOCKING. S-002:37, 71 (fields) and 38-41 (touch window and rules). The fixed field list cannot support the rules, so the hand check cannot apply them from a no-text extract.
   - The touch window starts at "the time its brief is recorded". No field holds a brief's record time or the time of a question file. Decision-record answer times are given only relative to the PR's open and merge times, not to dispatch.
   - C1 (line 48) needs the first-round verdict of the Critic, Reviewer or Source checker record under reviews/ or research/. The only review field is GitHub PR review state, so step 4's "first check" result cannot be computed.
   - T3's "closed unmerged, whose work later merges" needs closed-unmerged PRs sharing a branch or brief. The extract holds only the sampled merged PRs.
   - Step 3 leaves "found by the Orchestrator by pattern" (decision records naming the PR or brief) and "intake items of owner instructions or answers" undefined. No rule uses the intake field.
   - Fix: add fields for dispatch time, question-file time, first-round review verdict and round count, and closed-unmerged PRs by branch and brief. State the patterns exactly. Drop unused fields. Say what is recorded as "untested" if GitHub's records cannot be read for a repository, which is already an acknowledged risk.

3. BLOCKING. S-002:31 (K2). Kind by "role dispatched" cannot be decided without free text for the largest group of briefs.
   - Chief of Staff and Orchestrator briefs go to plans only "for a plan, brief, spec, gate case or project document". That depends on what the brief says. The extract holds only the role and whether the record exists.
   - Orchestrator and Chief of Staff commits are the bulk of the record (memo §2: 1,100 and 484 in Service-Desk).
   - Fix: map by role and path only, and send an Orchestrator or Chief of Staff brief to K3 (most changed lines). Or add a coded brief-type field.

4. BLOCKING. S-002:70 and 129 (AC6), and the case list at lines 23-24 and 45-52. The edge-case sample is not fixed before the extract exists, and some cases cannot be sampled.
   - "Each filter recorded in the README" lets the Orchestrator choose the filters after the fact. The brief requires the sample, draw and fields to be fixed beforehand.
   - E-P1 (no pull request at all) and E-P2 (closed unmerged) can never match "pull requests merged from 2026-10-01", so they are "not seen" by construction.
   - E-T4 (a question naming only a milestone), E-T5 (an owner comment that is only thanks) and E-R3 (a fix that names nothing) have no possible no-text filter.
   - Fix: write each case's filter into S-002. Give E-P1 and E-P2 their own sampling frames (plain commits outside PRs, closed PRs). Mark the cases a no-text extract cannot filter as "checked by the Critic from the records, not sampled".

5. BLOCKING. S-002:42 (T5) against 45 (E-T4). Touch rules T5 and E-T4 contradict each other.
   - T5 counts a gate or value-target ruling as a touch "on the piece it rules". A gate ruling names a project or milestone, which E-T4 says is not a touch.
   - The rule has no J1 code (touches list T1a to T3 only), and it is also an open owner question.
   - Fix: say which pieces a gate ruling lands on and by what field. Or state that T5 is outside the count until the owner rules it, and keep it out of J1 and the hand check.

6. BLOCKING. experiments/E-004.md:66 (draw). The draw can be ground by the people who run the trial. The side is the first 8 bytes of SHA-256 of `<trial id>:<entry number>:<entry commit id>`. The entry commit id is a hash the dispatching session creates, and re-committing or amending changes it. That is a choice left open after the trial starts, and T29 already says the Chief of Staff knows the arms.
   - Fix: fix the shuffle in the frozen trial record. Pre-register a seed, or derive it from the entry number alone, so the side is known before any entry commit exists. Have the Reviewer re-derive every draw.

7. BLOCKING. experiments/E-004.md:114 (Withdrawn) and 72 (judging time). Withdrawal and pieces that never merge are left to discretion.
   - A drawn piece is dropped "because its work was no longer needed". No one is named to decide, there is no cap, and no time limit applies. The condition "no owner touch" favours dropping a piece before it needs one.
   - A drawn piece that stays open stalls the look, since judging waits on "the last of its 60 pieces".
   - Line 118 completes incomplete records "from the touch log" at judging time, which allows retrospective additions by the Chief of Staff.
   - Fix: name the decider (the Reviewer, or the owner) and cap withdrawals. Set a rule for a piece unmerged after N days. Say that touch-log lines count only if time-stamped when written and before the look is judged.

8. BLOCKING. E-004:15, 65 and S-002:148 (J2) against governance/SURFACES.md:66-67, 77-92. The Chief of Staff is to record each entry and draw in `src/E-004/records/trials/<trial id>/log.jsonl`, and the count is `src/E-004/records/count.jsonl`. `src/**` belongs to the builder. The Chief of Staff has no write lane there, and the spec lists no other writer. "Entry committed before the draw" cannot be done as written.
   - Fix: put the logs where a named writer owns the lane (a Chief of Staff or Orchestrator path), or name the script and session that commits them. Add the trial log to "Needed outside this spec's lane".

9. Not blocking. S-002:10. The plain-words section is not true of the body, and it is not plain in two places.
   - It says "a sample of 60 past pieces, 20 from each repository". The body samples merged PRs, pieces or not (line 70), plus up to 2 per awkward case.
   - "Line" and "starting share" are never explained to the owner.
   - "Up to about 1 in 100 less often" comes from the nine shares only. The script computes the halving-pass gap at no other shares, while the second-look gap is swept over the whole 0.0001 grid. Say "at the nine shares computed".
   - Fix: reword, and say plainly that the line is how sure a trial must be.

10. Not blocking. E-004, "what it cannot catch". The registration form has no such section, and E-004 does not give one. A5 and A6, the "not shown" note and the odds' independence assumption are scattered. The cards' limits (the hold-up guard is coarse, trials are not blind, only large effects show) sit only in the cards and S-002's risks.
    - Fix: add a short "What this trial cannot catch" under Deciding threshold that names those limits and cites the cards.

11. Not blocking. E-004, D-047. Nothing says that a method and kind already judged cannot be entered again on the same plan. A repeat entry would be a re-run.
    - Fix: add one line to Step 1 saying that a method already judged on a kind needs a genuinely different design, which the Critic checks before the entry card goes out.

12. Not blocking. E-004:15 and 41 against 43. "The Definer ... sets its frozen line" reads as a choice, though line 43 says the line is copied. Reword to "copies the line 0.097 into the trial record".

13. Not blocking. S-002:68 and 72. Name exactly which lines the research question holds as "the rules verbatim" (the rules and edge cases only, without the commentary about Q-017 counts), fixed at the frozen commit, so D-055 neutrality holds.
    - Also say what happens when a repository has fewer than 10 PRs in a sampling stratum.
    - Also say how K1 reads the memo's label-based rules 1 to 3, which the README defines.
    - R1(a)'s "revert record" is undefined. The `Reopens:` mark cannot exist for past pieces (the table says "Not shown"), so the hand check will test reopening by reverts and candidates only.

14. Not blocking. E-004:81. Short reads are "unlabelled" but the marker is removed only where it appears in the brief. If it appears in merged files, the reader can see it. Say so as a known leak, or strip it from the shown files.

15. Not blocking. S-002:122 and 143 to 144. AC8's "fill over the same weeks" has no pass line. Give a number: for example, the two sides differ by no more than 5 pieces at any time.

16. Not blocking. S-002:121. The heading "(scenarios; owner-approved)" is untrue until the owner rules the scenario card.

## The known leftovers, rated
- S-002:205, the line script's independent run still listed as needed. Not blocking. It passed at round 3 (reviews/P-002-two-look-line/reviewer.md). Remove it or mark it done.
- S-002:10, "before it freezes". Not blocking. Use the past tense.
- "E-004 line 3's draft for the Critic's plan review". The words are on E-004:5 (`revision: 1 (draft for the Critic's plan review)`), not line 3, so correct the pointer. Line 3 is "Frozen once the line below is set". Not blocking. Both must be settled when the file freezes.
- line.py's A7 not naming the 0.0001 second-look sweep. Not blocking. The script does the sweep at lines 216 to 237 and the output records it.

## Join-up review (docs/design/JOIN_UP_REVIEW.md form; Design, 2026-11-12)
Screens checked: none. This project item has no screens or views of its own (P-002.md Design-5). The only displays are the Service Desk's queue and missed-round views, which S-002 files there as new work. Nothing was checked side by side, so the screen rows read "no screens" and there are no needed changes to the records.

Hand-offs checked side by side instead: J1 to J9 against the rules, E-004 and the surfaces.
- Not blocking. J1 and J9 have no code for rule T5 or T7 touches (finding 5).
- Blocking, same as finding 8. J1 and J2 log paths sit in `src/**`, where the Chief of Staff and Orchestrator cannot write.
- Not blocking. J3 matches E-004 Step 3's four parts: on, off, leak check, removal.
- Not blocking. J4's `reviews/E-004/<trial id>/reviewer.md` is the Orchestrator's lane.

Result: the join-up review is not clear while findings 5 and 8 stand. I carry the non-blocking differences into the gate case as risks.

## Six-part contract
- **Changed:** nothing. I wrote no file.
- **Why:** brief 271 asked for a plan review of S-002 and E-004 before the freeze and before the hand check.
- **Verified:**
  - I read S-002, E-004, line.py, line-output.txt, trial-terms.md, P-002.md sections 3 to 8, the two-look-line and design-gate decisions, the Q-017 decisions and README, the Q-017 memo's §1 to §5, both cards, SURFACES.md and the registration form.
  - I compared every figure in E-004 and S-002 against line-output.txt, and the quoted terms against trial-terms.md.
  - I did not rerun line.py. Its output was stable in brief 270's review.
- **Undone:**
  - I could not open reviews/P-002-value-target-odds/reviewer.md or research/Q-013-memo.md, so I could not confirm the "Facts relied on" lines that cite them (S-002:168, 180, 181).
  - I did not open reviews/P-002-two-look-line/ beyond its existence.
  - The hand check has not run, and I did not read any extract.
- **Needed outside your surface:**
  - The Orchestrator records this return verbatim in reviews/S-002/plan.md.
  - The Definer fixes findings 1 to 8 and re-brings the spec. The other findings can go in the same change.
  - The Chief of Staff or Orchestrator names who writes the trial log, and who writes the extract's filters if they stay with the Orchestrator.
- **Open questions:**
  1. Should T5 stay in the count, given the owner's open question 3?
  2. Should the draw be seeded in the frozen trial record, or fixed some other way?
  3. Should withdrawals be decided by the Reviewer or by the owner?

## Round 2
Verdict: FAIL

Brief 273, plan review round 2 of S-002 and E-004 (P-002, M8 to M10). I read only from /home/user/ml-fixed-273, plus the card /home/user/ml-cards/P-002-value-target.md. I wrote nothing. I read round 1 (reviews/S-002/plan.md), the files as they now stand, SURFACES.md, v3_checks.py (only for the paths concerned), trial-terms.md and line-output.txt. This is round 2 of three. Findings 3 and 4 and part of finding 6 are faults I did not raise in round 1. They implicate my own earlier check (D-050), and the Orchestrator should weigh that.

## Round 1 findings, checked
All sixteen findings and the four leftovers are fixed as stated or by a sound alternative, except finding 7, whose fix has two faults (findings 1 and 2 below).

- **Finding 1 (rule ids)** is fixed. The ids are K1 to K4, RP1 and RP2, RT1 to RT7, C1 and RR1 to RR3. Awkward cases are E-RP, E-K, E-RT and E-RR. A search of both files found no stale old ids. Ruled terms are written "ruled T<n>" or "ruled P<n>". E-004 line 12 and J1 and J9 agree.
- **Finding 2 (fields)** is fixed. Step 3 now holds dispatch time and its source, question and decision times, the first-check verdict and rounds, closed-unmerged matches by branch label and brief number, the "untested" rule (line 68) and the naming patterns (line 39). The intake field is dropped.
- **Finding 3 (K2)** is fixed. K2 maps by role alone. Chief of Staff and Orchestrator briefs go to K3. K4 makes a piece with no K2 kind ineligible for a trial.
- **Finding 4 (edge cases)** is fixed. Each filter is in the table at lines 76 to 95. E-RP1 has frame D and E-RP2 has frame U. E-RT4, E-RT5, E-RT6, E-RR1 and E-RR3 are marked not sampled and checked by the Critic. The "README records the filters" loophole is closed.
- **Finding 5 (RT5)** is fixed. RT5 is outside the count, has no J1 or J9 code, and AC2 and Open question 3 agree.
- **Finding 6 (draw)** is fixed. Sides come from SHA-256 of `E-004:<trial id>:<look>:<place>`, in blocks of 10 with 5 each way. The imbalance bound of 5 holds, and the Reviewer re-derives every side. See finding 2 for reserve places.
- **Finding 7 (withdrawal)** is partly fixed. The decider (a fresh Reviewer session), the cap of 3, the 60-day rule and the touch-log timing (line 123) are all there. Findings 1 and 2 below are the faults in it.
- **Finding 8 (paths)** is fixed. The logs and count are in `status/E-004/**`, the Orchestrator's lane (SURFACES.md lines 33 and 50). The touch log is `intake/touches/<yyyy-mm>.jsonl` in the Chief of Staff's lane (line 81). The v3 checks restrict nothing there: the only `status/` pattern is `status/[PQE]-nnn.toml`, which a directory does not match. Trial records are in `experiments/**` (Definer). `tests/E-004/` is the Builder's.
- **Findings 9 to 16** are done. The plain-words section matches the body and the figures. I checked 0.0097, 0.0367, 0.0131, 0.0124, 0.0314 and 0.0312 against line-output.txt lines 36 to 44. "What this trial cannot catch" exists, and its quotes match the card, lines 20 and 21. The re-run line is at E-004:44. The line is now "copied". The marker is stripped from the short reads including merged files. AC8 has the figure 5. The scenario heading is corrected. The four leftovers are cleared or reworded.

## Findings

1. BLOCKING. experiments/E-004.md:118 and 119, with specs/S-002.md:111 and 176. The withdrawal conditions contradict the 60-day rule.
   - Condition (ii) requires the pull request to be "closed unmerged, or never opened". A piece that is open and unmerged at 60 days with no owner touch fails (ii). The withdrawal check must then answer "no", so the piece stays, and the look waits for it with no limit.
   - Line 119 ("goes to the withdrawal check, under (iii)") and S-002:111 ("so no look waits on it for ever") promise the opposite. J2 says such a piece "is withdrawn".
   - This is the stall that round 1 finding 7 was about.
   - Fix: reword (ii) to "its work has not merged: its pull request was closed unmerged, never opened, or is still open". Keep (iii)'s 60-day alternative.

2. BLOCKING. experiments/E-004.md:68 and 118 against specs/S-002.md:159 (AC8) and 176 (J2). Reserve places 61 to 63 have no side fixed in the trial record.
   - The record holds the sides of places 1 to 60 only (E-004:46 and 68). A reserve place "takes the withdrawn piece's side" (line 118).
   - J2 gives `place (1 to 63)` and says the side is "the one the frozen trial record fixes for that place". AC8 says the same. The Reviewer "recomputes every place's side by the rule above" (E-004:70), and J2 says a side that differs from the record's for its place stops the trial and sends it to the owner. That would fire on every reserve piece.
   - E-004:119's claim that no look waits longer than "60 days after dispatch, plus the 30 days" is also untrue. A reserve piece must still be dispatched after the withdrawal and merged, or be settled at its own 60 days.
   - Fix: say that reserve sides are not in the trial record and are the withdrawn piece's side. Give the Reviewer's check for them (the log's withdrawal line names the side taken over). Reword J2 and AC8 to match. Correct the 60+30 sentence to say the bound holds for places 1 to 60, and that a reserve piece adds its own wait.

3. Not blocking. specs/S-002.md:74, the hand check's seed. The seed is "the full id of the start commit of the Orchestrator's extract brief", a hash the Orchestrator creates. That is the same grinding route as round 1 finding 6, and it conflicts with "the Orchestrator chooses nothing". The cut-off date is also the Orchestrator's day. Fix: fix the seed as a string in the spec (for example `S-002-handcheck`), or take it from a commit that the Critic's PASS record names, and state the cut-off rule. (Implicates my round 1 check, which missed it.)

4. Not blocking. specs/S-002.md:186 against 188. Areas touched lists `reviews/E-004/**`, which is the Orchestrator's lane, while line 188 says the same path is outside the Builder's areas. The builder brief gives "the areas touched" as its scope. Fix: drop `reviews/E-004/**` from line 186, or list the areas by writer. (Implicates my round 1 check.)

5. Not blocking. specs/S-002.md:98 (what the Researcher gets verbatim). The quoted rules point to things the Researcher is not given: "(below)" at RT1 and E-RT6, "Open question 3" and "J1 or J9" at RT5, and "the table above" at E-RT6. Fix: say in the research question what each reference means, or reword those sentences so they stand alone.

6. Not blocking. specs/S-002.md:39. Brief records for the other two repositories are "named in the extract's README before the extract is built". That is a choice left to the Orchestrator. Fix: name the files in the spec, or say the README states them and the Critic checks them before the sample is drawn.

7. Not blocking. experiments/E-004.md:118 and 20. The withdrawal check is said to be "not told the side", but it is given the brief record for (iii). A "with" brief carries the method's fenced block, so the side shows. Its Reviewer pack would also hold the trial records unless a separate pack is made. Fix: give it only the ending record and the touch records, not the brief. List a second per-task pack for the withdrawal check under "Needed outside this spec's lane" that keeps `status/E-004/trials/**` and `experiments/E-004/trials/**` out (D-006). Today only the analysis pack is listed (S-002:237).

8. Not blocking. experiments/E-004.md:123 and 124, and S-002:70. Late touch-log lines (committed after the piece merged but before judging) are counted. They are listed, but they can still be added retrospectively on one side. Fix: have the Reviewer report each look's result with and without late lines, and the card state both.

9. Not blocking. experiments/E-004.md:67 and 76, and S-002:176. "Every eligible piece is entered; none is skipped" conflicts with "No new piece is drawn while look 1 waits". "The look's weeks" is undefined, so the Reviewer's list of unentered pieces cannot be applied. Fix: define the look's weeks as from the entry of place 1 to the entry of place 60 and any reserves, and say that pieces dispatched while a look waits are outside the trial and listed.

10. Not blocking. specs/S-002.md:233 (Open question 8). It is right to ask, but it is not yet plain. It omits that a fourth withdrawal stops the trial. "Withdrawn" is not explained (the piece is left out and its place is refilled). Fix: add "a fourth stops the trial and brings the result to you", and say plainly that a withdrawn piece is left out and replaced.

11. Not blocking. specs/S-002.md:10 (plain words). It says each side is fixed "by a shuffle no one can steer", which is true. It does not say that the sides are readable ahead, which the owner would want to weigh. Fix: add one plain clause (see the open point on sides below).

12. Not blocking. E-004.md:5 and the S-002 header. Revision, `status: draft` and `<commit>` placeholders are to be settled at freeze. Nothing is wrong now.

## The Definer's two open points
- **Open question 8.** It is right to ask the owner. The cap of 3 per look matches the three reserve places (E-004:68 and 118). The 60-day rule and the Reviewer check are labelled "this plan's figures", and the question is worded for the owner's choice. It needs the wording fixes in finding 10 and the logic fixes in findings 1 and 2.
- **Sides fixed ahead, as a stated limit.** It is acceptable as a stated limit on three conditions.
  - The wording at E-004:142 and S-002:215 must also cover choosing which brief takes the next place. It says only that "a dispatch delayed on purpose is not caught", and E-004:67 says "none is skipped or chosen", which overclaims. The dispatcher also knows the side when it picks which brief goes next.
  - The limit goes on the entry card and the results card, and in the plain-words section (finding 11).
  - The Reviewer's checks stay as written (every entry against brief times, unentered pieces listed).
  - Fixing the sides ahead does remove the round 1 hole of drawing sides after the fact. Hash-grinding is not possible. The remaining risk is timing and choice by the dispatcher, which the hold-up checks only partly catch.

## Other checks that passed
- **Header and milestones.** The header names M8, M9 and M10, matching P-002.md section 3 (lines 126 to 128). The standard Discovery and Design lines are in the project document. E-004's M13 was already in place.
- **Ruled terms and figures.** Quoted terms match trial-terms.md (T16, T23, T24, T25, T29, P6, P7, P8, P14 and others). The figures match line-output.txt.
- **Hand check and re-run.** The hand check is fixed before any extract (sample, strata, filters and fields), apart from finding 3's seed. E-004 is not a re-run (line 44 added; D-047).
- **Acceptance criteria.** AC1 to AC21 are testable scenarios and trace to V1, apart from the AC8 reserve-side wording (finding 2).

## Join-up review (docs/design/JOIN_UP_REVIEW.md form; Design, 2026-11-12)
Screens checked: none. This item has no screens or views of its own (P-002.md Design-5). The Service Desk's queue and missed-round views are filed as new work, so no screen rows were compared.

Hand-offs checked side by side, J1 to J9 against the rules, E-004 and SURFACES.md:
- **J1, J2, J9, J4, paths.** J1 and J2 write to `status/E-004/**` (Orchestrator lane). J9's `intake/touches/` is the Chief of Staff's. J4's `reviews/E-004/<trial id>/reviewer.md` is the Orchestrator's. J1's rule codes match RT1 to RT3 and RT7, with RT5 and RT6 correctly uncoded. J3 matches E-004 Step 1 and Step 3.
- **J2 and E-004 Step 4.** Blocking, same as finding 2: J2 and AC8 say reserve places 61 to 63 have a side from the record, and the record has none.
- **J2 and E-004 Exclusions.** Blocking, same as finding 1: J2 says a piece unmerged at 60 days with no touch is withdrawn, and E-004:118 (ii) forbids it.
- **S-002:186 against 188.** Not blocking, finding 4.

Result: the join-up review is not clear while findings 1 and 2 stand. Findings 3 to 11 are carried into the gate's case as risks.

## Six-part contract
- **Changed:** nothing. I wrote no file.
- **Why:** brief 273 asked for round 2 of the plan review after the Definer's change 015ba8f.
- **Verified:**
  - Every round 1 finding against the files as they now stand.
  - The renamed rule ids across both files.
  - The E-004 figures against line-output.txt, and the cannot-catch quotes against the card.
  - The new paths against SURFACES.md and v3_checks.py.
  - The withdrawal rules end to end.
- **Undone:**
  - I did not open the diff, so I did not confirm that the plain-words and body edits are the only sentences changed. I judged the two files as they stand.
  - I did not re-run line.py.
  - I did not open reviews/P-002-value-target-odds/ or research/Q-013-memo.md, which are outside the manifest.
  - Round 1's quoted Q-017 line numbers were not re-checked, since they were not changed.
- **Needed outside your surface:**
  - The Orchestrator records this return verbatim as round 2 in reviews/S-002/plan.md.
  - The Definer fixes findings 1 and 2, and should fix 3 to 11 in the same change.
  - The Chief of Staff or Orchestrator adds the second per-task Reviewer pack (finding 7).
  - The owner rules the sides-known-ahead limit and question 8 on the scenario card, after the plan passes.
- **Open questions:**
  1. Should the reserve side be the withdrawn piece's side, or a fixed hash-derived side per reserve place? (Finding 2.)
  2. Should the hand-check seed be a fixed string or a named commit? (Finding 3.)
  3. Should late touch-log lines count at all, or be shown only in a with-and-without report? (Finding 8.)

## Round 3
Verdict: PASS

Brief 275, plan review round 3 of S-002 and E-004 (P-002, M8 to M10). I read only from /home/user/ml-fixed-275 and wrote nothing. I read both files as they now stand, reviews/S-002/plan.md (rounds 1 and 2), governance/SURFACES.md, governance/PACKS.toml, docs/gates/P-002/trial-terms.md for the T23 quote, and docs/design/JOIN_UP_REVIEW.md. This is a fresh session, so no finding implicates an earlier check of mine. Findings 3 to 5 below were not raised in rounds 1 or 2, so they implicate those earlier Critic checks (D-050), and the Orchestrator should weigh that.

## Round 2's findings, checked
Findings 1 to 11 are fixed as stated.
- **Finding 1 (withdrawal condition (ii) against the 60-day rule):** fixed. E-004:120 now reads "its work has not merged: its pull request was closed unmerged, never opened, or is still open". Line 121, J2 (S-002:176), AC8 and Open question 8 now agree that a piece with no owner touch that is unmerged at 60 days goes to the check and is withdrawn, unless that would be a fourth withdrawal.
- **Finding 2 (reserve places 61 to 63):** fixed. Reserve sides are not in the trial record and are the withdrawn piece's side, in these places:
  - E-004:46, 68, 69, 70, 120
  - S-002:110, 159, 160, 176
  The Reviewer checks each reserve place against the withdrawal line and the withdrawn piece's draw line. The 60+30 bound is now stated for places 1 to 60 only, and a reserve piece adds its own wait (E-004:121; S-002:111).
- **Finding 3 (hand-check seed):** fixed. The seed is the fixed string `S-002-handcheck`, with a worked example. The cut-off is 2026-11-12 00:00 UTC, and the rule that it is not the day the extract is built is stated (S-002:74). The shortfall rule is consistent: a stratum with fewer than 10 gives all it has and the rest comes from the other stratum, and a repository short of 20 gives all it has with the shortfall listed (S-002:74).
- **Finding 4 (areas touched):** the `reviews/E-004/**` contradiction is fixed. See finding 6 below for what is left.
- **Finding 5 (pointers):** mostly fixed at S-002:98. See finding 1 below for what is left.
- **Finding 6 (brief records for the other two repositories):** fixed. The README names the files and the Critic checks them before the sample is drawn (S-002:39, 73).
- **Finding 7 (withdrawal check's information and pack):**
  - The check gets no brief, trial record, log, entry or place (E-004:120).
  - A second per-task pack is listed in S-002:237, keeping out `status/E-004/trials/**`, `experiments/E-004/trials/**` and the brief records.
  - PACKS.toml has only the standing reviewer pack and the S-001 analysis pack, so the new pack is correctly "needed outside this spec's lane".
  - The conditions are mechanical, so the check is not told the side and has no side to act on.
- **Finding 8 (late touch-log lines):** fixed. Each look is reported with and without late lines, and the cards state both (E-004:125, Step 8, J4, AC9).
- **Finding 9 (look's weeks):** fixed. It is defined at E-004:67 and pieces outside it are listed. The "none is skipped or chosen" overclaim is gone, and E-004:67 and the "sides are known ahead" limit now cover choosing which brief goes next (E-004:144; S-002:215).
- **Finding 10 (Open question 8):** fixed. It now says a withdrawn piece is left out and replaced, and that a fourth stops the trial.
- **Finding 11 (plain words):** fixed. S-002:10 says the sides are readable ahead and can be exploited, and that the checks catch this only in part.
- **Finding 12:** left for the freeze, as the brief says. The `status: draft`, `frozen_at: <commit>`, `design_id`, `revision: 3 (draft...)` and `frozen: <commit>` placeholders remain (S-002:3; E-004:5, 152).

The earlier leftovers (the line script's run, "before it freezes", the "line 3" pointer and A7) stay cleared.

## Whole plan against brief 271's standard
- **Header and milestones:** `milestones: M8, M9, M10` matches P-002.md section 3.
- **Ruled terms and figures:**
  - I re-checked the T23, T15 and P6 to P8 quotes against trial-terms.md.
  - The E-004 figures and the plain-words figures (0.1063, 0.0097, 0.0367) were not changed by this commit and match line-output.txt, as checked in rounds 1 and 2.
- **Acceptance criteria:**
  - AC1 to AC21 are testable scenarios and carry a trace to V1.
  - AC8, AC9 and J2 now agree on reserve sides, the cap of 3, the 60-day rule and the Reviewer's checks.
- **Hand check:** the sample, strata, seed, cut-off, frames, filters and fields are all fixed before any extract exists. The not-sampled cases are assigned to the Critic.
- **D-047:** E-004 is not a re-run (E-004:44).
- **"What this trial cannot catch":** it is on record (E-004:140 to 146).
- **Paths:** all paths sit in the right lanes.
  - Trial logs and the count are in `status/**` (Orchestrator).
  - The touch log is in `intake/**` (Chief of Staff).
  - Trial records are in `experiments/**` (Definer).
  - The scripts are in `src/**` and `tests/**` (Builder).

## Findings (none blocking)
1. Not blocking. S-002:98 with the edge-case table at 76 to 95 (what the Researcher gets verbatim). Four references still point to things not quoted.
   - The table's Frame column uses M, U and D, and its Filter column says "fields of step 3". Neither is explained to the Researcher.
   - Line 39 says "step 1 below".
   - The E-RT5 row (line 91) says "(step 5)".
   - Ruled T25, T32 and P14, and V1, appear in the quoted rules without a gloss.
   - Fix: add glosses to the pointer list in line 98, which is outside the quoted span, so the quoted commit is unchanged. Say that the frames are M (merged pull requests), U (pull requests closed unmerged) and D (commits with no pull request), and that the fields are the extract's. Say "step 1" is the Orchestrator building the extract, and "step 5" is the Critic's check. Say the ruled terms are the owner's rulings, quoted in section M8 and not given.
2. Not blocking. S-002:74 and 78 (frame D, E-RP1). Frame D takes commits "in no merged pull request's own commits". A squash or rebase merge's resulting commit is not one of the pull request's own commits, so it would enter frame D as "work with no pull request". That contradicts RP1, which counts squash merges as pieces. Fix: exclude from frame D any commit that GitHub's record gives as a merged pull request's merge, squash or rebase commit, and say that where GitHub's records are not read, such commits in that repository are listed as "untested" for E-RP1. This is line 74, outside the quoted span.
3. Not blocking. E-004:67, 120 to 122 and S-002:175, 176 (the unit of entry against the unit of count). An entry is per brief, but the measure counts pieces, which are pull requests, and J1 has a line only for merged pull requests. The plan does not say what happens in these cases:
   - One pull request carries two entered briefs (E-RP4): it would sit on both sides, possibly opposite ones.
   - An entered brief merges as a non-piece (RP2: records only).
   - An entered brief produces two pull requests.
   - A piece that is unmerged at 60 days with an owner touch, or closed by the owner (E-004:121, 122), "stays as a piece that needed the owner". Such a piece has no J1 line, and RT1 to RT3 define touches only up to the merge.

   These cases leave the Reviewer to read the count at judging, after the sides are known. The effect is mostly conservative, so it is not blocking. Fix: add one Exclusions line settling each case (counted once on the entry's side with the first entry kept and the second void, or left out and listed), and define that an unmerged piece's touches are counted up to its settle date. Add an unmerged-piece line to J1 or to the J2 judging join.
4. Not blocking. S-002:176 and E-004:69. The entry line carries `dispatched_at`, which J1 defines as the commit time of the brief record. The entry is committed before the brief is written (T29), so that time does not yet exist. Fix: rename the entry's field `entered_at` and have the Reviewer join the brief record's time at judging. The check "entries in dispatch order by the brief records' times" (E-004:70) then reads as written.
5. Not blocking. S-002:158 (AC7). The trial record is said to carry "method, kind, switch, expected length and line". It omits the 120 sides of places 1 to 60 that E-004:46 and 68 put in it, and that AC8 and AC9 rely on. Fix: add them to the list.
6. Not blocking. S-002:186 (areas touched). It lists `specs/S-002.md`, `experiments/E-004.md` and `experiments/E-004/**`, which are the Definer's lane (SURFACES.md:56 to 59). The builder brief takes the areas touched as its scope. The surface guard would stop a builder commit there, but the scope should not invite one. Fix: list by writer. Builder: `src/E-004/**` and `tests/E-004/**`. Definer: the spec, E-004 and `experiments/E-004/trials/**`.
7. Not blocking. S-002:10 and 157 (plain words, AC6). Both say "20 from each repository", and the shortfall rule at line 74 allows fewer, for example in Model-Lab, whose first merged pull requests are in November. Fix: add "or all it has, with the shortfall listed".
8. Not blocking. E-004:16 and 120 (who starts withdrawal checks). The Orchestrator, which knows the sides, starts each check. Nothing makes it start one for every piece that meets (iii) through an ending record. A selective early check changes only when a reserve place opens, because the 60-day rule withdraws the same piece anyway. That is the timing limit already stated as a risk. Fix: add one line saying the Reviewer lists any piece that meets (i) to (iii) with no check started within 7 days of the ending record. The 7 days is a figure for the Definer to pick and the owner's card to show.
9. Not blocking. Settle at the freeze. The placeholders listed under round 2 finding 12 remain (revision, `status`, `frozen_at`, `design_id`, `frozen`), and the two per-task packs need the owner's approval. If any of findings 1 to 8 is fixed in S-002 lines 18 to 54 or in the table at 76 to 95, the quoted span changes. The Researcher gets that span "as it stands at the commit the Critic's plan review passes" (S-002:98), so the Critic re-checks only the changed rule and its cases (S-002:72).

## Join-up review (docs/design/JOIN_UP_REVIEW.md form; Design, 2026-11-12)
Screens checked: none. This project item has no screens or views of its own (P-002.md Design-5). The Service Desk's queue and missed-round views are filed there as new work, so no screen rows were compared. The five table checks (one meaning per colour or status signal, one navigation, consistent type, no two screens doing the same job, every screen's data in the records) read "no screens". There are no needed changes to the records.

Hand-offs checked side by side, J1 to J9 against the rules, E-004 and SURFACES.md:
- **Paths (J1, J2, J4, J9):** pass. These are in the lanes named under the whole-plan check above.
- **J2, AC8 and E-004 Step 4 and Exclusions on reserve sides:** now consistent. The draw line, the withdrawal line and the Reviewer's checks agree.
- **J2 and E-004 Exclusions on the 60-day piece:** now consistent.
- **J1 and J2 against the unit of entry:** non-blocking difference (finding 3).
- **J2 entry field against J1's `dispatched_at`:** non-blocking difference (finding 4).
- **AC7 against E-004:46:** non-blocking difference (finding 5).
- **S-002:186 against SURFACES.md:** non-blocking difference (finding 6).

Result: the join-up review is clear, with no blocking difference. The non-blocking differences, findings 3 to 6, are carried into the gate's case as risks.

## Six-part contract
- **Changed:** nothing. I wrote no file.
- **Why:** brief 275 asked for round 3 of the plan review, the last of three, after the Definer's commit 749c3c9.
- **Verified:**
  - Round 2's findings 1 to 11 against the files as they stand.
  - The withdrawal, reserve, wait and side rules end to end across E-004 and S-002, including AC8, AC9, J2, J4 and Open question 8.
  - The seed and cut-off, and the shortfall rule.
  - The withdrawal check's pack against PACKS.toml and SURFACES.md.
  - The T23, T15 and P6 to P8 quotes against trial-terms.md.
  - The paths against the lanes in SURFACES.md.
- **Undone:**
  - I did not open the diff of commit 749c3c9. I judged the files as they stand, so I cannot say that no other sentence changed.
  - I did not re-run line.py or recompute the E-004 figures against line-output.txt this round, since this commit did not touch them.
  - I did not open the Q-017 memo, Q-013 or the P-002-value-target-odds review, which are outside the manifest.
  - I did not read any extract, and the hand check has not run.
- **Needed outside your surface:**
  - The Orchestrator records this return verbatim as round 3 in reviews/S-002/plan.md.
  - The Definer fixes findings 1 to 8 at or before the freeze, keeping changes to S-002 lines 18 to 54 and the table at 76 to 95 to a minimum. The Critic re-checks only any changed rule's cases.
  - The Chief of Staff adds the two per-task Reviewer packs (analysis and withdrawal check), with the owner's approval.
  - The owner rules the scenario card after the freeze, including the sides-known-ahead limit and questions 2 to 8.
- **Open questions:**
  1. Should an entered brief that merges as a non-piece, or a pull request that carries two entered briefs, be left out and listed, or counted once on the first entry's side? (Finding 3.)
  2. Should the 7-day figure for starting a withdrawal check be the owner's to set on the card? (Finding 8.)

## Re-check after round 3
Verdict: FAIL

Brief 277: re-check after round 3, of the changes on brief 276 (commit f833d70). I read only /home/user/ml-fixed-277, plus briefs 276 and 277. I wrote nothing. This is not a new round, and I judged the files as they stand, because I had no diff. Findings 1 and 2 are blocking and both come from the new "entry and its pull requests" design. Findings 3 to 9 are not blocking.

## Round 3's findings 1 to 8, checked
- **1 (glosses for the Researcher): fixed.** S-002:98 now glosses M, U, D, "the fields of step 3", "step 1 below", "(step 5)", ruled T25, T32 and P14, and V1. The glosses match trial-terms.md lines 56, 63 and 84. Three small gaps are in finding 3 below.
- **2 (frame D): fixed**, with one gap, in finding 4 below.
- **3 (unit of entry against unit of count): the design is in place at E-004:123 to 129 and J2.** Both chosen cases are marked "this plan's design". I found faults in the text, in findings 1, 2, 6 and 7 below.
- **4 (entry time): fixed in the field name.** J2 now has `entered_at`, and E-004:69 agrees. A new double meaning of "dispatch" is in finding 5 below.
- **5 (AC7): fixed.** S-002:158 now carries the sides of places 1 to 60.
- **6 (areas touched): fixed.** I read `areas_touched` in v3_checks.py:332-344. It takes only comma-split tokens with no whitespace, so the prose lines at S-002:186 to 194 add no stray globs. The Definer's paths stay in the list, as before.
- **7 (shortfall wording): fixed** at S-002:10 and 157.
- **8 (7-day check): consistent** across E-004:16 and 120, J2, Open question 8 and "Needed outside".

## Findings

1. **BLOCKING. experiments/E-004.md:78, 80, 84 and 128; specs/S-002.md:176.** Item 4 of your brief: a place left empty leaves the plan's decision rules undefined, and the plan does not state the shortfall truly enough.
   - What the plan says is true as far as it goes. E-004:128 says the look "is judged on the pieces it has" and that the results card "says so", because the figures are for 30 each way.
   - Line 78 defines "leaned the right way" as "strictly fewer of the method's 30 pieces than of the other 30". That becomes false or undefined when a side has 29. Fewer touched pieces on a smaller side proves nothing.
   - Line 78 decides whether the second look runs, so the missing rule is a decision rule.
   - Nothing caps empty places, and nothing says the one-sided Fisher test or the line's size changes with uneven sides.
   - E-004:152 and the "What the figures assume" list omit "30 each way".
   - T23 (ruled) says each side gets 30. Empty places depart from it, and no Open question puts that to the owner.
   - **Answer to your question: a stated limit alone is not enough. The void case needs a reserve place.**
   - **Fix:** let a void entry open the next reserve place (61, 62, 63) and take the void entry's side, as a withdrawal does (E-004:120). That restores 30 each way with no new mechanism.
   - Count voids and withdrawals toward one cap. The Definer states the cap; the owner's card shows it.
   - Reword E-004:78, 84, 128 and J2 to match.
   - If a place can still end up empty, for example when the reserve places run out, then:
     - say in E-004:78 that "lean" compares shares, not counts;
     - say that the test is run on the actual counts;
     - have the Reviewer report the result with each empty place counted both ways, and say the result decides only if it is the same either way;
     - add "30 each way" to E-004:152.
   - Add an Open question 9 to S-002 for the scenario card (see finding 8).

2. **BLOCKING. experiments/E-004.md:124 and 129; specs/S-002.md:176.** Merging two entered briefs into one pull request lets the sides be steered after they are known, and the plan's reason for it is partly wrong.
   - The later entry is void and its place stays empty, with no cap. A session that can read the sides chooses which later entry is dropped by choosing to merge two works into one pull request.
   - E-004:124 says the rule avoids a place being "left out by a choice to merge the two works". The rule does exactly that to the later entry.
   - The claim that a leak "shrinks the difference" holds only for the method's text. When the later, touch-heavy "with" work is merged under an earlier "without" entry, its touches land on "without". That widens the gap in the method's favour.
   - A deliberate duplicate entry for one brief (void, place left empty, E-004:69 and 129) also burns a place. It lets the dispatcher shift which side the next piece gets, uncapped.
   - The "sides are known ahead" limit (E-004:150, 67; S-002:221) names choosing the next brief and delaying a dispatch, but not these levers.
   - **Fix:**
     - the reserve-place fix in finding 1, which makes the merge-lever useless, because the voided side is refilled;
     - the same cap for duplicate entries;
     - add "merging two entered briefs into one pull request, or entering a brief twice" to the limit in E-004:150, S-002:221 and the entry and results cards;
     - correct the "shrinks" sentence at E-004:124.

3. **Not blocking. specs/S-002.md:98 (the glosses) against the quoted span.**
   - Three terms in the quoted lines are still not glossed: "ruled T1" in RP2, "U3" in the K2 heading, and "pre-mortem R<n>" in the naming sentence at line 18.
   - Fix: add one clause each to the pointer list in line 98, outside the quoted span.

4. **Not blocking. specs/S-002.md:74 (frame D, E-RP1).**
   - The exclusion works for merge and squash commits. A rebase merge adds several commits, and GitHub's record gives only the tip, so the others would enter frame D as "no pull request".
   - Fix: say "every commit a rebase merge adds" and give the method, for example walking back from the merge commit to the pull request's base. Say that where this cannot be done, the repository's frame D is "untested" for E-RP1.

5. **Not blocking. experiments/E-004.md:67 and 70 against specs/S-002.md:39 and 176.** "Dispatch" now has two meanings.
   - E-004:67 says an entered piece is "dispatched at its entry's time".
   - J2 and S-002:39 say dispatch is the commit time of the brief record, joined at judging. E-004:70 orders entries "by the brief records' times".
   - The 60-day clock and the withdrawal check's "dispatch time" (E-004:120) depend on which one applies. An entry with no brief record ever written has no dispatch time under J2's reading, so its 60 days never start.
   - Fix: state that order is entry order and that the Reviewer checks the brief records follow in the same order. The 60-day clock starts at the brief record's commit time, or at `entered_at` if no brief record exists.

6. **Not blocking. experiments/E-004.md:126 and 127; specs/S-002.md:176.** The owner's close of a piece is not covered by any touch rule.
   - E-004:126 says RT3(b) counts the close of a pull request as a send-back "on the one that merges". RT3(b) holds only when the owner closed it, and says nothing for a piece that never merges.
   - E-004:122 says an owner-closed piece "needed the owner (a send-back, RT3)". Line 127 reads "its merge" as the settle date. But RT3(b) counts a close only on a later piece, and RT3(a) needs a review.
   - Fix: add to line 127 that the owner's close counts as an RT3 send-back on the piece itself, and add "closed by the owner" to the line-126 sentence.

7. **Not blocking. specs/S-002.md:176 (J4) and the results-card list at E-004:99.** Neither names voided entries, places left empty by side, entries counted from non-piece pull requests, or pieces with two pull requests, though E-004:128 says the card says so. Fix: add them to the Reviewer's record and the card.

8. **Not blocking. specs/S-002.md:231-239.** E-004:123 says the unit-of-entry design is "for the owner's scenario card", but the Open questions list holds no question on it. Fix: add Open question 9 in plain words: a piece in two entries counts once on the first entry's side and the later place is refilled or left empty, and the cap on voids. Fix also S-002:10 to say so.

9. **Not blocking. experiments/E-004.md:128 and 76.** "Judged on the pieces it has" does not say how the "30 days after the last piece" clock works for a void place. This goes away with the reserve-place fix in finding 1.

## Items 2 and 3 of your brief
- **E-RP1 and RP1 against frame D (item 2):** they agree, except for the rebase gap in finding 4.
  - E-RP1's "every commit" in frame D fits the frame as written.
  - The "untested" rule at line 74 matches line 68.
  - The line-98 gloss matches line 74.
- **The new Exclusions entry, the void entries and J2 (item 3):**
  - They agree with each other: E-004:123 to 129, J2's awkward cases and E-004:69 and 70.
  - The "first entry" and "later entry" wording is the same in both files.
  - The J2 judging join (first pull request to merge, touches up to that merge) matches E-004:126.
  - Findings 1, 2, 5 and 6 are where they fail, and finding 2 is the steering route.

## Six-part contract
- **Changed:** nothing. I wrote no file.
- **Why:** brief 277 asked for the re-check of the Definer's change on brief 276 (commit f833d70) after the round 3 PASS.
- **Verified:**
  - Round 3's findings 1 to 8 against the files as they stand.
  - The frame D wording against RP1 and E-RP1.
  - E-004:123 to 129 and J2 end to end against each other, and against the 60-day rule and withdrawal rules.
  - The Areas touched parser, v3_checks.py:332-344.
  - The glosses against trial-terms.md lines 33, 56, 63 and 84.
  - Every figure in E-004 lines 137 to 139 against line-output.txt, which was not changed by the Definer.
- **Undone:**
  - I did not open the diff of f833d70, so I cannot say that no other sentence changed.
  - I did not re-run line.py, because the figures are unchanged.
  - I did not open the Q-017 memo, the P-002-value-target-odds review or Q-013, which are outside the manifest.
  - I did not read any extract, and the hand check has not run.
  - I did not re-check P14's "ruled" status in the gloss. Line 84 of trial-terms.md marks it "Proposed, card". The design gate decision may have ruled it, but I did not open that.
- **Needed outside your surface:**
  - The Orchestrator records this return verbatim in reviews/S-002/plan.md as the re-check after round 3.
  - The Definer fixes findings 1 and 2 and brings the changed lines back for a re-check. Findings 3 to 9 can go in the same change.
  - If the span in S-002:98 changes, the quoted commit changes. The Critic re-checks only the changed lines.
  - The owner rules on the reserve places for voids and the cap on the scenario card.
- **Open questions:**
  1. Should a void entry open a reserve place under the same cap of 3 as withdrawals, or have places of its own? (Findings 1 and 2.)
  2. Should a duplicate entry for one brief refill its place or be capped separately? (Finding 2.)

## Focused confirmation review, after the owner's ruling at the plan stop
Verdict: PASS

Focused confirmation review of the Definer's change on brief 280 (commit 4a03208), the one check the owner's option A allows. Brief 281, S-002 and E-004 (P-002, M9). I read only /home/user/ml-fixed-281, plus briefs 280 and 281, and wrote nothing. I had no shell and no diff, so I judged the files as they stand against the re-check's findings in reviews/S-002/plan.md. No finding blocks. The three non-blocking findings are below.

## 1. The re-check's findings 1 to 9, checked against option A
- **Finding 1 (void and duplicate entries refilled): fixed.**
  - A void entry opens the next spare place (61 to 63) and takes the void entry's side. This is stated in E-004:46, 68, 69, 70, 120 and 128, and in S-002:110, 111, 159, 160 and 176 (J2).
  - The side is copied from the void entry's own draw line. The Reviewer checks it (E-004:70).
- **One limit of three a look: fixed and consistent.** Withdrawals and void entries together make three, and a fourth stops the trial and brings it to the owner. This is stated in E-004:120 and 128, S-002:111, AC8, J2 and Open questions 8 and 9.
- **"A place left empty": fixed.** E-004:129 and J2 define it as a void entry with no void line when the look is judged, or a fourth void entry. For such a look:
  - "Leaned" compares shares, not counts (E-004:78).
  - The tests run on the actual counts.
  - The Reviewer also works the result with each empty place filled in every way, and the result decides only if it is the same every way. Otherwise the trial stops and the results card says so (E-004:129; J4).
- **Finding 2 (the stated limit on sides known ahead): fixed.** "Merging two entered briefs into one pull request, or entering a brief twice" now appears in:
  - E-004:39 (entry card), 101 (results card) and 150;
  - S-002:10, 110, 177 (J3), 178 (J4) and 221.
- **The "shrinks the difference" sentence (E-004:124): corrected and true.** A leak of the method's text shrinks the difference. A touch-heavy later "with" work merged under an earlier "without" entry widens it in the method's favour. The sentence now says a merge can move the result either way.
- **Finding 3 (glosses at S-002:98): fixed.** "ruled T1", "U3" and "pre-mortem R<n>" are glossed outside the quoted span.
- **Finding 4 (rebase merges, frame D at S-002:74): fixed.** It now covers every commit a rebase merge adds, with the walk-back method and an "untested" fallback.
- **Finding 5 (the two meanings of "dispatch", E-004:67): fixed.**
  - Order is entry order, and the Reviewer checks the brief records follow in the same order.
  - The 60 days run from the brief record's commit time, or from `entered_at` if no brief record exists.
- **Finding 6 (an owner-closed piece, E-004:126 and 127): fixed.**
  - A close counts as an RT3 send-back on the piece itself.
  - "Closed by the owner" is added to the line-126 sentence.
- **Finding 7 (J4 and Step 8): fixed.** Void entries by side, the reserve place each opened, places left empty with the result worked both ways, entries from non-piece pull requests and entries merged in two or more pull requests are all listed.
- **Finding 8 (Open question 9 and S-002:10): fixed.** Open question 9 states in plain words how a piece in two entries is counted and refilled. It also states the shared limit and that deliberate use "could" steer, with the cap not catching it.
- **Finding 9 (the 30-day clock for an empty place): fixed.** E-004:129 says the 30 days run from the last piece the look has.
- **"30 each way" in what the figures assume:** it is in E-004:140 ("exactly 30 pieces fall each way", A2) and 152.

## 2. Is anything else made false, and is there a new route to steer?
I re-read the entry, void, withdrawal, reserve, wait and count rules end to end across E-004 Steps 4 and 5, Exclusions, S-002:110 and 111, AC8, AC9, J2, J4 and Open questions 8 and 9. They agree with each other.
- **Reserve places:** one per withdrawal or void line, filled in order by the next eligible piece dispatched after both the entry of place 60 and the line. Each takes its refilled side.
- **Side balance:** with refill, each side still ends at 30, so the bound of 5 in AC8 holds.
- **Place left empty:** the "same result every way, else stop" rule can only make a look not pass or stop. It cannot make a method pass on an unchosen fill, so it opens no route to a pass.
- **Duplicates and merges:** these can only move which side later pieces fall on. They are capped at three, listed, and now stated as a limit.
- **Void-line timing (finding 1 below):** it is a timing lever, not a new route to a pass.

The hand check is untouched by the change. I found no way to steer it.

## 3. Unchanged parts and figures
- **Unchanged parts:** with no diff I cannot prove S-002 lines 18 to 54 and the table at lines 76 to 95 are unchanged. I read them and found no sentence about voids, reserves or the limit that the change would have had to touch, and no sentence the change makes false. They read as round 3 and the re-check described them.
- **Figures:** I compared E-004 lines 137 to 139 and S-002:10 with line-output.txt (figures not recomputed, line.py not re-run). All agree:
  - 0.1063 at 0.632 and 0.368.
  - The bands 0.307 to 0.429 and 0.571 to 0.693.
  - The gaps 0.0097, 0.0124, 0.0131, 0.0314 and 0.0367.
  - The nine-share rows.
  - The ranges 0.09616 to 0.09725 and 0.09227 to 0.09359.

## 4. The Definer's two open points
- **A result that changes with how an empty place is filled stops the trial and goes to the owner.** This is acceptable as the plan's own design. It is labelled "this plan's design" in E-004:129, asked in Open question 9, and carried in J4 and the results card. It cannot produce a pass by a choice, only a stop.
- **The Orchestrator writing void lines itself.**
  - The line carries no judgement, since both facts are in the records.
  - The script copies the side from the draw line.
  - The judging Reviewer checks the 7-day timing, each void line against the entries, and each reserve side (E-004:70 and 128).
  - This is acceptable, with finding 1 below as a non-blocking limit.

## Findings (none blocking)
1. **Not blocking. experiments/E-004.md:128 and 150; specs/S-002.md:221.**
   - The Orchestrator knows the sides and picks when to write a void line within the 7 days.
   - That timing decides which later piece takes the reserve place, and which later pieces count as outside the look's weeks (E-004:67).
   - A late or missing line is only listed. This is the same timing lever the plan already accepts for withdrawal checks (round 3 finding 8), but the "cannot catch" text does not name it for void lines.
   - Fix: add "or the time a void line or a withdrawal check is started within the 7 days" to the limit's list of choices, in E-004:150 and S-002:221. Optionally add it to the J3 and J4 lists.
2. **Not blocking. experiments/E-004.md:129 with 121, and Step 5 item 1.**
   - "A place is left empty only when…" does not cover a reserve place that is opened but not filled because no eligible piece has been dispatched yet.
   - Line 121 says only that the reserve piece "adds its own wait". Step 5 item 1 does not say whether the look waits for an open reserve place.
   - Fix: say that a look with an open reserve place waits for it, or is judged as a place left empty after a stated time. This predates the change, but void entries now open more reserve places.
3. **Not blocking. experiments/E-004.md:5.**
   - The `revision: 3 (draft, after … rounds 1 and 2 …)` line is stale: it does not mention round 3, the re-check or this change.
   - Fix: update it at the freeze, with the other placeholders left for the freeze (S-002 header, E-004:152).

## Six-part contract
- **Changed:** nothing. I wrote no file.
- **Why:** brief 281 asked for the one focused confirmation review the owner chose at the plan stop (option A).
- **Verified:**
  - Re-check findings 1 to 9 against both files as they stand.
  - The entry, void, withdrawal, reserve, wait and count rules end to end, including AC8, AC9, J2, J3, J4 and Open questions 8 and 9.
  - The figures in E-004 lines 137 to 139 and S-002:10 against line-output.txt, which I read.
  - The glosses at S-002:98 and the frame D wording at S-002:74.
- **Undone:**
  - I did not open the diff of commit 4a03208, so "unchanged in content" for S-002 lines 18 to 54 and the table at 76 to 95 rests on reading them, not on a comparison.
  - I did not re-run line.py or recompute any figure.
  - I did not re-read S-002 lines 100 to 150 beyond M9's text and the acceptance criteria.
  - I did not open the Q-017 memo or the other records outside the manifest, and the hand check has not run.
- **Needed outside your surface:**
  - The Orchestrator records this return verbatim in reviews/S-002/plan.md as the focused confirmation review.
  - The Definer settles non-blocking findings 1 to 3 at or before the freeze, with the other placeholders. Neither finding touches S-002 lines 18 to 54 or the table at 76 to 95.
  - The Chief of Staff adds the two per-task Reviewer packs, with the owner's approval.
  - The owner rules the scenario card after the freeze, including the sides-known-ahead limit and Open questions 2 to 9.
- **Open questions:**
  1. Should the 7-day timing of void lines and withdrawal checks be named in the limit on the entry and results cards (finding 1)?
  2. Should a look wait for an open reserve place, or be judged as a place left empty after a stated time (finding 2)?

This is my first check of this change. It implicates no earlier check of mine (D-050).

## Re-run on the changed lines, before the freeze (brief 336)

Verdict: FAIL

One thing blocks the freeze, and it is small to fix. The change that settled how a piece's start time is read when its commits name more than one brief (the earliest brief record wins) is right for the past sample and moves no figure of the hand check, but it was not carried into the trial: there, the same rule lets a trial piece's counting window start before the piece was entered and its side drawn, while the trial's own join sheet still starts it at the entered brief. Whoever hands out the work can see the next side, so they could fold a new trial brief into a pull request that already carries an older brief the owner has stepped in on, and so place a piece that is certain to count as "needed the owner" on a side of their choosing. One clause closes it. Everything else I found is wording or a limit that can be stated: the owner's ruling and the trial terms are not contradicted, the confirmation rules hold together end to end, and the two hand-check changes agree with memo 5. I could not run git, so the claim that the hand check's rules changed only at two lines rests on the diff I was given, which shows two more changed lines in that section; neither moves a figure. Nothing here is irreversible.

## Findings

1. **Blocking. A trial piece whose trailers name a second, earlier brief gets a window that starts before its entry; two rules give two start times.**
   - Where: `/home/user/Model-Lab/specs/S-002.md`:46 (new clause: "where the trailers name more than one brief with a record, the earliest of those first adds"), against :190 (J2: "the piece's dispatch time, the commit time that first adds its brief record, is joined from the brief record by the Reviewer at judging") and `/home/user/Model-Lab/experiments/E-004.md`:67 and :127 ("from its dispatch up to that merge"). J1's `dispatched_at` at S-002.md:189 still reads "the commit time that first adds the brief record", singular.
   - Why it matters: before the change :46 was singular, and for a trial piece J2 gave the entered brief's record. Now J1's window for a piece whose commits also name an older brief that was never entered (dispatched before the trial froze, outside the look's weeks, or of a role K4 does not admit) starts at that older brief's record. The naming rule at :46 already makes a record naming "brief <b>" name the piece for any brief whose work it carries. So an owner question on the older brief, given before the trial piece's side was drawn, counts on the trial piece.
   - The steering route: the session that dispatches knows the next place's side (E-004.md:151) and knows which open pull requests already hold an owner touch. Folding the entered brief's work into such a pull request puts a piece certain to "need the owner" on the known side. E-004's limit covers only "merging two entered briefs", which voids an entry and is capped at 3 a look; a merge with a brief that was not entered voids nothing, is not capped and is not listed.
   - Fix (one clause in each of :46 or J1, J2 and E-004 Step 4): for a trial piece the window starts at the entered brief's dispatch (the first entry's, where two entered briefs merge), whatever other briefs its trailers name; the Reviewer lists every trial piece whose commits name a brief that is not its entry's. Touches naming the other brief that fall after the entry would still count on the trial piece: state that as a limit under "The sides are known ahead" and on the cards.
   - Stated limit instead? Not on its own: the touch has already happened when the choice is made, so the result of the choice is known in advance, unlike the other dispatch choices E-004 lists. With the clause above, the remainder can be a stated limit.
   - Self-implication (D-050): my role's earlier check (`/home/user/Model-Lab/reviews/Q-018-recode-5/_critic-verbatim.md`, finding 16) asked for this wording for the past count and did not ask what it does on a trial piece.

2. **Non-blocking. The Definer's open question on a piece whose trailers name several briefs, only some with a record.**
   - Where: S-002.md:46.
   - As written it has an answer: the first-commit fallback applies only "with no brief record", so the dispatch is the earliest first add among the briefs that have a record, and briefs with none are ignored. That is acceptable, but the window can then open after the piece's own first commit, and touches before it are missed.
   - No figure of memo 5 turns on it: memo 5 gives the dispatch as the first commit for every piece but Model-Lab #98 (`/home/user/Model-Lab/research/Q-018-memo-5.md`:9), #98 has both records, and Personal-Org-Operating-Model #20 has none (recode-5, finding 16).
   - Fix: say it in one clause ("briefs with no record are left out, and the piece is listed"), and add the case to step 6's list of what the rules cannot catch. Can be a stated limit.

3. **Non-blocking. The Definer's open question on untimed touches on a withdrawn piece.**
   - Where: S-002.md:197 ("an untimed one is taken as before it, since it cannot be shown to come after"); E-004.md:121 (the re-check: "timed before its withdrawal line", with no "or untimed"); E-004.md:20, :86, :101, :113 all say "or untimed".
   - Taking an untimed touch as before the withdrawal is right: it only causes the other-way result to be worked, which can bring a trial to the owner or stop it and can never pass a method, and such a line exists only when the owner's own answer holds it.
   - E-004's "Withdrawn" re-check should say the same, for one reading across the file. The result does not change, since Step 6's first branch already puts the piece back. Fix: add "or untimed" at E-004.md:121.
   - Related gap: J9 defines "while under way" as "after its dispatch and before its merge or settle date" (S-002.md:197); a withdrawn piece has neither. Fix: add "or its withdrawal line". Can be a stated limit.
   - Self-implication (D-050): my role's finding 6(b) in `/home/user/Model-Lab/reviews/S-002-rulings-7/_critic-verbatim.md` proposed the time condition this follows from.

4. **Non-blocking. AC9 marks only some of this plan's design as design.**
   - Where: S-002.md:174.
   - Marked: the list without the sides, the unstrike check, a struck line not counting, the withdrawn-piece exception, the stop at look 1. Not marked, and so reading as ruled: the Reviewer's check of the list and the log against the desk's record, counting a touch line only when a confirmed list or the answer holds it, the cut at the confirm line, and the results worked the other way.
   - The plain words (:10), Open question 20 (:266), Risks (:233), J9 and E-004 Step 6 mark all of these, so the owner is not misled where they rule. Fix: one "by this plan's design (J9)" covering everything in AC9 after "confirmed or added to".

5. **Non-blocking. The new start condition is unmarked, and the reason given for "no time limit" cites a record that does not say it.**
   - E-004.md:30 and S-002.md:10 and :177 add "the desk can keep your answer" to P20's three conditions (`/home/user/Model-Lab/docs/gates/P-002/trial-terms.md`:90) without saying it is this plan's addition. It is the cautious direction. Fix: mark it "this plan's design" at Step 0.
   - E-004.md:86 and S-002.md:197 say the confirmation has no time limit "since the ruling is the owner's own choice, never a default". The record's words (`/home/user/Model-Lab/decisions/questions/P-002-touch-log-check.md`:6) describe the question, which does not default, not each look's confirmation. The conclusion does follow from the ruling line ("Before each trial look is judged, the owner confirms"). Fix: give that as the reason.
   - The plain words do not carry the cost that Open question 20 does ("a look, and new pieces of its kind, wait for it"). Fix: one clause at :10, or carry it on the scenario card.

6. **Non-blocking. The Chief of Staff has no time bound for putting the list, and a line committed after each confirm line sends the list back without end.**
   - Where: E-004.md:86; S-002.md:197.
   - Neither changes a result, since every counted line must be on a list the owner confirmed. Both can hold a look unjudged with its kind closed (P11), by a session that knows the sides. The Orchestrator's like choices carry a 7-day figure and a late list. Fix: a figure for putting the list with the Reviewer listing a late one, or state it under "The touch log's keeper knows the sides". Can be a stated limit.

7. **Non-blocking. Small things the change left behind.**
   - E-004.md:50 and :51 still give the expected length as "plus 30 days"; with the confirmation it is a floor. Fix: "at the least".
   - S-002.md:266 lists where the ruling was written and leaves out E-004 Step 0 and "Deciding threshold", and the spec's :82, AC10, AC12 and "Needed outside this spec's lane".
   - E-004.md:5's revision line stops at brief 282; by its own words it is settled at the freeze.

8. **Item 3, the hand check: no figure of memo 5 moves; the "only two lines" claim I could not confirm.**
   - :46 agrees with the records: #98's dispatch is brief 258's record at 18:23:13 with 0 touches (memo 5 :9, :90; recode-5 finding 16); #20 has no brief record.
   - :112 agrees: (r)'s seen case, #30's L-0140 counted twice with no yes-or-no changed, is recode-5 finding 8, and memo 5 gives #30 4 touches (:68); (u) is recode-5 finding 15, and the pieces it names each count at least one touch (memo 5 :24, :68, :73, :78). Both add to the list of limits and change no rule.
   - change.diff, whose base is main before brief 321, also shows :82 and :114 changed in the M8 section. :82 changes only how a touch-log line counts at a trial look, outside the lines quoted to the Researcher. :114 item (5) adds the count of what the "later work" codes take off, which memo 5 section D gives (22 touches; 2 pieces; 0 back) and recode-5 findings 10 and 11 confirm. If both predate memo 5's commit, the Orchestrator's check stands; I hold no git to tell.
   - :46 lies inside the lines research/Q-018.md quotes (S-002.md:110), so that quote no longer matches the spec.

9. **Item 1 and item 2, the rest: no finding.**
   - Against the ruling, the trial terms and the project terms cited: the ruled option is quoted as recorded; reading P1 as "no sooner than" is marked as this plan's reading (E-004.md:76); the new stop is marked as design at E-004.md:79, :145 and S-002.md:174, :197, :266.
   - Entry, void, withdrawal, reserve, confirmation and count rules, read end to end as they stand: apart from finding 1, I found no route that is not already a stated limit. A list that leaves out a piece or a line, a strike or addition the answer does not hold, an unstrike of a held strike, and lines after the confirm line are each caught by the Reviewer's check against the desk's record. A withdrawal made because a touch was not logged is shown by the result worked the other way; where the deciding result is a pass, it stands, with both results on the results card for the owner's ruling.

## Six-part contract
- **Changed:** nothing; I am read only and wrote no file.
- **Why:** brief 336, the plan review re-run on the lines changed since round 3's confirmation, before the freeze.
- **Verified:** Read and Grep only; no shell, no git.
  - Read in full: `/home/user/Model-Lab/AGENTS.md`, my charter, `/home/user/Model-Lab/docs/briefs/336-critic.md`, `/home/user/Model-Lab/experiments/E-004.md`, `/home/user/Model-Lab/decisions/questions/P-002-touch-log-check.md`.
  - `/home/user/Model-Lab/specs/S-002.md`: lines 1 to 91, 109 to 116, 171 to 177, 186 to 190, 197, 233 and 266 to 272.
  - change.diff: lines 1 to 146 and 158 to 159 in full; the rest by a search of its changed-line openings.
  - `/home/user/Model-Lab/research/Q-018-memo-5.md`: lines 1 to 30, 138 to 149, 196 to 209, and searches for #98, L-0140 and the pieces (u) names.
  - `/home/user/Model-Lab/reviews/Q-018-recode-5/_critic-verbatim.md`: its findings' opening lines and finding 16 in full. `/home/user/Model-Lab/reviews/S-002-rulings-7/_critic-verbatim.md`: lines 30 to 59. `/home/user/Model-Lab/docs/gates/P-002/trial-terms.md`: the rows for P1, P11, P16, P20, T15 and T29.
  - A search of the before-copy of S-002.md found none of the new phrases of :46, :112 and :114, so those are changes.
- **Undone:**
  - Not read: S-002.md lines 92 to 108, 117 to 170, 178 to 185, 191 to 196, 198 to 232, 234 to 265 and 273 to 281, so the changed J3, J4 and the Risks line at :236 were not checked; `/home/user/Model-Lab/reviews/S-002/plan.md` beyond a search; reviews/S-002-rulings-4 to -6; `/home/user/Model-Lab/docs/projects/P-002.md`; the other decision records.
  - The diff of :112 was checked by phrase search, not word by word.
  - research/Q-018-extract/sample.jsonl is outside my manifest, so "the only other sampled piece whose trailers name more than one brief" at :46 rests on memo 5 :9 and recode-5 finding 16.
- **Needed outside my surface:**
  - The Definer: finding 1's clause, and whichever of findings 2 to 7 are taken.
  - The Orchestrator: confirm by git that :82 and :114 did not change after memo 5's commit; re-quote :46 in research/Q-018.md, since it is among the quoted lines.
  - The Chief of Staff: carry on the scenario card the limit left by finding 1 and those of findings 2, 3, 5 and 6 if stated rather than fixed.
- **Open questions:**
  - Whether finding 1's remaining import (touches naming a non-entered brief after the entry) should also be closed, by treating a trial pull request that carries a non-entered brief as listed and brought to the owner, or left as a stated limit. That is the owner's to see on the scenario card.
  - Whether a re-check of finding 1's clause alone is enough before the freeze; I think it is, since nothing else blocks.

## Focused confirmation review, at the second plan stop (brief 338)

Verdict: PASS

The focused fix does what the owner chose, and nothing in the changed lines blocks the freeze, but one claim is only partly confirmed. Not confirmed in full: the plan now says the second ruling leaves the hand check at 14 of 33. That is shown for #49 only. The new rule is general, and the 61 codes that both earlier Critics gave as "later work" were coded without it; nothing I may read shows whether any of them is a question about a plan its piece's own work wrote. If one is, a touch count moves, and for two pieces the 14 would move. That needs one re-read of those codes before the figure is put to the owner; it is not a change to the plan's rules. Otherwise: the route found last time is closed. A trial piece's counting now starts at its own entered brief, whatever other work its pull request carries, in every place the start time is given, and the Reviewer lists such pieces. What is left (questions on the other work after the start still count) is stated wherever the limits are listed. The six smaller points are each fixed or stated as a limit. The second ruling is written in as the card's option A says and no wider. The remaining findings are wording, or small gaps that can be stated as limits. Nothing here is irreversible.

## Findings

1. **Non-blocking for the plan's rules; a check is needed before the figure is relied on. "No count of memo 5 changes" is shown for #49 only.**
   - Where: `/home/user/Model-Lab/specs/S-002.md`:268 (Open question 22: "so no count of memo 5 changes and the hand check's figure stays 14 of 33"); :109 (step 3, *Later work*), whose own sentence is scoped to rows 60 and 61 and is right.
   - Confirmed: `/home/user/Model-Lab/research/Q-018-memo-5.md`:128 and :160 give #49 one touch, Q-031's first add at 568cd6e0, coded "not said" with both readings; :137 gives 14 of 33. "This piece" counts as "not said" does, so #49 does not move.
   - Not confirmed: memo 5 :163 gives 61 "later work" codes, and :143 to :144 say they take off 22 touches (Model-Lab #73: 1; #29: 1; Service-Desk #230: 4; Personal-Org-Operating-Model #30: 2, #27: 6, #25: 8) and turn 2 pieces (#73, #230) from needing the owner to not. The rule at :46 and :109 now applies to all of them. Any one that asks about a plan its piece's own commits drafted or plan-reviewed, outside its `Spec:` trailers, would now read "this piece". On #25, #27, #29 or #30 that moves touch totals and the 22; on #73 or #230 it moves 14 of 33. No record in my manifest says whether such a case exists; the codes file is outside it.
   - Fix: a fresh Critic with the records pack re-reads the "later work" codes against option A (at the least those on #73 and #230, which decide the yes-or-no figure). Until then, word :268 as :109 is worded: #49's rows change no count, and the other codes are re-read before the freeze.
   - Stated limit instead? No: it is a check to run, not a limit. It can be carried on the scenario card only as "not yet re-read".
   - Self-implication (D-050): the codes were made and checked by my role's earlier sessions. This finding does not fault them; they coded before the ruling.

2. **Non-blocking. "After the entry" and "after the dispatch" are used for the same boundary, and they are two different times.**
   - Where: "after the entry" / "before its entry" at S-002.md:46, :191 (J3), :192 (J4), :235 (Risks) and `/home/user/Model-Lab/experiments/E-004.md`:39, :102, :151; "after the dispatch" at E-004.md:67, S-002.md:190 (J2 awkward case) and :267.
   - The rule itself is clear: the window starts at the commit that first adds the entered brief's record, which comes after the entry (E-004.md:67). A touch on the other work between the entry and that commit does not count, though the limit's words say it does.
   - Steering: the session that dispatches chooses when the brief record lands, so on a folded piece it can put a foreseen answer inside or outside the window. That is the same choice as "delaying a dispatch", already a stated limit, so it is not a new route.
   - Fix: "after its dispatch" throughout, or one clause under "The sides are known ahead" saying the time between entry and brief record is the dispatcher's. Can be a stated limit.
   - Self-implication (D-050): brief 336's finding 1 used "after the entry" in its own fix wording, and the Definer followed it.

3. **Non-blocking. The Reviewer's list catches a fold only when the other work's commits name a brief.**
   - Where: E-004.md:67, :100, :151; S-002.md:46, :190, :192.
   - A trial brief's work folded into a pull request whose other commits name no brief (work with no brief, K3) is not listed, yet a touch after the dispatch that names the pull request by number still counts on it. Touches before the dispatch are shut out by the window either way, so finding 1 of brief 336 stays closed.
   - Fix: also list a trial piece whose first own commit is earlier than its entry, or state it with the fold limit. Can be a stated limit.
   - Also: "with that brief and its side" does not say whose side; the other brief has none. Fix: "and the trial piece's side".

4. **Non-blocking. J2's recount of an entry no count line carries does not say it uses the new start time.**
   - Where: S-002.md:190 ("recounting its RT1a, RT1c and RT7 touches with every question and note 'not said'"), against :46, which makes such an entry a trial piece whose dispatch is its entered brief's.
   - For that piece the count line's `dispatched_at` (:189) follows the general rule, so it can be an older, non-entered brief's. :46 gives the right answer, but J2's procedure names only the three coded touch types, not comments, fixes or send-backs before the entry.
   - It is narrow (the entered brief's number must be unreadable in the trailers, and the piece is listed on the results card), so I do not rate it a route. Fix: one clause in J2, "reading every touch on it from its entered brief's dispatch". 

5. **Non-blocking. The new pointers in "What a touch is" are not in step 4's list of what each pointer means.**
   - Where: S-002.md:110, against :46, which now points to "J2", "step 6 (v)" and E-004's "Exclusions" and "The sides are known ahead". :110 explains "J1", "J9" and "step 6" only in RT1's lines, and says the quoted lines stand alone.
   - Fix: add the three to :110 when research/Q-018.md is re-quoted.

6. **Non-blocking. The limit from brief 336's finding 6 is stated in full but not in the card lists.**
   - Where: stated at E-004.md:153 and S-002.md:233, each ending "on the entry card and the results card". The card summaries at E-004.md:39 and :102 and J3, J4 (S-002.md:191, :192) do not hold the clause that a session can hold a look unjudged.
   - Fix: one clause in each, or carry it on the scenario card.

7. **Item 1 of the brief: brief 336's finding 1 is closed as option A states it. No finding.**
   - The clause stands at S-002.md:46, :189 (J1 `dispatched_at`), :190 (J2, and a new awkward case) and E-004.md:67, with the first entry's dispatch where two entered briefs merge, and option A quoted word for word from `/home/user/Model-Lab/questions/P-002-plan-stop-2.md`:10.
   - The Reviewer's list is at E-004.md:67 and :100 and S-002.md:192.
   - The remainder is stated at S-002.md:10, :191, :192, :235, :267 and E-004.md:39, :102, :151, including that a fold voids no entry and is not capped.

8. **Item 2: findings 2 to 7 of brief 336. No finding beyond 6 above.**
   - Finding 2: fixed at :46 and stated as limit (v) at :112, which agrees with memo 5 :9 as brief 336 read it.
   - Finding 3: fixed ("or untimed" at E-004.md:121; "or its withdrawal line" at S-002.md:197).
   - Finding 4: fixed at S-002.md:174.
   - Finding 5: fixed. The added start condition is marked as this plan's at E-004.md:30 and S-002.md:10, :177; `/home/user/Model-Lab/docs/gates/P-002/trial-terms.md`:90 does name only the other three. The reason for no time limit now quotes the ruling line (E-004.md:86, S-002.md:197), and the quote is part of the line J9 gives in full. The cost is in the plain words at :10.
   - Finding 6: stated as a limit.
   - Finding 7: fixed (E-004.md:5, :50, :51; S-002.md:266). AC10 is not added to :266; it holds no word of the confirmation, so that part of brief 336's finding 7 was wrong (D-050: my role's).

9. **Item 3: the second ruling is written in as option A says and no wider. No finding beyond 1 above.**
   - Option A is quoted word for word at S-002.md:46 and :109 and cited at :197 and :268; the owner's words match `/home/user/Model-Lab/intake/P-002-owner-answers-2026-11-13.md`:10.
   - "Drafting it or adding its plan review" follows the card's own description ("drafted and reviewed").
   - :46 says it reads what a question asks about and does not widen which records name a piece. On a trial piece no code is read, so the ruling reaches no trial.
   - The window change moves no figure of memo 5: no sampled piece is a trial piece.

10. **Item 4: no new route found.** Read end to end on the changed lines, the only choices left to a session that knows the sides are the fold (stated), the entry-to-record timing (finding 2, equal to a stated limit) and holding a look unjudged (stated, changes no result). The hand check's rules changed only by the listing at :46 and (v), and the plan-written-by-piece reading.

## Six-part contract
- **Changed:** nothing; I am read only and wrote no file.
- **Why:** brief 338, the one focused confirmation review the owner chose at the second plan stop.
- **Verified:** Read and Grep only; no shell, no git.
  - Read in full: `/home/user/Model-Lab/AGENTS.md`, my charter, `/home/user/Model-Lab/docs/briefs/338-critic.md`, `/home/user/Model-Lab/docs/briefs/337-definer.md`, both cards, the intake item, and `/home/user/Model-Lab/reviews/S-002/plan.md` lines 543 to 622.
  - `/tmp/claude-0/-home-user/3bf22eb7-3034-5300-9273-72fad23a7eb4/scratchpad/before-338/change.diff`: every line, 1 to 186.
  - The files as they stand: phrase searches of `/home/user/Model-Lab/specs/S-002.md` and `/home/user/Model-Lab/experiments/E-004.md` put each changed phrase at the lines cited above, matching the diff.
  - `/home/user/Model-Lab/research/Q-018-memo-5.md`: lines 28, 72, 101, 111, 127 to 130, 137 to 144, 148 to 167, 180, 186, by search. `/home/user/Model-Lab/docs/gates/P-002/trial-terms.md`: rows P11 and P20.
- **Undone:**
  - The before-copies of the two files were not opened apart from the diff.
  - Unchanged text was read only as the diff's context lines; E-004's "An entry and its pull requests" sub-bullets (:125 on) were not read.
  - The quote of the touch-log ruling line rests on J9's own quotation and brief 336; `decisions/questions/P-002-touch-log-check.md` is outside my manifest.
  - Rows 60 and 61 rest on memo 5; `reviews/Q-018-later-work/_critic-check-verbatim.md` is outside my manifest.
- **Needed outside my surface:**
  - The Orchestrator: dispatch the re-read of the "later work" codes under option A (finding 1) before 14 of 33 goes on the scenario card; re-quote the changed lines in research/Q-018.md (carried from brief 336, with finding 5).
  - The Definer: the wording of S-002.md:268 (finding 1), and whichever of findings 2 to 6 are taken.
  - The Chief of Staff: carry on the scenario card the fold limit, and findings 2, 3 and 6 if stated rather than fixed.
- **Open questions:**
  - Whether the owner wants the re-read of finding 1 done before the freeze or only before the scenario card. I rated it non-blocking because the plan's rule is right and no trial or hand check can be steered through it; if an unconfirmed figure in the plan counts as the plan being wrong, this is the one finding that would change the verdict.
  - Whether a pull request that carries both a trial brief and other work should come to the owner rather than only be listed (left open by brief 336; still the owner's to see on the scenario card).

## Check of the lines changed after the second plan stop's review (brief 343)

Verdict: PASS

Nothing failed, and nothing in the changed lines makes the plan wrong or opens a new way to steer a trial or the hand check. Two things I could not check: the two commit ids now given for the cards "as put", because the question files are gone from the checkout and I have no way to read history, and the sample lines and the earlier re-code finding cited beside the moved hand-check results, which are outside what I may read (they moved word for word, so the change did not alter them). The five smaller points from the last review are each fixed or stated as a limit, and the 14 of 33 figure is now worded as the re-read gives it, with the re-read's one open question carried beside it. The citation changes, the two wording matches and the move of the hand check's results out of the quoted rule line change no rule's meaning. Three small wording gaps remain, all of which can be stated limits or carried on the owner's scenario card. Nothing here is irreversible.

## Findings

1. **Non-blocking. The new listing is described as catching a fold into work with no brief, but it catches only one that began before the entry; the gap is stated in one place only.**
   - Where: `/home/user/wt/ml-answers/specs/S-002.md`:46, :190 (J2 awkward case), :267 and `/home/user/wt/ml-answers/experiments/E-004.md`:67, each "every trial piece whose first commit's author time is earlier than its entry's `entered_at`, as one folded into work whose commits name no brief would be". S-002.md:110 (the new pointer for "The sides are known ahead") says a fold into "other work ... is only listed by the Reviewer".
   - Against: E-004.md:151, which alone says "so a fold into work whose commits name no brief and all come after the entry is not listed".
   - The card lists (E-004.md:39, :102; S-002.md:191, :192) and Risks (S-002.md:235) name only a fold into "another brief's work", so the unlisted case is not on them, though E-004.md:151 ends "This limit is on the entry card and the results card".
   - Steering: touches after the dispatch that name the pull request count on the trial piece whether the fold is listed or not, and touches before the dispatch are shut out either way. So this is the fold limit already stated, with a narrower listing than four sentences suggest, not a new route.
   - Fix: at S-002.md:46, :190, :267 and E-004.md:67, "as one folded into work whose commits name no brief and begun before the entry would be"; at S-002.md:110, "listed by the Reviewer only where its commits name another brief or begin before the entry"; one clause in the card lists, or carry it on the scenario card. It can be a stated limit; it already is one at E-004.md:151.
   - Self-implication (D-050): brief 338's finding 3 proposed this very listing ("whose first own commit is earlier than its entry") without naming its gap. That was my role's earlier session; the Definer followed it and stated the gap itself.

2. **Non-blocking. S-002.md:268 says the re-read "re-read the other 61 codes" without the re-read's own limit on how it was done.**
   - Where: S-002.md:268, against `/home/user/wt/ml-answers/reviews/Q-018-later-work/_critic-reread-verbatim.md`:34 ("I did not re-open every one of the 61 records in full. Where the piece's own files hold no plan outside its trailers, the ruling cannot change the code whatever the record says").
   - The figure itself is worded as the records give it: 0 of 61 changed (:5, :11), rows 60 and 61 confirmed "this piece" (:21), 14 of 33 from `/home/user/wt/ml-answers/research/Q-018-memo-5.md`:137, and the open question on #25's rows 92 to 99 carried (:39). `/home/user/wt/ml-answers/decisions/questions/P-002-plan-written-by-piece.md`:15 says the same.
   - Fix: add "from each piece's own-file list, not by re-opening every record" to :268, or leave it; the reasoning at :34 holds. Can be carried on the scenario card with the open question.
   - Self-implication (D-050): the re-read (brief 339) and the finding that asked for it (brief 338, finding 1) were my role's earlier sessions. I checked the wording against the record, not the re-read's judgement.

3. **Non-blocking, not checked. The commit ids for the cards "as put" could not be confirmed.**
   - Where: S-002.md:46, :109, :197, :267, :268 and E-004.md:67: `questions/P-002-plan-stop-2.md at commit 9c9a855` and `questions/P-002-plan-written-by-piece.md at commit d231a51`.
   - Neither question file is in the checkout (the decision records deleted them, as `/home/user/wt/ml-answers/decisions/questions/P-002-plan-stop-2.md`:12 and P-002-plan-written-by-piece.md:12 say), and I hold no tool that reads history.
   - Fix: the Orchestrator confirms each id holds the file with option A in the quoted words (`git show 9c9a855:questions/P-002-plan-stop-2.md`, `git show d231a51:questions/P-002-plan-written-by-piece.md`) before the freeze. Not a limit; a check to run.

4. **Item 1 of the brief: brief 338's findings 2 to 6 and finding 1's figure. No finding beyond 1 and 2 above.**
   - Finding 2 (one boundary): fixed. "After the entered brief's dispatch" at E-004.md:39, :102, :151 and S-002.md:191, :192, :235; "before its dispatch" and "after its dispatch" at S-002.md:46; the plain words at S-002.md:10 now say "after its brief was dispatched". A search of both files finds no "after the entry" or "before its entry" left for this boundary; the one "after the entry" at E-004.md:151 is the listing's own boundary, which is the entry, and is right.
   - Finding 3: fixed in part and stated as a limit (finding 1 above). "The trial piece's side" at E-004.md:67, :100 and S-002.md:190, :192.
   - Finding 4: fixed at S-002.md:190 ("reading every touch on it from its entered brief's dispatch").
   - Finding 5: fixed at S-002.md:110, which now explains "J2", "step 6 (v)", E-004's "Exclusions" with "An entry and its pull requests", and "The sides are known ahead". Each matches the part it points to, apart from the "only listed" wording in finding 1.
   - Finding 6: fixed. The clause that a session can hold a look unjudged is at E-004.md:39, :102 and S-002.md:191, :192, and agrees with the full statements at E-004.md:153 and S-002.md:233 ("no result changes").
   - Finding 1's figure: worded as the re-read gives it (finding 2 above).

5. **Item 2: brief 342's changes change no rule's meaning. No finding beyond 3 above.**
   - Citations: every place now cites `decisions/questions/P-002-plan-stop-2.md` or `P-002-plan-written-by-piece.md` (E-004.md:5, :67; S-002.md:46, :109, :197, :267, :268), with the quoted option words unchanged. A search finds no bare `questions/` citation of either card without its "at commit", and no "the decision record follows" left. Both decision records hold the owner's words as quoted (:9 of each).
   - Wording matches: S-002.md:10 and :267 agree with brief 341's wording (dispatch as the boundary; the first-commit listing).
   - The move: the two results that stood in S-002.md:46 (the parenthesis on Model-Lab #98's briefs 258 and 263 and Personal-Org-Operating-Model #20, and "No piece of the hand check's sample is a trial piece, so this changes no count of memo 5") now stand at the end of step 6, S-002.md:112, word for word with the same sources, under "kept here so that the lines step 4 quotes hold no result". Step 6 is outside the lines step 4 quotes. The rule at :46 is otherwise word for word, apart from brief 341's boundary and listing changes. Memo 5 :9 supports the #98 dispatch as stated.
   - Out of scope, noted only: :46 still holds three examples from the records with sample lines (Model-Lab #29's and #92's deleted question files; question file 197dd190; Personal-Org-Operating-Model #32's). They illustrate rules and state no count, the change did not touch them, and earlier reviews passed them.

6. **Item 3: nothing else made false, and no new route. No finding beyond 1 above.**
   - The new listing only lists; it moves no count, window or side. Its test uses the first commit's author time, which a committer can set, but nothing is decided by it.
   - E-004.md:67's new reason ("a touch after the trial piece's dispatch whose record names the piece still counts on it, whatever other work the record is about") agrees with S-002.md:46's naming rule and with J2's awkward case at :190.
   - The window's start is the same in every place it is given (S-002.md:46, :189, :190; E-004.md:67), so brief 336's finding 1 stays closed.
   - No sampled piece is a trial piece (S-002.md:112), so nothing in the change reaches the hand check's counts.

## Six-part contract

- **Changed (by file):** nothing. I am read only and wrote no file.
- **Why:** brief 343 asks for a check of only what change.diff touched: that brief 338's findings are fixed or rightly stated as limits, that brief 342 changed no rule's meaning, and that nothing else became false or steerable.
- **Verified:** by reading only; I ran no command. I read the diff's E-004 hunks in full (:5, :39, :67, :100, :102, :151) and its S-002 hunks at :10, :46, :109, :190 to :192, :235, :267 and :268 in full, both sides; the changed parts of S-002.md:110, :112 and :197 by searching the current file and the copy at 50de6a7 for the changed passages; both decision records; the re-read record; memo 5 :9 and :137; and brief 338's section of reviews/S-002/plan.md (:623 to :682).
- **Undone:** I did not read S-002.md:110 and :112 end to end in the diff (each is too long to read whole with my tools); I read every passage the briefs changed in them by search, so a change in those two lines outside the passages briefs 341 and 342 name would be missed. I did not confirm commits 9c9a855 and d231a51 (finding 3), nor research/Q-018-extract/sample.jsonl lines 67 and 60 or reviews/Q-018-recode-5/_critic-verbatim.md finding 16, which are outside my manifest and moved unchanged.
- **Needed outside my surface:** the Orchestrator confirms the two commit ids (finding 3) and, if a whole-line comparison of S-002.md:110 and :112 is wanted, runs a word diff of those two lines against 50de6a7. The Definer may take findings 1 and 2 as wording, or the Chief of Staff may carry them on the scenario card.
- **Open questions:** 1. The re-read's own open question stands and is now on record at S-002.md:268: whether a check record matched to a piece by its statement alone makes the plan it reviews the piece's work, which would send Personal-Org-Operating-Model #25's rows 92 to 99 back for re-reading. That is the owner's to rule, on the scenario card or before it. 2. Whether the unlisted fold (finding 1) should be on the entry and results cards in its own words, as E-004.md:151's last sentence implies, or only in the plan.

Files read: /home/user/wt/ml-answers/AGENTS.md; /home/user/wt/ml-answers/.claude/agents/critic.md; /home/user/wt/ml-answers/docs/briefs/343-critic.md, 341-definer.md and 342-definer.md; /home/user/wt/ml-answers/specs/S-002.md; /home/user/wt/ml-answers/experiments/E-004.md; /home/user/wt/ml-answers/reviews/S-002/plan.md (:623 to :682); /home/user/wt/ml-answers/decisions/questions/P-002-plan-stop-2.md and P-002-plan-written-by-piece.md; /home/user/wt/ml-answers/reviews/Q-018-later-work/_critic-reread-verbatim.md; /home/user/wt/ml-answers/research/Q-018-memo-5.md (:9, :137); /tmp/claude-0/-home-user/3bf22eb7-3034-5300-9273-72fad23a7eb4/scratchpad/before-343/change.diff, /tmp/claude-0/-home-user/3bf22eb7-3034-5300-9273-72fad23a7eb4/scratchpad/before-343/S-002.md and /tmp/claude-0/-home-user/3bf22eb7-3034-5300-9273-72fad23a7eb4/scratchpad/before-343/E-004.md.
