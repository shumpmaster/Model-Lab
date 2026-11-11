Verdict: PASS

*The Critic's check of P-002's brief brought into line with the Design gate ruling (docs/projects/P-002.md at commit 59d5775), brief 257, part A; a session on a different model from the writer. Recorded verbatim by the orchestrator, 2026-11-11. Round 1 FAIL (brief 257), round 2 PASS (brief 259); its non-blocking findings are left for the plan's next change. Part B, the M7 line, is reviews/P-002-m7-line/critic.md.*

## Round 1 (commit 59d5775)

## A. The brief brought into line with the Design gate ruling

Verdict: FAIL (two blocking findings, both quick to fix)

Most changed text matches the ruling. Checked against Parts 2 to 10 of /home/user/ml-fixed-257/decisions/questions/P-002-design-gate.md and the question as filed in /home/user/ml-cards/P-002-design-gate.md:

- **Section 5:** both ceiling bullets match Parts 2, 3a and 3b. "Existing AI plan only (Recommended)", "No cap" and "Keep all three" are quoted exactly. P15 to P17 are restated faithfully. "No cap, so the two-week limit and the queue of 3 are the only limits" matches "How it is carried out".
- **Section 6, last bullet:** the twelve confirmed terms (T16, T23 to T30, T32 to T34) are counted correctly. P1 to P11 are restated faithfully. P12 to P14 and P19 to P20 match Parts 6 and 8. P18 is kept open, with the right words ("Decide later on checked figures (Recommended)", someone other than the writer, a card of its own before the design freezes).
- **Section 6, other changed text:** the "How a method is tried" parenthesis and the "Cost to the owner's time" bullet match (5 per look, 10 with a second look, P20).
- **Section 3, Dependencies:** matches (P20, P4, P12, P19).
- **Section 7, U3:** the last sentence matches Part 9.
- **Section 8:** the constraints on the prompt engine, the owner's order and the owner's time match Parts 3 and 8.
- **Section 4, M7 row:** matches Part 10 and Reviewer rounds 1 to 3 (FAIL, FAIL, PASS).

Findings:

1. **Blocking. A ruled term is still called proposed.** Section 4, the "short reads" row (line 154): "Five per look, as proposed for the Design gate (section 6, last bullet)". P14 was ruled in Part 6 ("5 per look"). Change it to ruled, citing Part 6.
2. **Blocking. A trial term is called ruled that was not.** Section 6 italic header (line 180): "the rest of the trial terms at the Design gate, 2026-11-11 (…; last bullet)". P18 is a trial term and stays open (Part 7). The header says more than the ruling. Say "except P18, the line at two looks, left open".
3. **Non-blocking. U2's fallback is a loose paraphrase** (line 222). It says the P5 stop "sends the target back to the owner". P5 and the card's wording are "the work stops and comes back to the owner". Use the ruled words.
4. **Non-blocking. A stale statement of what the gate will decide.** Pre-mortem R15 (line 211): "The owner decides at the Design gate whether any part may start… until then the owner's order stands". This was decided in Part 8, A. Section 8 already says so. Mark it ruled or add a pointer.
5. **Non-blocking. A ruled check is still called proposed.** R7 (line 203): "proposed here: outside code, prompts and skills are checked before use". T10 is ruled. This is one of the six faults the owner left standing in Part 1, so it is not a new error. I name it as asked.
6. **Non-blocking. Other leftover text.**
   - Line 193: "the value target still to be set". The target is ruled.
   - Lines 209 and 214 (R13, R18): "owner-time ceiling… each round reports both" and "the owner's hours are counted with the spend". These sit beside line 187, "The owner's hours are not recorded", and the ruled "no cap". They are tension rather than error.
   - Lines 85 and 96: "for the owner to approve at the Design gate". These are draft notes, now past.
   - Line 238: "while this project is in Discovery".
