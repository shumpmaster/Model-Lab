Verdict: PASS

The Critic's neutral-phrasing check of research questions Q-002 to Q-007, on a different model from their writer, verbatim: round 1 (FAIL), round 2 (PASS, with one grammar fix to Q-003 and an optional one to Q-005, both applied). Recorded by the orchestrator. Session session_01QBwHGJH9m3A4Ray7WpHzBo, 2026-11-01.

## Round 1
Verdict: FAIL

Six small wording fixes are needed (Q-002, Q-003, Q-005, Q-006, Q-007, and a form check across all). None needs a redraft. Q-004 passes unchanged. The six together cover the map's five and the earlier Critic's findings 1, 2 and 4 to 7, with the minor gaps noted at the end.

I read the six questions, the form, the map, the earlier Critic's findings and OPERATING_MODEL.md §6 and the lines that cite neutrality (L38-47, L243-244, L287-302). I could not find a §4 or §5 headed "Groundwork research" or "Who sees what" by grep. The workflow is §4, the team is §5, and the rule I applied is "the Researcher never sees the hoped-for answer… the owner's leanings" (L243-244).

**Q-002 (levers on quality; fix needed)**
- (1) Neutrality: the question asks for evidence on one side only. "Include the finding, where it exists, that instructions are not the limiting factor." Nothing asks for the matching finding that they are the limiting factor.
  - Change to: "Include evidence on both sides: where instructions have been found to be the limiting factor, and where they have been found not to be."
  - "What each answer would change" opens with the instructions branch ("If instructions explain a large share, they are the main lever") and gives the other branches less. It is acceptable once the question is fixed.
- (2) Answerability: five levers across every failure kind is wide for one graded memo. Consider adding "Name the failure kinds you cover and which you leave out."
  - The decision is clear.
- (3) Form: fine.

**Q-003 (good work, checkers, small-sample measurement; fix needed)**
- (1) Neutrality: the question is balanced. It includes "the case where measurement at that scale cannot separate a change from noise" and asks about checker reliability.
  - Leak risk: the decision section gives the owner's budget, "within the owner's limit of about 100 test runs". That is an owner constraint, and §5 (L243-244) keeps the owner's leanings from the Researcher. If the Researcher sees this section, move the number to the Chief of Staff's notes.
  - Alternatively write "within a budget of about 100 test runs". The question text itself already says "only tens of runs are affordable".
  - "how can repeated runs be designed so they are not re-running for a better answer?" assumes repeated runs are wanted. Change to: "whether and how repeated runs can be designed…".
- (2) Answerability: the question is dense (judging, checker reliability, statistics, sample sizes, pre-registration) but answerable at depth 3. The decision is clear.
- (3) Form: fine.

**Q-004 (carry-over across models; passes)**
- (1) Neutrality: it is even. "reduce any loss or to make no difference. Include evidence that instructions carry over well." The decision section gives large and small losses equal weight.
  - Optional: "reduce any loss" assumes some loss exists. "reduce any loss, or to make no difference" is already there, so I would not make this a finding.
- (2) Answerability: "another model or a newer version" are two different cases. Optional: "Treat replacement by a different model and by a newer version of the same model separately."
- (3) Form: fine.

