# The Critic's re-check of brief 300's owner-words test and answer paths (brief 301)

*Recorded verbatim by the Orchestrator; the verdict file is reviews/Q-018-rules-2/critic.md. Brief 301 (docs/briefs/301-critic.md), on Model-Lab@8b49550 (brief 301's start line names the commit before it), S-002 as changed by brief 300 (commit c36f579). The Critic runs on a different model from S-002's writer (D-056) and apart from the Researcher.*

Verdict: PASS

In plain words: the changed question rule now gives the result the records show on every case the brief names. On Service-Desk #78, each of the 15 answer entries added while the piece was under way now counts, so the piece goes from one touch to 16. Each of the four operating-model pieces now counts the owner answers it actually got while it was under way. Service-Desk #26's edited ruling no longer counts twice. The Model-Lab piece whose only check record has no class is now undecided and listed. Brief 297's three wording points are fixed, and nothing else in the plan changed. Nothing blocks the re-run. The new test does let some agent text through: option texts the agent offered, its notes and corrections inside answer files, and one Service-Desk file that holds real answers but is classed as an unasked request. None of this changes any sampled piece's result that I could find, but it should be listed when the extract runs again. The ledger question to the owner is fair, with one overstated line: it says the ledger was the only record of early rulings, but plan drafts held them too. Nothing here is irreversible. Self-implication (D-050): finding 1's leak comes from the fix my own earlier check proposed (finding 8).

## Findings

1. **Non-blocking: the quoted-line form (2) also counts the agent's option texts.** S-002 :49.
   - Service-Desk 680797bd: of the 5 lines counted, 4 are the agent's option texts, "as offered" (records2/Service-Desk--d38d8364.md:583-586).
   - 3719ea74: of the 10 lines counted, 7 are option texts (:647-650, :653-655).
   - Each of these commits also adds the owner's own answer, so no touch changes. Touches are counted per commit, and out3.tsv shows no other change from 0 to at least 1 in Model-Lab or Service-Desk.
   - But the per-commit "owner-word lines" field (step 3, :109) is not a count of the owner's lines. Also, an append that adds only a question and its options under a heading like "questions and answers" would count as an answer.
   - Suggest: the memo treats the line count as a flag, not a measure, and lists each append whose only owner-word lines are form (2) or (3) lines, with no form (1) label.

2. **Non-blocking: the anywhere-quote form (3) counts agent lines in Personal-Org-Operating-Model's answer files.**
   - reviews/S-022/_owner-answers-2026-10.md:7 "The owner was told: "…"" is the agent's words to the owner.
   - The same file at :14 starts "On S-022 the owner gave no new answer", then quotes "1,600 words (S-022)".
   - reviews/S-025/_owner-answers-2026-10.md:24 and :31 are the orchestrator's notes ("the asked "Q4"", ("the Critic" to "the gate Critic")).
   - reviews/S-023/_owner-answers-2026-10.md:37 is a relay, and :109-111 is "Correction to answer 23 (… the orchestrator)".
   - On PO#25, #27 and #30, every commit counted also adds the owner's real choices, so no result changes that I could see.
   - A commit that adds only such a line, which the S-023 correction may be, would count as an append. I could not time it without git. The re-run should list each append counted only by form (3).

3. **Non-blocking: one Service-Desk "owner-request" file holds asked-and-answered questions.**
   - Rule :48 classes every `owner-request-` file as an unasked request (RT7).
   - docs/design/references/owner-request-2026-10-25-questions-and-order.md:17-28 holds the owner's answers to 8 questions put in a session. No decision record repeats them (grep of the clone: only specs, tests, reviews/M3G and this file).
   - In the sample, it is changed only by de012573, #237's first commit and so its dispatch (L25-Service-Desk-237.md:41-47). RT4 gives the same result, so nothing in the sample changes.
   - Add it to step 6's list beside Model-Lab's intake/P-002-owner-m7-sprint-review-2026-11-11.md, or class these files by their headings.

4. **Non-blocking: the Definer's open point, specs cited in passing.**
   - The reading is right: such a file names a piece by its text, like any record (:48).
   - It inflates touch counts on three pieces:
     - PO#25: S-023 and S-024's line :37, "1,600 words (S-022)".
     - PO#27: S-023's answers 36 and 37 name S-025.
     - PO#30: reviews/S-030/_owner-answers-2026-10.md:5-7 names S-029.
   - It cannot change V1 in the sample:
     - #20 and #22 cannot gain a touch: no answer file names S-010 to S-021 or #10 to #24 (grep, none).
     - PO#49 and PO#50 are unaffected by timing: q030 is added before #50's dispatch, and q031 after #49's merge (L50:137-153, L51:180-213).
   - Since the extract records which part of the naming rule matched (:109), the memo should give each piece's count with and without matches found only by a spec id in the text.

5. **Non-blocking: open question 15 overstates one fact.**
   - :258 says the ledger is "the only record of most of them", and the card's option A says rulings were kept "only in its ledger" (questions/P-002-ledger-answers.md:5 and :11).
   - Plan drafts also held rulings then: specs/S-020-usage-safe-stop-discovery.md:252 "Owner's rulings (2026-10-08)", specs/S-022-digest-budget.md:127 "(2026-10-10)". The S-022 and S-023 answer files both say their words "were first written down in the spec draft" (:4 and :5).
   - The source the question cites, reviews/S-031/_owner-answers-2026-10.md:5 "rulings in the ledger", describes how rulings are passed on, not that the ledger was the only record.
   - For #20 and #22 the point stands: S-017's and S-021's specs have no "Owner's rulings" section (grep).
   - Otherwise it is fair: three options, each with its cost, a recommendation and a default of none. It changes no rule: the ledger is listed only (:48), and the gloss is added (:110).
   - Reword it as "the ledger and the spec drafts".

6. **Non-blocking: two codability gaps in the removed-line matching (:49).**
   - A line can hold two forms (for example `1. "<q>" Answer: "<a>"` is both form (1) and form (2)). The rule does not say which form it is matched under. Suggest: the first of (1), (2), (3).
   - Matching goes by form, not by text, so a changed ruling (`Ruling: no` to `Ruling: yes`) is matched away. It is listed, so the hand check sees it.

7. **Confirmed against the records (items 1, 2 and 4):**
   - **SD#78:** I read each of the 15 appends by hand under forms (1) and (2), and each count matches out3.tsv:115-129 (2, 1, 4, 1, 1, 1, 1, 1, 1, 5, 4, 1, 10, 3, 1). 7e3e6071 (:563) and 1cf4987a (:624) are caught only by "verbatim" with "owner's". So RT1(a) goes from 1 to 16.
   - **PO#30:** its own file is first added in the window (667e193c) and then appended (879f5e3a, 83cc104b) (L47:61-178). That is at least 3.
   - **PO#25:** e3086031, 6e37e45e and 71bff0be (L57:68-119). The real owner choices are at :9-10, :18 and :20.
   - **PO#27:** 50893c0c is the dispatch (RT4), and the four S-025 appends follow.
   - **PO#35:** the dispatch is 71755edc (RT4). The count is the question file Q-024 (b42818e8) plus cac877e8. 59c359a1's answer 3 is one question with Q-024 (reviews/S-033/_owner-answers.md:9). So 1 goes to 2, which is right.
   - **SD#237:** 7234f058 adds 1 (L25:34-40).
   - **Kept out:** `Owner-Ruling:` (ML 56004034 and b6081c5a, unchanged at 1) and "Answered in draft 2:" (SD e24f55f9, 0).
   - **Finding 3:** 4977c952's added `Ruling:` line is matched by the `Ruling:` line it removes, so SD#26 goes from 2 to 1 (records2/Service-Desk--233211a9.md:21-31; out3.tsv:66).
   - **Finding 7(a):** fixed at :59, with ML#98 named.
   - **Brief 297's findings:** 2 is fixed at :46, 4 at :61, and 5 at :62.
   - **Unchanged:** only :46-49, :59, :61, :62, :109, :110 and :258 change. The draw, sample, seed, cut-off, edge-case filters and table, and RR1 to RR3 are untouched.
   - **Pairing and paths:** the pairing of a Personal-Org-Operating-Model question file with its `_owner-answer-q<nnn>.md` file fits the clone (S-035 to S-037), and each answer file at the cut-off holds its folder's spec id. The Model-Lab intake copies each repeat a decision record (two-look-line, design-gate, value-target, plan-stop, trial-gates). m7-sprint-review is the exception, and the Definer listed it.

8. **Self-implication (D-050).** My brief-299 finding 1 proposed counting "a double-quoted passage under a line naming … answer", and that is the leak in finding 1 above. This check also re-checks fixes to my own findings (brief 299's 1 to 3 and 7(a); brief 297's 2, 4 and 5). Triage should weigh finding 1 as partly caused by my own proposed fix.

## Six-part contract
- **Changed:** nothing. I hold no write tool.
- **Why:** brief 301, re-checking brief 300's change to S-002 (commit c36f579) before the extract is re-run (P-002, M8).
- **Verified:** Read, Grep and Glob only.
  - The diff (s002-300.diff, all of it); docs/briefs/300-definer.md and 301-critic.md; reviews/Q-018-recode/_critic-verbatim.md; reviews/Q-018-extract-widened/_critic-verbatim.md (findings 1-9); questions/P-002-ledger-answers.md.
  - out3.tsv (all of it); the pack's records2 for Service-Desk d38d8364 (all 704 lines) and 233211a9, Personal-Org-Operating-Model ad6df430 and c4fc482f; pack L25, L41, L47, L50, L51 and L57.
  - Clones: Personal-Org-Operating-Model reviews/S-022, S-023, S-024, S-025, S-029, S-030 and S-033 answer files; the `_owner-*` glob; greps of reviews and specs for spec ids and "Owner's rulings". Service-Desk docs/design/references/owner-* and the two 2026-10-25 files; reviews/77/reviewer.md headings; a grep for the questions-and-order answers. Model-Lab intake/ and decisions/questions/P-002* globs.
- **Undone:**
  - Per-commit timing of Personal-Org-Operating-Model answer-file appends: there is no git, and the pack holds those files only as they stand at the cut-off. So I did not compute exact counts for PO#25, #27 and #30 (the Definer gives "3 to 5", at least 3 and at least 4), and could not time S-023's correction section.
  - I did not scan every check record for headings that name another kind under :62.
- **Needed outside my surface:**
  - The Definer: wording for findings 3, 5 and 6, if taken.
  - The Orchestrator and Researcher, at the re-run: list the appends counted only by form (2) or (3), and the touches found only by a spec id in the text (findings 1, 2 and 4).
  - Triage: finding 8.
- **Open questions:** whether the passing-mention counts (finding 4) should become an owner question beside open question 11, or stay a listing.

Key paths:
- /home/user/Model-Lab/specs/S-002.md
- /home/user/Model-Lab/questions/P-002-ledger-answers.md
- /tmp/claude-0/-home-user/b9b3c098-5ac2-5fab-85c9-5ae65240ab9c/scratchpad/q018-pack2/records2/Service-Desk--d38d8364.md
- /tmp/claude-0/-home-user/b9b3c098-5ac2-5fab-85c9-5ae65240ab9c/scratchpad/hc/Service-Desk/docs/design/references/owner-request-2026-10-25-questions-and-order.md
- /tmp/claude-0/-home-user/b9b3c098-5ac2-5fab-85c9-5ae65240ab9c/scratchpad/hc/Personal-Org-Operating-Model/reviews/S-022/_owner-answers-2026-10.md
- /tmp/claude-0/-home-user/b9b3c098-5ac2-5fab-85c9-5ae65240ab9c/scratchpad/hc/Personal-Org-Operating-Model/reviews/S-023/_owner-answers-2026-10.md