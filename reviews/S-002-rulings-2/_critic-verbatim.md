# The Critic's re-check of brief 316's fix (brief 317)

*Recorded verbatim by the Orchestrator; the verdict file is reviews/S-002-rulings-2/critic.md. Brief 317 (docs/briefs/317-critic.md), on Model-Lab@3d1e8b3 (brief 317's start line names the commit before it), S-002 as changed by brief 316 (commit e89aa2c). The Critic runs on a different model from S-002's writer (D-056), apart from the Definer and from brief 315's Critic. While it ran, the shared checkout was on another branch for about a minute; its return cites lines only the fixed text holds (open questions 17 and 18), so it read the fixed text.*

Verdict: FAIL

Brief 316's fix closes all three blocking findings from brief 315. The later-work code now goes to the Critic, with a second Critic checking every code. The live count takes its code from the touch log. A ledger copy of a piece's starting ruling is now skipped. Both new rulings are written in with the owner's exact words and the cards' exact option text, and the non-blocking findings are fixed. The re-count can start on these rules. One new problem blocks the freeze, though not the re-count. In live trials, the role that decides whether a question asks for later work, and so whether it counts as a touch, is the Chief of Staff. The Chief of Staff knows which side each trial piece is on, and nobody checks its codes. The plan lists every other way someone who knows the sides could steer a trial, and this one is missing from that list. Several smaller points follow. The two new decision records the spec cites are not on this branch yet. One sentence about the counting script is wrong. On the records, Personal-Org-Operating-Model #20 (POOM #20 below) should go from 0 touches to 4, not 2 (my own earlier estimate in brief 315 was wrong). I could not see the Definer's table of expected changes, so I give my own reading of the records.

## Findings

1. **Blocking, for the Definer, with a gap for the owner. A coder who knows the sides is not disclosed.** specs/S-002.md:197 (J9) and :189 (J1): in the live count the Chief of Staff gives `later_work` for every question and note. A "later work" code takes the touch off the piece, and that changes a trial's deciding measure. experiments/E-004.md:149 says "The agents and the Chief of Staff know which pieces carry the method". No second check of the live codes exists. The card's gain "every code is checked" (questions/P-002-later-work-coder.md:10) is true only of the past count. The spec's lists of what a trial cannot catch leave this out: the plain-words paragraph (:10), J3 (:191), J4 (:192), Risks (:235) and E-004 "What this trial cannot catch" (:146-151, and Steps 1 and 8). The Definer should add it to each of those. The owner should then choose:
   - (a) leave it as a stated limit;
   - (b) have a fresh session that is not told the side check every live `later_work` code on trial pieces before each look is judged;
   - (c) for trial pieces only, treat every question as "not said", so it always counts.

   (b) and (c) go beyond ruling 17's words, so the owner must choose.

2. **Closed: brief 315 finding 1 (who codes `later_work`).** Step 3 *Later work* (:109): the Critic codes, and a second fresh Critic checks every code. Step 4 (:110): the Researcher takes the codes from the extract and codes none of its own. "From the extract alone" is kept (:114 item 4, :266). The Researcher sees only codes keyed by label, no text, so nothing from `decisions/**` reaches it (governance/PACKS.toml:24).

3. **Closed: brief 315 finding 2 (the live count cannot apply ruling 11).** J9 (:197) has `later_work`, `record` and `commit`. J1 (:189) reads those fields, and a question with no code is recorded as "not said". "Not said" counts "in every figure toward V1 and in a trial's deciding measure". That matches option A: "Where a record does not say, the touch counts on the piece under way and is listed for you" (questions/P-002-later-work-coder.md:9).

4. **Closed: brief 315 finding 3 (a ledger copy of the starting ruling counts).** Line 48 adds the skip and quotes option B word for word (questions/P-002-ledger-copy-of-start.md:12). Step 3 adds `same_words_in_start`. I checked both sampled cases:
   - **POOM #50:** L-0157's only quoted passage, "A — approve and build (Recommended)", is at line 5 of reviews/S-037/_owner-answer-q031.md. That record was first added in #50's first commit 7f30440, the dispatch (research/Q-018-extract/sample.jsonl:50). The extract reads that line as the owner's words by form (3) (research/Q-018-extract/extract.py:476). So the entry is skipped and #50 goes back to 0.
   - **POOM #49:** L-0156 (447cf875) has one quoted passage, "Merged, I want to go with your reccomendations on all of them". It is at line 5 of reviews/S-036/_owner-answer-q029.md (558fd054), first added in #49's first commit 3681644a (sample.jsonl:51). So it is skipped, and #49 goes back to 1 touch: the Q-031 question file de17627b, filed in #49's own window. That remaining touch depends on the Critic's code. Q-031 asks for approval of S-037, whose plan #49 itself adds (a84d1847, plus its plan-review records), so I read it as "this piece" or "not said". Either way it counts.

   The Definer's "#49 and #50 back" is right on the records.

5. **Non-blocking. The two rulings match the cards, with one small addition.** Open questions 17 and 18 (:262-263) and their quotes match docs/handoff/2026-11-12-chief-of-staff-p002-16.md:40-41 word for word. The additions are:
   - A Critic code the second Critic does not confirm is taken as "not said" (:109). This leans the same way as the card ("errs toward counting you as needed"), so I see no issue.
   - "until the owner rules" (:109) adds a settle-by-hand step. On the card that step is a cost of option B, not A. Better wording: the code stays "not said", so it counts, and is listed.
   - The J9 lines for questions the records show (finding 12): a fair way to carry out "codes it in the touch log".

6. **Non-blocking, needs action before the plan review passes. The cited decision records do not exist yet.** decisions/questions/P-002-later-work-coder.md and P-002-ledger-copy-of-start.md are cited at :46, :48, :52, :55, :109, :189, :197 and :262-267, but neither file is on orch/p002-fix. The handoff (:38) says the answers are "not yet recorded". Both records must land with the owner's exact words before any review can check these citations.

7. **Non-blocking; self-implication (D-050). J1's "the script reads no record's text" is wrong** (:189). To apply RT1(a), count.py has to read record text: the `#<n>`, brief and spec naming rule (:46), the owner's-words forms (:49) and RT5's class (:53). What it cannot do is judge what a record means. This premise came from my own role's earlier check (reviews/S-002-rulings/_critic-verbatim.md, finding 2: "it reads no text"). Suggested wording: "the script makes no judgement of a record's meaning, so…".

8. **Non-blocking; self-implication (D-050). POOM #20 goes from 0 to 4, not 0 to 2.** sample.jsonl:60 shows #20 carries briefs s-017, s-018 and s-019, with commits whose `Spec:` lines are S-017 (cc7730be), S-018 (a21f4e8e) and S-019 (08fead05).
   - L-0122 is the S-018 freeze, "Yes I want to skip noise", added at 17:26:38.
   - L-0123 is the S-019 freeze, "Approve", added at 17:54:04.
   - Both are approvals of work #20 itself carries, both are added by #20's own commits, and both name #20 by spec. So both are "this piece", not "later work".
   - L-0121, "Approve", at 17:07:42, and L-0124 (names "PR 20"; its part (2) is about #20's build-review pins) also count.
   - None is skipped by ruling 18: #20's first commit c1be111b adds no question, decision or answer record, and "Approve" stands in no answer record in the clone.

   My brief 315 finding 6 read L-0122 and L-0123 as "likely later work" and guessed 0 to 2. That was wrong. If the Definer's expected change for #20 is 0 to 2, it is wrong too.

   - **POOM #22:** 0 to 1 (L-0128, 20cf0bd6, at 17:20:58, not skipped: no record of the starting ruling holds "Yes, fix it now (Recommended)").
   - **What the coder needs:** each piece's brief numbers and spec ids from the extract. Without them, the freeze of a spec the piece carries looks like other work.
   - **Step 6 (q) (:112):** should name L-0122 and L-0123 beside L-0121.

9. **Non-blocking. Unclear: can a ledger entry skip another ledger entry?** Line 48 makes each entry "a decision record of its own". It then skips an entry when "a decision or answer record counted on that piece" holds the same words. If that includes other entries, L-0123's "Approve" stands character for character in L-0121's `decided_by:` line, and #20 drops to 3. Two different approvals would then collapse into one. Whether #20 needs the owner does not change, but the count and the Researcher's coding do. The Definer should say whether entries are skip sources. I'd say they are not, or else it should be listed in step 6 (r). Brief 315 missed this (self-implication, D-050).

10. **Non-blocking. "The ruling that started the piece" is only defined for pieces dispatched by their first commit.** RT4 (:52) names the starting ruling only for that case. For a piece dispatched by its brief record, "a record added at the dispatch is outside the window" and is not called the starting ruling. So `same_words_in_start` is empty, and a ledger copy of that record would count again. No sampled POOM piece has a brief record (sample.jsonl:31-60 all give `"dispatch_from": "first commit"`). But this can happen in the live count. The Definer should define the starting ruling for brief-dispatched pieces as a record first added at the dispatch commit. It should also list in step 6 a ledger copy, inside the window, of an answer recorded before the dispatch.

11. **Non-blocking. A record that asks both about the piece and about other work has no code rule.** L-0124 asks (1) whether to continue P-001 and (2) whether to cover #20's pins. Step 3 (:109) gives three codes but does not say how to code such a record. I suggest: "this piece" when any part asks about the piece under way.

12. **Definer's open questions.**
    - **(1) A code the second Critic does not confirm is taken as "not said":** no issue. It fits option A. See the wording note in finding 5.
    - **(2) RT7 notes coded for later work on RT7's own words:** no issue. RT7 covers an instruction "that changes a piece already under way" (:55). A note asking for a change after the piece lands is outside that, by RT7's own words. Counting it on that later work mirrors RT4, and it closes brief 315 finding 11.
    - **(3) The Chief of Staff logs a line for each question the records show:** a fair way to carry out "codes it in the touch log when each touch is logged". Faults for the Definer: finding 1 (not disclosed), and one wording point. J1 should say that a log line with a non-null `record` carries only a code and is never an RT1(c) touch itself. Today only J9's "counted once" (:197) says this. A missed line counts as "not said", which errs toward counting, so it is safe.

13. **Non-blocking. The coder's pack** (:109, "its records pack and the repositories"). The full clones hold `docs/briefs/**` and `docs/reports/**`, which the Critic's pack keeps out (governance/PACKS.toml:42). The coder needs only the listed records, as the read commit left each one. The spec should name the records pack as the coder's source.

14. **Brief 315's non-blocking findings.**
    - **4:** fixed; `asked_q` pairs the entry with its question file (:48, :109).
    - **7:** fixed; step 6 (l), (q), (r) and (s) (:112). Finding 8 above adds a small item.
    - **8:** fixed; every code is checked (:109, :111).
    - **9:** fixed. The Orchestrator recomputed the order with hashlib (research/Q-018-extract/README.md:112). It matches :111, and reviews/Q-018-recode-4/_critic-verbatim.md:65 confirms all ten were opened.
    - **10:** fixed; the card's words are cited at 2374271^ (README:112). I could not run git to read that commit.
    - **11:** fixed (:55).
    - **12:** fixed (:114 items 1 to 4, :266).

## Six-part contract
- **Changed:** nothing; I am read only.
- **Why:** brief 317, the re-check of brief 316's fix to specs/S-002.md before the re-count.
- **Verified:** Read, Grep and Glob only, with no shell.
  - specs/S-002.md:1-278, all of it.
  - Brief 315's findings, the two question cards, the handoff section and the list of decision records under decisions/questions/. The two new records are missing.
  - governance/PACKS.toml.
  - sample.jsonl lines 50, 51 and 60, and the dispatch fields of every row.
  - research/Q-018-extract/README.md:108-112, and extract.py:476 (form (3) applies to `_owner-answer*`).
  - In the POOM clone: docs/LEDGER.md L-0121 to L-0124, L-0128 and L-0155 to L-0157; reviews/S-036/_owner-answer-q029.md; reviews/S-037/_owner-answer-q031.md.
  - Records pack: Personal-Org-Operating-Model--de17627b (Q-031).
  - experiments/E-004.md:146-151; reviews/Q-018-recode-4/_critic-verbatim.md.
- **Undone:**
  - The diff of e89aa2c and commit 2374271^ (no git).
  - POOM #25, #27 and #30's ledger entries, and Model-Lab #81.
  - Comparison with the Definer's table of expected changes, which my pack keeps out.
- **Needed outside its surface:**
  - The Chief of Staff records the two decision records (finding 6).
  - The owner rules on finding 1's options once the Definer has written in the disclosure.
  - Triage of my D-050 flags (findings 7, 8 and 9).
- **Open questions:**
  - Finding 1: should the live `later_work` codes on trial pieces be checked by someone not told the side?
  - Finding 9: is a ledger entry a source for skipping another entry?

Files: /home/user/Model-Lab/specs/S-002.md, /home/user/Model-Lab/experiments/E-004.md, /home/user/Model-Lab/research/Q-018-extract/sample.jsonl, /home/user/Model-Lab/research/Q-018-extract/README.md, /home/user/Model-Lab/research/Q-018-extract/extract.py, /home/user/Model-Lab/governance/PACKS.toml, /home/user/Model-Lab/questions/P-002-later-work-coder.md, /home/user/Model-Lab/questions/P-002-ledger-copy-of-start.md, /home/user/Model-Lab/docs/handoff/2026-11-12-chief-of-staff-p002-16.md, /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/hc/Personal-Org-Operating-Model/docs/LEDGER.md
