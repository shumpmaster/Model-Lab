# The Critic's check of the widened extract before the re-coding (brief 297)

*Recorded verbatim by the Orchestrator; the verdict file is reviews/Q-018-extract-widened/critic.md. Brief 297 (docs/briefs/297-critic.md), on Model-Lab@ba43327 (the Critic cites its start as f2ee515, the session-line commit before the brief), the extract as widened by briefs 294 and 296. The Critic runs on a different model from S-002's writer (D-056) and apart from the Researcher.*

Verdict: PASS

In plain words: the widened extract now reads the records the way the counting rules say. The Researcher can start re-coding the sample. Nothing blocks. The two fixes that change results are right against the records they name. One review record (Model-Lab #44) now counts as reviewing its own pull request. The other change stops two Personal-Org-Operating-Model records (#47 and #49) giving a false "failed" from a passage that quotes another check. Every case my three earlier re-checks passed keeps its result. The rows the re-run changed beyond the Definer's table are what the rules' words require, on every row I spot-checked. The sample is unchanged as far as I can read it. The research question quotes the rules word for word and keeps every gloss. The extract holds no record text, path, message or comment, and not the owner's configured address. Seven small points are listed below. None changes a sampled result. I could not run anything (no shell), so byte-identity and the old-versus-new comparison rest on the helper's report. Self-implication (D-050): both result-changing fixes correct rules my own earlier re-checks passed (finding 7).

## Findings

1. **Non-blocking: the class reading at a line's start keeps the label word.**
   - Where: research/Q-018-extract/extract.py:362-363.
   - When an `Asked:` line has no ". " before the colon, the class becomes the whole start of the line, "Asked: A phase gate", not "A phase gate". It would then be wrongly marked "names other rulings too" (:449).
   - No current Model-Lab `Asked:` line reaches this branch. Every one has ". " before its class (decisions/questions/*.md, the `Asked:` lines), and the classes in the M files come out clean ("A phase gate", "Part of a value target" and so on).
   - Fix when convenient: start from the text after `Asked:`.

2. **Non-blocking: a question file the piece only deletes is treated as "changed" by it.**
   - Where: extract.py:456-465.
   - S-002 :46 says "adds it or changes it" but does not say whether a deletion counts.
   - The extract reads a deletion as a change. Examples: ML#29's question file 197dd190 (sample.jsonl:3, `names_from` "own commit" at 00:38:22, which is commit d7f8549a, a delete) and ML#92's 086b9225 (sample.jsonl:5).
   - A deletion adds no lines, so no touch can come from it. Only the "own file" listing (Open question 11) is affected.
   - Worth one clause in S-002 at the next revision, so the Researcher codes it without judgement.

3. **Non-blocking: brief-record dispatch times still come from the simplified git history.**
   - Where: extract.py:170 (`_first_adds`, no `--full-history`).
   - Question and decision records now use the full history (:406, :331). ML#25 and ML#26 show why that matters: both add the same question file, and only the full history finds the earlier add (Model-Lab.M.jsonl:26, fc06e7c9 at 23:55:58).
   - A brief record added in two pull requests would get the same problem.
   - Only one sampled piece takes its dispatch from a brief record, ML#98 (sample.jsonl:67). Its brief is added once, so I expect no change. I could not confirm this without git.

4. **Non-blocking: the Verdict-line skip is wider than S-002's `Verdict:` line.**
   - Where: extract.py:543. `^[*_]*verdict` also skips "Verdict (P-002-route): PASS" (Service-Desk reviews/P-002-route-asks/_critic-r1-verbatim.md:1-2) and "Verdicts of the round-3 reviews…" (Personal-Org-Operating-Model reviews/31/reviewer.md:69).
   - Skipping the first is a fair reading. The second is mid-file, and that record's opening comes earlier.
   - No sampled result changes. A clause in S-002, or `verdict\b[^:]*:` in the code, would close it.

5. **Non-blocking: the own-kind split is applied only in reading (iii).**
   - Where: extract.py:610. S-002 :60 says a record's words for another kind "never give any piece's result", for every reading.
   - The code splits lines by kind only in (iii). A `Round 1` heading or a top-line verdict that belongs to another kind's check would still be read under (ii) or (iv).
   - No sampled record does this. PO#20 is the only case that needs the split, and it reads FAIL by (iii) from its own "Build review: round 1 FAIL" (sample.jsonl:60, record 48a85c6f).

6. **Non-blocking, recording only:**
   - (a) **A top-line PASS read as round 1 shows rounds 0.** This applies to SD#341 3ea324e4, SD#6 1b7a31cc, SD#316 5ef73837, SD#300 8ec028d2 and PO#22 7054833b. It is what S-002 step 3's "0 when there is none" requires; I checked that none of these five records holds "round" or "re-check". The Researcher should read rounds 0 as "names no round", not "no round held".
   - (b) **PO#47's and PO#49's build reviews now give "none found", not their true PASS.** Each is a single-round build review with a top-line PASS. Rule (iv) excludes them because they mention other checks' rounds anywhere in the text. That is S-002's stated choice, and the Definer was right to keep it: Service-Desk reviews/187/reviewer.md:1 has a top-line PASS and names "round 2" only under "## What I checked" (:8, :22, :27). Neither piece's result changes, since both are plan pieces whose plan review round 1 is FAIL (PO#47 65934264, PO#49 65934264 and 6ee73633). It belongs in step 6's list of what the rules cannot catch.
   - (c) **Commit ids.** README.md:53 and research/Q-018.md:15 cite S-002 "at abbcbe0" as brief 296's start commit, but brief 296 names 6439ec1. The quote matches S-002 as it stands at my start commit f2ee515 (finding 8), so the text is right; only the id is loose. Also, Q-018.md:9 still credits only brief 294 with the widening and re-coding, not brief 296's re-run.
   - (d) **A personal-looking email address sits in another repository's records.** It is in Service-Desk reviews/S-001-model-3.5.0-records/_build-review-round1-verbatim.md:10, in a scratch-merge command. It is outside the extract, which copies no text. I name it only so the owner of that lane can decide; I have not repeated the address.

7. **Self-implication (D-050): two rules I passed needed these fixes.**
   - In round 2, and again as "3(b): fixed" in round 3, I passed the "first heading with its first paragraph" statement rule. I did not test it on a record whose first line is a `Verdict:` line. Under it, Model-Lab reviews/44/reviewer.md would have been read at `## Findings`. The opening fix (S-002 :59) now gives #44 (reviews/44/reviewer.md:3, "verdict on pull request #44").
   - In my round-1 check of the rules (reviews/Q-018-rules/_critic-verbatim.md:123-126), I passed PO#47 as FAIL from its plan review. I never tested reading (iii) on reviews/47/reviewer.md, where "round 1: FAIL" under `## Evidence` (:38) would have given a false build FAIL.
   - Triage should count both as issues my checks missed.

8. **Item 4 (sample and quote): no finding.**
   - sample.json holds 60 random and 14 edge-case items. Their line order matches every line reference in my earlier checks (ML#92 :5, ML#47 :10, SD#6 :38, PO#11 :42, ML#98 :67).
   - README.md:30-51 copies S-002 :84-105 unchanged, and its step-3 text (:54) matches S-002 :107.
   - research/Q-018.md:17-84 quotes S-002 :18-64 and the edge-case table verbatim. The three Q-017 count parentheses are left out (E-RP1 :24, E-K1 :43, E-RT3 :53).
   - Q-018.md:88-103 carries every gloss step 4 lists.
   - I could not re-run compare_old_new.py or diff bytes.

9. **Item 5 (no text in the extract): no finding.**
   - The frame files and sample.jsonl hold only labels, classes, times, hashes, the path forms from S-002, and RT5 class words. Step 3 asks for those class words explicitly. A grep for docs/, decisions/, questions/, specs/ and session ids found only path-form templates.
   - The `.list.jsonl` files hold head branch names in clear and the opening account, as S-002 step 3 allows.
   - github_reads.json holds accounts, times and agent marks, and no comment text.
   - The owner's configured address is a run-time argument (extract.py:86) and is not written. extract.py:89 matches the owner account's public GitHub noreply alias by its suffix. That alias is not the configured address.

## The items, in brief
- **Item 1.** Every widened field matches S-002's words except findings 1 to 5. Readings that still need judgement are in findings 2 and 4.
  - Comment records: extract.py:709-722 and sample_rows.py:18-22. SD#6, SD#11 and PO#18 say "yes" from reviews/6, 11 and 18's "Returns: the reviewer comment(s) on PR #n" lines.
  - The naming rule: :387-401.
  - The quoted-line test: :341-352.
  - RT5: :354-385 and :449.
  - Milestones: :374-378.
  - C1 path forms: :485-528.
  - Statement: :536-558.
  - Readings (i) to (iv): :568-639.
- **Item 2.** Both fixes are right on ML reviews/44, PO reviews/47 and PO reviews/49, and the Definer's reason against limiting (iv) holds on SD reviews/187. My passed cases keep their results:
  - FAIL: SD#11 (iii), SD#52 (iii), SD#78 (9c0ec757 (i)), PO#18 (iii), PO#27 (table), PO#20 (iii), PO#24 (ii), PO#25 (plan (i)), PO#47 (plan), ML#73, ML#81, SD#300 (EXP-007 r1).
  - PASS: PO#50 ((iv) on 3fed3942).
  - Undecided as before: ML#93 (build only), and SD#148, whose only own-kind-less record is a build-kind FAIL (2b117140).
  - Left out: ML#78 and ML#98.
  - ML#92's trial-gates record b3609d4c is still left out by RT5 (b).
- **Item 3.** The spot-checks agree with S-002's words:
  - ML#25/#29 197dd190: the first add at 23:55:58 is ML#26's own commit fc06e7c9, so ML#25's `first_added_in_pieces_first_commit` false is literal. Its own commit is at its dispatch, outside the window either way.
  - `names_from` "own commit": ML#92, #77, #59, #42 ×2, #56, #25 and SD#233 ×2, #105, #341, #22 (sample.jsonl:5, 9, 12, 14, 15, 16, 21, 23, 28, 31). In every Model-Lab case the own commit is a deletion (finding 2).
  - PO#32's question file 25a83251 is added in the piece's first commit, so RT4 applies. PO#35 gains 14b7aecb, first added at 16:19:03 inside its window and named by spec and own file. That is a new question touch the Researcher will code. It is right under S-002 :46.
  - The records that move to neighbouring pull requests follow their openings: P-001-checks-stop's critic record names "pull request #51's branch" (:3), and P-001-build-gate-stop's names "PR #44's branch" (:3).
  - Rounds 0: finding 6(a).
- **Item 4:** finding 8.
- **Item 5:** finding 9.

## Six-part contract
- **Changed:** nothing. I hold no write tool.
- **Why:** brief 297, the Critic's check of the widened extract and the settled readings before the re-coding (S-002 step 1's check, repeated; P-002, M8).
- **Verified,** with Read, Grep and Glob only:
  - specs/S-002.md :1-149 and :240-270; README.md in full; extract.py :1-889; sample_rows.py; sample.json; frames.json (the widened keys); github_reads.json :1-20 and :130-140; research/Q-018.md in full.
  - The fields of sample.jsonl for lines 3, 5, 7, 9, 21-31, 38, 41-60 and 63-74 (c1_records, questions_decisions_named, comment_records, owner_account_comments, dispatch) and Model-Lab.M.jsonl:26.
  - Records: reviews/Q-018-extract/critic.md, reviews/Q-018-rules/_critic-verbatim.md :90-129 and _critic-r3-verbatim.md; Model-Lab reviews/44/reviewer.md, P-001-checks-stop, P-001-harness-trade-offs and P-001-build-gate-stop critic.md, and every `Asked:` line in decisions/; Service-Desk reviews/187, 341, 6, 316, 300, 52, S-001-model-3.5.0-records round 1, S-001-trial-view-2 round 1, and every "reviewer comment" line; Personal-Org-Operating-Model reviews/47, 49, 22 and 25, and its "reviewer comment" line.
- **Undone:**
  - I could not run extract.py, compare_old_new.py or git. So I did not check: sample.json's byte-identity; the "0 rows differ on any pre-widening key" claim; the SHA-1 labels (taken as the helper gives them); "only PO reviews/47 and /49 change" across all records; and ML#98's brief-record first add (finding 3).
  - I did not read S-002 :150-239.
- **Needed outside my surface:**
  - The Definer, at the next revision of S-002: findings 2, 4 and 5, one clause each.
  - The Orchestrator: findings 1, 3 and 6(c), when convenient. None needs a re-run before the re-coding.
  - Triage: the self-implication in finding 7.
  - The Service-Desk records lane owner: finding 6(d).
- **Open questions:** none new. Open questions 11 to 14 are unchanged. Finding 6(b) should go into step 6's list of what the rules cannot catch.

Key paths: /home/user/Model-Lab/research/Q-018-extract/extract.py, /home/user/Model-Lab/research/Q-018-extract/sample.jsonl, /home/user/Model-Lab/research/Q-018-extract/README.md, /home/user/Model-Lab/research/Q-018.md, /home/user/Model-Lab/specs/S-002.md, /home/user/Model-Lab/reviews/44/reviewer.md, /home/user/Personal-Org-Operating-Model/reviews/47/reviewer.md, /home/user/Personal-Org-Operating-Model/reviews/49/reviewer.md, /home/user/Service-Desk/reviews/187/reviewer.md