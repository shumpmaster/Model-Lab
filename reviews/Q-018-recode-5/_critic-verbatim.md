# The Critic's step 5 on memo 5's changed items (brief 334)

*Recorded verbatim by the Orchestrator; the verdict file is reviews/Q-018-recode-5/critic.md. Brief 334 (docs/briefs/334-critic.md), on Model-Lab@e0f8f50, research/Q-018-memo-5.md against the extract and records pack q018-pack-323.*

Verdict: PASS

Nothing failed, and nothing in the memo's counts needs to change. I checked memo 5's changed items against the extract and the records pack: the records that name a piece only by being its own file, every ledger entry it counts or skips, the four notes under the unasked-instruction code, and the two figures. Every count and every skip holds, and both figures (22 touches taken off; 2 pieces moved to not needing the owner, none back) re-add correctly. I found three slips of labelling in the memo that change no count, two limits worth adding to the list of what the rules cannot catch, and one small wording gap for the Definer. Two results rest on judgement calls the owner is already due to see listed: one piece's only touch is a question the two earlier Critics coded differently, and one of the two pieces that moved did so on a single code. Nothing here is irreversible.

## Findings

All are non-blocking. Record labels are the extract's; "sample line" is a line of `/home/user/Model-Lab/research/Q-018-extract/sample.jsonl`.

**Item 1 — records naming a piece only by being its own file (memo 4, item 2): coded right.**

1. Service-Desk #230's four question files (b793d0d9, 6ab2fa98, 446c689a at 543527d2; e469c207 at 21060101): "later work" is right under RT4. I opened all four. Each offers a change "built in a small change after G7b lands", beside "As built". None is a touch, so #230 has 0.
2. Model-Lab #29: decision 9acdfce2 (d7f8549a, 00:38:22, one `Ruling:` line, class "Accepting an unknown as open") is "this piece" and counts 1. Question file 5e700c74 (12454c30) asks whether milestone M1, the count of past work, is reached, which is other work than #29, so "later work" is right. Its append 45d2bfd4 adds no owner words. Opened both.
3. Model-Lab #73: question file 9ea16fdb (78f74919) is the eight-question shortlist. Its questions come from #73's own research, but they ask for the owner's preferences that "decide what the research looks at next and what the plan proposes", and ask no change to #73. "Later work" holds. This is a judgement, and #73 is one of the two pieces whose yes-or-no it changes.
4. Model-Lab #81: question file 30491519 (bdab1c50) is the stop-rule card on the two write-ups #81 carries, so "this piece" is right and it counts 1. It gives no RT5 class and its name holds no gate word, so RT5 does not leave it out. Opened.
5. Service-Desk #26 (b2697809, row 36, one unmatched owner line) and Service-Desk #78 (d38d8364's 15 appends, and 7d757252 at 1382e156): the memo applies the extract's codes ("this piece") correctly. I did not open b2697809 or 7d757252; I read d38d8364's headings only (finding 9).

**Item 2 — ledger entries: every count and skip is right under rulings 15 and 18.**

6. Checked against each entry's `names_by`, `own_file`, `same_words_in`, `same_words_in_start` and `asked_q` in sample lines 41, 47, 50, 51, 52, 57, 59 and 60, and against each entry's text in the pack.
   - **Counted, right:** #20's d4f9e0fe, 0ccd2fd5, 689b54b0 and 878518f1, and #22's 20cf0bd6 (each names the piece by spec, is its own file, and has no same words anywhere). #30's aa4bb0c6 also counts: its second passage stands in no record.
   - **Skipped, with the right record named:** #35 5be98217 (0d5230c0 at 17:59:31; also paired with Q-024 by `asked_q`); #30 f3a6b509 (455192c4 at 22:06:38); #50 3b79e454 (starting ruling df986385); #49 447cf875 (starting rulings 08ba8ef8, 558fd054, 959abcab, as the extract gives them; I did not open 959abcab); #27 71ba6fcf (c4fc482f at 03:43:00) and 4c0ded4f (c4fc482f at 13:28:50 and 12:49:18); #25 8c0b9957 (ad6df430 at 15:42:40) and cf45170a (all four passages in ad6df430).
   - **Not counted, right:** #30 56c65486 and #27 71c48d9c and 3058ae12 have empty `names_by`; #30 9754623d is coded "later work".
