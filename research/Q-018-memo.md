# Q-018 memo: hand check of S-002's counting rules on the drawn sample

*Recorded verbatim by the Orchestrator from the Researcher's return on brief 286 (docs/briefs/286-researcher.md), Model-Lab@fdb85db.*

Researcher, 2026-11-12. Read: research/Q-018.md and research/Q-018-extract/ only (README.md, sample.json, sample.jsonl, frames.json, github_reads.json). No web, no specs, reviews, docs or decisions. Depth: level 1 (reading the records as extracted). Nothing written.

**In plain words.** First, what could not be done or decided. Twelve of the 34 pieces could not be given a first-check result as the rule is written. In five, the only check record found belongs to the wrong kind of work. In five more, a record exists but no first-round verdict line was found in it. And in three pieces, an owner question record was first added at exactly the moment the work was dispatched, so whether it counts as a touch depends on whether that moment is inside or outside the window. Two further limits apply. The extract has no free text, so it cannot tell whether a question and the record of its answer are one question or two, nor whether an owner comment was only thanks. And four parts of the touch rules (the hand-kept touch log and the unasked-instruction rule) find nothing in past records by design.

Here is what was found. Of the 74 drawn items, 70 are merged pull requests, 2 are pull requests closed unmerged and 2 are commits with no pull request. 34 of the 70 merged pull requests are pieces of work under the rules; the other 36 only change records, owner question or answer files, or "other" files. Of the 34 pieces, 14 are built work, 14 are plans and 6 are research. Every kind came from the line-count rule except one plan, whose brief gave its kind. 17 pieces have at least one owner touch (18 if one boundary case counts). There are 40 question or decision records and 8 owner comments, and no fixes or send-backs. 22 of those 40 records are files the piece itself adds or changes. No piece was reopened. 21 are still inside their 30 days and so pending; 13 have completed their 30 days and were not reopened. Nothing here is irreversible, and no count is judged large or small.

## 1. Conventions and grades
- **Fact-A**: read directly from a field of the extract (sample.jsonl line n, or the file named).
- **Fact-B**: worked out by me from extract fields: line sums, comparing times against windows, matching labels. It is reproducible from the cited fields.
- **Opinion**: my reading where a rule leaves room. Always marked.
- None of my facts is marked checked; the Source checker and the Critic do that.
- "Lines" for K3 means added plus removed. Under an added-only reading no piece's kind changes (Fact-B).
- A touch window is from `dispatch` up to `merged_at`. Records are compared by `first_added` (commit time); dispatch is the author time of the first commit, except for ML#98, where the brief record gives it.
- "Own file" means the question or decision record's label is among the piece's own changed files. Labels are stable per path (README, "Labels").

## 2. Results for all 74 drawn items
ML = Model-Lab, SD = Service-Desk, PO = Personal-Org-Operating-Model. L = line in sample.jsonl. "30d" is days30_complete. "q" is a question record, "d" a decision record. All Fact-A or Fact-B from that line unless marked.

