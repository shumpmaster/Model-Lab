# Q-018 memo 3: the hand check re-coded on the counting rules as brief 300 left them

Date: 2026-11-12. Researcher, brief 303. Sources: research/Q-018.md (the rules, verbatim at S-002 c9b2e25) and research/Q-018-extract/ (README.md, sample.json, sample.jsonl, and, for two checks, every `*.M.jsonl` file and frames.json). I used no web, no memory and no other file. Every coded result below is a **fact read from the extract**, graded **B (one source, the extract; not checked against the repositories)**, unless it is marked *estimate* or *opinion*.

## What this found and what it could not decide

The 74 drawn items are 70 merged pull requests, 2 pull requests closed unmerged and 2 commits with no pull request. 34 of them are pieces of work: 27 of the 60 random draws and 7 of the 14 edge-case draws. Under the rules as they read today, 12 of the 27 randomly drawn pieces (44%) had at least one owner touch before merging; across all 34 pieces it is 15. Every touch found is a question or an answer in the records (RT1(a)). No owner comment, owner fix or send-back was found. All 12 comments posted under the owner's account carry the agent footer, so they are the agent's. There are no reviews on GitHub. Every owner web-editor commit adds only records. Two readings move the count. Records that name a piece only by its spec id lower the number of touches but change no piece's yes-or-no. Answer lines in the quoted forms (2) or (3) carry every touch on three Personal-Org-Operating-Model pieces. Without them the random share falls to 9 of 27 (33%). I could not decide five things. The first is whether one Personal-Org-Operating-Model answer pairs with a question file, because the question ids are hashed; it moves a count from 3 to 2 and no yes-or-no. The second is four first-check results the rules leave undecided. The third is whether records that name a piece only by being its own file talk about other work (Open question 11), which needs text the extract does not hold. The fourth is how often the agent-footer comments overstate stepping in, and the fifth is whether a later pull request reverts or fixes a piece in other words; the Critic reads those. Nothing here is irreversible.

## 1. Every drawn item, with its result under each rule

Short names: ML is Model-Lab, SD is Service-Desk, POM is Personal-Org-Operating-Model. "nap" means not a piece (RP1 merged, RP2 fails: no built, plan or research file), so K, RT, C1 and RR do not apply. Every touch is RT1(a) unless another rule is named. Record labels and commit times (UTC) are the extract's. "own" means the record names the piece by being one of its own files, which is listed under Open question 11. "spec" means it names the piece by spec id. "No." is the sample.jsonl line.

