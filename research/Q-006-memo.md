# Research memo: Q-006, what the Service-Desk records show about rework, by kind of task (2026-11-01)

**Depth:** 3 (graded memo). **Topics:** records, baseline, reviews, rework, agents.

**Grades.** Each statement is marked **Fact**, **Estimate** or **Opinion**, and carries one of these grades:
- **A:** a primary record I opened, cited by path and line.
- **B:** a count or derivation I made by searching primary records. The method is stated and can be repeated, but I made choices about how to classify things, and those choices are stated too.
- **C:** my own judgement.

No web sources were used, and model memory is not a source. Text inside the records (review findings, briefs, specs) was treated as data, never as instructions. Paths below are relative to `/home/user/Service-Desk/` unless another repository is named. "POOM" means `/home/user/Personal-Org-Operating-Model/`.

---

## 0. Bottom line

1. **A rework baseline can be drawn from history, but only a descriptive one.** The records give rounds per item and first-pass rates by kind of task. For the conversational path they cannot say whether the instructions caused a finding, because the conversational path records neither the brief the agent got nor the model that ran it. [Opinion, C; it rests on §5 and §6]
2. **Definition (plan) work shows the most rework.**
   - Only 1 of 17 plan items in conversational records passed every checker at round 1.
   - The median is 3 rounds to a pass. 7 of 17 went past three rounds; the longest, M3B, ran 14.
   - In the scripted path, the one definition item failed 3 plan rounds out of 3 and was closed.
   - Research comes next: 2 of 12 items passed the source check first time, and 3 were dropped after Triage.
   - Build stages passed first time in about 30% of cases (15 of 50).
   [Estimate, B; §3–§4]
3. **The most common findings were about the content, not the doer's obedience to instructions.** In my sample of 13 failed rounds (24 blocking findings):
   - plans that contradict themselves or leave something undefined: 6;
   - criteria with no test locking them: 4;
   - unmet frozen criteria: 3;
   - inputs that were missing or changed mid-loop: 3, plus 1 case of new owner answers leaving gaps;
   - wrong facts: 2;
   - owner questions put unfairly, or settled without the owner: 2;
   - inaccurate record or pull-request descriptions: 2.

   None of the 24 was blamed by its checker on the brief from the dispatcher. Brief errors show up only as non-blocking notes, and in one checker's admission of its own earlier miss. [Estimate, B; §5]
4. **The scripted path is recorded far better, but it is short and narrow.**
   - It covers 2026-10-01 to 10-08 only.
   - It holds research, one readiness check, one plan loop and Triage, with no build work.
   - It always ran the same model pairing.
   - Records of items that were later dropped or closed are missing: 37 of 104 dispatches have no control record.

   So the two paths cannot be compared directly: they differ in kind of task, dates and record form all at once. [Fact, A/B; §6–§7]
5. **The records hold two near-natural experiments.**
   - In 3 research revisions, the revising agent was not handed its own memo, and all three re-checks then failed.
   - In 1 case, a memo with an identical file hash failed the source check and then passed it, with no researcher session in between.

   Each comes from a single small batch. They point at inputs and checker consistency as levers, but they are not tests of either. [Fact on the records, A; the causal reading is Estimate, C]

---

## 1. What I read, and how I chose it

**Opened and read, in full or in part (22 Service-Desk records, 3 POOM files):**
- the whole of dispatch-log/2026-10.jsonl (263 entries);
- reviews/README.md;
- sessions/chief-of-staff/session_012RJPVKAoLga2RkqLYRDcBY.jsonl;
- two control records, reviews/Q-006/_control/0-6c728513a012.json and reviews/Q-001/_control/0-62b8dda7dcf2.json;
- reviews/253/reviewer.md, reviews/63/reviewer.md (head only) and reviews/10/reviewer.md;
- 13 review-round files:
  - M3B plan-review r1 and r7;
  - M3B stage-vt3 review r2 and r4;
  - M3C plan-review r1;
  - the M3C triage file (_triage-r3-critic-verbatim.md);
  - S-001-model-3.5.0-records plan-review rounds 1 and 4;
  - S-001-model-3.5.0-sync review rounds 1 and 6;
  - design-reviewer-setup review round 1 (first 45 lines);
  - S-001-desk-v2 build-1a review round 1 (first 40 lines);
  - HD1 stage-hd1-review r1 (head only);