### 2a. Random part, Model-Lab (20, all one stratum; none has completed 30 days)
| L | Item | RP1/RP2 | Kind (rule) | Touches (rule: record) | C1 | RR |
|---|---|---|---|---|---|---|
| 1 | ML#61 | merged; records only → not a piece | — | — | — | — |
| 2 | ML#43 | piece (plan 347 lines, research 168) | plan (K3) | none. d 0380c2ec was first added 16:27:49, 76 s before dispatch 16:29:05, so outside the window | Critic plan review (S-001), round 1 FAIL, 7 rounds | pending |
| 3 | ML#29 | piece (plan 301) | plan (K3) | RT1(a) ×4: q 197dd190 (23:58:10), d 9acdfce2 (00:38:22), q 5e700c74 and q 3ae73360 (00:43:43). All own files, all named by path | no record (no Spec trailer) → left out | pending |
| 4 | ML#58 | records and owner q/a only → not a piece | — | — | — | — |
| 5 | ML#92 | piece (plan 10) | plan (K3) | RT1(a) ×1: d b3609d4c (02:32:58, own file) | no record → left out | pending |
| 6 | ML#64 | records only → not a piece | — | — | — | — |
| 7 | ML#93 | piece (plan 232) | plan (K3) | RT1(a) ×2: q 22147854 (03:08:30, own file); d 31505fb6 (03:50:31, names #93 by number) | only a Reviewer record (for built), PASS; no plan record → **undecided**, see U2 | pending |
| 8 | ML#13 | piece (research 39) | research (K3) | RT1(a) ×3: d f9f581ae (19:43:27), d 9c7e7ddd (19:54:45), d b6858127 (19:58:21). Not own files; named by path | Source checker, round 1 FAIL, 2 rounds | pending |
| 9 | ML#25 | records and owner q/a → not a piece | — | — | — | — |
| 10 | ML#47 | records and owner q/a → not a piece | — | — | — | — |
| 11 | ML#73 | piece (research 716) | research (K3) | RT1(a) ×1: q 9ea16fdb (19:53:21, own file) | Source checker record, 3 rounds, no first-round verdict found → **undecided** (U3) | pending |
| 12 | ML#77 | records and owner q/a → not a piece | — | — | — | — |
| 13 | ML#55 | records only → not a piece | — | — | — | — |
| 14 | ML#59 | records and owner q/a → not a piece | — | — | — | — |
| 15 | ML#42 | owner q/a and/or records → not a piece | — | — | — | — |
| 16 | ML#56 | owner q/a and/or records → not a piece | — | — | — | — |
| 17 | ML#81 | piece (research 2038) | research (K3) | RT1(a) ×1: q 30491519 (05:32:16, own file). d 9312a092 (13:55:50) is after the merge | two Source checker records, both "none found", 3 rounds → **undecided** (U3) | pending |
| 18 | ML#27 | records only → not a piece | — | — | — | — |
| 19 | ML#78 | piece (research 103) | research (K3) | none | two Source checker records, both "none found", 4 rounds → **undecided** (U3) | pending |
| 20 | ML#32 | records only → not a piece | — | — | — | — |

### 2b. Random part, Service-Desk (L21–30 from the stratum still inside 30 days; L31–40 from the stratum past 30 days)
| L | Item | RP1/RP2 | Kind (rule) | Touches | C1 | RR |
|---|---|---|---|---|---|---|
| 21 | SD#233 | bot merge; owner q/a and/or records → not a piece | — | — | — | — |
| 22 | SD#230 | piece (built 596, plan 41) | built (K3) | RT1(a) ×4: q b793d0d9, q 6ab2fa98, q 446c689a (09:40:32); q e469c207 (09:48:17). All own files. q f949703e (08:06:29) is before dispatch | Reviewer, round 1 FAIL, 2 rounds | pending |
| 23 | SD#105 | bot merge; owner q/a → not a piece | — | — | — | — |
| 24 | SD#76 | owner q/a → not a piece | — | — | — | — |
| 25 | SD#237 | piece (research 16) | research (K3) | RT1(a) ×5: q b0dc8e16, d184bc0b, f24d03df, 9e91287e, 2780ba86 (15:41:24), all own files. The five d records at 16:13:52 are 41 s after the merge | no record → left out | pending |
| 26 | SD#150 | bot merge; owner q/a → not a piece | — | — | — | — |
| 27 | SD#109 | bot merge; owner q/a → not a piece | — | — | — | — |
| 28 | SD#341 | piece (built 24) | built (K3) | none certain. d 8e21866a, an own file, was first added at 13:52:33, the dispatch instant → **undecided** (U1): 0 or 1 | Reviewer, round 1 PASS | pending |
| 29 | SD#93 | bot merge; records only → not a piece | — | — | — | — |
| 30 | SD#329 | records only → not a piece | — | — | — | — |
| 31 | SD#22 | piece (plan 13) | plan (K3) | none | no record → left out | not reopened (30d done) |
| 32 | SD#51 | records only → not a piece (30d) | — | — | — | — |
| 33 | SD#21 | owner q/a → not a piece (30d) | — | — | — | — |
| 34 | SD#61 | piece (plan 1471, research 28) | plan (K3) | none | no record → left out | not reopened |
| 35 | SD#26 | piece (plan 196) | plan (K3) | RT1(a) ×1: d 1d370480 (16:11:10, own file). Plus d 233211a9 (own file) at 15:46:35, the dispatch instant → **undecided** (U1): 1 or 2 | no record → left out | not reopened |
| 36 | SD#57 | records only → not a piece (30d) | — | — | — | — |
| 37 | SD#25 | piece (plan 80) | plan (K3) | none | no record → left out | not reopened |
| 38 | SD#6 | "other" and records, none built/plan/research → not a piece (an E-RP3 shape). 1 owner comment before merge, not counted because it is not a piece | — | — | (Reviewer PASS exists; not applied) | — |
| 39 | SD#31 | piece (plan 12) | plan (K3) | none | no record → left out | not reopened |
| 40 | SD#47 | records only → not a piece (30d) | — | — | — | — |

