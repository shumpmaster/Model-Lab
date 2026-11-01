# Research memo: Q-008, the count of past rework by kind of work (2026-11-01)

**Depth:** 3 (graded memo). **Topics:** records, baseline, reviews, rework, agents.
**Grades:** **A** means a primary record I opened, cited by path and line. **B** means a count or derivation I made, with the method stated. **C** means my own judgement. Each statement is tagged Fact, Estimate or Opinion, written in short form as [F-A], [E-B], [O-C] and so on.

**Where things are.** Paths are relative to /home/user/Service-Desk (SD) unless prefixed **ML** (/home/user/Model-Lab) or **POOM** (/home/user/Personal-Org-Operating-Model).

**Sources.** No web was used, and memory is not a source. Text in the records was treated as data.

**Blindness disclosure.** I did not open the barred paths. Three kinds of permitted record quote project content:
- ML reviews/P-001-* (read only for verdicts and findings);
- ML reviews/Q-008/critic.md, which quotes an earlier draft of this question;
- the M3C triage.

I read them only for verdicts and findings. They did not change any rule set out in §1. [F-A]

---

## Bottom line

1. Returns found in the records, per kind of work. [F-B, §2]

| Kind of work | Returns |
|---|---|
| Plans | 150 |
| Built work | 78 (plus 1 outside the sampling frame) |
| Research | 42 |
| Other reviewed work (orchestrator, Chief of Staff and setup PRs, model and rule PRs) | 27 |
| Owner, research or Discovery documents checked by the Critic | 14 |
| Gate case (scripted definition of ready) | 3 |

Triage was never checked.

2. Pieces that passed at the first try. [E-B, §2]

| Kind and source | Passed first try |
|---|---|
| Plans: SD conversational | 1 of 17 |
| Plans: POOM | 1 of 23 |
| Plans: SD scripted | 0 of 1 |
| Built work: SD | 15 of 50 |
| Built work: POOM | 17 of 28 (12 of 23 without 5 PR files that record no earlier round) |
| Research: SD scripted | 2 of 12 logged items (3 of 14 counting Q-014 and Q-015) |
| Research: ML | 3 of 7 by the original check; 0 of 7 once a later-added check is counted |
| Critic checks | 1 of 20 |
| Gate (SD scripted) | 0 of 1 |

3. Where the cause can be shown. [E-B, §3–§5]
   - I classified 117 of 314 returns. Every return was classified for research, the Critic, the gate, SD's early PR files and POOM's other PRs. For plans, built work and SD's orchestrator series I used samples drawn by a rule fixed beforehand.
   - Most returns record **what** the fault was. Few record **why** the worker made it.
   - Of the 81 classified returns whose findings are recorded, a record names a cause outside the worker's own output in 23. In the other 58 the cause is a residual: "capability of the agent, by elimination". Nothing in those records names the model, and none of them names the brief.
   - 41 classified returns have no record of findings at all: 26 scripted research rounds, 3 scripted plan rounds, 3 gate rounds and 9 summary-only POOM plan rounds.

4. Every cause, on equal terms (primary cause, over classified returns). [E-B; the classes are O-C]

| Primary cause | Returns |
|---|---|
| Capability, residual (2 of them named by the record) | 61 |
| No record of findings | 32 |
| The check itself | 10 |
| Material handed over | 7 |
| Something else (source access) | 3 |
| Instructions | 1 |
| Split of work | 1 |

The 32 with no record of findings are the 26 scripted research rounds, the 3 scripted plan rounds and the 3 gate rounds. The 9 summary-only POOM plan rounds are counted but not classified. Per-kind figures are in §4.

5. Where my figures can be compared with Q-006's, they agree. One cross-check: Q-006's 147 SD conversational files that begin with FAIL equal my 70 plan + 64 build + 13 other returns. I differ on one classification, design-reviewer-setup round 1 finding 4, and on Q-006's statement that the scripted path's finding content was out of reach: 4 triage files hold causes for 7 of its 33 returns. [F-B, §6]

---

## 1. Definitions, sampling and cause rules (fixed before any return was classified)

### 1.1 Terms

- **Piece:** one unit of work submitted to its check or checks. The unit depends on the kind:
  - a research memo;
  - a plan (a spec draft series, or an SD series folder with plan, critic or design checks);
  - a build unit (a stage, or a build series without stages, as in Q-006 §4);
  - a document or card put to the Critic (each research question or card counts separately).
