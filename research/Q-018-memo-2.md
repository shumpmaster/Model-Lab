# Q-018 memo 2: the hand check re-coded on the corrected counting rules

Dated 2026-11-12. Researcher, brief 298. Sources: only research/Q-018.md and research/Q-018-extract/ (README.md, sample.json, sample.jsonl, and Service-Desk.U.jsonl, read once to confirm the closed-unmerged rows). No web, no other files.

## What this found

All 74 drawn items were coded. 34 of them are pieces. The other 40 are not: 36 merged pull requests that only change records, owner questions or answers, or other files; 2 commits that landed with no pull request; and 2 pull requests closed without merging. Across the 34 pieces, 12 have at least one question touch from the question and decision records, 25 touches in all. No piece has a fix touch, a send-back touch or a counted comment touch. Every owner-account comment in the sample carries the agent footer, so each one counts as the agent's. For the first independent check, 16 pieces fail round 1, 4 pass, 4 are undecided and listed, and 10 have no check record and are left out of that measure only. No piece is reopened. 13 pieces have had their full 30 days and are not reopened; the other 21 are still pending.

Some things could not be decided from the extract:
- Whether records that name a piece only by being one of its own files are about other work (Open question 11). The text is not in the extract, so they are counted and listed.
- For one Personal-Org-Operating-Model piece, the exact trailer short form. The kind comes out the same either way.
- Whether the one Model-Lab piece whose only check record is unclassed is "undecided" or "left out".
- Whether any later shared-file pull request reverts or fixes a sampled piece in other words. That is the Critic's step.
- Comment touches in Model-Lab, which by rule come from the touch log. The log holds no past touches, so they are untested.

## Reading notes (all from the extract; grades given per statement class)

- **Fact (grade A, field read directly):** frame, repository, number, drawn_as, merged_at, dispatch and dispatch_from, each file's K1 class and line counts, briefs and trailer roles, `questions_decisions_named` with its `window_commits`, `rt5_reading`/`rt5_class`, `standard_milestones`, `c1_records`, `owner_account_comments`, `rt3b_matches` and `after_merge`.
- **Estimate (grade B, my application of the rules to those fields):** kind by K3, the touch counts, the C1 result and the RR status.
- **K3 "most changed lines":** I counted added plus removed lines. Using added lines alone changes no piece's kind.
- **Window:** after dispatch, not at it, and up to and including the merge.
- **Rounds:** a `rounds` of 0 means "the record names no round".
- **Fields that are absent or not read:**
  - The text of trailers: only the brief number, and a role that is null for short forms.
  - Record text, so whether a record is "about other work".
  - Real paths, so whether a research piece has a memo.
  - Reviews and comments on undrawn pull requests ("not read", README).
  - Forward closed-unmerged matches for unsampled pieces.
- **Rules that find nothing in past records, untested:** RT7, RT1(c), RT2(b) and RT3(c) (the touch log); RR1(b) (no `Reopens:` marks exist); RR1(c) (trial pieces only); K4 (trials only).
- **Reviews:** no pull request has a review (README, github_reads.json), so RT3(a), and the review half of RT1(b), find none anywhere.
- **Owner-identity commits:** every owner commit in the sample is a GitHub web-editor commit that changes only K1 records files. So RT2(a) finds none, and E-RT1 and E-RT3 are not seen.
- **Reverts:** no commit in any sampled row has a "Revert" subject or names a reverted commit, and no `Reopens:` mark exists. So RR1(a) finds nothing.

## Every drawn item

Key: P = piece (RP1 and RP2); N = not a piece; T = touches counted (rule, record label, time); C1 = first check; RR = reopening status. "Own file only" means the record names the piece only by being one of its own files (listed for Open question 11).

### Model-Lab, random part (20, drawn by the seeded SHA-256 order)