### 2c. Random part, Personal-Org-Operating-Model (10 past 30 days: L42, 44, 53–60; 10 inside)
| L | Item | RP1/RP2 | Kind (rule) | Touches | C1 | RR |
|---|---|---|---|---|---|---|
| 41 | PO#35 | piece (built 3527, plan 634) | built (K3) | RT1(b) ×1 owner comment before merge | Reviewer, round 1 PASS | pending |
| 42 | PO#11 | records only → not a piece. 1 owner comment, not counted | — | — | — | — |
| 43 | PO#47 | piece (plan 120) | plan (K3) | none. q c4c7c231 (13:09:42) is after the merge (13:05:19) | only a Reviewer record (for built), PASS → **undecided** (U2) | pending |
| 44 | PO#19 | records only → not a piece | — | — | — | — |
| 45 | PO#32 | owner q/a only → not a piece | — | — | (Reviewer PASS exists; not applied) | — |
| 46 | PO#52 | records only → not a piece | — | — | — | — |
| 47 | PO#30 | piece (built 588, plan 149) | built (K3) | RT1(b) ×2 owner comments before merge | Reviewer, round 1 PASS | pending |
| 48 | PO#48 | owner q/a → not a piece | — | — | — | — |
| 49 | PO#53 | records only → not a piece | — | — | — | — |
| 50 | PO#50 | piece (built 175, plan 4) | built (K3) | none | Reviewer record, 1 round, no verdict found → **undecided** (U3) | pending |
| 51 | PO#49 | piece (built 547, plan 109) | built (K3) | RT1(a) ×1: q de17627b (16:38:01, own file) | Reviewer, round 1 PASS | pending |
| 52 | PO#27 | piece (built 2520, plan 1066) | built (K3) | none | Reviewer, round 1 PASS | pending (merged 10-13 15:20; 30 days end after the cut-off) |
| 53 | PO#15 | records only → not a piece | — | — | — | — |
| 54 | PO#24 | piece (built 60) | built (K3) | none | Reviewer record, 1 round, no verdict found → **undecided** (U3) | not reopened |
| 55 | PO#23 | records only → not a piece | — | — | — | — |
| 56 | PO#14 | records only → not a piece | — | — | — | — |
| 57 | PO#25 | piece (plan 258, built 129) | plan (K3) | none. One commit has author class other (E-RT2 shape): not a touch | only a Reviewer record (for built), PASS → **undecided** (U2) | not reopened |
| 58 | PO#18 | piece (built 20, plan 2) | built (K3) | RT1(b) ×1 owner comment before merge | Reviewer, round 1 PASS | not reopened |
| 59 | PO#22 | piece (built 455, plan 106) | built (K3) | none | Reviewer, round 1 PASS | not reopened |
| 60 | PO#20 | piece (built 2110, plan 235) | built (K3). Its trailers name briefs s-017, s-018 and s-019, but no brief record exists and no role is read, so K2 does not map (E-K2/E-RP4 shapes) | none. Three commits have author class other: not touches (E-RT2) | Reviewer, round 1 PASS | not reopened |