- **Round:** one recorded check dispatch on a piece by one checker. Focused, recheck and confirmation checks count as rounds.
- **Return:** a round whose first column-0 `Verdict:` line is FAIL. That is the README rule (ML reviews/README.md:10-18). For files with no column-0 line, I used the round's own VERDICT line: the POOM reviews/7 files and the ML combined critic files.
- **PASS** includes "PASS with notes".
- **Passed at the first try:** every checker that checked the piece in round 1 passed it. Edge cases:
  - **A later-added check** is a checker whose first check comes after the piece had passed. Examples are the ML second source check of Q-002–Q-004 and the model-diverse Critic on Q-001. The piece still counts as a first-try pass in the main figure and as not passed in a sensitivity figure. The later check's FAIL counts as a return.
  - **A change of checker** (a new model or session in the same role) is an ordinary round.
  - **A round 2 after a PASS**, with no rework (for example M3E g1), counts as a round but not as a return.
  - **No recorded verdict:** the piece is left out and listed.
- **Rounds per piece:** the number of dispatches by the most-dispatched checker, up to the last recorded verdict. Where it matters I also give the round of the first all-checker PASS.

### 1.2 Sampling rule

- If a kind has 12 or fewer returns, or I had already read every return, I classify all of them.
- Otherwise:
  - list the returns by full path in ASCII order (for POOM plans: by spec number, then round);
  - number them 1..N;
  - take positions 1, 1+k, 1+2k, … with k = ceil(N/8).
- I picked the rule's target size of 12 first and lowered it to 8 after listing the populations but before opening any sampled file. Selection was by position only.
- Before drawing, I had read Q-006's descriptions of some returns: VT3 r2, records r1 and r4, desk-v2 1a r1, design-reviewer-setup r1, sync r1 and r6. [F-A, method]

### 1.3 Avoidability test

- **Avoidable:** the record shows a real blocking fault (with evidence, not later withdrawn), and the material needed to avoid it is shown to have been available to the worker. I count the material as available when the fault is internal to the work or its stated basis: a self-contradiction, an unmet frozen criterion, a misquote or wrong figure from a source the work itself cites, a conflict with a repository file the work cites or edits.
- **Not avoidable:** the record shows the fault came from outside the worker's control. Examples:
  - input changed after the work;
  - conflicting rulings;
  - the checker's own wording or suggestion;
  - the checker unable to open sources or files.
- **Cannot say:** what the worker was handed is not recorded and the fault depends on it, or the record is too thin to judge.
- **Mixed:** an avoidable blocking finding sits beside a not-avoidable one. I count the return as avoidable and flag it as mixed.

### 1.4 Cause rules

- **Contributing causes:** every class the record supports, from the question's list: material handed over (to the worker); written instructions (role file or brief); split of work between agents or steps; capability of the agent or its model; the check itself (including the checker's pack, rule, tools, a miss, or a suggested fix); something else, named.
- **Capability, residual:** used when the work is faulty and no record points anywhere else. It is a residual, not evidence about capability.
- **Primary cause:**
  1. the cause whose correction alone would have prevented the return;
  2. if the record (a checker or a Triage) names a root cause, that one;
  3. if still tied, in this order: material > instructions > split > check > capability > something else. Upstream causes come first because capability is usually only inferred.
- **When a brief fails to pass on material:** I list both causes and make material primary. Handing over the file or rule alone would have prevented the return, whatever the brief's wording.

---

## 2. Item 1: counts per kind

### 2.1 Research to source check

**SD scripted.** Source: dispatch-log/2026-10.jsonl outcome lines with role source-checker. Search: Grep `"outcome"`, content mode. [F-A for lines, F-B for counts]

| Item | Rounds | Result | Log lines |
|---|---|---|---|
| Q-001 | 3 | pass at 3 | :17, :34, :50 |
| Q-002 | 5 | pass | :18, :35, :51, :70, :78 |
| Q-004 | 3 | pass | :21, :36, :52 |
| Q-005 | 4 | pass | :45, :59, :67, :79 |
| Q-006 | 7 | pass | :90 … :133 |
| Q-007 | 2 | pass | :134, :145 |
| Q-008 | 1 | first try | :135 |
| Q-009 | 3 | dropped | :146, :151, :155 |
| Q-010 | 3 | dropped | :201, :209, :217 |
| Q-011 | 6 | pass | :202 … :244 |
| Q-012 | 3 | dropped | :241, :248, :252 |
| Q-013 | 1 | first try | :262 |

- Totals: 41 rounds, 32 returns, 9 PASS. Median 3 rounds. 2 of 12 passed first try.
- **Q-014:** research/Q-014-source-check.md:1 is PASS, but it has no log line, so earlier rounds cannot be known.
- **Q-015:** research/Q-015-source-check.md:1 is FAIL, with no pass recorded. That is 1 return.
- Counting both: 3 of 14 pieces passed first try (Q-014 flagged), and there are 33 returns.
- **Left out:** Q-003, which errored and was never checked (:11, :19).

**ML.** All 7 memos are counted.

