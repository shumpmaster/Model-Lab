# Project document — the prompt engine (P-001)

*One document, two parts (D-052). Part 1 is settled when the owner approves the move out of Discovery; after that its milestones change only as section 3 says; Part 2
stays living. The Critic checks Part 1 against the definition of ready.*

# Part 1 — The brief

*Lines in italics are instructions. CI checks that every section below has content beyond its instruction once a spec is frozen (S-009), and section 9 once a project is approved or waits on its Design gate (S-025).*

## 1. Scope
*What is in, what is explicitly out, and where it must work (target devices or places).*

## 2. Strategy
*In plain language: the chain from the deliverables to the value — how this work produces it.*

**The problem, stated without reference to any industry (Discovery-4, draft for the Critic).** Work passes from one worker to the next through a written hand-over: what to do, what to read, and what counts as done. An independent check then accepts the work or sends it back. Work sent back costs another round, and the record seldom shows why it went back: the written instructions, the material handed over, how the work was split, the worker's own capability, or the check itself. The problem is to make work pass its check first time more often, by finding which of those causes each return and changing only what helps, without adding more written rules than a worker reliably follows, and without the change being judged only by checks that can be fooled.

**How other fields solved it, and what that changes here** (research/Q-005-memo.md; research/Q-002-memo.md):
- *Written hand-over tools and checklists* (surgery, intensive care, shift handover) helped where the failure they targeted was common and the tool was carried out in full, and did nothing where it was mandated as text alone (Q-005 §1 item 1, P-1, P-2). Here: count how common each kind of return is before choosing what to change (M1), and check from the transcript that an instruction was followed, not only that it was written.
- *Fixes after single incidents* were mostly weak written reminders, and the same events recurred; fixes that do not depend on remembering a rule worked better (Q-005 §1 item 3, P-7). Here: prefer a tool permission or a mechanised check to another sentence of instruction wherever one will do.
- *Rule sets grow until they are not followed*, and fields that keep them usable retire rules on a schedule (Q-005 §1 item 4, P-6, P-11). Here: every instruction change is tested, and one that does not move its measure is removed.
- *Before-and-after comparisons misled in both directions*; only a concurrent comparison told which (Q-005 §1 item 2, P-8). Here: compare each change with no change on the same past tasks (M2).
- *In agent pipelines specifically*, instructions were the limiting factor for vague delegation and underspecified requirements, and not for persona wording, longer instruction lists or reasoning prompts; the model and the effort and context a session works with were larger levers on capability-limited tasks (Q-002 §1 items 4 and 5). Here: the instructions are one candidate cause among five, which is why the problem is stated as rework, not as "better prompts".

## 3. The 25,000-foot plan
*The deliverables two levels deep, with the dependencies between them. The second level is the milestones: each phase's standard milestones come with the model (OPERATING_MODEL.md §4); list here the project's own, at least one, after the standard ones in each phase and side by side with them, one per line, name first: `<plain-English name> (M<id>) · done when <what is achieved> · phase: <Discovery, Design, Build or Launch>`; a milestone added for later work on the product, a fix or an addition filed as a new project item, then gives that item: ` · for: P-<n>`; give each such item at least one, which its spec names in its header. Each is an achievement, never a task: use the name the owner would use, with no codes or ids in it, and say what is achieved, not what someone does. End every line you draft or reword with why the project needs it, in plain words: ` · why: <reason>`, with no ` · ` inside the reason; once written, a why is changed, never removed, and the owner may change it through the Chief of Staff. Draft them here during Discovery; the owner approves them at the Design gate. After that, have the Critic check each new or reworded line (adding or changing a why is a rewording): a new one before it goes to the owner, a reworded one before it is committed (a rewording needs no owner ruling); add one only with the owner's approval, and drop one, or change its order, its phase or its ` · for:` item, only by the owner's ruling; never delete or renumber one: to drop it, add ` · dropped` after its other parts, before any ` · why:`. A milestone built outside the pipeline names its sprints after its phase, before any ` · dropped` or ` · why:`: ` · sprints: PR #40, PR #41`. Also give each standard milestone one line anywhere in this section, saying whether this project takes it on and why: `- <Phase>-<n> (standard) · taken on · why: <reason>` or `- <Phase>-<n> (standard) · skipped · why: <reason>`, where `<Phase>-<n>` is its place in the model's table, Discovery-1 to Launch-5; one line holds for every run of its phase. Write Discovery's and Design's in the brief, ruled with the Design gate, and Build's and Launch's before the Build gate, ruled with it. Until its gate is ruled, adding or changing a line needs the Critic's check. After it, anything that drops work needs the owner's ruling: a change from taken on to skipped, a line removed, or a line first added as skipped; taking on more work (a change from skipped to taken on, or a line first added as taken on) and a change of its why alone need only the Critic's check. Skipping one excuses no record a check or a gate needs. When the owner accepts one of the project's own milestones, add ` · reached: <yyyy-mm-dd>` after any ` · sprints:` part and before any ` · dropped` or ` · why:`, in a commit whose `Owner-Ruling:` trailer names the owner's acceptance record; only the owner's ruling adds, changes or removes it (S-033).*

