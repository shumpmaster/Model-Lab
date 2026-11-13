# Memo: Q-018, the hand check of S-002's counting rules, re-coded on the rules as brief 305 left them

Researcher, item P-002, brief 308, 2026-11-12. Sources: only research/Q-018.md, research/Q-018-extract/README.md, sample.json and sample.jsonl. No web, no text from outside the manifest.

**What I found and what I could not decide.** I applied the rules to all 74 drawn items. 33 are pieces of work and 41 are not. Of the 33 pieces, 14 had at least one touch by the owner before merging under the rules as they read today. Every one of those touches is a question or an answer in the records. No owner comment, fix or send-back counts on any drawn piece: all 12 comments posted under the owner's account carry the agent footer. The count changes in one place. If I drop the commits whose only owner-word lines are quoted forms, rather than a "Ruling:", "Answer:" or "Decision:" label, three pieces in the operating-model repository fall to zero touches, and the share goes from 14 of 33 to 11 of 33. If I drop records that name a piece only by its spec id, no piece's "at least one touch" changes. For the first independent check, 20 pieces get a result (4 PASS, 16 FAIL), 4 are undecided and 9 have no check record and are left out. No piece was reverted, so the 13 pieces whose 30 days are complete are "not reopened" and the other 20 are pending. I could not decide four things from the extract alone:
- whether records that name a piece only by being one of its own files are about other work (the extract holds no text);
- the first check for four pieces whose only records are of another kind, unclassed, or give no first-round verdict;
- whether the owner words held in ledger entries, instruction files, intake items and the desk's other reference files would count; the rules leave these open (Open questions 2 and 15);
- whether any closed-unmerged pull request's work later merged in a piece that was not drawn.

## How to read this memo

- Every result below is a **fact, grade B**: I derived it by applying S-002's rules, as Q-018 quotes them, to the extract's fields. Nobody has checked it against the repositories yet; that is step 5, the Critic's.
- Statements marked **(opinion)** are my readings where the rules leave room.
- Times are UTC. Records are given by the extract's labels.
- "Touches" are given as three numbers, `today / without names_only_by_spec / without only_form_2_or_3`.
- I read "changed lines" in K3 as added plus removed lines **(opinion)**. Counting added lines alone gives the same kind for every piece. The closest case is POOM #25, plan 196 against built 127 added lines.
- Repositories are written ML (Model-Lab), SD (Service-Desk) and POOM (Personal-Org-Operating-Model).
- Except where noted, each piece's dispatch is its first commit (`dispatch_from`). The one exception is ML #98, dispatched by its brief record.

## The 74 drawn items

In the table, "random" means drawn in the random part (sample.json `random_part`); otherwise the column gives the edge case it was drawn for.

