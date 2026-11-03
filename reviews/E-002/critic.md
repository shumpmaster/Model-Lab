Verdict: PASS

The Critic's plan review of the two Design check registrations, E-001 (replay) and E-002 (judge consistency), reviewed together, on a different model from their writer (brief: docs/briefs/23-critic.md), verbatim: round 1 (both FAIL), round 2 (E-001 PASS, E-002 FAIL), round 3 (both PASS). The same record is filed as reviews/E-001/critic.md. Recorded by the orchestrator. Session session_01QBwHGN4kVVA3rfHx2b4FsF, 2026-11-03.

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

## Round 2
Verdict: FAIL
E-001: PASS
E-002: FAIL

Round 2. I read both revised files cold and checked each change you listed against its text, the records, and the environment where I could. E-001 clears. E-002 has one blocking defect, finding 1, which is a small fix.

Verification of the nine items:
- Start-commit rule (E-001 F1): fixed. It accepts a dispatch-log commit, the base of the branch or pull request, or the parent of the first commit. It says outright that a "Reviewed … at <commit>" names the finished work, and a piece with only that commit fails F1. E-002's use of the reviewed commit for Set C is flagged as correct there.
- Templates: both are now in the files. The brief-rebuilding template and confinement paragraph are in E-001, and the judge-brief template is in E-002, with E-001's check run pointed at it. E-002 requires one filled text per piece, identical byte for byte across judges. Sound.
- Faithful and template replay: reported separately in the hypothesis, measure and threshold. Template replay is limited to changes that touch neither the brief nor the template, and a brief change goes to the fallback. The result is never called faithful. Sound.
- "Usable in part": stated. Pool arithmetic is correct (plans 42, research 14, built work 48). M2 states its own pairs per kind, and a smaller pool means the fallback, with no mixing of past and new tasks. The 50-pairs figure is labelled as an inference. Sound.
- Reruns: a rerun costs 2 runs. The reserve of 4 gives at most 2 reruns, with at most 8 replay and 8 check runs, so the cap of 20 holds. E-002 is 8×2 + 2×2 = 20. Hard caps are counted as sessions started. Together that is exactly 40. A failed replay is not judged, so it saves a check run and gives slack. Sound.
- Pass gate against an empty pass: present. "Not tested" applies if fewer than 3 consistency-set pieces have a test-judge PASS, or fewer than 2 Set B pieces have a PASS from either judge. Set C adds first-time passes so the set is not all failed work. "Not tested" triggers the fallback. The binomial figures check out (24 in 100 and 1 in 100 over 10 pieces). The self-preference limit (2 of 8, one way, still passes) is stated plainly.
- F4 from the transcript file: usable. Subagent transcripts do exist at `<session folder>/subagents/agent-<id>.jsonl` in this environment, and F4 fails if the file is missing. Not verified for helpers started from inside a Builder subagent (finding 3).
- History-limited copy: `git init`, then `fetch --no-tags` of the one start commit, then `checkout --detach`. Sound in construction. The claim "tested on Model-Lab on 2026-11-03" cites no record (finding 3).
- Who runs each step: the Builder runs and starts every helper, and the Reviewer, who did not run it, analyses. This matches the playbook (§6: "run exactly as registered (Builder)"). The earlier bad citation to PROJECT §4 is gone from the text, though §4 stays in the sources line.
- Research stratum and first-time-pass pieces: added as separate strata, outside the thresholds. Research is judged on web-free memos alone. The first-time-pass pieces match Q-008 (plans HD1 and S-027, research SD Q-008 and Q-013). The built-work first-pass pieces are defined by a rule over Q-006 §4 and Q-008 §2.3.

Findings:

1. (B, E-002) Set C is selected by two rules that conflict. "The first two of E-001's first-time-pass pieces, in its list order … one plan and one built work where possible." E-001 lists plans first (HD1's plan, S-027), then research, then built work, so the first two are both plans. The "where possible" lets the Builder choose after seeing the records, and Set C counts toward the deciding consistency set. Fix: name the two pieces, or state one rule only (for example, the first plan and the first built piece in E-001's list that can be recovered, skipped ones listed).

2. (NB, E-001) F4 fails on any read of a path outside the copy. A Bash call touching /usr or a temp directory would fail the replay, and fail the whole kind, with no rerun, since that is not a set-up fault. List the system paths that are allowed (or say none and accept the strictness), and say who decides a borderline call.

