# The Critic's re-check of brief 321 (brief 322)

*Recorded verbatim by the Orchestrator; the verdict file is reviews/S-002-rulings-4/critic.md. Brief 322 (docs/briefs/322-critic.md), on Model-Lab@ce156fd, S-002 and E-004 as changed by brief 321 (1f17c6a). The Critic runs on a different model from S-002's writer (D-056), apart from brief 321's Definer and from the Critics of briefs 315, 317 and 320.*

Verdict: FAIL

Brief 321 closes all four of brief 320's findings it was given. The plans now say plainly that the Chief of Staff keeps the touch log and knows the sides. The three lines that claimed too much now claim only what holds. "Not tilted" is gone, and the re-count will report how much the later-work codes remove. A different ruling with the same short words is now listed as an under-count. The owner's choice is quoted word for word from the card. Nothing in the text blocks the re-count. Two gaps in how the new check is built block the freeze, though not the re-count. First, the list the owner is shown leaves out touches given late in a look, in the weeks while its last pieces are still being worked on. Those are exactly the touches a keeper who knows the sides could put against the wrong piece. Second, the owner's confirmation leaves no record and fixes no set of lines. A line the Chief of Staff adds after the owner has confirmed still counts, unseen by the owner. And nothing checks that the Chief of Staff wrote down the owner's changes as the owner gave them. Smaller points: letting the owner take lines out goes a little beyond "confirm or add to", and the plan does not mark it as its own reading. How a corrected line is treated in the "without late lines" result is unclear. And the owner's cost list leaves out the short list the card names as its cost. On the time-limit question, I find no limit is needed for fairness, and only the owner could set one.

## Findings

1. **Closed: brief 320 finding 1 (the disclosure and the three lines).** The disclosure is in:
   - S-002: the plain words (:10), J3 (:191), J4 (:192), J9 (:197) and Risks (:233, :236).
   - E-004: "Who does what" (:15), Step 1 item 6 (:39), Step 5 (:83), Step 8 (:103) and "What this trial cannot catch" (:152).

   The three lines are corrected:
   - The plain words (:10) now say "no code of whether a question asks for later work decides which of them count".
   - Risks (:236) now says "no 'later work' code reaches a trial's deciding measure", then that the keeper still decides what is logged.
   - Risks (:233) now adds that agents may ask less on one side and that the log's keeper knows the sides.

   The remaining limit (a touch the owner too does not recall, or one put against the wrong piece that the owner does not notice) is in J3, J4, J9, Risks :233, and E-004 Steps 1 and 8 and :152. Where the confirmation happens is stated (E-004 Step 5, :83), and so is what the desk shows and what happens to an added or corrected line. But see findings 6 to 9.

2. **Closed: brief 320 finding 3 (J1 `trial`, S-002:189).** The match is named: the entry line's repository against the pull request's, and its brief against a brief number in the `Agent-Session:` trailers. Every entry line that no J1 line carries is listed.
   - Non-blocking residue: nothing says what the Reviewer then does with a listed entry's piece. Its J1 line still has `trial: null` and its codes read, and J2's join (:190) takes the J1 line as it stands. One clause would close it: such a piece's RT1a, RT1c and RT7 touches are taken as "not said" at judging.

3. **Closed: brief 320 finding 5.**
   - Risks (:236) and E-004:154 now say "counted by one rule with no judgement, the card's 'both sides are counted the same way'". They also say this "does not make the comparison … even", because a method moves its own side's count.
   - No "tilted" is left in either file.
   - The re-count's order (:114) now reports "how many touches the sample's 'later work' codes remove … in all and by repository, and how many sampled pieces they change from needing the owner to not".

4. **Closed: brief 320 finding 7.** Step 6 (r) (:112) now lists the under-count: a later, different ruling whose short passages ("A", "Approve", "Approved") stand character for character in a counted record or the starting ruling is skipped.