### 2d. Edge-case part (14)
| L | Item | Drawn as | Result |
|---|---|---|---|
| 61 | SD commit 9e46dd841aa3 | E-RP1 | Frame D: a two-parent local merge by an agent on 2026-10-01, no files. No pull request → not a piece (E-RP1) |
| 62 | SD commit 04511022f1a3 | E-RP1 | Frame D: one-parent agent commit on 2026-11-09, 4 records files → not a piece (E-RP1) |
| 63 | SD#147 | E-RP2 | Closed unmerged by the owner on 10-19 21:07:36. Head prefix build/chief-of-staff/. One agent commit changing owner q/a file de64334e; 1 owner comment before close → not a piece (E-RP2). No sampled piece has an RT3(b) match |
| 64 | SD#174 | E-RP2 | Closed unmerged by the owner on 10-21. No commits; 1 owner comment before close → not a piece (E-RP2) |
| 65 | SD#316 | E-RP3 | "Other" and records only → not a piece. One owner web-editor commit adds a records file. Reviewer PASS exists (not applied) |
| 66 | ML#69 | E-RP3 | "Other" and records only → not a piece. One owner web-editor records commit |
| 67 | ML#98 | E-RP4 | Piece (research 344, plan 222). Briefs 258 and 263 are both Definer, so its kind is **plan (K2)**; K3 alone would give research. Dispatch 18:23:13 comes from the brief 258 record. Touches: none; d 56004034 (18:08:39) is before dispatch and q 357e6847 (20:34:35) after the merge. C1: no record (Spec S-002) → left out. RR: pending. One piece, as E-RP4 says |
| 68 | SD#78 | E-K1 | Piece (built ≫ plan 5441 > research 200) → built (K3). Touches: RT1(a) ×1 d 7d757252 (20:29:14, own file); RT1(b) ×1 owner comment; and d d38d8364 (own file) at the dispatch instant 11:54:38 → **undecided** (U1). Total 2 or 3. C1: Reviewer, round 1 PASS. RR: pending |
| 69 | SD#148 | E-K1 | Piece (plan 2533, research 163, built 73) → plan (K3). Touches: RT1(a) ×12, none own files: q 22932f98 (21:09:51), q 552be005 (21:43:10, names #148 by number), q 9af9edbc, 6cd03d48, 4da0c010, abd445ad, f0679007, 873f0732 (21:50:12), q d56be526 (21:52:09), q 93b16f32 and 70c94f21 (10-20 14:04:40), d 787e1996 (14:18:53). C1: only a Reviewer record (for built), PASS → **undecided** (U2). RR: pending |
| 70 | SD#36 | E-K2 | Piece (plan 2310, research 520) → plan (K3). Its trailer names brief s-001 with no role read and no record, so K2 does not map. Touches: none (d d6894fd9 is 16 min before dispatch). C1: no record (Spec S-001) → left out. RR: not reopened (30d) |
| 71 | SD#319 | E-RT2 | Records only → not a piece. Its author-class-other commit is moot |
| 72 | SD#300 | E-RT2 | Piece (research 879) → research (K3). 11 commits have author class other and carry Agent-Session trailers: not touches (E-RT2). Touches: RT1(a) ×4: q 8d12f7f3 (11-04 20:50:05), d e24f55f9 (20:51:10), q 76fc6d56 (22:17:16, own file), q c2476643 (11-05 16:24:30, own file, names #300). C1: only a Reviewer record (for built), PASS; no Source checker record → **undecided** (U2). RR: pending |
| 73 | SD#52 | E-RR2 | Piece (built 709) → built (K3). Touches: none (d 4bce8209 is 2 min before dispatch). C1: Reviewer, round 1 PASS. RR: not reopened. E-RR2 candidates: 49 later pull requests sharing a file (#72 to #253); no later commit names #52 |
| 74 | SD#11 | E-RR2 | Piece (built 4) → built (K3). Touches: RT1(b) ×3 owner comments before merge. C1: Reviewer, round 1 PASS. RR: not reopened. E-RR2 candidates: #14, #18, #27, #48, #65, #148 |