| Item | Files (K1) | RP | Kind | Touches | C1 | RR |
|---|---|---|---|---|---|---|
| #61 | records | N (RP2) | – | – | – | – |
| #43 | plan 347 lines, research 168 | P | plan (K3; E-K1 type) | none: no named record first added or appended in its window | FAIL: plan.md 0df9522f, reading (ii), 5 rounds; 3 unclassed records listed (02002bc5, 5fa6595b, 7e3de039) | pending; candidates #44, #51 |
| #29 | plan 301 | P | plan (K3) | 2× RT1(a). (1) question 8628e3d2: decision 9acdfce2 first added 2026-11-02 00:38:22 with an owner-words line; class "Accepting an unknown as open", reading (c); milestone Discovery-8, so listed (Open question 13); own file only. (2) question 24955290: question file 5e700c74 first added 00:43:43; class "A milestone mark", reading (c); own file only. Left out by RT5(b): question b96c30cc (3ae73360, class exactly "A phase gate"). | left out: no record of any kind, listed | pending; candidates #31, #39, #44, #51; later commit b6d588c8 names #29 |
| #58 | owner Q/A, records | N | – | – | – | – |
| #92 | plan 10 | P | plan (K3) | none. Question 087a5be7 (086b9225 and b3609d4c; owner words at 02:32:58, in the window) has class exactly "Part of a value target", so RT5(b) leaves it out. | left out: no record, listed | pending; candidates #93, #97, #98 |
| #64 | records | N | – | – | – | – |
| #93 | plan 232 | P | plan (K3) | 1× RT1(a): question 0d05d5f2, question file 22147854 first added 2026-11-11 03:08:30 (own file), with its decision 31505fb6 (owner words at 03:50:31, names #93) counted as the same question. No class, reading (d), name holds no gate word; milestone Discovery-8, so listed (Open question 13). Question 523aa41e is first added after the merge. | undecided, listed (Q-018/U2, Open question 12): only records of another kind. These are a build review, cdb3e6dc, round 1 PASS, which is not a plan check; two P-card Critic checks; and 1 unclassed record. | pending; candidates #94, #97, #98; later commits 5aefa062, e9f1f2f5, 130e78ac, 75ccb647 |
| #13 | research 39 | P | research (K3) | none | FAIL: source check f33fac53 FAIL (ii) and Critic check 0f1c0335 FAIL (ii) | pending; later commit 1bfb69e9 |
| #25 | owner Q/A | N | – | – | – | – |
| #47 | owner Q/A, records | N | – | – | – | – |
| #73 | research 716 | P | research (K3) | 1× RT1(a): question 9915ab5c, file 9ea16fdb first added 2026-11-08 19:53:21; reading (d); own file only | FAIL: be10cf2b FAIL and 4241d270 FAIL, both (ii) | pending; candidate #74 |
| #77 | owner Q/A | N | – | – | – | – |
| #55 | records | N | – | – | – | – |
| #59 | owner Q/A | N | – | – | – | – |
| #42 | records, owner Q/A | N | – | – | – | – |
| #56 | owner Q/A | N | – | – | – | – |
| #81 | research | P | research (K3) | 1× RT1(a): question 813d3838, file 30491519 first added 2026-11-09 05:32:16; reading (d); own file only | FAIL: cba2f3bb FAIL and 41905828 FAIL, both (ii) | pending; candidate #82 |
| #27 | records | N | – | – | – | – |
| #78 | research 103 | P | research (K3) | none | left out: no record, listed | pending; no candidates |
| #32 | records | N | – | – | – | – |

RT1(b) in Model-Lab: none of the sampled pull requests has a comment. By rule it is counted from the touch log, which holds no past touches, so it is **untested** for every Model-Lab piece.

### Service-Desk, random part (20: 10 with their 30 days complete, 10 without)

