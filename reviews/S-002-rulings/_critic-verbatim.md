# The Critic's check of brief 314's revision to the owner's seven rulings (brief 315)

*Recorded verbatim by the Orchestrator; the verdict file is reviews/S-002-rulings/critic.md. Brief 315 (docs/briefs/315-critic.md), on Model-Lab@b700ba0 (brief 315's start line names the commit before it), S-002 as changed by brief 314 (commit 13c471e). The Critic runs on a different model from S-002's writer (D-056) and apart from the Definer.*

Verdict: FAIL

The rulings are mostly written in correctly. All seven quotes match their decision records word for word. For rulings 12, 13 and 14 the rule text is unchanged: I compared C1, RT5 and E-RT4 with the copies quoted in research/Q-018.md, and the only change is an added sentence quoting the ruling. Ruling 16 (`notes_only`, RT7) can be coded as written and gives the right result on Service-Desk #78's record. Three things fail. First, the new `later_work` code is given to the Researcher to read from the text of decision and question records. The Researcher's pack keeps `decisions/**` out (D-055, D-006), and the research question says the rules are applied "from the extract alone". Second, the ongoing count (J1, a script) has no way to apply the later-work clause at all. Third, ruling 15 as written lets a ledger copy of a piece's own starting ruling count as a touch. That changes Personal-Org-Operating-Model #50 from "no touch" to "needed the owner", and that is a gap for the owner, not a matter of wording. I could not see the Definer's table of expected changes, because it is the writer's summary and is kept out of my pack. Finding 6 gives my own reading of the records for the Orchestrator to compare against it.

## Findings

1. **Blocking (for the Definer; a pack change would also need the owner). Who codes `later_work`.** specs/S-002.md:109 ("*Later work*"): "the Researcher codes it, from the text of each such record … which the Orchestrator gives the Researcher beside the extract".
   - governance/PACKS.toml:24 (`[roles.researcher]`) has `must_not_see = [… "decisions/**" …]`. Under D-006, what a role must not see is kept out of its pack, so handing it copies is still a breach. The records involved include Model-Lab's own P-002 rulings, for example decisions/questions/P-002-trial-gates.md, which is "Part of a value target". Those hold exactly the owner's leanings and hoped-for answers that D-055 keeps from the Researcher.
   - The question files are no better. Model-Lab's questions/P-002-groundwork-shortlist.md (pack record Model-Lab--9ea16fdb, line 8) says of itself: "the Researcher is kept from seeing them".
   - research/Q-018.md:7 tells the Researcher to apply the rules "from the extract alone".
   - Options: (a) the Critic codes `later_work` in step 5, since it already holds the records pack and may read `decisions/`, and a second fresh Critic session checks that coding; (b) a per-task Researcher pack, approved by the owner, that knowingly opens these records; (c) the touch log. Whichever is chosen, "Needed outside this spec's lane" (line 264) must also name the change to Q-018's "from the extract alone" and its re-quoted lines.

2. **Blocking (for the Definer). The count cannot apply ruling 11.** RT4 (line 52) and "What a touch is" (line 46) now make a touch depend on whether the record "asks for later work". J1 (line 189) is a script, `src/E-004/count.py`, and it reads no text. Neither J1, AC2 nor the touch log (J9) has a field or a named coder for this. The spec also says "the piece's touches are given both with it and without it" for "not said", but never says which figure counts toward V1 or decides a trial look. The spec needs to name who codes it for the live count and where the code is recorded, for example a line in the touch log or a field fed into J1, and say which figure decides.

3. **Blocking before the freeze (a gap for the owner; Definer's open question 1). A ledger copy of the piece's starting ruling counts.** The skip test (line 48, "It is skipped on a piece when a decision or answer record counted on that piece … holds the same words") never fires when the only record holding those words is the starting ruling, because RT4 does not count that ruling.
   - Personal-Org-Operating-Model #50: its answer record df986385 (reviews/S-037/_owner-answer-q031.md, holding "A — approve and build (Recommended)") is the starting ruling, first added at 23:35:08 in the piece's first commit (research/Q-018-extract/sample.jsonl:50). The ledger entry 3b79e454 (LEDGER.md L-0157, `decided_by: owner (… "A — approve and build (Recommended)" on Q-031 …)`) follows at 23:35:24. So #50 goes from 0 touches to 1.
   - Personal-Org-Operating-Model #49: its starting rulings 558fd054 and 08ba8ef8 were added at 15:59:40, and the ledger entry 447cf875, quoting "Merged, I want to go with your reccomendations on all of them", follows at 16:00:06 (sample.jsonl:51). So #49 goes from 1 touch to 2.
   - The ruling's own words ("so that one answer counts once") do not settle whether the copy should count once or not at all.
   - Options for the owner: (a) count the copy, as the rules now read; (b) also skip an entry when the piece's starting ruling (RT4) holds the same words, since the entry is that ruling.
   - Until the owner rules, the re-coding should report #49 and #50 both ways.

4. **Non-blocking (for the Definer; open question 5). A ledger entry and its question file can count as two questions.** Line 48 calls an entry "a decision record of its own, with no question file: one question". The ruling does not say "with no question file". Personal-Org-Operating-Model's entries name their question in their `asked:` line ("Asked as Q-031", LEDGER.md:2261). So when a question file counts on a piece and its answer record does not, the entry counts again. That breaks RT1(a)'s "counted once per question" (Q-018/U4). I found no sampled case: #49's Q-031 entry falls after its merge, and #35's entry is skipped. The fix is to pair the entry with the question file whose `Q-<nnn>` its `asked:` line gives, carried in clear as the answer records already are, or else to list the case in step 6.

5. **No issue, with one note (open questions 4 and 6).**
   - (4) A ledger entry can never be marked by RT5, because its file name is docs/LEDGER.md. That is consistent: no Personal-Org-Operating-Model record carries a class, or a gate word in its name, at the cut-off (RT5(d)). It belongs in step 6 (l).
   - (6) "Already counted": reading it as "counted on the piece, in either order" is the only reading that keeps "one answer counts once" without changing the answer-record rules. Note that when the entry comes first, the touch is timed by the later answer record, which can matter at a trial look's cut-off.

6. **Non-blocking. Expected sampled changes, my reading of the records; Orchestrator to compare with the Definer's table.**
   - Personal-Org-Operating-Model #20 (dispatch 16:55:59 on 10-05): its four entries are L-0121 ("Approve", the S-017 freeze that started it, 17:07:42), L-0122 and L-0123 (freezes of S-018 and S-019, which name S-017 only in passing, so likely coded "later work"), and L-0124 (names PR 20). Likely result: from 0 to 2.
   - #22 (dispatch 17:14:27): L-0128, "Yes, fix it now (Recommended)", the S-021 freeze, at 17:20:58. From 0 to 1.
   - #50 from 0 to 1 and #49 from 1 to 2 (finding 3).
   - #35's 5be98217 is skipped: reviews/S-033/_owner-answers.md:9 holds "A. Approve and build (Recommended)" character for character.
   - I did not check #25, #27 or #30.
   - Service-Desk #230: its four own question files ask for changes "built in a small change after G7b lands" (pack record Service-Desk--b793d0d9:10), so likely from 4 to 0.
   - Model-Lab #73: 9ea16fdb is an owner shortlist about future research, so likely from 1 to 0. Model-Lab #81 is similar but I did not check it.
   - Service-Desk #78: notes 3 to 9, 10 to 14, 19 to 21 and 22 to 24 sit under headings that name only notes. Notes 15 to 18 ("which also answers") and 25 to 27 ("the orchestrator's answer") stay under RT1(a). The codes move to RT7's code, but whether #78 needed the owner does not change.
   - #20 and #22 count only because the freeze approval was written down minutes after the first commit.

7. **Non-blocking. Step 6 (line 112) is not complete.** Items (b), (l) and (o) are correctly marked as settled. Missing:
   - Ledger cases under (c): an approval given before the work began but written down after its first commit (#20 L-0121, #22 L-0128).
   - The character-for-character test, which misses a reworded copy and counts it twice.
   - `later_work` being a judgement with no E-code and no row in the edge-case table.
   - The RT5 point from finding 5.

8. **Non-blocking. Step 5's check of `later_work` (line 114) only covers part of it.** The Critic opens only records coded "later work" or "not said", plus the own-file ones. A record that names the piece by number or spec and is wrongly coded "this piece" is never checked. Check every code (there are few), or a stated sample.

9. **Non-blocking; self-implication (D-050). The order of the ten E-RT4 pieces has never been recomputed.** Step 5 (line 111) cites reviews/Q-018-recode-4/_critic-verbatim.md, finding 6, for the order of the ten pieces. That earlier Critic check says at lines 27 and 83: "I cannot compute SHA-256 … I did not recompute the SHA-256 order". The cited record does not establish the order, and this rests on my own role's earlier check. The Orchestrator should recompute it with `python3 -I` and hashlib and record the result.

10. **Non-blocking. A quote I could not check.** Line 46 quotes "the ruled card's words: 'where the record does not say, it is listed for you rather than guessed'". No record on this branch holds them. The decision record does not, and the card questions/P-002-later-work-questions.md exists only in git history (PR #105). The spec should cite the card by commit, or the Orchestrator should confirm the words.

11. **Non-blocking. Rulings 11 and 16 together.** `later_work` is coded for "each question RT1(a) would count" (line 109). It is not said whether a note diverted to RT7's code that asks for later work (for example, Service-Desk #78's notes 28 to 31, "to be mocked up before anything is built") still counts on the piece.

12. **Non-blocking. The "What the owner's rulings … need" paragraph (line 114).** It is right for rulings 10 and 12 to 14. It leaves out three things: Q-018 must be re-quoted with the revised lines (step 4), the extract README must list the new fields, and the coder or pack question from finding 1.

## Six-part contract
- **Changed:** nothing; I am read only.
- **Why:** brief 315, the Critic's check of brief 314's change (13c471e) to specs/S-002.md.
- **Verified:** Read and Grep only, with no shell. I checked the seven decision records against specs/S-002.md:46, 48, 52, 53, 55, 56, 59, 109, 111, 112, 114 and 246 to 261. I checked the old text against research/Q-018.md:45, 52, 55 and 58, and the Researcher's pack in governance/PACKS.toml:17-26. I checked sample.jsonl lines 50, 51, 59 and 60 (dispatch times, ledger labels and times), research/Q-018-memo-4.md, and the clones' LEDGER.md (L-0121 to L-0128, L-0155 to L-0157), reviews/S-037/_owner-answer-q031.md, reviews/S-033/_owner-answers.md and Service-Desk decisions/questions/P-001-trial-view-notes-2.md. In the records pack I read Model-Lab--9ea16fdb and Service-Desk--b793d0d9. I could not run git (no diff of 13c471e) or SHA-256.
- **Undone:** the SHA-256 order; #25, #27 and #30's ledger entries; Model-Lab #81; comparison with the Definer's table, which I cannot see.
- **Needed outside its surface:** the Orchestrator recomputes the E-RT4 order and confirms the card's quoted words from PR #105; the owner rules on the pack (if finding 1 option (b) is chosen) and on finding 3.
- **Open questions:** finding 1 (who codes `later_work`); finding 3 (should a ledger copy of a starting ruling count once, or not at all?).

Files: /home/user/Model-Lab/specs/S-002.md, /home/user/Model-Lab/governance/PACKS.toml, /home/user/Model-Lab/research/Q-018.md, /home/user/Model-Lab/research/Q-018-extract/sample.jsonl, /home/user/Model-Lab/reviews/Q-018-recode-4/_critic-verbatim.md, /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/hc/Personal-Org-Operating-Model/docs/LEDGER.md