| Memo | Rounds | Verdicts | Records |
|---|---|---|---|
| Q-001 map | 2 | FAIL, PASS | research/Q-001-source-check.md:1; -2.md:1 |
| Q-002, Q-003, Q-004 | 3 each | first check PASS; later-added second check FAIL; corrections confirmation PASS | Q-002/003/004-source-check.md:1; Q-002-to-Q-004-source-check-2.md:1, :5-11; Q-002-to-Q-007-corrections-confirmation.md:1, :12-78 |
| Q-005 | 3 | FAIL, FAIL, then confirmation PASS | |
| Q-006 | 2 | FAIL, PASS | research/Q-006-source-check.md:1, :86 |
| Q-007 | 3 | FAIL, FAIL, then confirmation PASS | |

- First try: 3 of 7. Counting the later-added check: 0 of 7. Returns: 9 (the Q-002–Q-004 second check is one file covering three memos).
- Nothing was left out. [F-A/B]

### 2.2 Plans to plan review

**SD scripted, P-001.** 1 piece. Plan review failed at :180, :184 and :188. Triage followed at :190, and the item was closed by re-scope. So 0 first try and 3 returns. [F-A]

**SD conversational.** 17 items, re-derived from first verdict lines.
- Search: Grep `^Verdict:` over reviews, glob `**/_*.md`, content mode.
- Passed first try: HD1 only (1 of 17).
- Rounds to the final pass, for the 16 items that have one: 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 6, 8, 14. Median 3.
- First all-checker PASS came earlier for three items: records at 3, M3G at 5, M3B at 5. Later drafts reopened them.
- S-001-notifications has no final pass.
- Returns: **70** FAIL-first plan files. [E-B]

**POOM.** 23 specs with complete round files:
- S-007, S-009, S-010 and S-011: 2 rounds each.
- S-012: 3 FAIL, then re-scoped, with no pass.
- S-012r: 4 rounds.
- S-013: r1–r3 FAIL and confirmation-1 FAIL. No pass is recorded in reviews/.
- S-014: 4 rounds. S-015: 4. S-016: 6.
- S-022: 5. S-023: 16. S-024: 12. S-025: 3. S-026: 5. All five come from POOM reviews/S-029/_triage-plan-stop-rule-verbatim.md:7-47 [F-A].
- S-027: 1. S-028: 3. S-029: 4. S-030: 3. S-031: 3. S-032: 3. S-033: 4. S-034: 3.

Results:
- Passed first try: S-027 only (1 of 23).
- Median rounds to the final pass: 3, over 21 specs. The rounds to the first PASS also have a median of 3.
- Returns in round files: **67**.
- Summary-only specs: S-002 had rounds 1–3 FAIL (POOM reviews/1/reviewer.md:7). S-017 had rounds 1–4 FAIL, S-018 rounds 1–2 FAIL and S-019 round 1 FAIL (POOM reviews/20/reviewer.md:4-6). That adds 4 pieces (0 first try) and **10** returns, not classified.
- **Left out:**
  - S-004, whose rounds 1–3 are not in reviews/ (its confirmation FAIL is classified under "Other");
  - specs with no plan-review file in reviews/. I did not search specs/ or the ledger.

[E-B]

### 2.3 Built work to build review

**SD conversational.** 50 units, as in Q-006 §4. M3D 3 and 6b are left out because they have one checker file or a combined multi-stage file.
- Passed first try: 15 of 50. M3E: 8 of 15. desk-v2: 0 of 10.
- Dispatch rounds per unit: 1 round for 8 units, 2 for 23, 3 for 15, 4 for 3 and 5 for 1 (VT3). Median 2. Some of these rounds came after a PASS.
- No pass: trial-view-1 build and design-lab-answers build.
- Returns: **64** FAIL-first files. [E-B]

**POOM.** 28 pieces:
- reviews/7 builds of S-007, S-009, S-010, S-012, S-013, S-014, S-015 and S-016;
- 5 S-015 proof reviews;
- S-017, S-018 and S-019 (reviews/20);
- S-020 (reviews/21), S-023/24 (reviews/26), S-025/27 (reviews/27) and S-005/006 (reviews/5);
- S-032, S-033 and S-034;
- PRs 25, 28, 29, 30 and 31, each a single PASS.

Results:
- Passed first try: 17 of 28, or 12 of 23 without the 5 single-PASS PRs.
- Rounds: S-009, S-014, S-017, S-020, S-023/24, S-025/27, S-005/6, S-033 and the proof brief took 2 each. S-032 took 3, and the proof diagnostics 4.
- Returns: **14**. [E-B]

**Outside the frame.** SD reviews/263/design-reviewer.md:3-6 has 1 return: adding Model-Lab to the desk, round 1 FAIL, round 2 PASS. It is the one built piece whose worker brief is recorded (ML docs/briefs/04-builder.md). [F-A]

### 2.4 Documents to the Critic (owner questions, research questions, Discovery documents)

