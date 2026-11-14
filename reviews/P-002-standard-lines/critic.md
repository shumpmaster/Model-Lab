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

---

# The Critic on the five reworded lines, verbatim

*Brief 347 (docs/briefs/347-critic.md), at Model-Lab 2497728; a fresh session. Recorded verbatim by the Orchestrator, 2026-11-14. Note on the order (the Critic's open question): the five rewordings were committed on the session's branch (60af4b0) before this check, not on the default branch; section 3 asks for the check before a reworded line is committed, so that order was not kept, and this record says so.*

Verdict: PASS

I checked the five standard lines the Chief of Staff reworded after the last check. All five now fix what that check found. Build-4 no longer holds the Build gate until every trial the screening ever runs is finished. It now covers only the first trials. Launch-4 says "may fall after", as the record does, and "by the Launch gate". Launch-3 says the repository is archived only once the prompt engine's results are in too. Launch-5 now gives the reason the screening must leave the desk and run on its own. Build-5 says the desk takes part only once it is ready to keep your confirmation. Each why is still plain, about this project, and true of the records I could read. Two small wording points remain, and neither blocks. Launch-3 says "this repository's results" where it means this project's, so "too" reads oddly. Launch-5 says the repository "is archived" when that has not happened yet. Nothing here is irreversible, and you rule all five with the Build gate. One flag: the new Build-4 wording is the text the earlier Critic check proposed, so here I am judging that check's own fix (noted below).

**Each line, quoted whole** (docs/projects/P-002.md)

- :134 `- Build-4 (standard) · taken on · why: each of the first methods the owner lets through (M13) is a registered trial, and each must end with a recorded result and the owner's ruling on its results card before anything enters the operating model`. Finding 1 of brief 345 is fixed. The line now covers M13's trials, "up to the number the stop rule sets before its summary" (:138; E-004 Step 7, P4, :96), not every later trial. The form is right, and the line is about this project and plain. It is true of the records. Each trial is a frozen copy of E-004 (E-004:8). A results card comes after a trial is "judged, or stopped, or voided" (E-004:99), so every trial does end with a recorded result. A method enters the model only after its results card (E-004:108, T13 and T17). It matches the model's Build-4, "each registered experiment has a recorded result" (v3_checks.py:554). "(M13)" comes after the words it supports, as a cross-reference, which is allowed.
- :135 `- Build-5 (standard) · taken on · why: the count, the touch log, the draw, each trial's log, the owner's confirmation on the desk, once the desk is ready to keep it, and the reading rounds must work together on real merged work, not one at a time`. Finding 5 is fixed. It agrees with E-004 Step 0 (:30), where no trial starts until the desk can keep the owner's answer, and with S-002, "Needed outside this spec's lane" (:274), where that record is filed in the Service Desk as new work. Form right, about this project, plain, true.
- :144 `- Launch-3 (standard) · taken on · why: the owner ruled that this repository's results move into the operating model repository, after which, once the prompt engine's are in too, this repository is archived`. Finding 3 is fixed. It is true: P-001-work-repo.md:1 says "Model-Lab is archived once both are in", and :13 says "once both are in, the work repo is archived". Form right, about this project. See finding 1 for a small wording point.
- :145 `- Launch-4 (standard) · taken on · why: the target is checked 12 months after the first trial starts, which may fall after this project leaves the desk, so the count and its status updates must be running and reporting on their own by the Launch gate`. Finding 2 is fixed. "May fall after" matches :104, and "by the Launch gate" matches the model's "confirmed running at, or just before, the Launch gate" (v3_checks.py:559 to :561). The status updates are P17 (:176), and the 12-month check is V1 (:192). Form right, about this project, plain, true. M15's approved why (:147) still says "likely". It is not one of the five lines, and changing it would be a rewording that needs its own check. That is not a finding here.
- :146 `- Launch-5 (standard) · taken on · why: the screening must leave the desk and run on its own, since this repository is archived, and the hand check found the first counting rules wrong in four places and the Critic flagged its own earlier misses, so those lessons must be recorded at handover for the operating model to correct`. Finding 4 is fixed. The why now covers both parts of the model's Launch-5, leaving the desk to own its running and recording the lessons at handover (v3_checks.py:562 to :564). The new clause is true: the archiving is at P-001-work-repo.md:1, and M15 at :147 needs "nothing needed from this repository". The two facts about the lessons are unchanged from the line brief 345 checked against the handoff and reviews/S-002/plan.md. Those files are not in my manifest, so I rely on that check for them. Form right, about this project, plain. See finding 2.

The other five lines (:131, :132, :133, :142, :143) are word for word as brief 345 quoted them. No reason contains ` · `. No why was removed, only changed, as section 3 allows (:94).

**Findings**

1. Not blocking. docs/projects/P-002.md:144 (Launch-3). "This repository's results" covers both projects' results, so "once the prompt engine's are in too" reads as if the prompt engine's results were not among them. The ruling speaks of each project's result (P-001-work-repo.md:1, "each result moves fully into the operating model repository"). Fix: "the owner ruled that this project's results move into the operating model repository, after which, once the prompt engine's are in too, this repository is archived".
2. Not blocking. docs/projects/P-002.md:146 (Launch-5). "Since this repository is archived" states as a fact something still to come. Model-Lab is temporary and is archived only once both results are in (AGENTS.md:46 to :49). Fix: "since this repository will be archived".

**Self-implication (D-050):** flagged. The new Build-4 wording is the fix that the Critic's own earlier check proposed, nearly word for word (reviews/P-002-standard-lines/critic.md, finding 1: "each of the first methods the owner lets through (M13) is a registered trial, and each must end with …"). So here the Critic role is judging its own earlier suggestion. This session is fresh and has not checked these lines before. I checked the new wording against E-004 and v3_checks.py, not against that suggestion, and found it sound. Brief 345's open question still stands, and it is for the owner: should Build-4 cover only the first trials, or should the Build gate pass with Build-4 not reached? This wording takes the first answer.

**Six-part contract**
- Changed: nothing. I hold no write tool.
- Why: brief 347 asked for the Critic's check of the five standard lines reworded after brief 345's findings, before they are committed (section 3, :94; model S-032).
- Verified: I compared each line with brief 345's quote and its finding, then checked each why against the model's standard milestone text (v3_checks.py:549 to :565), section 3's form rule (:94), the facts in P-002 (:104, :138, :147, :176, :192), E-004 (:8, :30, :96, :99, :108), S-002 "Needed outside this spec's lane" (:274) and P-001-work-repo.md (:1, :13). I checked that the five unchanged lines match brief 345's quotes, and I checked every reason for ` · `.
- Undone: I did not re-check Launch-5's unchanged facts (the four wrong rules, the Critic's own flags) against the handoff or reviews/S-002/plan.md, because neither is in my manifest. I rely on brief 345's check of them. I could not see whether the reworded lines are already committed to the default branch, since this is not a git checkout.
- Needed outside my surface: the Orchestrator records this return verbatim under brief 345's record in reviews/P-002-standard-lines/critic.md. The Chief of Staff decides whether to take up findings 1 and 2. Either rewording needs the Critic's check again (:94).
- Open questions: section 3 (:94) asks for a reworded line's check "before it is committed". If these rewordings are already on the default branch at the start commit, that order was not kept. The Orchestrator can confirm it from the branch history. Brief 345's Build-4 question is still for the owner at the gate.

