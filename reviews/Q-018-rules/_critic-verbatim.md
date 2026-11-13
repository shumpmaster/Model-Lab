# The Critic's re-check of S-002's corrected counting rules on step 5's cases (brief 289)

*Recorded verbatim by the Orchestrator; the verdict file is reviews/Q-018-rules/critic.md. Brief 289 (docs/briefs/289-critic.md), on Model-Lab@d5adfae, the rules as corrected by brief 288 (commit 884858a). The Critic runs on a different model from S-002's writer (D-056) and apart from the Researcher.*

Verdict: FAIL

**In plain words.** Most of the corrected rules now give the result the records show. All six first-check cases from finding 1 come out right or very nearly so, the agent-comment rule fixes all 8 comments, and the U1 wording, the trailer short forms and the left-out records work on their cases. Four faults remain, and each gives a wrong result on a case I named:
- The first-check rule takes as "the piece's" any review record whose text mentions its number. That pulls in other pieces' reviews, and test-case numbers such as "#11". So Service-Desk #148 gets a FAIL from another spec's plan review, not the "undecided" the Definer reports.
- Personal-Org-Operating-Model writes many verdicts as `VERDICT: FAIL`. The rule only reads `Verdict:`, so PO#25's round-1 FAIL is lost.
- RT5's new field leaves out records it should keep. Any file name holding `gate` is dropped, which catches Service-Desk's questions about the desk's gate cards. The Discovery-8 tag drops a stop-rule ruling on ML#93's own work.
- RT4 says "read by when the ruling was given", but records date rulings only by day or "about". SD#341's record dates the answer after the commit that adds it, so RT4's new clause does not apply there.

All four go to the Definer, and each is a small fix. Nothing is irreversible.

