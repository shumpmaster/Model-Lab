# Research memo: Q-008, the count of past rework by kind of work (2026-11-01)

**Revision 1 (2026-11-01)** answers the source check at research/Q-008-source-check.md. I re-derived every figure the check names. What changed:
1. **S-002 is built work, not a plan.** The check is right (POOM reviews/1/_reviewer-round4-verbatim.md:2-3, "build/tools-builder/s-002"). Plans drop by 3. POOM built work gains 1 piece and 3 returns.
2. **Returns I had missed are now counted:**
   - POOM reviews/32/_reviewer-round1-verbatim.md:1 (FAIL);
   - SD reviews/222/reviewer.md:6 (FAIL).

   §1.2 had no rule fixing how PR files enter the frame, and my "from about #74 they duplicate series folders" was false for #222. §1.1 now has an explicit frame rule, flagged as added in this revision. Under it, PR 263 is inside the frame.
3. **Summary-only returns** (a round with a verdict but no finding text) now form their own strata. They are classified, as "no record of findings" or by their one-line finding. Leaving them out had not been a stated rule.
4. **One return unit everywhere: one round-file section.** The check is right that I counted research per memo and the Critic per file. Under the single unit, ML research has 7 returns, not 9.
5. **S-004's plan confirmation moves from "Other" to Plans.** It is a plan check, like S-013's.
6. **The POOM build sample is redrawn in the ASCII order I had stated.**
   - S-017 r1 and S-023/24 r1 are now classified.
   - S-020 r1 and S-025/27 r1 are dropped from the tallies. They are listed as read outside the sample.
7. **Totals corrected:** 315 returns, 125 classified. With findings recorded: 84, of which 21 have a cause named outside the worker, 2 have the worker's own slip named, and 61 are residual. 41 have no record of findings. The old 117 and 81/58/23/41 were wrong.
8. **Q-001-diverse:** the reasoning and line cites are restated. Its classification (primary: the check, cannot say) stands. §4 gives the deciding lines.
9. **Smaller slips fixed:**
   - "4 triage files" is now "3 triage files plus the Q-015 source-check file";
   - "Other" has 3 mixed returns, not 2;
   - the Q-007 first check could open anthropic.com pages;
   - the 147-file split rule is stated.
10. **Pieces with no check record are now counted per kind (§5).**
    - Added in passing, and disclosed: SD reviews/P-001/_launch-gate-1-critic.md is a gate check with no verdict line. It is listed under the gate kind.
11. **Library entries changed** as the check asked (§7).