| No. | Item, drawn as | RP | Kind (rule) | Touches before merge (rule, record, time) | C1 | RR |
|---|---|---|---|---|---|---|
| 1 | ML #61, random | nap | – | – | – | – |
| 2 | ML #43, random | piece | plans (K3: plan 347 lines, research 168; E-K1) | 0. 18 records name it only by spec; none is added inside the window (16:29:05–17:23:59) | FAIL (plan 0df9522f, (ii)); 3 unclassed records listed | pending |
| 3 | ML #29, random | piece | plans (K3) | 2: decision 9acdfce2, first add 11-02 00:38:22 (own; class "Accepting an unknown as open", RT5(c), gate milestone, listed under Open question 13); question 5e700c74, first add 00:43:43 (own). Question 3ae73360 is left out by RT5(b) ("A phase gate"), listed. Decisions b6081c5a and 66512cad fall after the merge | left out, no record (listed) | pending |
| 4 | ML #58, random | nap | – | – | – | – |
| 5 | ML #92, random | piece | plans (K3) | 0. Decision b3609d4c (02:32:58) is left out by RT5(b) ("Part of a value target"), listed. Intake copy b97ada67 (02:32:58) listed | left out | pending |
| 6 | ML #64, random | nap | – | – | – | – |
| 7 | ML #93, random | piece | plans (K3) | 1: question 22147854, first add 11-11 03:08:30 (own), answered by decision 31505fb6 at 03:50:31 (names it by number; the same question, U4). No class, RT5(d); gate milestone, listed under Open question 13. 4973eb45 and 56004034 fall after the merge, RT5(b) | undecided, listed (Open question 12): its only build record, cdb3e6dc (PASS), checks another kind of work; also 2 records of another kind and 1 unclassed | pending |
| 8 | ML #13, random | piece | research (K3) | 0 | FAIL (source check f33fac53 and Critic's check 0f1c0335, both (ii) FAIL; no memo, so the Critic's check is the one; FAIL either way) | pending |
| 9 | ML #25, random | nap | – | – | – | – |
| 10 | ML #47, random | nap | – | – | – | – |
| 11 | ML #73, random | piece | research (K3) | 1: question 9ea16fdb, 11-08 19:53:21 (own). Decision da219f2f falls after the merge | FAIL (be10cf2b and 4241d270, both (ii)) | pending |
| 12 | ML #77, random | nap | – | – | – | – |
| 13 | ML #55, random | nap | – | – | – | – |
| 14 | ML #59, random | nap | – | – | – | – |
| 15 | ML #42, random | nap | – | – | – | – |
| 16 | ML #56, random | nap | – | – | – | – |
| 17 | ML #81, random | piece | research (K3) | 1: question 30491519, 11-09 05:32:16 (own). Decision 9312a092 falls after the merge | FAIL (cba2f3bb and 41905828, both (ii)) | pending |
| 18 | ML #27, random | nap | – | – | – | – |
| 19 | ML #78, random | piece | research (K3) | 0 | left out | pending |
| 20 | ML #32, random | nap | – | – | – | – |
| 21 | SD #233, random | nap (merged by a bot) | – | – | – | – |
| 22 | SD #230, random | piece | built (K3: 596 lines against plan 41; E-K1) | 4: questions b793d0d9, 6ab2fa98 and 446c689a at 10-25 09:40:32, and e469c207 at 09:48:17 (all own) | FAIL (8eae195c (ii) FAIL; 23917e4b (i) FAIL; 96463ddc gives no round-1 verdict) | pending |
| 23 | SD #105, random | nap (bot) | – | – | – | – |
| 24 | SD #76, random | nap | – | – | – | – |
| 25 | SD #237, random | piece | research (K3) | 6: an append to answer record 5ae5d612 at 10-25 15:19:03 (6 owner-word lines, own, read from its own commit); questions b0dc8e16, d184bc0b, f24d03df, 9e91287e and 2780ba86 at 15:41:24 (own). Their decisions come at 16:13:52, after the merge | left out | pending |
| 26 | SD #150, random | nap (bot) | – | – | – | – |
| 27 | SD #109, random | nap (bot) | – | – | – | – |
| 28 | SD #341, random | piece | built (K3) | 0. Decision 8e21866a is added in its first commit (RT4) | PASS (3ea324e4, (iv); 69809936 gives none) | pending |
| 29 | SD #93, random | nap (bot) | – | – | – | – |
| 30 | SD #329, random | nap | – | – | – | – |
| 31 | SD #22, random | piece | plans (K3) | 0. 84ddb037 is RT4; 84cee8be is a notes file | left out | not reopened (28 E-RR2 candidates) |
| 32 | SD #51, random | nap | – | – | – | – |
| 33 | SD #21, random | nap | – | – | – | – |
| 34 | SD #61, random | piece | plans (K3: 1,471 lines against research 28; E-K1) | 0 | left out | not reopened (3 candidates: #66, #69, #72) |
| 35 | SD #26, random | piece | plans (K3) | 1: decision b2697809, first add 10-04 16:11:10 (1 line of form (1), own). 233211a9 is RT4; its 16:11:10 commit is not an append, listed. Notes files 4782268e and 1d370480 are left out | left out | not reopened (24) |
| 36 | SD #57, random | nap | – | – | – | – |
| 37 | SD #25, random | piece | plans (K3) | 0 | left out | not reopened (25) |
| 38 | SD #6, random | nap | – (1 owner-account comment: footer and a session record, so the agent's) | – | – | – |
| 39 | SD #31, random | piece | plans (K3) | 0. ad5eedfa is RT4 | left out | not reopened (22) |
| 40 | SD #47, random | nap | – | – | – | – |
| 41 | POM #35, random | piece | built (K3: 3,527 lines against plan 634; E-K1) | 3 (or 2, section 2): appends to answer record 0d5230c0 at 10-17 16:13:32 and 17:59:31 (the second names Q-024); question 14b7aecb at 16:19:03 (spec and own). The answer record's first add at the dispatch is RT4. One comment at 20:04:42 has the footer, so it is the agent's. The owner's web-editor commit at 20:33:11 adds records only. Ledger entry 5be98217 listed | FAIL (675ec21d (i)) | pending |
| 42 | POM #11, random | nap | – (1 footer comment; ledger entry 730a2fac listed) | – | – | – |
| 43 | POM #47, random | piece | plans (K3) | 0. Question c4c7c231 comes at 13:09:42, after the merge | FAIL (65934264 (i)) | pending |
| 44 | POM #19, random | nap | – | – | – | – |
| 45 | POM #32, random | nap | – | – | – | – |
| 46 | POM #52, random | nap | – | – | – | – |
| 47 | POM #30, random | piece | built (K3: 588 lines against plan 149; E-K1) | 5: answer record 455192c4, first add 10-13 20:24:30, appends 20:47:13 and 22:06:38 (spec and own); answer record 4efc6a60, first add 22:13:25 and append 23:15:11 (spec only). All are forms (2) or (3) only. 2 footer comments are the agent's. Ledger entries 56c65486, aa4bb0c6, f3a6b509 and 9754623d listed | undecided, listed (Q-018/U3): its build record 63a11d59 gives no round-1 verdict; its plan records are of another kind | pending |
| 48 | POM #48, random | nap | – | – | – | – |
| 49 | POM #53, random | nap | – | – | – | – |
| 50 | POM #50, random | piece | built (K3: 175 lines against 4) | 0. df986385 is RT4; the rest come before the dispatch. Ledger entry 3b79e454 and instruction file 104f5eb5 listed | PASS (3fed3942 (iv), f5ba9a62 (i)) | pending |
| 51 | POM #49, random | piece | built (K3: 547 lines against plan 109; E-K1) | 1: question de17627b at 11-05 16:38:01 (spec and own). Ledger entry 447cf875 listed | PASS (0e5d0a2e (i) and f5ba9a62 (i); cdb45b88 gives none) | pending |
| 52 | POM #27, random | piece | built (K3: 2,520 lines against plan 1,066; E-K1) | 10: e219aae3 appends at 10-12 20:17:26 and 10-13 01:19:02 (spec only); 2cb87e77 at 00:04:21 and 00:45:50 (spec only); c4fc482f at 03:18:48, 03:43:00, 12:49:18 and 13:28:50 (spec and own; its first add is RT4); 5f201b8e, first add 10-12 19:46:08 and append 21:52:33 (spec only). Its 21:52:44 and 21:54:24 commits are not appends, listed. All are forms (2) or (3) only. The owner's web-editor commit at 15:20:04 adds records only. 4 ledger entries listed | FAIL (b835d08f (iii)) | pending (its 30 days end 11-12 15:20, after the cut-off) |
| 53 | POM #15, random | nap | – | – | – | – |
| 54 | POM #24, random | piece | built (K3) | 0 | FAIL (063b6a95 (ii)) | not reopened (8) |
| 55 | POM #23, random | nap | – | – | – | – |
| 56 | POM #14, random | nap | – | – | – | – |
| 57 | POM #25, random | piece | plans (K3: 258 lines against built 129; E-K1) | 11: ad6df430, first add 10-11 01:00:35 and appends 14:31:36 and 15:42:40 (spec and own); e219aae3, first add 01:16:39 and appends 14:31:59, 18:46:24, 10-12 00:35:38 (names Q-013) and 01:20:59 (spec only); 2cb87e77, first add 01:16:42 and appends 15:43:07 and 15:43:54 (spec only). All are forms (2) or (3) only. E-RT2 commit 17:41:47 listed. Ledger entries 8c0b9957 and cf45170a listed | FAIL (03b9d86d (i)) | not reopened (0) |
| 58 | POM #18, random | piece | built (K3: 20 lines against 2; E-K1) | 0. 1 comment with footer and session record is the agent's | FAIL (d019f699 (iii)) | not reopened (10) |
| 59 | POM #22, random | piece | built (K3: 455 lines against 106; E-K1) | 0. Ledger entry 20cf0bd6 listed | PASS (7054833b (iv)) | not reopened (4) |
| 60 | POM #20, random | piece | built (K2: tools-builder by the short form `-tb-`, briefs s-017 to s-019, no brief records; E-K1) | 0. 3 E-RT2 commits listed. Ledger entries d4f9e0fe, 0ccd2fd5, 689b54b0 and 878518f1 listed | FAIL (48a85c6f (iii)) | not reopened (10) |
| 61 | SD commit 9e46dd841aa3, E-RP1 | not a piece (no pull request; a two-parent agent commit with no files) | – | – | – | – |
| 62 | SD commit 04511022f1a3, E-RP1 | not a piece (no pull request; an agent commit of 4 records files) | – | – | – | – |
| 63 | SD #147, E-RP2 | not a piece (closed unmerged by the owner, 10-19 21:07:36; 1 commit to an owner question-or-answer file) | – | RT3(b): no merged pull request matches it by head branch or brief (no frame M file in any repository has an `rt3b_matches` entry). 1 footer comment is the agent's | – | – |
| 64 | SD #174, E-RP2 | not a piece (closed unmerged by the owner, 10-21 00:30:05; no commits) | – | as #147 | – | – |
| 65 | SD #316, E-RP3 | nap | – | – | – | – |
| 66 | ML #69, E-RP3 | nap | – | – | – | – |
| 67 | ML #98, E-RP4 | one piece (two briefs, 258 and 263) | plans (K2: both briefs are definer briefs. Its files have more research lines, 344, than plan lines, 222; K4 would list this only in a trial) | 0. Dispatch is brief record 258 at 11-11 18:23:13; question 357e6847 comes after the merge (RT5(b)). Intake item a62f6a50 listed | undecided, listed (Open question 12): only c50bbebd, unclassed | pending |
| 68 | SD #78, E-K1 | piece | built (K3: built far above plan's 5,441 lines; also research 200) | 17: 16 appends to d38d8364 (its first add is RT4) at 10-16 12:11:02, 13:28:21, 13:35:07, 16:42:38, 4 at 16:42:39, 16:42:40, 16:42:53, 17:05:56, 17:21:23, 17:35:13, 17:39:03 and 17:56:50 (own); decision 7d757252, first add 20:29:14 (own). 1 footer comment is the agent's | FAIL (9c0ec757 (i)) | pending |
| 69 | SD #148, E-K1 | piece | plans (K3: 2,533 lines against built 73 and research 163) | 1: question 552be005 at 10-19 21:43:10 (number). 4 "other reference" owner files listed (they are the piece's own research-class files) | undecided, listed (Open question 12): build records such as 2b117140 (FAIL) check another kind of work | pending |
| 70 | SD #36, E-K2 (drawn) | piece | plans (K2, `-def-`, brief s-001 with no record). Read with the short forms, its role is in K2's list, so it is not a true E-K2 | 0 | left out | not reopened (46) |
| 71 | SD #319, E-RT2 | nap | – (1 E-RT2 commit listed) | – | – | – |
| 72 | SD #300, E-RT2 | piece | research (K3) | 2: question 76fc6d56 at 11-04 22:17:16 (spec and own); question c2476643 at 11-05 16:24:30 (number, spec and own). Decisions come at 11-06 16:40:44, after the merge. Notes files e24f55f9 and 048d8585 are left out. 11 E-RT2 commits listed | FAIL (Critic's check 9f16cd20 (i); no memo) | pending |
| 73 | SD #52, E-RR2 | piece | built (K3) | 0 | FAIL (6fc7083c (iii)) | not reopened (49) |
| 74 | SD #11, E-RR2 | piece | built (K3) | 0. 3 comments with footer and session record are the agent's | FAIL (2d2438a5 (iii)) | not reopened (6) |