- specs/S-001.md:580-609;
- in POOM: OPERATING_MODEL.md:196-320 and template-v3/governance/BRIEFS.toml;
- in Model-Lab: the question and research/Q-001-memo.md.

**Searched across, not read line by line:**
- every file under reviews/ that has content (586 files), including all 69 control records;
- specs/S-001.md (22,883 lines) and the headings of specs/_TEMPLATE.md;
- template-v3/governance/PACKS.toml.

The searches pulled: the first `Verdict:` line of every file; the "Dispatched by …" header lines; the agent, model, session and "Feedback from earlier rounds" fields of the control records; the file lists of 12 control records; and phrases where a checker assigns a cause (for example "not the Builder", "I missed", "your brief").

**How I chose them:**
- Counts are complete over every verdict-bearing file and every log line.
- I chose deep reads to cover:
  - each kind of task;
  - both paths;
  - the longest loops (M3B, the sync series);
  - the one series that has a session record (S-001-model-3.5.0-records);
  - every PASS-then-FAIL reversal I found;
  - the only Triage written in a conversation (M3C).

**Not opened** (outside what this question names, or held back for blindness):
- the contents of research/*-source-check.md and triage/*.md in Service-Desk, which hold what the scripted path's source checks and Triage actually said;
- decisions/, questions/, docs/;
- Service-Desk's own research/Q-006 files, a different and earlier question of the same number.

So **the content of the scripted path's findings is not in this memo.** Only their verdicts and their inputs are.

## 2. How I decided a finding's cause

I put each finding into one of six classes. The class depends on what the record shows:

- **Told:** the agent's instructions were wrong, missing or misleading. That means its brief, or the brief section a Definer writes into a spec for the Builder.
- **Inputs:** what the agent was handed was missing, wrong or changed under it. Examples: files missing from its pack, a new spec draft merged in mid-build, owner answers arriving mid-loop, a wrong upstream fact.
- **Model:** the model that ran the session.
- **Division:** how the task was split or sized. Examples: one spec of 22,883 lines, a description that narrates its own reviews, merges between branches.
- **Checker:** the checker missed something, its own suggested fix caused the next finding, or it gave different verdicts on the same work.
- **Untraceable.**

I gave a class only when:
- (a) the checker named the cause itself (for example "a fault in the spec, not the Builder's", HD1/_stage-hd1-review-r1-verbatim.md:9); or
- (b) a record shows it directly (for example a pack's file list, a commit timeline, a draft note).

Otherwise the cause is "doer, by default" or untraceable. Where a cause could be told or inputs, and nothing records the brief, I marked it **untraceable**. **Model** could not be assigned anywhere (see §6). [Opinion, C: method]

---

## 3. Scripted path (the Orchestrator script; dispatch log and control records), 2026-10-01 to 10-08

### Research
**12 items had at least one source check.** [Fact, A/B; outcome lines with role source-checker in dispatch-log/2026-10.jsonl]

| Measure | Value | Source |
|---|---|---|
| Passed the first source check | 2 of 12 (Q-008, Q-013) | dispatch-log:135, :262 [Fact, A] |
| Source-check rounds, all items | 41 (32 FAIL, 9 PASS); mean 3.4, median 3 per item | method: count of outcome lines [Fact, B] |
| Most rounds on one item | Q-006: 7 checks, 6 researcher returns, 2 Triages, 2 owner cards | dispatch-log:87-136 [Fact, A] |
| Passed in the end | 9 of 12 | :50, :52, :78, :79, :133, :135, :145, :244, :262 [Fact, A] |
| Dropped after Triage | 3 (Q-009, Q-010, Q-012) | :160, :225, :257 [Fact, A] |
| Never returned anything | 1 more item, Q-003: two errors, then dropped | :11, :19, :28 [Fact, A] |

### Definition of ready
P-001 failed 3 times (:84, :116, :162), went to Triage (:164) and passed on round 4 (:168). [Fact, A]

### Definition (plan)
1. Two Definer attempts ended in error after 5 h 29 min and 3 h 51 min of log time (:171-174).
2. The retry returned (:178).
3. Plan review then failed 3 of 3 rounds (:180, :184, :188).
4. Triage followed (:190), and the owner ruled "re-scope", which closed the item (:192). [Fact, A]

The control records' 30-minute session limit (reviews/Q-001/_control/0-62b8dda7dcf2.json:51) cannot be checked for P-001, because P-001 has no control records. [Fact, A]

### Triage
- There were 10 Triage dispatches. Each returned verdict "none" (for example :58, :190), and nothing in the scripted path checks Triage. [Fact, A]
- So no first-pass rate exists for Triage. [Fact, B]

### Questions to the owner
- There were 15 cards and 15 decision lines. 5 decisions were made by proxy (:75, :102, :108, :113, :159). [Fact, A]
- The words used: drop 4, re-specify 3, resubmit 3, confirm 2, build 1, retry 1, re-scope 1. [Fact, B]
- Of the two "confirm" rulings (one focused confirmation review), one led to a PASS (Q-005, :79). The other led to another FAIL and a second card (Q-006, :104-108). [Fact, A]
- How good the cards were cannot be judged: they are in queue/ and decisions/, which I was told not to read. [Fact]

### Inputs that can be traced from control records
1. **The revising researcher was not handed its own memo.**
   - At 2026-10-01T09:15:57Z three researcher revisions (Q-001, Q-002, Q-004) were dispatched with a brief to "Revise your memo".
   - Their packs held the question and the source check but no memo:
     - reviews/Q-001/_control/0-bcdb1d743941.json:3, :51-59;
     - reviews/Q-002/_control/1-d048b87ce06f.json:53-54;
     - reviews/Q-004/_control/2-7da710f0b27a.json:52-53.
   - All three following checks failed (:34-36).
   - From the next revision on, the pack included the memo (reviews/Q-001/_control/0-5adedb5ae23d.json:68), and two of the three items then passed (:50, :52).

   [Fact, A. That the missing memo caused the failures: Estimate, C. The check findings are not in scope.]
2. **The same memo got two different verdicts.**
   - Q-005's memo had hash 766515… at its third check (reviews/Q-005/_control/1-fe151d6987ac.json:83) and at the confirmation check (1-218e36411c3b.json:85).
   - The first gave FAIL (:67) and the second PASS (:79), with no researcher session between them.
   - The confirmation check's pack also held the question (1-218e36411c3b.json:87), and the earlier one's did not. [Fact, A]
   - The cause is **untraceable** from what I may read: it could be checker variance, the pack difference, or an owner ruling. [Opinion, C]
   - By contrast, Q-006's memo 23b09b… failed both times (reviews/Q-006/_control/0-bcb320bfac82.json:101, 0-4794c1dacad6.json:101; dispatch-log:98, :104). [Fact, A]
3. **Pack contents changed during the week.**
   - The template's source-checker pack does not include the question (POOM template-v3/governance/PACKS.toml:60-61).
   - Q-001's source checks lacked it (reviews/Q-001/_control/0-62b8dda7dcf2.json:53-58).
   - Q-006's checks had it (reviews/Q-006/_control/0-bcb320bfac82.json:103).

   [Fact, A] The scripted path is therefore not one fixed procedure across the week. [Opinion, C]
4. **Triage briefs say there is no earlier feedback.**
   - Every critic-triage brief says "Feedback from earlier rounds in this folder: none" (for example reviews/Q-006/_control/0-6c728513a012.json:3).
   - Yet its pack holds the source check and the earlier control records (:101-113). [Fact, A]

---

## 4. Conversational path (a Claude Code session dispatching helper agents; reviews/<series>/_*-verbatim.md and reviews/<PR>/), about 2026-10-17 to 10-30

### Volume
- **330 round files carry a column-0 `Verdict:` line.** 147 begin with FAIL and 183 with PASS (counting "PASS with notes").
- Q-001's map counted 149 files containing a FAIL line. That figure includes two M3D files whose first verdict line is PASS (M3D/_stage-4-review-r3-verbatim.md:10 and :45; _stage-3-4-5-design-r1-verbatim.md:22 and :62).

[Fact, B: search for `^Verdict:` over reviews/**/_*.md]

