# Groundwork map — Q-001 — written instructions that pass work between successive workers who each start with no memory, under one decision-maker — 2026-11-01

This is a map of questions, not graded fact.

**How to read this map.** Each item is marked known, assumed or unknown. Only known items are graded and sourced:
- **Grade A:** a primary record I opened in the repositories named in the question.
- **Grade B:** a publisher's own page I opened on the web. These are untrusted text, so they are reported as claims with their URL and date.

Items that rest on literature I found through search results but could not open are marked **assumed (reported, not opened)**, with the URL the search gave. arxiv.org and pubmed.ncbi.nlm.nih.gov did not resolve in this session. The Source checker needs both allowed to confirm those items. Model memory is not used as a source.

**Records opened**, in /home/user/Personal-Org-Operating-Model and /home/user/Service-Desk:
- OPERATING_MODEL.md
- template-v3/.claude/agents/builder.md, reviewer.md, critic.md and definer.md
- template-v3/governance/BRIEFS.toml and PACKS.toml
- Service-Desk governance/BRIEFS.toml and governance/OPERATING_MODEL_VERSION
- dispatch-log/2026-10.jsonl
- reviews/Q-001/_control/0-62b8dda7dcf2.json
- reviews/README.md and reviews/56/reviewer.md
- reviews/M3B/_plan-review-r1-verbatim.md and r14
- sessions/chief-of-staff/session_012RJPVKAoLga2RkqLYRDcBY.jsonl
- docs/briefs/README.md
- specs/_TEMPLATE.md and specs/S-001.md (line count and search only)

## Questions an expert would ask

