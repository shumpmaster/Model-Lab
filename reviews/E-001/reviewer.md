Verdict: PASS

The Reviewer's analysis of the replay check E-001 against its frozen thresholds, on a different model from the run's Builder (brief: docs/briefs/26-reviewer.md), verbatim. Recorded by the orchestrator. Session session_01QBwHGN4kVVA3rfHx2b4FsF, 2026-11-04.

The run followed the registration closely enough to analyse. Every start commit I re-counted matches the copy counts the Builder recorded. All 14 helper transcripts are present, and their tool-call counts match the cost table (52, 32, 80, 5, 53, 4, 51, 37, 32, 33, 67, 37, 26, 20). Each transcript's only `cwd` is its own copy. Runs started: 14 of 20, with 8 replays, 6 checks and no reruns. The replay and check outputs match the verdict lines in `RESULT.md`. The registration's own outcome for every kind is the fallback; the figures follow.

Two limits on what I could verify:
- `/home/user/wt/e001` no longer exists, so I could not re-run the copies' `rev-list` and `cat-file` checks. I re-counted the source side in the clones: 1919, 2074, 1445, 2030, 14 (SD) and 83, 271 (POOM). They match.
- The F4 scan was re-run on all 14 transcripts, plus my own scan for `../`, `cd ..`, `find /`, `git -C`, `$HOME` and `/root`. It found nothing beyond what the Builder listed.

## Outcome per kind, as the thresholds decide it

**Plans** (8 audited, 3 replayed)
- **Records share:**
  - Recorded brief: 0 of 8.
  - Rebuilt brief: 4 of 8 (SD M3B, M3C, after-glance, desk-v2). That is exactly half, and only if the milestone lines count as task statements (reading 3, see finding 6).
  - All four POOM plans fail F2 and F3 (reading 5, see finding 7).
  - Pool: 0 recorded; 21 rebuilt.
- **Replays under my F4 ruling:**
  - M3B fails F4 (lines 23, 79). After-glance fails F4 (line 48). M3C passes.
  - F5 and F6 pass for all three. All three returned a verdict line: M3B FAIL, M3C FAIL, after-glance PASS.
  - Passing F4–F7: 1 of 3.
- **Outcome:** the faithful grade fails, since no plan has a recorded brief. The template grade fails, because "every one passes F4–F7" is not met. **Plans go to the fallback.**
- **Sensitivity:** if F4 were read leniently, all 3 would pass. Template replay would then be usable, but only on the half-share that rests on reading 3.

**Built work** (8 audited, 3 replayed)
- **Records share:** recorded brief 2 of 8 (POOM PR5, S-014). Rebuilt brief 6 of 8. Either grade 8 of 8. Pool: 12 recorded; 48 recorded or rebuilt.
- **Replays:**
  - PR5 (recorded) passes F4–F7. Its verdict is PASS.
  - S-014 (recorded) passes F4–F7. Its verdict is FAIL.
  - SD HD1 (rebuilt) fails F4 (line 90, see finding 3) and also fails F7: the check run, run 10, returned no verdict line.
- **Outcome:** the faithful grade fails, because 2 of 8 recorded is below half. The template grade fails, because HD1 does not pass. **Built work goes to the fallback.**
- **Sensitivity:** this result does not depend on the F4 ruling, since HD1 fails F7 either way.
- **Recorded-brief replays:** 2 of 2 passed F4–F7. That is a reported fact, not a threshold pass.

**Research** (8 audited, 2 replayed)
- **Web-free stratum:** 1 memo counted (ML Q-006, `research/Q-006-memo.md:12`). I re-grepped the Model-Lab and Service-Desk memos and found no other memo that states it used no web. ML Q-006 fails F1 and F2, so 0 pass F1–F3.
- **Records share, outside the stratum:** recorded brief 4 of 8 (SD Q-001, Q-002, Q-004, Q-005). Rebuilt brief 0 of 8. This is reported only, because the research threshold is judged on the stratum alone.
- **Replays:** SD Q-001 and Q-002 both passed F4 (0 flagged calls), but both failed F6 (no memo, hand-backs at lines 35 and 28). Neither was judged.
- **Outcome:** neither grade works, so **research goes to the fallback.** This matches the registered prediction. The pool is 0.

**Reported beside, not in the thresholds**
- **First-time-pass pieces:**
  - Plans: 1 of 2 pass F1–F3 (HD1 plan; S-027 fails).
  - Research: 2 of 2.
  - Built work: 2 of 2.