| Item | Files | RP | Kind | Touches | C1 | RR |
|---|---|---|---|---|---|---|
| #233 | owner Q/A (deleted) | N | – | – (merged by a bot) | – | – |
| #230 | built 596, plan 41 | P | built (K3; E-K1 type) | 4× RT1(a), all question files and all own file only, reading (d): 1bf7e881 (b793d0d9) at 2026-10-25 09:40:32; 45dac543 (6ab2fa98) at 09:40:32; 87fdbd6f (446c689a) at 09:40:32; a543f851 (e469c207) at 09:48:17 | FAIL: reviewer.md 8eae195c FAIL (ii); stage review 23917e4b FAIL (i); 96463ddc gives none; 3 records of another kind (design and similar names) listed | pending; 21 candidates (#231 to #257) |
| #105 | owner Q/A | N | – | – (bot merge) | – | – |
| #76 | owner Q/A | N | – | – | – | – |
| #237 | research 16 | P | research (K3) | 5× RT1(a), question files first added 2026-10-25 15:41:24, all own file only, reading (d): cc9cba8c, 0d3493dd, bb7ca514, cf3937cf, f940100f. Their decisions are added at 16:13:52, after the merge. | left out: no record, listed | pending; candidate #238; later commit de894bb0 |
| #150 | owner Q/A | N | – | – (bot merge) | – | – |
| #109 | owner Q/A | N | – | – (bot merge) | – | – |
| #341 | built 24 | P | built (K3) | none. Decision 8e21866a was first added in the piece's first commit, at its dispatch, so it is the ruling that started the piece (RT4, Q-018/U1). Its question file ebaa8dbe was filed earlier and is read for the piece only from that same instant. | PASS: 3ea324e4 PASS (iv), rounds 0; 69809936 gives none (rounds 0); 1 record of another kind (d357cc26) | pending; candidate #342; later commits edfdc13a, d2c8a200, 461b9f72 |
| #93 | records | N | – | – (bot merge) | – | – |
| #329 | records | N | – | – | – | – |
| #22 | plan 13, owner Q/A | P | plan (K3) | none. 84cee8be is a `-notes.md` file; 84ddb037 was first added in the first commit (RT4). | left out: no record | **not reopened** (30 days complete); 30 candidates (#23 to #260) |
| #51 | records | N | – | – | – | – |
| #21 | owner Q/A | N | – | – | – | – |
| #61 | plan 1471, research 28 | P | plan (K3; E-K1 type) | none | left out: no record | **not reopened**; candidates #66, #69, #72 |
| #26 | plan 196 | P | plan (K3) | 2× RT1(a), both own file only. (1) Question 64200268: decision 233211a9 was first added in the first commit (RT4); its append at 2026-10-04 16:11:10 adds an owner-words line and counts, while the append at 16:25:20 adds none. (2) Question 64fbc9af: decision b2697809 first added at 16:11:10 with an owner-words line. Not counted: two `-notes.md` files, 4782268e and 1d370480. | left out: no record | **not reopened**; 29 candidates (#28 to #260) |
| #57 | records | N | – | – | – | – |
| #25 | plan 80 | P | plan (K3) | none | left out: no record | **not reopened**; 30 candidates (#26 to #260) |
| #6 | records, other | N (E-RP3 type) | – | not a piece. Its 1 owner-account comment carries the footer, and a session record (1b7a31cc) shows it posted, so it is the agent's. | – | – |
| #31 | plan 12, owner Q/A | P | plan (K3) | none. Decision ad5eedfa was first added in the first commit (RT4). | left out: no record | **not reopened**; 22 candidates (#39 to #282) |
| #47 | records | N | – | – | – | – |

### Personal-Org-Operating-Model, random part (20)