7. **Non-blocking. A citation could be sharper.** Section 4 line 159, the ceilings row, still says "Set at the Design gate (…answer 8)". Add a pointer to Parts 2 and 3.

## Six-part contract (the whole return, both parts)

- **Changed:** nothing. Read-only. No files were written.
- **Why:** to check the brief against the ruling for A, and the M7 line against section 3's form for B.
- **Verified:**
  - Every changed passage against the ruling and the question as filed, and against /home/user/ml-fixed-257/docs/gates/P-002/trial-terms.md.
  - The M7 line against brief line 117.
  - The Reviewer's rounds, to the extent reviewer.md records them.
- **Undone:**
  - I read no earlier version of the brief, so I judged the changed passages from your list.
  - I ran no git, so the merge commit and the Owner-Ruling trailer are unchecked.
  - I did not read /home/user/ml-cards/P-002-value-target.md or P-002-trial-gates.md, or their rulings. I relied on trial-terms.md for the terms they set.
  - I did not read docs/briefs, docs/reports, docs/handoff, sessions or any -notes.md file. One grep result surfaced a handoff line. I did not use it.
- **Needed outside your surface:**
  - Fix findings 1 and 2, then have the Critic re-check A. Findings 3 to 7 are for the Chief of Staff to fix or ignore.
  - The Orchestrator confirms #93 against git.
  - The M7 commit's `Owner-Ruling:` trailer must name decisions/questions/P-002-design-gate.md.
- **Open questions:** none for the owner. P18 stays for its own card.

## Round 2 (commit dea20ae)

Verdict: PASS

Round 2 of the check of /home/user/ml-fixed-259/docs/projects/P-002.md at dea20ae. Both blocking findings from round 1 are answered. Nothing ruled is still called proposed, except R7, which the owner left standing in Part 1. Nothing is called ruled that was not.

**Round 1 findings, one by one**
- 1 (blocking, short-reads row): Answered. Line 154 now reads "Five per look, as the owner ruled ("5 per look", decisions/questions/P-002-design-gate.md, Part 6; ...)". That matches Part 6.
- 2 (blocking, section 6 italic header): Answered. Line 180 now reads "...except the line at two looks (P18), which the owner left open for a card of its own during Design". That matches Part 7 and "How it is carried out". Every other trial term is covered by a ruled part: Part 3b (P15 to P17), Part 4 (the twelve), Part 5 (P1 to P11), Part 6 (P14), Part 8 (P12, P13, P19, P20).
- 3 (U2 fallback): Answered. Line 222 now uses the ruled words: "the work stops and comes back to the owner", citing P5. This matches the record: "U2's fallback rests on P5, which is ruled".
- 4 (R15 stale): Mostly answered. A pointer was added: "Ruled at the gate: trials may start with guards beside the prompt engine (... P12 and P13)". This matches Part 8, A. The earlier clause "The owner decides at the Design gate ... until then the owner's order stands" is still there in the present tense. The pointer makes it readable, so I count it answered. See finding 3 below.
- 5 (R7 "proposed here"): The writer's reason holds. Part 1 lists "it calls one check you ruled 'proposed'" among the six faults, and the owner chose A, so they stand. The word is still wrong on the facts, because T10 is ruled. It is the owner's standing exception. Not blocking.
- 6 (leftover text): The reasons hold in part.
  - Line 193 is fixed. It now says "'The measure' is the value target (section 6)".
  - R13 (line 209): The reason holds. It is the pre-mortem's response as passed. The owner-time ceiling was set at the gate, as "no cap". P17 gives the per-update report.
  - R18 (line 214): The reason holds only in part. "The owner's hours are counted with the spend" still sits against line 187, "The owner's hours are not recorded". See finding 2.
  - Lines 85 and 96: The reason holds. They are dated drafting notes on a plan the owner approved in Part 1, A.
  - Line 238: The reason holds. "While this project is in Discovery" is a true statement of a ruling that held during Discovery. It does not claim to be current.