**Self-implication (D-050):** I am flagging that findings 3, 5 and 10 below come from fixes my own step-5 check recommended (reviews/Q-018/_critic-verbatim.md, finding 4: "Treat a question file the piece itself changes as naming the piece"; "Give RT5 a field … a gate or value-target name"; finding 2's "A record found only of another kind gives undecided"). The Definer carried them out as asked. Where they over-reach, the root cause is in my earlier check.

## Findings

**1. Blocking. C1 "Which records are the piece's" (specs/S-002.md:59): matching a record by "names the piece by its pull request number" takes in other pieces' check records.**
- Unlike line 46, this clause sets no whole-word limit and says "any case". It also does not limit itself to records about the piece.
- SD#148: two plan-kind records name "#148" only as evidence:
  - /home/user/Service-Desk/reviews/S-001-desk-v2/_critic-round1-verbatim.md:32, `Verdict: FAIL` at :7
  - _plan-review-round1-verbatim.md:113, `Verdict: FAIL` at :7
  - Both are reviews of desk v2. By the rule, SD#148 is FAIL from another piece's plan review, not "undecided" as the Definer's return says.
- SD#52 takes in:
  - SD#78's round-1 build review (reviews/S-001-trial-view-2/_build-review-round1-verbatim.md:23, "PR #52")
  - reviews/287/_reviewer-r1-verbatim.md:55
  - a test case, "ac85 #52" (S-001-desk-v2/_build-4-review-round2-verbatim.md:33)
  - reviews/300/reviewer.md:23
- SD#11 takes in reviews/245/reviewer.md:25 and M3G/_stage-qw2-review-r1-verbatim.md:26, where "notify-ac77-desk #11" is a test case.
- Going the other way, SD#52's own record (reviews/52/reviewer.md:3, "PR #54") would give SD#54 a round-1 FAIL that is SD#52's.
- Fix: match by text only for a record that says it reviews the piece (for example "Reviewed: PR #n", or a heading naming the piece), or drop text matching. Then make the rest of the clause whole-word.

**2. Blocking. C1 verdict wording (:60): `VERDICT:` in upper case is not read.**
- Personal-Org-Operating-Model has more than 40 such records, among them reviews/S-022/_plan-review-s022-round1-verbatim.md:5 "VERDICT: FAIL".
- PO#25's plan (Spec S-022, extract line 15) therefore gets no round-1 verdict by (i). Rounds 2 to 5 give none either, so the rule says "undecided" where the record shows FAIL.
- Fix: read `Verdict:` in any case.

**3. Blocking. RT5's field (:51) catches records outside RT5's own definition ("a phase gate, a value target").**
- (a) "its name holds `gate`" is a substring test. It drops Service-Desk product questions about the desk's gate cards:
  - decisions/questions/P-001-gate-card.md (Milestone MD2)
  - P-001-gate-buttons.md (MD2)
  - P-001-glance-waits-gates.md (M3E)
- (b) The Discovery-8 tag drops P-002-brief-stop.md (:1 "one focused last check", :4 Discovery-8). That is a stop-rule ruling on ML#93's own work, not a gate ruling. P-002-research-stop-3.md, a stop-rule ruling of the same sort tagged Discovery-5 (:4), is still counted.
- Fix: match a gate by a named gate (`design-gate`, `build-gate`, `launch-gate`, whole words) and `value-target`. Do not drop a stop-rule ruling for its milestone tag (see question 3c).

**4. Blocking. RT4 (:50) against RT1(a)'s commit timing (:47).**
- The clause "read by when the ruling was given, not by when its record was committed" reads as general. The records date rulings by day or "about":
  - SD#341: /home/user/Service-Desk/decisions/questions/P-003-check-author-scope.md:10 dates the answer "at about 13:53Z". The first commit that adds it is 13:52:33 (sample.jsonl line 28). So "a ruling given before that commit, as the record dates it" does not hold, and RT4's clause does not apply.
  - Whether the window includes its start (U1's original question) is still not said. So SD#341 comes out a touch or undecided, where the records show its starting ruling.
  - SD#26: P-001-o6-define.md:4 dates only the day, "2026-10-04", the same day as dispatch at 15:46:35.
  - SD#78: the appends to P-001-trial-view-notes-2.md are dated only "2026-10-16", the same day as dispatch at 11:54:38. Read by "when given", none of them can be placed.
- Fix: a record first added in the piece's first commit is the starting ruling (RT4). Every other record and append is timed by its commit, and the window excludes its start.

**5. Non-blocking (self-implication). Own-file naming (:46) over-counts pieces that only file questions about other work, and it clashes with RT4's "a question about another piece".**
- SD#237's 5 question files are about the M3G picture, not #237. My finding 7 said so.
- ML#29 counts P-001-accept-m1.md (filed in PR #29, :4), a milestone mark that is not about the gate-case piece.
- Meanwhile its one real touch (open-unknowns) is dropped by RT5.
- The rule does not say which wins when a record names the piece and is about another piece. This goes with open question 11.

**6. Non-blocking. PO#24.**
- The heading is "## Round 1 (a6b4f40): Verdict FAIL. Summary by the orchestrator…" (reviews/24/reviewer.md:77). The verdict does not *end* the heading.
- Under it, "The round-1 verdict was FAIL" (:79) is not a listed wording.
- Read literally, the rule gives nothing, so PO#24 is undecided. Intended, it is FAIL. Fix: "a verdict in the heading".

**7. Non-blocking. (i)'s "`round1` or `r1` in its name" also matches round10 to round16 and r10 to r14.**
- Examples: PO reviews/S-023/_plan-review-s023-round10…16, S-024 round10…12, and Service-Desk reviews/M3B/_plan-review-r10…r14.
- Fix: round1 or r1 as a whole name part.

**8. Non-blocking. Service-Desk's folder list (:58) leaves out topic folders.**
- SD#148's own Reviewer rounds are in reviews/design-reviewer-setup/ (_review-round1-verbatim.md:1 "Pull request #148…").
- That folder is neither on the list nor "listed as unclassed".

**9. Non-blocking. The new U labels clash with S-002's own.**
- C1 and RT1 now use "(U2)", "(U3)", "(U4)" and RT4 uses "U1" in Q-018 memo's sense.
- S-002 already uses U1 ("U1's fallback", :47, :80) and U3 (:32, and step 4's gloss of U3, :108) for the project's unknowns.
- The quoted research question would carry the clash.

**10. Non-blocking (self-implication in part). Which file or version is read.**
- RT5 reads a `Milestone:` line. ML#29's decision record P-001-open-unknowns.md has none (:1-3), and its question file was deleted by the piece. The Definer's "Discovery-8" for it must come from the deleted file. The rule does not say which governs.
- "names the piece" likewise does not say which version of a record is read. SD#148's q 552be005 named #148 by number, but no current question or decision record in Service-Desk does.

**11. Non-blocking. The rest of the spec has not caught up.**
- Step 5 (:109) still reads "every owner comment counted under RT1(b)", against the new E-RT5 row (:101).
- Step 3's fields (:107) lack comment authorship, appends, the Milestone line and the Critic's registration check.
- Step 4's glosses are not updated. The Definer reports the last two as undone.

**12. Non-blocking. E-K2's filter now means something else.**
- Its text is unchanged (:95), but with K2's short forms SD#36 (`-def-`) and PO#20 (`-tb-`) no longer match it.
- The widened extract must re-code the sample as drawn, not draw it again. Say so.

**13. Non-blocking. Smaller gaps.**
- The agent footer is "such as". The footers should be listed.
- "A repository whose agent comments carry the footer, as the Critic's reading shows" has no answer for Model-Lab, where no comment was read.
- One line can report two kinds of check (PO reviews/20/reviewer.md:4, plan "FAIL rounds 1 to 4" and "Build review: round 1 FAIL"). "Only its lines for the piece's kind" cannot split it. The result is the same here.

## 1. The cases, against the records

**Finding 1 (C1 rounds):**
- **SD#11: FAIL, right.** reviews/11/reviewer.md:3 "Round 1 at 30f5205: FAIL", read by (iii). The records the rule wrongly takes in (finding 1) pass, so the result does not change.
- **SD#52: FAIL, right.** reviews/52/reviewer.md:5. Other pieces' FAILs are also taken in (finding 1).
- **SD#78: FAIL, right if #78's head branch is orch/trial-view-2.**
  - That branch is named at S-001-trial-view-2/_build-review-round1-verbatim.md:3 and :8, whose `Verdict: FAIL` is at :1.
  - The extract holds only a label for the branch, so I could not confirm it.
  - reviews/78/reviewer.md alone gives no round-1 verdict: "**Round-1 findings…**" (:21) is bold text, not a Round 1 heading, and (iv) is ruled out by round 2.
- **PO#18: FAIL, right** (:3).
- **PO#27: FAIL, right.** The table at :9-14 has a Round 1 column with Verdict "FAIL (B1)". "### Round 1 findings" is rightly not a Round 1 heading.
- **PO#20: FAIL, right** (:4, but see finding 13).
- **PO#24: undecided as written, FAIL as intended** (finding 6).
- **PO#50: PASS, right.**
  - (ii)'s "## Round 1" (:5) gives no wording. The top-line verdict counts under (iv), since the record names only round 1, reading (i) to (iv) as a fall-through, which the rule should say.
  - reviews/S-037/_build-review-round1-verbatim.md:5 also gives PASS (Spec S-037, extract line 39).

**Finding 2 (C1 paths, U2 and U3):**
- **ML#73: FAIL, right** (Q-009-source-check.md:5,7).
- **ML#81: FAIL, right** (Q-015 and Q-016 source checks, :5,7).
- **ML#78: left out and listed, right.** Its only research files are entries checks, and it has no other record.
- **ML#93: undecided, right.**
  - reviews/93/reviewer.md is a build review.
  - reviews/P-002-design-gate-brief/critic.md and P-002-m7-line/critic.md are of another kind.
  - There is no plan review.
- **SD#148: wrong record** (findings 1 and 8).
- **PO#47: FAIL, right.**
  - The extract shows no Spec trailer (line 36).
  - The piece changes specs/S-036-check-run-copy.md: "Round 3 followed", as its reviewer.md:44 describes.
  - That makes reviews/S-036/_plan-review-round1-verbatim.md:5 "Verdict: FAIL" the piece's.
- **PO#25: wrong, undecided where the record shows FAIL** (finding 2).
- **SD#300: FAIL, right.** reviews/EXP-007/_critic-r1-verbatim.md:9, the Critic's check of the registration, experiments/EXP-007-widget-refresh.md. Its reviews/300/reviewer.md is of another kind.
- **ML#98: left out, right.** The record is after the cut-off.

**Finding 3 (RT1(b)):** right, 0 of 8 counted.
- This rests on the footers as read in brief 287.
- The session records also show the Reviewer's comments were posted by sessions: SD reviews/11/reviewer.md:3 and PO reviews/18/reviewer.md:3 ("Returns: the reviewer comment(s) on PR #n").
- I could not read the comments again.

**Finding 4 (RT1(a)):**
- **SD#78's appends: right in kind.**
  - The record is the piece's own file. It holds `Answer:` lines (:9, :46-49) and quoted lines under "The owner's answers… verbatim" (:18-19).
  - The count needs the extract to diff each commit, and it falls under finding 4's timing problem.
- **SD#148's board scope: still missed, as the Definer says.** P-001-board-scope.md names only MD2 (:3).
  - Most of #148's roughly 22 MD2-only records now drop too. No current question or decision record names #148.
- **SD#26: partly right.**
  - The notes file 1d370480 is out, which is right.
  - P-001-o3-define counts at 16:11:10 by the literal clause.
  - But O3 and O6 were both "asked in the session on 2026-10-04" (o3-define.md:4; o6-define.md:4), so read by "when given" it cannot be placed (finding 4).
- **ML#13: 0, right.** No shared-path matching. P-001-milestones-m2-runs-critic.md holds no owner words (:1-5).
- **ML#29: wrong** (findings 5 and 10).
- **ML#92: trial-gates is out by RT5**, Discovery-2 (:4). Right as RT5 reads.
- **ML#93: brief-stop is out** (finding 3).
- **The other own-file cases:**
  - SD#230: counts 4. That is open question 11.
  - SD#237: counts 5, which is wrong.
  - ML#73 (groundwork-shortlist) and ML#81 (research-stop-3): right.
  - PO#49 and SD#300: not checked against the text.

**Finding 5 (U1):**
- **SD#78: right.** The note is dated 10-16 with a 06:49 screenshot, before dispatch at 11:54:38.
- **SD#26: undecided as written**, because it is dated by day only.
- **SD#341: wrong as written** (finding 4).

**Finding 9 (K2 short forms):**
- SD#36 `-def-` gives Definer, so plans. PO#20 `-tb-` gives tools-builder, so built work. Both right, and the same as before.

## 2. Can the corrected rules be coded from the records alone?

Not yet. The ambiguities are findings 1, 2, 4, 5, 6, 7, 9, 10 and 13.

Owner words can be coded, but only if the extract diffs each commit's added lines. That field is not yet in step 3.

## 3. The Definer's four open questions

**(a) Leaving Service-Desk's S-001 out of naming a piece: a sound rule, not the owner's choice.**
- Without it, any record citing S-001 would name almost every Service-Desk piece.
- A more general form would also hold for later counts: "a spec id in the `Spec:` trailers of more than one piece under way at the same time names none". The Definer may choose either.
- Either way, milestone-only questions (E-RT4) become Service-Desk's main gap.

**(b) SD#148 "undecided" on C1: first a fault in the rule, then a choice for the owner.**
- The rule as written does not give "undecided" (finding 1). Its own Reviewer rounds are outside the listed folders (finding 8).
- C1 already allows "the Reviewer's" plan review in the other two repositories, but file names (`_review-round<n>`) class those rounds as build reviews. That clash is the Definer's to settle.
- Then the owner chooses:
  - (i) Strict: only the check of the piece's kind counts, and the rest are undecided and listed.
  - (ii) Fallback: when no check of the kind exists, the piece's only independent check before merge counts. SD#148 would then be FAIL from design-reviewer-setup round 1. ML#93's review came after merge, so it stays undecided.
- In trials, the kind is fixed at dispatch, so this affects only the hand check and the starting figure.

**(c) RT5 putting every Discovery-8 record outside the count: partly a fault, partly the owner's choice.**
- The fault (Definer): stop-rule rulings (brief-stop) and gate-named product questions fall outside RT5's own definition (finding 3).
- The choice (owner, inside Open question 3): is a definition-of-ready ruling before the Design gate a gate ruling? P-001-open-unknowns is one: "the owner's own answer, never a default" (:3).
- Options:
  - (i) Gate and value-target rulings only, by name. Every other Discovery-8 ruling counts.
  - (ii) Definition-of-ready rulings stay out with the gates.
  - (iii) Keep the field and list each excluded record for the owner.

**(d) SD#148's board-scope answer still missed: a choice for the owner under E-RT4, not a fault in the corrected rule.**
- Options:
  - (i) Keep it missed, and on record as something the rules cannot catch.
  - (ii) The Definer adds the reverse citation: a question record whose path the piece's own commits cite, inside the window, names the piece. This would likely catch it through governance/domains/design/README.md, which cites P-001-board-scope. I did not check that #148 added that citation.
  - (iii) Count a milestone-only question on every piece of that milestone under way at the time. This over-counts pieces running side by side.
- Finding 7 of brief 287 shows that MD2-only questions were mostly about #148.

## 4. Nothing else changed

The diff has three hunks:
- lines 31 to 54
- the E-RT5 row (101)
- open questions 10 and 11 (251, 252)

Unchanged:
- K1, K3, K4, RP1, RP2, RT2, RT3, RT6, RT7, RR1 to RR3
- the window, frames, draw, seed and cut-off (:84)
- every sampled filter row (:88-99, :104)
- the status line

The E-RT5 row is a check the Critic does, not a draw filter. It widens step 5, and step 5's text does not yet match (finding 11).

E-K2's filter changes in meaning, not in text (finding 12).

I could not confirm that commit 884858a changes only S-002, because I was given only the S-002 diff.

## Six-part contract
- **Changed:** nothing. I hold no write tool.
- **Why:** brief 289, the re-check of S-002's corrected rules on step 5's cases (P-002, M8).
- **Verified:** with Read, Grep and Glob:
  - the S-002 diff, specs/S-002.md:1-110 and :236-256
  - reviews/Q-018/_critic-verbatim.md and docs/briefs/288-definer.md
  - research/Q-018-memo.md §2 and §4
  - research/Q-018-extract sample.jsonl and M.jsonl (dispatch times, spec trailers, labels)
  - Service-Desk: reviews 11, 52, 78, 148, 245, 300; S-001-trial-view-2; S-001-desk-v2; EXP-007; design-reviewer-setup; decisions P-001-trial-view-notes-2, board-scope, o3-define, o6-define, gate-card, gate-buttons, glance-waits-gates, P-003-check-author-scope
  - PO: reviews 18, 20, 24, 25, 27, 47, 50; S-022, S-036, S-037; a case-insensitive grep for verdict lines
  - Model-Lab: research Q-009, 012, 014, 015, 016 source checks; reviews/93 and its other naming records; decisions P-001-open-unknowns, accept-m1, milestones-m2-runs-critic and the P-002 gate, stop and value records
- **Undone:**
  - I have no git, so I could not check commit times, messages or hashes (0c40cd7c, 233211a9, 8e21866a and others) beyond the extract, or SD#78's head branch.
  - I could not re-read the PR comments.
  - I did not check the text of PO#49's and SD#300's own question files.
  - I could not see the deleted questions/P-001-open-unknowns.md.
  - I could not confirm that commit 884858a touches only S-002.
- **Needed outside my surface:**
  - The Definer: findings 1 to 4 (blocking) and 5 to 13, then a Critic re-check of those cases only.
  - The Orchestrator: extract fields for comment authorship, the owner-word lines each commit adds, each record's `Milestone:` line (including deleted question files), the check-record path list, and SD#78's head branch.
  - Triage: note the self-implication on findings 3, 5 and 10.
- **Open questions:** for the owner, 3(b)(ii), 3(c) and 3(d) above, with open question 11.

Key paths: /home/user/Model-Lab/specs/S-002.md, /home/user/Service-Desk/reviews/S-001-desk-v2/_critic-round1-verbatim.md, /home/user/Personal-Org-Operating-Model/reviews/S-022/_plan-review-s022-round1-verbatim.md, /home/user/Service-Desk/decisions/questions/P-003-check-author-scope.md, /home/user/Service-Desk/decisions/questions/P-001-gate-buttons.md, /home/user/Model-Lab/decisions/questions/P-002-brief-stop.md