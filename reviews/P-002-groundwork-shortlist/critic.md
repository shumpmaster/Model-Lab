Verdict: PASS

*The Critic on questions/P-002-groundwork-shortlist.md, the owner shortlist of the Q-009 groundwork map: round 1 (FAIL), round 2 (FAIL), round 3 (PASS); briefs 143 to 145. Each round a fresh session on a different model from the card's writer, started by the Chief of Staff (session_01QBwHGNSLmSrYQgS6BPjV8p), 2026-11-08. Recorded verbatim by the Orchestrator from each helper's return; each round's own verdict line is recorded as "The round's verdict was …" (LL-68). After round 3, its finding 1 was applied ("already under way, measures … and aims to improve them").*

## Round 1

The round's verdict was FAIL.

I opened every Context source I was allowed to. These are the map (Q-009-memo.md, plus Q-009-input-1.md "Area 1 gaps"), OPERATING_MODEL §2, §4 "Groundwork research" (line 196) and §5, AGENTS.md §5, the card template, and portfolio library facts Q-007-F08 and Q-007-F09. I did not read docs/projects/ or decisions/, so I cannot verify the "Milestone: Discovery-3" line or the name "prompt engine" (finding 9).

The eight questions keep the map's meaning, with two exceptions: question 6 (finding 3) and the unexplained naming in question 7 (finding 9). Context lines 2, 4 (the injection half), 5 and 6 are accurate. The injection half of line 4 matches F08 and F09, and the "about ten minutes / verbatim / added to intent" line matches line 196. Line 3 is accurate but understates its own weakness (finding 4).

1. **Question 1, "Fact beside it" (line 9). BLOCKING.**
   - What is wrong: The card gives "no source measures what an organisation loses by not screening". That is true (map A3; input-1 Area 1 gaps), but it is the only fact offered. The map is equally unmeasured on the cost of adopting a bad practice (A4: "unknown here"; 40.2% of tested medical practices were ineffective). It also holds a fact pointing the other way: vendor model IDs are retired about 12–14 months after the snapshot (A2). A lone "nobody has measured the cost of skipping" reads as a nudge toward B ("rely on what already happens"), though the line is framed as neutral.
   - Why it matters: This is the first question, and it anchors the rest.
   - Fix direction (not done here): Give balanced facts or none.

2. **Question 2, "Fact beside it" (line 10). BLOCKING.**
   - What is wrong: "in medicine, a typical review needed updating after a few years; in AI tooling, findings changed within a year" is stronger than the records.
   - Medical side: The 3.3 years is Cochrane pregnancy reviews' median to first update (F5-6). The 5.5 years is search-only (F5-5/F13-5), so the Researcher never opened it. AHRQ says 5.8 years for half of 17 guidelines. "Typical" is not supported.
   - AI side: "Findings changed within a year" rests on one Google-staked DORA sign flip (F5-7, [B]) and a few other [B] items. The map itself says E1 is "unknown (a half-life for practice findings)". The card's own Context line 25 is more careful ("an industry finding... changed sign within a year; not yet source-checked"). The caveat is missing where the owner actually reads it, beside the question.
   - Lean: A short AI shelf life pushes toward "B. On a schedule".
   - Why it matters: Unverified, stake-bearing claims are presented as settled fact beside a preference question.
   - Fix direction (not done here): Restate with the same hedges as line 25, or drop it.

3. **Question 6, option C and its fact (lines 14 and 8). BLOCKING.**
   - Option C: "Yes, within the spend limit" is not in the map's question, which was about whether agents may try outside things at all and, if so, only ones that send no project data out. No spend limit exists yet (map J5: the charter field is a placeholder), and question 8 asks the owner to set one.
   - Ambiguity: Option C does not say whether project data may leave, so an owner could read it as permitting that. Options A, B and C mix two different axes (data and money).
   - Missing option: Nothing reads "yes, with no limit".
   - The fact: It is accurate (F08, F09: recognised, unsolved), but it is the only fact. It pushes toward A or B, and option B does not address planted instructions at all (that risk is about what the agent reads, not what leaves).
   - Missing context: The map notes SD's data-class table is empty (K6), so "sends none of your project data" cannot be checked today. The card does not say so.
   - Why it matters: The owner could pick an option that means something other than intended.

4. **Source-check status (card lines 9, 10, 14, 25).**
   - What is wrong: The map's [B] items are unconfirmed until the Source checker opens them. The "not yet source-checked" caveat appears only in Context line 25. The facts beside questions 1, 2 and 6 carry no such caveat.
   - Why it matters: The owner sees them as established. Non-blocking if finding 2 is fixed. It adds to it otherwise.
   - Severity: Non-blocking.

5. **D-019 and the template require gain, cost and reversibility for each option (lines 9–16).**
   - What is wrong: No option states what it costs or what it rules out. Example, question 5: the map (I1) says a graduated product gets a method change "only when the owner says something is wrong", with no automatic route. So option A has a cost and a mechanism that the owner is not told.
   - Why it matters: The owner cannot weigh options that have no consequences attached. This is acceptable only for pure preference questions, such as 3, 4 and 8.
   - Severity: Non-blocking, but questions 5, 6 and 7 should carry a consequence.