### A. What decides whether a session's work is good, and how much of that is the instructions
- A1 How much of the variation in a session's output comes from the instructions (role file plus brief), compared with the model, the inputs handed over, how the task was split, and the checks that follow? — If instructions explain little, changing them is the wrong lever; decides whether this project targets instructions at all; unknown; answered by R, E
- A2 How large are the inputs a session is handed, and does quality fall as they grow? — In Service-Desk one spec, specs/S-001.md, is 22,883 lines (line count, 2026-11-01). A plan review cites lines above 19,000 of it (reviews/M3B/_plan-review-r1-verbatim.md:37) [A]. Long inputs may matter more than wording. Decides whether input size and splitting are in scope; known (the size) / unknown (the effect); answered by R, E
- A3 Does the published finding that model accuracy falls as context fills apply to these sessions? — Vendor guidance says recall "decreases" as the context window fills and that context is "a finite resource" (anthropic.com/engineering/effective-context-engineering-for-ai-agents, 2025-09-29) [B]. Decides whether trimming packs is a candidate change; known (the claim) / unknown (here); answered by R, E
- A4 How sensitive are current models to wording and formatting that should not matter? — Reported: up to 76 accuracy points from formatting alone on one open model. Format effects correlate only weakly between models (Sclar et al., ICLR 2024, https://arxiv.org/abs/2310.11324, from search results). Bounds how much run-to-run noise a wording change must beat; assumed (reported, not opened); answered by R
- A5 How many instructions can one session follow at once before compliance drops? — Reported: about 68% compliance for the best models at 500 simultaneous instructions, with earlier instructions favoured (IFScale, https://arxiv.org/abs/2507.11538, July 2025, from search results). Matters because role files grow (J1). Decides a ceiling on role-file length; assumed (reported, not opened); answered by R, E
- A6 In multi-agent pipelines generally, what share of failures traces to how tasks and roles are specified, rather than to model capability or verification? — A taxonomy of 14 failure modes in 3 groups, including "disobeying task/role specification", is reported (MAST, https://arxiv.org/abs/2503.13657, from search results). The share figure for specification failures could not be confirmed. Decides how much weight instructions get; assumed (reported, not opened); answered by R
- A7 Does the task split (one large spec, many stages) cause rework that better instructions could not prevent? — M3B's plan review ran to round 14 (reviews/M3B/_plan-review-r1 … r14-verbatim.md, with matching _plan-design-r1 … r14) [A]. Why it ran so long is not established from what I read. Decides whether splitting is a co-equal lever; known (the count) / unknown (the cause); answered by R, E

### B. Whether and how instruction quality can be observed or measured
- B1 What outcome stands for "good work": first-pass review rate, number of rounds, blocking findings, defects found later, owner corrections, or cost? — Each role file already names measures, for example "First-pass review yield; defects found after delivery" (builder.md:46-47), "Plan review first-pass rate" (definer.md:46-47) and "Catch rate on seeded defects" (reviewer.md:42-43) [A]. Decides the measure; known (named) / unknown (whether any is compiled); answered by O, R
- B2 What baseline counts, including "leave everything as it is"? — The rulebook makes every rule "an experiment with a target, a measure and a kill criterion" (OPERATING_MODEL.md:425-426). Targets are set "once real projects give a baseline" (:422-423) [A]. Decides whether no-change is a registered arm; known (the rule) / unknown (the baseline); answered by O, E
- B3 How do we tell a real improvement from run-to-run variation when runs number in the tens? — Vendor guidance: report standard errors, cluster them where items are related, compare paired differences on the same items, and run power analysis (anthropic.com/research/statistical-approach-to-model-evals, 2024-11-19). It also says to run multiple trials, because "model outputs vary between runs" (anthropic.com/engineering/demystifying-evals-for-ai-agents, 2026-01-09) [B]. Decides the experiment design and its size; known (methods) / unknown (the sizes needed here); answered by R
- B4 Can past tasks be replayed under a new instruction version, giving a paired comparison on the same inputs? — Script-dispatched sessions record the source commit, the pack's file hashes and the brief text (reviews/Q-001/_control/0-62b8dda7dcf2.json:3, :53-58, :168) [A]. That may make replay possible. Decides whether a replay harness is the method; known (records exist) / unknown (whether replay is faithful); answered by E
- B5 How do repeated trials fit the rule "No re-running for a better answer" (OPERATING_MODEL.md:299)? — Measuring variance needs repeated runs, and the rule forbids re-running for a better result [A]. Decides whether repeats must be pre-registered as part of the method; known (the rule) / unknown (the reconciliation); answered by O
- B6 Who reads the session transcripts, and how often? — Vendor guidance: "You won't know if your graders are working well unless you read the transcripts" (demystifying-evals, 2026-01-09) [B]. Decides the reading effort and who does it; unknown; answered by O, R
- B7 Can an outcome be graded on what was produced rather than on the steps taken? — The same vendor page advises grading the outcome an agent produced rather than the path it took (paraphrase; demystifying-evals, 2026-01-09) [B]. Decides the grading form; known (the claim) / unknown (here); answered by R

### C. Recording instruction versions, tying them to work, rolling back
- C1 Is the instruction version tied to each piece of work? — **Scripted path:** yes. The control record holds the brief text verbatim, the agent file's SHA-256, the model, the CLI version and the source commit (reviews/Q-001/_control/0-62b8dda7dcf2.json:3, :15, :54-55, :60, :168) [A]. **Dispatch log, dispatch lines:** action, gate, item, role, route, spec, stage, time and trigger. **Dispatch log, outcome lines:** item, role, session, time, trigger, result, verdict and record. Both kinds also carry a hash link (prev). A search for "model" or "brief" in dispatch-log/2026-10.jsonl finds 0 matches, so no line names the model or the instruction version (dispatch-log/2026-10.jsonl:5-15) [A]. Decides whether linking needs building; known; answered by —
- C2 Is the brief recorded for sessions started from a conversation rather than by the script? — docs/briefs/README.md says "One file per builder dispatch … It's the record of what the agent was told". The folder holds only that README (glob, 2026-11-01). The Chief of Staff's session file records each helper's role and times, but no brief text or model. Token figures are null on 10 of its 15 helper lines (sessions/chief-of-staff/session_012RJ…jsonl:2-16) [A]. Most build and review rounds may lack a brief record. Decides whether a baseline is possible from history; known; answered by —
- C3 What share of Service-Desk work ran through each path? — The dispatch log names S-001 on 12 lines, all for P-001 between 2026-10-05 and 2026-10-06 (dispatch-log/2026-10.jsonl:171-189). Later rounds (M3B, 2026-10-26 to 2026-10-29) are filed under reviews/ only [A]. Decides which history is usable; known (partly) / unknown (shares); answered by R
- C4 Which version label governs a session? — The rulebook header says v3.0.0 (OPERATING_MODEL.md:1). critic.md refers to "model 3.4.0" (:14). Service-Desk records 3.6.0 (governance/OPERATING_MODEL_VERSION) [A]. Decides a single version key for instructions; known; answered by O, R
- C5 How is an instruction change rolled back, and who may do it? — BRIEFS.toml says "Changing this file is a rule change (R3)" (BRIEFS.toml:2). R3 changes are the owner's (OPERATING_MODEL.md:66). Rule changes are never delegable (:97-98) [A]. Whether agent-file edits are also R3 is not stated in what I read. Decides the rollback path and its cost in owner time; known (briefs) / unknown (agent files); answered by O

### D. By kind of task, and for checker findings on failed work
- D1 Do research, definition, build, review, triage and owner-question tasks respond differently to instruction changes? — The checks differ by type: Source checker, Critic plan review, locked checks plus Reviewer, Triage, and the Critic reading decision cards (OPERATING_MODEL.md:311-316, critic.md:12) [A]. Decides which task kind to try first; known (structure) / unknown (response); answered by R, E
- D2 Are the findings a checker hands back written so the next round can act on them? — The revise routes are one-line pointers to the findings file, for example "Revise specs/{spec}.md: reviews/{spec}/plan.md holds the plan review's findings" (BRIEFS.toml:22, :28, :30). The findings' own form is the checker's (checker_return, BRIEFS.toml:13) [A]. Decides whether the finding format is a lever; known (form) / unknown (effect); answered by E
- D3 Do failed rounds converge or oscillate? For example, does a fix create a new finding? — In M3B, round 1 lists five blocking findings (r1, about :20-:50) and round 14 passed (r14:7) [A]. The path between is unread. Decides the stop-rule and finding-format work; unknown; answered by R
- D4 How are questions put to the owner instructed and judged? — Seven-part card, Critic reads it "cold" (OPERATING_MODEL.md:69-73) [A]. Decides whether owner-question instructions are in scope; known (rule) / unknown (quality); answered by O

### E. How the standing role file and the per-task brief interact
- E1 Where does the task-specific "what, to what standard, from which inputs" actually live? — In the scripted path the brief is a fixed one-line route template, for example `ready-dispatch = "Do your role's duties for this item, as your agent file describes."` (BRIEFS.toml:17). It must hold no content copied from work products (:1-2). The standard lives in the spec or question in the pack (PACKS.toml) [A]. In the conversational path the brief is free text (specs/_TEMPLATE.md:34-37) [A]. Decides which of the three (role file, brief, pack) is the object of change; known; answered by —
- E2 What happens when a role file and a brief conflict, and which wins? — No precedence rule found in the files read. Decides whether a precedence rule is needed; unknown; answered by O, R
- E3 Does a fixed brief header conflict with role duties? — The header says "Work only from the files in this folder" (BRIEFS.toml:9), while research needs the web and builders need the repository [A]. Decides whether the header is reworded per role; known (wording) / unknown (effect); answered by R
- E4 Should rules learned in one project go into the shared role file, a project brief, or the pack? — Decides where accretion lands; unknown; answered by O

### F. Whether instructions carry over when the model behind a role changes
- F1 How much do instructions written for one model lose on another? — Reported: prompts tuned for one model often do worse on another ("model drifting", PromptBridge 2025, via https://awesomepapers.io/papers/wang2025promptbridge, search result). The specific percentages found in blogs could not be traced to a paper. Decides whether instructions are versioned per model; assumed (reported, not opened); answered by R, E
- F2 Does the pipeline record which model ran each session? — In the scripted path, yes (control record :60, "model": "claude-sonnet-5-5") [A]. In the conversational path, no (C2) [A]. Rules name models only by requirement (builder.md:44; OPERATING_MODEL.md:254) [A]. Decides whether model changes can be detected afterwards; known; answered by —
- F3 Does the model-diversity rule interact with this? — Every checker must run on a different model from what it checks (OPERATING_MODEL.md:251-253) [A]. A change of model for one role can force changes in others. Decides the scope of any model-portability test; known (rule) / unknown (effect); answered by R
- F4 Can a fixed set of tasks double as a check when a model changes? — Vendor guidance: "Evals also shape how quickly you can adopt new models" (demystifying-evals, 2026-01-09) [B]. Decides whether a regression set is a deliverable; known (claim) / unknown (here); answered by O, E

### G. Cost in agent runs and money
- G1 What does one session cost? — Reported reviewer helper sizes range from 56,509 to 213,771 tokens (session_012RJ…jsonl:11-16). Most figures are null (C2). The usage object holds `cost_usd_estimate: null` (:17) [A]. Decides the experiment budget; known (partial) / unknown (cost); answered by R
- G2 How many trials per arm does a detectable effect need, and what does that cost? — Depends on B3; decides feasibility; unknown; answered by R, E
- G3 Is there a spend ceiling for research or measurement sub-projects? — The research sub-project cost limit is **[open]** (OPERATING_MODEL.md:96). Each sub-project has its own budget and counts toward the cap (:190-192) [A]. Decides scale; known (open); answered by O
- G4 Do per-session limits (50 turns, 30 minutes) cut off work and confound results? — See the control record :43-59 [A]. Decides whether limits are held fixed across arms; known (limits) / unknown (effect); answered by R

### H. Owner's time and the owner's decisions
- H1 How much owner time is available, and for what: setting the measure, approving changes, reading results? — Discovery's time limit is **[open]** (OPERATING_MODEL.md:114). The priority order puts the owner's attention above speed and cost (:35-36) [A]. Decides which approach is affordable; unknown; answered by O
- H2 Which decisions are only the owner's? — Rule changes (R3, including brief templates), value targets, success criteria and kills are never delegable (OPERATING_MODEL.md:66, :97-98; BRIEFS.toml:2) [A]. Decides the approval load of any change cadence; known; answered by —
- H3 Should agent-file changes be treated like brief templates (owner approval) or delegated within limits? — Decides speed of iteration; unknown; answered by O

### I. Interaction with existing reviews and checks
- I1 If the checkers' instructions change, does the measure of the doers stop meaning the same thing? — Checkers are themselves role files (reviewer.md, critic.md) [A]. Decides whether doer and checker instructions are ever changed together; known (structure) / unknown (effect); answered by O, E
- I2 Do checkers' verdicts count as ground truth, or is there an independent reading? — Reviewer measure: "Catch rate on seeded defects" (reviewer.md:42-43). Hidden holdouts exist for builds (OPERATING_MODEL.md:324-325) [A]. Decides whether seeded defects or holdouts anchor the measure; known (tools exist) / unknown (whether run); answered by R, E
- I3 How does the stop rule (three plan rounds, three build rounds, OPERATING_MODEL.md:203-206) interact with round counts used as a measure? — The scripted path dispatched Triage after a third plan FAIL (dispatch-log:180-189). M3B's records run to round 14 [A]. How the M3B rounds were counted is not established. Decides whether "rounds" is a valid measure; known (records) / unknown (counting); answered by R
- I4 Can a model judge work from its own model family fairly? — Reported: LLM evaluators recognise and favour their own outputs (Panickssery, Bowman, Feng, NeurIPS 2024, https://arxiv.org/abs/2404.13076, search result). The pipeline already requires different models (F3). Decides who grades any experiment; assumed (reported, not opened); answered by R

### J. Risks of changing instructions in response to single failures
- J1 Do role files grow with each fix? — The critic file's Duties (critic.md:12-20) are written as long paragraphs. By the Source checker's count, :14 is 1,272 characters and :18 is 1,957. The Duties cite model S-032 at :14 and :20, and :14 carries an exception for lines approved "before the project took model 3.4.0", a rule dated to a later model version. The ruling cited under May read is L-0119 (:31) [A]. Vendor guidance advises against stuffing "a laundry list of edge cases into a prompt" (effective-context-engineering, 2025-09-29) [B]. How fast role files have grown across versions is not established from what I read. Decides a growth limit or retirement rule; known (current length and citations) / unknown (growth rate); answered by O, R
- J2 Do accumulated rules conflict with one another? — See E2 and E3; also rule ecology in organisations, where new rules prompt changes in related rules (March, Schulz & Zhou, *The Dynamics of Rules*, Stanford UP 2000, via https://www.sup.org/books/cite/?id=388, search result). Decides whether a conflict check is built; assumed (reported, not opened) for the literature / unknown here; answered by R
- J3 Does tuning instructions to pass the checks drift away from the goal? — Specification gaming: meeting the literal specification without the intended outcome (DeepMind, 2020-04-21, https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/, search result). Decides whether held-out tasks or outcome measures are required; assumed (reported, not opened); answered by R
- J4 Is a single failure evidence of an instruction fault, or of noise? — See A4 and B3. Decides the threshold for making a change; unknown; answered by E
- J5 Does the "rule of two" or the generalisation gate (OPERATING_MODEL.md:426) already govern this? — Decides whether new process is needed; known (named) / unknown (content: v2.5.1 text not read); answered by R

### K. What other fields learned about written handover instructions
- K1 Structured handover between shifts in medicine. — Reported: a structured handover bundle (I-PASS) went with a 23% fall in medical errors in nine hospitals. It was a before-after study with no concurrent control, its authors hold a stake in the method, and it came with training and tools beyond the written form (Starmer et al., NEJM 2014, via https://psnet.ahrq.gov/resources/resource/28485 and https://hms.harvard.edu/news/improved-hospital-handoffs-cut-adverse-events-almost-half, search results). Suggests the written form may help only as part of a bundle; assumed (reported, not opened); answered by R
- K2 Checklists that helped, and the same checklist that did not. — Reported: deaths fell from 1.5% to 0.8% after a 19-item surgical checklist in eight hospitals (Haynes et al., NEJM 2009, via https://pmc.ncbi.nlm.nih.gov/articles/PMC2810011, search result). A province-wide mandated rollout across 101 hospitals found no significant change. The accompanying editorial suggested the checklist was not actually used (Urbach et al., NEJM 2014, via https://www.fiercehealthcare.com/healthcare/surgical-safety-checklists-may-not-improve-patient-outcomes-after-all, search result). Shows compliance and context, not the text alone, carry the effect; assumed (reported, not opened); answered by R
- K3 Intent-based orders versus detailed procedure (military orders, aviation procedures, "work as imagined versus work as done"). — Not searched in this pass; unknown; answered by R
- K4 How organisations retire rules, not only add them. — See J2; unknown; answered by R

### L. (added) Records needed before anything can be measured
- L1 Are the existing review records complete and consistent enough to serve as a baseline? — 149 review-round files in reviews/ (names matching `_*verbatim*.md`) contain a line starting `Verdict: FAIL` (search, 2026-11-01) [A]. Their naming varies (`_plan-review-r1`, `_plan-review-round1`, `_stage-…`, `_build-1a-…`). The verdict rule is the first column-0 `Verdict:` line (reviews/README.md:10-18) [A]. Decides whether a baseline can be mined or must be collected fresh; known (volume, naming) / unknown (completeness); answered by R
- L2 Should the conversational path record its briefs, model and usage the way the script does? — See C2 and F2. Decides a records change, which is itself a rule change; unknown; answered by O

### M. (added) Blindness and isolation when instructions change
- M1 Could an instruction change break the rules on what each role must not see? — Packs keep, for example, the hoped-for answer from the Researcher and holdouts from the Builder (PACKS.toml:17-26, :66-72) [A]. A brief that quotes content would break this, which is why briefs hold ids only (BRIEFS.toml:1-2) [A]. Free-text briefs are not under that check (E1). Decides whether free-text briefs need the same check; known (rules) / unknown (compliance); answered by R
- M2 Do sessions treat handed-over text as data rather than instructions? — The brief header says so (BRIEFS.toml:9) [A]. Untrusted text is read only by the Input reader (OPERATING_MODEL.md:240-242) [A]. Decides whether instruction experiments must include adversarial inputs; known (rule) / unknown (effect); answered by R

## Owner shortlist
1. If this work succeeds, what should be better for you: fewer rounds of rework, fewer problems reaching you, less of your time, or lower running cost? Pick one to come first.
2. Is "leave the instructions as they are" an acceptable result, if testing shows changes don't help?
3. Should every change to an agent's standing instructions need your approval, as changes to brief templates already do, or may the team change them within limits you set?
4. How much are you willing to spend on testing instruction changes, in money or number of agent runs, for this project?
5. About how much of your time per week can this take, and for what: choosing the measure, approving changes, or reading results?
6. When an agent works for you inside a conversation rather than through the automatic pipeline, should it keep the same full record of what it was told and which model ran it, even if that is slower?
7. Should the instructions be expected to keep working when the model behind a role is changed, or is it fine to re-tune them each time?
8. Which kind of work frustrates you most today: research, writing specs, building, reviewing, tracing failures, or the questions put to you?

## Research shortlist
1. In multi-step pipelines of language-model agents, how much of the variation in output quality is attributable to instruction wording, compared with the model, the size and quality of the inputs, how the task is divided, and the checks applied? — decision: whether instructions are the lever this project targets, and which other levers enter scope; depth: 3
2. What methods detect a real change in agent-pipeline outcomes when only tens of runs are affordable (paired comparisons on replayed tasks, repeated trials, clustered errors, power analysis), what sample sizes do they need, and how do they handle a rule against re-running for a better result? — decision: whether measurement is feasible within budget, and the experiment's design and baseline; depth: 3
3. How well do written instructions carry over when the language model behind a role is replaced, and which practices reduce any loss? — decision: whether instructions are versioned per model and whether a fixed task set is kept for model changes; depth: 3
4. In fields that hand work between people or teams through written instructions (clinical handover, surgical and aviation checklists, military orders, software runbooks), under what conditions did written procedures improve outcomes, show no effect or cause harm, and how was the growth and retirement of rules managed? — decision: which transferable conditions and design limits shape scope; depth: 3
5. What do the Service-Desk records (reviews/, dispatch-log/, session files, control records) show about rounds per item, first-pass rates and kinds of findings by task type, and are they complete enough to serve as a baseline? — decision: whether a baseline can be drawn from history or must be collected fresh; depth: 3

## Design traps to avoid
- **Blaming the wording for what the inputs or the split caused.** A 22,883-line spec and 14-round reviews may reflect input size and task division, not instructions. (A1, A2, A7)
- **Measuring doers with checkers whose own instructions are changing.** The measure moves with the treatment. (I1)
- **Before-after comparisons across different tasks, models or versions.** Without paired replays on the same inputs, a change of model or task masquerades as an instruction effect. (B4, F2, C4)
- **Building a baseline only from the scripted path.** It records the brief, model and file hashes, but much of the work ran through conversations that recorded neither the brief nor the model. (C1–C3, L1)
- **Fixing after each failure.** This risks role-file growth and rule conflicts, and published guidance warns against edge-case lists. The critic file's duties already run to paragraphs of over a thousand characters, one carrying an exception dated to a later model version. Whether that came from fixes after failures is not established. (J1, J2, J4)
- **Fitting instructions to pass the checks rather than to reach the goal.** (J3; keep held-out tasks or outcome measures, I2)
- **Repeated trials that break the no-re-run rule** unless the repeats are pre-registered as the method. (B5)
- **Grading with the same model family that did the work.** (I4, F3)
- **Treating "rounds to pass" as a clean measure** while the stop rule's counting is unclear. (I3)
- **Free-text briefs that leak the hoped-for answer or protected content** into blind roles. (M1)
- **Changing rules faster than the owner can approve them.** Brief templates are R3 and never delegable. (C5, H2, H3)

## Gaps found in existing questions or plans
- **Q-001 (this question)**, gaps found while mapping:
  - It does not name the two ways sessions are started (scripted and conversational), or that they keep different records (C1–C3).
  - It does not name the inputs and pack size as a factor separate from instructions (A2).
  - It does not name the version-label mismatch between rulebook, template and project (C4).
  - It does not name the conflict between repeated trials and the no-re-run rule (B5).
  - It does not name blindness and isolation as something instruction changes can break (M1, M2).
  - It names checker findings, but not changes to the checkers' own instructions (I1).
- **docs/briefs/README.md in Service-Desk** says each builder dispatch's brief is filed there. The folder holds only the README (C2).
- **Network access for the Source checker:** arxiv.org and pubmed.ncbi.nlm.nih.gov were unreachable from this session. Every literature item above is marked assumed until a session with those domains allowed opens it.

**Sources opened (web, untrusted text, reported as claims):**
- https://www.anthropic.com/research/statistical-approach-to-model-evals (2024-11-19)
- https://anthropic.com/engineering/demystifying-evals-for-ai-agents (2026-01-09)
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (2025-09-29)

**Seen only in search results, not opened:**
- https://arxiv.org/abs/2310.11324
- https://arxiv.org/abs/2507.11538
- https://arxiv.org/abs/2503.13657
- https://arxiv.org/abs/2404.13076
- https://awesomepapers.io/papers/wang2025promptbridge
- https://psnet.ahrq.gov/resources/resource/28485
- https://hms.harvard.edu/news/improved-hospital-handoffs-cut-adverse-events-almost-half
- https://pmc.ncbi.nlm.nih.gov/articles/PMC2810011
- https://www.fiercehealthcare.com/healthcare/surgical-safety-checklists-may-not-improve-patient-outcomes-after-all
- https://www.sup.org/books/cite/?id=388
- https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/