**Q-005 (other fields' written procedures; fix needed)**
- (1) Neutrality: the question is balanced ("improve outcomes, make no difference, or cause harm"). The decision section assumes limits and transfer will exist.
  - "what limits they set on how instructions are added to and retired" presumes limits exist. Change to "what limits, if any".
  - "What each answer would change" has no branch for "nothing transfers". Add: "if none transfer, the project relies on its own evidence."
  - "what did they find about rules added in response to single incidents?" is neutral, but add "(benefits as well as costs)" to match Q-007(c).
- (2) Answerability: six fields at depth 3 invites a shallow tour. Add: "Choose the fields with the strongest evidence and say which were left out."
  - Map item K3 (intent-based orders versus detailed procedure, "work as imagined versus work as done") appears only as "military orders". Optional: add "including intent-based orders versus detailed procedure".
- (3) Form: fine.

**Q-006 (Service-Desk records; fix needed)**
- (1) Neutrality: it is mostly even. It lists the causes ("what the agent was told… inputs… model… division… checker") and then "which cannot be traced".
  - "What each answer would change" is tilted: "Usable records give the project a baseline at no new run cost; unusable ones mean new runs from the owner's test budget." This frames usable as the better outcome.
  - Change to: "Usable records give a baseline without new runs; unusable ones mean the baseline is collected with new runs."
  - The same section quotes the owner's scope: 'within "every kind, incrementally"'. That is an owner leaning. Remove the quotation and write "sets where work starts across the kinds of task".
- (2) Answerability: there are 149 or more review files and six task kinds, and attribution of findings to causes is a judgment. At depth 3 it will be a sample.
  - Add: "State how many records you read and how you chose them, and how you decided a finding's cause."
  - A cold reader can follow the decision.
- (3) Form: fine.

**Q-007 (handoff loss, override, changing instructions; fix needed)**
- (1) Neutrality: "What each answer would change" presupposes the findings. "Known handoff losses set what a brief must carry; known override and gaming risks set what a change must be tested against; the evidence on changing after failures sets the project's rule for when to change."
  - It has no branch for "little is known" or "no rule is warranted". Add: "where the evidence is thin, the project treats the point as untested; (c) may show no rule is warranted."
  - Sub-question (c) is even ("benefits and the costs… on a schedule or not at all"). Sub-questions (a) and (b) ask only about losses and failures. Add to (a): "and what is preserved or improved by that design".
- (2) Answerability: it is three memos in one (handoff, injection and gaming, change policy). Split into three questions, or say it is graded as three parts, one per sub-question. It also overlaps Q-005's incident rules.
  - Add: "(c) is about language-model pipelines; Q-005 covers other fields." Or merge Q-005's incident-rules sentence into this one.
- (3) Form: fine.

**Form across all six**
- Each has the three sections, a `topics:` line and a `depth:` line.
- Each names the project and says it is the "subject being studied, not… evidence" (earlier findings 3 and 8).
- I cannot check whether the topics match the library's, because I was told to read nothing else.
- Possible leak: all six decision sections call the project "the prompt engine", which names the owner's chosen solution. Confirm the Researcher's pack excludes the decision section. If it does not, drop the label.

**Coverage of the map's five**
- Shortlist 1 is Q-002. Shortlist 2 is Q-003, including the no-re-run conflict. Shortlist 3 is Q-004. Shortlist 4 is Q-005. Shortlist 5 is Q-006. Q-007 is an addition from earlier finding 7 and map items J, M and E.

**Coverage of the earlier Critic's findings**
- Finding 1 (the case that instructions are not the limiting factor): Q-002, but one-sided (see above).
- Finding 2 (benefits and risks): Q-005 and Q-007(c). Q-007(a) and (b) are risk-only.
- Finding 4 (alternative levers): Q-002 covers tools and context design, and checks. Checker count and rounds are not named. Optional: add "the number of checkers or rounds" to Q-002's "the checks applied after it".
- Finding 5 (good work, checker reliability): Q-003.
- Finding 6 (instruction design): Q-002.
- Finding 7: handoff and injection in Q-007, existing reviews' failure modes in Q-006. Q-006 does not separate the scripted path from the conversational path, which the map flags (C1-C3). Add to Q-006's records sentence: "and how they differ between work started by the script and work started from a conversation".

**Gaps and overlaps**
- No question asks whether changing the checkers' own instructions changes what the doers' measure means (map I1) or how fast role files grow (J1). Q-007(c) could take both if the Chief of Staff wants them covered.
- Overlaps:
  - Q-002 against Q-003 on the "checks" lever.
  - Q-005 against Q-007(c) on rules added after incidents.
  - Q-002's "the model" lever against Q-004.
  - Each overlap is tolerable once the scope notes above are added.

## Round 2
Verdict: PASS

All my round-1 findings are resolved. I found nothing new that leans. I read Q-002 to Q-007 again in full.

**Resolved**
- **Q-002:** The question now asks for "evidence on both sides" and has "(including the number of checkers or rounds)" and "Name the failure kinds you cover and which you leave out."
- **Q-003:** The owner's limit is now "a budget of about 100 test runs". "Whether and how repeated runs" is in.
- **Q-004:** The two replacement cases are separated.
- **Q-005:**
  - "limits, if any" is in.
  - "(benefits as well as costs)" is in.
  - Intent-based orders are named.
  - "Choose the fields with the strongest evidence and say which were left out." is in.
  - "if none transfer, the project relies on its own evidence" is in.
- **Q-006:**
  - The baseline line is now neutral: "Usable records give a baseline without new runs; unusable ones mean the baseline is collected with new runs".
  - The quoted owner phrase is gone.
  - The script versus conversation split is added.
  - The sampling and cause-decision statement is added.
- **Q-007:** The preserved or improved clause, three graded parts, the Q-005 scope note, the checker-instruction and file-growth items, and the thin-evidence and "no rule is warranted" branches are all in.
- **Label:** "The prompt engine" no longer appears in any of the six.
- **Form:** Each file has the three sections, a `topics:` line and a `depth:` line. The pipeline-as-subject sentence is in all six.

**One fix, grammar only (Q-003)**
- The question now reads "…what sample sizes do they need, and whether and how repeated runs can be designed…". The last clause no longer parallels the two before it.
- Change to: "…what sample sizes do they need, and can repeated runs be designed, and if so how, so they are not re-running for a better answer?"

**Optional, not a finding (Q-005)**
- "military orders, including intent-based orders versus detailed procedure, software runbooks" reads as if "software runbooks" belongs to the military clause. Put "(including intent-based orders versus detailed procedure)" after "military orders" in brackets, or move it to the end of the list.

**Residual note, not a failure**
- Q-002, Q-003 and Q-006 still name P-001's purpose in the decision section ("how the written instructions… are written, checked and changed"). That describes the project and does not state a hoped-for answer, so I let it stand.