**Discovery**
- Discovery-1 (standard) · taken on · why: the owner logged the idea and agreed on 2026-11-01 to take it up first
- Discovery-2 (standard) · taken on · why: the owner wants fewer review rounds and better research, and the project needs a point at which it stops
- Discovery-3 (standard) · taken on · why: the groundwork map's questions shape the research and the owner has answered its short list
- Discovery-4 (standard) · taken on · why: the research found the instructions may not be the main cause of rework, so the problem must be stated before it is solved
- Discovery-5 (standard) · taken on · why: seven research questions were asked, the groundwork map among them, and every finding must be source-checked before it is relied on
- Discovery-6 (standard) · taken on · why: the research names design traps that could make the project measure the wrong thing
- Discovery-7 (standard) · taken on · why: the owner set a testing budget and the work touches every project's agents, so its limits must be agreed
- Discovery-8 (standard) · taken on · why: the owner rules the Design gate on a checked brief
- The causes of rework are known (M1) · done when the share of work sent back is counted from past records for each kind of task, each kind has a stated cause, and a starting figure is on record for later comparison · phase: Discovery · why: the owner wants to close the gaps in how work passes between agents, and the research found that wording may matter less than inputs and how work is split

**Design**
- Design-1 (standard) · taken on · why: success must be set in scenarios the owner can approve
- Design-2 (standard) · taken on · why: the change touches how every role hands work to the next
- Design-3 (standard) · taken on · why: whether the candidate changes help is unknown and must be tested, not assumed
- Design-4 (standard) · taken on · why: much of the outside evidence was hard to confirm, so every fact relied on needs its source
- Design-5 (standard) · taken on · why: the agents' instructions, inputs, records and checks must fit together
- Design-6 (standard) · taken on · why: the plan changes the model's own rules and must pass review before anything is built
- A fair test of the changes is ready (M2) · done when a test comparing each candidate change with leaving things as they are, on the same past tasks, is written down before any run, with its measure, its size within the owner's 100-run limit and a group where nothing changes · phase: Design · why: the owner accepted that no change may be the result, and the research found that about 100 paired runs can only show large gains, so the test must be set up before it is run

**Build**
- Every agent's brief and model on record (M3) · done when every agent session, whether started by the automatic pipeline or from a conversation, records the brief it was given and the model that ran it, and each brief can be read against how its work went (review rounds, fails, rework) · phase: Build · why: the owner ruled that conversation-started agents keep this record across the model and approved recording each brief against how its work went, and the automatic pipeline already records it, so the record covers every session
- Each tested change has a result (M4) · done when every tested change has a recorded result, kept, dropped or no difference found, from runs within the testing budget the owner sets at the Build gate · phase: Build · why: the owner wants a refined prompt engine that is not redundant with the model's existing checks, so each change must earn its place

- The operating model runs on what worked (M5) · done when the changes that proved themselves and the rule for recording each brief are part of the operating model under its own rules, and nothing of the result is left only in the work repository · phase: Build · why: the owner wants the result integrated into the operating model completely and ruled that each result moves fully into the model repository
- Every slip in this work corrected (M6) · done when each entry in the lessons log is corrected in the operating model or closed with its reason · phase: Build · why: the owner asked that every slip, error and miss be tracked and corrected within this workflow at the end

