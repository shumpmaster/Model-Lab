# The Critic's re-check of brief 325 (brief 326)

*Recorded verbatim by the Orchestrator; the verdict file is reviews/S-002-rulings-6/critic.md. Brief 326 (docs/briefs/326-critic.md), on Model-Lab@f85a51c, S-002 and E-004 as changed by brief 325 (4834f68). The Critic runs on a different model from S-002's writer (D-056), apart from briefs 321's, 323's and 325's Definers and from the Critics of briefs 315, 317, 320, 322 and 324.*

Verdict: PASS

Brief 325 fixes all four findings it was given from brief 324. The count now goes by what the owner was actually shown. Once the desk keeps its own record of a confirmation, a look counts only the lines that record says it showed, with the owner's changes as the record gives them. Anything else in the log that differs is listed by side and does not decide the result. A line the Chief of Staff writes after the list is shown no longer counts unseen, even if the owner has not confirmed yet. A line quietly taken out that the record does not hold still counts, and is listed. Where the log and the record disagree, the record wins. This rule reads the same in the five places that state it. The "without late lines" result is now the log as it stood when each piece merged. The acceptance criterion that needs the desk's record (AC5) now applies only once the desk keeps it. The plain words now keep the owner's choice ("confirm or add to") apart from this plan's own design. The Definer's three answers are sound. The text still says the owner's option B and nothing more, and every addition is marked as this plan's. Nothing in this text blocks the freeze. Four small wording gaps remain, and are worth fixing at the same time. The re-count is still waiting on an older task that is not in this text: widening the records pack to hold the ledger entries.

## Findings

1. **Closed: brief 324 finding 5 (the one counting rule).**
   - The rule reads the same at E-004:83 (Step 5), E-004:133 (Exclusions), S-002:174 (AC9) and S-002:197 (J9): count "the lines the desk's record says it showed that are put against the look's pieces, with each change the record holds applied as the record gives it". Every other difference ("a line not shown, a removal or change the record does not hold, a change logged differently") is listed by side outside the deciding result, with the logged version beside it.
   - U1's fallback (S-002:82) gives the counting clause in the same words. It points to E-004 for the listing clause rather than repeating it, which is acceptable.
   - Part (a) is closed: E-004:83 says "a line committed after the desk showed the list does not count in that look, even if it was committed before the owner confirmed", and J9's awkward case says the same (S-002:197).
   - Part (b) is closed: "a line taken out that the record does not hold still counts, and is listed" (E-004:83; S-002:197 awkward case).
   - Part (c) is closed: "a change the log gives differently from the record counts as the record gives it" (E-004:83; S-002:197 awkward case). The old wordings ("committed up to", "confirmation's time", "as the Chief of Staff logged them", "logs a change") no longer appear in either file (Grep).

2. **Closed: finding 7 (the "without late lines" result).** It is now the log as it stood at each piece's merge, from git history: additions out, a corrected line as first logged, a removed line back in if it was committed before its piece merged. This is at E-004:133, and the same in S-002:174 (AC9), :192 (J4), :197 (J9), E-004:102 (Step 8) and :114 (Measure).

3. **Closed: finding 8.** AC5 (S-002:170) now reads "once the desk keeps its record of each confirmation (Needed outside this spec's lane), that record holds …".

4. **Closed: finding 9.** The plain words (S-002:10) put "(you chose this on 2026-11-13, Open question 20)" right after "confirm or add to that look's conversation lines through the desk". Then comes "the rest of this check is this plan's design, not your choice", followed by the display, taking a line out and the desk's record. "or correct onto the wrong piece" is now in the plain-words list of misses.

5. **Non-blocking: the fallback reads a little differently in AC9 and U1.**
   - J9 (S-002:197), Step 5 (E-004:83) and Exclusions (E-004:133) say the lines committed before judging count "as the log then stands", and Step 5 adds "a line taken out by then not counting".
   - AC9 (S-002:174) says only "counting the touch-log lines committed before it judges", and U1 (S-002:82) says "a line counts … only when that commit is before the look is judged". Neither says a line taken out before judging stops counting.
   - AC9 is what the locked test is written from, so a test author could count a removed line.
   - Fix: add "as the log then stands" to AC9 and U1.

6. **Non-blocking: when the owner changes a line again at look 2, the text does not say which record wins.**
   - The owner's own changes at look 1 on look 1's pieces are committed after look 1's list was shown, so look 2 shows them again (E-004:83; S-002:197). If the owner then changes or removes one at look 2, look 1's record and look 2's record both speak to it.
   - The text says look 1's lines count "as look 1's record gives them" and the lines shown at look 2 "as look 2's record gives them". The natural reading is that the later record wins, but the text does not say so.
   - Fix: "where both records give a line, look 2's governs".
   - A related small point: at look 2, "the look's pieces" means its 60 new pieces for the display (E-004:83). It should be said that a correction "onto" or "off" the look's pieces, at look 2, means all 120.

7. **Non-blocking: the plain words (S-002:10) leave out two stated limits that every other limit list carries.**
   - (a) "or at a time outside its piece's window", for an unnoticed wrong line and for a correction. Every other list has it: J3, J4, J9, Risks, E-004 Step 1 item 6, Step 5, Step 8 and "What this trial cannot catch".
   - (b) Until the desk keeps its record, "nothing fixes which lines the owner was shown or when the owner confirmed". In that period a line committed after the confirmation but before judging can count unseen. The plain words give only the transcription half of this limit.
   - The entry and results cards carry both limits, so this does not block. But the plain words are what the owner reads to approve the plan.

