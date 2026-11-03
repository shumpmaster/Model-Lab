# E-001 result: the records check (step 1) and the replay runs (step 2, six of eight places run)

experiment: experiments/E-001.md (frozen at 4e2cb12)   spec: S-001 (draft)   run by: builder, session_01QBwHGN4kVVA3rfHx2b4FsF   date: 2026-11-03
status: **step 1 done (session_01QBwHGN4kVVA3rfHx2b4FsF); step 2 run in part (session_01QBwHGMu36mvZdxN2ssBspJ, 2026-11-03): 6 of the 8 places replayed, the 2 POOM places not run (no access to that repository).** **Runs started: 10** (6 replay runs, 4 check runs, 0 set-up reruns), out of a cap of 20. See "Step 2" below.

The Builder reports the measures only. The Reviewer analyses them against the thresholds (E-001, "Who does what").

## Why step 2 was not run in the step-1 session (kept as written then)
Step 2 needs one helper session per replay. Each must run on Opus 5.5 with **its working directory set to the copy** under /home/user/wt/e001/. Its transcript must be **stored in the starting session's folder as `subagents/agent-<id>.jsonl`**, or F4 fails by rule.

This Builder session has no tool that starts such a helper. It has no Agent or Task tool. The only tool that starts a session is the remote `create_session`, and it starts a separate cloud session in its own container. That session can see neither this container's copies nor this session's subagent folder, so its transcript would not be stored where F4 reads it. Starting one would therefore spend a run on a replay that fails F4 by rule, not because of the record.

So, as the dispatch brief instructs, the Builder stopped after step 1. No working copies were made, and nothing exists under /home/user/wt/e001/.

## How the check was done
- **Full history.** `git rev-parse --is-shallow-repository` returns `false` for Service-Desk (SD), Personal-Org-Operating-Model (POOM), Model-Lab (ML) and portfolio, so no fetch was needed. All reads were read-only: no checkout and no write in any clone.
- **Scripts** (in this folder):
  - `records_check.py` checks F1 and F2 by machine for every audited piece: each piece's first work commit and its first parent, the named inputs present at the start commit, and the text of every cited record line. Its output is `records_check.json`.
  - `sd_scripted_research.py` handles the SD scripted research. For each item it finds the round-1 dispatch's control record, prints its recorded brief, and checks every manifest entry's sha256 against the file at the start commit.
- **Line cites** are `<commit>:<path>:<line>`. `HEAD:` is the clone's checked-out commit (SD c0d6ef8, POOM d069e10, ML e3fd48d).

### Readings the Builder made (flagged for the Reviewer)
The registration leaves these points open. Each reading below is applied the same way to every piece.

1. **F1 when the work's first commit is a recording by the orchestrator, not the worker's own.** This covers scripted research and ML research, whose workers hold no write tools.
   - The start is the first parent of that commit.
   - If that parent is dated *after* the dispatch, it passes only when a record shows it equals what the agent had.
   - It fails when the parent holds output the agent could not have had within its reach.
   - SD scripted research passes on this rule. Each control record's manifest lists every file in the agent's working folder, and all of them are byte-identical at the parent (sha256).
   - ML Q-001, Q-002, Q-004 and Q-006 fail on it (see the table).
2. **F2 with a glob that matches nothing** (`checks/**` in SD; `library/**` in ML before 2026-11-01 19:45, when the portfolio library began, portfolio 5ea7d2a). Such a glob names no file, so nothing it names is missing.
3. **F3, "rebuilt": what counts as a task statement.** A record at the start commit that states this piece's work, copied verbatim. The source kind is given for every rebuilt piece:
   - **stage:** a stage row or build section of the spec;
   - **ruling:** an owner ruling or request asking for the work;
   - **ledger:** a ledger decision or licence naming the build;
   - **milestone:** a milestone line in the project document.

   Two rebuilt plans rest on a milestone line alone (SD M3B and M3C). If the Reviewer does not accept a milestone line as a task statement, those two become **neither**.
4. **Who the agent is in a piece with two lanes.** POOM PR5, S-007's build and S-023/24 each have orchestrator commits beside the builder's. F1–F3 are graded on the dispatched worker, the builder, consistent with F6 (a replay need only change one of the original's paths). The orchestrator lane is noted.
5. **POOM plans.** These were written by the POOM orchestrator session itself: every commit's author is `orchestrator`, and no worker was dispatched. That role has no role file and no context pack at the start commit:
   - the roster in governance/SURFACES.md:4-6 lists only `tools-builder` and `reviewer`;
   - .claude/agents/ holds only those two files;
   - POOM has no PACKS.toml for its own roles.

   So the template's `<role file path>` and "Read first" cannot be filled. That gives F3 **neither**, and F2 **fails** on the missing role file.
   - Alternative reading, not applied: AGENTS.md as the orchestrator's role file. The Reviewer may take it. Under it, the task-statement records would still need finding for S-007, S-015 and S-022. S-012r has its ruling recorded at the start, 5ee6c05 (L-0081). S-027 has its ruling at 93ed08c (the owner's answer B1).