### Definition (plan review by the Reviewer, the Critic and the Design reviewer)
- **17 plan items.** All checkers passed at round 1 only for HD1 (HD1/_plan-review-r1-verbatim.md:7, _plan-design-r1-verbatim.md:7).
- Counting each checker separately: 2 of 29 passed first time. [Estimate, B: series classified by file name]
- **Rounds to a recorded pass** for the 16 items that have one: 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 6, 8, 14. The median is 3 and the mean 4.1. [Estimate, B]
  - M3B: 14 plan-review and 14 plan-design rounds over drafts 1–13 (M3B/_plan-review-r1…r14-verbatim.md:3).
  - M3G: Critic round 8.
  - S-001-model-3.5.0-records: plan review round 6.
- **One item has no recorded pass.** S-001-notifications ends on plan-review round 4 FAIL and Critic round 6 FAIL, yet its build reviews exist. [Fact, B]

### Build (stage review by the Reviewer, Design reviewer or Security reviewer)
- **About 15 of 50 stage units passed every checker at round 1.** [Estimate, B]
  - Excluded: M3D stages 3 and 6b, whose combined files cannot be split by stage.
  - M3E: 8 of 15.
  - S-001-desk-v2: 0 of 10.
- **Rounds per stage** ranged from 1 to 5; M3B VT3 reached 5 (M3B/_stage-vt3-review-r5-verbatim.md:3). [Fact, A]