8. **Non-blocking: the "without" result for a piece that never merges is not defined.** "The log as it stood at each piece's merge" (E-004:133) does not say what happens for a piece settled unmerged. The Exclusions bullet "A piece that never merges" (E-004:129) reads "its merge" as its settle date for counting touches. Saying the same here would close it.

9. **The Definer's open questions (brief item 2): all three are sound.**
   - **Look 2 shows again the lines committed after look 1's list was shown, not after its confirmation.** This is right, and it follows from finding 1. A line committed between the showing and the confirmation is not counted at look 1. If look 2 only showed lines committed after the confirmation, that line would never be shown and could never count. Keying on the confirmation only in the fallback is also consistent, because there look 1 counts every line committed before judging.
   - **A correction onto or off the look's pieces counts as corrected.** This follows directly from "put against the look's pieces, with each change the record holds applied". Onto counts there; off stops counting (E-004:83). The edge case at look 2 is in finding 6.
   - **A quiet removal on look 1's pieces after look 1's confirmation still counts as look 1's record gives it, though look 2 does not show it.** This is sound. The owner confirmed that line, and the removal never reached them, so the record decides and the removal is listed by side. One case was checked: a quiet move after look 1 from one look-1 piece to another. The new line is shown at look 2 and counts only if the owner confirms it, so no line counts that the owner did not see or confirm.

10. **Brief item 3: still option B and nothing more.**
    - The owner's words "B: you confirm (Recommended)" match decisions/questions/P-002-touch-log-check.md:9.
    - Option B as quoted at E-004:83 and S-002:197 matches the card's line 12 word for word. The cost "a short list for you to read before each look" at E-004:40 and :117 matches its line 14. I read the card from the scratchpad clone, not at commit 55e645e, because I have no git.
    - Every addition is marked: "the details below are this plan's design, except the one marked as this plan's reading" (E-004:83); "in this plan's design" and "taking out being this plan's reading" (S-002:197); "(Step 5; this plan's design)" and "(this plan's design)" (E-004:133); and the plain words' "the rest of this check is this plan's design, not your choice" (S-002:10).
    - Requiring the desk's record before a look is not made a gate, as brief 325 asked. The look waits only for the owner's confirmation (E-004:36, :83).

11. **Brief item 4: what blocks.**
    - **The freeze:** nothing in this text. Findings 5 to 8 are cheap to fix first. After that, the plan review should be run again on the changed lines.
    - **The re-count:** still the item outside this text from brief 320 finding 4 and brief 324 finding 11. Widening the records pack to hold the ledger entries still looks undone. "ledger" appears only in research/Q-018-extract/extract.py (lines 424, 452, 463), not in research/Q-018-extract/pack.py, research/Q-018-extract/pack2.py or governance/PACKS.toml.

12. **Self-implication (D-050).** The rule checked in finding 1 and the "without" result in finding 2 are my role's own fix wording (brief 324, findings 5 and 7). Brief 325 items 1 and 2 carried them over almost word for word. So passing them is partly the Critic judging its own earlier fix. Triage should weigh findings 1, 2 and 9 with this flag.

## Six-part contract
- **Changed:** nothing. I am read only.
- **Why:** brief 326, a re-check of brief 325 before the re-count and the freeze.
- **Verified:** Read, Grep and Glob only, with no shell and no git.
  - Read: AGENTS.md, the critic charter, briefs 325 and 326, reviews/S-002-rulings-5/_critic-verbatim.md, decisions/questions/P-002-touch-log-check.md, and the card from the scratchpad clone.
  - Read: S-002 lines 1–20, 80–83 and 165–281; E-004 lines 13–42 and 80–154.
  - Grep: the old cut-off wordings in both files (no matches); "ledger" in governance/PACKS.toml and research/**/*.py.
- **Undone:**
  - Commit 4834f68's diff, and the card as it stood at 55e645e (no git).
  - S-002 lines 21–79 and 84–164, and E-004 lines 1–12, 43–79 and 155 onward, which are outside the passages the brief names.
  - I did not run check_all.sh or surface_guard.py (no shell).
- **Needed outside its surface:**
  - The Definer: findings 5 to 8, which do not block.
  - Triage: the D-050 flag in finding 12.
  - The Orchestrator: the pack widening named in finding 11, before the re-count, and running the plan review again before the freeze.
  - The Service Desk: the confirmation record, unchanged from S-002:272.
- **Open questions:**
  - Should look 2's record govern where both looks' records give the same line (finding 6)? My answer is yes.
  - Should the plain words state the fallback's unseen-line limit (finding 7b)?

Files:
- /home/user/Model-Lab/specs/S-002.md
- /home/user/Model-Lab/experiments/E-004.md
- /home/user/Model-Lab/docs/briefs/325-definer.md
- /home/user/Model-Lab/docs/briefs/326-critic.md
- /home/user/Model-Lab/reviews/S-002-rulings-5/_critic-verbatim.md
- /home/user/Model-Lab/decisions/questions/P-002-touch-log-check.md
- /tmp/claude-0/-home-user/ae0ca834-f091-5216-bef6-407ce00e0f8f/scratchpad/hc/Model-Lab/questions/P-002-touch-log-check.md
- /home/user/Model-Lab/research/Q-018-extract/pack.py
- /home/user/Model-Lab/research/Q-018-extract/pack2.py
- /home/user/Model-Lab/governance/PACKS.toml
