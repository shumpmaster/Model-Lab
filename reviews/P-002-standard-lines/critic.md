# The Critic on P-002's Build and Launch standard lines, verbatim

*Brief 345 (docs/briefs/345-critic.md), at Model-Lab 6989282; a fresh session. Recorded verbatim by the Orchestrator, 2026-11-14.*

Verdict: PASS

I checked the ten Build and Launch standard lines the Chief of Staff added to the screening project's plan. All ten are in the right form, all say taken on, and each why says in plain words why this project needs that step. I found no false fact. Each fact matches the records: the Check author writes the locked checks before the count is built, the Reviewer tries to break the count, the reading briefs are refused if they hold names, outside code runs only in a closed place, results come to you on a results card, the hand-over and archiving were your ruling, the 12-month check, the hand check finding four rules wrong, and the Critic flagging its own misses. Five points are worth a small rewording, but none blocks. The one most worth fixing is Build-4: as written, it would hold the Build gate until every trial the screening ever runs has finished. Nothing here is irreversible. You rule all ten lines with the Build gate.

**Each line, quoted whole** (docs/projects/P-002.md)

- :131 `- Build-1 (standard) · taken on · why: the count decides the target and the draw decides which side each trial piece falls on, so their checks must be written by the Check author from the frozen plan before either is built`. Form right. The why is about this project and plain. True: section 4 (:157) says the Check author writes the locked checks "before the count is built", and S-002:281 says the same. The draw script is `src/E-004/draw.py` (E-004:19, :68).
- :132 `- Build-2 (standard) · taken on · why: the count's and the draw's scripts, the check on reading briefs and the closed place for outside code must be built to the frozen plan before anything is counted, drawn or tried`. Form right, about this project, plain. True: E-004:19 names the scripts. S-002 AC19 (:184) has a brief holding names "refused before it is sent". S-002:158 to :160 describe the place, and section 4 (:162) says the Builder sets it up.
- :133 `- Build-3 (standard) · taken on · why: a wrong count would misreport the target and a steerable draw would spoil every trial, so a reviewer must try to break both before either is trusted`. Form right, about this project, plain. True: section 4 (:158) says "the Reviewer tries to break it before it is trusted", and E-004:20 has the Reviewer re-derive every draw.
- :134 `- Build-4 (standard) · taken on · why: each method the owner lets through is a registered trial, and each must end with a recorded result and the owner's ruling on its results card before anything enters the operating model`. Form right, about this project, plain. True: E-004:8 (each trial gets a frozen record copied from E-004), Step 8 (:99, T13) and :108 (T17). See finding 1.
- :135 `- Build-5 (standard) · taken on · why: the count, the touch log, the draw, each trial's log, the owner's confirmation on the desk and the reading rounds must work together on real merged work, not one at a time`. Form right, about this project, plain. True: E-004 Step 0 (:30) needs the desk's record of your confirmation before any trial starts. E-004 Step 6 (:86) joins the touch log, the trial's log and the desk. S-002 AC16 covers the reading rounds.
- :142 `- Launch-1 (standard) · taken on · why: the count, the feeds and the trial records must run from the operating model repository, since this repository is temporary`. Form right, about this project, plain. True: AGENTS.md:46 to :49 and decisions/questions/P-001-work-repo.md:1. It matches M15 (:147).
- :143 `- Launch-2 (standard) · taken on · why: the operating model repository's own roles must be named to keep the count, the touch log, the reading rounds and the trials going after this project ends`. Form right, about this project, plain. True: section 4 (:167) says that repository's own roles are "Named at the hand-over".
- :144 `- Launch-3 (standard) · taken on · why: the owner ruled that this repository's results move into the operating model repository, after which this repository is archived`. Form right, about this project, plain. True: P-001-work-repo.md:1 and :13 ("each result moves fully into the model repo when done; once both are in, the work repo is archived"). See finding 3.
- :145 `- Launch-4 (standard) · taken on · why: the target is checked 12 months after the first trial starts, likely after this project leaves the desk, so the count and its status updates must run and report on their own before then`. Form right, about this project, plain. True: V1 (:192) and P17 in section 5 (:176). See finding 2.
- :146 `- Launch-5 (standard) · taken on · why: the hand check found the first counting rules wrong in four places and the Critic flagged its own earlier misses, so those lessons must be recorded at handover for the operating model to correct`. Form right, about this project, plain. True: docs/handoff/2026-11-12-chief-of-staff-p002-14.md:7 ("four of the rules give wrong answers"). The Critic's own flags are in reviews/S-002/plan.md:135 and :236, and in the handoff at :13 and :16. See finding 4 and the self-implication note.