**Files read**
- /home/user/Model-Lab/docs/briefs/347-critic.md
- /home/user/Model-Lab/.claude/agents/critic.md
- /home/user/Model-Lab/AGENTS.md
- /home/user/Model-Lab/docs/projects/P-002.md
- /home/user/Model-Lab/reviews/P-002-standard-lines/critic.md
- /home/user/Model-Lab/experiments/E-004.md
- /home/user/Model-Lab/specs/S-002.md (only the "Needed outside this spec's lane" section and the lines near it, by search)
- /home/user/Model-Lab/decisions/questions/P-001-work-repo.md
- /home/user/Model-Lab/governance/checks/v3_checks.py (lines 545 to 569)

## Recheck of Launch-3 and Launch-5 on brief 347's two wording points, before commit (brief 352, Check 2)

*A fresh session, at Model-Lab f206b5c, on the proposed lines given as a diff, not yet committed. Recorded verbatim by the Orchestrator, session session_01QBwHGJ2r2y9re3AuyKDzEi, 2026-11-14. The same return also held Check 1, recorded in reviews/S-002/plan.md; the one six-part contract is copied in both records.*

**Check 2: standard-line check of the two reworded lines in launch-lines.diff (docs/projects/P-002.md:144 and :146, not yet committed)**

Verdict: PASS

Both rewordings fix what brief 347 found. Launch-3 now says "this project's results", so "once the prompt engine's are in too" reads correctly. Launch-5 now says the repository "will be archived", not that it is. Each line keeps the standard form. Each why is plain, about this project, and true of the records I could read. The check comes before the lines are committed, which is the order section 3 asks for. I have no findings.

