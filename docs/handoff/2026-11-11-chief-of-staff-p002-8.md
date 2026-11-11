# Handoff — the screening (P-002), 11 November 2026, Design started

*Written by the Chief of Staff (session_01QBwHGN6YeYid8ERiP8HY5Z). It follows docs/handoff/2026-11-11-chief-of-staff-p002-7.md.*

## What this means for you

The milestone for the re-run sums is still not marked reached: the automatic checks cannot see a Design gate ruled in conversation, and they want a Reviewer's record of the pull request that held its work, which it never had (LL-82). Everything else in your ruling is now in the plan, waiting on your merge of pull request 97. Design has started: the Definer has written a first draft of the counting rules, the trial design and the sources, with both versions of the line at two looks worked out. That draft is not yet checked, and it raises six smaller questions for you, which come later on cards. Nothing is irreversible.

## Where it stands
- **PR #97** (branch claude/p002-design-gate-ruling-sld3g4): the brief's sections 3 to 8 in line with decisions/questions/P-002-design-gate.md; the Critic on it FAIL then PASS (reviews/P-002-design-gate-brief/critic.md); M7's reworded line PASS (reviews/P-002-m7-line/critic.md); LL-82; briefs 257 to 259; session lines. Waits on the owner's merge.
- **M7's line** is unchanged. The Critic-passed text, with ` · sprints: PR #93 · reached: 2026-11-11`, is quoted in reviews/P-002-m7-line/critic.md. It fails `v3_checks milestones` (no status record shows the project approved; LL-43) and `v3_checks trace` (no reviews/93/reviewer.md). Asked of the owner: whether a Reviewer should review #93 after merge so the sprint can land.
- **The Definer's draft plan** (brief 258): commit bf54505 on the local branch build/definer/p002-design, worktree /home/user/wt/ml-definer-258, from 494311d. specs/S-002.md (M8, M9 summary, M10; AC1 to AC21; J1 to J9), experiments/E-004.md (the fixed trial plan), experiments/E-004/line.py and line-output.txt. Surface guard and check_all pass. Not pushed: this environment pushes one branch, and #97 is open on it. If the container is gone, re-dispatch brief 258 from its start commit.

## Next, in order
1. After #97 merges: restart the push branch from main, merge build/definer/p002-design with `--no-ff` (a draft plan, R0), and open its pull request.
2. P18: a Reviewer runs experiments/E-004/line.py independently (both versions, every figure in line-output.txt, and a second way), recorded in reviews/<name>/reviewer.md. Then the owner's card on the line at two looks, filed first as questions/P-002-two-look-line.md, with both tables from line-output.txt and no recommendation beyond what the checked figures show; the Critic checks the card first.
3. M8's hand check by the route the owner ruled (S-002, "The hand check"): the Orchestrator builds the extract (no free text) to S-002's sample; the Researcher applies the rules as a memo; the Critic checks every edge case.
4. The Critic's plan review of S-002 and E-004 (reads docs/projects/P-002.md, L-0008). Then the S-002 open questions 2 to 7 to the owner (T7 unasked instructions, T5 gate rulings as touches, U3's 26-week mark, feeds F1 to F4 and the 14-day rhythm, the Reviewer reading outside code in the empty environment, trial pieces kept out of the prompt engine's paired test), on cards that each show the item, its origin, and a gain and cost per option (LL-80).
5. The Critic's non-blocking leftovers in the brief (R7, R18, R3, R9, R15) at the plan's next change.

## Standing conditions (unchanged)
- Do not disturb the prompt engine's running work (PR #87 is its own). Brief records here keep model names out, so this project's plans are not eligible pieces for its fair test.
- The owner's private details are never written to any file or sent out.
- Give every checker the cards as put as files: `git show 964da47:questions/P-002-value-target.md`, `git show 3ae1268:questions/P-002-trial-gates.md` (copies at /home/user/ml-cards/ in this container).

## Mechanics learned this session
- The PR body's first paragraph must be 15 to 150 words; test with `governance_checks.py pr-body --event <json>` before opening.
- A reached mark or a sprint on a conversation-run project fails the checks today (LL-82); test a milestone change in a separate worktree first (LL-81).

## Token checkpoint
Three helpers reported 422,237 tokens: the Critic 67,068 and 60,658, the Definer 294,511 (sessions/chief-of-staff/session_01QBwHGN6YeYid8ERiP8HY5Z.jsonl). The session's own usage is not read here.