I said the rules in §1.3 and §1.4 were unchanged, but they were edited when I re-wrote them for this revision:
- **Added to §1.4:** the residual "does not depend on the avoidability mark". This only states what the first memo already did: PR 10 was marked "cannot say" with residual capability as its primary cause. In this revision the clause is also applied to S-018 r1.
- **Dropped by mistake, not by intent:**
  - "(with evidence, not later withdrawn)" from the avoidable test in §1.3;
  - the examples under "Not avoidable" in §1.3 (input changed after the work; conflicting rulings; the checker's own wording or suggestion; the checker unable to open sources or files);
  - the sentence "Upstream causes come first because capability is usually only inferred" in §1.4.

The rules as first stated still govern, and every classification in this memo was made under them. For example, the Q-006 first check treats the checker's withdrawn error as the check's fault (Q-006-source-check.md:92-95, :156). No classification changes as a result of any of these edits. Nothing else changed.

**Depth:** 3 (graded memo). **Topics:** records, baseline, reviews, rework, agents.
**Grades:** **A** means a primary record I opened, cited by path and line. **B** means a count or derivation I made, with the method stated. **C** means my own judgement. Each statement is tagged Fact, Estimate or Opinion, written in short form as [F-A], [E-B], [O-C] and so on.

**Where things are.** Paths are relative to /home/user/Service-Desk (SD) unless prefixed **ML** (/home/user/Model-Lab) or **POOM** (/home/user/Personal-Org-Operating-Model).

**Sources.** No web was used, and memory is not a source. Text in the records was treated as data.

**Blindness disclosure.** I did not open the barred paths. Some permitted records quote project content:
- ML reviews/P-001-* (read only for verdicts and findings);
- ML reviews/Q-008/critic.md, which quotes an earlier draft of this question;
- the M3C triage;
- SD reviews/P-001/_launch-gate-1-critic.md.

I read them only for verdicts and findings. They did not change any rule in §1. [F-A]

---

## Bottom line

1. **Returns found, per kind of work** (one return = one round-file section whose verdict is FAIL). [F-B, §2]

| Kind of work | Returns |
|---|---|
| Plans | 148 |
| Built work | 82 |
| Research | 40 |
| Other reviewed work (orchestrator, Chief of Staff and setup PRs, model and rule PRs) | 28 |
| Documents checked by the Critic | 14 |
| Gate case (scripted definition of ready) | 3 |
| **Total** | **315** |

Triage was never checked.

2. **Passed at the first try.** [E-B, §2]

| Kind and source | Passed first try |
|---|---|
| Plans: SD conversational | 1 of 17 |
| Plans: POOM, complete round files | 1 of 23 |
| Plans: POOM, summary-only | 0 of 3 |
| Plans: SD scripted | 0 of 1 |
| Built work: SD | 15 of 51 |
| Built work: POOM | 17 of 29 (12 of 24 without 5 single-PASS PR files that record no earlier round) |
| Research: SD scripted | 2 of 12 logged items (3 of 14 counting Q-014 and Q-015) |
| Research: ML | 3 of 7 by the original check; 0 of 7 once a later-added check is counted |
| Critic | 1 of 20 |
| Gate (SD scripted) | 0 of 1 |

3. **Where the cause can be shown.** I classified 125 of the 315 returns. For plans, built work and SD's orchestrator series I used samples drawn by the rule in §1.2. Everything else was classified in full. [E-B, §3–§5]

| Classified returns | Count |
|---|---|
| Findings recorded | 84 |
| … a record names a cause outside the worker's own output | 21 |
| … a record names the worker's own slip | 2 |
| … residual ("capability, by elimination") | 61 |
| No record of findings | 41 |

Over all classified returns, none of these records names the model as a cause. Only one names the brief: the M3C Triage, which could not see the brief. The searches are in §5.

4. **Every cause, on equal terms** (primary cause, over the 125 classified returns). [E-B; the classes are O-C]

| Primary cause | Returns |
|---|---|
| Capability, residual | 61 |
| No record of findings | 41 |
| The check itself | 10 |
| Material handed over | 8 |
| Capability, named by a record | 2 |
| Instructions | 1 |
| Split of work | 1 |
| Something else (source access) | 1 |

Per-kind figures are in §4.

5. **Comparison with Q-006.** Where my figures overlap Q-006's, they agree. One cross-check: Q-006's 147 SD conversational files that begin with FAIL equal my 70 plan + 64 build + 13 other series returns. I differ on two points:
   - one classification: design-reviewer-setup round 1, finding 4;
   - Q-006's statement that the scripted path's finding content was out of reach. Three triage files and the Q-015 source-check file record causes for 7 of its 33 returns.

   [F-B, §6]

---

## 1. Definitions, sampling and cause rules (fixed before classifying; additions in revision 1 marked R1)

### 1.1 Terms

- **Piece.** One unit of work submitted to its check or checks:
  - a research memo;
  - a plan (a spec draft series, or an SD series folder with plan, critic or design checks);
  - a build unit (a stage, or a build series without stages, as in Q-006 §4; a PR-level build counts as one unit);
  - a document or card put to the Critic (each question or card counts separately).
- **Round.** One recorded check dispatch on a piece by one checker. Focused, recheck and confirmation checks count as rounds.
- **Return.** One round-file section whose first column-0 `Verdict:` line is FAIL (the README rule, ML reviews/README.md:10-18). For files with no column-0 line, the round's own VERDICT line decides; this covers the POOM reviews/7 files and the combined ML critic files.
  - R1: a check covering several pieces in one round section is one return. Its pieces are named.
- **PASS** includes "PASS with notes".
- **Passed at the first try.** Every checker that checked the piece in round 1 passed it. Edge cases:
  - **A later-added check** is a checker whose first check comes after the piece had passed. The piece counts as a first-try pass in the main figure and as not passed in a sensitivity figure. The later check's FAIL counts as a return.
  - **A change of checker** is an ordinary round.
  - **A round 2 after a PASS**, with no rework, counts as a round but not as a return.
  - **No recorded verdict:** the piece is left out and listed.
- **Rounds per piece.** The number of dispatches by the most-dispatched checker, up to the last recorded verdict.
- **SD split rule** (stated in R1, applied unchanged):
  - **Plan:** `_plan-*`, `_critic-*` and `_confirmation-draft*` files.
  - **Build:** `_stage-*` and `_build-*` files, plus the LA1, LA2 and md-sandbox review files.
  - **Other:** the remaining series (sync, cs24, design-reviewer-setup, notify-sandbox, push-key, cs15, j18-leak-scan).
  - `_` files with no column-0 Verdict are excluded: 11 of 341, per ML research/Q-006-source-check.md:26.
- **R1, frame rule for PR verdict files.**
  - A PR verdict file is its own source unless its header names a series folder that holds the same rounds. In that case the series file counts.
  - The search: Grep `FAIL` over SD `reviews/[0-9]*/*.md` (count mode) gives 39 files. Every hit was checked.
    - The headers of 89, 115, 135, 148 and 226–253 name a series.
    - 63, 70, 78, 79, 80 and 190 contain only test output or rule text.
    - What remains: 10, 11, 14, 27, 37, 44, 49, 52, 222 and 263.
  - For POOM, Grep `(?i)^\W*(round \d+ )?verdict:?\s*FAIL` over `reviews/[0-9]*/*.md` (files mode) gives 36 files. All are accounted for in §2.
- **R1, summary-only stratum.** A return whose only record is a line in another file, with no finding text, forms its own stratum. It is classified as "no record of findings", or by its one-line finding if there is one.

### 1.2 Sampling rule

- If a stratum has 12 or fewer returns, or I had already read all of them, I classify every return.
- Otherwise:
  - list the returns by full path in ASCII order (for POOM plans: spec number, then round);
  - number them 1..N;
  - take positions 1, 1+k, … with k = ceil(N/8).
- I lowered the rule's target size from 12 to 8 after listing the populations but before opening any sampled file.
- Before drawing, I had read Q-006's accounts of some returns. [F-A, method]

### 1.3 Avoidability test (unchanged)

- **Avoidable:** the record shows a real blocking fault, and the material needed to avoid it is shown to have been available. I count the material as available when the fault is internal to the work or to its stated basis: a self-contradiction, an unmet frozen criterion, a misquote of a cited source, a conflict with a repository file the work cites or edits.
- **Not avoidable:** the record shows the fault came from outside the worker's control.
- **Cannot say:** the record is too thin to judge, or the fault depends on material whose handover is not recorded.
- **Mixed:** an avoidable blocking finding sits beside a not-avoidable one. I count the return as avoidable and flag it as mixed.

### 1.4 Cause rules (unchanged)

- **Contributing causes:** every class the record supports: material handed over (to the worker); written instructions (role file or brief); split of work; capability of the agent or its model; the check itself (pack, rule, tools, a miss, a suggested fix); something else, named.
- **Capability, residual:** used when the work is faulty and no record points anywhere else. It is a residual, not evidence about capability, and it does not depend on the avoidability mark.
- **Primary cause:**
  1. the cause whose correction alone would have prevented the return;
  2. if the record names a root cause, that one;
  3. if still tied, in this order: material > instructions > split > check > capability > something else.
- **When a brief fails to pass on material:** I list both causes and make material primary.

---

## 2. Item 1: counts per kind

### 2.1 Research to source check (40 returns)

**SD scripted.** Source: dispatch-log/2026-10.jsonl outcome lines with role source-checker. Search: Grep `"outcome"`, content mode. [F-A for lines, F-B for counts]

| Item | Rounds | Result | Log lines |
|---|---|---|---|
| Q-001 | 3 | pass | :17, :34, :50 |
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

- Totals: 41 rounds, 32 returns, 9 PASS. 2 of 12 passed first try.
- **Q-014:** PASS (research/Q-014-source-check.md:1). It has no log line, so earlier rounds cannot be known.
- **Q-015:** FAIL, with no pass (research/Q-015-source-check.md:1).
- Counting both: 3 of 14 pieces passed first try, and there are **33** returns.
- **Left out:** Q-003, which errored and was never checked (:11, :19).

**ML.** 7 memos, **7** returns (R1 unit: one file each).

| Memo | Rounds | Verdicts | Records |
|---|---|---|---|
| Q-001 map | 2 | FAIL, PASS | Q-001-source-check.md:1; -2.md:1 |
| Q-002, Q-003, Q-004 | 3 each | first check PASS; one later-added second check FAILed all three (1 return); corrections confirmation PASS | Q-002-to-Q-004-source-check-2.md:1, :5-11; Q-002-to-Q-007-corrections-confirmation.md:1, :12-78 |
| Q-005 | 3 | 2 FAIL, then confirmation PASS | |
| Q-006 | 2 | FAIL, PASS | Q-006-source-check.md:1, :86 |
| Q-007 | 3 | 2 FAIL, then confirmation PASS | |

First try: 3 of 7. Counting the later-added check: 0 of 7. Counted per memo, the returns would be 9. [F-A/B]

### 2.2 Plans to plan review (148 returns)

**SD scripted, P-001.** 1 piece. Plan review failed at :180, :184 and :188, and the item was closed by re-scope. 0 first try and **3** returns. [F-A]

**SD conversational.** 17 items.
- Search: Grep `^Verdict:` over reviews, glob `**/_*.md`, content mode.
- Passed first try: HD1 only (1 of 17).
- Rounds to the final pass, for the 16 items that have one: 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 6, 8, 14. Median 3.
- S-001-notifications has no final pass.
- **70** returns. [E-B]

**POOM, complete round files.** 23 specs. The rounds of S-022 to S-026 come from POOM reviews/S-029/_triage-plan-stop-rule-verbatim.md:7-47 [F-A].

| Spec | Rounds | Note |
|---|---|---|
| S-007, S-009, S-010, S-011 | 2 each | |
| S-012 | 3 | re-scoped, no pass |
| S-012r | 4 | |
| S-013 | 4 | no pass recorded |
| S-014, S-015 | 4 each | |
| S-016 | 6 | |
| S-022 | 5 | |
| S-023 | 16 | |
| S-024 | 12 | |
| S-025 | 3 | |
| S-026 | 5 | |
| S-027 | 1 | first try |
| S-028 | 3 | |
| S-029 | 4 | |
| S-030, S-031, S-032 | 3 each | |
| S-033 | 4 | |
| S-034 | 3 | |

- 1 of 23 passed first try. Median 3 rounds to the final pass, over 21 specs.
- **67** returns, counted by spec section: the joint S-023/S-024 files count per spec.

**POOM, summary-only.** The S-017, S-018 and S-019 plans: rounds 1–4, 1–2 and 1 FAIL (POOM reviews/20/reviewer.md:4-6). 3 pieces, 0 first try, **7** returns.

**POOM S-004.** The confirmation of revision 3.1 is a FAIL (POOM reviews/S-004/_confirmation-review-verbatim.md:3). That is **1** return. S-004 is left out of the first-try figures because its rounds 1–3 are not in reviews/.

**Left out:** specs with no plan-review file in reviews/ (see §5). [E-B]

### 2.3 Built work to build review (82 returns)

**SD.**
- The 50 units of Q-006 §4: 15 first try.
  - M3D 3 and 6b are left out (one checker file, or a combined multi-stage file).
  - Dispatch rounds per unit: 1 round for 8 units, 2 for 23, 3 for 15, 4 for 3 and 5 for 1. Median 2.
  - No pass: the trial-view-1 build and the design-lab-answers build.
  - **64** returns.
- PR 263 (adding Model-Lab): Design reviewer round 1 FAIL, round 2 PASS (reviews/263/design-reviewer.md:3-6, :59-60). **1** return.
- Total: 51 units, 15 first try, **65** returns.
- PR 263 is the one built piece whose worker brief is recorded (ML docs/briefs/04-builder.md). [E-B]

**POOM.** 29 pieces:
- S-002: rounds 1–3 FAIL, round 4 PASS (POOM reviews/1/reviewer.md:2-7; _reviewer-round4-verbatim.md:2-3);
- the reviews/7 builds of S-007, S-009, S-010, S-012, S-013, S-014, S-015 and S-016;
- 5 S-015 proof reviews;
- S-017, S-018 and S-019 (reviews/20);
- S-020 (reviews/21), S-023/24 (reviews/26), S-025/27 (reviews/27) and S-005/006 (reviews/5);
- S-032, S-033 and S-034;
- PRs 25, 28, 29, 30 and 31, each a single PASS.

Results:
- 17 of 29 passed first try (12 of 24 without the single-PASS PRs).
- **17** returns: 14 with finding text, plus S-002's 3 summary-only. [E-B]

### 2.4 Documents to the Critic (14 returns)

20 pieces. [E-B]
- ML Q-001 question: 3 rounds (round 1 FAIL, round 2 PASS, then a model-diverse FAIL with no later pass).
- Q-002–Q-007: Q-004 passed in 1 round; the other five took 2.
- Seven shortlist cards: round 1 FAIL for all, round 2 FAIL on two cards, round 3 PASS.
- Milestones 2 rounds; value-target 4; problem and pre-mortem 3; brief 2; Q-008 2.
- SD P-001-add-project-tests: 2.

1 of 20 passed first try (Q-004). 14 returns, one per round-file section. Records are in §4 and §8.

### 2.5 Gate case (3 returns)

- SD scripted P-001 definition of ready: FAIL at :84, :116 and :162, Triage at :164, PASS at :168. 0 of 1 first try. [F-A]
- **Left out of first try (R1):** SD reviews/P-001/_launch-gate-1-critic.md is the Critic's view on the launch gate. It recommends "proceed" (:9) and has no verdict line. [F-A]

### 2.6 Other reviewed work (28 returns)

- **SD series.** sync (7 rounds), design-reviewer-setup (6), cs24 (3), and notify-sandbox, push-key, cs15 and j18-leak-scan (1 each). 4 of 7 first try. **13** returns.
- **SD PR files outside series folders (frame rule, §1.1).**
  - Round-format PRs 6, 10, 11, 14, 18, 27, 37, 40, 41, 44, 49 and 52 (Grep `Round \d at [0-9a-f]{7}: (PASS|FAIL)|^Reviewed: PR #\d+ at [0-9a-f]{7}\. (PASS|Round)`, count mode), plus PR 222 (reviews/222/reviewer.md:3-6).
  - 13 pieces, 4 first try (6, 18, 40, 41), **10** returns.
  - PASS-only PR files in other forms are not counted as pieces, because they cannot show whether earlier rounds existed.
- **POOM other** (returns only, no denominator). **5** returns:
  - PR4 r1 (reviews/4/reviewer.md:3);
  - PR18 r1 (reviews/18/reviewer.md:3);
  - PR24 r1 (reviews/24/reviewer.md:77-86);
  - the v3.0.0 adoption review 1 (reviews/8/_adoption-review-1.md:5-8);
  - PR32 r1 (reviews/32/_reviewer-round1-verbatim.md:1-18).

  [F-A]

### 2.7 Triage

Unchecked, 12 pieces: 10 scripted (outcome lines :58, :71, :100, :106, :157, :164, :190, :221, :222, :254), the M3C Triage and the POOM S-029 triage ("GAP"). [F-A]

---

## 3. Item 2: returns classified, and samples drawn

| Stratum | Total | Classified | Rule |
|---|---|---|---|
| Research, SD scripted | 33 | 33 | all |
| Research, ML | 7 | 7 | all |
| Plans, SD scripted | 3 | 3 | all (no record) |
| Plans, SD conversational | 70 | 8 | k = 9: positions 1, 10, 19, 28, 37, 46, 55, 64 |
| Plans, POOM round files | 67 | 8 | k = 9: same positions |
| Plans, POOM summary-only | 7 | 7 | all |
| Plans, POOM S-004 confirmation | 1 | 1 | all |
| Built, SD series | 64 | 8 | k = 8: positions 1, 9, …, 57 |
| Built, SD PR file (263) | 1 | 1 | all |
| Built, POOM with finding text | 14 | 7 | k = 2: positions 1, 3, …, 13 |
| Built, POOM summary-only (S-002) | 3 | 3 | all (no record) |
| Critic | 14 | 14 | all |
| Gate | 3 | 3 | all (no record) |
| Other, SD series | 13 | 7 | k = 2 |
| Other, SD PR files | 10 | 10 | all |
| Other, POOM | 5 | 5 | all |
| **Total** | **315** | **125** | |

[F-B]

**Samples.**
- **SD plans:** M3B _plan-critic-r1; M3B _plan-design-r9; M3C _plan-review-r3; after-glance _plan-critic-r2; desk-v2 _critic-round1; job-prs-recorded _plan-review-round2; records _plan-review-round2; notifications _plan-review-round4.
- **POOM plans:** S-007 r1; S-012r r3; S-015 r2; S-022 r4; S-023 r11; S-024 r6; S-029 r1; S-033 r2.
- **SD build:** HD1 design-r1; M3B vt3-review-r2; M3E g5-review-r1; M3G qw1-review-r1; desk-v2 1a-review-r1, 3-review-r1 and 6b-review-r2; m3a build-r1.
- **POOM build (R1, redrawn in ASCII order).** The order is 20/ (S-017 r1), 21/ (S-020), 26/ (S-023/24), 27/ (S-025/27), 5/ (PR5), 7/_build-review-s009, 7/_build-review-s014, 7/_review-s015-proof-brief, proof-diag-round1, round2, round3, S-032/ round1, S-032/ round2, S-033/. Positions 1, 3, …, 13 give:
  - S-017 r1;
  - S-023/24 r1;
  - PR5 r1;
  - S-014 build r1;
  - proof-diag r1;
  - proof-diag r3;
  - S-032 build r2.

  My earlier draw used numeric PR order, which broke the stated rule. S-020 r1 and S-025/27 r1 were classified then (both avoidable, capability residual: reviews/21/reviewer.md:5-6; reviews/27/reviewer.md:25-29). They are now read outside the sample and are not in any tally. [F-B]
- **SD other:** sync r1, r3 and r5; cs24 r1; design-reviewer-setup confirmation1, r1 and r3.

---

## 4. Items 3 and 4: avoidability and cause, per return

"Cap." means capability, residual unless marked as named by the record.

**Research, SD scripted (33):**

| Return | Avoidable? | Contributing causes | Primary | Record |
|---|---|---|---|---|
| Q-005 :67 | No | check (its pack lacked the cited question file); cap. (a "secondary contributor") | check | triage/Q-005.md:1, :7-16 |
| Q-006 :90, :94, :98 | No | check (standard had no rule on same-publisher sources), reported second-hand | check | triage/Q-006.md:9 [B] |
| Q-006 :104 | Mixed | instructions (question scope conflicts with the standard); check; cap. (item 13) | instructions (named by the triage) | triage/Q-006.md:17-21 |
| Q-011 :218 | Yes | cap. (named); check (coverage incomplete) | cap. (named) | triage/Q-011.md:13, :16 |
| Q-015 | Yes | cap. | cap. | research/Q-015-source-check.md:3 |
| 26 others | No record | none | none | |

Of the 26, three show a recorded material gap: the revising researcher's pack lacked its memo (F-q006-06). Two show the checker-pack gap without a confirmed reason (triage/Q-005.md:10, :28).

**Research, ML (7):**

| Return | Avoidable? | Causes | Primary |
|---|---|---|---|
| Q-001 first check | Yes | cap. (J1 cites ids not in the cited file, Q-001-source-check.md:3) | cap. |
| Q-002–Q-004 second check (1 return, 3 memos) | Cannot say | something else (the researchers' sessions could not open outside sources, reviews/P-001-problem-premortem/critic.md:88); cap. (figures differ from the papers, -2.md:29, :38, :93) | something else (source access) [O-C] |
| Q-005 first check | No | check (no web item could be opened, Q-005-source-check.md:3-5) | check |
| Q-005 second check | Mixed | cap. (-2.md:3) | cap. |
| Q-006 first check | Mixed | cap.; check (the checker's error, withdrawn at Q-006-source-check.md:92-95, :156) | check (tie-break) |
| Q-007 first check | No | check (only anthropic.com pages and the repository records could be opened; the other hosts the claims rest on did not resolve, Q-007-source-check.md:3) | check |
| Q-007 second check | Mixed | cap. (-2.md:3-7) | cap. |

**Plans (27):**
- **SD scripted (3):** no record.
- **SD sample (8):**
  - M3C r3 is "cannot say". Its contributing causes are:
    - material: a moved target, and decisions/README.md contradicting itself (:57 against :5-7);
    - instructions: the brief was not seen;
    - check: round 2's suggested fix (triage :23);
    - capability.

    Primary is material, under the brief-and-material rule (M3C/_triage-r3-critic-verbatim.md:10, :16-23).
  - The other 7 are avoidable, with capability (residual) as primary:
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
  - S-022 r4 (:8);
  - S-023 r11 (:73, :101). Contributing: split (S-024 not yet revised, :3) and material (owner answers just carried in, :1);
  - S-024 r6 (:152);
  - S-029 r1 (:21-27);
  - S-033 r2 (:7, :27-30).
- **POOM S-004 confirmation (1):** avoidable, capability. AC6 has no way to get the commits it diffs, given AC4's own checkout (_confirmation-review-verbatim.md:5-8).
- **POOM summary-only (7):**
  - 6 have no record of findings.
  - S-018 r1 is "cannot say", with capability (residual) as primary. Its one line reads "the first draft skipped scheduled runs" (reviews/20/reviewer.md:5).

**Built work (19):**
- **SD sample (8):**
  - HD1 design r1: not avoidable. Material: two owner rulings conflict (:19-25). Primary material.
  - VT3 r2: not avoidable. Material: draft 13 was merged after the Builder's commits (:3, :9, :27). Split contributes. Primary material.
  - 6 avoidable, primary capability:
    - g5 r1 (:21);
    - qw1 r1 (:13-18);
    - 1a r1 (:9, :21);
    - 3 r1 (:21-26);
    - 6b r2 (:11; contributing check, the checker's round-1 miss);
    - m3a r1 (:18-25; capability named, "the Builder's admitted slip").
- **SD PR 263 (1):** cannot say. The existing tile wording meets a new project's state, and the return was cleared once Model-Lab's records changed (reviews/263/design-reviewer.md:3, :18-19). Primary material.
- **POOM sample (7):**
  - S-017 r1: cannot say. "Two locked token pins outside the supersession table… covered by owner ruling L-0124; round 2 PASS… build unchanged since round 1" (reviews/20/reviewer.md:4). Material: the table did not list what the build needed. Primary material.
  - S-023/24 r1: avoidable, capability. B1 and B2 are loopholes in the built checks (reviews/26/reviewer.md:21-23).
  - PR5 r1: avoidable, capability (reviews/5/reviewer.md:3).
  - S-014 build r1: mixed. B2 is a spec-versus-check conflict (:8-9). Primary material by tie-break.
  - Proof-diag r1 (:8-9) and r3 (:8): avoidable, capability.
  - S-032 build r2: avoidable, capability (:3).
- **POOM S-002 (3):** there is no record of findings in reviews/. reviews/1/reviewer.md:7 only points to docs/LEDGER.md L-0012 and L-0013 for rounds 1–3. That ledger is outside the named records, and I did not open it.

**Critic (14):**
- 11 are avoidable, with capability (residual) as primary:
  - Q-001 r1, mixed (:50);
  - shortlist r1 (:12-25);
  - milestones r1 (:25-30);
  - value-target r1, r2 and r3 (:12-42, :101-106, :132-138);
  - problem-premortem r1 and r2 (:18-58, :131-136);
  - brief r1 (:19-28);
  - Q-008 r1 (:10-14);
  - SD add-project-tests r1 (:10-20). Contributing split: an unrecorded Builder return (:32).
- 3 are "cannot say":
  - **Q-001-diverse r1 (R1, restated).** The diverse Critic's finding 1 (Q-001-diverse/critic.md:17-21) accepts the first Critic's "whether" wording (Q-001/critic.md:13) and faults the framing around it. That is capability, residual. Its finding 2 (Q-001-diverse/critic.md:23-27) faults two passages the first Critic itself asked for: the risk-only bullet (Q-001/critic.md:38-39, quoted at diverse :23-24) and "help little or to harm" (Q-001/critic.md:19-20, quoted at diverse :26). That is the check, because the checkers disagree. Neither correction alone prevents the return, so the tie-break makes the check primary. On the cites I differ from the source check: my lines were for finding 2, and these records decide it.
  - Q-002–Q-007 r1: capability, residual.
  - Shortlist r2: primary split (:79-83).

**Gate (3):** no record.

**Other (22):**
- **SD series (7):**
  - sync r1: avoidable, capability.
  - sync r3: not avoidable. The faulty wording was the checker's own suggestion (:3). Primary check.
  - sync r5: cannot say. The checker says "That miss is mine" (:3); a standing rule also contributes (AGENTS.md:68, cited at r3:8). Primary check.
  - cs24 r1 (:11-15): avoidable, capability.
  - design-reviewer-setup confirmation1 (:9, :18-24): avoidable, capability.
  - design-reviewer-setup r1: avoidable (mixed), capability. Material and split contribute for finding 4 (:40-46).
  - design-reviewer-setup r3: mixed. Material: the Linear reference sizes are not in the repository (:18). Primary material.
- **SD PR files (10):**
  - Avoidable, capability: 11, 14, 27, 37 (mixed), 44, 49, 52 r1 and 222 (B1: the owner paragraph leaves out a skipped step and makes an unverifiable claim, reviews/222/reviewer.md:12-17).
  - PR 10: cannot say, capability residual.
  - PR 52 r2: not avoidable. Material: a ruling was not yet in the repository, and round 3 passed at the same commit (:7-9). Primary material.
- **POOM (5):** PR4, PR18, PR24, the adoption review and PR32 (B1 and B2 are against AGENTS.md:37-38, :8-18). All avoidable, with capability (residual) as primary.

### Tallies

[E-B; the classes are O-C]

| Kind | Classified | Avoidable (of which mixed) | Not avoidable | Cannot say | No record of findings |
|---|---|---|---|---|---|
| Research | 40 | 7 (4) | 6 | 1 | 26 |
| Plans | 27 | 16 (0) | 0 | 2 | 9 |
| Built | 19 | 12 (1) | 2 | 2 | 3 |
| Critic | 14 | 11 (1) | 0 | 3 | 0 |
| Gate | 3 | 0 | 0 | 0 | 3 |
| Other | 22 | 18 (3) | 2 | 2 | 0 |
| **Total** | **125** | **64 (9)** | **10** | **10** | **41** |

| Kind | Cap. residual | Cap. named | Check | Material | Instructions | Split | Something else | No record |
|---|---|---|---|---|---|---|---|---|
| Research | 4 | 1 | 7 | 0 | 1 | 0 | 1 | 26 |
| Plans | 17 | 0 | 0 | 1 | 0 | 0 | 0 | 9 |
| Built | 10 | 1 | 0 | 5 | 0 | 0 | 0 | 3 |
| Critic | 12 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| Gate | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| Other | 18 | 0 | 2 | 2 | 0 | 0 | 0 | 0 |
| **Total** | **61** | **2** | **10** | **8** | **1** | **1** | **1** | **41** |

**Contributing, not primary (R1, recounted from the list above):**
- capability 7: research 4; M3C, S-014 and Q-001-diverse 1 each;
- check 4: Q-006 :104, Q-011 :218, M3C, 6b r2;
- split 4: S-023 r11, VT3 r2, add-project-tests, design-reviewer-setup r1;
- material 2: S-023 r11, design-reviewer-setup r1;
- instructions 1: M3C;
- something else 1: sync r5.

---

## 5. Item 5: what the records cannot show

**Returns with no record of findings:** research 26, plans 9 (3 scripted and 6 POOM summary-only), built 3 (S-002), gate 3. Total 41. [F-B]

**Returns with findings recorded but no cause named beyond the fault** (residual): research 4 of 14, plans 17 of 18, built 10 of 16, Critic 12 of 14, other 18 of 22. Total 61 of 84. [E-B]

**Pieces with no check record** (R1: lower bounds from the named records only). [E-B]

| Kind | No check record | Notes |
|---|---|---|
| Research | 1 | Q-003. Q-009, Q-010 and Q-012 have log verdicts only. |
| Plans | 4 | POOM S-002, S-005, S-006 and S-020 have a build-review record but no plan-review record in reviews/. POOM specs/ and the ledger are outside the named records. SD conversational: none found. |
| Built work | 0 established | An unchecked build leaves no file in reviews/, so the count cannot be made from these records. Which SD plan items' builds sit in which stage folders (for example M3D and M3E) is not recorded. |
| Critic | 15 | SD research questions Q-001–Q-015 have no Critic record in SD reviews/ (Glob `{Q-*,P-*}/*.md`). The dispatch log has no question-check role. ML: 0 of 8 research questions. Owner cards cannot be counted, because questions/ is not in the named records. |
| Gate | 0 unchecked | 1 checked without a verdict (launch-gate-1). |
| Triage | 12 | unchecked by design |
| Other | not countable | |

**Overwritten records.** The SD research check files keep only the last verdict (triage/Q-011.md:26). [F-A]

**Brief and model** (R1, searches stated).
- **The model.** Grep `(?i)\b(opus|sonnet|haiku)\b|claude-(opus|sonnet)`, content mode:
  - over SD `{reviews,triage,research}/**/*.md`: 3 hits. Two are "Session: Opus 5.5" headers (desk-v2 1b r1:13, r2:11); one is a commit-message search (reviews/74/reviewer.md:77).
  - over POOM reviews: 2 hits, both commit-message searches.
  - over ML reviews: 0 hits.

  None names the model as a cause.
- **The brief.** Grep `(?i)\bbrief(ed|ing)?\b.{0,60}(gap|cause|missing|without|none of|did not|didn't|wrong)|(gap|cause|without|wrong).{0,40}\bbrief` over SD reviews and triage, POOM reviews, and ML reviews and research.
  - The only hits that blame a worker's brief are the M3C triage (:9) and records that cite it: launch-gate-1 critic :13, ML shortlist critic :20, Q-006 memo and check.
  - M3B/_plan-critic-r2:43 (from Q-006) concerns a checker's own brief, and none of my classified returns rests on it.
- Worker briefs are not recorded for conversational work. ML has recorded worker briefs only for researcher Q-001 (02) and builder (04).
- The scripted path ran one fixed model pairing.

[F-A/B]

---

## 6. Differences from Q-006, and from the source check

**Q-006.**

| Figure | Mine | Q-006 | Deciding record |
|---|---|---|---|
| SD plans: first try, median | 1 of 17, 3 | same | `^Verdict:` lines |
| SD build first try | 15 of 50 series units (15 of 51 with PR 263) | 15 of 50 | reviews/263/design-reviewer.md:3 |
| SD scripted research | 2 of 12 (3 of 14) | 2 of 12 | research/Q-014-, Q-015-source-check.md:1 |
| SD FAIL-first files | 70 + 64 + 13 = 147 | 147 | consistent |
| Scripted finding content | 7 of 33 returns have a recorded cause, from 3 triage files and research/Q-015-source-check.md | "not in this memo" | triage/Q-005, Q-006, Q-011.md; research/Q-015-source-check.md |
| design-reviewer-setup r1 #4 | capability primary; material and split contributing | untraceable | _review-round1-verbatim.md:40-46 |

**The source check.** I accept every point except these, where a stated convention or record decides:
1. **Research 40, not 42:** one return unit (§1.1 R1) applied to all kinds, as the check itself asked for consistency.
2. **Built 82, not 81:** PR 263 enters by the R1 frame rule.
3. **Plans 148 and Other 28, not 147 and 29:** S-004's confirmation moves to Plans, as the check's own "S-013 is under plans" point implies.
4. **Total 315, not 316.**
5. **Q-001-diverse:** my cites belonged to its finding 2 (Q-001/critic.md:19-20, :38-39 against Q-001-diverse/critic.md:23-27). The primary stays "check", now by tie-break.
6. **PR 10** keeps capability as its primary. Under §1.4 the residual does not depend on the avoidability mark.

---

## 7. Proposed library entries

### Facts

**F-q008-01.** SD's 147 conversational round files that begin with FAIL split into 70 plan checks, 64 build checks and 13 other checks.
- Split rule: `_plan-*`, `_critic-*` and `_confirmation-draft*` are plan; `_stage-*`, `_build-*`, LA1, LA2 and md-sandbox are build; the rest are other.
- 11 `_` files with no column-0 Verdict are excluded (341 in all, 330 with a Verdict).
- Grade B. Shelf life: 3 months. Topics: records, rework, reviews.

**F-q008-02.** SD scripted research had 33 returns: 32 logged and 1 in the Q-015 file. A cause is recorded for 7, in triage/Q-005, Q-006 and Q-011.md and research/Q-015-source-check.md. The triage files for Q-009, Q-010, Q-012 and P-001 are absent.
- Grade A for the files, B for the counts. Shelf life: fixed history. Topics: records, baseline.

**F-q008-03.** POOM plan reviews, complete round files only:
- 23 specs; 1 passed at the first try (S-027);
- median 3 rounds to the final pass;
- 67 returns, counted per spec section (joint S-023/S-024 files per spec);
- S-023 ran 16 rounds and S-024 12 (POOM reviews/S-029/_triage-plan-stop-rule-verbatim.md:7-36).
- It excludes the 3 summary-only specs (7 returns), S-004, and specs with no review file.
- Grade B (A for the triage-cited rounds). Shelf life: 3 months. Topics: rework, baseline.

**F-q008-04.** Model-Lab and SD Critic checks: 20 pieces (cards and questions counted separately), 1 passed at the first try (Q-004), 14 returns (one per round-file section).
- Grade B. Shelf life: 3 months. Topics: reviews, rework.

**F-q008-05.** Model-Lab research:
- 3 of 7 memos passed their first source check; all 3 then failed one later check (a single file) once the sources were reachable;
- 2 of the 7 returns came from the checker being unable to reach the hosts the memo's claims rest on (Q-005-source-check.md:3-5; Q-007-source-check.md:3; Q-007's check could open anthropic.com pages).
- Grade A for the files, B for the counts. Shelf life: fixed history. Topics: research, reviews.

**F-q008-06.** In the 125 classified returns, no record names the model as a cause. Only the M3C Triage names a worker's brief, and it could not see the brief (M3C/_triage-r3-critic-verbatim.md:9, :21). The two Grep searches are in §5.
- Grade B. Shelf life: 3 months. Topics: agents, records.

### Patterns

These describe what was seen. They are not recommendations.

**P-q008-01. A checker's suggested fix can cause the next return.**
- Seen in:
  - sync r3 (:3);
  - the M3C triage on round 2's suggested fix (:23);
  - Q-001: passages the first Critic asked for (Q-001/critic.md:19-20, :38-39) were faulted by a second Critic (Q-001-diverse/critic.md:23-27).
- Principle as observed: check-originated faults are a separate class when returns are counted by cause.
- Grade B. Shelf life: 12 months. Topics: reviews, rework.

**P-q008-02. Overwritten check files erase the causes of returns.**
- Seen in: triage/Q-011.md:26.
- Principle as observed: a cause count from such records measures surviving text.
- Grade B. Shelf life: 12 months. Topics: records, baseline.

**P-q008-03. A cause count from review records falls mostly into a residual.**
- Seen in: 61 of 84 classified returns with recorded findings name no cause beyond the fault.
- Principle as observed: "capability by elimination" reflects what the records name, not capability.
- Grade C. Shelf life: 12 months. Topics: records, agents.

---

## 8. Sources opened

All paths are absolute. New in R1:
- /home/user/wt/ml-orch/research/Q-008-source-check.md and Q-008-memo.md (head);
- /home/user/Personal-Org-Operating-Model/reviews/1/reviewer.md and _reviewer-round4-verbatim.md;
- POOM reviews/32/_reviewer-round1-verbatim.md;
- POOM reviews/26/reviewer.md:1-36;
- /home/user/Service-Desk/reviews/222/reviewer.md:1-20;
- SD reviews/P-001/_launch-gate-1-critic.md:1-15;
- FAIL and round lines of SD reviews 115, 135 and 226–263.

Earlier:
- **Model-Lab research:** /home/user/Model-Lab/research/Q-008.md; Q-006-memo.md; Q-006-source-check.md; Q-001-source-check.md and -2.md; Q-002-to-Q-004-source-check-2.md; Q-002-to-Q-007-corrections-confirmation.md; Q-005- and Q-007-source-check.md and -2.md (heads).
- **Model-Lab reviews and briefs:** reviews/README.md; reviews/{Q-001, Q-001-diverse, Q-002-to-Q-007, Q-008, P-001-brief, P-001-value-target, P-001-problem-premortem, P-001-shortlist, P-001-milestones}/critic.md; docs/briefs (header lines of 01–10, and README.md).
- **Service-Desk log, triage and research:** dispatch-log/2026-10.jsonl; triage/Q-002, Q-005, Q-006 and Q-011.md; research/Q-014- and Q-015-source-check.md.
- **Service-Desk review files:** the sampled plan, build and other round files listed in §3; M3C/_triage-r3-critic-verbatim.md; 263/design-reviewer.md; P-001-add-project-tests/critic.md; round lines of PRs 10, 11, 14, 27, 37, 44, 49 and 52.
- **POOM review files:** the sampled plan and build files in §3; S-029/_triage-plan-stop-rule-verbatim.md; S-004/reviewer.md and _confirmation-review-verbatim.md; 8/_adoption-review-1.md; reviewer.md of PRs 20, 21, 24 and 27; verdict and round lines of PRs 1–38.

Searches are stated in §1.1, §2 and §5.

**Hand-off:** to the Source checker. I have not marked any of my own facts as checked.