6. **"F2 checks the named inputs only."** The registration requires this to be said. What else a conversation-started agent read is not recorded and was not checked.
   - The SD scripted researchers had WebSearch and WebFetch (each control record's `tools`; SD .claude/agents/researcher.md:4).
   - Their round-1 memos cite 15 to 23 web URLs each.
   - No brief, pack or question names a web page, so F2 passes on its wording.

   The registration's step-2 premise, "no other research piece passes F2", therefore **does not hold as F2 is worded**: four SD scripted research pieces pass F1–F3. This does not touch the research threshold, which is judged on the web-free stratum alone.

## The records check: returned pieces (24)
Under "Brief": R = recorded, B = rebuilt (with the task-statement kind), N = neither. "Start" is the start commit; the number in brackets is `rev-list --count` there.

### Plans (8)
| # | Piece | Start (count) | F1 | F2 | F3 | Notes |
|---|---|---|---|---|---|---|
| 1 | SD M3B plan | SD 3bfe663 (1919) | **pass**: parent of the first work commit 31ff26d (definer), the commit reviewed in round 1 (HEAD:reviews/M3B/_plan-critic-r1-verbatim.md:3) | **pass**: .claude/agents/definer.md, docs/PROJECT.md, library/** (92 files) and specs/S-001.md, all at 3bfe663; the definer pack is `docs/PROJECT.md, library/**, {ruling}` (3bfe663:governance/PACKS.toml, [roles.definer]), with `{ruling}` unset | **B (milestone)**: task from 3bfe663:docs/PROJECT.md:113 | Round 1: FAIL from the Critic, the Reviewer and the Design reviewer (reviews/M3B/_plan-{critic,review,design}-r1-verbatim.md:7) |
| 2 | POOM S-007 plan | POOM 03121f0 (168) | **pass**: parent of fea44b3 (orchestrator, the first draft) | **fail**: no role file for the writer's role (03121f0:governance/SURFACES.md:4-6; .claude/agents/ holds tools-builder.md and reviewer.md only) | **N**: the writer is the orchestrator session itself, with no role file, no pack and no dispatch (reading 5) | Round 1 FAIL (HEAD:reviews/7/_plan-review-s007-round1-verbatim.md:6) |
| 3 | SD M3C plan | SD d2a1d60 (2074) | **pass**: parent of b26e876 (definer); the review names the base: "at e477cc2 against d2a1d60" (HEAD:reviews/M3C/_plan-review-r1-verbatim.md:5) | **pass**: same four inputs, all present | **B (milestone)**: d2a1d60:docs/PROJECT.md:117 | Round 1 FAIL (HEAD:reviews/M3C/_plan-review-r1-verbatim.md:1) |
| 4 | POOM S-012r plan | POOM 5ee6c05 (236) | **pass**: parent of 84caf74, the commit reviewed (HEAD:reviews/7/_plan-review-s012r-round1-verbatim.md:3) | **fail**: no role file (as #2) | **N** (reading 5) | Round 1 FAIL (same file:5) |
| 5 | SD after-glance plan | SD 2d0edb0 (1445) | **pass**: parent of 671eada (definer), the commit reviewed (HEAD:reviews/S-001-after-glance/_plan-critic-r1-verbatim.md:3) | **pass**: the four inputs, plus the five ruling files and the owner's request, all present | **B (ruling)**: 2d0edb0:decisions/questions/P-001-glance2-{anchor,arrow,counts,palette,standard}.md:1 and docs/design/references/owner-request-2026-10-24-glance-emphasis.md:62-72 | Round 1 FAIL from the Critic and the Reviewer (_plan-critic-r1:7, _plan-review-r1:7) |
| 6 | POOM S-015 plan | POOM 6c3c9a4 (271) | **pass**: parent of 20f25ca (orchestrator, "Draft S-015") | **fail**: no role file (as #2) | **N** (reading 5) | Round 1 FAIL (HEAD:reviews/7/_plan-review-s015-round1-verbatim.md:5) |
| 7 | SD desk-v2 plan | SD 87ce4f0 (1133) | **pass**: first parent of a0b472a (definer, the work's first commit) | **pass**: the four inputs and the ruling, all present | **B (ruling)**: 87ce4f0:decisions/questions/P-001-redesign-direction-v2.md:1 | Round 1 FAIL from the Critic and the plan review (_critic-round1:7, _plan-review-round1:7). **In-flight input:** the definer's first act merged the board branch's draft 4 (ac4f882), which is not an ancestor of 87ce4f0, so the start lacks it |
| 8 | POOM S-022 plan | POOM 30cfbaf (520) | **pass**: parent of 0c0380a, the commit reviewed (HEAD:reviews/S-022/_plan-review-s022-round1-verbatim.md:3) | **fail**: no role file (as #2) | **N** (reading 5) | Round 1 FAIL (same file:5) |

### Built work (8)
| # | Piece | Start (count) | F1 | F2 | F3 | Notes |
|---|---|---|---|---|---|---|
| 1 | SD HD1 stage | SD 2c20c9a (2030) | **pass**: the review names it, "HD1's work over 2c20c9a" (HEAD:reviews/HD1/_stage-hd1-review-r1-verbatim.md:3); it is the parent of a1be3ee (builder) | **pass**: .claude/agents/builder.md, specs/S-001.md, docs/PROJECT.md and tests/acceptance/** (1 file), all present; checks/** matches nothing (reading 2); the builder pack is from 2c20c9a:governance/PACKS.toml [roles.builder] | **B (stage)**: 2c20c9a:specs/S-001.md:3727 | Round 1 FAIL from the Reviewer and the Design reviewer (:7 of each) |
| 2 | POOM S-017 build | POOM fb6d0c8 (470) | **pass**: parent of cc7730b (tools-builder); the review is HEAD:reviews/20/reviewer.md:4 | **pass**: .claude/agents/tools-builder.md, specs/S-017-loop-and-alerts.md and docs/LEDGER.md, all present; the role file says "Reads: anything", which names no pack | **B (ledger)**: fb6d0c8:docs/LEDGER.md:1737 (L-0121, "tools-builder builds it on build/tools-bui[lder/s-017]"); no brief file (docs/briefs/ at fb6d0c8 has no s-017) | Round 1 FAIL (reviews/20/reviewer.md:4) |
| 3 | SD M3B VT3 stage | SD 55a2484 (1999) | **pass**: "VT3's work over 55a2484" (HEAD:reviews/M3B/_stage-vt3-design-r1-verbatim.md:3); parent of 5d9b0d2 | **pass** (as #1) | **B (stage)**: 55a2484:specs/S-001.md:3361 | Round 1: the Reviewer PASS (_stage-vt3-review-r1:7), the Design reviewer FAIL (_stage-vt3-design-r1:7). The plan's draft 13 was merged later (fc5607c), after round 1: it is not an ancestor of 99154a5 |
| 4 | POOM S-023/24 build | POOM 6ba7f05 (602) | **pass**: the first parent of both lanes' first commits, the builder's 6788f25 and the orchestrator's 4f41556; the lanes are named at HEAD:reviews/26/reviewer.md:8-9 | **pass**: tools-builder.md, specs/S-023-six-phases.md, specs/S-024-phase-gates.md and docs/LEDGER.md, all present | **B (ledger)** for the builder lane: 6ba7f05:docs/LEDGER.md:1923 and :1938 (the licences for "The joint S-023 and S-024 build"); no brief file | Round 1 FAIL at f7044c7 (reviews/26/reviewer.md:12). **Joint piece:** the orchestrator lane (4f41556..4a9c3eb, 7 commits) has no role file (reading 5). **In-flight input:** the builder's first commit merges 4a9c3eb, the orchestrator lane, made after the start |
| 5 | SD M3E G5 stage | SD 87bac4d (1508) | **pass**: "base 87bac4d" (HEAD:reviews/M3E/_stage-g5-review-r1-verbatim.md:3); parent of 45e09fa | **pass** (as #1) | **B (stage)**: 87bac4d:specs/S-001.md:2590 | Round 1 FAIL from the Reviewer and the Design reviewer (:7 of each) |
| 6 | POOM PR5 build (S-005) | POOM 450c4dd (83) | **pass**: parent of a1ac59d, the builder's first commit; the review names the PR base ea87ed9 and content at bf078f7 (HEAD:reviews/5/_reviewer-round1-verbatim.md:1, :10). 450c4dd is the builder's start, two commits above that base | **pass**: tools-builder.md, docs/briefs/s-005.md, specs/S-005-governance-follow-ups.md, docs/research/003* (2 files), docs/LEDGER.md (L-0052), tools/check_all.sh and tools/surface_guard.py, all present. The brief's "governance/enforcement.toml's warn-only mechanism" (s-005.md:9) is the project path the tools read (450c4dd:tools/govlib.py:1191); in POOM it is template/governance/enforcement.toml, which is present | **R**: 450c4dd:docs/briefs/s-005.md (filed in 450c4dd, "Brief the S-005 build", before the build) | Round 1 FAIL (reviews/5/_reviewer-round1-verbatim.md:6). **Joint piece:** the orchestrator's AC7 commit 7d55a1c sits beside the builder lane (the brief gives AC7 to the orchestrator, s-005.md:5) |
| 7 | SD M3G QW1 stage | SD c2f6f94 (1759) | **pass**: "QW1's work over c2f6f94" (HEAD:reviews/M3G/_stage-qw1-review-r1-verbatim.md:3); parent of 5f62cd7 | **pass** (as #1) | **B (stage)**: c2f6f94:specs/S-001.md:2962 | Round 1: the Reviewer FAIL (:7), the Design reviewer PASS (:7). **In-flight inputs:** the Definer's QW1 notes (2513f0c) and the push branch with G9c landed (725f223) were merged in mid-work |
| 8 | POOM S-014 build | POOM 6c3c9a4 (271) | **pass**: parent of 17d4a1e (tools-builder); the review is of the merge 7a98d07 (HEAD:reviews/7/_build-review-s014-round1-verbatim.md:3) | **pass**: tools-builder.md, docs/briefs/s-014.md, specs/S-014-session-runner.md, template-v3/governance/{PACKS,RUNNER,BRIEFS}.toml, tools/govlib.py and tools/review_check.py, all present | **R**: 6c3c9a4:docs/briefs/s-014.md (the start commit is the brief's own filing, "File the S-014 builder brief") | Round 1 FAIL (same file:5). **In-flight input:** the RUNNER.toml fix 273492c was merged at 1ad2610 |

### Research (8)
| # | Piece | Start (count) | F1 | F2 | F3 | Notes |
|---|---|---|---|---|---|---|
| 1 | SD Q-001 | SD 18d7923 (14) | **pass**: parent of 4e79086, the memo's first commit. 18d7923 (01:51:38) is dated after the dispatch at 01:46:42 (dispatch-log/2026-10.jsonl:5), but it changes only status and dispatch-log files, and every file in the agent's folder is byte-identical there (control manifest, reading 1) | **pass**: the manifest of reviews/Q-001/_control/0-22dc0e573e9a.json (added in 4e79086), namely .claude/agents/researcher.md and research/Q-001.md, sha256 match at 18d7923; BRIEF.md matches the control's brief text; the question names no URL | **R**: the brief text is in the control record's `brief` field (model claude-opus-5-5) | Round 1 FAIL (dispatch-log/2026-10.jsonl:17). The round-1 memo cites 15 URLs (4e79086:research/Q-001-memo.md) (reading 6) |
| 2 | ML Q-001 | (none established) | **fail**: the memo's first commit 78bdbbc has parent 3d252f2, committed at 16:58:40, after the dispatch at 16:56:53 (HEAD:docs/briefs/02-researcher.md:7; sessions/chief-of-staff/session_01QBwHGJH9m3A4Ray7WpHzBo.jsonl:3). The only earlier commit is dafb1de, "Initial commit", and no record shows the tree the agent had | **fail**: the brief names files in two other repositories, POOM (OPERATING_MODEL.md, template-v3/…) and Service-Desk (reviews/, research/, specs/, dispatch-log/, governance/), plus "the web" (02-researcher.md:11); none is in ML at 3d252f2 | **R**: HEAD:docs/briefs/02-researcher.md:7-15, recorded from the helper's transcript on 2026-11-01 (:5) | Round 1 FAIL (research/Q-001-source-check.md:1) |
| 3 | SD Q-002 | SD 18d7923 (14) | **pass** (as #1): parent of c219a90; the dispatch is at :6 | **pass**: the manifest of reviews/Q-002/_control/1-2ed0f3aed3ba.json all matches | **R** (control `brief`) | Round 1 FAIL (:18) |
| 4 | ML Q-002 | (none established) | **fail**: the memo's first commit d879b98 has parent c42334b (18:06:51), which holds Q-003's memo, recorded after the six researchers started at 17:58:49 (session_01QBwHGJH9m3A4Ray7WpHzBo.jsonl:10-15) | **fail**: the question names the subject in POOM, "OPERATING_MODEL.md; … template-v3/.claude/agents/; … BRIEFS.toml and PACKS.toml" (671335c:research/Q-002.md:7); absent from ML | **B (ruling: the question)**: research/Q-002.md; role file .claude/agents/researcher.md; the pack is research/{question}.md, library/** (none) and research/_GROUNDWORK.md (ML governance/PACKS.toml [roles.researcher]); these files are the same at 671335c and c42334b | Round 1 PASS by the first check, with a later-added second check FAIL (Q-008 §2.1); it is in the returned list as Q-008 drew it |
| 5 | SD Q-004 | SD 18d7923 (14) | **pass** (as #1): parent of ea94e82; the dispatch is at :8 | **pass**: the manifest of reviews/Q-004/_control/3-9d41b24ca75f.json all matches | **R** | Round 1 FAIL (:21) |
| 6 | ML Q-003 | ML 671335c (17) | **pass**: parent of c42334b, the first of the six recordings. 671335c (17:58:15) predates the start at 17:58:49 (session lines :10-15) | **fail**: 671335c:research/Q-003.md:7 names the POOM files, absent | **B (the question)**: as #4 | Round 1 PASS by the first check, then the later-added check FAIL |
| 7 | SD Q-005 | SD 77aa913 (28) | **pass** (as #1): parent of 739d7d9; the dispatch at :33 (10:45:54) precedes 77aa913 (10:51:02), which changes only status and dispatch-log files | **pass**: the manifest of reviews/Q-005/_control/3-6dcc64a42ffe.json all matches | **R** | Round 1 FAIL (:45) |
| 8 | ML Q-004 | (none established) | **fail**: the memo's first commit f54d6d7 has parent d879b98, which holds the Q-002 and Q-003 memos, recorded after the start at 17:58:49 | **fail**: 671335c:research/Q-004.md:7 names the POOM files, absent | **B (the question)**: as #4 | Round 1 PASS by the first check, then the later-added check FAIL |

SD research start counts are from `git -C /home/user/Service-Desk rev-list --count <start>`.

## The records check: first-time-pass pieces (6), reported beside, not in the thresholds
| Piece | How chosen | Start | F1 | F2 | F3 |
|---|---|---|---|---|---|
| SD HD1 plan | Q-008 §2.2 | SD 548031e (2026) | **pass**: parent of f6c194c (definer), the commit reviewed (HEAD:reviews/HD1/_plan-review-r1-verbatim.md:3) | **pass**: the four definer inputs and the ruling file, all present | **B (ruling)**: 548031e:decisions/questions/P-001-headers-approve.md:1 ("Ruling: B") and :8 (option A: "the Definer writes it into the spec …"). Round 1 PASS from the Reviewer and the Design reviewer (:7 of each) |
| POOM S-027 plan | Q-008 §2.2 | POOM 93ed08c (645) | **pass**: parent of 7c81268, the commit reviewed (HEAD:reviews/S-027/_plan-review-s027-round1-verbatim.md:7) | **fail**: no role file (reading 5) | **N**. Round 1 PASS (:5) |
| SD Q-008 | Q-008 §2.1 | SD c0e360d (227) | **pass** (as research #1): parent of 3a54748 | **pass**: all 46 entries of the manifest of reviews/Q-008/_control/2-970092bed9e7.json match, library entries included | **R**. Round 1 PASS (dispatch-log/2026-10.jsonl:135). The round-1 memo cites 23 URLs |
| SD Q-013 | Q-008 §2.1 | SD cc23b06 (490) | **pass**: parent of 3a6c6c9, which adds the round-1 memo and control 0-2888fc13a8b3 (dispatched 21:36:11) | **pass**: all 92 entries of that manifest match at cc23b06 | **R**. Round 1 PASS (:262). **Anomaly:** no dispatch line for the 21:36:11 session is in the log. A second session (21:42:17, :258) was ignored as an anomaly (:260), yet its commit 7a36033 rewrote research/Q-013-memo.md (98+/52−) before the source check was dispatched (:261). So the memo the check saw may be the second session's, while the outcome (:259) credits the first |
| SD built: followups | The first PASS in Q-006 §4's list (ML research/Q-006-memo.md:250, "PASS (15): followups, …"), with one round only (reviews/S-001-followups/ holds one build-review file) | SD 706eb45 (722) | **pass**: the range "706eb45..914c06d" (HEAD:reviews/S-001-followups/_build-review-round1-verbatim.md:3); parent of 2170e52 (builder) and of 2b81fa8 (chief-of-staff) | **pass**: the builder inputs, all present | **B (stage)**: 706eb45:specs/S-001.md:413-416 ("Where the build stands (amendment of 2026-10-17 …)"). Round 1 PASS (:1). **Joint piece:** Chief of Staff commit 2b81fa8 |
| POOM built: S-007 build | Q-008 §2.3 order: S-002 first, which failed rounds 1–3 (HEAD:reviews/1/reviewer.md:7); then the reviews/7 builds, of which S-007 is first, and it passed round 1 (HEAD:reviews/7/_build-review-s007-verbatim.md:6, the only S-007 build-review file) | POOM 8c60a80 (175) | **pass**: parent of 9aa70fb, the builder's first commit; the review range is 7eaad1a..7bf761c (:4), and the orchestrator's lane starts at 7eaad1a | **pass**: tools-builder.md, specs/S-007-v3-layout-and-templates.md and docs/LEDGER.md, all present | **B (ledger)**: 8c60a80:docs/LEDGER.md:1047 (L-0071: "tools-builder writes the tests first, then scripts/new-project-v3.sh and scripts/new-portfolio.sh, on build/tools-builder/s-007"). Not R: docs/briefs/s-007.md was filed at b8d54f9 (16:11, after the build) as "Recorded after the fact … the text below is its substance" (:5), so it is substance, not text, and it is dated after the start, so it is not used. Round 1 PASS. **Joint piece:** orchestrator commits 1c90817, 8c60a80 and 36f25b9 |

## The web-free research stratum (reported separately)
The Builder counted these directly from each memo's sources statement, over the 19 memos Q-008 counts (SD Q-001, -002, -004 to -013; ML Q-001 to Q-007), in both their round-1 text and today's.
- **SD:** none. Every round-1 memo cites web URLs, from 5 (Q-006) to 36 (Q-011), and none states that no web was used. Examples: 739d7d9:research/Q-005-memo.md:13 ("Web searches: 5"); 1477af0:research/Q-006-memo.md:45 ("I ran two web searches"); 3a54748:research/Q-008-memo.md:5 ("read … through web search and web fetch").
- **ML:** one, Q-006 (c55d934:research/Q-006-memo.md:10, "No web sources were used"; 0 URLs).
  - Q-005 used search-result extracts and states "no web page was opened directly" (f37a8ff:research/Q-005-memo.md:26). That is web use, so it is not counted.
  - The other five cite 16 to 43 URLs.

| Piece | Start | F1 | F2 | F3 |
|---|---|---|---|---|
| ML Q-006 | (none established) | **fail**: the memo's first commit c55d934 has parent 50d1c5a (18:09:03, the Q-003 source check's verdict), recorded after the start at 17:58:49 | **fail**: the question names Service-Desk's records (671335c:research/Q-006.md:5) and the POOM files (:7), all absent from ML | **B (the question)**. Round 1 FAIL (research/Q-006-source-check.md:1) |

## Measures (E-001, "Measure")
**Records share**, returned pieces passing F1–F3, out of those audited, by brief grade:

| Kind | Audited | Pass, recorded brief | Pass, rebuilt brief | Pass, either | Fail |
|---|---|---|---|---|---|
| Plans | 8 | 0 of 8 | 4 of 8 (SD M3B, M3C, after-glance, desk-v2; 2 of them, M3B and M3C, rest on a milestone line, reading 3) | 4 of 8 | 4: every POOM plan (F2 and F3, reading 5) |
| Built work | 8 | 2 of 8 (POOM PR5, S-014) | 6 of 8 (SD HD1, VT3, G5, QW1: stage; POOM S-017, S-023/24: ledger) | 8 of 8 | 0 |
| Research | 8 | 4 of 8 (SD Q-001, -002, -004, -005) | 0 of 8 | 4 of 8 | 4: every ML piece (F2; and F1 for Q-001, Q-002, Q-004) |

Reported beside, not added in:
- **First-time-pass pieces:**
  - plans 1 of 2 (HD1 plan, B; S-027 N);
  - research 2 of 2 (SD Q-008 and Q-013, both R);
  - built 2 of 2 (SD followups, POOM S-007 build, both B).
- **Web-free stratum:** 1 memo counted (ML Q-006), 0 pass F1–F3.

**Run result** (replays passing F4–F7, out of those run): see "Step 2: measures" below.

**Pool for M2** (records share × returned pieces of the kind; returned pieces only):

| Kind | Returned pieces | Recorded-brief share | Pool, recorded | Recorded-or-rebuilt share | Pool, recorded or rebuilt |
|---|---|---|---|---|---|
| Plans | 42 | 0/8 | 0 | 4/8 | 21 |
| Built work | 48 | 2/8 | 12 | 8/8 | 48 |
| Research | (web-free memos passing F1–F3, counted directly) | — | 0 | — | 0 |

Each pool holds for work that was sent back only. It says nothing about work that passed first time.

**Cost:** step 1 started no helper sessions. Step 2's cost per run is under "Step 2: cost" below.

## The working copies, and runs F4–F7 (as written at step 1; step 2 below supersedes it)
- **Copies made:** none. Each copy's two checks (the `rev-list --count` equality and the later-commit `cat-file` failure) were therefore not run. The start-commit counts above are the full clone's side of the first check.
- **Runs:** none started. There are no F4–F7 verdicts and no transcript paths.
- **What step 2 would take, by its rule.** Recorded for the next attempt only; not a run plan the Builder has started. 8 places, rotating plans, built work and research as 3, 3 and 2, recorded briefs first, in list order:
  - **Plans:** SD M3B, SD M3C, SD after-glance. All are rebuilt, since no plan has a recorded brief.
  - **Built work:** POOM PR5 (R), POOM S-014 (R), SD HD1 (B).
  - **Research:** the web-free memos first, but none passes. Then, by list order, SD Q-001 and SD Q-002 (R), unless the Reviewer rules on reading 6 that these cannot take research places.

## Step 2: the replay runs

In plain words: six of the eight places the registration's rule names were replayed, and four of those replays were judged. The two Personal-Org-Operating-Model places (built work, both with a recorded brief) were not run, because this session could not get access to that repository. Of the three plan replays, all three finished a spec draft and got a verdict (two FAIL, one PASS). The one built-work replay finished its change, but its check run ended without a verdict. Both research replays stopped without a memo, because the confinement bars the web and the role bars memory as a source. Three things for the Reviewer to rule on: reads of the helpers' own saved command output under /root, one browser lookup under /root, and context the harness gave every helper.

Run by the Builder, session_01QBwHGMu36mvZdxN2ssBspJ (a top-level session), 2026-11-03. Every helper was started with the Agent tool, as a general-purpose subagent, with `model: opus` for replays and `model: fable` for check runs. Each transcript records the served model: claude-opus-5-5 for every replay and claude-fable-5-1 for every check run.

### Set-up
- **Clones.** Service-Desk was cloned with full history (`git rev-parse --is-shallow-repository` → `false`, 2,275 commits). Model-Lab was already complete (`git fetch --unshallow` → "on a complete repository"). Personal-Org-Operating-Model could not be attached: `add_repo` was denied by the session's permission check, and the repository is private, so a plain clone asked for credentials. **POOM PR5 and POOM S-014 were therefore not run** (see "Places not run").
- **The places, by the rule** (rotation plans, built work, research, 3, 3, 2; recorded briefs first, in list order; from step 1's table):
  - plans: SD M3B, SD M3C, SD after-glance (all rebuilt);
  - built work: POOM PR5 (R), POOM S-014 (R), SD HD1 (B);
  - research: no web-free memo passes F1–F3, so SD Q-001 and SD Q-002 (R), the first returned research pieces passing F1–F3. Step 1's reading 6 notes that both did their original work on the web.
- **Working directory.** The Agent tool offers no working-directory parameter. A one-file hook added to this session (`agent.spawn`) set each helper's working directory from a first prompt line `CWD: /home/user/wt/e001/<copy>` and removed that line, so the helper received exactly the brief. Its whole code:
  ```ts
  const MARKER = /^CWD: (\/home\/user\/wt\/e001\/[A-Za-z0-9._\/-]+)\n/
  on('agent.spawn', ($, e, next) => {
    const m = MARKER.exec(e.prompt)
    if (!m || m[1].includes('..')) return next(e)
    return next({ ...e, cwd: m[1], prompt: e.prompt.slice(m[0].length) })
  })
  ```
  For all 10 runs, the transcript's only `cwd` value is the run's copy, the helper's metadata gives the same `cwd`, and the transcript's first message equals the brief file byte for byte (`brief_match.py` → `match`).
- **Copies.** All 10 are under /home/user/wt/e001/, outside every clone. Each was made as step 2.1 says (`git init`; `git fetch --no-tags <source> <full sha>`; `git checkout --detach FETCH_HEAD`). Replay copies fetch from the Service-Desk clone. Check copies fetch the replay's commit from the replay copy. The two checks for each copy are in `copies_step2.txt`:

  | Copy | Commit | rev-list --count copy = source | Later commit absent |
  |---|---|---|---|
  | sd-m3b-plan | 3bfe663 | 1919 = 1919 | 31ff26d fails (pass) |
  | sd-m3c-plan | d2a1d60 | 2074 = 2074 | e477cc2 fails (pass) |
  | sd-afterglance-plan | 2d0edb0 | 1445 = 1445 | 671eada fails (pass) |
  | sd-hd1-build | 2c20c9a | 2030 = 2030 | 374c7d9 fails (pass) |
  | sd-q001-research | 18d7923 | 14 = 14 | 4e79086 fails (pass) |
  | sd-q002-research | 18d7923 | 14 = 14 | c219a90 fails (pass) |
  | sd-m3b-plan-check | 86fdcfa | 1920 = 1920 | none later exists (skipped by rule); the original round-1 31ff26d fails |
  | sd-m3c-plan-check | b1c13f9 | 2075 = 2075 | skipped by rule; e477cc2 fails |
  | sd-afterglance-plan-check | 9bdc956 | 1446 = 1446 | skipped by rule; 671eada fails |
  | sd-hd1-build-check | 8d6435f | 2031 = 2031 | skipped by rule; 374c7d9 fails |

  The first-try fetch with short shas failed ("couldn't find remote ref") into the same empty repositories, before any checkout. It was redone with full shas, and nothing else was in them.
- **Briefs.** Every brief, as sent, is in `briefs/`. The rebuilt briefs fill the template from files at the start commit:
  - role file: `.claude/agents/<role>.md`;
  - task: SD M3B from 3bfe663:docs/PROJECT.md:113; SD M3C from d2a1d60:docs/PROJECT.md:117; SD after-glance from 2d0edb0:decisions/questions/P-001-glance2-{anchor,arrow,counts,palette,standard}.md:1 and docs/design/references/owner-request-2026-10-24-glance-emphasis.md:62-72; SD HD1 from 2c20c9a:specs/S-001.md:3727, the stage row;
  - Read first: the role's `must_read` in governance/PACKS.toml at the start commit, in order. The definer has `docs/PROJECT.md, library/**, {ruling}`, where `{ruling}` is unset for M3B and M3C and is the five ruling files for after-glance. The builder has `specs/{spec}.md, docs/PROJECT.md, tests/acceptance/**, checks/**`. The spec path follows as the template's last field, which repeats specs/S-001.md for HD1;
  - Hand back: a spec draft at specs/S-001.md for plans, and for HD1 a change to code or tests at the paths the task statement names.

  The recorded briefs (SD Q-001, Q-002) are the control records' `brief` field (4e79086:reviews/Q-001/_control/0-22dc0e573e9a.json; c219a90:reviews/Q-002/_control/1-2ed0f3aed3ba.json), unchanged. They contain no absolute path, plus the confinement paragraph.
- **Judge briefs.** These fill E-002's template.
  - **The checker** is the role that does that kind's check at the start commit: the critic for plans (the definer's role file hands off "to the Critic (plan review)", 3bfe663:.claude/agents/definer.md:41); the reviewer for built work. Research would take the source checker; no research replay reached a check.
  - **"Judge it against"** names the task-statement record: docs/PROJECT.md:113 and :117; the five ruling files and the owner-request lines; specs/S-001.md:3727.
  - **The original's checks.** Each original plan or stage went to more than one checker in round 1 (for example the Critic, the Reviewer and the Design reviewer for M3B). The template takes one checker role, so each replay had one check run.

### Runs, with F4–F7
F4 lines are transcript lines (`f4_scan.py <jsonl> <copy>`), and "flagged" counts the calls the scanner flags. The Builder reads each flagged line and sorts it here, except the borderline kinds, which the registration leaves to the Reviewer.
- **F5.** No brief names a script to run, except that HD1's stage row names the tests to lock.
- **F6.** The test is: the deliverable of its kind; at least one path the original round-1 submission changed; nothing outside the role's write lane at the start commit (definer: specs/**, experiments/**; builder: src/**, tests/**, not tests/acceptance/**, docs/handover/**; researcher: none).

| Run | Piece (grade) | F4, no leak | F5, tools | F6, finishes | F7, checkable | Check run | Recorded round 1 |
|---|---|---|---|---|---|---|---|
| 1 replay | SD M3B plan (B) | **Borderline, for the Reviewer:** lines 23 and 79 Read the helper's own command output, which the harness saved under /root/.claude/projects/…/tool-results/ because it was too large to show inline (lines 21 and 77 are the tool results that name those files, showing the copy's docs/PROJECT.md and specs/S-001.md). No other call outside the copy. Every other /tmp use is files the run created (lines 140-166, scratchpad/m3b) | pass (no script named) | **pass**: commit 86fdcfa (line 198, hand-back line 201) changes specs/S-001.md only, which the original 31ff26d changed; it is in the definer lane | run 2 | **FAIL** (run 2, hand-back line 132) | FAIL (Critic, Reviewer, Design reviewer) |
| 5 replay | SD M3C plan (B) | **pass**: 2 flagged, both false positives. Line 203 is a Python edit of specs/S-001.md whose text contains `https://needs-you.pages.dev`; line 215 is a `sed` edit whose pattern holds "/the". Scratchpad use is its own files (line 158, scratchpad/m3c) | pass (no script named) | **pass**: commit b1c13f9 (line 215, hand-back 218) changes specs/S-001.md only, as did the original b26e876/e477cc2 | run 8 | **FAIL** (run 8, hand-back line 154) | FAIL (Reviewer) |
| 7 replay | SD after-glance plan (B) | **Borderline, for the Reviewer:** line 48 Reads its own saved output under /root/.claude/…/tool-results/, as in run 1. Scratchpad use is its own files (lines 158-178) | pass (no script named) | **pass**: commit 9bdc956 (line 201, hand-back 204) changes specs/S-001.md only, as did the original 671eada | run 9 | **PASS** (run 9, hand-back line 139) | FAIL (Critic, Reviewer) |
| 3 replay | SD HD1 stage (B) | **Borderline, for the Reviewer:** line 90 runs `ls ~/.cache/ms-playwright` (a path under /root, looking for a browser; the listing printed nothing) and `which chromium chromium-browser google-chrome` (finds /usr/bin/google-chrome). Line 42 writes the suite's output to the scratchpad (scratchpad/base.txt, its own file). 8 more flagged, all false positives from strings in commands: CSS (`600 28px/1.2`, `/font:`), regexes (`/1\.3`), file globs (`/.test`) and the desk's own hash routes (`#/p/Service-Desk`, `#/waiting`), in lines 126, 130, 149, 152, 194, 201, 238 and 262. It ran Chromium through Playwright on a scratch page inside the copy (`.hd1-scratch/`, deleted) | **pass**: the suite ran in the copy, 1553/1553 before the change (line 42) and 1557/1557 after (lines 248-258); surface_guard at line 266 | **pass**: commit 8d6435f (line 269, hand-back 275) changes 15 files under src/ and tests/, 14 of which the original's 2c20c9a..374c7d9 changed; all are in the builder lane. The helper reports one clause of the stage row not met: the one-line headings at 360 px | run 10 | **fail**: run 10 returned no verdict line. Its last message (transcript line 148) is "Waiting on the two test runs; nothing else is independent of their result.", and the session then ended with no hand-back | FAIL (Reviewer, Design reviewer) |
| 4 replay | SD Q-001 research (R) | **pass** (0 flagged, 5 calls) | pass (no script named) | **fail**: no memo. Hand-back line 35 is "BLOCKED. I wrote no memo": the brief bars the web, the role bars memory as a source (.claude/agents/researcher.md, "Never"), and the copy holds no library | not judged | — | FAIL |
| 6 replay | SD Q-002 research (R) | **pass** (0 flagged, 4 calls) | pass (no script named) | **fail**: no memo (hand-back line 28, "blocked, no memo produced", the same reasons) | not judged | — | FAIL |

Check runs' own transcripts, where E-001 asks for no F4: run 2 Reads its own saved output under /root/.claude/…/tool-results/ at line 34; run 8 at line 55; run 10 at lines 69, 78, 79, 88 and 96. Run 9 has 0 flagged.

**The verdicts, first lines as returned** (hand-back lines above):
- **Run 2, SD M3B replay: `Verdict: FAIL`.** One blocking finding: specs/S-001.md:3241-3243, reading (c), "the board's count on Home is a showing", against docs/PROJECT.md:195-196 and :416-417. Four non-blocking findings.
- **Run 8, SD M3C replay: `Verdict: FAIL`.** One blocking finding: specs/S-001.md:13987 (and :3795), "each step before the archive is undone in a minute or two", against the rollback paragraph :19985-19989 and :3917, :17313. Seven non-blocking findings.
- **Run 9, SD after-glance replay: `Verdict: PASS`.** No blocking findings; seven non-blocking.
- **Run 10, SD HD1 replay:** no verdict line.

### Step 2: measures
**Run result** (replays passing F4–F7, out of those run), by kind and brief grade. "F4 open" means F4 passes only if the Reviewer accepts the borderline lines above.

| Kind | Grade | Places by the rule | Run | Pass F4–F6 | Pass F4–F7 | Notes |
|---|---|---|---|---|---|---|
| Plans | recorded | 0 (no plan has a recorded brief) | 0 | — | — | |
| Plans | rebuilt | 3 | 3 | 3 (2 with F4 open: M3B, after-glance) | 3 (2 with F4 open) | M3C is the only plan replay with no borderline F4 line |
| Built work | recorded | 2 (POOM PR5, S-014) | **0** | — | — | not run: no access to POOM |
| Built work | rebuilt | 1 (SD HD1) | 1 | 1 (F4 open: line 90) | **0** | F7 fails: no verdict line |
| Research | recorded | 2 (SD Q-001, Q-002, by reading 6) | 2 | 0 | 0 | F6 fails for both: no memo |
| Research | web-free stratum | 0 pass F1–F3 (step 1) | 0 | — | — | |

**Beside the recorded round 1** (reported, not deciding; E-001 "Measure"):
- **SD M3B.** Replay FAIL; the original FAIL from all three checkers.
- **SD M3C.** Replay FAIL; the original FAIL.
- **SD after-glance.** Replay PASS; the original FAIL from the Critic and the Reviewer. This is the one gap. Its likeliest causes:
  - different work: the replay's draft is not the original's;
  - one checker instead of two: the original also had the Reviewer, which ran the repository checks and the desk tests, and found six points;
  - a different judge, of unrecorded model.
- **SD HD1.** No replay verdict; the original FAIL.
- **SD Q-001, Q-002.** Not judged; the originals FAIL.

**Records share and pool:** unchanged from step 1 (above); step 2 adds no audit.

### Step 2: cost
As each helper reported at return (the task notification's usage):

| Run | Kind | Piece | Model (served) | Tokens | Tool uses | Time (s) |
|---|---|---|---|---|---|---|
| 1 | replay | SD M3B plan | claude-opus-5-5 | 199,653 | 52 | 613.3 |
| 2 | check | SD M3B plan | claude-fable-5-1 | 152,649 | 32 | 334.3 |
| 3 | replay | SD HD1 stage | claude-opus-5-5 | 302,073 | 80 | 1,822.7 |
| 4 | replay | SD Q-001 | claude-opus-5-5 | 67,141 | 5 | 32.9 |
| 5 | replay | SD M3C plan | claude-opus-5-5 | 194,530 | 53 | 568.6 |
| 6 | replay | SD Q-002 | claude-opus-5-5 | 63,806 | 4 | 30.7 |
| 7 | replay | SD after-glance plan | claude-opus-5-5 | 263,131 | 51 | 641.8 |
| 8 | check | SD M3C plan | claude-fable-5-1 | 194,442 | 37 | 506.5 |
| 9 | check | SD after-glance plan | claude-fable-5-1 | 148,837 | 32 | 345.0 |
| 10 | check | SD HD1 stage | claude-fable-5-1 | 166,148 | 33 | 251.3 |
| | | **Total** | | **1,752,410** | **379** | **5,147.2** |

Runs 1, 3, 5 and 7–10 ran with other helpers alongside them, so their times overlap. **Runs started: 10 of 20** (6 replays of at most 8, 4 checks of at most 8, 0 reruns).

### Places not run
- **POOM PR5 and POOM S-014** (built work, recorded brief). Both pass F1–F3 (step 1), and the rule names them. They were not replayed because the session could not reach Personal-Org-Operating-Model: the attach tool was refused, and the repository is private.
- No other piece was put in their places. The rule's "a kind that runs short" is about pieces failing F1–F3, and these two pass; whether they can still be run is for the orchestrator. If they are, they take 2 replay runs and up to 2 check runs, inside the 10 left.

### Readings and limits (for the Reviewer)
1. **Context the harness gave every helper, beyond the brief.** It is not a tool call, so F4 does not cover it, but it bears on faithfulness. Each helper's system context (transcript lines 4 and 7) held this session's project instructions (Model-Lab's CLAUDE.md, which points to Model-Lab's AGENTS.md), this session's id in the commit-attribution note, the scratchpad's path, and a list of available tools including WebFetch and WebSearch. The replays copied this session's id into their commit trailers (`Agent-Session: session_01QBwHGMu36mvZdxN2ssBspJ`, e.g. run 1's hand-back), and three (runs 1, 3, 5) cite "CLAUDE.md" for leaving co-author lines out. Both Model-Lab's and Service-Desk's CLAUDE.md say this (Service-Desk 3bfe663:CLAUDE.md:16), so which one each meant is not clear. No helper's tool call read a Model-Lab file.
2. **Saved command output under /root** (runs 1, 7 and the check runs). The harness writes a too-large tool output to /root/.claude/projects/<session>/tool-results/ and tells the helper to read it there. The file holds only that helper's own output from inside its copy. By F4's wording, any path under /root fails. Whether a harness-saved copy of the helper's own output is such a path is the Reviewer's ruling. It decides F4 for runs 1 and 7.
3. **HD1's browser lookup** (run 3, line 90): `ls ~/.cache/ms-playwright` under /root, looking for the tool the work needed. It decides F4 for run 3.
4. **The shared scratchpad.** Every helper was told of the same scratchpad folder under /tmp. `scratch_scan.py` lists every scratchpad file each run named: no file is named by two runs, and no run lists the folder. So no run read another's file, as far as tool-call text shows.
5. **Helpers ran in parallel** (runs 1–3, 5, 7–10 overlapped). The hook sets the working directory per helper, and each transcript's cwd is its own copy only.
6. **Research replays.** Both stopped for the reason step 1's reading 6 foresaw. The originals used the web; the confinement bars it; the researcher role bars memory. The copies also expose files the original researchers' folders did not hold (docs/PROJECT.md, queue/, decisions/; both helpers say they did not open them, and Q-002's grep listed docs/PROJECT.md's name in its results).
7. **Run 10's end.** The judge started two test runs in the background, wrote that it was waiting on them, and its session ended with no hand-back. The Builder did not prompt it further, since any added message would change the judge brief that E-002 requires to be the same for every judgement. A rerun is allowed only for F4/F5 set-up faults, so none was made.
8. **Transcripts.** The 10 transcripts are in this session's folder, `/root/.claude/projects/-home-user-Model-Lab/121cbe4f-db70-5bc2-846b-22ce591f8402/subagents/agent-<id>.jsonl`, with the ids in `runs_step2.tsv`. **They are not yet copied into `src/E-001/transcripts/`**: the copy was refused by the session's permission check, and it waits on the owner. Each replay's output commit is saved as a patch in `replay_outputs/`.

### Files added at step 2 (src/E-001/)
- `briefs/`: the 10 briefs as sent.
- `copies_step2.txt`: each copy's two checks.
- `runs_step2.tsv`: each run, agent id, copy, cost and outcome.
- `f4_scan.py`, `brief_match.py`, `scratch_scan.py`: the scripts used above.
- `replay_outputs/*.patch`: the four replays' commits.

## Pieces used (for M2's held-back set and test pool)
- **Audited, returned:**
  - SD M3B plan, POOM S-007 plan, SD M3C plan, POOM S-012r plan, SD after-glance plan, POOM S-015 plan, SD desk-v2 plan, POOM S-022 plan;
  - SD HD1 stage, POOM S-017 build, SD M3B VT3, POOM S-023/24 build, SD M3E G5, POOM PR5, SD M3G QW1, POOM S-014 build;
  - SD Q-001, ML Q-001, SD Q-002, ML Q-002, SD Q-004, ML Q-003, SD Q-005, ML Q-004.
- **Audited, first-time-pass:** SD HD1 plan, POOM S-027 plan, SD Q-008, SD Q-013, SD followups build, POOM S-007 build.
- **Audited, web-free:** ML Q-006.
- **Replayed (step 2):** SD M3B plan, SD M3C plan, SD after-glance plan, SD HD1 stage, SD Q-001, SD Q-002. **Judged by a check run:** the first four.

## Open points for the Reviewer
1. **Reading 3, milestone lines as task statements.** It decides whether SD M3B and M3C are rebuilt or neither. The plans' rebuilt share would go from 4 of 8 to 2 of 8.
2. **Reading 5, AGENTS.md as the POOM orchestrator's role file.** It decides whether the four POOM plans and S-027 can be rebuilt.
3. **Reading 6, research pieces that pass F2 as worded but did their task on the web.** The four SD scripted pieces, which may take research places in step 2.
4. **Replay faithfulness beyond F1–F3, which this check does not grade.**
   - Three built pieces took in material made after their start, within round 1: QW1, S-014 and S-023/24.
   - So did one plan: desk-v2's board draft.
   - The SD scripted researchers worked in a folder holding only their manifest files (3, 46 or 92 files, by manifest), not a whole repository. A replay copy built by step 2.1 exposes the whole repository at the start commit, including status/ and the dispatch log.