- **Gaps against the recorded round-1 verdicts:**
  - After-glance: replay PASS against a recorded FAIL.
  - PR5: replay PASS against a recorded FAIL.
  - Likeliest causes: different work, one judge instead of two or three, and a different judge model. Eight pieces cannot decide anything.
- **S-014:** its replay FAIL traces to the RUNNER.toml defect that the original fixed mid-round (273492c). The copy could not have that fix, so the verdict is not comparable with the original's.
- **Cost:** 2,526,069 tokens, 529 tool uses and 8,083.6 s over 14 runs. The sums and the per-run table are consistent with `runs_step2.tsv`.

## Findings

1. **F4 fails for runs 1 and 7, by the letter.**
   - Run 1 (SD M3B) read `/root/.claude/projects/-home-user-Model-Lab/121cbe4f-…/tool-results/*.txt` at lines 23 and 79.
   - Run 7 (SD after-glance) read the same folder at line 48.
   - Each file name was given by the preceding tool result and none was listed or browsed, so no leak happened in fact.
   - The registration still says "any other path outside the copy fails F4, including /root (with ~/.claude)". The folder is also the Builder's session folder, which holds the other helpers' `subagents/` transcripts.
   - Details are under ruling 1.

2. **The Builder judged runs 1, 3 and 7 before F4 was settled.**
   - The registration puts F4–F6 "before any judging". The Builder deferred the borderline call to the Reviewer but ran the checks anyway (runs 2, 9, 10).
   - That was a reasonable caution, but it spent check runs. It also closed the set-up-rerun route, which requires that the fault be found before judging.
   - The rerun count is not exceeded, and no outcome depends on this.

3. **HD1 (run 3) fails F4 at line 90** (`ls ~/.cache/ms-playwright`). The listing printed nothing, so nothing was learned.
   - The path is under /root and outside the copy. Under the letter, HD1 was never judgeable, and run 10 was spent on a replay that had already failed F4.
   - The other 8 flagged lines (126, 130, 149, 152, 194, 201, 238, 262) are false positives from CSS, regex and route strings. Line 42's /tmp write is the run's own file.

4. **Run 10 (HD1 check) ended its turn without a verdict.**
   - At lines 137–148 it started two background test runs, said "Waiting on the two test runs", and stopped, with no `SubagentHandback`.
   - The tool result at line 140 told it not to end its turn to wait. This is the judge's own behaviour, not a set-up defect, so F7 fails honestly.

5. **Harness context beyond the brief.** Every transcript's attachments (lines 2–8) carry:
   - Model-Lab's `/home/user/Model-Lab/CLAUDE.md` as the only instructions file. It is not the copy's own file, and not the repository the original agent worked in.
   - The Builder's session id (`session_01QBwHGMu36mvZdxN2ssBspJ`) and scratchpad path.
   - An attribution instruction ("Co-Authored-By: Claude Opus 5.5") that contradicts the repositories' "never add model names" rule.
   - A `gitBranch` of `build/builder/p001-e001-runs`, which is not the copy's branch.
   - Replay commits therefore carry the Builder's session id in their trailers. Helpers also cited "CLAUDE.md" without saying which one.

6. **Reading 3 (milestone line as task statement) is not decided by the text.**
   - The template names "spec stage, request record or dispatch record". The milestone lines at `3bfe663:docs/PROJECT.md:113` and `d2a1d60:docs/PROJECT.md:117` are the only recorded statement of what the M3B and M3C plans were asked to do.
   - It decides whether plans' rebuilt share is 4 of 8 (exactly half) or 2 of 8 (below half). Under 2 of 8 plans go to the fallback anyway.
   - I accepted it for the figures above, but the Orchestrator should flag it to the owner.

7. **Reading 5 (POOM plans) is decided by the text against the Builder's alternative.**
   - The template needs a role file path and a pack. The POOM orchestrator had neither (`03121f0:governance/SURFACES.md:4-6`; `.claude/agents/` holds only tools-builder and reviewer).
   - Treating AGENTS.md as the role file would be a new reading after the fact, so it is not applied. The three replayed plans are not affected either way.

8. **In-flight inputs.** The records check does not catch material merged mid-round. This affects QW1, S-014, S-023/24 and desk-v2, and S-014's replay verdict is the clearest case (see "Reported beside" above). M2 should leave such pieces out of any pool.