### Other work reviewed (Orchestrator and Chief of Staff pull requests, checker setup)
- S-001-model-3.5.0-sync: 7 rounds, 6 FAILs.
- design-reviewer-setup, which wrote a checker's own rulebook: 6 rounds, 5 FAILs.
- cs24: 3 rounds.
- notify-sandbox, push-key, cs15 and j18-leak-scan: each passed first time.

[Fact, B]

### Triage
One conversational Triage exists (M3C/_triage-r3-critic-verbatim.md). It is not checked. [Fact, A]

### Rounds past the stop rule
- The rule is three plan rounds and three build rounds (POOM OPERATING_MODEL.md:203-206).
- Conversational series past it: M3B 14, M3G 8, the sync series 7, records 6, design-reviewer-setup 6, VT3 5, and M3D 6a 4. [Fact, B]
- In one case the spec's own draft notes cite an owner ruling for the 4th round (specs/S-001.md:600-602). [Fact, A]
- For the others, whether a ruling allowed the extra rounds is in decisions/, which is outside my access. **Untraceable.**

---

## 5. Kinds of finding that sent work back, and their causes (sample of 13 FAIL rounds, 24 blocking findings)

| Kind of finding | n | Examples (path:line) | Cause as recorded |
|---|---|---|---|
| Plan contradicts itself or leaves something undefined | 6 | M3B r1 B1, B2, B4, B5 (M3B/_plan-review-r1-verbatim.md:20-49); records r1 #1 (_plan-review-round1-verbatim.md:27-38); M3C r1 B1 (:23-28) | Doer, by default. The contradictions sit far apart in a 22,883-line spec, for example :11002 against :12773 and :13574 against :13606 (M3B r1:27-29, :21-23). That makes **division** plausible. [Opinion, C] |
| Criterion not locked by any test | 4 | records r4 #1 (:43-48); HD1 r1 B1 (:19-24); HD1 r2 B2 (reviews/253/reviewer.md:130-145); VT3 r2 F1 (:19-24) | Two are **inputs** (a spec draft merged into the branch mid-build): HD1 r2 says "It isn't the Builder's slip: draft 3 … landed … four minutes before the Builder's B1 commit" (reviews/253/reviewer.md:112), and VT3 r2 says "draft 13's VT3 row now lists…" (:9). One followed an owner answer (records r4: draft 4 wrote in owner answers, specs/S-001.md:592-599). One is the doer's. |
| Unmet frozen criterion | 3 | desk-v2 1a r1 #1-#3 (S-001-desk-v2/_build-1a-review-round1-verbatim.md:21-40) | Doer (Builder) |
| Inputs incomplete or missing | 2 | design-reviewer-setup r1 #1, #4 (:13-25, :40-45) | Inputs |
| Owner question unfair, or an open owner question settled by the work | 2 | M3C r1 B3 (:38-44); design-reviewer-setup r1 #2 (:27-31) | M3C's Triage calls it "a brief or orchestration gap that rests on wrong facts" but adds "I could not see the brief" (M3C/_triage-r3-critic-verbatim.md:9, :21). **Untraceable** between told and inputs. |
| Wrong fact | 2 | M3B r1 B3 (:33-37); M3C r1 B2 (:30-36) | Doer, or an upstream fact. Untraceable. |
| Record or pull-request description inaccurate | 2 | sync r1 #1 (:5); sync r6 #1 (:5-13) | **Division**: all 6 blocking findings concerned the description's account of its own reviews, "never on the sync itself" (sync r6:15-21) |
| Gap left by owner answers written in | 1 | M3B r7 B1 (:41-45), after the r6 PASS on draft 6 | **Inputs (moving target)** |
| Untestable checklist item | 1 | design-reviewer-setup r1 #3 (:33-38) | Doer |
| Fix brought back a fault | 1 | VT3 r4 F2 (:29-37) | Doer (the fix) |