- :144 `- Launch-3 (standard) · taken on · why: the owner ruled that this project's results move into the operating model repository, after which, once the prompt engine's are in too, this repository is archived`. Brief 347's finding 1 is fixed. It is true: decisions/questions/P-001-work-repo.md:1 says "each result moves fully into the operating model repository, and Model-Lab is archived once both are in", and :13 says "once both are in, the work repo is archived". The form is right, it is about this project and it is plain. No ` · ` appears inside the reason.
- :146 `- Launch-5 (standard) · taken on · why: the screening must leave the desk and run on its own, since this repository will be archived, and the hand check found the first counting rules wrong in four places and the Critic flagged its own earlier misses, so those lessons must be recorded at handover for the operating model to correct`. Brief 347's finding 2 is fixed. The future tense matches AGENTS.md:46 to :49 ("This repository is temporary … it is archived once both are in") and P-001-work-repo.md:1. The rest of the line is word for word what brief 347 checked. The form is right, it is about this project and it is plain. No ` · ` appears inside the reason.

Self-implication (D-050): flagged. Both rewordings take brief 347's suggested words exactly, so the Critic role is again judging its own earlier fix. This session is fresh and has not checked these lines before. I judged them against P-001-work-repo.md and AGENTS.md. Launch-5's two facts about the lessons (the four wrong rules, and the Critic's own flags) are unchanged. I rely on brief 345's check of them, since their sources are not in my manifest.

**Six-part contract** (one for both checks)
- **Changed (by file):** nothing. I hold no write tool.
- **Why:** brief 352 asks, before the Build gate's ruling, for two things. First, a plan review of brief 351's change to S-002 (D-043). Second, the standard-line check of the reworded Launch-3 and Launch-5 (critic charter, last duty; P-002 section 3).
- **Verified:** by reading and searching only, with no shell.
  - I read both diffs in full and compared each changed line before and after.
  - At :46 the only changes are "for which plan a question asks about, … with the briefs and specs its trailers give" and "nor narrow".
  - At :109 the only changes are "For which plan a question asks about, … with the briefs and specs its trailers give" and "So" replaced by "Under that first ruling,".
  - At :197 the only changes are "for which plan a question asks about, … with the briefs and specs its trailers give".
  - The owner's words, the date, f71cbca, d231a51, the intake paths and "14 of 33" are unchanged in each version.
  - I searched S-002 for "work the piece carries", "piece's work" and "whose work it carries". The trailer readings at :46 and :109 now agree with the limited clause. The general form is left only at :271, and at :270, where it describes the re-read.
  - The quoted range in step 4 runs from :18 to :105–107, so :46 is quoted to the Researcher and :271 is not.
  - Decision records: P-002-check-named-by-statement.md:1, :9 and :12; P-001-work-repo.md:1 and :13.
- **Undone:**
  - I could not run a word-level diff without a shell. My comparison of the long lines is by reading, helped by searches.
  - I did not read research/Q-018-memo-5.md or reviews/Q-018-later-work/_critic-reread-verbatim.md, which are not in my manifest. So I did not confirm that #25's `Spec:` trailers do not give S-023. My judgement that "with the briefs and specs its trailers give" changes no code rests on that reading already standing in step 3 when the codes were made and checked.
  - I did not re-check Launch-5's unchanged facts about the lessons.
- **Needed outside my surface:** the Orchestrator records Check 1 verbatim in reviews/S-002/plan.md, and Check 2 under brief 347's record in reviews/P-002-standard-lines/critic.md. The Chief of Staff may commit the two Launch lines as checked. The Definer, if dispatched, may take up Check 1's findings 1 and 2. Neither is needed before the freeze or the gate.
- **Open questions:** whether S-002 is frozen before the next pass. If it is, Check 1's finding 1 needs a superseding entry rather than an edit (AGENTS.md §1). That is for the Orchestrator.

**Files read**
- /home/user/Model-Lab/AGENTS.md
- /home/user/Model-Lab/.claude/agents/critic.md
- /home/user/Model-Lab/docs/briefs/352-critic.md
- /tmp/claude-0/-home-user/93707dce-1a9e-58fe-b386-0565a8518ddc/scratchpad/before-352/s002-change.diff
- /tmp/claude-0/-home-user/93707dce-1a9e-58fe-b386-0565a8518ddc/scratchpad/before-352/launch-lines.diff
- /home/user/Model-Lab/docs/briefs/351-definer.md
- /home/user/Model-Lab/decisions/questions/P-002-check-named-by-statement.md
- /home/user/Model-Lab/reviews/S-002/plan.md (headings, then from :765 "## Check of the lines changed by brief 348" to the end)
- /home/user/Model-Lab/specs/S-002.md (:244 to :275, plus searches of the whole file)
- /home/user/Model-Lab/docs/projects/P-002.md (by search: lines 19, 96, 141 to 147, 254, 274)
- /home/user/Model-Lab/reviews/P-002-standard-lines/critic.md
- /home/user/Model-Lab/decisions/questions/P-001-work-repo.md