20 pieces. [E-B]
- **ML Q-001 question:** round 1 FAIL, round 2 PASS, then a model-diverse round FAIL with no further pass (reviews/Q-001/critic.md:6, :58; reviews/Q-001-diverse/critic.md:1-6). 3 rounds.
- **Q-002–Q-007, six questions:** Q-004 passed unchanged and the other five took 2 rounds (reviews/Q-002-to-Q-007/critic.md:8, :87).
- **Seven shortlist cards:** round 1 FAIL for all, round 2 FAIL on two cards, round 3 PASS (reviews/P-001-shortlist/critic.md:6, :75-83, :124).
- **Milestones:** 2 rounds. **Value-target:** 4. **Problem and pre-mortem:** 3. **Brief:** 2. **Q-008:** 2. Their verdict lines are listed in §7.
- **SD P-001-add-project-tests:** 2 rounds (SD reviews/P-001-add-project-tests/critic.md:6).

Passed first try: 1 of 20 (Q-004). Returns: **14**, counting one per round file section.

### 2.5 Gate case

SD scripted P-001 definition of ready: FAIL at :84, :116 and :162, Triage at :164, PASS at :168. That is 0 of 1 first try and **3** returns. [F-A]

### 2.6 Other reviewed work

- **SD orchestrator, Chief of Staff and setup series:** sync (7 rounds), design-reviewer-setup (6), cs24 (3), and notify-sandbox, push-key, cs15 and j18-leak-scan (1 each). That is 4 of 7 first try and **13** returns. [E-B]
- **SD early PR files with round lines.**
  - Search: Grep `Round \d at [0-9a-f]{7}: (PASS|FAIL)|^Reviewed: PR #\d+ at [0-9a-f]{7}\. (PASS|Round)`, glob `[0-9]*/reviewer.md`, count mode.
  - 12 PRs: 6, 10, 11, 14, 18, 27, 37, 40, 41, 44, 49 and 52. 4 passed first try (6, 18, 40, 41). **9** returns; PR 52 took 3 rounds.
  - Left out: the other PR files. From about #74 they duplicate series folders, and before that they do not record rounds in a common form. [E-B]
- **POOM other** (returns only, no denominator): **5** returns.
  - PR4 r1 (POOM reviews/4/reviewer.md:3);
  - PR18 r1 (POOM reviews/18/reviewer.md:3);
  - PR24 r1 (POOM reviews/24/reviewer.md:77-86);
  - the v3.0.0 adoption review 1 (POOM reviews/8/_adoption-review-1.md:5-8);
  - the S-004 confirmation (POOM reviews/S-004/_confirmation-review-verbatim.md:3-8).

  [F-A]

### 2.7 Triage

Triage was never checked. That covers 10 scripted dispatches (outcome lines :58, :71, :100, :106, :157, :164, :190, :221, :222, :254), the M3C conversational Triage and the POOM S-029 triage (verdict "GAP"). [F-A]

---

## 3. Item 2: returns classified, and samples drawn

| Kind and source | Total returns | Classified | Rule |
|---|---|---|---|
| Research, SD scripted | 33 | 33 | all |
| Research, ML | 9 | 9 | all |
| Plans, SD scripted | 3 | 3 | all (no record) |
| Plans, SD conversational | 70 | 8 | k = 9: positions 1, 10, 19, 28, 37, 46, 55, 64 |
| Plans, POOM round files | 67 | 8 | k = 9: same positions |
| Plans, POOM summary-only | 10 | 0 | outside the frame; one-line or no cause |
| Built, SD | 64 | 8 | k = 8: positions 1, 9, 17, 25, 33, 41, 49, 57 |
| Built, POOM | 14 | 7 | k = 2: positions 1, 3, …, 13 |
| Critic | 14 | 14 | all (already read) |
| Gate | 3 | 3 | all (no record) |
| Other, SD series | 13 | 7 | k = 2: positions 1, 3, …, 13 |
| Other, SD early PRs | 9 | 9 | all |
| Other, POOM | 5 | 5 | all |

[F-B]

The sampled files, in position order:
- **SD plans:** M3B _plan-critic-r1; M3B _plan-design-r9; M3C _plan-review-r3; after-glance _plan-critic-r2; desk-v2 _critic-round1; job-prs-recorded _plan-review-round2; records _plan-review-round2; notifications _plan-review-round4.
- **POOM plans:** S-007 r1; S-012r r3; S-015 r2; S-022 r4; S-023 r11; S-024 r6; S-029 r1; S-033 r2.
- **SD build:** HD1 design-r1; M3B vt3-review-r2; M3E g5-review-r1; M3G qw1-review-r1; desk-v2 1a-review-r1, 3-review-r1 and 6b-review-r2; m3a build-r1.
- **POOM build:** PR5 r1; S-014 build r1; S-015 proof-diag r1 and r3; S-020 r1; S-025/27 r1; S-032 build r2.
- **SD other:** sync r1, r3 and r5; cs24 r1; design-reviewer-setup confirmation1, r1 and r3.

---