[Counts: Estimate, B. Classes: Opinion, C.]

### Cross-cutting evidence

**What the agent was told.** No blocking finding in the sample was blamed on the dispatcher's brief. Brief errors appear as non-blocking notes:
- "Your brief said 23 forced", where the reviewer counted 20 (HD1/_stage-hd1-review-r1-verbatim.md:63);
- a commit hash in the brief that does not exist (HD1/_stage-hd1-review-r2-verbatim.md:52; M3G/_stage-qw3-review-r1-verbatim.md:11);
- "seven" where there were eight (M3B/_stage-vt1-review-r1-verbatim.md:60);
- "digest regenerated" when it was not (S-001-model-3.5.0-sync/_review-round2-verbatim.md:35).

One checker blamed its own round-1 miss on accepting "the brief's framing" (M3B/_plan-critic-r2-verbatim.md:43). [Fact, A]

The briefs the Definer writes into the spec for the Builder were caught at plan stage, before any build. The worst case:
- the brief told the Builder to use the private project's files "as real records" (S-001-m3a/_critic-round2-verbatim.md:34-36);
- that was fixed in round 3 (_critic-round3-verbatim.md:9). [Fact, A]

**Inputs changing under a loop:** spec drafts merged into build branches (HD1, VT3), and owner answers written into plans (M3B r7, records r4).
- The M3C Triage counts 5 of 5 blockers in rounds 2–3 as tracing to the owner's switch to gate first (M3C/_triage-r3-critic-verbatim.md:18).
- In every PASS-then-FAIL reversal I opened, the FAIL followed a new draft (M3B r6→r7; records r3→r4). None was a re-check of the same draft.

[Fact, A, for the cases opened. That this holds generally: Estimate, C.]

**The checker:**
- Checkers admit misses that cost a round: S-001-desk-v2/_build-6b-review-round2-verbatim.md:11; _build-2-review-round2-verbatim.md:63; S-001-m3a/_plan-review-round3-verbatim.md:16; S-001-model-3.5.0-sync/_review-round6-verbatim.md:7.
- A checker's own suggested fix caused the next blocker (M3C/_triage-r3-critic-verbatim.md:23).
- The Q-005 verdict flip is described in §3. [Fact, A]

**Division:** the same process finding recurs as a non-blocking note. surface_guard fails over a whole branch once definer or chief-of-staff commits are merged in:
- M3B/_stage-vt3-review-r2-verbatim.md:27;
- reviews/253/reviewer.md:151;
- M3G/_stage-qw3-review-r1-verbatim.md:45;
- M3E/_stage-g9b-review-r1-verbatim.md:52. [Fact, A]

**Model:** never assignable (§6).

---

## 6. Script compared with conversation