- 7 (ceilings row): Answered. Line 159 now says "the existing AI plan only, and no cap on the owner's time (... Parts 2 and 3; section 5)". That matches Parts 2, 3a and 3b.

**New and remaining findings (all non-blocking)**
1. R7, line 203: "proposed here: outside code, prompts and skills are checked before use". This is the one ruled term still called proposed. It is covered by the owner's Part 1 choice. Fix it at the next change to the plan.
2. R18, line 214: "the owner's hours are counted with the spend (R13)". The brief says elsewhere that the hours are not recorded and there is no cap. Likewise "A cap on open proposals" is, in the ruling, the queue of 3 (P15). This is the same tension as round 1, finding 6. A one-line pointer like R15's would settle it.
3. Pre-mortem, now that "the measure" is the value target:
   - R3's cell says "The measure pairs the share of work with how often it is sent back or fixed". V1 pairs the share with first-check passing and reopening within 30 days. Send-backs and fixes are touches, which are the share itself.
   - R9 (line 205) says "the plan sets no default ... only once the owner chooses". The owner has since ruled that every result, passed or not, comes to a results card and nothing is dropped automatically (T13, T14).
   - R15's opening clause is still in the present tense.
   - These are passed pre-mortem text. They are for a pointer or a later change, not a block.
4. M7 line (117): It has no `· sprints: PR #93` or `· reached: 2026-11-11`, while section 4 line 145 says the owner accepted M7 as reached. The record says the line takes both in a commit whose `Owner-Ruling:` trailer names the ruling record, after the Critic's check (part B). This is correct as long as that commit follows. Do not add "reached" any other way.

**Changed sentences checked against the ruling and the question as filed**
- Section 4 short-reads row: Matches Part 6.
- Section 4 ceilings row: Matches Parts 2 and 3.
- Section 6 italic header: Matches Part 7. P18 is correctly left open.
- Section 6 last bullet (read as a check on the header): The counts (twelve confirmed, P1 to P11, P12 to P17, P19, P20) match. P18 is open, with a card of its own "before the trial design freezes".
- Section 7 opening paragraph, "The measure" sentence: True. V1 is the value target.
- R15 "What the plan does" cell: Matches Part 8, A. It does not overstate: the guards are cited.
- U2 fallback: Matches P5 and "How it is carried out".
- P18: Called open everywhere I looked (lines 180 and 188). No open term is called ruled.

**Six-part contract**
- **Changed:** nothing. Read-only. No files written.
- **Why:** to check round 2 of part A against the ruling and the question as filed.
- **Verified:**
  - Each round 1 finding against the fixed file.
  - Each changed sentence against /home/user/ml-fixed-259/decisions/questions/P-002-design-gate.md, /home/user/ml-cards/P-002-design-gate.md and /home/user/ml-fixed-259/docs/gates/P-002/trial-terms.md.
  - A search for "propos", "still to be set", "not yet ruled" and "to be ruled" in P-002.md. I read every hit; none was a ruled term called proposed except R7.
- **Undone:**
  - I did not read /home/user/ml-cards/P-002-value-target.md or P-002-trial-gates.md. I relied on trial-terms.md for the terms they set, as in round 1.
  - I ran no git, so the merge commit, the diff since round 1 and the `Owner-Ruling:` trailer are unchecked. I judged "changed" text from your list and by reading.
  - I did not read docs/briefs, docs/reports, docs/handoff, sessions or any -notes.md file.
- **Needed outside your surface:**
  - Chief of Staff: optionally fix R7 and R18 and add pointers for R3, R9 and R15 (findings 1 to 3).
  - Orchestrator: record this verdict verbatim, and make sure the M7 commit carries `· sprints: PR #93`, `· reached: 2026-11-11` and an `Owner-Ruling:` trailer naming decisions/questions/P-002-design-gate.md, after the Critic's check (part B).
- **Open questions:** none for the owner. P18 stays for its own card.
