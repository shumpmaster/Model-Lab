# The Critic's E-RT4 check of the new tenth piece, and its re-check of brief 311 (brief 312)

*Recorded verbatim by the Orchestrator; the verdict file is reviews/Q-018-recode-4/critic.md. Brief 312 (docs/briefs/312-critic.md), on Model-Lab@64f8b14 (brief 312's start line names the commit before it), S-002 as changed by brief 311 (commit 9eb6077), with the records pack built by brief 307. The Critic runs on a different model from S-002's writer (D-056) and apart from the Definer.*

Verdict: PASS

The one thing that blocked my last check is now closed. Model-Lab #93 is the new tenth piece in the check of questions that name only a milestone. I opened every question and decision file first added while it was under way. There are exactly two, a stop-rule question and its answer. Both name #93 (one by being its own file, the other by its pull request number), and both are about the piece's own plan. So neither is milestone-only, and the rules count them as one question, which is what the memo already says. The line in open question 10 can now say I checked both sets as the sample stands. Brief 311's changes are right against the records, can be coded from the extract with no text written, and change no sampled count or time. On Model-Lab #29, the Definer is right and memo 4 and my own earlier finding were wrong: the question file was first added at 23:55:58, before #29's window opens. Nothing changes for #29, because the question is timed by its decision record either way. I found nothing new for step 6's list. The memo and the checks together close step 6. What is left are four small wording and records fixes, none blocking. Nothing here is irreversible. Two findings implicate my role's earlier checks (finding 7).

## Findings

**1. E-RT4 on Model-Lab #93: closed (closes brief 310 finding 1). Non-blocking notes only.**
- #93's window runs from 2026-11-11 02:46:02 (dispatch by its first commit, 565aa90e) to 04:21:18 (merge) (pack L07 :227-229; research/Q-018-extract/Model-Lab.list.jsonl:93).
- **The full set of in-window files.** Only #93's own commits (02:46:02 to 03:08:30, L07 :22-189) and #94's commits (03:50:31 to 04:21:58, research/Q-018-extract/Model-Lab.M.jsonl:92) have Model-Lab commit times in the window. Model-Lab.D.jsonl has none. Of those commits, only two add a question or decision file:
  - 22147854, questions/P-002-brief-stop.md, added 03:08:30 by #93's own commit 8af03d2e.
  - 31505fb6, decisions/questions/P-002-brief-stop.md, added 03:50:31 by dc39b953 (#94's first commit).
- **Files just outside the window.** The trial-gates and value-target files (086b9225, bf61a933, b3609d4c, 02:22:27 to 02:32:58) come before the dispatch. The design-gate files (4973eb45, 56004034) come after the merge. P-002-two-look-line is from PR #99.
- **The question file 22147854** (records/Model-Lab--22147854.md):
  - Its text names only `Milestone: Discovery-8` (:4) and no number, brief or spec. It names #93 by being #93's own file (:46 "What a touch is").
  - It was asked about the piece: it is the stop card on "the screening's brief", which is docs/projects/P-002.md, the plan #93 changes (L07 :4).
- **The decision 31505fb6** (records/Model-Lab--31505fb6.md) names the piece by number: ":7 … from questions/P-002-brief-stop.md (filed in PR #93; …)".
- **How the rules read them** (:47, :53):
  - They are one question, timed at 03:08:30 by the question file's first add, which is in the window and not in the piece's first commit.
  - RT5 gives no class. The `Asked:` line lacks the ": the owner's own <word>, never a default" form, and `RISK CLASS: R0 (questions/**)` does not end ", the owner's own <word>)". So (d) applies, and "brief-stop" holds no gate word. It is counted under RT1, and listed with Discovery-8 (Open question 13).
  - This is exactly memo 4 :33 and :176 (1/1/1).
- **Result:** #93 adds no milestone-only case and no missed touch. This matches my line-order reading in reviews/Q-018/_critic-verbatim.md:115 and reviews/Q-018-recode/_critic-verbatim.md:62.
- **Open question 10 (:253):** with this check (set (a), #93) and brief 310 finding 1 (set (b), SD #341), the line can now read that the Critic checked both sets as the sample stands after #237 stopped being a piece.
- **Note on the order.** I cannot compute SHA-256, so the order of the ten rests on the Orchestrator's and the Definer's computations. My brief 310 finding 1 gave an order (POOM #35 and ML #43 last) that differs from this brief's (2nd and 4th). That list was grouped as my 2026 finding 7 mentioned the pieces, not in hash order. The nine pieces other than #93 are the same in both, so the tenth does not depend on this.

**2. Brief 311's changes: right, codable, and no sampled count or time changes. Non-blocking: one step 3 wording gap.**
- **K3 (:41), "added plus … removed lines":**
  - Right, and the extract carries both numbers.
  - Memo 4 :17 already coded it this way, so no kind changes. My three spot checks in brief 310 finding 7(a) still hold.
- **RT1(a) "first add or an append" (:47):**
  - It can be coded. The extract's `question_ids_in_owner_word_lines` is on every in-window commit, first adds included (README :81). In sample.jsonl, the first-add commits carry it, and only lines 41 and 57 hold an id, both on appends. So no count changes.
  - Gap: step 3 (:109) still says ids are given "for each append to an answer record". It should say "for its first add and each append", to match RT1(a) and the extract.
- **RT1(a)'s paired-record clause (:47):**
  - Right. It can be coded from `names_by`, `names_from` and `names_from_time`. It matches the memo's timing of #29 at 00:38:22: 9acdfce2 was first added 2026-11-02T00:38:22Z (pack L03 :329).
  - Its #29 example is still true. After finding 3, though, it no longer shows a case where the clause is needed, since the question file's first add falls outside the window anyway. The Definer may keep it as an illustration.
- **Step 6 (m) (:112):** the #47 and #49 reason now reads as my brief 310 finding 8 fix. Right.
- **Step 6 (p) (:112):** matches brief 310 findings 5 and 9(a), and the records they cite (POOM docs/LEDGER.md:325; records2 e219aae3 :328, :342). Right.
- **Open question 10 (:253):** right as it stood at hand-out. Its last clause, "the Critic has yet to open #93's questions and decisions", is now out of date (finding 1).

**3. The Definer's question on ML #29: the Definer is right. Non-blocking.**
- research/Q-017-extract/Model-Lab.commits.jsonl:822 shows `<questions:197dd190>` "added" by fc06e7c9 at 2026-11-01T23:55:58Z, which is #26's own commit (Q-018-extract/Model-Lab.merged.jsonl:26). It was then changed by adcd44ae at 23:57:25 (:819). The same path was added separately on #25's branch by 54c31b93 at 23:58:10 (:815).
- Both commits are reachable at the cut-off, so the earliest commit that adds the file is fc06e7c, before #29's window opens at 23:56:17.
- The extract's widened field agrees: research/Q-018-extract/sample.jsonl line 9 gives 197dd190 `"first_added": "2026-11-01T23:55:58Z"`.
- So memo 4 :128 ("first added at 23:58:10 … inside #29's window") and my brief 310 finding 7(b) are wrong on the time.
- **What changes:** nothing for #29. The question file has no in-window first add, and under the paired-record clause it would not time the question even if it did. The question stays at 1, timed by the decision at 00:38:22. The extract ran its naming test on fc06e7c's text and does not list 197dd190 as naming #29 (sample.jsonl line 3).
- **Root cause:** the older fields and the records pack find first adds without `--full-history`, which leaves out side branches. The older fields are `questions_decisions` (sample.jsonl lines 3 and 18, 23:58:10). The pack is pack.py:32, records/Model-Lab--197dd190.md:1, which holds 54c31b93's text, not fc06e7c's. The rule-level fields use the earliest commit over full history (extract.py:432-448). The memo and my check took the time from the older field and the pack.
- **Fixes:**
  - Researcher: correct memo 4 :128.
  - Definer: in "What a touch is" (:46), make "the commit that first adds it to the default branch" say "the reachable commit with the earliest commit time that adds it", which is what the extract does. Otherwise it can be read as landing order: #25 merged at 00:35:55, before #26 at 00:36:04.
  - Orchestrator: in later packs, show the full-history first add, or mark where it differs from the older field.

**4. Brief item 4, step 6: nothing new for its list.**
- Finding 3 is a wording and records-pack fault, not something the rules cannot catch.
- Finding 2's gap is wording only.
- So step 6's list (a) to (p) (:112), the memo, and the Critic's checks together close step 6 and M8's last clause, once finding 1's line in open question 10 is updated.

**5. Non-blocking: the full-history issue may touch my earlier pack-based checks.**
- My E-RT4 readings of the other nine pieces used the pack's first-add times and texts.
- Where a record was added on two branches, the pack can give the later add. For #93's two files the old and widened times agree (L07 :219-220, :236-237).
- I did not compare the other nine pieces' in-window files field by field. The Orchestrator can list every sampled record whose older `first_added` differs from its widened `first_added`. That one list would settle it.

**6. The ten pieces under reading (a)** are as given (SD #230, POOM #35, SD #341, ML #43, ML #29, SD #22, ML #92, SD #78, SD #148, ML #93). Every one has now been opened for E-RT4: nine in reviews/Q-018/_critic-verbatim.md finding 7 and reviews/Q-018-recode/_critic-verbatim.md finding 6, and #93 here.

**7. Self-implication (D-050). Triage should count these as misses by my role's earlier checks.**
- My brief 310 finding 7(b) gave 197dd190's first add as 23:58:10 by #25's commit, inside #29's window. It was 23:55:58 by #26's commit, before the window (finding 3). The two-readings question it put to the Definer has no real case at #29.
- My brief 310 finding 1 presented a grouped list of the ten as if it were the hash order (finding 1, note on the order).
- Possible further misses: my earlier E-RT4 and timing checks relied on pack first-add times taken from simplified history (finding 5).

## Six-part contract
- **Changed:** nothing. I hold no write tool.
- **Why:** brief 312: close brief 310's blocking finding (E-RT4 under reading (a)), re-check brief 311's changes, settle the Definer's #29 question, and say whether step 6 closes (P-002, M8).
- **Verified:** with Read, Grep and Glob only, with no shell and no git.
  - Model-Lab: AGENTS.md; .claude/agents/critic.md; docs/briefs/312-critic.md; specs/S-002.md :1-125 and :240-274; research/Q-018-memo-4.md in full.
  - Review records: reviews/Q-018-recode-3/_critic-verbatim.md in full; reviews/Q-018/_critic-verbatim.md :94-121; reviews/Q-018-recode/_critic-verbatim.md :44-73.
  - research/Q-018-extract: README.md (:46, :57, :77-81); Model-Lab.list.jsonl :90-93; Model-Lab.M.jsonl :92 and a scan of commit times on 2026-11-11 02:00 to 04:59; Model-Lab.D.jsonl (none); sample.jsonl greps for `first_add`, `question_ids_in_owner_word_lines` and 197dd190; extract.py :278-302 and :432-448.
  - research/Q-017-extract/Model-Lab.commits.jsonl :808, :815, :819-822.
  - The pack: L07-Model-Lab-93.md in full; L03 (197dd190 and 9acdfce2 lines); records Model-Lab--22147854.md, --31505fb6.md and --197dd190.md.
  - The clone (hc/Model-Lab): decisions/questions/P-002-* listing and dates; P-002-two-look-line.md :2, :6, :12.
- **Undone:**
  - I did not recompute the SHA-256 order.
  - I could not read fc06e7c's version of 197dd190 (no git). I relied on the extract's naming result for it.
  - I did not compare older and widened first-add times for the other nine E-RT4 pieces (finding 5).
- **Needed outside my surface:**
  - Definer: open question 10's line (finding 1); the step 3 wording (finding 2); the "first adds it" wording (finding 3).
  - Researcher: memo 4 :128 (finding 3).
  - Orchestrator: the full-history first add in packs, and the list of differing first-add times (findings 3 and 5).
  - Triage: finding 7.
- **Open questions:** nothing new for the owner.

Key paths:
- /home/user/Model-Lab/specs/S-002.md
- /home/user/Model-Lab/research/Q-018-memo-4.md
- /home/user/Model-Lab/research/Q-018-extract/sample.jsonl
- /home/user/Model-Lab/research/Q-018-extract/extract.py
- /home/user/Model-Lab/research/Q-017-extract/Model-Lab.commits.jsonl
- /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/q018-pack-307/L07-Model-Lab-93.md
- /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/q018-pack-307/records/Model-Lab--22147854.md
- /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/q018-pack-307/records/Model-Lab--31505fb6.md
- /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/q018-pack-307/records/Model-Lab--197dd190.md
