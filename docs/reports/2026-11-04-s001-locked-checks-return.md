# The Check author's return on S-001's locked checks (brief 72), verbatim

*Recorded by the Orchestrator, 2026-11-04. The writer's own summary of its work: kept out of the Critic's and the Reviewer's packs (docs/reports/**). The commit it describes is e0d8104 on build/check-author/s001-locked.*

## S-001 locked checks (dispatch b): AC1 to AC11 and join tests J1 to J8, committed on `build/check-author/s001-locked`

The 20 files are committed, but 179 of 222 tests fail because the Builder's scripts under `src/E-003/` do not exist yet.

**Where and how to run.** Worktree is `/tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/wt-check`, branch `build/check-author/s001-locked`. Commit `e0d8104cc7e2f88f19e6370d0cf84743d92e9679` is the only commit, on top of 7d6c999. `git log --format='%an %ae' -3` gives:
- check-author check-author@agents.invalid
- orchestrator orchestrator@agents.invalid
- orchestrator orchestrator@agents.invalid

The commit message carries `Agent-Session: session_01QBwHGJ9ZMyT9fK17HjfmCc` and `Spec: S-001`. I left off the attribution reminder's Co-Authored-By line because the project CLAUDE.md and the role file forbid model names in commits.

Run everything with `python3 -m unittest discover -s tests/acceptance -p 'test_*.py'` from the worktree root. Standard library only; pytest is not installed. For one file, use `-p 'test_j7*.py'`.

### 1. Files, the criterion or join each checks, and current result
Everything is in `tests/acceptance/`. Eight tests in the table pass now; every other test that passes now is in one of the 100%-pass files (AC1, J7, J8) or in the "partly pass" row.

| File | Checks | Result now |
|---|---|---|
| `e003_support.py` | Shared helpers and reference maths (exact binomial, Newcombe, card draw). Its docstring lists all interfaces. | n/a |
| `test_ac01_change_texts.py` | AC1: C1 to C3 files exactly as frozen, word counts 35/11/64, role files and playbooks unchanged since f4298cd. | 8/8 pass |
| `test_ac02_pair_start.py` | AC2: both arms, fresh copies, briefs differ only by the change paragraph and copy path, same model, same hour, within 7 days; no record means not eligible. | fail, `pair.py` missing |
| `test_ac03_pair_audit.py` | AC3: in-flight inputs, foreign commit taken in, context differs, leak, one rerun then leave out, never rerun for a better answer. | fail, `pair.py`, `transcript_check.py` missing |
| `test_ac04_heldback_gate.py` | AC4: `kind.py can-open` gate. | 8 gate tests fail; 4 repository tests pass |
| `test_ac05_judging.py` | AC5: verdict-line rules, one follow-up then at most one new session, arm outcome (judge PASS and locked checks exit 0), judge model differs from doers', brief carries no arm label, hand-back or commit messages, and the transcript check (outside reads, web, sheets repository). | fail, `judge.py`, `transcript_check.py` missing |
| `test_ac06_owner_cards.py` | AC6: 8 cards at 4/2/2, seeded draw against an independent reference, shortfall rule, locked-check failures never drawn, extension to 6 answered or 12 shown, rescoring, disagreements. | fail, `cards.py` missing |
| `test_ac07_decision.py` | AC7: exact one-sided test at 1 in 40, judge confirmation (6 answered, at most 2 disagreements), gain with 95% range, fewer than 10 pairs, the false-pass guard (change's false passes at most the unchanged check's plus one). | 1 passes (spec anchors), 11 fail, `analyse.py` missing |
| `test_ac08_counts_card.py` | AC8: caps 133/132, 133/66, totals 266/200 (and the 40 and 100 sizes), start limits, due at every 20 runs and every 16 weeks, card contents, power from `sizing.py`, weeks to target, no outcome, ruling recorded. | fail, `counts.py` missing |
| `test_ac09_model_change.py` | AC9: group by model, test the larger group only, say so; arms on different served models are a set-up fault. | fail, `analyse.py` missing |
| `test_ac10_v2_record.py` | AC10: V2 cutoffs 5/13/18 of 30, and the record carries the V2 measure, how pieces are counted and the removal test. | 1 passes (cutoff arithmetic), 4 fail |
| `test_ac11_removal.py` | AC11: apply then remove is byte for byte (CRLF, no trailing newline, unicode, a role file); per-pair clean-removal check. | fail, `change.py` missing |
| `test_j1_change_to_arm.py` | J1 insertion position, C1 and C2 fills, every awkward case. | fail, `change.py` missing |
| `test_j2_dispatch_record.py` | J2 entry from brief records and control files, awkward cases, 7-day boundary. | fail, `pair.py` missing |
| `test_j3_neutral_export.py` | J3 two-commit bundle, neutral fields, trees equal, no other object reachable, fill file, INDEX hashes, `last`, tamper refused, reader list. | fail, `export.py` missing |
| `test_j4_sheet_route.py` | J4 block parser (three forms plus refusals) and fill script (SHA gate, determinism, writes nothing else). | fail, `block.py`, `fill_judge_brief.py` missing |
| `test_j5_verdict_record.py` | J5 verdict-line, counts-block and closing-block forms, test numbers, label and path checks. | fail, `verdicts.py` missing |
| `test_j6_cards_record.py` | J6 cards file, sheet-text and arm-label absence, quotation replaced by test number. | fail, `cards.py` missing |
| `test_j7_analysis_pack.py` | J7 entry, validator and manifest checks, with synthetic good and broken manifests. | 12 pass, 1 skip |
| `test_j8_holdout_pack.py` | J8 entry, the extract's withheld paths, change ids, "arm" and change sentences, validator. | 15 pass, 1 skip |