| | Scripted | Conversational |
|---|---|---|
| Brief text recorded | Yes, verbatim in each control record (for example reviews/Q-001/_control/0-62b8dda7dcf2.json:3) | No. Headers give only date, branch and commit (239 files begin "Dispatched by the orchestrator on …"); about 90 S-001-* round files have no header at all |
| Model recorded | Yes. Researcher claude-opus-5-5, source-checker and Triage claude-sonnet-5-5 (0-22dc0e573e9a.json:54; 0-62b8dda7dcf2.json:60; 0-6c728513a012.json:116) | Named in 1 of 330 round files ("Session: Opus 5.5", S-001-desk-v2/_build-1b-review-round1-verbatim.md:13) |
| Inputs recorded | The pack's files, with hashes (manifest) | No |
| Usage | Not in what I read | One session file. Tokens null on 10 of 15 helper lines; end usage all null (session_…jsonl:2-10, :13, :17) |
| Kinds of task | Research, readiness check, one plan loop, Triage, cards | Plan, build and pull-request review, one Triage |
| Dates | 10-01 to 10-08 | About 10-17 to 10-30 |

All rows are [Fact, A/B].

**Consequences:**
1. Any difference between the paths is confounded by kind of task, date, and how records were kept. [Opinion, C]
2. The scripted path used one fixed model pairing throughout, so even there the model's effect cannot be separated out. [Fact, A; Opinion, C]
3. Both paths call their dispatcher "the orchestrator" (dispatch-log entries; "Dispatched by the orchestrator" headers). A record does not say which path it came from. [Fact, A]

---

## 7. Completeness and consistency of the records: what is missing

1. **Records of closed or dropped items are absent** (file-existence check; contents not opened) [Fact, A/B]:
   - research/Q-009-, Q-010- and Q-012-memo.md and their -source-check.md, logged at :142-155 and :197-252;
   - triage/Q-009.md, Q-010.md, Q-012.md and P-001.md (:157, :164, :190, :221, :254);
   - reviews/P-001/_critic-dor.md (:84, :116, :162, :168);
   - reviews/S-001/plan.md (:180, :184, :188);
   - docs/reports/P-001-definer.md (:178).

   The control records follow the same pattern. 67 of 104 logged dispatches have one; the 37 that do not all belong to Q-003, Q-009, Q-010, Q-012 and P-001, which were closed by drop, re-scope or error. [Fact, B] This biases any baseline toward work that succeeded. [Opinion, C]
2. **The dispatch log stops at 2026-10-08T21:52:08Z (:263).** Yet Q-014 and Q-015 have memos and source checks in research/, and none has a dispatch line. [Fact, A/B]
3. **Two sessions ran without a dispatch line.** Each has a control record, and the log flags an "anomaly" each time:
   - Q-006, session at 01:25:01, logged at :120-121;
   - Q-013, session at 21:36:11, logged at :259-260.

   [Fact, A]
4. **Round counts are recorded twice.**
   - Pull-request verdict files from about #220 on repeat the rounds of the series verbatim (reviews/253/reviewer.md:3-6 against HD1/_stage-hd1-review-r1-verbatim.md:7-9).
   - Earlier pull-request files keep only a one-line summary of failed rounds, with the details on GitHub (reviews/10/reviewer.md:3).
   - The tally must use one source or the other. [Fact, A]
5. **Round files are missing or inconsistent.** [Fact, A/B]
   - Missing rounds:
     - M3D 6a-review rounds 2–3;
     - the build for S-001-trial-view-1 has only round 1 (FAIL);
     - the build for S-001-design-lab-answers has rounds 1–2 (both FAIL) and no pass;
     - S-001-notifications has no final plan pass.
   - Naming varies: r1 / round1 / round3-recheck / confirmation / focused.
   - Multi-stage files hold several verdicts: M3D/_stage-3-4-5-design-r1-verbatim.md.
   - A stray nested path exists: reviews/reviews/40/owner.md.