3. (NB, E-001) Two environment claims need a record. The tested copy-construction on Model-Lab needs a cited record. Transcript storage for helpers started by a Builder that is itself a subagent is unverified. If the transcript is missing, F4 fails by rule, so the cost of being wrong is a failed run, not a wrong answer.

4. (NB, E-001 and E-002) The judge's copy "with the replay's output added" does not say who commits the output. It should be a commit on the start commit, because E-002 requires a copy holding only "the commit judged and its ancestors". The sources line of E-001 still lists PROJECT §4, which does not assign the Design checks. This is harmless now.

5. (NB, E-001) Selection of the built-work first-pass piece depends on the Builder reading rounds in Q-008 §2.3's list. §2.3 does not itself say which passed in round 1. The Builder should cite the record lines, which F1–F3 already require.

Views on the earlier four points, now closed:
- (1) Fable 5.1 kept, with both caveats now written in.
- (2) The rebuilt-brief grade is handled correctly.
- (3) Research is predicted to fall to the fallback in advance. The web-free stratum is separate and counted directly.
- (4) The returned-piece limit is stated per kind. First-time-pass pieces are audited.

Files reviewed (I wrote none):
/home/user/wt/ml-definer/experiments/E-001.md
/home/user/wt/ml-definer/experiments/E-002.md

## Round 3
Verdict: PASS
E-001: PASS
E-002: PASS

Round 3. I re-read both files in full. Finding 1 from round 2 is fixed, non-blocking points 2–5 are handled, and nothing the changes touched broke what already passed.

Round-2 points:
1. E-002 Set C (was blocking) is fixed.
   - The rule is now single: the first plan and the first built-work piece in E-001's first-time-pass list whose round-1 submission and check pack can be recovered.
   - The pieces are named: for plans, SD HD1's plan then POOM S-027; for built work, the SD unit then the POOM piece, as E-001 defines them.
   - Skipped pieces are listed with the reason. If a kind has none recoverable, Set C shrinks and the result says so.
   - The Builder has no choice left.
   - The run count is unchanged: 8×2 + 2×2 = 20.
2. F4 system paths (NB) are fixed.
   - Allowed: read-only /usr, /bin, /lib and /etc, and files the run creates in /tmp. Everything else outside the copy fails, including the rest of /home/user and /root with its ~/.claude.
   - Borderline calls go to the Reviewer, who must cite the transcript line.
3. Environment claims (NB) are fixed.
   - The "tested on Model-Lab" sentence is replaced by a check on every copy, recorded in the result: `rev-list --count` equal in the copy and the full clone, and a later commit's `cat-file -t` fails. A copy that fails is a set-up fault.
   - A missing transcript fails F4 by rule, and the file says this includes helpers started by a Builder that is itself a helper.
4. Committing the replay's output (NB) is fixed.
   - The Builder commits it on top of the start commit, or uses the replay's own last commit, and makes a second copy from that commit.
   - E-002 step 2.4 is referenced consistently.
   - PROJECT §4 is dropped from E-001's sources.
5. The built-work first-pass piece (NB) is fixed. The Builder must cite the review file and line showing the chosen piece's round-1 PASS, and that every earlier piece in the list did not pass in round 1.

Findings (all non-blocking):
1. (E-001) The copy check says `cat-file -t <the full clone's head>` must fail. If a piece's start commit is the full clone's head, or the head is its ancestor, the check fails for no fault. Say "a commit later than the start commit that exists in the full clone", and skip the check when none exists.
2. (E-001 and E-002) E-002 says the replay output is a commit on top of the start commit. E-001 also allows the replay's own last commit. The copy rule, "the commit judged and its ancestors", covers both. Harmless, but the Reviewer should read them together.
3. (E-001) An F4 failure caused by a helper wandering outside the copy is not a set-up fault, so it gets no rerun and fails the kind. This is strict, but it is stated and decided in advance, which is what the playbook asks.

The checks that already passed in round 2 still hold: the start-commit rule, both templates in the files, faithful and template replay reported separately, and "usable in part". The rerun cost of 2 within the 4-run reserve and the hard caps of 20 each, 40 together, also hold. So do the pass gate, the F4 transcript source, the working-copy construction, who runs each step, and the separate research and first-time-pass strata. The binomial figures (24 and 1 in 100) are correct. Both files can be frozen once the `frozen:` line is set before any run.

Files reviewed (I wrote none):
/home/user/wt/ml-definer/experiments/E-001.md
/home/user/wt/ml-definer/experiments/E-002.md
