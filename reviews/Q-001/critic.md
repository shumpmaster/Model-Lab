Verdict: PASS

The Critic's neutral-phrasing check of research question Q-001 (D-055), verbatim: round 1 (FAIL), round 2 on the redraft (PASS). Recorded by the orchestrator. Recorded verbatim. Session: session_01QBwHGJH9m3A4Ray7WpHzBo (Critic subagent a82ffa2e8ca7eed36), 2026-11-01.

## Round 1
Verdict: FAIL

I checked /home/user/Model-Lab/research/Q-001.md against /home/user/Model-Lab/research/_QUESTION.md, /home/user/Model-Lab/research/_GROUNDWORK.md and OPERATING_MODEL.md (§4 "Groundwork research", lines 194 and 243–244; the knowledge method, line 287). The form is mostly right. The question is mostly neutral, but it has two framing problems and five clear gaps.

**Neutral phrasing**

1. Line 9: "before designing how such instructions are written, measured and improved over time". This assumes the outcome is a design for writing, measuring and improving instructions, which is a preferred solution. It also assumes instruction quality can be measured. A Researcher reading this will map how to build such a system, not whether instructions are the right thing to work on.
   - Change to: "before deciding whether and how the instructions should be changed, observed or measured."
   - Then "how instruction quality can be observed or measured" becomes "whether, and how, instruction quality can be observed or measured."

2. Line 9: "what determines whether an instruction handed to an agent leads to good work". This treats the instruction as the cause and leaves out rival causes, so the map could only confirm that instructions matter. Rival causes include the model chosen, the quality of the inputs, how the task is split up, the reviewers' own mistakes, and limits on what an agent can see or hold in context.
   - Change to: "what determines whether an agent session produces good work, and how much of that the instructions explain compared with other factors (the model, the inputs, how the task is split, the checks)."

3. Line 9 (minor): the list of outside fields, "handoffs between human teams, procedure writing, clinical or aviation checklists, requirements engineering", leads the Researcher toward fields that favour checklists and written procedure.
   - Either drop the list, or add a field that points the other way: "...and fields where written procedure was found to help little or to harm."

**Gaps**

None of these areas is in the scope, and an expert would cover each one:

4. **Cost and usage of agent runs.** Longer instructions, more review rounds and experiments all cost tokens, money and time. Nothing asks what instruction changes cost or what measuring them costs.
   - Add: "what writing, running and measuring instructions costs in agent runs and money, and how that limits what can be tried."

5. **The owner's time.** One human owner is the scarce resource. Nothing asks how much owner attention reviewing, approving or tuning instructions takes, or what the owner must do that nobody else can.
   - Add: "how much of the owner's time each approach needs, and which decisions can only be the owner's."

6. **Versioning and tracing.** "How instructions are changed" (line 9) does not cover how versions are recorded or rolled back. It also does not cover how a piece of work is traced to the exact instructions it ran under, which you need before you can say whether a change helped.
   - Add: "how instruction versions are recorded, tied to the work produced under them, and rolled back."

7. **Differences by task type.** Research, build, review, triage and gate tasks may fail in different ways and need different measures. The question treats "an instruction" as one kind of thing.
   - Add: "how the answers differ by kind of task (research, build, review, triage)."

8. **Over-fitting to past failures.** Patching instructions after each failure tends to make them longer, contradictory and narrowly fitted to old cases. Measures can also be gamed (Goodhart's law: a measure that becomes a target stops measuring well). This is a known design trap, and nothing invites it.
   - Add: "the risks of changing instructions in response to individual failures, including growth, conflict between rules, and fitting to the checks rather than the goal."

9. **Smaller gaps** (could be folded into the items above):
   - Results vary from run to run and there are few runs, so it is hard to tell a real improvement from noise.
   - Instructions may not carry over when the model behind a role changes.
   - The role definition and the task brief can conflict, and nothing says which wins.
   - Reviewer feedback that sends work back is itself an instruction, and its quality goes unexamined.
   - No "leave it as it is" option is named as the baseline to compare against.

**Form**

10. It meets the form: it starts "Groundwork map:", has the three sections in order, and has the topics and depth lines. One inconsistency: line 20 says "depth: 3 graded memo (in the groundwork-map form)", but the groundwork-map form says "This is a map of questions, not graded fact", and only known items are graded.
    - Change to: "depth: 3 (groundwork map; known items graded and sourced)", or whatever depth convention the Chief of Staff uses for groundwork requests. Either way the two documents should not contradict each other.

11. I could not check the topics line against the library's topics. Model-Lab has no library entries with topics to compare it to. The Orchestrator should confirm the six words match the library's terms.

12. Note, not a failure: the scope names specific repositories and files (line 7). That is fine as context, but those documents should hold no owner leanings or hoped-for answers. Under the "Who sees what" rule (line 243), the Researcher must never see them. I did not check those documents.

## Round 2 (confirmation, on the redraft)
Verdict: PASS

I checked the redraft at /home/user/Model-Lab/research/Q-001.md. Findings 1–10 are resolved, and the redraft adds no new leaning or gap.

1. **Resolved.** Line 9 now reads "before deciding whether and how these instructions should be changed, observed or measured". It no longer assumes a system for improving instructions will be built.
2. **Resolved.** Line 10 asks how much of good work "the instructions explain compared with other factors (the model, the inputs, how the task is split, the checks)". Rival causes now get equal weight.
3. **Resolved.** Line 20 drops the list of fields that lean toward checklists and adds "where written procedure was found to help little or to harm".
4. **Resolved.** Line 16 adds cost in agent runs and money.
5. **Resolved.** Line 17 adds the owner's time and which decisions can only be the owner's.
6. **Resolved.** Line 12 adds how versions are recorded, tied to the work and rolled back.
7. **Resolved.** Line 13 adds differences by kind of task. It also widens my list to definition work and questions put to the owner.
8. **Resolved.** Line 19 adds the risks of changing instructions after single failures: growth, conflicting rules, and fitting to the checks rather than the goal.
9. **Resolved.**
   - Run-to-run variation and comparing against leaving things as they are: line 11.
   - Whether instructions carry over when the model changes: line 15.
   - Conflict between the role definition and the brief: line 14.
   - Checker findings handed back with failed work: lines 7 and 13.
10. **Resolved.** Line 31 now reads "depth: 3 (groundwork map; known items graded and sourced)", which agrees with the groundwork-map form.

**New leaning or gap:** none. Every new line is put as an open question ("whether", "how", "how much"), and none states a hoped-for answer or a preferred approach.

**11 and 12:** I accept your answers and have nothing further to add.
