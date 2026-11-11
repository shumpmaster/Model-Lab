Verdict: FAIL

*The Critic on P-002's brief (docs/projects/P-002.md, Part 1) before the Design gate: round 1 (FAIL), brief 246; round 2 (FAIL), brief 247. Each round a fresh session on a different model from the plan's writer, started by the Chief of Staff (session_01QBwHGJRsdA6DND96m5Z9xE), 2026-11-11, on fixed copies Model-Lab@d96a853 (round 1) and Model-Lab@6397b75 (round 2). Round 2's second-level headings are recorded one level lower, so they nest under their round. Recorded verbatim by the Orchestrator from the helper's return; the round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's.*

## Round 1 (brief 246)

The round's verdict was FAIL.

I read P-002.md in full and opened the records it cites for the new parts. These were the value-target, trial-gates, route, groundwork-shortlist and target rulings, the odds intake and its Reviewer record, Q-017 §1/§5, the role files, AGENTS.md, the archived v2.5.1 tier table, OPERATING_MODEL §3/§4, and docs/PROJECT.md. I ran nothing.

What holds up:
- Every Discovery-1 to 8 and Design-1 to 6 standard line is present, in the right form, with a plain why.
- M7 to M15 are each in the form, carry a why with no " · " inside, and read as achievements. Names are plain apart from the required (M#).
- The pieces of section 6 I was asked to check match the odds record and the Reviewer's findings:
  - "about 5 times in 10 (0.53 / 0.54)" is correct.
  - "0.093 to 0.104" matches the Reviewer's sweep.
- The route, "no data out", desk and Model-Lab-archive quotations match their records.
- Tier T1 and the "3+ concurrent agents" trigger match AGENTS.md and the v2.5.1 table.

Blocking

1. Section 4 (rows "Reading the feeds (M12)" and "Research on each lead") and section 8 (Terms, "Screener"). No role owns picking leads from the feeds and kicking off research.
   - Section 8 defines the Screener as "the role that reads a feed and picks leads". The roster in .claude/agents/ has no such role.
   - The Input reader only returns structured findings and "never writes files". The Researcher is blind to the plan and may not write the question it answers.
   - So the step the owner described as the core of the pipeline ("read by screeners … automated research prompts that get kicked off", groundwork-shortlist answer 2) has no owner. It also has no named writer of the neutral research question. Section 4 requires an owner for every deliverable.
   - Name which roster role (or the Chief of Staff) picks leads and files each research question, and who sets the reading schedule in motion.

2. Section 1 "Out" (the claim "this project changes nothing the prompt engine is testing or counting"), section 3 M14 and Dependencies, and section 8.
   - The plan guards only trials: "no trial runs on a kind while the prompt engine tests or counts that kind".
   - The prompt engine's V2 (docs/PROJECT.md line 109) counts the first 30 pieces of each kind "under the changed operating model, in any project", and Launch-4 requires that count to be running.
   - M14 puts approved methods into that same operating model, and M11, M9 and M10 add pieces in Model-Lab, which that count covers. Neither is guarded or even named. This contradicts the Out claim.
   - The Dependencies sentence also states the trial rule as settled, although section 6 lists it as only proposed.
   - Needed: a constraint pair for "entering a method into the model" and "this project's own pieces" against the prompt engine's counting window, or an honest scoping of the Out claim. This is the judged item 4.

Non-blocking

3. Section 3, Dependencies, first citation to value-target "How it is carried out". That record says only that the log is specced in Design and built after the gate, and that no trial runs before then. It does not hold "owner has set the spend and time ceilings" or "M11's starting count is on record". Those are the Chief of Staff's own conditions and should be marked so. Section 6 "Cost to the owner's time" and section 5 have the same attribution issue: "no trial runs before then" sits next to an answer-8 citation that says only "Set at Design gate".

4. Section 1 "Out", "Any automatic change to the Service Desk or the operating model (the same record, answer 5)". Answer 5 concerns the desk only. The operating-model half rests on trial-gates ("through the model's own change process"). Cite both.

5. Section 6, last bullet, and section 4 row 1. The independent run of the odds is listed under "Proposed for the Design gate, not yet ruled".
   - The owner ordered it (intake/P-002-owner-instruction-2026-11-11.md). It has happened: reviews/P-002-value-target-odds/reviewer.md is a round 1 FAIL.
   - Its two findings are corrected only in the intake item, with the script left unchanged. The plan says nothing of this. Say M7 is not yet reached and what remains.
   - The bullet also cites the question files "as filed, in PRs #90 and #91", which are not in the repository copy.

6. Section 8 "Line": "here 1 in 10, the chance that a method doing nothing would pass". The Reviewer's finding 4 says this must read "about 1 in 10". One look gives 0.06 to 0.08, and two looks give 0.093 to 0.104 at the shares shown. Section 6 itself says "about" and "0.093 to 0.104". The sweep also shows 0.041 at a 5% start, so "from 0.093 to 0.104" is the range at the shares examined, not at every start.

7. Section 4, row "counting rules … hand check". Both roles are stretched.
   - The Researcher (tools Read, Grep, Glob, WebSearch, WebFetch; blind to the plan and rulings) is given a hand check of past pieces in three repositories against rules that come from the owner's ruling.
   - The Source checker "opens every cited source". It does not "re-derive" counts. Q-017 managed this only through extracts and Critic checks (P-002-q017-decide and P-002-q017-stop). State the extract route and who re-derives.
   - Related: the Reviewer, who "never changes files", is asked to check outside code "in a place that holds no project data". That place is not yet defined, though U4 and M10 own it.

8. Section 1 (areas) cites research/Q-015-memo.md as a source. The owner's ruling P-002-research-stop-3 set the Q-015 and Q-016 memos aside and kept only their filed library entries. Cite the entries, or say the memo is used only for its list of areas. Section 7 also omits the Q-017 rulings P-002-q017-next, P-002-q017-decide and P-002-q017-stop from "the owner's ruling on what is relied on".

9. Section 7 U3. The Critic's earlier table, from the Q-017 §1 counts, puts research pull requests in all three repositories at 55 over about seven weeks. That is fewer than one 30-and-30 trial. The brief shows no sign of that pace, only "unknown". Give the pace so the owner can weigh the 12-month target and the "five trials" stop rule at the gate. The reason is that M13's "up to the number the stop rule sets" rests on rules not yet ruled.

10. M8's why ("an earlier count built without a sample check miscounted") cites no record. It is supportable from P-002-q017-next (the merge-coding fix) but should say so.

11. Plainness on a phone:
    - Section 2's new chain and section 3 lean on codes in prose ("pre-mortem R6, R8; M10, M12").
    - Section 5's four-column table and the dense section 8 bullets will be hard to read on a small screen.
    - M10's done-when ("are written in the frozen plan") reads close to a task. Say what is then true, for example that the owner can see which feeds are read and how often.

Other checks, no finding:
- Section 5 spend wording and the P-001 ceiling match.
- DATA-CLASSES is left unchanged, as stated.
- M14's named roles (orchestrator, tools-builder) match AGENTS.md line 15.
- Section 9 "The owner is the user." agrees with the rest of the brief.

Files read: /home/user/ml-fixed-245/docs/projects/P-002.md and the records named above, all under /home/user/ml-fixed-245/.

## Round 2 (brief 247)

The round's verdict was FAIL.

Round 2 on docs/projects/P-002.md Part 1, read cold and compared with the records it cites. I ran nothing. Two round 1 findings are only partly answered (7 and 11). One new load-bearing unknown is missing (finding 1). The remaining findings are non-blocking.

I could not check three things. The question files at commits 451dd08 and daf76d7 are not in this copy. The intake/P-002-owner-instruction-2026-11-11.md and docs/LESSONS.md LL-54 citations I checked only lightly. I did not read section 6's V1 line or the pre-mortem beyond agreement checks.

### Round 1 findings, one by one

1. Who picks leads and writes the research question: answered. Section 4 and section 8 "Screener" now give the Chief of Staff the picking and the question, and the Input reader the reading. This leaves a new non-blocking mismatch (finding 4).
2. Guards on methods entering the operating model and on this project's own pieces: answered. Section 8 has the V2 pair and the "own pieces" pair, and the Dependencies sentence now says "Proposed for the owner to rule". Section 1 "Out" now says "designed so that" and points to the guards in section 8. Those guards are still proposals. The plan says so, so this is not a failure.
3. Chief of Staff conditions cited to a record that does not hold them: answered. Dependencies says "as the Chief of Staff's own design". Sections 5 and 6 now cite "no trial before the gate" and answer 8 separately.
4. Operating-model half of the desk citation: answered. "Out" cites trial-gates "How it is carried out" for the model.
5. State of the independent odds run: answered. The M7 row says "not yet reached" and names the two failed rounds. The Reviewer record (reviews/P-002-value-target-odds/reviewer.md) agrees. Section 6 now says "up to about 0.106 at starting shares near 4 in 10 and 6 in 10", which matches the Reviewer's round 2 sweep (0.1062 maximum). The question-file commit hashes are unchecked (see "I could not check" above).
6. "about 1 in 10": answered, in section 6 and in the section 8 "Line" term.
7. Roles for the hand check and the outside-code check: partly answered. The extract route is now stated (Orchestrator extract, Researcher memo, Critic checks edge cases), citing P-002-q017-stop, -decide and -next. The place where outside code is checked is flagged as unset, with M10 and U4 owning it. The Researcher and Reviewer role files still sit awkwardly with these tasks (see finding 4). I count this as answered enough.
8. Q-015 memo citation and missing Q-017 rulings: answered. Section 1 cites research/Q-015.md, which exists, says the memo is set aside, and cites P-002-research-stop-3. Section 7 lists the Q-017 rulings.
9. Pace for the 12-month target: answered. U3's figures (124, 150, 55 over about seven weeks) match Q-017 §1: 90+8+26, 100+19+31 and 29+21+5. The memo marks "supported in part", and the plan says so. Finding 3 below adds a caveat.
10. M8's why had no record: answered. LL-73, P-002-q017-next and Q-017 §5 are cited in "Records behind the whys". LL-73's title matches.
11. Plainness: partly answered. Section 5 is now a list, and M10's done-when now says what the owner can see. Codes remain in prose (see finding 8).

### Milestones (judgement 1)

- All 14 standard lines (Discovery-1 to 8 and Design-1 to 6) are present, in form, taken on, with a plain why and no " · " inside any why.
- M7 to M15 each have the name, done when, phase and why form. Each reads as an achievement, not a task. Names carry only the required (M#) tag.
- M7's why holds: it cites LL-54, and the independent run is the owner's order.
- M8's why holds, per the answer to round 1 finding 10.
- M9's why is stronger than its record (finding 5).
- M10, M12 and M13 whys hold against Q-012-15, Q-011-10 and Q-014-18.
- Discovery-8's why only restates the milestone ("the owner rules the Design gate on a checked brief"). It does not say why the project needs it, but it is acceptable. Non-blocking.

### Findings

1. **BLOCKING. Section 7 unknowns and section 2 chain link 4. A load-bearing unknown is left out: can a method be switched on and off piece by piece?**
   - The whole trial design rests on shuffled assignment of individual pieces to "the method or not".
   - The Critic's earlier record (reviews/P-002-value-target/critic.md, line 209) said that a method that changes rules or session structure cannot be toggled per piece. It also said that a method which leaks to the "without" pieces shrinks the difference and reads as "not shown". The plan answers this nowhere.
   - Section 6 only proposes "one method per kind of work at a time". R14 covers live work and model changes, not toggling.
   - Definition of ready item 7 and the Design gate need each unknown named, with a test and a fallback.
   - Needed: an unknown such as U5 with a test, for example a design check in M9 that each method can be applied piece by piece, and a fallback, for example only trial methods that can be switched per piece.

2. **Non-blocking. Section 4, row "Reading the feeds (M12)".**
   - The Input reader's role file gives its trigger as "A Researcher request for outside material" and its handoff as "Structured findings to the Researcher". The plan has it read feeds on a schedule and return to the Chief of Staff.
   - Say that this is a project-specific brief for the role.
   - The row "Starting each reading round on its schedule" names the Chief of Staff. Nothing in the plan says what actually starts a round on a schedule. Dispatch is by the Orchestrator (CLAUDE.md), and no scheduler is named.
   - The plan never says that web searches and fetches are themselves outbound. The Input reader and Researcher hold WebSearch and WebFetch, and a query can carry project words. This pair is missing from section 8: "no data out" against reading outside text by search. State that queries and fetches carry no project data.

3. **Non-blocking. Section 7 U3, "fewer than one trial needs".**
   - The sentence follows 124, 150 and 55 and reads as if all three are short. Only research (55) is short of 60. Built (124) and plans (150) exceed 60.
   - Q-017's by-kind table counts a pull request under every kind it touches. Single-kind pull requests are far fewer: built 1, 0, 0; plans 7, 0, 1; research 1, 0, 0.
   - Section 8 lets a piece touch several kinds. A trial needs "pieces of one kind", and the plan does not say how a multi-kind piece is classed (M8 or M9 should).
   - The pace is therefore an upper bound. Say so.

4. **Non-blocking. Section 4, rows "Research on each lead" and "Checking outside code".**
   - The Researcher is blind to the plan and rulings. Make sure the hand-check and lead questions arrive as questions, not as plan text.
   - The Reviewer "never changes files". Whoever builds the sandbox for outside code is unnamed; M10 and U4 own that.

5. **Non-blocking. Section 6 "How a method is tried and kept" and "Cost to the owner's time", M9's why, and the section 4 "short reads" row.**
   - "30 pieces each way", "5 short reads per look" and "the owner's design, P-002-trial-gates.md" are not in the cited record. The decision file holds only "two looks planned per trial" and the approvals. The question files that held the sizes are removed.
   - M9's why says "the owner ruled ... 30 pieces each way". That is stronger than its record. The odds intake (line 58) attributes these to "the card's part 3, option A".
   - Cite the commit or intake that holds them, or mark them as the card's terms.

6. **Non-blocking. Section 5 data classes.**
   - governance/DATA-CLASSES.md is an unfilled template with different class names (Public, Internal code, Secrets, Personal, Regulated).
   - The plan's five classes do not map onto them. "The AI service the sessions already run on" is not named.
   - Say that the list is the project's own pending the file, and that the file's vendor row is still to be filled for T1.

7. **Non-blocking. Section 6 last bullet.** It cites question files "at commit 451dd08 and daf76d7" that I could not open. Fine if recorded, but "the rest come from the two questions as filed" gives the owner nothing to check at a glance.

8. **Non-blocking. Plainness on a phone.**
   - Codes remain in prose: "pre-mortem R6, R8; M10, M12" in section 2's chain, "(M12)" in section 4, and "R12" and "Q-" tags throughout section 2.
   - Section 8's constraint bullets are dense, with 11 pairs and many nested citations.
   - Section 2's chain would read better if the codes were cut or kept to the end of each link.

### Judgements 3 to 5

- **Scope, owners, limits and terms agree with each other and with the rulings.**
  - The route ruling matches (no new groundwork request during Discovery).
  - The prompt engine's V2 (docs/PROJECT.md line 109) is now paired with M14 in section 8.
  - The spend wording matches P-001-spend-ceiling, with the owner's override in place.
  - "No data out" is kept. The owner's time ceiling is clearly for the gate. The "Proposed" list is not presented as ruled.
- **The owners table gives each role work its role file allows**, apart from findings 2 and 4.
- **Section 9** ("The owner is the user.") agrees with the rest of the brief.

Files read: /home/user/ml-fixed-247/docs/projects/P-002.md, reviews/P-002-brief/critic.md, reviews/P-002-value-target-odds/reviewer.md, decisions/questions/P-002-value-target.md, -trial-gates.md, -route.md, -research-stop-3.md, -q017-next.md and -q017-decide.md, decisions/questions/P-001-spend-ceiling.md, research/Q-017-memo.md, docs/PROJECT.md, governance/DATA-CLASSES.md, AGENTS.md, .claude/agents/input-reader.md, reviewer.md and researcher.md, and /home/user/Personal-Org-Operating-Model/OPERATING_MODEL.md §4.