6. **"No recommendation" (line 17).**
   - Preference questions: It is acceptable under D-019 for the pure preference questions (3, 4, 8), and honest given that the model forbids guessing leanings.
   - Not pure preferences: Questions 6 (safety) and 7 (division of labour) are not pure preferences. The Chief of Staff could give a reasoned view or explain why it holds back.
   - Contradiction: "none for questions 1 to 8" sits beside a stated process recommendation ("answer what you can, say 'later'"), which is a recommendation, and nudges toward deferral.
   - Severity: Non-blocking.
   - Leak risk: "A 'later' answer becomes part of the research" (line 17) could pass the owner's leanings to the Researcher. Check this against §5 and D-055.
   - Severity of the leak risk: Non-blocking, but worth a decision.

7. **Only question 1 offers a "later" or "decide after research" choice (line 9).** The process recommendation tells the owner to say "later" to any question, but no other question lists it. Non-blocking.

8. **Plainness on a phone (lines 5, 9–16, and the title).**
   - Dense lines: Each question runs its choices and "(Fact beside it: ...)" together in one long line.
   - Undefined jargon: "screening", "groundwork map", "rule reviews", "prompt injection", "status page" and "this effort" are all used undefined. Question 8's "put into this" is ambiguous.
   - Unclear sentence: "screening outside AI practice" in the opening could be misread.
   - Codes in the WHY line: S-020 and D-055 sit mid-sentence rather than after the words they support.
   - Severity: Non-blocking. One option or fact per line, and one plain sentence saying what "screening" means, would fix most of it.

9. **Question 7 naming (line 15).** The card says "the separate prompt-engine effort"; the map says "the instruction-measuring effort" (the P-001 research). I could not verify "prompt engine" from my allowed records. If it is not the owner's own name for that effort, it will confuse. The card also does not mention the overlap the map found (H2: at least five overlapping findings), which is the reason for the question. Non-blocking, to verify.

10. **Question 4 (line 12).** Options A to C are not mutually exclusive ("daily use" and "others pay" can both hold). The map offered them as examples. As letters they force a single choice. Non-blocking: say "pick any".

11. **Line 18, "WHO HAS CHECKED IT".** It states the Critic has checked the card, but that is only true after this check passes. Non-blocking, since it is a wording point for the final version.

To clear the FAIL, fix findings 1, 2 and 3. The rest can ride along.

## Round 2

The round's verdict was FAIL.

I opened every Context source: the Operating Model §3 "Graduation and re-entry" (line 116), §4 "Groundwork research" (line 196) and §5 "Who sees what" (lines 241-246); Service-Desk governance/DATA-CLASSES.md; Q-009 memo K6, I1 and H2; the portfolio ideas/KICKOFF-cutting-edge.md; Model-Lab AGENTS.md §5; and questions/_TEMPLATE.md. The five Context bullets are all supported by their sources. The eight questions keep the map's meaning, and the money and data mix in question 6 is gone. The failures are in the consequence lines.

1. BLOCKING. Question 5, option A, "this adds a step each time", is not what the records say.
   - What the records say: a graduated product returns only when the owner raises something (Operating Model line 116, memo I1). That supports "today it takes method changes only when you raise one".
   - What they don't say: nothing records how option A would work, or that it adds a step. If a change reached the status page without the owner raising it, the owner would arguably have fewer steps, not more.
   - So "adds a step each time" is the card's own inference, stated as fact.
   - It also tilts the choice. Option A carries only a burden. Option B carries a comfort ("stays as built until you raise a change"). Option C carries nothing.
   - B's real downside, that the status page falls behind the method, is not stated.

2. BLOCKING. Question 5, "the status page has left the desk", is asserted as fact but is not supported by the card's own Context.
   - Memo I2 and B6 say the status page's graduation is "not established".
   - Only the portfolio kickoff says "the desk has graduated", and the card does not cite it.
   - Either cite the kickoff in Context or drop the claim.

3. BLOCKING. Question 6 has the same one-sided pattern.
   - Only option B has a consequence: "the list ... is still blank, so it would be filled in first." The consequence is accurate to DATA-CLASSES.md, which is all placeholders.
   - It is a cost on the middle option only, so it tilts the owner away from B.
   - Options A and C get no consequence. C ("no such limit") also runs into the blank table, and nothing says so.
   - "Would be filled in first" is an inference; the file only says it is required from T2.

4. BLOCKING. Question 7 has the same pattern.
   - Only option A has a consequence: "they would agree a boundary". Memo H2 supports the overlap.
   - It reads as extra work and nudges the owner toward B.
   - B and C get nothing, such as what it means for one effort to own every instruction change, or the memo's H3 and H4 risk that two efforts change the same instructions at once.
   - Questions 5, 6 and 7 together show the same defect as round 1: a consequence on one option only, and it is always a cost. Either give every option a matching, record-backed consequence or give none.

5. Non-blocking. Question 5, option C, "each with your approval", is the only option that mentions approval. That sounds like the safe choice. Rule changes already need the owner's approval (Operating Model line 66), so it is not distinctive.