| # | Item | Drawn as | Piece? (RP1, RP2) | Kind (rule) | Owner touches before merge: today / no-spec-only / no-form-2-3-only, and the records they rest on | First check (C1) | Reopening (RR1 to RR3) |
|---|---|---|---|---|---|---|---|
| 1 | ML #61 | random | No: all files records | – | – | – | – |
| 2 | ML #43 | random | Yes | plan (K3: plan 347, research 168) | 0/0/0. 16 records name it only by spec; none is added inside its window (16:29:05 to 17:23:59 on 11-04) | FAIL: plan record 0df9522f, reading (ii), 5 rounds; 3 unclassed records not read | pending |
| 3 | ML #29 | random | Yes | plan (K3, plan only) | 2/2/2. (i) Question 8628e3d2: decision 9acdfce2, own file, first added 00:38:22 on 11-02 with 1 form-(1) line; RT5(c), class "Accepting an unknown as open"; milestone Discovery-8 (listed, Open question 13). (ii) Question 24955290: question file 5e700c74, own file, first added 00:43:43; RT5(c), "A milestone mark". 3ae73360 and 66512cad, "A phase gate", are left out (RT5(b)) | left out (no record at C1's paths), listed | pending |
| 4 | ML #58 | random | No: owner question or answer and records only | – | – | – | – |
| 5 | ML #92 | random | Yes | plan (K3) | 0/0/0. Decision b3609d4c, "Part of a value target", is left out by RT5(b), though first added in the window (02:32:58) with 2 owner-word lines. Intake copy b97ada67 listed | left out, listed | pending |
| 6 | ML #64 | random | No: records only | – | – | – | – |
| 7 | ML #93 | random | Yes | plan (K3) | 1/1/1. Question 0d05d5f2: question file 22147854, own file, first added 03:08:30 on 11-11; its decision 31505fb6 (by number, 03:50:31, 2 form-(1) lines) is the same question. Both RT5(d) with no word; milestone Discovery-8 (listed, Open question 13). 4973eb45 and 56004034 fall after the merge and are RT5(b) naming other rulings (listed below) | undecided, listed (Open question 12): its only record of a check kind is build review cdb3e6dc (PASS), which is of another kind for a plan piece; the rest are another kind or unclassed | pending |
| 8 | ML #13 | random | Yes | research (K3) | 0/0/0 | FAIL: f33fac53 and 0f1c0335, both FAIL by (ii) | pending |
| 9 | ML #25 | random | No: owner question or answer and records | – | – | – | – |
| 10 | ML #47 | random | No: owner question or answer and records | – | – | – | – |
| 11 | ML #73 | random | Yes | research (K3) | 1/1/1. Question file 9ea16fdb, own file, 19:53:21 on 11-08; decision da219f2f falls after the merge | FAIL: be10cf2b and 4241d270, both (ii) | pending |
| 12 | ML #77 | random | No: owner question or answer | – | – | – | – |
| 13 | ML #55 | random | No: records only | – | – | – | – |
| 14 | ML #59 | random | No: owner question or answer and records | – | – | – | – |
| 15 | ML #42 | random | No: owner question or answer | – | – | – | – |
| 16 | ML #56 | random | No: owner question or answer | – | – | – | – |
| 17 | ML #81 | random | Yes | research (K3) | 1/1/1. Question file 30491519, own file, 05:32:16 on 11-09; decision 9312a092 after the merge | FAIL: cba2f3bb and 41905828, both (ii) | pending |
| 18 | ML #27 | random | No: records only | – | – | – | – |
| 19 | ML #78 | random | Yes | research (K3) | 0/0/0 | left out, listed | pending |
| 20 | ML #32 | random | No: records only | – | – | – | – |
| 21 | SD #233 | random | No: owner question or answer and records; merged by a bot | – | – | – | – |
| 22 | SD #230 | random | Yes (E-K1) | built (K3: built 596, plan 41) | 4/4/4. Question files b793d0d9, 6ab2fa98 and 446c689a (09:40:32 on 10-25) and e469c207 (09:48:17), each own file only | FAIL: 8eae195c FAIL by (ii); 23917e4b FAIL by (i); 96463ddc none | pending |
| 23 | SD #105 | random | No: owner question or answer; bot | – | – | – | – |
| 24 | SD #76 | random | No: owner question or answer | – | – | – | – |
| 25 | SD #237 | random | No (K1 change (iii)): owner-answers and request files plus records | – | – | – | – |
| 26 | SD #150 | random | No: owner question or answer; bot | – | – | – | – |
| 27 | SD #109 | random | No: owner question or answer; bot | – | – | – | – |
| 28 | SD #341 | random | Yes | built (K3) | 0/0/0. Decision 8e21866a was first added in the piece's first commit, so it is the ruling that started the piece (RT4) | PASS: 3ea324e4 by (iv); 69809936 gives none | pending |
| 29 | SD #93 | random | No: records; bot | – | – | – | – |
| 30 | SD #329 | random | No: records | – | – | – | – |
| 31 | SD #22 | random | Yes | plan (K3) | 0/0/0. 84ddb037 is the starting ruling (RT4); 84cee8be is a `-notes.md` file, not counted | left out, listed | not reopened; 28 E-RR2 candidates |
| 32 | SD #51 | random | No: records | – | – | – | – |
| 33 | SD #21 | random | No: owner question or answer and records | – | – | – | – |
| 34 | SD #61 | random | Yes (E-K1) | plan (K3: plan 1471, research 28) | 0/0/0 | left out, listed | not reopened; 3 candidates (#66, #69, #72) |
| 35 | SD #26 | random | Yes | plan (K3) | 1/1/1. Decision b2697809, own file, first added 16:11:10 on 10-04 with 1 form-(1) line. 233211a9 is the starting ruling, and its commit at 16:11:10 is not an append (1 added line matched against 3 removed), listed. Notes files 4782268e and 1d370480 not counted | left out, listed | not reopened; 24 candidates |
| 36 | SD #57 | random | No: records | – | – | – | – |
| 37 | SD #25 | random | Yes | plan (K3) | 0/0/0 | left out, listed | not reopened; 25 candidates |
| 38 | SD #6 | random | No: other and records | – | – | – | – |
| 39 | SD #31 | random | Yes | plan (K3) | 0/0/0. ad5eedfa is the starting ruling (RT4) | left out, listed | not reopened; 22 candidates |
| 40 | SD #47 | random | No: records | – | – | – | – |
| 41 | POOM #35 | random | Yes (E-K1) | built (K3: built 3527, plan 634) | 2/2/2. Answer record 0d5230c0 (spec and own file) is, as first added, the starting ruling. Its append at 16:13:32 on 10-17 (form (1), names no id) is one question. Its append at 17:59:31 (form (1), names Q-024) pairs with question file Q-024 (14b7aecb, first added 16:19:03), giving one question timed at 16:19:03 | FAIL: 675ec21d FAIL by (i); 66417607 and a501ea2c none; plan records not read | pending |
| 42 | POOM #11 | random | No: records | – | – | – | – |
| 43 | POOM #47 | random | Yes | plan (K3) | 0/0/0. Q-029's question file c4c7c231 (by number) was first added 13:09:42 on 11-05, after the merge | FAIL: plan record 65934264 FAIL by (i) | pending |
| 44 | POOM #19 | random | No: records | – | – | – | – |
| 45 | POOM #32 | random | No: owner question or answer (Q-022) and records | – | – | – | – |
| 46 | POOM #52 | random | No: records | – | – | – | – |
| 47 | POOM #30 | random | Yes (E-K1) | built (K3: built 588, plan 149) | 5/3/0. Answer record 455192c4 (spec and own file): first added 20:24:30 on 10-13, appends at 20:47:13 and 22:06:38, so 3. Answer record 4efc6a60 (spec only): first added 22:13:25, append at 23:15:11, so 2. Every commit is form (2) or (3) only | undecided, listed (U3): build record 63a11d59 gives no round-1 verdict; plan records are of another kind | pending |
| 48 | POOM #48 | random | No: owner question or answer (Q-029, Q-030) and records | – | – | – | – |
| 49 | POOM #53 | random | No: records | – | – | – | – |
| 50 | POOM #50 | random | Yes (E-K1) | built (K3: built 175, plan 4) | 0/0/0. Q-030 (5b41d98e, 08ba8ef8) and Q-031's question file de17627b were first added before the dispatch. df986385 (Q-031's answer) was first added in the first commit, so it is the starting ruling | PASS: 3fed3942 by (iv) and f5ba9a62 by (i) | pending |
| 51 | POOM #49 | random | Yes (E-K1) | built (K3: built 547, plan 109) | 1/1/1. Q-031's question file de17627b (spec and own file) was first added 16:38:01 on 11-05; its answer df986385 falls after the merge. Q-029's and Q-030's answers (558fd054, 08ba8ef8) are starting rulings (RT4) | PASS: 0e5d0a2e and f5ba9a62 PASS; cdb45b88 none | pending |
| 52 | POOM #27 | random | Yes (E-K1) | built (K3: built 2520, plan 1066) | 10/4/0. e219aae3 (spec only, read from its append at 20:17:26 on 10-12): appends at 20:17:26 and at 01:19:02 on 10-13, so 2. 2cb87e77 (spec only, read from 00:04:21 on 10-13): appends at 00:04:21 and 00:45:50, so 2 (00:06:18 adds no owner words). c4fc482f (spec and own file; starting ruling): appends at 03:18:48, 03:43:00, 12:49:18 and 13:28:50, so 4. 5f201b8e (spec only): first added 19:46:08 and an append at 21:52:33, so 2; its commits at 21:52:44 and 21:54:24 are not appends (listed). All form (2) or (3) only | FAIL: build record b835d08f FAIL by (iii) | pending |
| 53 | POOM #15 | random | No: records | – | – | – | – |
| 54 | POOM #24 | random | Yes | built (K3) | 0/0/0 | FAIL: 063b6a95 by (ii) | not reopened; 8 candidates |
| 55 | POOM #23 | random | No: records | – | – | – | – |
| 56 | POOM #14 | random | No: records | – | – | – | – |
| 57 | POOM #25 | random | Yes (E-K1) | plan (K3: plan 258, built 129) | 11/3/0. ad6df430 (spec and own file): first added 01:00:35 on 10-11 plus 2 appends, so 3. e219aae3 (spec only): first added 01:16:39 plus 4 appends (14:31:59, 18:46:24, 00:35:38 on 10-12 naming Q-013, which no named question file pairs with, and 01:20:59), so 5. 2cb87e77 (spec only): first added 01:16:42 plus 2 appends (15:43:07; 15:43:54 with 1 line left unmatched), so 3. All form (2) or (3) only | FAIL: plan record 03b9d86d FAIL by (i); build record 89151c4e not read for a plan piece | not reopened; 0 candidates |
| 58 | POOM #18 | random | Yes (E-K1) | built (K3: built 20, plan 2) | 0/0/0 | FAIL: d019f699 by (iii) | not reopened; 10 candidates |
| 59 | POOM #22 | random | Yes (E-K1) | built (K3: built 455, plan 106) | 0/0/0 | PASS: 7054833b by (iv) | not reopened; 4 candidates (#26, #27, #30, #49) |
| 60 | POOM #20 | random | Yes (E-K1; trailers name 3 briefs, the E-RP4 shape) | built (K2: `-tb-` short form, so tools-builder; briefs s-017 to s-019, no brief records) | 0/0/0 | FAIL: 48a85c6f by (iii), 5 rounds | not reopened; 10 candidates |
| 61 | SD commit 9e46dd84… | E-RP1 | No (no pull request): an agent commit with 2 parents and no files, 2026-10-01T02:21:54, a local merge | – | – | – | – |
| 62 | SD commit 04511022… | E-RP1 | No (no pull request): an agent commit with 1 parent and 4 records files, 2026-11-09T20:35:08 | – | – | – | – |
| 63 | SD #147 | E-RP2 | No (closed unmerged; owner closed it 2026-10-19T21:07:36; one commit touching an owner question or answer file) | – | RT3(b): no sampled piece's `rt3b_matches` names it | – | – |
| 64 | SD #174 | E-RP2 | No (closed unmerged; owner closed it 2026-10-21T00:30:05; no commits) | – | RT3(b): none in the sample | – | – |
| 65 | SD #316 | E-RP3 | No: other and records | – | – | – | – |
| 66 | ML #69 | E-RP3 | No: other (and records) | – | – | – | – |
| 67 | ML #98 | E-RP4 | Yes: one piece for briefs 258 and 263 (E-RP4) | plans (K2: both briefs are Definer by trailer role name; dispatched by brief record 258 at 18:23:13 on 11-11). K3 would give research (344 against plan 222), listed | 0/0/0. 357e6847 falls after the merge and is RT5(b). Intake item a62f6a50 listed | undecided, listed (Open question 12): its only record, c50bbebd, is unclassed | pending |
| 68 | SD #78 | E-K1 | Yes | built (K3: built over 6277, plan 5441, research 200) | 16/16/6. Decision d38d8364 (own file) is the starting ruling, but 15 appends fall in the window between 12:11:02 and 17:56:50 on 10-16. 5 of them hold form (1): 13:35:07, 17:05:56, 17:35:13, 17:39:03, 17:56:50. Decision 7d757252 (own file) adds 1 more: first added 20:29:14, form (1) | FAIL: 9c0ec757 by (i); 7e4cc02b and 36f50bca none | pending |
| 69 | SD #148 | E-K1 | Yes | plan (K3: plan 2533, built 73, research 42) | 1/1/1. Question file 552be005, by number, 21:43:10 on 10-19 | undecided, listed (Open question 12): only build-kind records (2b117140 FAIL and others), which are of another kind for a plan piece | pending |
| 70 | SD #36 | E-K2 | Yes | plans (K2: `-def-` short form, so Definer; brief s-001 with no record) | 0/0/0 | left out, listed | not reopened; 46 candidates |
| 71 | SD #319 | E-RT2 | No: records only | – | – | – | – |
| 72 | SD #300 | E-RT2 | Yes | research (K3) | 2/2/2. Question 76fc6d56 (spec and own file), 22:17:16 on 11-04. Question c2476643 (number, spec and own file), 16:24:30 on 11-05. Their decisions fall after the merge. Notes files e24f55f9 and 048d8585 not counted | FAIL: research record 9f16cd20 by (i); build record 8ec028d2 not read | pending |
| 73 | SD #52 | E-RR2 | Yes | built (K3) | 0/0/0. Every named record falls after the merge | FAIL: 6fc7083c by (iii) | not reopened; 49 candidates |
| 74 | SD #11 | E-RR2 | Yes | built (K3) | 0/0/0. Named records fall after the merge | FAIL: 2d2438a5 by (iii) | not reopened; 6 candidates |