7. Wrong record named, count unchanged (memo line 132): the memo says 689b54b0's passage "stands in 0ccd2fd5's". It does not. 689b54b0 is L-0123, "Approve"; 0ccd2fd5 is L-0122, "Yes I want to skip noise"; the entry that holds "Approve" is d4f9e0fe, L-0121, as S-002 itself says. The extract carries no entry-against-entry field, so the Researcher could not have read this from it. Both entries count either way.
8. A seen case of step 6's limit (r), for the record: #30's aa4bb0c6 (L-0140) quotes "Approve and build (Recommended)", which 455192c4's append at 20:47:13 already holds, 15 seconds earlier. It escapes the skip only because its passage "Small follow-up fixes" appears in the answer record solely inside the agent's question text, in lower case. So #30's 4 touches include one answer counted twice. That is right by the rule's words and changes no yes-or-no.

**Item 3 — appends under RT7's code: right under ruling 16.**

9. Service-Desk #78: the four `notes_only: true` commits are 14d854aa, 01221fd4, 79afa01b and c0ab80c5 (rows 108, 110, 112, 114). In the pack's d38d8364, their lines sit under "Notes 3 to 9 …", "Notes 10 to 14 …", "Notes 22 to 24 …" and "Notes 19 to 21 …, the owner's message verbatim", none naming an answer or ruling. The other 12 stay under RT1(a) correctly: 5f6d7303 ("which also answers the question"), b8ca4c9c ("after the orchestrator's answer"), 5f36faa0 (answers and a note together), 7e3e6071 (an approval), and the rest answers. All 16 are "this piece". 12 + 4 = 16.

**Item 4 — the two figures: right.**

10. Touches taken off, 22. Recounted from the codes and each commit's `unmatched_owner_word_lines` and `read_for_piece`:

| Piece | Taken off | What |
|---|---|---|
| Model-Lab #29 | 1 | 5e700c74's first add |
| Model-Lab #73 | 1 | 9ea16fdb |
| Service-Desk #230 | 4 | four question files |
| Personal-Org-Operating-Model #30 | 2 | 4efc6a60, rows 48 and 49 |
| Personal-Org-Operating-Model #27 | 6 | rows 70, 71, 74, 76, 81, 82 |
| Personal-Org-Operating-Model #25 | 8 | rows 92 to 99 |

   On #27, rows 63 to 69, 72 and 73 are not read for the piece, row 75 adds no owner words, and rows 83 and 84 are not appends. The memo's reason that 9754623d takes nothing off is right: all three of its passages stand in 4efc6a60.
   - Code totals: 61 "later work" (11, 11, 39) and 3 "not said".
   - Touch totals: 42 with the codes (3, 20, 19) and 64 without (5, 24, 35).
   - Shares: 14 of 33 with, 16 of 33 without; random part 11 and 13 of 26.