6. **"Round" does not always mean rework.** M3E runs a round 2 after both round-1 verdicts were PASS (for example g1: _stage-g1-review-r1 and -r2 both PASS). M3B r12 re-reviews draft 11 at a new commit (M3B/_plan-review-r12-verbatim.md:3). [Fact, A] So rounds overstate rework unless they are tied to drafts. [Opinion, C]
7. **The one session file covers one series only.**
   - Its 12 checker helper lines match the 12 round files of S-001-model-3.5.0-records in number. [Estimate, B]
   - One Definer helper overlaps three later rounds (22:42 to 00:55, session_…jsonl:5-9), so helper lines cannot be matched to rounds one-to-one. [Fact, A]
   - Two later "start" lines have no helpers and no end line (:18-19). [Fact, A]
   - The other conversational round files have no session record at all. [Fact, B]

**Overall judgement.** Kind of task, round sequence and verdict can be recovered for most conversational series and for every scripted item. Brief, model and inputs can be recovered only for the scripted items that survived. Content of findings can be recovered only for the conversational path, plus whatever is in the scripted source checks and Triage files, which I did not open. [Opinion, C]

---

## 8. Answer to the decision this question serves

- **Rework rates by kind of task (definition, build, research):** the records are good enough for a starting point, provided they are cleaned:
  - deduplicate the pull-request files;
  - tie rounds to drafts;
  - mark the gaps;
  - report survivorship.

  [Opinion, C]
- **Anything that attributes rework to instructions, as against inputs, model or division:** the records are not enough, and a baseline has to be collected fresh. [Opinion, C]
- The scripted control records (brief text, pack hashes, model, source commit) look sufficient to replay those sessions under a changed instruction. That would give paired comparisons for research and source checking. [Opinion, C; the content of the records is Fact, A]
- **Where to start, by kind of task:** definition (plan) shows the most rework, then research. Both are heavily affected by inputs changing mid-loop and by the size of the spec. [Estimate, B/C]

## 9. What cannot be traced
- Any finding's link to the model: no variation was recorded in one path, and nothing was recorded in the other.
- The conversational briefs: not recorded anywhere I may read.
- What the scripted path's checks and Triage said: they sit in research/*-source-check.md and triage/*.md, outside this question's named records; and for closed items, those files are gone.
- Why Q-005's identical memo flipped to PASS.
- Whether rounds past three each had an owner ruling: that is in decisions/, which I must not see.
- Where records of closed items went.
- Cost per session: null in nearly every case.

## 10. Questions added (none closed)
1. May the scripted path's source checks and Triage files (research/*-source-check.md, triage/*.md) be opened, so the content of its findings can be classified? If so, how is blindness kept for the Model-Lab Q-006 line of work? *Decision: whether the scripted part of the baseline can include finding content.*
2. Can the records of closed items (Q-003, Q-009, Q-010, Q-012, P-001) be recovered from git history, and is removing them on close intended? *Decision: whether survivorship bias can be removed from a historical baseline.*
3. Is there dispatch history after 2026-10-08, in another month file or another path, and how were Q-014 and Q-015 dispatched? *Decision: the extent of the scripted record.*
4. Can the conversational briefs and models be recovered from the Claude Code session transcripts? *Decision: whether conversational history can support attribution.*
5. How should a "round" be counted for the stop rule and as a measure: per draft, per checker, or per dispatch? *Decision: definition of the main measure.*

---

## 11. Proposed library entries

Every entry is checked on 2026-11-01. The topic "records, baseline" means the entry is about records and the baseline built from them.

### Facts

**F-q006-01. The dispatch log covers 2026-10-01 to 2026-10-08 only.**
- The one month file, dispatch-log/2026-10.jsonl, holds 263 entries; the last is at :263, 2026-10-08T21:52:08Z.
- It has 104 dispatch lines.
- Source: dispatch-log/2026-10.jsonl. Grade A.
- Shelf life: until the log changes; re-check before each use.
- Topics: records, baseline.

**F-q006-02. Scripted research items: 2 of 12 passed the first source check.**
- 41 checks in all: 32 FAIL, 9 PASS. 3 items were dropped after Triage, and 10 Triage dispatches in all were never checked.
- Source: dispatch-log/2026-10.jsonl, outcome and dispatch lines.
- Grade A (my count).
- Shelf life: fixed history; re-check if records are restored.
- Topics: rework, reviews, baseline.