## 4. Items 3 and 4: avoidability and cause, per return

"Cap." means capability, residual unless marked as named by the record.

**Research, SD scripted (33):**

| Return | Avoidable? | Contributing causes | Primary | Record |
|---|---|---|---|---|
| Q-005 :67 | No | check (its pack lacked research/Q-005.md, which the memo cites); cap. (the citation was left in, a "secondary contributor") | check | triage/Q-005.md:1, :7-16 |
| Q-006 :90, :94, :98 | No | check (standard had no rule on same-publisher sources), reported second-hand by the later triage | check | triage/Q-006.md:9 [B] |
| Q-006 :104 | Mixed | instructions (the question's "public docs only" conflicts with the standard); check (standard); cap. (item 13 had no source) | instructions (named by the triage) | triage/Q-006.md:18-21, :17 |
| Q-011 :218 | Yes | cap. (named: claims not on the cited page); check (coverage incomplete) | cap. (named) | triage/Q-011.md:13, :16 |
| Q-015 | Yes | cap. (left out a contradicting sentence of a source it quoted) | cap. | research/Q-015-source-check.md:3 |
| 26 others | Cannot say | no record of findings | none | |

Notes on the 26 with no record:
- 3 of them (Q-001 :34, Q-002 :35, Q-004 :36) have a recorded material gap: the revising researcher's pack lacked its memo (F-q006-06).
- 2 (Q-005 :45, :59) have the checker-pack gap recorded (triage/Q-005.md:10), but the reason for the FAIL was not confirmed (:28).
- Q-002's three have only a hypothesis (triage/Q-002.md:22-25).

**Research, ML (9):**

| Return | Avoidable? | Causes | Primary |
|---|---|---|---|
| Q-001 first check | Yes | cap. (J1 cites ids that are not in the cited file, Q-001-source-check.md:3) | cap. |
| Q-002, Q-003, Q-004 second check (3) | Cannot say | something else (the researchers' sessions could not open outside sources: reviews/P-001-problem-premortem/critic.md:88); cap. (figures differ from the papers, Q-002-to-Q-004-source-check-2.md:29, :38, :93) | something else (source access) [O-C] |
| Q-005 first check | No | check (the checker could reach no web host, Q-005-source-check.md:3-5) | check |
| Q-005 second check | Mixed | cap. (quotes not verbatim; a sentence not in the NTSB report, -2.md:3); independence standard | cap. |
| Q-006 first check | Mixed | cap. (model count, overstatement); check (desk-v2 count was the checker's error, withdrawn at Q-006-source-check.md:92-95, :156) | check (tie-break) |
| Q-007 first check | No | check (hosts unreachable, Q-007-source-check.md:3) | check |
| Q-007 second check | Mixed | cap. (two figures do not match their sources; absence claims, -2.md:3-7) | cap. |

**Plans (19 classified):**
- **SD scripted (3):** no record. reviews/S-001/plan.md is absent.
- **SD sample (8):**
  - M3C r3 is "cannot say". Its contributing causes are:
    - material: a moved target (the owner switched to gate first), and rule text in decisions/README.md that contradicts itself (:57 against :5-7);
    - instructions: the Definer "apparently got none of the rules", though the brief was not seen;
    - check: round 2's suggested fix led to round 3's B1;
    - capability.

    Primary is material, under the brief-and-material rule (M3C/_triage-r3-critic-verbatim.md:10, :16-23).
  - The other 7 are avoidable, with capability (residual) as primary. All are self-contradictions or conflicts with cited rulings or rules:
    - M3B critic r1 (:19-45);
    - M3B design r9 (:15);
    - after-glance critic r2 (:44-69);
    - desk-v2 critic r1 (:11-37);
    - job-prs r2 (:14-17);
    - records r2 (:38);
    - notifications r4 (:3).
- **POOM sample (8):** all avoidable, with capability (residual) as primary:
  - S-007 r1 (:8-10);
  - S-012r r3 (:10);
  - S-015 r2 (:8-10);
  - S-022 r4 (:8, a fault brought in by a fix);
  - S-023 r11 (:73, :101). Contributing: split, since the coupled S-024 had not yet been revised (:3), and material, from owner answers 13–16 just carried in (:1);
  - S-024 r6 (:152);
  - S-029 r1 (:21-27);
  - S-033 r2 (:7, :27-30).

**Built work (15 classified):**
- **SD (8):**
  - HD1 design r1: not avoidable. Material: two owner rulings conflict (:19-25). Primary material.
  - VT3 r2: not avoidable. Material changed: draft 13 was merged after the Builder's commits (:3, :9, :27). Split contributes. Primary material.
  - 6 avoidable, primary capability:
    - g5 r1 (:21);
    - qw1 r1 (:13-18);
    - 1a r1 (:9, :21);
    - 3 r1 (:21-26);
    - 6b r2 (:11; contributing check, "I missed it in round 1");
    - m3a r1 (:18-25; capability named by the record, "the Builder's admitted slip").
- **POOM (7):**
  - S-014 build r1: mixed. B1 is a Builder defect. B2 is a "spec-versus-check conflict… needs an owner ruling" (:8-9). Primary material by tie-break.
  - 6 avoidable, primary capability:
    - PR5 r1 (reviews/5/reviewer.md:3);
    - proof-diag r1 (:8-9) and r3 (:8);
    - S-020 r1 (reviews/21/reviewer.md:5-6);
    - S-025/27 r1 (reviews/27/reviewer.md:25-29);
    - S-032 build r2 (:3).
- **Outside the frame:** PR 263 design r1 is "cannot say". The tile's wording on a new project's state is existing code, and it was fixed once Model-Lab's own records changed (reviews/263/design-reviewer.md:3, :18-19). Primary material.

**Critic (14):**
- 11 are avoidable, with capability (residual) as primary. They are internal inconsistencies, misattributions, or claims beyond the records the work cites:
  - Q-001 r1, mixed (:50);
  - shortlist r1 (:12-25);
  - milestones r1 (:25-30);
  - value-target r1, r2 and r3 (:12-42, :101-106, :132-138; r2 and r3 were brought in by fixes);
  - problem-premortem r1 and r2 (:18-58, :131-136);
  - brief r1 (:19-28);
  - Q-008 r1 (:10-14);
  - SD add-project-tests r1 (:10-20). Contributing split: it cites a Builder return that was never recorded (:32).
- 3 are "cannot say":
  - Q-001-diverse r1. Contributing: check, because a new checker failed wording the first Critic had proposed (Q-001/critic.md:19-20 against Q-001-diverse/critic.md:23-27); capability. Primary check.
  - Q-002–Q-007 r1. Neutrality fixes against a standard that the record does not show was handed to the writer. Primary capability (residual).
  - Shortlist r2. It cites a source check that was "not in the Model-Lab tree" (:79-83). Primary split (recording lagged).

**Gate (3):** no record. reviews/P-001/_critic-dor.md and triage/P-001.md are absent.

**Other (21 classified):**
- **SD series (7):**
  - sync r1: avoidable, capability (:5).
  - sync r3: not avoidable. The faulty wording was the checker's own suggestion, "the miss is mine" (:3). Primary check.
  - sync r5: cannot say. Check: the checker passed the list in round 4 and says "That miss is mine" (:3). Something else: a standing rule that the opening recounts failures (AGENTS.md:68, as cited at r3:8). Primary check.
  - cs24 r1: avoidable, capability (:11-15).
  - design-reviewer-setup confirmation1: avoidable, capability (:9, :18-24).
  - design-reviewer-setup r1: avoidable (mixed), capability. Contributing material and split: finding 4 relies on documents that are on no route to main (:40-46).
  - design-reviewer-setup r3: mixed. B1 is material: the Linear reference sizes are not in the repository (:18). Primary material.
- **SD early PRs (9):**
  - Avoidable, capability: 11, 14, 27, 37 (mixed), 44, 49 and 52 r1.
  - PR 10: cannot say. The one-line summary gives the fault only (reviews/10/reviewer.md:3).
  - PR 52 r2: not avoidable. Material: the spec text then on main conflicted with a ruling not yet in the repository, and round 3 passed at the same commit (reviews/52/reviewer.md:7-9). Primary material.
- **POOM (5):** all avoidable, with capability (residual) as primary.

### Tallies by kind

[E-B; the classes are O-C]

| Kind | Classified | Avoidable (of which mixed) | Not avoidable | Cannot say or no record |
|---|---|---|---|---|
| Research | 42 | 7 (4) | 6 | 29 |
| Plans | 19 | 15 | 0 | 4 |
| Built (in frame) | 15 | 13 (1) | 2 | 0 |
| Critic | 14 | 11 (1) | 0 | 3 |
| Gate | 3 | 0 | 0 | 3 |
| Other | 21 | 17 (2) | 2 | 2 |

| Kind | Cap. (residual / named) | Check | Material | Instructions | Split | Something else | No record |
|---|---|---|---|---|---|---|---|
| Research | 5 / 1 named | 7 | 0 | 1 | 0 | 3 | 26 |
| Plans | 15 / 0 | 0 | 1 | 0 | 0 | 0 | 3 |
| Built | 12 / 1 | 0 | 3 | 0 | 0 | 0 | 0 |
| Critic | 12 / 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| Gate | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| Other | 17 / 0 | 2 | 2 | 0 | 0 | 0 | 0 |

- **Contributing, not primary:** check 5, material 3, split 3, instructions 1 (M3C, where the brief and material case applies), something else 1, capability 4.
- **The model** is named as a cause by no classified record.
- **The brief** is named as a cause only by the M3C Triage, which says it could not see the brief. [F-A]

---

## 5. Item 5: what the records cannot show

- **Returns with no record of findings:** research 26 of 33 SD scripted; plans 3 scripted plus 9 of the 10 POOM summary-only returns; gate 3 of 3. ML research, the Critic and SD conversational returns all have their check text. [F-B]
- **Returns whose findings are recorded but no record names a cause** (residual capability, among the classified returns): research 4, plans 15 of 16, built 11 of 15, Critic 12 of 14, other 17 of 21. [E-B]
- **Pieces with no check record at all:**
  - research: Q-003, which errored;
  - Triage: 12 pieces, by design;
  - the scripted P-001 Definer report (docs/reports/P-001-definer.md is absent; its verdicts exist only in the log).

  The source-check files for Q-009, Q-010 and Q-012 are absent too; their verdicts are only log lines. [F-A, F-q006-03]
- **Overwritten records:** the SD research/*-source-check.md files hold only the last verdict. The triage itself says the round-1 and round-2 checks "were overwritten" (triage/Q-011.md:26). [F-A]
- **Worker briefs:**
  - they are not recorded for SD and POOM conversational work;
  - in ML docs/briefs, the recorded worker briefs are the researcher's for Q-001 (02) and the builder's (04, used for PR 263); the rest are checker briefs;
  - so for every classified conversational return, "instructions" can be supported only through a Triage. [F-A]
- **The model:**
  - in the scripted path every worker ran one fixed pairing;
  - the SD conversational records name a model in 2 of 330 round files (F-q006-04);
  - so the model cannot be separated out as a cause. [F-A/B]

---

## 6. Where my figures differ from Q-006's, and which record decides

| Figure | Mine | Q-006 | Deciding record |
|---|---|---|---|
| SD conv plans: first try, median | 1 of 17, 3 | same | `^Verdict:` lines (same search) |
| SD build first try | 15 of 50 | same | same |
| SD scripted research | 2 of 12 (3 of 14 with Q-014/Q-015) | 2 of 12 | research/Q-014-, Q-015-source-check.md:1 |
| SD FAIL-first round files | 70 + 64 + 13 = 147 | 147 | consistent |
| Scripted finding content | 7 of 33 returns have a recorded cause | "not in this memo" | triage/Q-002, Q-005, Q-006, Q-011.md and research/Q-015-source-check.md (Q-006 did not open them) |
| design-reviewer-setup r1 #4 | capability primary; material or split contributing | untraceable | _review-round1-verbatim.md:40-46 ("on no route to main") |

All other overlapping classifications agree. VT3 r2 is input or material in both. desk-v2 1a r1 and sync r1 are doer or capability in both. [F-B]

---

## 7. Proposed library entries

### Facts

**F-q008-01.** SD's 147 conversational round files that begin with FAIL split into 70 plan checks, 64 build checks and 13 orchestrator, Chief of Staff and setup checks.
- Source: first column-0 `Verdict:` lines in reviews/**/_*.md.
- Grade B. Shelf life: 3 months. Topics: records, rework, reviews.

**F-q008-02.** SD scripted research had 33 returns: 32 logged and 1 in the Q-015 file. A cause is recorded for 7, all in triage/Q-005, Q-006 and Q-011.md and research/Q-015-source-check.md. Triage files for Q-009, Q-010, Q-012 and P-001 are absent.
- Grade A for the files, B for the counts. Shelf life: fixed history; re-check if records are restored. Topics: records, baseline.

**F-q008-03.** POOM plan reviews:
- 23 specs with complete round files; 1 passed at the first try (S-027);
- median 3 rounds to the final pass; 67 returns;
- S-023 ran 16 rounds and S-024 12 (POOM reviews/S-029/_triage-plan-stop-rule-verbatim.md:7-36).
- Grade B (A for the triage-cited rounds). Shelf life: 3 months. Topics: rework, baseline.

**F-q008-04.** Model-Lab Critic checks: 20 pieces, 1 passed at the first try (Q-004), 14 returns.
- Grade B. Shelf life: 3 months. Topics: reviews, rework.

**F-q008-05.** Model-Lab research:
- 3 of 7 memos passed their first source check, and all 3 then failed a later check once the sources were reachable;
- 2 of 9 returns came from the checker being unable to reach any web host (Q-005-source-check.md:3-5; Q-007-source-check.md:3).
- Grade A for the files, B for the counts. Shelf life: fixed history. Topics: research, reviews.

**F-q008-06.** In the 117 classified returns, no record names the model as a cause. Only one record, the M3C Triage, names the brief, and it could not see the brief (M3C/_triage-r3-critic-verbatim.md:21).
- Grade B. Shelf life: 3 months. Topics: agents, records.

### Patterns

These describe what was seen. They are not recommendations.

**P-q008-01. A checker's suggested fix can cause the next return.**
- Seen in: sync r3 (:3); the M3C triage on round 2's suggested fix leading to round 3's B1 (:23); Q-001 r1's wording, failed by a different Critic (Q-001/critic.md:19-20; Q-001-diverse/critic.md:23-27).
- Principle as observed: when returns are counted by cause, check-originated faults are a separate class.
- Grade B. Shelf life: 12 months. Topics: reviews, rework.

**P-q008-02. Overwritten check files erase the causes of returns.**
- Seen in: SD research check files keep only the last verdict (triage/Q-011.md:26).
- Principle as observed: a cause count from such records measures surviving text, not what happened.
- Grade B. Shelf life: 12 months. Topics: records, baseline.

**P-q008-03. A cause count from review records falls mostly into a residual.**
- Seen in: 58 of 81 classified returns with recorded findings name no cause beyond the fault.
- Principle as observed: capability by elimination is a property of what the records name, not evidence about capability.
- Grade C. Shelf life: 12 months. Topics: records, agents.

---

## 8. Sources opened

All paths are absolute.

- **Model-Lab research:** /home/user/Model-Lab/research/Q-008.md; Q-006-memo.md; Q-006-source-check.md; Q-001-source-check.md and -2.md; Q-002-to-Q-004-source-check-2.md (head and grep); Q-002-to-Q-007-corrections-confirmation.md (head and headings); Q-005-source-check.md and -2.md (heads); Q-007-source-check.md and -2.md (heads).
- **Model-Lab reviews and briefs:** /home/user/Model-Lab/reviews/README.md; reviews/{Q-001, Q-001-diverse, Q-002-to-Q-007, Q-008, P-001-brief, P-001-value-target, P-001-problem-premortem, P-001-shortlist, P-001-milestones}/critic.md (verdicts and findings); docs/briefs/README.md and header lines of 01–10; .claude/agents/researcher.md.
- **Service-Desk log, triage and research:** /home/user/Service-Desk/dispatch-log/2026-10.jsonl (outcome lines); triage/Q-002.md, Q-005.md, Q-006.md, Q-011.md; research/Q-014-source-check.md and Q-015-source-check.md (heads).
- **Service-Desk plan reviews:** reviews/M3B/_plan-critic-r1 and _plan-design-r9; M3C/_plan-review-r3 and _triage-r3-critic; S-001-after-glance/_plan-critic-r2; S-001-desk-v2/_critic-round1; S-001-job-prs-recorded/_plan-review-round2; S-001-model-3.5.0-records/_plan-review-round2; S-001-notifications/_plan-review-round4.
- **Service-Desk build reviews:** HD1/_stage-hd1-design-r1; M3B/_stage-vt3-review-r2; M3E/_stage-g5-review-r1; M3G/_stage-qw1-review-r1; S-001-desk-v2/_build-1a-review-round1, _build-3-review-round1 and _build-6b-review-round2; S-001-m3a/_build-review-round1; 263/design-reviewer.md (rounds and round 1).
- **Service-Desk other reviews:** S-001-model-3.5.0-sync/_review-round1, 3 and 5; cs24/_review-round1; design-reviewer-setup/_review-round1, _review-round3 and _confirmation1; P-001-add-project-tests/critic.md; dor-fail-2-round3/reviewer.md; PR files 10, 11, 14, 27, 37, 44, 49 and 52 (round lines). All are *-verbatim.md files under /home/user/Service-Desk/reviews/ unless named otherwise.
- **POOM reviews:** /home/user/Personal-Org-Operating-Model/reviews/7/_plan-review-s007-round1, s012r-round3, s015-round2, _build-review-s014-round1, _review-s015-proof-diag-round1 and round3; S-022/_plan-review-s022-round4; S-023/_plan-review-s023-round11; S-024/_plan-review-s024-round6; S-029/_plan-review-s029-round1 and _triage-plan-stop-rule-verbatim; S-033/_plan-review-round2; S-032/_build-review-round2; S-004/reviewer.md and _confirmation-review-verbatim.md; 8/_adoption-review-1.md; reviewer.md of PRs 21, 24 and 27; verdict and round lines of PRs 1, 4, 5, 18, 20, 25–38.

**Searches** (all Grep; repeatable):
- `^Verdict:\s*FAIL` on SD reviews (files mode);
- `^Verdict:` on SD reviews, glob `**/_*.md` (content mode);
- `"outcome"` and the role or verdict pattern on the dispatch log (content and count modes);
- `^Verdict:|^#+ .*[Rr]ound` on POOM reviews (content);
- `^(ROUND \d+ )?VERDICT|^Verdict` (case-insensitive) on POOM reviews/7;
- the PR round pattern in §2.6 on SD reviews `[0-9]*/reviewer.md` (count);
- `FAIL` on SD reviews `[0-9]*/*.md` (count);
- Globs over SD research/, triage/ and reviews/ and over POOM reviews/.

**Hand-off:** to the Source checker. I have not marked any of my own facts as checked.
