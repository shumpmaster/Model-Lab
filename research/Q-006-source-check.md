Verdict: FAIL

Memo: /home/user/Model-Lab/research/Q-006-memo.md. Read-only check; I wrote no files and did not open the forbidden paths. Most citations hold. The memo fails on three things:
- The "7 of 17 past three rounds" figure and the "one item has no recorded pass" claim do not reproduce.
- "A model is named in 1 of 330 round files" is wrong: it is 2.
- The §0 item 3 claim that no checker blamed a brief overstates what the M3C Triage says.

Counts below are my own, from scripts over dispatch-log/2026-10.jsonl, reviews/*/_control/*.json and reviews/**/_*.md. Paths are relative to /home/user/Service-Desk.

| Item | Claim | Source | Result | Note |
|---|---|---|---|---|
| 1 | Log has 263 entries; last is :263 at 2026-10-08T21:52:08Z; 104 dispatch lines | dispatch-log/2026-10.jsonl | Confirmed | Only one month file exists. 104 is a count (grade B), not a read-off (A). |
| 2 | 12 research items checked; 2 passed first time (Q-008 :135, Q-013 :262) | same | Confirmed | I count 12 items. Q-003 never reached a check. |
| 3 | 41 source-check outcomes: 32 FAIL, 9 PASS; mean 3.4; median 3 | same | Confirmed | I get 41/32/9, mean 3.42, median 3. 41 is logged outcomes. Control records show 33 source-checker sessions, i.e. 32 matching a logged outcome plus one extra for Q-006 (see item 11). |
| 4 | 9 of 12 passed in the end; cited lines; 3 dropped (Q-009, Q-010, Q-012 at :160, :225, :257) | same | Confirmed | All cited lines match. |
| 5 | Q-006: 7 checks, 6 researcher returns, 2 Triages, 2 owner cards | :87-136 | Confirmed | Checks at :90, :94, :98, :104, :112, :120, :133. Returns at :88, :92, :96, :110, :117, :127. |
| 6 | P-001: DoR failed 3 times (:84, :116, :162), Triage :164, pass :168; Definer errors :171-174; plan review FAIL ×3 (:180, :184, :188); Triage :190; re-scope :192 | same | Confirmed | Error durations are 5h29m and 3h51m, as stated. |
| 7 | 10 Triage dispatches, all verdict "none"; 15 cards and 15 decisions; 5 by proxy; word tally (drop 4, re-specify 3, resubmit 3, confirm 2, build 1, retry 1, re-scope 1) | same | Confirmed | All tallies reproduce. |
| 8 | 37 of 104 dispatches have no control record; 67 have one | dispatch log against reviews/*/_control | Confirmed | I match by item, role and dispatch time: 67 matched, 37 not. The 37 are P-001 14, Q-009 7, Q-010 7, Q-012 7, Q-003 2. There are 69 control records in all; the 2 without a dispatch line are Q-006 01:25:01 and Q-013 21:36:11. |
| 9 | The three revisions at 2026-10-01T09:15:57Z had no memo in their pack; all three re-checks failed (:34-36); later packs held the memo | Q-001/_control/0-bcdb1d743941.json, Q-002/_control/1-d048b87ce06f.json, Q-004/_control/2-7da710f0b27a.json | Confirmed | Briefs say "Revise your memo". Packs hold the question and source check only. Later revisions (11:28:52 and after) include the memo. Q-001 and Q-004 then passed (:50, :52). |
| 10 | Q-005: memo hash 766515… at the third check (14:48:25, FAIL :67) and the confirmation check (16:23:47, PASS :79), no researcher between | Q-005/_control/1-fe151d6987ac.json, 1-218e36411c3b.json | Confirmed | The packs differ in more than the question. The source-check file hash differs too (381b… against f528…). The memo mentions only the question. Between the two checks there is a Triage (:69) and an owner "confirm" (:75). |
| 11 | Two sessions ran with no dispatch line, and the log flags an anomaly each time | :119-121, :258-261 | Partly confirmed | The undispatched sessions are Q-006 01:25:01 and Q-013 21:36:11, as stated. The anomaly lines name the neighbouring sessions (01:28:40 and 21:42:17), which do have dispatch lines. So Q-006 had 8 source-checker sessions but 7 logged outcomes. |
| 12 | Scripted briefs and models are recorded; one model pairing (researcher opus-5-5; source-checker and Triage sonnet-5-5) | control records | Confirmed | Counts: 31 researcher, 33 source-checker, 5 critic-triage controls, all as stated. Cited lines :3, :53-60, :51, :54, :60, :116 all match. |
| 13 | Pack changed during the week: template source-checker pack excludes the question (PACKS.toml:60-61); Q-001 checks lacked it; Q-006 checks had it | POOM PACKS.toml; control manifests | Confirmed | Checks from Q-002 15:52 onward carry the question; earlier ones lack it. |
| 14 | Triage briefs say "Feedback from earlier rounds: none" while the pack holds the source check (:101-113) | Q-006/_control/0-6c728513a012.json | Confirmed | |
| 15 | 330 round files carry a column-0 Verdict:, 147 FAIL / 183 PASS; 149 files contain a FAIL line; the two M3D files named have a first PASS | reviews/**/_*.md | Confirmed (B) | 341 `_*.md` files; 330 have a Verdict line. I get 147/183, and 149 files with any FAIL line. The cited M3D line numbers (:10/:45, :22/:62) match. The README rule ("first column-0 Verdict decides") supports the method. Minor: I count 587 files under reviews/, the memo says 586. |
| 16 | Plan items: 17; 1 passed all checkers at round 1 (HD1); 2 of 29 series | reviews/*/_plan-*, _critic-* | Confirmed (B) | I get 17 items, 29 item-checker series, and only HD1's two pass at round 1. The 17 includes S-001-desk-v2, which a truncated directory listing hides. |
| 17 | Plan rounds to a pass: 16 values (1,2,2,2,3,3,3,3,3,3,4,4,4,6,8,14), median 3, mean 4.1; "7 of 17 went past three"; "one item has no recorded pass" | same | Not reproduced | I get 15 items with a recorded pass: 1; 2,2,2; 3×6; 4,4; 6; 8; 14. This counts the trial-view-2 focused recheck as round 4. Median 3 reproduces, mean 4.07, range 1–14 reproduces. Two items have no pass, not one: S-001-notifications (plan review r4 FAIL, Critic r6 FAIL) and S-001-desk-v2 (Critic and plan review r1–r3 all FAIL, builds exist). Items past three rounds: M3B, M3C, M3G, records, notifications, plus trial-view-2 if the recheck counts. That is 5–6, not 7. I cannot identify the memo's 16th value, a 4. |
| 18 | Build stages: about 15 of 50 first-pass; M3E 8 of 15; desk-v2 0 of 10; rounds 1–5, VT3 reached 5 | reviews/**/_stage-*, _build-* | Approximately confirmed (B) | By my method I get 41 stage units with 15 first-pass. That includes M3D 3, 3-4-5 and 6b, which have only one checker file each. Adding 9 non-stage build series (1 first-pass, followups) gives 16 of 50. Excluding the three partial M3D units gives 13 of 47. M3E 8/15 and desk-v2 0/10 reproduce exactly. About 30% holds. M3B VT3 r5 is at :3 as stated. |
| 19 | Series past the stop rule: M3B 14, M3G 8, sync 7, records 6, design-reviewer-setup 6, VT3 5, M3D 6a 4; stop rule at POOM OPERATING_MODEL.md:203-206; spec draft notes cite an owner ruling at specs/S-001.md:600-602 | reviews; POOM; specs | Partly confirmed | The listed counts and citations are right. The list is incomplete: M3C (4 plan rounds), S-001-notifications (Critic 6, plan review 4) and trial-view-2 (3 plus recheck) are also past three. |
| 20 | Cause-sample table: 13 FAIL rounds, 24 blocking findings, per-kind counts | the 13 cited round files | Confirmed | Blocking counts: M3B r1 5, r7 1; VT3 r2 1, r4 1; M3C r1 3; records r1 1, r4 1; HD1 r1 1, r2 1; sync r1 1, r6 1; design-reviewer-setup r1 4; desk-v2 1a r1 3. Total 24, and the §5 table sums to 24. Cited line ranges match. Quotes at 253/reviewer.md:112, M3C triage :9 and :21, and sync r6:15-21 all match. |
| 21 | §0 item 3 kinds list: plan 6, criteria 4, frozen 3, "inputs 3, plus 1", wrong facts 2, owner questions 2, descriptions 2 | §0 against §5 | Internally inconsistent | The §5 table has Inputs 2 plus owner-answer gap 1, plus untestable checklist 1 and fix-fault 1. §0 gives "3, plus 1" and omits the last two, so its items sum to 23, not 24. |
| 22 | §0 item 3 and §5: "None of the 24 was blamed by its checker on the brief" | M3C/_triage-r3-critic-verbatim.md:9, :21, :45 | Overstated | The Triage calls M3C r1 B3 "a brief or orchestration gap". It names as root cause that the Definer "got none of the rules" and recommends "write a fresh brief". The memo's own §5 row marks this "untraceable between told and inputs", which contradicts the §0 sentence. |
| 23 | §5: "In every PASS-then-FAIL reversal I opened, the FAIL followed a new draft" (also behind P-q006-02) | M3B/_stage-vt3-review-r3 → r4 | Contradicted | VT3 r3 is PASS and r4 is FAIL. The FAIL followed a Builder fix commit (4f509ed), not a new draft. The memo opened VT3 r4 and counts it in the table. I find 11 PASS-then-FAIL pairs across the series; the memo opened a few. |
| 24 | §5 example: contradictions "sit far apart" (:13574 against :13606) | M3B/_plan-review-r1:21-23 | Misleading | :13574 and :13606 are 32 lines apart. The :11002 against :12773 example is far apart. |
| 25 | §6 and F-q006-04: model named in 1 of 330 round files | reviews | Wrong | Two files name it: S-001-desk-v2/_build-1b-review-round1-verbatim.md:13 and _build-1b-review-round2-verbatim.md:11 ("Session: Opus 5.5"). Also: 239 files begin "Dispatched by the orchestrator" (confirmed). "About 90 S-001-* files have no header" is 82 of 154 by my count. |
| 26 | §7 absent records (Q-009/10/12 memo, source-check, triage; triage/P-001; reviews/P-001/_critic-dor.md; reviews/S-001/plan.md; docs/reports/P-001-definer.md); Q-014/Q-015 memos exist with no dispatch lines | file existence | Confirmed | triage/Q-006 and Q-002 exist. Q-014 and Q-015 are in research/ and not in the log. |
| 27 | §7 round-file gaps: M3D 6a r2-3 missing; trial-view-1 build r1 only; design-lab-answers builds r1-2 FAIL; M3E g1 r2 after two PASS; M3B r12 re-reviews draft 11 at a new commit; stray reviews/reviews/40/owner.md | reviews | Confirmed | M3B r11 (a7c8e1d) and r12 (7c9bfdb) are both draft 11. |
| 28 | Session file: 15 helper lines, 10 with null tokens (:2-10, :13); end usage null (:17); 12 checker helpers match 12 round files; two later starts with no helpers (:18-19) | sessions/chief-of-staff/session_012RJPVKAoLga2RkqLYRDcBY.jsonl | Confirmed | Imprecision: the Definer helper at :5 (22:42 to 00:55) overlaps about ten later helper lines, not "three". |
| 29 | Checker-assigned cause (§5) follows the §2 method | §2 against §5 | Mostly follows; five rows do not | Rows that do not (see "Cause-class check" below). |
| 30 | Brief-error notes and checker admissions (HD1 :63, :52; qw3 :11; vt1 :60; sync r2 :35; M3B plan-critic r2 :43; m3a critic r2 :34-36 / r3 :9; desk-v2 and sync admissions; surface_guard notes) | cited files | Confirmed | All spot-checked lines match. |