## 4. Owners
*An owner for every deliverable, including anything that needs the owner or an outside party.*

## 5. Limits
*The spend ceiling, the data boundaries (what data may go to which outside service), and the tier (T1, T2 or T3 by the tier triggers), which is the project's trust level.*

## 6. Value and stop rule
*This project's own measure of value, the target and date, and what counts as a miss — including the cost to the owner's time. Write each value target on its own line starting with its ID, like `V1: <measure>, <target>, <date>`; spec criteria trace to these IDs.*

## 7. Solid foundation
*Every load-bearing unknown, each answered with evidence (library entry or research memo), including through research sub-projects if needed. Name the groundwork map this rests on (research/<Q-id>-memo.md) and the owner's answers to its shortlist, or say why no map was needed.*

**Pre-mortem (Discovery-6, draft for the Critic).** Imagine it is the end and the project failed. The likeliest reasons, each with what would show it early and how the plan answers it:

| # | How it failed | Early sign | What the plan does about it | Source |
|---|---|---|---|---|
| R1 | We tuned the wording, but the work was being sent back for other reasons: missing inputs, badly split tasks, or the model's limits | M1's count assigns most returns to causes other than the instructions | Stop rule: back to the owner to re-aim or close; changes may target inputs or checks, not only wording | Q-002 §1 items 4–5; Q-006 §0 item 3 |
| R2 | The test was too small to tell a real gain from chance, and we kept changes that did nothing | Fewer than about 15 tasks in the test where the two versions disagree | Keep a change only on a gain of 20 points or more in a paired test on the same tasks (value target, if the owner rules it) | Q-003 §0 item 3, §4 |
| R3 | The checks that judged the test were fooled: a model judge preferred work like its own, or the work gamed the check | Pass rates rise while the owner's or a second checker's view does not | Judge on a different model from the work; keep a held-back check the work never sees; sample results for the owner | Q-003 (judges favour their own outputs, as reported in Q-002 §1 item 6); Q-007 §bottom line 2 |
| R4 | We fitted the changes to the past tasks we tested on, and they did not hold on new work | Gains in the test vanish in real use | The second value target measures real use, and a change that fails it is retired, not tuned | Q-004 §1; Q-003 §4 |
| R5 | The model changed under us, and instructions tuned for one model stopped working | A model version change during or after testing | Record the model with every brief (M3); re-test kept changes when the model changes | Q-004 §1 items 1–2 and the tentative retirement dates in §4.5.1 |
| R6 | Each fix added another rule, and the instructions grew past what agents follow | Instruction length rises across the project | Every change carries its own removal test; prefer a mechanised check to more text | Q-005 P-6, P-7; Q-007 §bottom line 2 |
| R7 | The past records could not show what caused a return, because the briefs were never kept | M1 cannot assign a cause for most conversational-path work | Record each brief and model from now on (M3); state plainly which counts are descriptive only | Q-006 §0 items 1 and 4 |
| R8 | The research behind the plan was weaker than it looked, because most outside sources could not be opened | Facts the plan relies on stay unconfirmed in the library | Rely only on library entries that passed the Source checker; test the environment's access before any further research (LL-12, LL-22) | research/Q-002-to-Q-007-corrections-confirmation.md |

These risks shape any further research: R1 and R7 are answered by M1's count of past records, not by new outside research; R3 and R5 may each need one narrow research question before Design if M1 leaves them open.

## 8. Clear and consistent
*Key terms defined; constraints checked against each other and found not to contradict.*

## 9. The target user
*Either the one line `The owner is the user.`, or the two lines `Profile: docs/users/PROFILE.md` and `Approved: decisions/questions/<project item>-user-profile-<n>.md`. Build the profile from Discovery's research, in the form docs/users/_PROFILE.md, and have the owner approve it before the definition-of-ready check (S-025).*

# Part 2 — The intent

## Intent
The owner's purpose, preferences and trade-offs for this project, and what they would hate. Drafted by
the Chief of Staff from conversations, portfolio defaults and past rulings; confirmed on the
move-to-Design card.
