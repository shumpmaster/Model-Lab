Verdict: PASS

*The Source checker's check of research/Q-008-memo.md (brief: docs/briefs/13-source-checker.md), on a different model from the Researcher, verbatim: round 1 (FAIL), round 2 on the revised memo (PASS). Recorded by the orchestrator. Session session_01QBwHGHrHnEvMNYgKDoaH8w, 2026-11-01.*

## Round 1
Verdict: FAIL

The memo is a careful piece of work and most of its figures hold. Four load-bearing figures do not reproduce, and one stated rule was not followed. Filing should wait for a corrected memo. No files were written and no entries were filed. I did not open the barred paths.

## Item 1: re-derived counts

**Held, reproduced from the same records:**
- SD scripted research: 41 rounds, 32 returns, 9 PASS, 2 of 12 first try. I parsed `dispatch-log/2026-10.jsonl`.
- Per-item rounds match, and the Q-003 error lines (:11, :19) match.
- SD conversational: 147 `_*.md` files whose first column-0 `Verdict:` is FAIL (the memo's 70+64+13 split follows if LA1 counts as build).
- 17 plan items, 1 passed first try (HD1).
- 50 build units, 15 first try. The 15th is `S-001/_reviewer-build.md`, which is the Q-006 method.
- M3E 8 of 15 and desk-v2 0 of 10.
- SD early PRs: 12 PRs, 4 first try, 9 returns.
- POOM plans: 67 returns by (spec, round), which is also what the sampling positions imply.
- POOM builds: 28 pieces, 17 first try, 14 returns. The 14 includes 4 for the S-015 proof pieces.
- ML research: 3 of 7 first try. ML Critic: 14 returns, 1 of 20 first try. Gate: 3 returns, 0 of 1.
- The §4 per-kind tallies, apart from the slips below.

**Where my figures differ, and which record decides:**
1. **S-002 is a build, not a plan.**
   - The memo counts S-002 rounds 1–3 as 3 summary-only plan returns (reviews/1/reviewer.md:7).
   - `reviews/1/_reviewer-round4-verbatim.md:3` reviews `build/tools-builder/s-002`. LEDGER L-0012 and L-0013 say "S-002 review round 1 FAILED on one weakened test" and that the build was reviewed in four rounds.
   - Corrected: Plans 150 becomes 147, and POOM summary-only plans go from 10 to 7. Built work 78 becomes 81, and POOM builds go from 14 to 17. POOM built pieces go from 28 to 29, and first try from 17 of 28 to 17 of 29 (12 of 24 without the single-PASS PRs).
2. **"Other reviewed work" is understated.**
   - POOM `reviews/32/_reviewer-round1-verbatim.md:1` is a FAIL (question-file PR for S-031). It is not counted.
   - SD `reviews/222/reviewer.md:6` (model 3.6.0 sync, round 1 FAIL) is not counted. The memo's reason for leaving out later PR files ("from about #74 they duplicate series folders") is false for PR 222, because no series folder holds it.
   - Corrected: 27 becomes at least 29, and POOM other goes from 5 to 6. The headline total goes from 314 to 316.
3. **"117 classified" is wrong.**
   - The memo's own §3 table sums to 114. PR 263, outside the frame, makes 115.
   - The bottom-line 4 table sums to 115, not 117.
   - The 114 is split as research 42, plans 19, built 15, Critic 14, gate 3 and other 21.
4. **The "81 / 58 / 23 / 41" figures in bottom line 3 are wrong.**
   - "41 classified returns have no record of findings" includes 9 POOM summary-only returns that the memo itself says are not classified. The correct figure is 32.
   - Returns classified with findings recorded: 82 (83 with PR 263). Of these, 23 name a cause outside the worker's output, and 59 are residual capability.
   - The memo's own §5 sums to 59 (4+15+11+12+17), not 58.
   - The bottom-line 4 table row "Capability, residual (2 of them named) 61" mixes the two. It is 61 capability in total, of which 59 are residual and 2 are named by a record.
5. **Smaller slips:**
   - Bottom line 5 says "4 triage files hold causes for 7 returns". It is 3 triage files (Q-005, Q-006, Q-011) plus the Q-015 source-check file.
   - The §4 tally counts 2 mixed under "Other". The text marks three: design-reviewer-setup r1, design-reviewer-setup r3 and PR 37.
   - ML research counts 9 returns because one file covering Q-002–Q-004 is split into 3. The memo discloses this. The Critic counts one return per round file, so the convention is inconsistent. By files it is 7.
   - S-004's confirmation is a plan-type check counted under "Other", while S-013's plan confirmation is counted under plans.

## Item 2: sample check

I opened the cited record lines for 30 classified returns:
- All 21 whose primary cause is not capability, plus the 2 whose capability cause the record names.
- 9 whose primary cause is capability, residual.

**Non-capability primaries opened and supported:**
- Q-005 :67, Q-006 :90/:94/:98 (second-hand via the later triage) and :104, Q-011 :218 and Q-015.
- ML: Q-001, the Q-002–Q-004 second check, Q-005 first and second, Q-006 first, Q-007 first and second.
- Plans: M3C r3.
- Built: HD1, VT3 r2, S-014 build r1, PR 263 and m3a r1.
- Critic: shortlist r2.
- Other: sync r3 and r5, design-reviewer-setup r3 and PR 52 r2.

**Capability residual sampled and supported:**
- g5 r1, desk-v2 1a r1, S-007 r1, S-032 build r2, S-023 r11.
- ML Q-001, ML Q-005 second, ML Q-007 second.
- Q-015.

**Rule application:**
- §1.3 and §1.4 were applied as written. The brief-and-material rule and the tie-break order are followed.
- The Q-006 first check is "check by tie-break", which is defensible under the order.
- PR 10 is "cannot say" yet counted as capability. This is a small inconsistency.

**Problems found:**
- **Q-001-diverse "check" reasoning is not supported by the cited lines.**
  - The memo says a new checker "failed wording the first Critic had proposed" (cites Q-001/critic.md:19-20 and Q-001-diverse/critic.md:23-27).
  - The first Critic's proposed wording is at `Q-001/critic.md:13`.
  - The diverse Critic's finding 1 is at `Q-001-diverse/critic.md:17-21`, and it accepts that wording ("does include 'whether'") and faults the surrounding framing. Lines 23-27 are a different finding.
  - "Two checkers disagreed" may still support the "check" class, but the stated reason and the line cites are wrong.
- Cite slip: the M3C-triage-r2 suggested-fix claim is right, but verify the line numbers if reused.

## Item 3: sampling rule

- **Applied as stated:**
  - SD plans: k=9, positions 1, 10, …, 64 match.
  - SD builds: k=8, positions 1, 9, …, 57 match.
  - SD other: k=2 matches.
  - POOM plans (spec number, then round): positions match.
- **Not applied as stated: POOM builds.**
  - The rule says ASCII order of full path, with N=14 and k=2.
  - ASCII order puts `20/` (S-017 r1), `21/`, `26/`, `27/`, `5/`, then `7/…`, then `S-032/`, `S-033/`. The odd positions are S-017 r1, S-023/24 r1, PR5 r1, S-014 r1, proof-diag r1, proof-diag r3 and S-032 r2.
  - The memo's sample (PR5, S-014, diag r1, diag r3, S-020, S-025/27, S-032 r2) is what numeric PR order gives.
  - Two sampled returns differ: S-017 r1 and S-023/24 r1 should have been drawn instead of S-020 r1 and S-025/27 r1.
- **Also:** excluding the 10 (really 7) summary-only POOM plan returns and the unsearched PR files as "outside the frame" was not a rule fixed in §1.2.

## Item 4: proposed entries

| Entry | Call | Change needed |
|---|---|---|
| F-q008-01 | Fileable | Add the split rule (`_plan`/`_critic` = plan; `_stage`/`_build` plus LA1 = build; others = other). Add that 11 `_` files with no column-0 Verdict are excluded. |
| F-q008-02 | Fileable | None. 33 returns and 7 with a cause reproduce. The absent triage and check files are confirmed. |
| F-q008-03 | Fileable with change | Say it covers complete round files only: 23 specs, 67 returns by spec section (joint S-023/S-024 files counted per spec). It excludes the summary-only plans (7 after the S-002 correction), S-004 and any spec with no review file. |
| F-q008-04 | Fileable with change | State the unit rule: cards and questions are counted separately, and returns are counted per round-file section. The 14 and 1 of 20 reproduce. |
| F-q008-05 | Fileable with change | Change "unable to reach any web host". The Q-007 first check could open anthropic.com pages. Say "the hosts the memo rests on". Note the 9 returns come from 7 files. |
| F-q008-06 | Hold | "117 classified" is wrong (114, or 115 with PR 263). The two absence claims (no record names the model, only M3C names the brief) need a stated search. |
| P-q008-01 | Fileable with change | Drop the Q-001 instance, or recite it correctly (see Item 2). The sync r3 and M3C-triage instances hold. |
| P-q008-02 | Fileable | None. `triage/Q-011.md:26` confirms the overwrite. |
| P-q008-03 | Hold | "58 of 81" is wrong. It is 59 of 82 (83 with PR 263). It is fileable once corrected. |

## Item 5: the question's five items

- All five are answered. Definitions and left-out lists are given, a sampling rule is stated, and the avoidability test and cause rules are stated before classifying. Counts of returns with no recorded cause are given per kind.
- Gap: pieces with no check record at all are not counted per kind for plans, built work and the Critic. POOM specs with no plan-review file were not searched, as the memo admits. Only the research pieces (Q-003, Q-009, Q-010, Q-012) and the P-001 Definer report are listed.
- Corrected headline counts would be: Plans 147, Built 81 (+1 outside the frame), Research 42, Other at least 29, Critic 14, Gate 3, total 316 (the memo says 314). Classified: 114 in the frame, 115 with PR 263.

Files checked, all read-only:
- /home/user/wt/ml-orch/research/Q-008-memo.md
- /home/user/Service-Desk/dispatch-log/2026-10.jsonl
- /home/user/Service-Desk/reviews, triage and research
- /home/user/Personal-Org-Operating-Model/reviews
- /home/user/Model-Lab/reviews and research

## Round 2
Verdict: PASS

The revision resolves every finding from my first record. The changed totals reproduce from the records and from the memo's own tables. Remaining slips are small and listed below. Nothing written or filed.

## Findings from the first record

| Finding | Status |
|---|---|
| S-002 is build, not plan | Resolved. Plans 150 became 148 (147 plus S-004), POOM built is 29 pieces and 17 returns, first try 17 of 29 (12 of 24). |
| PR 222 and POOM PR 32 missed | Resolved. Both are counted. The frame rule in §1.1 is stated, and its search (39 SD files, 36 POOM files) reproduces. The SD files that remain outside series folders are 10, 11, 14, 27, 37, 44, 49, 52, 222 and 263. The 36 POOM files are all accounted for in §2. |
| 117, 41/81/58 wrong | Resolved. 125 classified, 84 with findings (21 outside the worker, 2 named slips, 61 residual), 41 with no record. These sum correctly and agree with §5. |
| POOM build sample drawn in numeric order | Resolved. My ASCII ordering gives odd positions S-017 r1, S-023/24 r1, PR5 r1, S-014 r1, diag r1, diag r3, S-032 r2, which is exactly the redrawn sample. S-020 and S-025/27 are dropped from the tallies. |
| Q-001-diverse reasoning and cites | Resolved. The restatement is correct. Finding 1 (diverse :17-21) accepts the first Critic's "whether" wording (Q-001/critic.md:13). Finding 2 (diverse :23-27) faults passages the first Critic asked for (Q-001/critic.md:38-39 and :19-20). The class (check, by tie-break) is supported. |
| Smaller slips (3 triage files plus Q-015, 3 mixed in Other, Q-007 wording, split rule, ML 9 vs 7) | Resolved. |
| Pieces with no check record per kind | Resolved as lower bounds. The Critic figure of 15 SD questions with no Critic file and 0 of 8 ML questions checks out. |

## Re-derived totals

- **Returns:** 148 plans, 82 built, 40 research, 28 other, 14 Critic, 3 gate, total 315. The stratum table sums to 315 returns and 125 classified.
- **Per-kind tallies:** I recounted each kind's avoidable, not avoidable, cannot-say and no-record columns, and the cause table.
  - The totals are 64 avoidable (9 mixed), 10 not avoidable, 10 cannot say and 41 no record.
  - By cause: 61 residual capability, 2 named capability, 10 check, 8 material, 1 instructions, 1 split, 1 something else and 41 no record.
  - Both tables sum to 125.
  - §5's residual-by-kind figures (4 of 14, 17 of 18, 10 of 16, 12 of 14, 18 of 22) sum to 61 of 84.
- **First-try figures:** SD built 15 of 51, POOM built 17 of 29, SD other PRs 4 of 13. These reproduce.

## Newly classified returns

I opened the cited lines for each of these:
- **S-017 r1** (reviews/20/reviewer.md:4): cannot say, material primary. It is defensible, since the supersession table omitted the locked pins and the owner ruling L-0124 covered them.
- **S-023/24 r1** (reviews/26:21-23): the two blockers are loopholes in the built checks, so avoidable, capability.
- **PR 222** (reviews/222/reviewer.md:12-17): the owner paragraph omits the skipped step and makes an unverifiable claim. Avoidable, capability.
- **PR 32** (B1 id used as subject, B2 wrong reason for approval): avoidable, capability. This agrees with AGENTS.md:37-38.
- **S-004 confirmation** (:5-8): AC6 lacks the commits it diffs, given AC4's own checkout. Avoidable, capability.
- **Summary-only strata:**
  - S-017, S-018 and S-019 plans: 6 returns have no finding text. S-018 r1 has the one line "first draft skipped scheduled runs", so it is cannot-say, capability.
  - S-002: 3 returns, no record in reviews/.

## The six disagreements in §6

1. **One return unit (research 40, not 42): accept.** The check asked for a single convention. ML research is now 7 files, and the Critic is already per section. Joint POOM files count per spec section, which fits the same rule.
2. **PR 263 in frame (built 82): accept.** It has no series folder and is its own source under the frame rule.
3. **S-004 under plans (148 and 28, not 147 and 29): accept.** It is a plan check like S-013's confirmation.
4. **Total 315, not 316: accept.** The difference is points 1 to 3.
5. **Q-001-diverse cites: accept.** Verified above.
6. **PR 10 as capability residual: accept on the substance.** The record gives the fault, "the memo carried the researcher's own summary", and points nowhere else. That meets the §1.4 residual definition as it stood originally.

## Remaining slips (none moves a figure or a class)

- The revision note says "The rules in §1.3 and §1.4 are unchanged", but they were edited.
  - §1.4 gained the clause "and it does not depend on the avoidability mark", added to support the PR 10 call.
  - §1.3 and §1.4 lost the "(with evidence, not later withdrawn)" qualifier, the examples under "Not avoidable", and the "Upstream causes come first" sentence.
  - The substance is close to the original, but the "unchanged" claim should be corrected, or the edits disclosed.
- S-002's causes are in docs/LEDGER.md L-0012 and L-0013 (weakened test, digest traceback, line-ending regression), which is outside the named records. "No record of findings" holds only as "none in reviews/". Say so in §4.
- The §4 note on the three material-gap returns cites the library entry F-q006-06 second-hand. I did not re-open it in this pass.

## Per-entry filing call for §7

| Entry | Call |
|---|---|
| F-q008-01 | Fileable. The split rule is stated, and 70/64/13 reproduce. |
| F-q008-02 | Fileable. |
| F-q008-03 | Fileable. The exclusions are stated. 67 returns by spec section and median 3 over 21 specs reproduce. |
| F-q008-04 | Fileable. The unit rule is stated. The 14 and 1 of 20 reproduce. |
| F-q008-05 | Fileable. 3 of 7, 2 of the 7 returns and the Q-007 wording are right. |
| F-q008-06 | Fileable. 125 is right. I ran the model-name search (3 SD hits, 2 POOM hits, 0 ML hits, none a cause). I ran the brief search too. For classified returns, only the M3C Triage blames a worker's brief. |
| P-q008-01 | Fileable. The Q-001 instance is now correctly cited. |
| P-q008-02 | Fileable. |
| P-q008-03 | Fileable. 61 of 84 is correct. |

All nine entries may be filed once the "unchanged" wording in the revision note is fixed. That wording is not a figure and does not hold the entries.

Records checked, all read-only:
- /home/user/wt/ml-orch/research/Q-008-memo.md
- /home/user/Service-Desk/reviews, triage and research
- /home/user/Personal-Org-Operating-Model/reviews
- /home/user/Model-Lab/reviews and research