6. Non-blocking. Question 7 uses "the prompt engine" and "this effort" without saying what they are, and the intro calls this work "the screening".
   - I confirmed in the kickoff that "prompt engine" is the owner's own name, so the term is fine.
   - "This effort" is ambiguous on a phone. "The screening" would be consistent.
   - The Context bullet on the overlap says "the prompt engine's research", while the memo says "instruction-measuring effort". The mapping to the kickoff is correct.

7. Non-blocking. The RECOMMENDATION line ends "What would change it: nothing", which reads oddly for a card with no recommendation.
   - DEFAULT "none" and TIMEOUT "none" depart from the template's letter and hours.
   - They are defensible for preference questions, and "no recommendation" is acceptable here.

8. Non-blocking. "WHO HAS CHECKED IT: the Critic checks this card before it is put" is a future-tense claim, not a record of a check. Update it once this review is recorded.
   - "made without your earlier words" is not stated in the memo. It is implied only by the Operating Model's Researcher rule (§5). Cite it, or soften it.

9. Passes:
   - Questions 1 to 4 are fair, with no consequence lines and balanced options. Adding "Both equally" in question 3 is fair.
   - Question 4's "pick any" fits the map's "for example" list.
   - Question 8 mirrors the map and offers "set it at the Design gate".
   - The opening paragraph is plain, says nothing is irreversible, and gives no paths.
   - The Milestone line and Context section are present, per Model-Lab AGENTS.md §5.

File reviewed: /home/user/Model-Lab/questions/P-002-groundwork-shortlist.md

## Round 3

The round's verdict was PASS.

I opened every Context source, and each fact on the card matches its record. I did not open Model-Lab docs/projects/ or decisions/.

Sources checked:
- Personal-Org-Operating-Model OPERATING_MODEL.md line 116 ("Graduation and re-entry"): "comes back only when the owner says something is wrong... no automated process brings it back". It matches the Context line and the Question 5 parenthetical.
- Line 196 ("Groundwork research"): "about ten minutes", "recorded verbatim and added to the intent". It matches.
- Lines 245-246 ("Who sees what"): the Researcher never sees the owner's leanings. It matches.
- Service-Desk governance/DATA-CLASSES.md: every row is a template placeholder. It matches the Context line and the Question 6 parenthetical.
- Q-009-memo.md: I1, K6 and H2 are quoted accurately. The eight questions keep the map's shortlist meaning. Option sets were added for 3 and 4, and a "Case by case" option was added for 5 and "Both equally" for 3. These are neutral and each invites the owner's own words.
- portfolio ideas/KICKOFF-cutting-edge.md and IDEAS.md: "prompt engine" is the owner's own name for the separate effort. Lines 37-38 of the kick-off name the overlap with it.
- Model-Lab AGENTS.md §5 and questions/_TEMPLATE.md: the card has the Milestone line, WHY, OPTIONS, RECOMMENDATION, RISK CLASS, DEFAULT and a Context section with sources.

Findings (all non-blocking):

1. Line 32, Question 7: "The prompt engine, already running, measures and improves the agents' written instructions". The records I could read show it measuring (the library entries from Q-002 to Q-008) and the owner's proposal to "improve the weak ones". They do not show improving as something already done. The sentence also gives "already running" as fact. The wording slightly overstates, but it applies to all three options and does not tilt them. A softer phrase such as "measures, and aims to improve" would be safer.

2. Line 28, Question 6, parenthetical "(Which of your data may go where is not yet written down.)". This is accurate and stated once. It does sit next to the options that restrict data, so a reader may feel nudged toward A or B. This is acceptable because it is a fact that bears on every option.

3. Line 24, Question 5, parenthetical "(Today a product in use takes a method change only when you raise one.)". The record says a graduated product returns only when the owner raises a problem. Applying that to "method change" is the map's own reading (I1), so it is supported. The Service Desk's graduation is confirmed in IDEAS.md line 25 (2026-11-01).

4. Line 38, WHO HAS CHECKED IT: "the Critic, three rounds (reviews/P-002-groundwork-shortlist/critic.md)". That file does not exist yet; only reviews/P-002-route and reviews/P-002-route-2 exist. The line is true only once this round's verdict is recorded there, so the Orchestrator must record it before the card is put to the owner.

5. Lines 40 and 37, DEFAULT and TIMEOUT. "none" and "no recommendation" depart from the template and from AGENTS.md §5, where reversible questions adopt the recommendation at timeout. The card explains why, so this is acceptable for preference questions. The owner has no default at timeout; the card says "unanswered, the research waits".

6. Lines 5-7, plainness on a phone. The opening paragraph is long and dense. It uses "the map of what an expert would ask about it ends in eight questions", "intent" and "Design gate" with little explanation. The questions themselves are short and plain, and "the screening" is defined. A shorter opening would read better on a phone, but this is not a defect.

7. Line 31, option 6C "Yes, with no such limit". This is accurate. The wording is a little stark compared with 6A and 6B. Because every question allows the owner's own words, this does not tilt the choice.

I found no per-option consequences or leaning facts, and no fact on the card contradicts its record. The questions are fair and keep the map's meaning.