11. Pieces changed: 2 to not needing (Model-Lab #73, Service-Desk #230), 0 back. Right. The one commit shared across two sampled pieces with codes on both (ebbc97b7, rows 63 and 96) carries the same code.
12. For the owner's list, not an error: Personal-Org-Operating-Model #49's only touch is question file de17627b (Q-031), coded "not said" because the two Critics differed. Its text asks approval of S-037, the work of #50, and L-0157 ("Asked as Q-031") is #50's entry. Counting it on #49 is right under ruling 17. Had the first Critic's "later work" stood, the figures would read 23 touches and 3 pieces. The memo lists the code (E, F4) but does not say #49's yes-or-no hangs on it.

**Item 5 — open questions.**

13. F1 (four pieces undecided on the first check): settled by C1's words and the owner's ruling in `/home/user/Model-Lab/decisions/questions/P-002-check-of-other-kind.md`. No gap.
14. F2 and question (2) (Service-Desk #300): settled by C1's words, "for a research piece with no memo (a research question or an experiment registration), the Critic's check of it". #300 has `has_memo: false`, and 9f16cd20 is its record by "experiment or question id" and by its own statement. FAIL stands.
15. F3 and question (1) (the unit of a touch): settled by RT1(a)'s words. A record's first add is "one question", and "each later commit that adds the owner's words … is one more", so the unit is the record's first add and then the commit. The limit this leaves, several answers in one first add or one commit counting once, is not in step 6's list (a) to (t); (e) covers only timing. For the Definer to add to that list, not for the owner.
16. Question (3), dispatch times:
    - Personal-Org-Operating-Model #20: settled. `record_exists` is false for s-017, s-018 and s-019, so by K2's short-form words the dispatch is the first commit.
    - Model-Lab #98: a small wording gap for the Definer. "What a touch is" says "the first commit that adds its brief record", in the singular, and does not say which record when a piece carries two briefs (258 at 18:23:13, 263 at 19:18:31). The extract takes the earlier. No count turns on it: #98 has 0 touches in the wider window, so 0 in the narrower.

**Item 6 — found in passing, outside item (6).**

17. Memo line 159: "POOM #53 (NP): c4c7c231 … 5b41d98e", rows 54 to 58. Those rows are on sample line 48, which is Personal-Org-Operating-Model #48; #53 is line 49. Both are non-pieces, so no count changes.
18. Memo line 173: "POOM #27 5b4e82a7 (11-12 21:52:44)" should read 10-12. The extract gives 5f201b8e's commits at 2026-10-12T21:52:44Z and 21:54:24Z, and 11-12 would be past the cut-off.

**Self-implication (D-050).** No finding implicates a check of this session's own. Findings 3 and 12 bear on the `later_work` codes of the Critics of briefs 328 and 330, which the brief says may share this session's model; I saw neither record and judged the codes only from the pack's texts. Finding 3 agrees with both; finding 12 leans to the first Critic's reading against the second's.

## Contract

- **changed:** nothing. Read only; no file written.
- **why:** brief 334, step 5 on memo 5's changed items (S-002, "What the owner's rulings of 2026-11-12 need of the hand check", item (6)).
- **verified:** by field searches (the session has no shell) of `/home/user/Model-Lab/research/Q-018-extract/sample.jsonl`: all 131 `later_work` codes with their rows; every `ledger_entries` entry of sample lines 41 to 60; the window commits of rows 33 to 41, 45 to 49, 60 to 99 and 107 to 122; dispatch and merge times; the `briefs` fields of lines 60, 67 and 70; and 9f16cd20's check record. In the pack at `/tmp/claude-0/-home-user/3bf22eb7-3034-5300-9273-72fad23a7eb4/scratchpad/q018-pack-323`: `CODING.md`; the full text of eight records in `records2/` (the four Service-Desk #230 question files and Model-Lab 5e700c74, 9ea16fdb, 30491519, 9acdfce2); the heading and `decided_by:` lines of 15 ledger entries; the heading lines of Service-Desk d38d8364; and parts of Personal-Org-Operating-Model 455192c4 and de17627b. Also read: memo 5, memo 4's item 2, S-002's rules and steps 3 to 6, the extract's README, and five ruling records under `/home/user/Model-Lab/decisions/questions/`.
- **undone:** I did not open the full clones or GitHub's records; the pack and the extract were enough for the changed items. Not opened: Service-Desk b2697809 and 7d757252, Personal-Org-Operating-Model 959abcab, 0d5230c0, c4fc482f, ad6df430, 4efc6a60, e219aae3, 2cb87e77 and 5f201b8e; for these I relied on the extract's fields and the already-checked codes. `/home/user/Model-Lab/research/Q-018.md` was not re-read; I used S-002's text of the rules. The unchanged results (kinds, first checks, reopening, comments) were not re-checked. One oversized search result was saved by the harness outside the scratchpad and re-read from there; it holds only extract fields.
- **needed outside your surface:**
  - Orchestrator: record this verdict verbatim; have the memo's three slips (findings 7, 17, 18) noted or corrected by its writer.
  - Definer: add finding 15's limit, and the seen case in finding 8, to step 6's list; say which brief record gives the dispatch of a piece with several briefs (finding 16).
  - Chief of Staff: when the "not said" codes are listed for the owner, say that Personal-Org-Operating-Model #49's yes-or-no rests on one (finding 12).
- **open questions:** none for the owner beyond the listing in finding 12, which ruling 17 already requires.
