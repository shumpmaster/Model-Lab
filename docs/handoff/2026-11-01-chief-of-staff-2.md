# Handoff — the prompt engine (P-001), second session of 1 November 2026

*Written by the Chief of Staff (session_01QBwHGHrHnEvMNYgKDoaH8w) at a natural stopping point, so a fresh session can carry on without this conversation. It follows docs/handoff/2026-11-01-chief-of-staff.md.*

## Where it stands
- **Phase:** Discovery, first run.
- **Done this session:**
  - The checked facts are filed: 88 entries in the portfolio library (portfolio PR #3, waiting for the owner's merge; library/README.md indexes them). Held back: F-Q004-5 and everything the confirmations hold.
  - **Success defined (Discovery-2):** the owner ruled option A (decisions/questions/P-001-value-target.md, in PR #10): first-time pass rate up 20 points; V1 in the paired test, V2 over the first 30 real pieces of each kind; no calendar date; the miss and stop rule adopted with it. Written into docs/PROJECT.md section 6. Critic: reviews/P-001-value-target/critic.md (PASS at round 4).
  - **The right problem chosen (Discovery-4)** and **the risks known (Discovery-6):** problem statement in section 2, pre-mortem R1–R9 in section 7. Critic: reviews/P-001-problem-premortem/critic.md (PASS at round 3).
  - **The rest of the brief** (sections 1, 2 chain, 4, 5, 7 groundwork and unknowns U1–U5, 8, 9 "The owner is the user.") and **Part 2, the intent.** Critic: reviews/P-001-brief/critic.md (PASS at round 2). M2's done-when reworded (decisions/questions/P-001-milestones-m2-runs-critic.md).
  - **The owner's unasked ruling:** the desk notifies the owner when a conversation must move to a new session, in the model and the desk (decisions/questions/P-001-session-move-notice.md; lessons log LL-25).
  - Lessons log LL-25 to LL-28.
  - Research question Q-008 (the count of past rework, M1) drafted and passed by the Critic at round 2 (reviews/Q-008/critic.md); not yet dispatched.
- **Branches** (all pushed): cos/p001-discovery-2 (the brief, two decision records), orch/p001-discovery-2 (briefs 06–10, review records, lessons, Q-008, this handoff), cos/session-01QBwHGHrHnEvMNYgKDoaH8w (session lines). Their pull requests are listed in the owner's closing message.

## Next, in order
1. **The count of past rework (M1, closes U1 and U5).** Dispatch a Researcher on it (records only, no web: no network check needed, LL-22), then a Source checker on a different model. Its figures replace section 6's starting figures, and the real-use odds are restated. If it shows the instructions are not a meaningful cause of avoidable rework for any kind, the stop rule sends the project to the owner.
2. **Questions for the Design gate** (filed first, Critic-checked on a different model):
   - the spend ceiling (section 5 carries the Chief of Staff's proposal);
   - accepting U2, U3 and U4 as open into Design and Build (definition of ready item 7);
   - whether researchers may read the web directly (LL-07);
   - who approves role-file changes, and whether instructions are re-checked on model changes (withdrawn earlier, to come with evidence);
   - the library's open choices from the Source checker: shelf lives (OPERATING_MODEL §6 [open]), mapping the memos' letter grades to strong/moderate/weak (Q-007's "A" means opened, not strong), and fields the pattern form lacks;
   - the desk follow-ups (LL-21; deploysNeedOwner on one project only; the "default branch not found" wording, Service-Desk reviews/263) and the route for the desk's part of the session-move notice (LL-25; the desk is graduated, so the owner approves the route); and the desk showing the portfolio's pull requests that wait on the owner, and counting library patterns beside facts (LL-28; the owner agreed on 2026-11-01 to add it to these follow-ups).
3. **The brief's last pieces and the definition-of-ready check:** the Discovery-1 to -8 and Design lines in section 3 stand; after M1, the Critic checks the whole brief against the definition of ready, then the Design gate case (docs/gates/, the gate form) goes to the owner.
4. **Before the second idea starts:** the tools assume one project per repository (LL-16); bring the owner options.

## Open at handoff
- PR #10 (the value-target answer) had all checks green and was waiting for the asks-merge workflow.
- Portfolio PR #3 (the library) waits for the owner: the portfolio repository has no asks-merge workflow.

## Token checkpoint
Helpers this session used about 499,000 tokens in all; the session lines for helpers sent back for further rounds hold running totals, not each round's use (lessons log LL-34). This session's own tokens and the owner's remaining plan allowance cannot be read; the plan's weekly limit allowed use at the time of writing.

## Working rules carried forward
Those in the first handoff, plus: run `governance_checks.py pr-body` on a drafted body before opening a pull request (LL-27); before citing research, look up the entry's filing status in the confirmation or the library (LL-26).

## Update at the second stopping point (late on 1 November)
- **Done since:** the count of past rework (Q-008, M1) researched and source-checked (two rounds), its nine entries filed in the portfolio library; the owner's four Design-gate rulings recorded (spend: the existing plan unless the owner overrides; only the Input reader reads the web; the desk gaps, plus the milestone screen, into one desk item after the Design gate; fixed library shelf lives and labels); the count's results written into the brief (section 6 starting figures, section 7 U1 and U5); the owner's ruling after the count: **A, go on now** (decisions/questions/P-001-after-the-count.md, once recorded); the pull-request briefing idea logged with its kick-off (portfolio ideas/KICKOFF-pr-briefing.md), to run in its own session; lessons LL-28 to LL-36.
- **Next, in order:**
  1. Record the owner's after-count answer (the text is ready in the session; PR #20 files the question and must merge first).
  2. M1's "done when" says "each kind has a stated cause", which the records cannot give; reword it (Critic check, no owner ruling) or put it to the owner as not reachable as written, then ask the owner to accept M1.
  3. Ask the owner to accept U2, U3 and U4 as open into Design (definition of ready item 7).
  4. The whole-brief definition-of-ready check by the Critic, then the Design gate case (docs/gates/, gate form).
  5. Carry the two rule-change rulings (researchers and the web; library shelf lives and labels) and LL-01 to LL-36 into the operating model at the end of the cycle (M5, M6).
  6. Before the second idea starts: the tools assume one project per repository (LL-16).
- **Every pull request here needs the owner's merge:** Model-Lab has no asks-merge grant (LL-33).

## Update at the third stopping point (just after midnight, 2 November)
- **Done since:** the owner's after-count ruling recorded (PR #24, A, go on now); M1 renamed and reworded to what the count delivered ("How often work is sent back, and what the records show of why, is known"), Critic-passed (reviews/P-001-open-unknowns/critic.md); the open-unknowns question filed (PR #25) and **answered by the owner in the session on 2026-11-02: "A: accept all three (Recommended)"**; lessons LL-37 (a session's own usage can be read from the session's status: context, tokens and estimated cost).
- **Next, in order:**
  1. Once PR #25 is merged, record the owner's answer in decisions/questions/P-001-open-unknowns.md (first line `Ruling: A — U2, U3 and U4 stay open into Design and Build, with the tests and fallbacks in docs/PROJECT.md section 7`; the owner's words: the owner chose "A: accept all three (Recommended)"), deleting the question file in the same pull request; then update section 7's "Draft." sentence to cite the ruling.
  2. Ask the owner to accept M1 as reached (the count is done and source-checked), recorded with an `Owner-Ruling:` trailer.
  3. The Critic's definition-of-ready check of the whole brief (Part 1 and Part 2), on a different model.
  4. The Design gate case (docs/gates/, the gate form), with the Critic's view beside it.
  5. Carry the two rule-change rulings and LL-01 to LL-37 into the operating model at the end of the cycle (M5, M6); before the second idea, LL-16.
- **Token checkpoint:** helpers about 1.54 million tokens over the session; the session itself, by its own status, about 600,000 tokens of context in use and about $50 estimated cost at the last reading.
- **Every pull request here needs the owner's merge** (no asks-merge grant, LL-33).

## Update by the next session (session_01QBwHGN4kVVA3rfHx2b4FsF, 2 November)
- **Done:** the third stopping point's records and session lines carried in (they were pushed with no pull request, LL-38); the owner's open-unknowns answer recorded (decisions/questions/P-001-open-unknowns.md) and section 7 cites it; the Critic's definition-of-ready check of the whole brief, FAIL at round 1 (outside judges against the spend ceiling; a portfolio-wide preference in Part 2), PASS at round 2 (reviews/P-001-ready/critic.md); the Design gate case in three rounds (docs/gates/P-001/design-gate-1-case.md to -3-case.md; a case is never changed after the Critic has read it, so each round is a new number), each with the gate Critic's view (reviews/P-001/_design-gate-1-critic.md to -3-critic.md), all recommending proceed; case 3 went to the owner at the three-round limit with its view's non-blocking points open (M1 drawn as done before the owner's ruling, the M1 sprint reason and one citation, the form's other standard visuals), for the owner to read beside it; the case-3 Critic disclosed it opened the case-2 view, outside its pack; two questions filed, passed by the Critic at round 2 (reviews/P-001-gate-questions/critic.md): the Design gate (questions/P-001-design-gate.md) and accepting M1 (questions/P-001-accept-m1.md); lessons LL-38 to LL-41.
- **Changed from the last list:** asking the owner to accept M1 moved to the Design gate, because a milestone's reached mark may be added only once the milestones are approved there (OPERATING_MODEL.md §3).
- **Next, in order:**
  1. Once the owner answers and the question files are on the default branch: record both answers in decisions/questions/ (deleting the question files). If the gate is `proceed`, add ` · reached: <date>` to M1 in a commit whose `Owner-Ruling:` trailer names decisions/questions/P-001-accept-m1.md (first line `Ruling: A` with a `Question: questions/P-001-accept-m1.md` line, or `Ruling: accept M1`), and confirm Part 2, the intent, as confirmed by the ruling.
  2. Design starts: the replay check (U2) and the judge-consistency check (U3), within 40 of the 100 runs; then the Definer writes the fair test (M2) for the Critic's plan review. Check the environment can do what Design needs first (LL-22).
  3. Renumber the briefing session's LL-36 when its branch lands (LL-39).
  4. At the end of the cycle: the two rule-change rulings and LL-01 to LL-41 into the operating model (M5, M6); before the second idea, LL-16.
- **Every pull request here needs the owner's merge** (no asks-merge grant, LL-33). This session pushes only its one branch, claude/chief-of-staff-discovery-064xiz, as the environment allows.
- **After the owner's answers (2 November):** the owner ruled the Design gate "A: proceed (Recommended)" and accepted M1, "A: accept M1 (Recommended)"; both recorded in decisions/questions/. M1's reached mark could not be added: the milestones check reads approval only from the pipeline's status record, which this project lacks (LL-43). The briefing session's lesson (PR #30) landed as LL-42 through this session's branch.
- **Next:** (1) put LL-43 to the owner with LL-35 and LL-40 (how a conversation-run project's gate ruling reaches the status record), then add M1's mark; (2) Design: the environment check (LL-22), then the replay (U2) and judge-consistency (U3) checks within 40 of the 100 runs, then the Definer's fair test (M2).