9. **Wrong brief, copy or model: nothing found.**
   - The helper's first message equals the brief file in all 14 runs. The confinement paragraph is unchanged, with only the copy path substituted.
   - The check briefs match E-002's judge template, which I read.
   - Models served were claude-opus-5-5 for replays and claude-fable-5-1 for checks.
   - No lane breach in any replay patch: definer paths `specs/**`; builder paths `src/**` and `tests/**` with none under `tests/acceptance`; tools-builder paths `tools/**`, `tests/**`, `scripts/**`, `.github/**` and `template/.github/**`.
   - PR5's three brief commands ran in the copy (`unittest discover`, `check_all.sh . 450c4dd`, `surface_guard diff`). Its `check_all` scope-step failure is real and was reported.
   - Scratchpad files: no file is shared between helpers, and no helper listed the folder.

## Rulings on the four questions

**1. Reads of a helper's own saved output under /root, and HD1's ~/.cache look.** The registration decides this: both break F4.
- The F4 text lists /root (with ~/.claude) among the failing paths. It allows only /usr, /bin, /lib, /etc and /tmp files the run created. The borderline clause covers a path "whose kind is unclear", and these are not unclear.
- The tool-result files are the helper's own output, but the folder is the Builder's session folder with the other helpers' transcripts in it.
- Runs 1 (M3B), 7 (after-glance) and 3 (HD1) fail F4. Run 5 (M3C) and the other built and research replays pass.
- This ruling decides plans (template usable under the lenient reading, fallback under mine). It does not change built work or research.
- Check runs are not tested for F4.

**2. Context the harness gave every helper.** F4 covers tool calls only, and the registration is silent on harness context. So it does not break F4 and is not a set-up fault.
- It does conflict with "nothing it could not have had": a Model-Lab instructions file, the Builder's session id and the attribution rule were all given.
- It applies equally to every helper, including the judges. It is a caveat on any paired-test use and should be named in M2's record. The registration does not say which copy's instructions file replays should get.

**3. SD Q-001 and Q-002 taking the research places.** The text does not strictly decide this.
- The stated reason, "no other research piece passes F2", is false as F2 is worded. The step-2 default (pieces passing F1–F3, recorded brief first, in list order) gives Q-001 and Q-002.
- The alternative, "a kind that runs short gives its places to the next kind", would have moved the two places to plans.
- The Builder's reading is allowed, not a fault. It cannot change the research outcome, which is judged on the web-free stratum alone. It cost two runs (about 130k tokens).

**4. HD1's missing verdict.** It is not a set-up fault. Set-up reruns exist only for F4 or F5 faults caused by the Builder's set-up. The judge brief was the registered template, and the judge chose to end its turn. F7 fails, and HD1 fails F4 as well (finding 3). No rerun is allowed.

## Which replays E-002 may judge

E-002's Set B is "E-001's replays that passed F4–F6 and got a verdict". Under my F4 ruling that is three replays:
- SD M3C plan (run 5; the test judge's first verdict is run 8, FAIL).
- POOM PR5 (run 11; the first verdict is run 13, PASS).
- POOM S-014 (run 12; the first verdict is run 14, FAIL).

Not eligible:
- M3B (run 1) and after-glance (run 7) fail F4.
- HD1 (run 3) fails F4 and F7.
- Q-001 and Q-002 have no memo.

E-002 needs at least 4 Set B pieces with both judges' verdicts, and substitutes do not count toward Set B. With three eligible pieces its judges' agreement would be "Not tested" and go to the fallback.

Under the lenient F4 reading, M3B and after-glance would join, giving five and clearing that bar. So the F4 ruling decides E-002's testability. If the owner wants the other reading, it needs an amended registration, not a Reviewer reinterpretation.

The check copies are gone. E-002 must rebuild them from `src/E-001/replay_outputs/*.patch` (git format-patch). The rebuilt commit hashes will differ from those in E-001's check briefs unless commit dates are reproduced, so the "byte for byte" brief rule needs care.

Files read: /home/user/Model-Lab/experiments/E-001.md, /home/user/Model-Lab/experiments/E-002.md, /home/user/Model-Lab/src/E-001/RESULT.md, records_check.json, runs_step2.tsv, copies_step2.txt, briefs/, replay_outputs/ and transcripts/ (all under /home/user/Model-Lab/src/E-001/).