Notes on rules across the sample:
- **RP1:** all 70 frame M items merged by merge commit (README).
- **RT2(a):** tested. 20 owner web-editor commits were found, and every one adds only records files, such as review records. None is a fix.
- **RT3(a):** untested. GitHub holds no review on any pull request (README).
- **RT3(b):** tested. No match exists.
- **RT6:** untested. No single touch fell on two sampled pieces.
- **RR1(a):** tested. There are no reverts and no "Revert" subjects in the sample.
- **Untested by design:** RR1(b), RR1(c), K4, RT1(c), RT2(b), RT3(c) and RT7.
- **RT1(b) in Model-Lab:** taken from the touch log; Model-Lab's sampled pull requests have no comments.

## 2. Touch counts per piece: today, without spec-only naming, without form-(2)/(3)-only commits

| Piece | Today | Without `names_only_by_spec` | Without `only_form_2_or_3` | Both removed | Does "at least one" change? |
|---|---|---|---|---|---|
| ML #29 | 2 | 2 | 2 | 2 | no |
| ML #93 | 1 | 1 | 1 | 1 | no |
| ML #73 | 1 | 1 | 1 | 1 | no |
| ML #81 | 1 | 1 | 1 | 1 | no |
| SD #230 | 4 | 4 | 4 | 4 | no |
| SD #237 | 6 | 6 | 6 | 6 | no |
| SD #26 | 1 | 1 | 1 | 1 | no |
| POM #35 | 3 (or 2) | 3 (or 2) | 3 (or 2) | 3 (or 2) | no |
| POM #30 | 5 | 3 | 0 | 0 | yes, with the form filter |
| POM #49 | 1 | 1 | 1 | 1 | no |
| POM #27 | 10 | 4 | 0 | 0 | yes, with the form filter |
| POM #25 | 11 | 3 | 0 | 0 | yes, with the form filter |
| SD #78 (edge) | 17 | 17 | 6 | 6 | no |
| SD #148 (edge) | 1 | 1 | 1 | 1 | no |
| SD #300 (edge) | 2 | 2 | 2 | 2 | no |