| Item | Files | RP | Kind | Touches | C1 | RR |
|---|---|---|---|---|---|---|
| #35 | built 3527, plan 634 | P | built (K3; E-K1 type) | 1× RT1(a): question c118231f, file 14b7aecb first added 2026-10-17 16:19:03; names it by spec and own file; reading (d). The 1 owner-account comment carries the footer, so it is the agent's (no session record). | FAIL: build review round-1 file 675ec21d FAIL (i); 66417607 and a501ea2c give none. Plan records (6edad31a FAIL and others) are of another kind and not read. | pending; candidates #38, #46, #49, #50 |
| #11 | records | N | – | 1 comment with the footer (agent's) | – | – |
| #47 | plan 120 | P | plan (K3) | none: question c4c7c231 is first added after the merge | FAIL: 65934264 FAIL (i); 594ac4bd and 2e369272 give none. Build records are not read. | pending; candidate #49 |
| #19 | records | N | – | – | – | – |
| #32 | records, owner Q/A | N | – | – | – | – |
| #52 | records | N | – | – | – | – |
| #30 | built 588, plan 149 | P | built (K3) | none. Its 2 owner-account comments carry the footer, so they are the agent's. | undecided, listed (Q-018/U3): its only build record, 63a11d59 (rounds 4), gives no round-1 verdict. Its plan records (b487cfbc FAIL and others) are of another kind. | pending; candidates #34, #35, #38, #46, #49, #50; later commit d34a7fd4 |
| #48 | owner Q/A, records | N | – | – | – | – |
| #53 | records | N | – | – | – | – |
| #50 | built 175, plan 4 | P | built (K3) | none: 5b41d98e and de17627b were both first added before dispatch, with no append in the window | PASS: 3fed3942 PASS (iv) and f5ba9a62 PASS (i). Plan FAILs (6ee73633) are of another kind. | pending; no candidates |
| #49 | built 547, plan 109 | P | built (K3) | 1× RT1(a): question 86e7e557, file de17627b first added 2026-11-05 16:38:01; spec and own file; reading (d) | PASS: 0e5d0a2e and f5ba9a62 PASS (i); cdb45b88 gives none. Plan FAILs are of another kind. | pending; candidate #50 |
| #27 | built 2520, plan 1066 | P | built (K3) | none | FAIL: b835d08f FAIL (iii) | pending; 10 candidates |
| #15 | records | N | – | – | – | – |
| #24 | built | P | built (K3) | none | FAIL: 063b6a95 FAIL (ii) | **not reopened**; 8 candidates |
| #23 | records | N | – | – | – | – |
| #14 | records | N | – | – | – | – |
| #25 | plan 258, built 129 | P | plan (K3) | none | FAIL: 03b9d86d FAIL (i); four later-round records give none. Build record 89151c4e is of another kind (rounds 0). | **not reopened**; no candidates |
| #18 | built 20, plan 2 | P | built (K3) | none. The 1 owner-account comment has the footer and a session record (d019f699), so it is the agent's. | FAIL: d019f699 FAIL (iii) | **not reopened**; 10 candidates |
| #22 | built 455, plan 106 | P | built (K3) | none | PASS: 7054833b PASS (iv), rounds 0 | **not reopened**; candidates #26, #27, #30, #49 |
| #20 | built 2110, plan 235 | P | built: K2 by the `-tb-` short form (estimate, see the undecided cases); K3 gives built too | none | FAIL: 48a85c6f FAIL (iii), 5 rounds | **not reopened**; 10 candidates |

### Edge-case part (14, the first matches in seeded order not already drawn)

| Item | Drawn as | RP | Kind | Touches | C1 | RR |
|---|---|---|---|---|---|---|
| Service-Desk commit 9e46dd84 (2 parents, agent, no files, 2026-10-01) | E-RP1 | N (no pull request); counted apart: Service-Desk, 2026-10 | – | – | – | – |
| Service-Desk commit 04511022 (agent, records, 2026-11-09) | E-RP1 | N; counted apart: Service-Desk, 2026-11 | – | – | – | – |
| Service-Desk #147 (closed by the owner; 1 commit, owner Q/A) | E-RP2 | N | – | its 1 comment has the footer (agent's). RT3(b): it matches no sampled piece. | – | – |
| Service-Desk #174 (closed by the owner; no own commits) | E-RP2 | N | – | as for #147 | – | – |
| Service-Desk #316 | E-RP3 | N (records, other) | – | – | – | – |
| Model-Lab #69 | E-RP3 | N (records, other) | – | – | – | – |
| Model-Lab #98 | E-RP4 (briefs 258 and 263) | P (one piece, E-RP4) | **plans (K2: both briefs are Definer).** K3 would give research (344 lines against 222 of plan), so this is listed. | none: question 357e6847 is first added after the merge. Dispatched by brief record 258 at 2026-11-11 18:23:13. | undecided, listed: its only record, c50bbebd, is unclassed (see the undecided cases) | pending; candidate #99 |
| Service-Desk #78 | E-K1 | P | built (K3) | 1× RT1(a): question 4bec8cdd, decision 7d757252 first added 2026-10-16 20:29:14 with 2 owner-words lines; own file only. d38d8364 was first added in the first commit (RT4). The 1 owner-account comment has the footer (agent's). | FAIL: 9c0ec757 FAIL (i); 7e4cc02b and 36f50bca give none. Plan records (7e1da1a6 FAIL and others) are not read. | pending; 72 candidates (#79 to #304) |
| Service-Desk #148 | E-K1 | P | plan (K3: plan 2533, research 163, built 73) | 1× RT1(a): question 692b8dc7, file 552be005 first added 2026-10-19 21:43:10; names #148 by number; reading (d) | undecided, listed (Open question 12): only build-kind records (2b117140 FAIL (i), and others) plus 4 of another kind | pending; 10 candidates |
| Service-Desk #36 | E-K2 | P | plans (K2 via the `-def-` short form; README says so); K3 gives plans too | none | left out: no record | **not reopened**; 46 candidates |
| Service-Desk #319 | E-RT2 | N (records) | – | – (1 commit with author class other: not a touch, listed) | – | – |
| Service-Desk #300 | E-RT2 | P | research (K3) | 2× RT1(a): question 4bc380fd, file 76fc6d56 first added 2026-11-04 22:17:16 (spec, own file); question 96ef8dad, file c2476643 first added 2026-11-05 16:24:30 (number, spec, own file). Not counted: e24f55f9, a notes file. Its decisions come after the merge. | FAIL: Critic check of a question, 9f16cd20, FAIL (i); 3 later-round records give none. Build 8ec028d2 PASS is of another kind; 5 unclassed records and 8 of another kind are listed. | pending; candidates #310, #316, #320; later commits ef83ea7b, 340bdca7 |
| Service-Desk #52 | E-RR2 | P | built (K3) | none | FAIL: 6fc7083c FAIL (iii) | **not reopened**; 51 candidates (#72 to #253) |
| Service-Desk #11 | E-RR2 | P | built (K3) | none. Its 3 owner-account comments have the footer and a session record (2d2438a5), so they are the agent's. | FAIL: 2d2438a5 FAIL (iii) | **not reopened**; candidates #14, #18, #27, #48, #65, #148 |