5. **The owner's ruling, quoted.**
   - The owner's words "B: you confirm (Recommended)" match decisions/questions/P-002-touch-log-check.md:9 and the handoff (docs/handoff/2026-11-13-chief-of-staff-p002-17.md:23).
   - Option B as quoted at S-002:197 and E-004:83 matches the card's line 12 character for character: "Before each trial look is judged, you confirm or add to that look's conversation lines through the desk."
   - I read the card in the scratchpad clone (hc/Model-Lab/questions/P-002-touch-log-check.md). Without git I cannot confirm that copy is the one at commit 55e645e.

6. **Blocking for the freeze (not the re-count), for the Definer: the desk's list misses touches put against other work after the look's weeks end.**
   - S-002:197 and E-004:83 show the owner lines against other work or work not yet dispatched only when the line's time "falls in the look's weeks".
   - A look's weeks end at the entry of place 60, or of its last reserve place (E-004:67).
   - The pieces entered last keep running after that, up to their merge or the 60 days. A touch on such a piece in those weeks, logged against later or other work, is never shown. That is the very "put against the wrong piece" case option B was chosen to catch (card line 5).
   - Fix: show every such line whose time falls between the look's first entry and its last merge or settle date, that is, inside any of the look's pieces' windows.
   - This is the Definer's addition, not the card's. The card names no time span.

7. **Blocking for the freeze, for the Definer (part may need the Service Desk): the confirmation has no record and no cut-off, and the Chief of Staff's transcription is unchecked.**
   - J9 (:197) defines only `"event": "touch"` lines. Nothing records that the owner confirmed, when, or which lines were shown. So the Reviewer cannot check AC5's and AC9's "the look is not judged until the owner has confirmed" (:170, :174).
   - AC9 counts "only touch-log lines committed before it judges" (:174; E-004:133). A line the Chief of Staff commits after the owner confirms, but before the Reviewer judges, counts in the deciding result without the owner having seen it. It is listed only as late, and only if its piece merged. That reopens the path B closes.
   - At look 2 (judged on all 120 pieces, E-004:80), Step 5 shows "the look's pieces". It does not say whether look 1's pieces' lines committed since look 1's confirmation are shown again.
   - On brief item 3(b): yes, it is a further limit. The Chief of Staff, who knows the sides, writes down the owner's changes (S-002:197, E-004:83), and nothing compares them with what the owner gave.
   - Fix: record the confirmation, either as a log line or the desk's own record of the lines shown and the owner's changes. Have the Reviewer count only lines committed up to that confirmation, and list any line after it. Have the Reviewer compare the log's `where: "desk"` lines and removals with the desk's record. If the desk will keep no record, state the transcription limit in J3, J4, Risks and E-004 Steps 1 and 8 and :152.
   - Self-implication (D-050): option (b) was first framed in my role's brief 320 finding 1(b), with no confirmation record or cut-off named.

8. **Non-blocking: "takes out" goes beyond the card's "confirm or add to", and is not marked.**
   - AC5 (:170), J9 (:197), E-004:83 and E-004:114 let the owner take a line out. Reading "confirm" as including "not confirm" is fair. But E-004:12 requires such details to be marked "this plan's reading" or "this plan's design", and Step 5's paragraph marks none of its details: the desk's display, how a correction is logged, or a removal.
   - The miss this adds (a true touch wrongly taken out, or corrected onto the wrong piece or out of its window) is not in any limit list.
   - The plain words (:10) tell the owner only "what you add or correct counts". They do not say a line taken out stops counting.

9. **Non-blocking: a correction in the "without late lines" result.**
   - A correction is a new `where: "desk"` line, with the old line taken out in the same commit (S-002:197, E-004:83). The new line is late for a merged piece (E-004:133).
   - So in the "without late lines" result the touch vanishes entirely, rather than standing as first logged.
   - Say which the reported second result uses. For example, the line as it stood before the confirmation, from git history.

10. **Non-blocking: AC5 (:170) and AC9 (:174) say "last piece has merged".** J9 (:197) and E-004:83 say "merged or been settled". AC5's and AC9's wording leaves out a look whose last piece is settled unmerged at 60 days.

