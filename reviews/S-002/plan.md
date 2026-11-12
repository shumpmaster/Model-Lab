Verdict: FAIL

The Critic's plan review of specs/S-002.md and experiments/E-004.md (P-002, M8 to M10), in a fresh session on a different model from the writer, the Definer. Round 1 (brief: docs/briefs/271-critic.md, at Model-Lab 51bc87c, read from a fixed copy): FAIL, eight blocking findings. Recorded verbatim by the orchestrator, session session_01QBwHGNPKhVy6fgoUjKtW6q, 2026-11-12. Correction to the brief: it said a FAIL stops work before another round; the stop rule's limit for plan rounds is three (docs/LESSONS.md LL-55; reviews/S-001/plan.md, FAIL at rounds 1 and 2 and PASS at round 3), so round 1's findings go back to the Definer, and round 2 counts as the second of three.

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
