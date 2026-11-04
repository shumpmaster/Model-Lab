Verdict: FAIL

The Critic's cold read of questions/P-001-gate-record.md, on a different model from its writer, verbatim. Recorded by the orchestrator. Session session_01QBwHGLd77YbwCSMSPU26vW, 2026-11-04.

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