Every other piece has 0 under all four readings. A question file's first add carries no owner-word lines, so the form filter does not remove it.

## 3. The share (V1) under the rules as they read today

- **Random part:** 12 of 27 pieces (ML 4 of 8, SD 3 of 8, POM 5 of 11), 44.4%. This is a fact: a count. It is also 12 of 27 without spec-only naming, and 9 of 27 (33.3%) without form-(2)/(3)-only commits or with both readings removed.
- **All 34 pieces, edge cases included (not a random sample):** 15 of 34 today, and 12 of 34 without form-(2)/(3)-only commits.
- *Estimate:* if Open question 15 brought Personal-Org-Operating-Model's ledger entries in, POM #22 and #20 have listed in-window entries that name them by spec or number. They could move to at least one touch (random part up to 14 of 27), subject to the owner-words test, which the extract does not apply to ledger entries.

## 4. Cases I could not decide, and why

1. **POM #35's pairing.** Its 17:59:31 append names Q-024, and RT1(a) makes it one question with the Q-024 question file. The extract gives the question file's pairing label only as a hash (`609e0ca6`), so I cannot tell whether question 14b7aecb is Q-024. If it is, the count is 2; if not, 3. "At least one" holds either way. Field absent: the Q-id of each question file in clear.
2. **Open question 11.** These records name a piece only by being its own file, and the rules count them while that question is open: ML #29 (9acdfce2, 5e700c74), ML #93 (22147854), ML #73 (9ea16fdb), ML #81 (30491519), SD #230 (all 4), SD #237 (5ae5d612 and all 5 questions), SD #26 (b2697809) and SD #78 (d38d8364, 7d757252). Whether their text is about other work cannot be read: the extract holds no record text. All are counted and listed. *Estimate:* if all were dropped, ML #29, #73, #81, SD #230, #237, #26 and #78 would fall to 0, leaving 5 of 27 random pieces.
3. **C1 is undecided for four pieces.** ML #93, ML #98 and SD #148 have records only of another kind or unclassed (Open question 12). POM #30's only build record gives no round-1 verdict (Q-018/U3).
4. **E-RT5, E-RT4, E-RR1 and E-RR3 need record or comment text,** which the extract does not hold. They are for the Critic (step 5).
5. **E-RP1's count per month is not in the sample.** frames.json gives frame D totals only (ML 4, SD 566, POM 0).