The note at :96 matches section 3's rule (:94) that Build's and Launch's lines are written before the Build gate and ruled with it. That holds: S-002 is still `status: draft` (S-002:3). No reason contains ` · `.

**Findings**

1. Not blocking. docs/projects/P-002.md:134 (Build-4). "Each method the owner lets through" covers every trial the screening ever runs. Build-4 means each registered experiment has a recorded result by the Build gate (governance/checks/v3_checks.py:554), and the screening keeps letting methods through after Build (E-004 Step 7, P4, :96). Read literally, Build-4 could never be reached. Fix: narrow it to the trials run in Build, for example "each of the first methods the owner lets through (M13) is a registered trial, and each must end with …".
2. Not blocking. docs/projects/P-002.md:145 (Launch-4). "Likely after this project leaves the desk" is stronger than the record, which says "may fall after the project leaves the desk" (:104). The same "likely" is in M15's approved why (:147). Also, "before then" reads as before the 12-month check, but Launch-4 is confirmed at or just before the Launch gate (v3_checks.py:559 to :561). Fix: "which may fall after this project leaves the desk, so the count and its status updates must be running and reporting on their own by the Launch gate".
3. Not blocking. docs/projects/P-002.md:144 (Launch-3). "After which this repository is archived" leaves out that archiving waits for both projects' results ("once both are in", P-001-work-repo.md:1). Fix: "… after which, once the prompt engine's are in too, this repository is archived".
4. Not blocking. docs/projects/P-002.md:146 (Launch-5). The why covers only the lessons part of Launch-5. It does not say why this project must graduate: leave the desk and own its running, monitoring and review (v3_checks.py:562 to :564). Its facts are true. Fix: add a plain clause, for example "the screening must leave the desk and run on its own, since this repository is archived, and …".
5. Not blocking. docs/projects/P-002.md:135 (Build-5). The desk's record of your confirmation is built in the Service Desk, as new work filed there (S-002, "Needed outside this spec's lane"), not in this project's Build. The line is not false, since the parts must still work together. Fix, optional: say "the owner's confirmation on the desk, once the desk is ready to keep it".

**Self-implication (D-050):** none of my own earlier checks is judged here. This is a fresh session, and I have not checked these lines before. Launch-5's why does rest on earlier Critic sessions missing things (reviews/S-002/plan.md:135, :236; handoff 14 :16). I confirmed only that those flags exist. I did not judge them.

**Six-part contract**
- Changed: nothing. I hold no write tool.
- Why: brief 345 asked for the Critic's check of the ten Build and Launch standard lines before the Build gate (model S-032).
- Verified: I read each line against the model's names for the standard milestones (v3_checks.py:550 to :564), the section 3 form rule (:94) and the records in the manifest, as cited under each line. I searched S-002 for the check on reading briefs, the place for outside code and the Check author. I checked each reason for ` · `.
- Undone: I read S-002 only in part (lines 1 to 85, 150 to 161, the AC list and the section headings). I read reviews/S-002/plan.md lines 1 to 411 of 764. Research/Q-018-memo-5.md holds nothing that bears on these lines beyond the re-coding; it does not contradict Launch-5.
- Needed outside your surface: the Orchestrator records this return verbatim in reviews/P-002-standard-lines/critic.md. The Chief of Staff decides whether to reword lines 134, 144, 145, 146 and 135 before the Build gate. Any rewording needs the Critic's check again (section 3, :94).
- Open questions: should Build-4 cover only the first trials (M13), or should the project expect to pass the Build gate with Build-4 not reached? That is for the owner at the gate.

**Files read**
- /home/user/Model-Lab/docs/briefs/345-critic.md
- /home/user/Model-Lab/docs/projects/P-002.md
- /home/user/Model-Lab/specs/S-002.md (in part)
- /home/user/Model-Lab/experiments/E-004.md
- /home/user/Model-Lab/AGENTS.md
- /home/user/Model-Lab/decisions/questions/P-001-work-repo.md
- /home/user/Model-Lab/research/Q-018-memo-5.md
- /home/user/Model-Lab/reviews/S-002/plan.md (lines 1 to 411)
- /home/user/Model-Lab/docs/handoff/2026-11-12-chief-of-staff-p002-14.md
- /home/user/Model-Lab/governance/checks/v3_checks.py (lines 540 to 574)
- /home/user/Model-Lab/.claude/agents/critic.md (my charter, as given to this session)