Rules found nothing anywhere in the sample (fact, B):
- **RT1(b):** every comment under the owner's account (SD #6, #78, #11, #147, #174; POOM #35, #11, #30, #18) carries the agent footer, so it is the agent's (E-RT1). In Model-Lab no drawn pull request has a comment, so RT1(b) falls to the touch log, which holds nothing past, and no comment is listed beside it.
- **RT2(a):** every commit under the owner's identity is a web-editor commit of records files only, which RT2(a) does not count.
- **RT3(a):** GitHub has no reviews on these pull requests.
- **RT3(b):** every drawn piece's `rt3b_matches` is empty.

Rules untested, and why:
- **RT7, RT1(c), RT2(b) and RT3(c):** the touch log holds no past entries.
- **RR1(b):** the `Reopens:` mark cannot exist on past pieces.
- **RR1(c) and K4:** they apply to trials only.
- **RT6:** no counted touch rests on a record that also lands inside another drawn piece's window. For example, e219aae3's commit at 01:20:59 on 10-12 falls in both POOM #25's and #27's windows, but it is read only for #25.

## Cases I could not decide from the extract

1. **First check undecided (4 pieces).**
   - ML #93 and SD #148: their only check-kind records are of another kind (Open question 12).
   - ML #98: its only record is unclassed (Open question 12).
   - POOM #30: its build record gives no round-1 verdict (U3).