Cause-class check (§2 requires: checker named the cause, or a record shows it directly; otherwise "doer by default" or untraceable)
- Follow the method:
  - HD1 r2 and VT3 r2 → Inputs (checker words at 253/reviewer.md:112, and "with draft 13 merged" at VT3 r2:3, :9). Nuance: the HD1 r2 checker says draft 3 landed "on another branch".
  - desk-v2 1a → Doer.
  - HD1 r1 → Doer.
  - VT3 r4 → Doer (the fix).
  - M3C B3, M3B B3 and M3C B2 → Untraceable.
- Do not follow the method:
  - design-reviewer-setup r1 #1 and #4 → "Inputs". The checker names no cause and no pack list is recorded. #1 is the doer's own list being incomplete.
  - sync r1 and r6 → "Division". No checker names that cause. The checker says only "how this description told the story". Also, R1 (test change omitted) and R2 ("Nothing failed" claim, which pre-dates any review, per r6:7) are not about the description's account of its own reviews. Only R3–R6 fit "narrates its own reviews".
  - M3B r7 B1 → "Inputs (moving target)". The finding is a plan self-inconsistency (a fifth mark with no counted part). The record shows only a new draft, not a cause.
  - records r4 #1 → "followed an owner answer". The record shows the draft contained the owner answer, but nothing says that caused the missing test.
  - "Doer, by default" is not one of the six classes; it only appears as the §2 fallback.

