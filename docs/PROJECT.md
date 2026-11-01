# Project document — the prompt engine (P-001)

*One document, two parts (D-052). Part 1 is settled when the owner approves the move out of Discovery; after that its milestones change only as section 3 says; Part 2
stays living. The Critic checks Part 1 against the definition of ready.*

# Part 1 — The brief

*Lines in italics are instructions. CI checks that every section below has content beyond its instruction once a spec is frozen (S-009), and section 9 once a project is approved or waits on its Design gate (S-025).*

## 1. Scope
*What is in, what is explicitly out, and where it must work (target devices or places).*

## 2. Strategy
*In plain language: the chain from the deliverables to the value — how this work produces it.*

## 3. The 25,000-foot plan
*The deliverables two levels deep, with the dependencies between them. The second level is the milestones: each phase's standard milestones come with the model (OPERATING_MODEL.md §4); list here the project's own, at least one, after the standard ones in each phase and side by side with them, one per line, name first: `<plain-English name> (M<id>) · done when <what is achieved> · phase: <Discovery, Design, Build or Launch>`; a milestone added for later work on the product, a fix or an addition filed as a new project item, then gives that item: ` · for: P-<n>`; give each such item at least one, which its spec names in its header. Each is an achievement, never a task: use the name the owner would use, with no codes or ids in it, and say what is achieved, not what someone does. End every line you draft or reword with why the project needs it, in plain words: ` · why: <reason>`, with no ` · ` inside the reason; once written, a why is changed, never removed, and the owner may change it through the Chief of Staff. Draft them here during Discovery; the owner approves them at the Design gate. After that, have the Critic check each new or reworded line (adding or changing a why is a rewording): a new one before it goes to the owner, a reworded one before it is committed (a rewording needs no owner ruling); add one only with the owner's approval, and drop one, or change its order, its phase or its ` · for:` item, only by the owner's ruling; never delete or renumber one: to drop it, add ` · dropped` after its other parts, before any ` · why:`. A milestone built outside the pipeline names its sprints after its phase, before any ` · dropped` or ` · why:`: ` · sprints: PR #40, PR #41`. Also give each standard milestone one line anywhere in this section, saying whether this project takes it on and why: `- <Phase>-<n> (standard) · taken on · why: <reason>` or `- <Phase>-<n> (standard) · skipped · why: <reason>`, where `<Phase>-<n>` is its place in the model's table, Discovery-1 to Launch-5; one line holds for every run of its phase. Write Discovery's and Design's in the brief, ruled with the Design gate, and Build's and Launch's before the Build gate, ruled with it. Until its gate is ruled, adding or changing a line needs the Critic's check. After it, anything that drops work needs the owner's ruling: a change from taken on to skipped, a line removed, or a line first added as skipped; taking on more work (a change from skipped to taken on, or a line first added as taken on) and a change of its why alone need only the Critic's check. Skipping one excuses no record a check or a gate needs. When the owner accepts one of the project's own milestones, add ` · reached: <yyyy-mm-dd>` after any ` · sprints:` part and before any ` · dropped` or ` · why:`, in a commit whose `Owner-Ruling:` trailer names the owner's acceptance record; only the owner's ruling adds, changes or removes it (S-033).*

**Discovery**
- Discovery-1 (standard) · taken on · why: the owner logged the idea and agreed on 2026-11-01 to take it up first
- Discovery-2 (standard) · taken on · why: the project needs its own measure of success and a point at which it stops
- Discovery-3 (standard) · taken on · why: the groundwork map's questions shape the research and the owner has answered its short list
- Discovery-4 (standard) · taken on · why: the research found the instructions may not be the main cause of rework, so the problem must be stated before it is solved
- Discovery-5 (standard) · taken on · why: six research questions were asked and every finding must be source-checked before it is relied on
- Discovery-6 (standard) · taken on · why: the research names design traps that could make the project measure the wrong thing
- Discovery-7 (standard) · taken on · why: the owner set a testing budget and the work touches every project's agents, so its limits must be agreed
- Discovery-8 (standard) · taken on · why: the owner rules the Design gate on a checked brief
- The causes of rework are known (M1) · done when the causes of work being sent back across the model's past work are measured by kind of task, with a starting point the project can compare later changes against · phase: Discovery · why: the owner wants to close the gaps in how work passes between agents, and the research found that wording may matter less than inputs and how work is split

**Design**
- Design-1 (standard) · taken on · why: success must be set in scenarios the owner can approve
- Design-2 (standard) · taken on · why: the change touches how every role hands work to the next
- Design-3 (standard) · taken on · why: whether instruction changes help is unknown and must be tested, not assumed
- Design-4 (standard) · taken on · why: much of the outside evidence was hard to confirm, so every fact relied on needs its source
- Design-5 (standard) · taken on · why: the agents' instructions, their records and their checks must fit together
- Design-6 (standard) · taken on · why: the plan changes the model's own rules and must pass review before anything is built
- A fair test of instruction changes is ready (M2) · done when a test comparing instruction versions on the same past tasks is registered in advance, with its measure, its sample within the owner's 100-run limit and a no-change arm · phase: Design · why: the owner accepted that no change may be the result, and the research found that only a paired test of this size can tell a real gain from noise

**Build**
- Every agent's brief and model on record (M3) · done when every agent session, whether started by the automatic pipeline or from a conversation, records the brief it was given and the model that ran it · phase: Build · why: the owner ruled this should hold across the model, and without it no one can tell which instructions led to clean first passes
- Instruction changes proven or ruled out (M4) · done when the registered test has run and each tested change is kept, dropped or found to make no difference · phase: Build · why: the owner wants a refined prompt engine that is not redundant with the model's existing checks, so each change must earn its place

**Launch**
- The operating model runs on what worked (M5) · done when the changes that proved themselves, and the rules for recording and testing instructions, are part of the operating model under its own rules and Service-Desk has adopted that version · phase: Launch · why: the owner wants the result integrated into the operating model completely, not kept in a separate repository
- Every slip in this work corrected (M6) · done when each entry in the lessons log is corrected in the operating model or closed with its reason · phase: Launch · why: the owner asked that every slip, error and miss be tracked and corrected within this workflow at the end

## 4. Owners
*An owner for every deliverable, including anything that needs the owner or an outside party.*

## 5. Limits
*The spend ceiling, the data boundaries (what data may go to which outside service), and the tier (T1, T2 or T3 by the tier triggers), which is the project's trust level.*

## 6. Value and stop rule
*This project's own measure of value, the target and date, and what counts as a miss — including the cost to the owner's time. Write each value target on its own line starting with its ID, like `V1: <measure>, <target>, <date>`; spec criteria trace to these IDs.*

## 7. Solid foundation
*Every load-bearing unknown, each answered with evidence (library entry or research memo), including through research sub-projects if needed. Name the groundwork map this rests on (research/<Q-id>-memo.md) and the owner's answers to its shortlist, or say why no map was needed.*

## 8. Clear and consistent
*Key terms defined; constraints checked against each other and found not to contradict.*

## 9. The target user
*Either the one line `The owner is the user.`, or the two lines `Profile: docs/users/PROFILE.md` and `Approved: decisions/questions/<project item>-user-profile-<n>.md`. Build the profile from Discovery's research, in the form docs/users/_PROFILE.md, and have the owner approve it before the definition-of-ready check (S-025).*

# Part 2 — The intent

## Intent
The owner's purpose, preferences and trade-offs for this project, and what they would hate. Drafted by
the Chief of Staff from conversations, portfolio defaults and past rulings; confirmed on the
move-to-Design card.