### 2e. Totals (all Fact-B; reported on equal terms, not judged)
- **Pieces.** 34 of 70 merged pull requests; 27 of the 60 random (ML 8, SD 8, PO 11), and 7 of the 10 merged edge items. Not pieces: 36 merged, plus 2 closed unmerged (E-RP2) and 2 frame D commits (E-RP1).
- **Kinds.** 14 built, 14 plan, 6 research. K3 gave 33 and K2 gave 1 (ML#98).
- **Touches.**
  - RT1(a): 40 definite records (22 own files, 18 not), plus 3 at the dispatch instant.
  - RT1(b): 8 comments on 5 pieces.
  - RT2(a): 0. Every owner web-editor commit changes only records files.
  - RT3(a): 0 (no reviews exist). RT3(b): 0.
  - Pieces with at least one definite touch: 17 of 34; 18 if SD#341's boundary record counts. In the random part: 13 of 27, or 14.
- **C1.**
  - PASS 11: SD#341, SD#78, SD#52, SD#11, PO#35, PO#30, PO#49, PO#27, PO#18, PO#22, PO#20.
  - FAIL 3: ML#43, ML#13, SD#230.
  - No record, left out 10: ML#29, ML#92, ML#98, SD#237, SD#22, SD#61, SD#26, SD#25, SD#31, SD#36.
  - Undecided 10: U2 ×5 and U3 ×5.
- **Reopening.** 0 reopened; 21 pending; 13 not reopened (SD#22, #61, #26, #25, #31, #36, #52, #11; PO#24, #25, #18, #22, #20).
- **E-RR2 candidates for pieces past 30 days** (later merged pull requests sharing a file): SD#22 28, SD#61 3, SD#26 24, SD#25 25, SD#31 22, SD#36 46, SD#52 49, SD#11 6, PO#24 8, PO#18 10, PO#22 4, PO#20 10, PO#25 0. No later commit names any of their numbers.
- **Pending pieces' candidates** (inside the 30-day window up to the cut-off): ML#29, #93, #13 and SD#237, #341, #300, PO#30 also have later commits naming their number. All are listed in sample.jsonl `after_merge`.

## 3. Rules untested, and why
- **K4, RR1(c):** these apply to trials only.
- **RR1(b):** the `Reopens:` mark cannot exist on past pieces. `reopens_marks` is empty on all 72 pull requests (Fact-A).
- **RT1(c), RT2(b), RT3(c), RT7:** the touch log holds no past touches.
- **RT5:** not coded, by the rule.
- **RT3(a):** tested; nothing found. No pull request in the three repositories has a review (github_reads.json; Fact-A).
- **RT6:** applied by counting each record on every piece whose window it falls in. In this sample, no record fell in two sampled pieces' windows, so RT6 never changed a count (Fact-B).
- **RR1(a):** tested. `reverts_naming_it` is empty everywhere and no commit has a "Revert" subject (Fact-A).
- **K1:** taken as given. Paths are not written, so I cannot check any file's class.

## 4. Cases I could not decide
- **U1, a record at the dispatch instant.** SD#341 (d 8e21866a), SD#26 (d 233211a9) and SD#78 (d d38d8364) are each the piece's own file, first added at exactly the dispatch time, which is the author time of the first commit. The rule does not say whether the window includes its start. RT4 also excludes "the ruling that started the piece, given before its dispatch". These look like the starting ruling recorded in the first commit (Opinion), but the text was not read.
- **U2, a check record of another kind.** ML#93 (plan), SD#148 (plan), PO#47 (plan) and PO#25 (plan) have only a Reviewer record, PASS. SD#300 (research) also has only a Reviewer record, PASS. C1 names the check by kind, so read strictly each is "no such record, left out". Read by the record that exists, each is PASS. The rule does not say which (Opinion: strict reading).
- **U3, a record with no first-round verdict.** The extract gives `verdict: none found` for ML#73, ML#81 (two records), ML#78 (two records), PO#50 and PO#24. The record exists, so "left out for having no record" does not apply word for word. The verdict may use another wording, which needs the text.
- **U4, question and answer as one touch or two.** RT1(a) counts question files and decision records, but the extract cannot tell a question from the record of its answer. ML#29 is the clear case: its own commit d7f8549a deletes q 197dd190 and adds d 9acdfce2 at the same instant, so both are counted. Of the 40 RT1(a) records, 22 are the piece's own files. Whether an agent-filed record in the piece is "a question put to the owner" needs the text.
- **U5, naming by path.** Many matches are by path only. The extract does not say whether a record's match is to its own path, which would name the piece trivially. This affects the own-file records in ML#29, ML#92, ML#93, ML#73, ML#81, SD#230, SD#237, SD#26, SD#78 and PO#49.
- **U6, the RT1(b) comments.** The 8 comments are counted unread. Whether any is thanks only (E-RT5), or was posted under the owner's account by an agent session, is not in the fields (README).
- **U7, the null brief role on SD#36 and PO#20.** I treated both as "K2 does not map", so K3 applies. In SD#36 it is also unclear whether "s-001" is a brief at all in Service-Desk, whose brief folder holds only its README (README).

## 5. Sampled awkward cases
- **Seen (sample.json edge part):**
  - E-RP1 ×2: SD 9e46dd84, 04511022.
  - E-RP2 ×2: SD#147, #174.
  - E-RP3 ×2: SD#316, ML#69.
  - E-RP4 ×1: ML#98, the only match.
  - E-K1 ×2: SD#78, #148.
  - E-K2 ×1: SD#36.
  - E-RT2 ×2: SD#319, #300.
  - E-RR2 ×2: SD#52, #11.
- **Also met in the random part (Fact-B):**
  - E-RP3 shape: SD#6.
  - E-RP4 shape: PO#20.
  - E-K1 shapes: ML#43, SD#230, SD#61 and most PO pieces.
  - E-RT2 shapes: PO#25, PO#20.
  - E-RP5 shape: none. All 5 bot merges (SD#233, #105, #150, #109, #93) are not pieces.
- **Not seen:** E-RP5, E-RP6, E-K3, E-RT1, E-RT3. None of the sampled Service-Desk pieces took its dispatch from a control file.
- **Not sampled (for the Critic, step 5):** E-RT4, E-RT5, E-RT6, E-RR1, E-RR3. For E-RT4, the first 10 pieces in sample.jsonl's order are ML#43, #29, #92, #93, #13, #73, #81, #78, SD#230, #237. If "the sample's order" means hash order across repositories, the list differs.

## 6. Fields absent or "not read"
- Comment text and review text: absent. Reviews for undrawn frame M pull requests: "not read" (unused).
- Paths, subjects and messages: absent. Hence U4, U5 and K1 unchecked.
- E-RP1's "number per month": frames.json gives only totals for frame D (SD 566, ML 4, PO 0). A per-month split is absent.
- Brief role: null for SD s-001 and PO s-017, s-018, s-019; those brief records do not exist.
- Frame U rows carry no field for later merges. RT3(b) rests on the later pieces' `rt3b_matches`, which are empty for every sampled piece.
- Comment authorship by session: absent.

## 7. Field scan
Not run. The brief rules out the web, and this question is about these records only.

## 8. Proposed library entries (not checked; for the Source checker)
- **Fact.** At 2026-11-12, no pull request in Model-Lab, Service-Desk or Personal-Org-Operating-Model had a GitHub review or line comment.
  - Source: research/Q-018-extract/github_reads.json. Grade: Fact-A.
  - Shelf life: until the next extract. Topics: measurement, owner-touch, GitHub records.
- **Fact.** In the Q-018 sample, 34 of 70 merged pull requests were pieces under S-002 RP2 (27 of 60 random).
  - Source: sample.jsonl `files` classes. Grade: Fact-B.
  - Shelf life: tied to this extract. Topics: measurement, piece definition.
- **Fact.** Of 40 RT1(a) records within piece windows, 22 are question or decision files the piece itself changes.
  - Source: sample.jsonl `questions_decisions` against `files` labels. Grade: Fact-B.
  - Shelf life: tied to this extract. Topics: measurement, owner-touch.
- **Pattern (Opinion).** A no-text count of question and decision records cannot tell a question from its answer record or from a self-reference by path. RT1(a) counts from such an extract therefore need a text check, or a one-touch-per-question rule.
  - Source: U4 and U5 above. Topics: measurement design.

## Six-part contract
- **Changed (by file):** nothing. I hold no write tool. This memo is to be recorded as research/Q-018-memo.md.
- **Why:** brief 286, research question Q-018 (S-002 hand check, M8).
- **Verified (command and output):**
  - Read-only Grep and Read over /home/user/Model-Lab/research/Q-018-extract/. sample.jsonl has 74 lines (Grep count: 74).
  - Per-line fields were taken with `Grep -o` on `dispatch`, `merged_at`, `first_check`, `briefs`, `trailer_briefs`, `spec`, commit author and committer classes, top-level `files` (status as a list), `questions_decisions` and `after_merge`.
  - These patterns returned no matches anywhere: `rt3b_matches`, `reviews`, `reopens_marks`, `reverts_naming_it` (non-empty), `revert_subject: true`.
  - Sums and window comparisons were done by hand. No code was run.
- **Undone:**
  - I did not read docs/DIGEST.md or the open sprint, because the brief's manifest excludes docs/. So I cannot name the open sprint or the branch; the brief names its start branch as claude/great-newton-o6ep0u.
  - The model is withheld from this record under the brief's standing instruction.
  - The not-sampled cases (E-RT4, E-RT5, E-RT6, E-RR1, E-RR3) are the Critic's.
- **Needed outside my surface:**
  - The Critic's step 5 check of this coding against the records.
  - A ruling or spec reading on U1 (is the window's start inclusive?), U2 (is the check record chosen by kind or by the record found?) and U4 (does a question and its answer count once?).
- **Open questions:** U1 to U7 above. I add none beyond them and close none.

Paths: /home/user/Model-Lab/research/Q-018.md, /home/user/Model-Lab/research/Q-018-extract/sample.jsonl, /home/user/Model-Lab/research/Q-018-extract/sample.json, /home/user/Model-Lab/research/Q-018-extract/frames.json, /home/user/Model-Lab/research/Q-018-extract/github_reads.json