## Cases I could not decide, and why

1. **Personal-Org-Operating-Model #20, the K2 short form.** The extract gives briefs s-017, s-018 and s-019 with a null role, not the trailer text. The table in rule K2 names `-tb-s017` to `-tb-s019` in this repository, so I read it as tools-builder, giving built work (estimate, grade B). K3 also gives built, so the result does not depend on it.
2. **Model-Lab #98, the C1 result.** Its only record is unclassed. C1 says a piece with only records "of another kind" is undecided, and one with no record of any kind is left out. An unclassed record is neither of those exactly. I coded it undecided and listed it.
3. **Open question 11.** The extract has no record text, so whether a record that names a piece only as its own file is "about other work" cannot be read. These are counted under the rules as they read today and listed (below).
4. **Whose check counts for research pieces (Model-Lab #13, #73, #81; Service-Desk #300).** C1 picks the Source checker's check when a memo exists and the Critic's when none does. The extract does not say whether the piece has a memo. Every research-kind record that gives a round-1 verdict here is FAIL, so the result is the same either way.
5. **RT3(b) for #147 and #174.** No sampled piece's `rt3b_matches` names them. Whether their work merged later in an unsampled pull request is not in the sampled rows.
6. **E-RR1 and E-RR3.** Whether any E-RR2 candidate reverts or fixes a sampled piece in other words needs the records' text. That is the Critic's step.
7. **RT1(b) in Model-Lab** is untested: by rule it comes from the touch log.
8. **Pending pieces.** 21 pieces cannot be judged for reopening until their 30 days pass (RR3).

## Sampled awkward cases, seen and not seen

- **Seen:**
  - E-RP1: 2 commits.
  - E-RP2: #147 and #174.
  - E-RP3: Service-Desk #316 and Model-Lab #69, plus Service-Desk #6 in the random part.
  - E-RP4: Model-Lab #98.
  - E-K1: Service-Desk #78 and #148, and in the random part Model-Lab #43; Service-Desk #230 and #61; Personal-Org-Operating-Model #35, #30, #50, #49, #27, #25, #18, #22 and #20.
  - E-RT2: Service-Desk #319 and #300, and in the random part Personal-Org-Operating-Model #25 and #20.
  - E-RR2: Service-Desk #52 and #11.
- **Drawn as E-K2 but not an E-K2 case:** Service-Desk #36. Its `-def-` is in K2's table, so it tests the short-form table. E-K2 itself, a trailer role K2 does not map, is **not seen** on any sampled item.
- **Not seen:** E-RP5, E-RP6, E-K3, E-RT1, E-RT3. On E-RP5: the bot merges seen (Service-Desk #233, #105, #150, #109, #93) are all non-pieces, and a bot's merge is not a touch anyway.
- **Not sampled (Critic's step 5):** E-RT4, E-RT5, E-RT6, E-RR1, E-RR3. For E-RT5, the extract shows every owner-account comment in the sample carrying the footer: 16 comments on 11 pull requests.

## Records the rules say to list

- **Counted and named only as the piece's own file (Open question 11):**
  - Model-Lab #29: 9acdfce2 and 5e700c74.
  - Model-Lab #93: 22147854. Its paired decision names the piece by number.
  - Model-Lab #73: 9ea16fdb.
  - Model-Lab #81: 30491519.
  - Service-Desk #230: b793d0d9, 6ab2fa98, 446c689a, e469c207.
  - Service-Desk #237: b0dc8e16, d184bc0b, f24d03df, 9e91287e, 2780ba86.
  - Service-Desk #26: 233211a9 (its append) and b2697809.
  - Service-Desk #78: 7d757252.
- **Counted although their milestone is a gate one (Open question 13):** Model-Lab #29's 9acdfce2 (Discovery-8, class "Accepting an unknown as open") and Model-Lab #93's 22147854 and 31505fb6 (Discovery-8, no class).
- **Left out by RT5(b) inside a sampled window:** Model-Lab #29's 3ae73360 ("A phase gate") and Model-Lab #92's 086b9225 and b3609d4c ("Part of a value target"). Both classes are exact forms, so neither is listed as naming other rulings. Records whose class names other rulings appear only outside any window: Model-Lab #43's 58cc6884 and 7196c3a9 ("Touches the value target (term 1) and a rule change (term 4)"), and Model-Lab #93's 4973eb45 and 56004034 ("A phase gate, its ceilings, a value target's terms, …").
- **Rulings that started the piece (RT4, Q-018/U1), not counted:** Service-Desk #341's 8e21866a, #22's 84ddb037, #26's 233211a9 as first added, #31's ad5eedfa, and #78's d38d8364.
- **Notes files, not counted:** Service-Desk #22's 84cee8be, #26's 4782268e and 1d370480, #300's e24f55f9, and on non-windowed records of #52 and #11, 7de704c9, be649c32 and a1d1c4c9.
- **Agent comments under the owner's account (E-RT1, E-RT5), all with the footer:**
  - With a session record as well: Service-Desk #6 (1), Personal-Org-Operating-Model #18 (1) and Service-Desk #11 (3).
  - Footer only: Personal-Org-Operating-Model #35 (1), #11 (1) and #30 (2); Service-Desk #78 (1), #147 (1) and #174 (1).
- **Unclassed or other-kind check records:** as given per item above. One record's statement skipped a branch: on Model-Lab #58, record f14c0d97 skipped head branch 33528900, which heads #55 and #61.
- **Owner-identity web-editor commits adding records only (not touches):** these appear on Service-Desk #6, #52 and #11, Personal-Org-Operating-Model #18 and others. Among the files they add are the build-review records that C1 reads (1b7a31cc, 6fc7083c, 2d2438a5, d019f699). This is a reading of the fields, not a rule result.
- **Pieces with no check record, left out of C1 only:** Model-Lab #29, #92 and #78; Service-Desk #237, #22, #61, #26, #25, #31 and #36.

## Proposed library entries

None. This memo codes one sample against one frozen spec and finds no general fact or pattern with a shelf life beyond it.

## Six-part contract

- **Changed:** nothing; I hold no write tool. This memo is to be recorded verbatim as research/Q-018-memo-2.md.
- **Why:** brief 298 asked for Q-018 to be re-coded on S-002's corrected rules from the extract alone.
- **Verified:** read-only Grep and Read on /home/user/Model-Lab/research/Q-018.md and /home/user/Model-Lab/research/Q-018-extract/ (README.md, sample.json, sample.jsonl, and Service-Desk.U.jsonl once). No commands run, no web.
- **Undone:**
  - E-RT4, E-RT5, E-RR1 and E-RR3: the Critic's step 5.
  - Model-Lab RT1(b): the touch log.
  - The 21 pending reopenings.
- **Needed outside my lane:** the Critic should check the coding against the records, especially Service-Desk #230 and #237's own-file question files and Model-Lab #98's unclassed record c50bbebd.
- **Open questions:**
  - Open questions 11, 12 and 13, as listed above.
  - Whether an unclassed-only piece is "undecided" or "left out" under C1; the rule's text does not say.
  - Whether trailer short forms should be carried in the extract, so that K2 can be read without the inference made for Personal-Org-Operating-Model #20.