## 5. Awkward cases seen and not seen (sample.json)

- **Seen:** E-RP1 (SD 9e46dd84, 04511022); E-RP2 (SD #147, #174); E-RP3 (SD #316, ML #69); E-RP4 (ML #98); E-K1 (drawn SD #78, #148, plus 14 more among the random pieces); E-RT2 (drawn SD #319, #300, plus random POM #25 and #20); E-RR2 (drawn SD #52, #11, plus candidates on every completed piece but POM #25).
- **Drawn as E-K2 but not a true E-K2:** SD #36 tests the `-def-` short form. No sampled trailer gives a role K2 does not map, and no unlisted short form was seen.
- **Not seen:** E-RP5, E-RP6, E-K3, E-RT1, E-RT3. Every owner-account comment carries the footer, so none counts under E-RT5.
- **Not sampled:** E-RT4, E-RT5, E-RT6, E-RR1, E-RR3.

## 6. Records the rules say to list

**Not an append (RT1(a))**
- SD #26: 233211a9 at 10-04 16:11:10 (a changed ruling matched away).
- POM #27: 5f201b8e at 21:52:44 and 21:54:24.

**Notes files left out**
- SD #22: 84cee8be.
- SD #26: 4782268e, 1d370480.
- SD #300: e24f55f9, 048d8585.
- SD #52: 7de704c9.
- SD #11: be649c32, a1d1c4c9.

**RT5(b), left out, with class**
- Inside a window:
  - ML #29: 3ae73360, "A phase gate".
  - ML #92: b3609d4c, "Part of a value target".
- Outside any window:
  - ML #43: 58cc6884 and 7196c3a9, "Touches the value target (term 1) and a rule change (term 4)", which names other rulings; d4f1074c and cddf5100, "A phase gate".
  - ML #93: 4973eb45 and 56004034, "A phase gate, its ceilings, a value target's terms, the acceptance of open unknowns and of a milestone", which names other rulings.
  - ML #98: 357e6847.

**Open question 13: counted, with a gate milestone**
- ML #29: 9acdfce2.
- ML #93: 22147854 and 31505fb6.

**Owner items listed only (RT7 and Open question 15)**
- ML #92: intake copy b97ada67.
- ML #98: intake item a62f6a50.
- SD #148: other reference files 1c669f9a, 96e547ef and bcc111f8 (10-19 21:02:09) and 0695bbf6 (10-20 13:56:12).
- POM #50: instruction file 104f5eb5.
- POM ledger entries quoting the owner: #35 (1), #30 (4), #50 (1), #49 (1), #27 (4), #25 (2), #22 (1), #20 (4).
- Non-pieces: ML #47 e9f4765b; ML #55 983a764d; POM #11 730a2fac.

**RT1(b) comments counted as the agent's (12 in all)**
- SD #6: 1, footer and session record.
- SD #11: 3, footer and session record.
- POM #18: 1, footer and session record.
- Footer only: POM #35 (1), POM #11 (1), POM #30 (2), SD #78 (1), SD #147 (1), SD #174 (1).

**E-RT2 commits, not touches**
- POM #25 (1), POM #20 (3), SD #316 (4), SD #319 (1), SD #300 (11). All carry an `Agent-Session:` trailer.

**C1**
- Left out (no record): ML #29, #92, #78; SD #237, #22, #61, #26, #25, #31, #36.
- Undecided: as section 4.
- Unclassed records: ML #43 (3), ML #93 (1), ML #98 (1), SD #300 (5).
- Statement skipped: one, on ML #58, a non-piece.

## 7. Fields absent or "not read"

- Record text, needed for Open question 11 and E-RT4.
- Question-file ids in clear, needed for POM pairing.
- Comment text.
- Review records' authorship. The owner's web-editor commits add the build records C1 reads for SD #52 (6fc7083c), SD #11 (2d2438a5) and POM #18 (d019f699). C1 reads them by path, "whoever wrote it".
- Frame D per month.

GitHub reviews are recorded as none, not as "not read".

## 8. Other observations (opinion, grade C)

SD #237's only research-class files, and SD #148's research files, are files under the design references folder, one of them an owner-answers record. So a piece can exist under RP2 because of the owner's own answer files. I report this without judging it.

## Proposed library entries (for the Source checker)

- **Fact (B, extract; shelf life until S-002 next changes; topics: V1, hand check, counting rules).** In the Q-018 random sample (27 pieces merged 2026-10-01 to 2026-11-12), 12 had at least one owner touch before merging under S-002 at c9b2e25. Without form-(2)/(3)-only commits the figure is 9, and without spec-only naming it is unchanged at 12.
- **Pattern (C, opinion from one sample; shelf life one revision of S-002; topics: counting rules, owner-answer paths).** In Personal-Org-Operating-Model, touch counts come almost entirely from per-spec answer records appended in the quoted forms and named by spec id. So the form-(2)/(3) reading, not the spec-id reading, decides those pieces' yes-or-no.

## Six-part contract

- **Changed:** nothing. I hold no write tool.
- **Why:** brief 303. The Orchestrator records this verbatim as research/Q-018-memo-3.md.
- **Verified:** Read and Grep only, no shell, over research/Q-018.md, the extract's README.md, sample.json, sample.jsonl, every `*.M.jsonl` file (a grep for `rt3b_matches`: no match) and frames.json (frame sizes). Line totals for K3 and the touch tallies are my own arithmetic on the grepped fields, not run code.
- **Undone:**
  - E-RT4, E-RT5, E-RR1 and E-RR3: the Critic, step 5.
  - The Q-024 pairing.
  - Open question 11 text reads.
  - Frame D per month.
- **Needed outside my surface:**
  - The Source checker, for the entries.
  - Whoever owns the extract, for the clear Q-ids of POM question files, if the pairing matters.
- **Open questions:**
  - Open questions 2, 3, 11, 12, 13 and 15, as named above.
  - Whether the owner's web-editor commits of build-review records should still count as independent checks: asked for the owner's view, not raised as a new rule.