The two skips are the checks on a recorded manifest in `docs/briefs/`. None exists until a blind or analysis dispatch records one. Run them before each dispatch with `S001_MANIFEST=<brief record> python3 -m unittest discover -s tests/acceptance -p 'test_j8*.py'` (or `test_j7*`).

Every failure I could inspect says "interface missing" and nothing else. I also ran the J3, J4-parser and J5 tests against throwaway scripts kept outside the repo and not committed. All of those tests passed. Two deliberately broken exporters (no fixed date, wrong label message) each failed the J3 test. A fixture bug I found this way, a mixed-forms case that was actually a valid stopped block, is fixed. The other interface tests have not been run against any implementation, so a fixture bug could still sit in them.

### 2. Interfaces named (all invented only as far as a test needs)
The scripts are `python3 -I src/E-003/<name>.py <subcommand>`, run from the repository root:

- `change.py` with `apply`, `remove`, `verify-removal`, `fill-c1`, `fill-c2`.
- `pair.py` with `entry`, `plan --no-run`, `audit`, `context-compare`, `rerun-decision`, `locked-checks`.
- `transcript_check.py check` prints `clean`, or `leak@<line>` with exit 1.
- `fill_judge_brief.py`, `export.py`, `block.py parse`, `verdicts.py check`, `judge.py`, `cards.py`, `analyse.py` with `run` and `v2`, `counts.py`, `kind.py can-open`.

Conventions:
- A decision command prints one JSON object and exits 0, even for a negative decision.
- A refusal exits 1.
- A usage error exits 2.

The full list, with arguments and output keys, is in the docstring at the top of `e003_support.py`, and each test file repeats the part it uses.

### 3. Contradictions and gaps in the spec
1. **No file names or command lines for the Builder's scripts.** The fill script, transcript check, export reader, block parser and the rest are named but not located. The names above are mine.
2. **J4, `k1-canary` in the full form.** One sentence lets it be `unseen`, `seen` or `unread`; another says "in the full form it is `unseen`". I test `unseen` in the full form and the three words in the stopped and void forms.
3. **J4, "writes nothing but the J5 line".** The fill script cannot know most J5 fields. I read it as: the only file created is `--out`, and stdout holds no sheet text.
4. **J5, closing block layout.** The separators between the counts block, the verdict file and `sha256:` are not given. I assume plain concatenation. "Tokens, tool uses, seconds" are read as integers.
5. **J1.**
   - The spec does not say how the "task statement" is found in a brief, so `apply` takes it as a file.
   - It does not say how a cited stage's line range is derived. I assume the heading to the next same-or-higher heading.
6. **J2.**
   - The layout of a Service Desk control file "holding several roles" is not given. I use a JSON list of entries.
   - The two-lane case needs a record format the spec does not give, so it is not tested.
7. **J3.**
   - The neutral author and the fixed date are not named. I require only that they are the same in both commits and in every export, and differ from the source's.
   - The `.fill.json` keys are not given. I check that the values appear.
   - The "no deliverable, so no export" case is not tested.
8. **AC6.** Two details are my reading:
   - How a shortfall is added to the 4/2/2 sample sizes.
   - "Further cards via `choice` in the order G1, G3, G2", read as the first non-empty leftover group in that order.
9. **AC5.**
   - The spec does not say whether the new judge session gets its own follow-up. I test only that a third session never starts.
   - The invocation of a project's locked checks is not given, so `pair.py locked-checks` takes the command as an argument.
   - E-001's allowed system paths (F4) are in `src/**`, which I may not read. The transcript tests therefore cover only clearly inside and clearly outside paths.
10. **J7 and J8.** The spec says the manifest is recorded "in the dispatch's brief record" but not which field says which pack it is for. I tell the two apart by the agent file (`check-author.md` or `reviewer.md`).
11. **AC10.** "How those pieces are counted from the review records" has no content defined. I ask only that the record name the review records and say what counts as first time.
12. **AC2.** "Records the pair" has no location, so I test only the returned arms.
13. **Local false failure.** `surface_guard diff origin/main..HEAD` in `check_all` reports earlier chief-of-staff and orchestrator commits as not by check-author (see section 6).

### 4. Which tests can pass without the Builder
They pass now: AC1 (all 8), J7 (12), J8 (15), AC4's four repository and record tests, the spec-anchor test in AC7, and the cutoff-arithmetic test in AC10. Everything else needs `src/E-003/` and fails until the Builder writes it.

### 5. `check_all.sh` summary
Run in the worktree after committing, as `bash governance/checks/check_all.sh . origin/main`. The summary is all PASS, including `v3_checks joins`, except two lines:
- `record_checks merges`, the known false failure (LL-29).
- `surface_guard diff --range origin/main..HEAD`, which lists the earlier chief-of-staff and orchestrator commits as not check-author. That is a property of comparing against `origin/main`, not of my commit.

### 6. Surface guard
`python3 governance/checks/surface_guard.py diff --range 7d6c999..build/check-author/s001-locked --branch build/check-author/s001-locked` printed `OK: 1 commit(s) in 7d6c999..build/check-author/s001-locked checked (0 merge(s) skipped, 0 exempt, 0 human)` and exited 0.

Not pushed.
