# The Critic's re-check of brief 305's K1 fix (brief 306)

*Recorded verbatim by the Orchestrator; the verdict file is reviews/Q-018-rules-3/critic.md. Brief 306 (docs/briefs/306-critic.md), on Model-Lab@9523e46 (brief 306's start line names the commit before it), S-002 as changed by brief 305 (commit c866461). The Critic runs on a different model from S-002's writer (D-056) and apart from the Definer.*

Verdict: PASS

**Summary.** Brief 305's fix to K1 does its job. Every file at the owner-answer paths, and every Service-Desk `docs/design/references/owner-*` file, is now classed as owner question or answer. Service-Desk #237 is no longer a piece. Service-Desk #148 and #61 and the six Personal-Org-Operating-Model pull requests stay pieces, and none changes kind. No other rule that reads a file's class gives a different result on any sampled item, and none of the draw's edge-case filters now picks a different item. The new step 3 field, step 6's (a) to (h), open question 16, the rewording of open question 15 and the reworded line 48 match the records and can be coded without writing any text. One fact is wrong: the owner's GitHub-plan file holds two answers to session questions, not one. It is not blocking, because those answers are not read and nothing counted changes. Nothing here is irreversible.

## Findings

**1. Non-blocking: owner-github-plan-2026-10-18.md holds two answers, not "one" (S-002.md:48 and :112, step 6(g)).**
- The Service-Desk clone's docs/design/references/owner-github-plan-2026-10-18.md has two session questions, each answered:
  - :5 "Which GitHub plan…" answered: "Pro".
  - :13 "Is a payment method on file…" answered: "Card on file, over 3,000".
- :21 is also an unasked instruction from the owner, given verbatim.
- Neither line is read under RT1(a), so no count changes.
- Fix (Definer): "one" becomes "two" at :48 and :112(g).

**2. Item 1, K1 change (iii) (:20) tested against the clones and the extract.**
- **What it classes.** The 13 `owner-*` files directly in Service-Desk's docs/design/references/ are all records of the owner's words: their headings read "The owner's request / report / answers / workflow / GitHub plan / word …". The 19 Personal-Org-Operating-Model `reviews/<folder>/_owner-answer*.md` files are all answer records.
- **What it leaves alone.** Agent files in the same folder keep their class:
  - research-2026-10-19-modern-mobile-design.md (label 0ef5d2b4, 42 lines) stays research.
  - So do README.md and comments-2026-10.md.
  - `_owner-instruction-` files stay records.
- **Labels checked.** In the extract, the 12 "other reference file" labels plus 5ae5d612 (owner-answers) cover all 13 files.
- **Sampled items touching these files.** Only Service-Desk #237 (sample.jsonl:25) and #148 (:69) change any of them.
- **Each named item's piece status and kind** (I worked these out myself; see "Undone" for why I did not compare with the Definer's table):
  - **Service-Desk #237: leaves.** Its only research files, 5ae5d612 (owner-answers) and e719ce00 (owner-request), become owner question or answer. What is left is 5 question files and 7 records. Not a piece; no kind.
  - **Service-Desk #148: stays, kind plans.** Four of its research files become owner question or answer: 0695bbf6, 1c669f9a, 96e547ef and bcc111f8. It keeps 0ef5d2b4 (research), 3 built files (68 lines) and well over 1,700 plan lines. K3 gives plans either way.
  - **Service-Desk #61: stays, kind plans.** It touches no reclassed file. It has 1,471 plan lines, and its research is 7827ee96 plus three files with no lines.
  - **Personal-Org-Operating-Model #35, #30, #50, #49 and #27: stay, kind built.** Each changes its answer files (0d5230c0, 455192c4, df986385, 558fd054 with 08ba8ef8, and c4fc482f), which move from records to owner question or answer. Neither class is built, plan or research, so neither piece status nor K3's line counts change. All five have no brief role (K3), and built work has the most lines in each.
  - **Personal-Org-Operating-Model #25: stays, kind plans.** Its answer file is ad6df430. By K3 it has 258 plan lines against 129 built.