Conclusions resting on a figure that failed
- §0 item 2 and §8 "7 of 17 went past three rounds": does not reproduce (5–6). The §4 line "One item has no recorded pass" should say two items. The ranking (plan most rework, then research) still stands on figures that reproduce: first-pass 1/17, 2/12, about 30% for build. It is confounded across paths and record forms, as the memo says.
- §0 item 3, "none blamed on the brief", conflicts with the M3C Triage and with the memo's own §5 row. The conclusion "content, not obedience to instructions" needs softening.
- §0 item 3's category list does not sum to the table (see item 21).
- Anything citing "1 of 330" model-naming (§6, F-q006-04, §9): the figure is 2.
- P-q006-02's generalisation ("reversals followed redrafts") is contradicted by VT3 r3→r4.
- P-q006-03's account ("every finding about the description's own review history") fits only R3–R6.
- The grade A labels on counts: F-q006-02 is a count the memo's own rules grade B. F-q006-01's 104 is also a count.

Proposed library entries (not filed; I was told to write no files)
- F-q006-01 (log covers 2026-10-01 to 10-08, 263 entries, 104 dispatches): may be filed. Change the grade to A for the span and entry count and B for "104".
- F-q006-02 (2 of 12 first pass; 41 checks, 32/9; 3 dropped; 10 Triages unchecked): may be filed after one change. Grade it B, not A, and say "41 logged outcomes". Add line refs (:135, :262, :160, :225, :257). Optionally note that Q-006 had an extra source-check session (01:28:40) whose outcome the log ignored.
- F-q006-03 (37 of 104 dispatches lack a control record; the records of closed or dropped items are absent): may be filed. Grade B. The cause (pruned on close) must stay unstated, as it is now.
- F-q006-04 (conversational path records neither brief nor model): not as proposed. Change "1 of 330" to "2 of 330" (both in S-001-desk-v2 build-1b). Change "neither … nor model" to "almost never the model".
- F-q006-05 (Q-005 hash-identical memo: FAIL then PASS): may be filed with one addition. Say the packs also differed (the question added; a different source-check file) and that an owner "confirm" (:75) and a Triage (:69) came between. Without that it reads as pure checker variance.
- F-q006-06 (three revisions without the memo; three re-checks failed): may be filed as proposed (grade A; the causal link stays an estimate). It rests on the manifest listing only.
- F-q006-07 (plan 1 of 17, median 3, "7 of 17 past three", M3B 14, build about 15 of 50): not as proposed. Remove or correct "7 of 17" (mine is 5–6). Keep 1 of 17, median 3, M3B 14. Say "two items have no recorded pass". State the build figure as 13–16 of 47–50 with the method.
- F-q006-08 (PR verdict files from about #220 duplicate the series' round files): may be filed, but only the HD1 example is checked (reviews/253/reviewer.md rounds 1–3 appear verbatim in the HD1 round files). Word "from about #220" as "for example". The header counts (the "## Round" lines) fit the pattern but I did not compare each pair.
- P-q006-01 (records of failed work vanish): not as proposed. The condition "work items are pruned on close" is not established; the memo's own §10 Q2 asks whether it is. Reword it as "records of closed items are absent; cause not established". Grade the principle C.
- P-q006-02 (a new draft reopens review): not as proposed. M3B r6→r7, records r3→r4 and VT3 r1→r2 support it. VT3 r3→r4 followed a Builder fix, not a draft. M3B r7 B1 and 253/reviewer.md:112 are not clean examples of it. Narrow the claim to "some", or add the Builder-fix case.
- P-q006-03 (self-referential description): not as proposed. The 6 FAILs are right (r1–r6, r7 PASS), and all six blocking findings concern the description. Only R3–R6 concern its account of the reviews; R1 and R2 do not. Correct the account, and file at B or C.
- P-q006-04 (re-checking identical work tests the checker): may be filed only as grade C and only if it records that the Q-005 pack was not held fixed (item 10). Otherwise hold.

Files read: /home/user/Model-Lab/research/Q-006-memo.md, /home/user/Model-Lab/research/Q-006.md, and in /home/user/Service-Desk: dispatch-log/2026-10.jsonl, reviews/** (rounds, 69 control records, README.md), sessions/chief-of-staff/session_012RJPVKAoLga2RkqLYRDcBY.jsonl, specs/S-001.md:578-610, research/ and triage/ file lists; in /home/user/Personal-Org-Operating-Model: OPERATING_MODEL.md:196-210 and template-v3/governance/PACKS.toml:50-70.

---

## Round 2 — focused confirmation on the revised memo (recorded verbatim)

Verdict: PASS

Confirmation of /home/user/Model-Lab/research/Q-006-memo.md after revision. I checked only the items I raised. I wrote no files.

**Findings**

- **The desk-v2 point: the Researcher is right and I was wrong.**
  - /home/user/Service-Desk/reviews/S-001-desk-v2/_confirmation-draft4-verbatim.md is a fresh Reviewer's check of draft 4. It was run under the owner's answer A ("a fresh reviewer checks only those fixes; then building starts").
  - It has `Verdict: PASS` at :7. My earlier script missed it because its file name did not match my pattern.
  - So the plan items with a recorded pass are 16 and only S-001-notifications has none. This is the original memo's 16-value list, with desk-v2 at 4.
  - I re-ran the numbers on that basis.
    - The median is 3 and the mean is 4.06 (65 over 16).
    - "More than three check dispatches by one checker" gives 7 of 17: M3B, M3G, records, notifications, M3C, trial-view-2 and desk-v2.
    - Without focused, recheck and confirmation checks it gives 4 of 17: M3B, M3G, records, notifications.
    - Both figures hold, and the memo states the counting rule (§4 Method and stop-rule list).
  - Item 17 is resolved.

- **Item 18, build estimate: holds.**
  - The memo now gives the method and the units. Its pass list is 12 stage-unit passes plus followups, LA2 and `_reviewer-build`.
  - That matches my 12 stage-unit first-passes (M3E 8, M3B vt2, M3D 1 and 8, M3G qw2) plus followups. I confirmed `S-001/_reviewer-build.md` begins PASS.
  - Result: 15 of 50, with sensitivity 13 of 47 to 17 of 52.

- **Item 19, past-the-stop-rule list: holds.** It now includes M3C 4, notifications (Critic 6, plan review 4), trial-view-2 4 and desk-v2 4. It also gives desk-v2 1a design and review at 4.

- **Item 10, Q-005: holds.**
  - I checked every hash and line the memo now cites.
  - BRIEF.md differs: 074d1f… (fe151, :55) against 16ef73… (218e3, :55).
  - The pack also differs in the source-check file (:84/:86) and in three added files: sources.md (:57), a library fact (:83) and the question (:87).
  - The Triage (:69) and the owner "confirm" ruling (:75) sit between the two checks.
  - F-q006-05 and P-q006-04 now say the pack was not held fixed.

- **Items 21 and 22: fixed.**
  - The §0 kinds list now sums to 24 and matches the §5 table.
  - The M3C Triage's "brief or orchestration gap" and its recommendation of a fresh brief are stated as an exception to "no reviewer blamed the brief".

- **Item 23: fixed.** The memo now says it counted 11 PASS-then-FAIL reversals and opened 4. VT3 r3→r4 is reported as following a Builder fix, not a draft, and P-q006-02 is narrowed to match.

- **Item 24: fixed.** The "far apart" example now uses M3B r1 B2 (:12773 against :11002) and B1 (:12789 against :13606), which are far apart.

- **Item 25: fixed.** The memo says 2 of 330 files name the model (desk-v2 1b r1:13 and r2:11), and "82 of 154" S-001-* files with no header, which matches my count. F-q006-04 now says "almost never".

- **Item 28: fixed.** The Definer helper at :5 is now said to overlap the 9 helper lines starting during it (:6–:14).

- **Cause-class rows: now follow §2.**
  - design-reviewer-setup #1 is "Doer, by default", and #4 is untraceable.
  - sync r1 and r6 are "Doer, by default; no checker names a cause". The memo says R1 and R2 are not about the reviews and R3–R6 are.
  - M3B r7 B1 and records r4 #1 are "Doer, by default", since the record shows only that the draft held owner answers.
  - HD1 r2 and VT3 r2 stay Inputs, with the "another branch" nuance quoted.

- **Library entries.**
  - May be filed as written:
    - F-q006-01 (the grade split between A and B is stated).
    - F-q006-02 (grade B, line references, and the extra Q-006 session noted).
    - F-q006-03 (cause stated as not established).
    - F-q006-05 (the differences listed).
    - F-q006-06.
    - F-q006-07 (7 of 17 and 4 of 17 with the rule stated, one item with no pass, build range).
    - F-q006-08 (grade A for the example only).
    - P-q006-01 (grade C, cause not claimed).
    - P-q006-02 (grade C, 4 of 11 opened).
    - P-q006-03 (R1, R2 and R3–R6 separated).
    - P-q006-04 (grade C, confounded).
  - F-q006-04 may be filed with one grade fix: it is labelled "Grade A", but its "2 of 330" is a count, which the memo's own rules grade B.

**Remaining minor points (neither blocks the PASS)**
- §7 item 3 still reads as if the anomaly lines name the two undispatched sessions (Q-006 01:25:01, Q-013 21:36:11). They name the neighbouring sessions (01:28:40 and 21:42:17). F-q006-02 states the Q-006 case correctly.
- The sessions-without-dispatch-line count and its control records are right. Only the wording about which session the anomaly names is loose.

No conclusion in §0 or §8 now rests on a figure that failed my recomputation.

My earlier FAIL report is superseded for items 10, 17, 18, 19, 21–25 and 28. Items 17 and the "two items with no pass" claim were my error and are withdrawn.
