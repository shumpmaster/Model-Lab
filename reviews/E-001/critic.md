Verdict: FAIL

The Critic's plan review of the two Design check registrations, E-001 (replay) and E-002 (judge consistency), reviewed together, on a different model from their writer (brief: docs/briefs/23-critic.md), verbatim. The same record is filed as reviews/E-002/critic.md. Recorded by the orchestrator. Session session_01QBwHGN4kVVA3rfHx2b4FsF, 2026-11-03.

## Round 1
Verdict: FAIL
E-001: FAIL
E-002: FAIL

I read both registrations, experiments/_REGISTRATION.md, docs/PROJECT.md, the open-unknowns ruling, the environment check and research/Q-008-memo.md. I checked the sampling, the budget arithmetic and the cited claims against them.

Findings. Each is blocking (B) or non-blocking (NB), and each names the file it applies to.

1. (B, E-001) Wrong start commit. F1 accepts "a review record's 'at <commit>'" as the commit a task started from. In Q-008 that is the commit the reviewer checked, which is the finished work (the "Reviewed: PR #n at <sha>" lines). A replay made there starts with the answer in the tree. F4 would not catch it, because the leak is inside the "start commit". F1 must name the parent or base of the work, and say what to do when only the reviewed commit is recorded (the piece fails F1). E-002 Set A is right to use the reviewed commit, because it judges the submission; the two files use "at <commit>" in opposite senses.

2. (B, E-001) The "fixed template" for rebuilding a brief is not in the registration. The same gap applies to the prompt that builds a judge's brief (E-001 step 3 and E-002 "What a judgement is"). Nobody else could run these as written. The two judgements of one piece also need to be built from the same prompt, or "consistency" measures prompt drift. Put both templates in the file before it is frozen.

3. (B, E-001) A rebuilt brief counted as "working" contradicts the question. The question asks for a re-run with "what its agent had then and nothing it could not have had". A rebuilt brief is something the agent never had.
   - Q-008 §5 says worker briefs are not recorded for conversational work, and only two are recorded in Model-Lab. Nearly every piece will therefore be "rebuilt".
   - F3 then passes almost any piece that has a spec, so it is close to vacuous.
   - The candidate changes include changes to briefs. A control arm on a synthetic brief is not "leaving things as they are", and cannot be compared with the starting figures.
   - Fix: report recorded-brief and rebuilt-brief replays as separate results per kind. Rebuilt briefs may support only changes that do not touch the brief or the template. The result must call it "template replay", not "faithful replay".

4. (B, E-001) The "works" threshold does not answer the hypothesis, which says "often enough to fill a paired test". "Works" is half of the audited pieces passing F1–F3, at least 2 replayed, and all replays passing. Nothing compares the pool with the sample M2 needs.
   - PROJECT §6 puts a three-kind test at about 300 runs. If I read that as roughly 50 pairs per kind, then research (19 pieces) and plans (44) cannot reach it even at 100% usable.
   - PROJECT does not state pairs per kind, so this is my inference. The registration should state the needed pool now, or say that "works" means only "usable in part", and what M2 then does.

5. (B, E-001 and E-002) The 40-run cap holds only on the writer's reading. A reran replay needs a new check run too, since E-002 depends on it.
   - If "4 reruns" means 4 sessions, only 2 reruns can be completed. If a rerun means replay plus check, E-001 can reach 24 runs.
   - Define the cost of a rerun and stop reruns when the 4 are spent.
   - E-002's "8 replay results" does not say whether replays that failed F4–F6 (leaked, unfinished) are judged. Say they are not, and fill the place from the list.
   - With that settled, 20 + 20 = 40 exactly. Any ambiguity breaks it.

6. (B, E-002) A pass can be empty. All 8 Set B pieces are replays of work that was sent back in the past. If the judges say FAIL on nearly all of them, "at most 1 self-flip" and "at most 2 differences" hold trivially, and M2 adopts the test judge.
   - The size-power paragraph covers only random flips.
   - Require, before a pass counts, a minimum number of pieces where any judge returned PASS. Otherwise the result is "not tested", which triggers the fallback.
   - The self-preference test has the same hole. It cannot show "the same-model judge is kinder" if nothing passes. The registration also gives no power statement for self-preference.

