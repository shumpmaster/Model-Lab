Verdict: PASS

The Critic's cold read of questions/P-001-gate-record.md, on a different model from its writer, verbatim (PASS at round 3; its non-blocking findings 6 and 8 were applied after it). Recorded by the orchestrator. Session session_01QBwHGLd77YbwCSMSPU26vW, 2026-11-04.

## Round 1
Verdict: FAIL

The question has one blocking flaw, which is B's cost claim. It is overstated and leaves out a variant that makes B the cheapest option. The rest is non-blocking.

1. **BLOCKING: B's cost claim is wrong as written.**
   - The question says a hand-written status record "could make [the script] start helper sessions or raise cards".
   - The checks only need `spec` to be a string in a `status/P-*.toml` file (`governance/checks/v3_checks.py`, `approved_in`, line 615). The record's `state` is free.
   - `governance/ROUTING.toml` lines 369-376 (route "finished") map `state = ["done","closed"]` to `action = "none"`. `governance/ROUTING.toml` lines 360-367 do the same for "waiting-owner".
   - So a record written in a state the script does nothing with would satisfy the checks and give the script no work. The risk the question describes only exists if the record says "ready".
   - The remaining B costs are real but different: the status README says status files are "written only by the Orchestrator" (`status/README.md` line 3), and a made-up spec or stage could draw anomalies.
   - The owner is steered off B on a premise that is partly false. The question should do three things:
     - say that the script's action depends on the record's state;
     - say whether an inert-state record is workable;
     - name the real costs (breaking "written only by the Orchestrator", a record that misdescribes the project's position, and `note_spec` and `check_status` anomalies if the spec is not real). It should say which of these were verified.
   - The "Reversible" line for B ("anything the script did in between may not be undone") needs the same correction.
   - The recommendation's reason, "without risking the script acting on a false record", rests on this claim. The "what would change it" line, "accept the risk of the script acting", does too.

2. **BLOCKING: the options are not fairly set.** This follows from finding 1 and from the way A is described.
   - Because of finding 1, B is the only route that serves the stated need (mark M1) quickly. The question's own WHY makes that need central.
   - A's gain of "nothing is written that the pipeline's script could act on" is the same advantage an inert-state B record would have, so it does not separate them.
   - A's cost does not say how long it takes. A spec, a builder and a review in the operating-model repository mean M1 stays unmarked for an unstated time, and M2 and the fair test are next. The cost line should say how long and what is held up.
   - A does not say what "carried into this project" involves. The route I could check says the checks would take the ruling record as approval. This is a rule change to a protection mechanism. The question does not say that A would also change the protection that decides when milestones are locked (`v3_checks.py` lines 117-133, the "approved" and "waits on Design gate" tests).

3. **Non-blocking: C's claim is correct but loosely worded.**
   - Verified: `v3_checks.py` lines 146-148 say that while the project is neither approved nor waiting on its Design gate, any reached part is a finding. So C does mean no milestone can be marked.
   - The protections for standard lines and drops are conditioned on "approved or waits on its Design gate" (lines 123-133). C therefore means they do not apply either, which agrees with the question.
   - "Go unprotected" is vague. Say which protections are meant (lines 123-133: a Critic-Check on added or changed standard lines, and an Owner-Ruling on drops). Say what could go wrong in the meantime: unreviewed edits to milestones M1 to M6.
   - C's "your project page shows none reached" is asserted without a cited record.

4. **Non-blocking: the first Context line has no fact behind "the checks read a gate's approval only from a status record".**
   - The citation holds up for `approved_in` (line 615).
   - There is also a second route in the checks: `waiting_on_design_gate` (line 618) accepts a status with `next_gate = "dor"`, and the question does not mention it. Its relevance is that it is also a status-record route, so it does not change the conclusion.
   - The question should still name both, because A's change would have to cover both tests.

5. **Non-blocking: the citation to the Critic's record is to a file that does not exist yet.**
   - "record: reviews/P-001-gate-record/critic.md" under WHO HAS CHECKED IT. `reviews/P-001-gate-record/` does not exist in the worktree.
   - This is expected before the Orchestrator records this verdict. Do not file the question until that record exists and holds a PASS. After a FAIL, the line should also say which round it is.

6. **Non-blocking: the form is mostly followed, but there are some deviations.**
   - The template (`questions/_TEMPLATE.md`) has no "WHO HAS CHECKED IT" line. §2 (OPERATING_MODEL.md lines 69-73) requires the seven parts, including "who has checked it", so the addition is right. The template is the part that is behind.
   - The "Milestone:" line says only M1. §2 asks that the milestone line say which standard milestone place the question serves, and M2 to M6 are affected too (the question says "the fair test and the rest later"). Consider "M1 (and M2 to M6 later)".
   - The template has `DEFAULT: <letter>   TIMEOUT: <hours>`. The question writes "none" for both. That matches the card form's "if the owner doesn't decide" (§2) only if the "none" is explained. It says "a rule change is the owner's ruling", which is enough.
   - The "decision" and "why it's the owner's" parts are both present in WHY. The background Context has 6 lines, and §2 allows at most 5. Fold lines 3 and 6, or accept the overage consciously.

7. **Non-blocking: Plain English first is mostly met, but some terms need glossing for a cold reader.**
   - Undefined or insider terms: "the checks", "status record", "pipeline's script", "helper sessions", "Design-gate ruling", "spec", "tools builder", "the fair test", "M5, M6". WHY opens with "the project's automatic checks" and then "status record" without saying what either is.
   - Add one sentence saying what the checks are for and what the pipeline is, and what "a project run from a conversation" means.
   - The title itself is clear ("how should your gate rulings reach the records the checks read").

8. **Non-blocking: the risk class is probably right, but it is not shown as computed.**
   - R3 and "reversible (A, C); B possibly not" are given. The template says "computed".
   - R3 is plausible: the change is to rule checks. Give the computation, or cite the rule that assigns R3.
   - After correction under finding 1, B's reversibility line may change to "reversible".
   - Blast radius is "every project run from a conversation; this project's milestone marks". This is fair for A. For B it is only this project, and the question should say that.

9. **Non-blocking: the recommendation leans on unstated things.**
   - It relies on finding 1's premise.
   - It also relies on an unstated judgement that the delay is acceptable.
   - It does not say that LL-43's own "Correction proposed" (`/home/user/Model-Lab/docs/LESSONS.md` line 317) offers a third route, "the Orchestrator writes it from the ruling record". That is close to B but done by the script. The question omits it. A fair option set would mention this variant, or say why it is excluded.
   - "Medium confidence" is given without a reason.

10. **Non-blocking: missing for the owner.**
    - A single sentence saying what the owner has to do next under each option, and what happens to the M1 mark under each. For example, under A, the mark is added in a later commit with an `Owner-Ruling:` trailer naming `decisions/questions/P-001-accept-m1.md`. That record already says the mark is added "once that record exists" (line 10), so the owner's earlier ruling stands under any option.
    - Whether the standard Discovery and Design milestone lines (LL-35 and LL-40) are fixed by A. The Context cites them, but no option says whether they are solved. If A does not fix them, say so. The question presents A as serving "every project run from a conversation", which may over-promise.

Records checked:
- `/home/user/wt/ml-ask-gate/questions/P-001-gate-record.md`
- `/home/user/wt/ml-ask-gate/questions/_TEMPLATE.md`
- `/home/user/wt/ml-ask-gate/governance/checks/v3_checks.py` (lines 112-148, 613-622)
- `/home/user/wt/ml-ask-gate/governance/ROUTING.toml` (lines 360-376)
- `/home/user/wt/ml-ask-gate/governance/checks/orchestrator.py` (lines 97, 1154-1181)
- `/home/user/wt/ml-ask-gate/status/README.md`
- `/home/user/wt/ml-ask-gate/.github/workflows/orchestrator.yml` (line 17: cron every 30 minutes)
- `/home/user/Model-Lab/docs/LESSONS.md` (LL-35, LL-40, LL-43)
- `/home/user/Model-Lab/decisions/questions/P-001-accept-m1.md`
- `/home/user/Model-Lab/decisions/questions/P-001-design-gate.md`
- `/home/user/Personal-Org-Operating-Model/OPERATING_MODEL.md` §2 (lines 69-73)

I did not find the "Plain English first" heading in `OPERATING_MODEL.md` by that name. My Plain English judgement is made against the seven-part card text at lines 69-73.

## Round 2
Verdict: FAIL

Round 2 improves the question, but B is still not described truthfully. That is one blocking finding. Items 4 and 5 are also blocking: they correct the "safe" and "reversible" claims that B's description and the recommendation rest on.

1. **BLOCKING: a "waiting-owner" record with no gate or card is not valid, and the question says it is inert.**
   - `governance/checks/orchestrator.py` `check_status` lines 770-771 give the error "state waiting-owner without gate and card".
   - `load_statuses` (lines 1176-1179) logs an anomaly and skips any record with errors. So the script would not do nothing: it would write an anomaly into the dispatch log and ignore the record.
   - `governance/ROUTING.toml` lines 360-367 ("waiting-owner" means no action) only applies to a record that loads.
   - For a valid waiting-owner record, `gate` and `card` are required. `gate` must be one of `GATES` (line 101). `check_status` line 772 also errors if `gate` is set in any other state.
   - The ten REQUIRED fields (line 153: kind, stage, state, role, last_verdict, plan_round, build_round, confirm_used, attempts, sessions) are also needed. The question names none of this.
   - B's description ("in the 'waiting-owner' state, for which the script's routing table says 'do nothing'") and Context line 21 are therefore misleading.

2. **BLOCKING: the desk would flag the record to you, and the question says the desk is unchecked.**
   - `/home/user/Service-Desk/src/public/lib/model.js` lines 685-695 cover a waiting-owner status with `gate` or `card` missing. With no open card for the item, the desk adds a `status-card` flag titled "P-001: waiting on you: card ... (card file not found)".
   - Lines 696-704 give the same flag when `gate` and `card` are present but `queue/P-001-<gate>-<card>.md` does not exist.
   - Lines 247-252 also look for `decisions/P-001/<gate>-<card>.md`.
   - Either way, B as written puts a false "waiting on you" item in the owner's desk. This was checkable. The question says "how it would show this one has not been checked", and the recommendation line 11 says "B is safe enough as far as the script goes". Both are wrong on what the files show.

3. **BLOCKING: B's reversibility claim ("reversible, by deleting the record") is incomplete.**
   - Anomalies are appended to the hash-chained dispatch log (`orchestrator.py` `anomaly()` lines 1089-1094, and `log()`), and `status/processed.json` keeps their keys.
   - Deleting the record would not remove them. The log is described as verified by `verify-log` (line 47).
   - The question's header says REVERSIBILITY: reversible without qualification, for B included.

4. **BLOCKING: the "inert" alternatives are not examined.**
   - A status with `state = "done"` or `"closed"` loads and gets no action (`ROUTING.toml` lines 369-376). It needs no gate or card.
   - The desk would show it as "done" or "closed: <outcome>" (`model.js` lines 716-717), which misstates a project that is in Design.
   - It still meets `approved_in` (`v3_checks.py` line 615) only if `spec` is a string that matches `SPEC_ID_RE` (`check_status` line 757). The question does not say what spec a project with no spec would use, or whether the spec must exist (`note_spec`).
   - A fair B has to say which state would be used, and what each does to the script and the desk.

5. **BLOCKING in effect: the recommendation rests on the wrong B.**
   - Its "what would change it" line says B is "safe enough as far as the script goes". Under findings 1 to 4 that is not shown. After correction, the recommendation's lean toward A (which I think is still plausible) needs re-stating on the true costs of B.

6. **Non-blocking: the claim that nothing else waits.**
   - WHY says "Nothing else in the project waits on it: the fair test goes on either way." No record is cited, and this is a factual claim about the project.
   - The question does cite `decisions/questions/P-001-design-gate.md` line 11 (the Definer writes the fair test next). That supports it in part, but the claim should carry a citation.

7. **Non-blocking: A's and C's costs.**
   - C: verified against `v3_checks.py` lines 123-133 and 146-148. Reached marks are findings while not approved, and the standard-line and drop protections apply only when approved or waiting on the Design gate. The cost line is true.
   - A: "how long it takes is not known" and "does not by itself fix the related gap" for LL-35 and LL-40 are honest. That is what `docs/LESSONS.md` LL-43 (line 317) proposes, and the two routes in A's last sentence match LL-43. Fair.
   - "made ... then copied into this project" is stated as the route. It is consistent with the instruction given to me but I did not re-verify a copy mechanism.

8. **Non-blocking: the form and plain English.**
   - Context is now 5 lines, which is within the limit. WHO HAS CHECKED IT cites the round-1 record and states FAIL at round 1, which is honest. Update it after this round.
   - "status record", "the script" and "routing table" are glossed better. "The pipeline's script, not a conversation, runs the work" is understandable. "Routing table" is still insider language in B and Context line 21.
   - The Milestone line (M1 to M6) is fine. RISK CLASS R3 is cited to OPERATING_MODEL §2. I did not re-check that citation's text in round 2.

9. **Non-blocking: the question says only this project gains from B, and that A, B and C differ in blast radius.**
   - This is correct and consistent with finding 2: B's blast radius also includes the owner's desk.

Records checked: `/home/user/wt/ml-ask-gate/questions/P-001-gate-record.md`, `/home/user/wt/ml-ask-gate/governance/checks/orchestrator.py` (lines 97-101, 153, 702-772, 1154-1181), `/home/user/wt/ml-ask-gate/governance/ROUTING.toml` (360-376), `/home/user/wt/ml-ask-gate/governance/checks/v3_checks.py` (117-148, 613-622), `/home/user/Service-Desk/src/public/lib/model.js` (230-252, 685-717).

## Round 3
Verdict: PASS

Round 3 corrects what blocked rounds 1 and 2. I checked each claim about B against the code, and they hold. I found no blocking issue. The findings below are non-blocking.

1. **Non-blocking, checked: a "done" record with `spec = "S-001"` makes the script log nothing.**
   - `governance/ROUTING.toml` lines 369-376 (route "finished", states done/closed) give `action = "none"`.
   - `route_item` (`orchestrator.py` lines 476-479) returns no action for "none". The route loop only calls `act`, which writes log lines, when there is an action (lines 1525-1532).
   - `check_status` (lines 702-772) accepts a done record that has the ten REQUIRED fields (line 153) and a spec that matches `SPEC_ID_RE` (line 757). The error at line 770 applies only to waiting-owner, and the one at line 772 only to a record that sets `gate` in another state.
   - `specs/S-001.md` exists in the worktree, so the spec is real. `note_spec` (lines 1142-1145) only raises the spec counter.
   - So the question's "'done' loads quietly" is true for logs.
   - One caveat the question does not raise: `write()` (lines 1626-1630) compares the file's text with `dump_status` and rewrites it if it differs. A hand-written record not in the canonical form (header comment line, the `FIELD_ORDER` order) would be rewritten by the script on its next run. That is not a log entry and it is harmless, but "quietly" is not strictly "untouched".

2. **Non-blocking, checked: the "waiting-owner" claim is true.**
   - `check_status` lines 770-771 give an error, and `load_statuses` (lines 1176-1179) logs an anomaly and skips the record. The question says the script "rejects the record and logs an error".
   - The desk behaviour is also as stated. `model.js` lines 685-695 (gate or card missing, no open card: a `status-card` flag) and lines 696-704 (card file not found: a flag) both give a false "waiting on you" item.

3. **Non-blocking, checked: the "ready and the working states start work" claim is true.**
   - The routing table has dispatch routes for them. `route_item` / `_dispatch` (lines 449-468) log and plan a dispatch.
   - A stage 4 or later record with an unfrozen spec raises a card instead (line 455). That is also a side effect, so "start work" is a fair summary.

4. **Non-blocking, checked: the "done" effect on the desk is true.** `model.js` line 716 sets `item.finished = 'done'`. The question says the desk "shows the project as finished while it is in Design".

5. **Non-blocking, checked: reversibility and blast radius.**
   - "Reversible, but anything the script logged or did meanwhile stays in its log" is correct and honest. Anomalies go to the hash-chained log and to `processed.json` (`anomaly()` lines 1089-1094, `write()` lines 1637-1651).
   - A "done" record logs nothing (finding 1), so the cost applies to the other states, as the question says.
   - The blast radius (A all conversation-run projects; B this project and the desk's view; C this project's milestones) is fair.

6. **Non-blocking: other checks switch on at the same time.**
   - Once any `status/P-*.toml` holds a spec, other checks activate, not only the milestone ones (`v3_checks.py` line 73: section 3 must list a live milestone; lines 2009-2018: a research request filed after approval needs a milestone tag).
   - Every option that makes the checks see approval does this, A included. The question calls it "protections", which is true but incomplete. Consider one clause saying the project becomes subject to the checks that apply to approved projects.

7. **Non-blocking: A's second route.** A says the spec may have the script write the status record from the ruling. That is LL-43's own proposal (`docs/LESSONS.md` line 317), so it is not new. It is a fair statement of the choice.

8. **Non-blocking: plain English.**
   - "Working states", "card" and "status record" are glossed in the WHY and options, but "working states" is not defined. Context line 21 is dense. A cold reader can follow it.
   - The Context cites "Service-Desk src/public/lib/model.js", which is in another repository. Name the repository (it is "Service-Desk") and the lines (685-704, 716).

9. **Non-blocking: form.** The Milestone line (M1 to M6), the seven card parts and 5 Context lines are in order. WHO HAS CHECKED IT cites the Critic's record at round 3. `reviews/P-001-gate-record/critic.md` should hold this PASS once recorded, before the question is filed.

10. **Non-blocking: the recommendation.**
    - It now leans on stated things: A's unknown time (the stated reason for medium confidence), and the "done" side effect on the desk as the thing that would change it.
    - The risk class (R3, cited to OPERATING_MODEL.md §2) is unchanged, and the owner has everything needed to decide. I did not re-check the R3 citation text.

Records checked: `/home/user/wt/ml-ask-gate/questions/P-001-gate-record.md`, `/home/user/wt/ml-ask-gate/governance/checks/orchestrator.py` (153, 449-468, 476-479, 702-792, 1089-1094, 1142-1181, 1525-1663), `/home/user/wt/ml-ask-gate/governance/ROUTING.toml` (360-376), `/home/user/wt/ml-ask-gate/governance/checks/v3_checks.py` (73, 613-622, 2009-2018, 2362), `/home/user/Service-Desk/src/public/lib/model.js` (247-252, 685-717), `/home/user/wt/ml-ask-gate/specs/S-001.md` (existence only).