**F-q006-03. Records and control records of closed or dropped items are absent.**
- 37 of 104 dispatches have no control record, and all belong to items closed by drop, re-scope or error.
- Source: reviews/*/_control/ against dispatch-log/2026-10.jsonl.
- Grade A/B.
- Shelf life: 3 months.
- Topics: records, baseline.

**F-q006-04. The conversational path records neither brief nor model.**
- A model is named in 1 of 330 round files (S-001-desk-v2/_build-1b-review-round1-verbatim.md:13).
- The scripted control records hold the brief verbatim, the model, and the pack's file hashes (reviews/Q-001/_control/0-62b8dda7dcf2.json:3, :53-60).
- Grade A.
- Shelf life: 3 months.
- Topics: records, agents.

**F-q006-05. A hash-identical memo failed one source check and passed the next, with no revision between.**
- Item Q-005: reviews/Q-005/_control/1-fe151d6987ac.json:83 and 1-218e36411c3b.json:85; dispatch-log:67, :79.
- Grade A. Cause unknown.
- Shelf life: fixed history.
- Topics: reviews, agents.

**F-q006-06. Three researcher revisions were dispatched without the memo they were told to revise, and all three re-checks failed.**
- reviews/Q-001/_control/0-bcdb1d743941.json:51-59; reviews/Q-002/_control/1-d048b87ce06f.json:53-54; reviews/Q-004/_control/2-7da710f0b27a.json:52-53; dispatch-log:34-36.
- Grade A. The causal link is an estimate.
- Shelf life: fixed history.
- Topics: agents, rework.

**F-q006-07. Conversational plan items: 1 of 17 passed every checker at round 1.**
- Median 3 rounds to a pass; 7 of 17 went past three; M3B ran 14.
- Build stages: about 15 of 50 passed first time.
- Source: `^Verdict:` lines in reviews/**/_*.md.
- Grade B (classified by file name).
- Shelf life: 3 months.
- Topics: rework, reviews, baseline.

**F-q006-08. Pull-request verdict files from about #220 on duplicate the series' round files verbatim.**
- reviews/253/reviewer.md:3-6 against HD1/_stage-hd1-review-r1-verbatim.md:7-9.
- Grade A.
- Shelf life: 3 months.
- Topics: records.

### Patterns

**P-q006-01. Records of failed work vanish, and the baseline flatters.**
- Problem: baselines built from surviving run records.
- Principle: keep the records of dropped or closed items, or report survivorship next to every rate.
- Origin: Service-Desk, F-q006-03.
- Conditions: work items are pruned on close.
- Grade B.
- Shelf life: 12 months.
- Topics: records, baseline.

**P-q006-02. A new draft reopens review.**
- Problem: reading rounds as checker inconsistency.
- Principle: the PASS-then-FAIL reversals I opened followed redrafts that wrote in owner answers or merged spec drafts. Count rounds per triggering draft, and separate "the target moved" from "the doer failed".
- Sources: M3B/_plan-review-r7-verbatim.md:9; specs/S-001.md:592-602; reviews/253/reviewer.md:112; M3C/_triage-r3-critic-verbatim.md:18.
- Grade B.
- Shelf life: 12 months.
- Topics: rework, reviews.

**P-q006-03. A self-referential description keeps failing review.**
- Problem: a pull-request description that narrates its own review history.
- What happened: 6 consecutive FAILs, every blocking finding about the description and none about the change (S-001-model-3.5.0-sync/_review-round6-verbatim.md:15-21).
- Principle: describe the change, not the review history.
- Conditions: a reviewer must certify that the description is true.
- Grade B.
- Shelf life: 12 months.
- Topics: rework, records.

**P-q006-04. Re-checking identical work tests the checker.**
- Problem: telling checker noise from doer quality.
- Principle: re-check hash-identical work, keeping the pack fixed or varying it on purpose.
- Origin: Q-005 (F-q006-05).
- Conditions: the work product's hash is recorded with the verdict.
- Grade C (one instance).
- Shelf life: 12 months.
- Topics: reviews, baseline, agents.

**Hand-off:** this memo goes to the Source checker. Every citation is to a local record and can be checked by opening the path and line.