2. **Open question 11: records naming a piece only by being its own files.** These are counted and listed, but the extract has no text, so I cannot tell whether a record is about other work:
   - ML #29: 9acdfce2 and 5e700c74
   - ML #73: 9ea16fdb
   - ML #81: 30491519
   - SD #230: four question files
   - SD #26: b2697809
   - SD #78: d38d8364 and 7d757252
   - ML #93's question file 22147854 is also own-file only, but its paired decision names the piece by number.
3. **ML #29, the time of question 8628e3d2.** Its question file 197dd190 was first added at 23:58:10 on 11-01, inside #29's window, but it does not name #29. #29's commits only delete it, and its text does not name #29. So the touch is timed by the decision at 00:38:22 **(opinion)**. The count is 1 either way.
4. **Owner words in files the rules do not read.** These are listed only; whether they count turns on Open questions 2 and 15:
   - POOM ledger entries quoting the owner, inside the window:
     - #35: 5be98217 (spec)
     - #30: 56c65486 (names nothing), aa4bb0c6, f3a6b509, 9754623d (number and spec)
     - #50: 3b79e454
     - #49: 447cf875
     - #27: 71c48d9c and 3058ae12 (name nothing), 71ba6fcf, 4c0ded4f
     - #25: 8c0b9957, cf45170a
     - #22: 20cf0bd6
     - #20: d4f9e0fe, 0ccd2fd5, 689b54b0, 878518f1 (number)
   - The instruction file 104f5eb5 on POOM #50 (number and spec, 00:21:35 on 11-06), under RT7.
   - Intake items: b97ada67 on ML #92, a copy of an answer; a62f6a50 on ML #98.
   - SD #148's own other reference files: 1c669f9a, 96e547ef and bcc111f8 (21:02:09 on 10-19) and 0695bbf6 (13:56:12 on 10-20).
   - POOM #20, #22 and #50 have no touch today but each has such items naming them.