7. (NB, E-001) F4 relies on "the transcript shows". The environment check establishes only that each helper reports tokens, tool uses and time at return, not that a readable transcript exists. Confirm it, or state the substitute (for example, a log of the paths each helper opened).
   - The method for making the history-limited copy is also unspecified. A plain clone keeps later objects. A helper could also read the full clones at their known absolute paths. State the construction and forbid access outside the copy.

8. (NB, E-001) "The Builder that runs this check (docs/PROJECT.md section 4)": section 4 gives the Builder the test (M4) in Build, not the Design checks. It does not say who starts the helper sessions in step 2 either. Name who runs each step.
   - The cited "section 8" for "replay for a further kind is checked when it enters the test" is not in section 8.
   - V1 does not name "the three kinds"; V2 does.

9. (NB, E-001) The pool formula (records share × Q-008 totals) extrapolates from returned pieces to every piece, including the 2 plans and 32 built pieces that passed first time. Those were never audited, and may have thinner records. The pool is also computed on research pieces taken in list order, not by a rule. At least report the pool over returned pieces only, and add a few first-time-pass pieces to the no-run records check.
   - F2 says "everything the task read". For conversation-started work the records cannot show that. Require each F1–F3 verdict to cite the lines it rests on.
   - F6 "same kind and scope" is not defined. One F6 failure fails the whole kind and cannot be rerun, so define it.

10. (NB, E-002) The "all go the same-model judge's way" rule fires on a single disagreement, and the registration does not say what M2 does when that is reported alongside a pass.
    - Set A costs 4 runs for non-deciding data. Its pieces' worker models are unknown, and the original round-1 briefs for judges are not recorded. Spending those runs on more Set B pieces would serve U3 better, but the budget is exactly fixed.
    - Q-008's samples are returns, not always round 1 (for example S-023 r11, job-prs r2). The "round-1 submission" for those pieces comes from a different return, so state that.

11. (NB, both) The claims I could check match their records:
    - The sample order and the Set A and substitute lists match Q-008 §3.
    - The totals 44, 19 and 80 match Q-008 and PROJECT §6.
    - The binomial figures of about 37 and about 4 in 100 are correct (0.367 and 0.035).
    - The four models and the one-provider limit match the environment check.
    - ML Q-006 does state that no web was used.
    - The cited decision files exist.
    - One loose claim: "original model not recorded (Q-008 §5)". §5 finds two "Session: Opus 5.5" headers in SD desk-v2 1b.

Points raised by the writer:

(1) Test judge. Keep Fable 5.1. Sonnet 5.5 is in the same 5.5 line as the Opus 5.5 workers, so it adds nothing as a "different" judge, and the registration is right to say the family is unestablished. Add two points. A Fable/Opus disagreement may reflect capability, not bias. The registration should also say the pieces' original workers (Set A) are of unknown model, so the Fable-is-different premise holds only for Set B. Do not add Sonnet runs; there is no room in the 40.

(2) Rebuilt brief. Not acceptable as written (finding 3). Counting it as working is defensible for a paired test where both arms get the same brief and only a non-brief change differs. It must not be called faithful replay. It must be reported separately, and it must not support tests of brief changes. The recorded-brief share should be stated in the result and used by M2.

(3) Research falling to the fallback. This is a legitimate and likely honest result: web pages cannot be restored, and Q-008 §2 shows ML researchers' sessions often could not open outside sources. Accept it, but make three changes. State the prediction in advance. Count the web-free memos among the 19 directly instead of share × 19. Keep the rule-added web-free memos as a separate stratum. They are chosen because they pass F2, so mixing them into the "at least half" test inflates the share. E-002 should also say research from the web cannot be judged by the test judge at all.

(4) Pieces leaning to sent-back work. A real bias, and the registration discloses it, but disclosure is not enough. A paired test on previously failed tasks has a different baseline from the population, and the pool formula ignores it. Add first-time-pass pieces to the no-run records check, report the pool over returned pieces only (finding 9), and make the result say which kind-level conclusions hold only for sent-back work.

Files reviewed (I wrote none):
/home/user/wt/ml-definer/experiments/E-001.md
/home/user/wt/ml-definer/experiments/E-002.md