- **Across all of frame M**, the other Service-Desk pull requests touching these files (#115, #128, #217, #236, #247, #248, #252) all keep built or plan files. #237 is the only one that leaves.
- **A small note, older than this fix.** Change (iii) also classes Service-Desk's role notes under decisions/ (46 `-notes*.md` files) as owner question or answer. extract.py's `_label_of` already did so by rule 1. RT1(a) leaves them out by name (most end `-notes.md`; the two batch records end `-notes-1.md` and `-notes-2.md` and are read), and none holds "reviewer comment", so nothing is affected.
- **Not caught by (iii):** comments-2026-10.md ("The owner's design comments… word for word") and references/README.md (the owner's words, verbatim) stay research.
  - In the sample, no pull request has them as its only built, plan or research files.
  - Step 6(a) covers the general case, but it says "answer record". The Definer may want it to say "a record of the owner's words".

**3. Item 2, other rules that read a file's class: none changes a sampled result.**
- **RT1(b):** the moved Personal-Org-Operating-Model answer files hold no "reviewer comment" line, and neither do Service-Desk's decisions/, questions/ or references/ files.
- **RT2(a):** no commit under the owner's identity in the sample touches a reclassed file. All 19 such commits change only records files.
- **K3:** only #148's research lines fall (163 to 42 added lines). Its kind stays plans.
- **Edge-case filters at the draw:**
  - E-RP3: no newly matching pull request.
  - E-K1: #78 and #148 still match. #217, #247, #248 and #252 stop matching, but none of them was drawn, so the draw is unchanged.
  - E-K3 and E-RP5 were "not seen", and taking files out of research cannot add a match.
  - E-RT3: no web-editor commit under the owner's identity in any frame M row changes one of the 13 Service-Desk files or the 19 Personal-Org-Operating-Model answer labels, so it stays "not seen".

**4. Item 3, against the records and whether each can be coded with no text written.**
- **Step 3's clear `Q-<nnn>` field (:109).** It pairs as RT1(a) does (:47). reviews/S-033/_owner-answers.md:9 holds "On Q-024 (questions/Q-024-approve-s033.md)…" on an `Answer:` line. sample.jsonl:41 already gives `question_ids_in_owner_word_lines: ["Q-024"]`, but gives the question file's `question_label` as a hash (609e0ca6). So the Orchestrator's re-code must write the id in clear. The field can be coded.
- **Step 6 (a) to (h) (:112), each checked:**
  - (c) S-022's answer file :3 says its words were "first written down in the spec draft", and Model-Lab P-001-open-unknowns.md:8 says "Recorded from the previous session's handoff".
  - (b) P-001-trial-view-notes-2.md :32 and :43 cover notes 3 to 9.
  - (e) The count of six is right: sample.jsonl:68 has commits at 16:42:38, four at 16:42:39 and one at 16:42:40.
  - (d) The S-023 and S-024 copies were first added at 01:16:39 and 01:16:42.
  - (f) 7234f058 has 4 form-(3) lines.
  - (g) questions-and-order.md:17-28 holds eight answers, but see finding 1.
- **Open question 15 (:258).** All of its stated facts hold:
  - The first answer file is ad6df430 (S-022), first added at 2026-10-11 01:00:35.
  - S-020 :252 and S-022 :127 have "Owner's rulings" sections.
  - S-017 and S-021 have none.
- **Open question 16 (:259).** It is a fair owner question: options, costs and a recommendation, with no rule changed.
  - Option (b) would need a new extract field (which naming word sits on the line above each form-(2) line).
  - Under (b), notes 15 to 18 would stay under RT1(a), because their heading line (:74) names "answers" as well as "Notes". If the owner picks (b), the card might say so.

**5. Item 4, the two-form matching order and the changed-ruling case (:49).**
- Both can be coded, and both match the extract README's fields. The README already matched form (1) by its first label, and forms (2) and (3) together.
- Neither changes a sampled count. The extract that memo 3 coded already applied these readings. Its matched-away pairs are Service-Desk #26 (:35) and Personal-Org-Operating-Model #27 (two commits, :52) and #25 (:57), and none changes a yes-or-no.

**6. Self-implication (D-050).**
- This check re-checks the fix that the Critic's own brief 304 finding 1 proposed.
- Brief 304's finding 8(e) said "eight" of #78's commits fall in 16:42:38 to 16:42:40. The extract shows six, and the spec's six is right. Triage should count that as a miss in my role's earlier check.

## Six-part contract
- **Changed:** nothing. I have no write tool.
- **Why:** brief 306, the re-check of brief 305's K1 fix for S-002 (P-002, M8).
- **Verified:** with Read, Grep and Glob only.
  - Model-Lab: specs/S-002.md in full; docs/briefs/305 and 306; reviews/Q-018-recode-2/_critic-verbatim.md; reviews/Q-018-rules-2/_critic-verbatim.md; research/Q-018-extract/README.md, sample.json, sample.jsonl (file classes, k2_roles, window commits, answer-record labels), Service-Desk.M.jsonl and Personal-Org-Operating-Model.M.jsonl (owner-file labels, web-editor commits), extract.py (K1); research/Q-017-memo.md, the path rules.
  - Clones: Service-Desk docs/design/references/ (all owner-* files, README.md, comments-2026-10.md), decisions/ file names, and P-001-trial-view-notes-2.md; Personal-Org-Operating-Model reviews/*/_owner-answer* (S-022, S-033), and specs' "Owner's rulings" sections; Model-Lab decisions/questions/P-001-open-unknowns.md.
- **Undone:**
  - I could not read the diff a1d9f1f..c866461 (no git), so I checked the text as it stands at the commit I was given.
  - Commit hashes and times come from the extract, not from git.
  - research/Q-018-memo-3.md and questions/P-002-unasked-notes.md were not opened.
  - The Definer's own table is the writer's summary, which my pack keeps out. My piece and kind results are worked out independently.
  - comments-2026-10.md and references/README.md were not traced across the whole of frame M (labels only, no hashing).
- **Needed outside my surface:**
  - Definer: finding 1, plus optional wording in 6(a).
  - Orchestrator: the K1 re-code of the drawn sample, and `question_label` in clear for Personal-Org-Operating-Model question files.
  - Triage: finding 6.
- **Open questions:** none new. Open question 16 is put correctly to the owner.

Key paths:
- /home/user/Model-Lab/specs/S-002.md
- /home/user/Model-Lab/research/Q-018-extract/sample.jsonl
- /home/user/Model-Lab/research/Q-018-extract/Service-Desk.M.jsonl
- /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/hc/Service-Desk/docs/design/references/owner-github-plan-2026-10-18.md
- /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/hc/Service-Desk/docs/design/references/comments-2026-10.md