5. **RT3(b) for closed-unmerged pull requests.** The extract gives matches only from each merged piece's side, so I cannot tell whether SD #147's or #174's work later merged in a piece that was not drawn.
6. **E-RT5, thanks-only comments.** These cannot be judged, because no comment text is kept. No drawn comment is the owner's anyway.

## Awkward cases seen and not seen (sample.json `edge_case_part`)

- **Seen:**
  - E-RP1: two SD commits, a local merge and a direct push.
  - E-RP2: SD #147 and #174, both closed by the owner.
  - E-RP3: SD #316 and ML #69.
  - E-RP4: ML #98; POOM #20, drawn at random, has the same shape.
  - E-K1: SD #78 and #148, and 14 pieces drawn at random.
  - E-RT2: SD #319 (one commit) and #300 (11 commits); in the random part also POOM #25 (1) and #20 (3), plus SD #316 (4). All have a tool's default identity and no files changed, and none is a touch.
  - E-RR2: SD #52 and #11, and 11 more 30-day pieces with candidates.
  - The short-form table: SD #36 (`-def-`) and POOM #20 (`-tb-`).
- **Not seen:**
  - E-RP5. Five drawn pull requests were merged by a bot (SD #233, #105, #150, #109, #93), and none is a piece.
  - E-RP6: no "Revert" subject.
  - E-K2's own case: no trailer gives a role K2 does not map.
  - E-K3: no Service-Desk piece is dispatched by a control file.
  - E-RT1.
  - E-RT3: every owner web-editor commit changes records only.
- **Not sampled, left to the Critic:** E-RT4, E-RT5, E-RT6, E-RR1 and E-RR3. For E-RT5: 12 comments under the owner's account appear in the sample, and all carry the footer. SD #6, POOM #18 and SD #11 also have a session record showing they were posted.

## Records the rules say to list

- **RT5 left out:**
  - ML #29: 3ae73360 and 66512cad, "A phase gate".
  - ML #92: b3609d4c, "Part of a value target", inside the window.
  - ML #93: 4973eb45 and 56004034, after the merge, naming other rulings: "A phase gate, its ceilings, a value target's terms, the acceptance of open unknowns and of a milestone".
  - ML #43, all outside its window:
    - 58cc6884 and 7196c3a9, naming other rulings: "Touches the value target (term 1) and a rule change (term 4)".
    - d4f1074c and cddf5100: "A phase gate".
  - ML #98: 357e6847, "part of a value target", after the merge.
- **Counted with a gate milestone (Open question 13):** ML #29 9acdfce2 (Discovery-8); ML #93 22147854 and 31505fb6 (Discovery-8).
- **Not appends:**
  - SD #26: 233211a9 at 16:11:10.
  - POOM #27: 5f201b8e at 21:52:44 and at 21:54:24.
- **Starting rulings (RT4):** SD #341 8e21866a; SD #22 84ddb037; SD #26 233211a9; SD #31 ad5eedfa; POOM #35 0d5230c0; #50 df986385; #49 558fd054 and 08ba8ef8; #27 c4fc482f; SD #78 d38d8364.
- **`-notes.md` files not counted:** SD #22 84cee8be; SD #26 4782268e and 1d370480; SD #300 e24f55f9 and 048d8585.
- **Comments shown as posted by a session:**
  - SD #6, 1 comment (record 1b7a31cc)
  - POOM #18, 1 comment (record d019f699)
  - SD #11, 3 comments (record 2d2438a5)
- **First check left out (no record):** ML #29, #92, #78; SD #22, #61, #26, #25, #31, #36.
- **Observation (fact, B):** the build review records of SD #52 (6fc7083c), SD #11 (2d2438a5) and POOM #18 (d019f699) were committed under the owner's identity through the web editor. C1 classes a record by its path, whoever wrote it, so this changes no result.

## Question touches per piece, and the share

- **Pieces with question touches (today / no spec-only / no form-(2)-or-(3)-only):**
  - ML: #29 2/2/2, #93 1/1/1, #73 1/1/1, #81 1/1/1
  - SD: #230 4/4/4, #26 1/1/1, #78 16/16/6, #148 1/1/1, #300 2/2/2
  - POOM: #35 2/2/2, #30 5/3/0, #49 1/1/1, #27 10/4/0, #25 11/3/0
  - Every other piece: 0/0/0.
- **"At least one touch" with the variants:**
  - Without the spec-only records: no piece changes.
  - Without the form-(2)-or-(3)-only commits: three pieces drop to none, POOM #30, #27 and #25.
  - With both removed: the same three.
- **Question ids carried, with their pairing (RT1(a)):**
  - Q-024: question file 14b7aecb, paired with answer 0d5230c0's append at 17:59:31 (POOM #35).
  - Q-029: question file c4c7c231 and answer 558fd054.
  - Q-030: question file 5b41d98e and answer 08ba8ef8.
  - Q-031: question file de17627b and answer df986385.
  - Q-022: question file 74b08fff (POOM #32, not a piece).
  - The append on POOM #25 that names Q-013 has no named question file to pair with.
  - `question_id` is null on the `_owner-answers*.md` records (0d5230c0, 455192c4, 4efc6a60, e219aae3, 2cb87e77, c4fc482f, 5f201b8e, ad6df430); the extract gives such an id only for `_owner-answer-q<nnn>.md` files.
- **Share of pieces with at least one owner touch before merging, under the rules as they read today: 14 of 33.**
  - Random part: 11 of 26.
  - Edge-case part: 3 of 7.
  - By repository: ML 4 of 9, SD 5 of 13, POOM 5 of 11.
  - Without the form-(2)-or-(3)-only commits: 11 of 33.
  - Without the spec-only records: 14 of 33.
- **Missing or "not read" fields:** record and comment text (needed for Open question 11 and E-RT5); entries in the touch log (none from the past); RT5 class in SD and POOM (none at the cut-off, by design); later merges of closed-unmerged pull requests' work from their own side.

**Proposed library entries:** none. This memo applies fixed rules to one extract; it finds no general fact or pattern with a shelf life.

## Six-part contract

- **Changed:** nothing. I hold no write tool, and this memo is my return, to be recorded as research/Q-018-memo-4.md.
- **Why:** brief 308. Answer Q-018 from the extract alone, on the rules as brief 305 left them.
- **Verified:** I have no shell and ran no commands. Every result comes from Read and Grep over /home/user/Model-Lab/research/Q-018.md and over /home/user/Model-Lab/research/Q-018-extract/README.md, sample.json and sample.jsonl (fields: files, k2_roles, briefs, questions_decisions_named with window_commits, owner_account_comments, commits, c1_records, after_merge, rt3b_matches, owner_items_listed_in_window). Nothing has been checked against the repositories; that is the Critic's step 5.
- **Undone:**
  - The six undecided cases above.
  - The Critic's not-sampled cases: E-RT4, E-RT5, E-RT6, E-RR1, E-RR3.
  - Opening the E-RR2 candidates.
- **Needed outside my surface:**
  - The Critic's check of this coding (step 5).
  - The owner's rulings on Open questions 2, 3, 11, 12, 13 and 15, which move the results listed above.
- **Open questions:**
  - Should K3's "changed lines" be added plus removed lines (the reading used here) or added lines only? No result here changes either way.
  - Should RT1(a) time a paired question by the paired question file's first add inside the window when that file does not itself name the piece (ML #29)?
