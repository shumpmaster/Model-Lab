Verdict: FAIL

*The Critic's check of P-002's brief brought into line with the Design gate ruling (docs/projects/P-002.md at commit 59d5775), brief 257, part A; a session on a different model from the writer. Recorded verbatim by the orchestrator, 2026-11-11. Part B, the M7 line, is reviews/P-002-m7-line/critic.md.*

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