11. **Non-blocking: the owner's cost, and brief item 3(a), the time limit.**
    - The card names the cost of B as "a short list for you to read before each look" (card line 14). E-004 Step 1 item 7 (:40), "What it costs the owner", and the Sample's cost quote (:117) leave it out.
    - On the time limit: the card sets none and its DEFAULT and TIMEOUT are "none". The owner is never shown a side (:197), so a wait cannot steer the result. A limit that ended in a default would be a new rule only the owner could set. So I would not add one.
    - The wait does lengthen a trial beyond Step 2's expected weeks (E-004:50–51) and AC14's 26-week mark. The entry card should say so. Step 5 already says the desk shows the look waiting.
    - Finding 7's cut-off removes the one risk the wait adds: late lines building up while the look waits.

12. **Additions judged sound.**
    - AC9's "once the owner has confirmed" follows directly from "before each trial look is judged".
    - "Never a piece's side" keeps the owner as blind as the short reads are (T29).
    - The desk showing each line's piece, type and time (no owner's words, which the log does not hold) is sound.
    - "A line added or corrected … is a late line for a merged piece" (E-004:133) follows from the existing rule.
    - Open question 20 (:266) quotes the owner's words, and each place it lists does hold the change: U1's fallback :82; "Needed outside" :270 and :272; E-004 :15, :21, :39, :83, :101, :103, :114, :133 and :152.

13. **What blocks (brief item 4).**
    - The re-count: nothing in this text. It still needs brief 320 finding 4 done first: the records pack widened to hold the ledger entries. I found "ledger" only in research/Q-018-extract/extract.py, not in pack.py or pack2.py.
    - The freeze: findings 6 and 7, then the plan review re-run on the changed lines and the cards the handoff still lists (:29).

## Six-part contract
- **Changed:** nothing. I am read only.
- **Why:** brief 322, a re-check of brief 321 before the re-count and the freeze.
- **Verified:** Read, Grep and Glob only, with no shell and no git.
  - AGENTS.md, the critic charter and briefs 321 and 322.
  - specs/S-002.md: lines 1–103, 165–199 and 232–281, plus greps of :112 and :114.
  - experiments/E-004.md: in full.
  - decisions/questions/P-002-touch-log-check.md.
  - reviews/S-002-rulings-3/_critic-verbatim.md.
  - docs/handoff/2026-11-13-chief-of-staff-p002-17.md.
  - The card, from the scratchpad clone.
  - Greps for "tilted" (none left) and for "ledger" in research/Q-018-extract/*.py.
- **Undone:**
  - Commit 1f17c6a's diff, and the card as it stood at 55e645e (no git).
  - S-002 lines 104–164 and 200–231, outside the step 6 (r) and re-count lines.
  - A grep result list showed one file name in the scratchpad that looks like the writer's working script (edit321.py). I did not open it (D-006).
- **Needed outside its surface:**
  - The Definer: findings 6 to 10, and the residue in finding 2.
  - The Service Desk: the desk's own record of each confirmation (finding 7), filed as new work for the owner to approve.
  - The Orchestrator: the pack widening (brief 320 finding 4).
  - Triage: my D-050 flag on finding 7.
- **Open questions:**
  - Should the desk keep its own record of each confirmation, or should the transcription stay a stated limit? Either way is within B; a record is stronger.
  - Should the "without late lines" result treat a correction as the line as first logged?

Files:
- /home/user/Model-Lab/specs/S-002.md
- /home/user/Model-Lab/experiments/E-004.md
- /home/user/Model-Lab/decisions/questions/P-002-touch-log-check.md
- /home/user/Model-Lab/reviews/S-002-rulings-3/_critic-verbatim.md
- /home/user/Model-Lab/docs/briefs/321-definer.md
- /home/user/Model-Lab/docs/briefs/322-critic.md
- /home/user/Model-Lab/docs/handoff/2026-11-13-chief-of-staff-p002-17.md
- /tmp/claude-0/-home-user/ae0ca834-f091-5216-bef6-407ce00e0f8f/scratchpad/hc/Model-Lab/questions/P-002-touch-log-check.md
