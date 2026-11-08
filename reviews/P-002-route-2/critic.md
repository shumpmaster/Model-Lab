Verdict: FAIL

*The Critic on the re-made route card questions/P-002-route.md and the sizing record it rests on, intake/P-002-upgrade-footprint-2026-11-08.md, made at the owner's ruling "Size it first (Recommended)" (questions/P-002-route-stop.md). Each round is a fresh session on a different model from the card's writer, started by the Chief of Staff (session_01QBwHGNSLmSrYQgS6BPjV8p), and its return is recorded verbatim, its own verdict line as "The round's verdict was …" (LL-68). The verdict above is the latest round's.*

## Round 1 (uncommitted draft)

The round's verdict was FAIL.

The card is well formed and fairly put. It fails because the sizing record it rests on has factual errors, one of them in exactly the area the three earlier failures were about, which is the reach on the prompt engine's tests. The conclusion ("no test result changes") may still hold, because it rests on the trial run. But the record cannot be cited as it stands, and the fixes are small. After they are made, the card needs one more check.

**What I could and could not check**
- I have no shell, so I could not repeat the trial's test runs or `check_all.sh`. I could not read git history either, so I could not verify the commit hashes (3a2606a, b18259c, a1706c2, a30fdc0) or "main changes nothing under tools/ after b18259c".
- Method: the record states the commands, the scratch worktree, the base commit and the before/after comparison plainly enough that a second person could repeat them. Three gaps:
  - It does not give the Python version.
  - It does not say where the before and after outputs are kept, so "every test's result the same" cannot be re-read.
  - It does not say how PACKS.toml and SURFACES.md were merged beyond "applied cleanly".
- Checked and consistent with the record:
  - The six scripts. Model-Lab and the model's tools/ have the same line counts except v3_checks, orchestrator, session_runner, governance_checks and orchestrator_git. govlib is the same length, which fits "one comment".
  - The four agent files. critic, builder, definer and researcher carry the new S-035 wording in the model's template and not in Model-Lab.
  - The workflow. The model's orchestrator.yml adds ` --check-tree` on the tree untar line only (line 326).
  - SETUP.md, requests/README.md and SURFACES.md differ in length by 1, 1 and 2 lines. All three are listed.
  - docs/projects/ does not exist in Model-Lab. docs/PROJECT.md is said to be left unchanged.
  - Model-Lab has no design images today.
- Context sources I opened:
  - Supported: lines 17, 18, 19, 21, 23, 25 and 26 of the card, and LL-16 (status open).
  - Supported with a note: line 20, subject to findings 1 to 3 below.
  - Line 24 (the owner's answer "Size it first (Recommended)") has no answer record yet. The card says so itself, so I could not verify the quote.

**Findings**

1. **BLOCKING.** The record, "What reaches the prompt engine", first bullet, says the tests "load only `govlib.glob_match` and `session_runner.norm`". Its second bullet says they "read only its own pack roles". Both are incomplete.
   - `tests/acceptance/test_ac11_removal.py:86` reads the live `.claude/agents/critic.md`. The upgrade changes that file.
   - `tests/acceptance/test_ac01_change_texts.py:72-84` walks every file in `.claude/agents` and `docs/playbooks`, looking for four phrases.
   - `e003_support.py:130-135` imports whole modules (session_runner.py, govlib.py), not just two functions.
   - Why it matters: the card's main reassurance is "nothing of the prompt engine's tests is reached". The files the record lists as unreached are only the ones named. The trial's identical results suggest no break. But the record, and the owner who rests on it, would repeat the understating that sank the earlier cards. The record needs to name these two tests and the files they read. It should also say why the new agent-file lines cannot collide (I saw no collision).

2. **BLOCKING.** The record, "In plain words", says "changes 21 files and adds two". Its own table lists 19 changed files and 2 added: 6 scripts, 4 agents, 1 workflow, 5 docs and briefs, PACKS, SURFACES and the version file, with PROJECT.md not changed. Either the count or the table is wrong. A footprint record whose headline number does not match its table cannot be trusted by the owner or the Reviewer.

3. **BLOCKING.** The record's PACKS row says "docs/projects lines in eight standard roles". The model's current PACKS.toml has docs/projects entries in nine roles: input-reader, researcher, definer, critic, reviewer, source-checker, builder, critic-gate and user-rep. Model-Lab's PACKS.toml has none of them, and its reviewer line (line 53) lacks the entry. This is a second miscount of the same kind, on a governance file that the Reviewer will diff.

4. **Non-blocking, to fix at the same time.** Card line 11 says "the two cases that differ are absent from the prompt engine's work today". The record only says "neither appeared in the trial". I confirmed from the files that Model-Lab has no design images and no `sprints: PR #n` line in docs/PROJECT.md. The record should say it checked this.
   - The cut-short-history case is the normal state of every check run, because the check run's copy is a one-commit copy (CHANGELOG 3.7.2).
   - The card should say that the "sprint was merged" test will begin to note, not fail, as soon as the prompt engine records its first sprint line. This is a weaker check, not an equal one.
   - Today's wording ("absent today") can mislead the owner into reading it as a permanent absence.

5. **Non-blocking.** Card line 22 says screening work filed before the upgrade "could count in the prompt engine's records". The 3.7.2 `v3_checks.py` keeps the same time-based matching (model tools lines 1042, 1165-1196). The card does not say whether the upgrade removes that risk. It does not, so the risk applies after the upgrade too, until the screening has its own plan. A plain reader will take the fact as an argument for upgrading first. State that the upgrade does not remove it, or drop the line.

6. **Non-blocking.** Card line 5 is the plain-English paragraph. The form in AGENTS.md §4 says it starts with anything that failed or was skipped. The previous card's three failures appear only in line 12. The paragraph also lists "scripts, agent files, a folder" and omits the workflow line, the pack and brief lists, the surface map, and the setup, gate and profile forms. The BLAST RADIUS on line 13 also omits the surface map, setup guide, gate form, profile form and version file. Given this card's history, list the whole footprint, or say plainly "21 files; the full list is in the record".

7. **Non-blocking.** Line 14 sets DEFAULT and TIMEOUT to "none". The template asks for a letter and hours, and AGENTS.md §5 says reversible questions adopt the recommendation at timeout. The card explains the deviation ("starting a project is yours to rule"), and the earlier stop card did the same. I accept it as a deliberate, stated choice.

8. **Non-blocking.** Options are fairly put: A and B both state gain, cost and reversibility, the recommendation carries a confidence level and a "what would change it", and it is not presented as the only reasonable choice. Two plain-English points:
   - "Landing" and "main line" are used without a one-line explanation in the title and paragraph.
   - B's cost ("no date") is accurate. The card could add that the date depends on a task that is still to be created (line 25 of the card says so).

9. **Non-blocking.** Line 24 cites an answer record that does not exist yet. The card says "its answer record follows once that question is on main", and that is honest. The owner's quoted words cannot be checked until that record exists.

**Re-check route:** correct findings 1 to 3 in the sizing record. The card then needs a second round, with findings 4 to 6 reworded at the same time.

Files read:
- /home/user/Model-Lab/questions/P-002-route.md
- /home/user/Model-Lab/intake/P-002-upgrade-footprint-2026-11-08.md
- /home/user/Model-Lab/tests/acceptance/test_ac11_removal.py
- /home/user/Model-Lab/tests/acceptance/test_ac01_change_texts.py
- /home/user/Model-Lab/tests/acceptance/e003_support.py
- /home/user/Model-Lab/governance/PACKS.toml
- /home/user/Personal-Org-Operating-Model/template-v3/governance/PACKS.toml
- /home/user/Personal-Org-Operating-Model/CHANGELOG.md

## Round 2 (uncommitted draft)

The round's verdict was FAIL (round 2). The three round-1 defects are mostly fixed: the file and role counts now match, the missing tests are named, and the opening leads with the failure and the whole footprint. I found two new blocking gaps in what the card says the upgrade reaches. I cannot run anything. For the reasons in findings 8 and 9, the trial itself cannot be repeated.

**What I confirmed against the files**
- **File counts.** The table holds 21 files: 19 changed and 2 added.
  - Six scripts under governance/checks have no counterpart in the Model-Lab copy of the new features (the S-035 to S-037 and cut-short-history markers). Model-Lab has none of them; tools/ has them in all six: orchestrator.py, v3_checks.py, session_runner.py, governance_checks.py, orchestrator_git.py, govlib.py.
  - Four agent files each carry one new S-035 line in template-v3 (definer, researcher, builder, critic). The Model-Lab copies have none.
  - orchestrator.yml: only the `--check-tree` flag on the tree untar line differs.
  - The other changed forms, BRIEFS.toml, SURFACES.md, PACKS.toml, SETUP.md, _GATE.md, _PROFILE.md and intake/requests/README.md, each carry the S-035 plan-of-its-own text in template-v3. Model-Lab has none of it.
  - docs/projects/ is absent in Model-Lab and present in template-v3 with two files. The version file reads 3.6.0 and the model is 3.7.2.
- **Pack roles.** Exactly nine roles in template-v3 PACKS.toml gain docs/projects lines: input-reader, researcher, definer, critic, reviewer, source-checker, builder, critic-gate, user-rep. This matches the record. S-001-analysis and S-001-holdout are Model-Lab's own and are not in the model.
- **Named tests.**
  - e003_support.py lines 116-135 and 343-345 load govlib and session_runner and use `glob_match` and `norm`. Line 339 reads PACKS.toml.
  - test_ac01 lines 72-84 and test_ac11 line 86 read the agent files as the record says.
  - I grepped all of tests/ for governance/checks, v3_checks, orchestrator, check_all, SURFACES, BRIEFS, SETUP, _GATE, _PROFILE, the version file and the workflows. I found no other test that reads a changed file, so the test inventory is now complete.
- **Cited sources.**
  - v3_checks.py:849-854 and 959-1010 do match research by position. `match` takes the latest Discovery run starting at or before the line, across every item.
  - LL-16 is open.
  - The risk-paths R3 rule covers governance/**.
  - The IDEAS 11-08 entry and the P-001-work-repo ruling exist.
  - docs/PROJECT.md has no real `sprints:` line; its only matches are instruction text.
  - docs/design holds no images.
  - The weekly-landing task is "still to be created", as the handoff says.

**Findings**

1. **Blocking. Card line 5 and BLAST RADIUS (line 13); record "What reaches the prompt engine" (lines 29-36).** Both say the upgrade leaves the prompt engine's "experiments" untouched, and that only tests read the changed files. The experiment itself reads a changed file.
   - experiments/E-003.md line 31 defines the "existing check standard" as Model-Lab's copy of .claude/agents/critic.md, with reviewer.md, source-checker.md and the playbook.
   - The held-back pack S-001-holdout reads critic.md, so the upgrade edits a file the blind dispatch reads.
   - specs/S-001.md line 295 freezes the pack total at "50,540 bytes", measured with `wc -c` over critic.md and the other pack files. The upgrade changes that total.
   - specs/S-001.md line 300 records the three role files as "the same in both [repositories] but for one word (critic.md:31)". The upgrade also breaks that sameness.
   - No test catches either figure.
   - Why it matters to the owner: the card tells the owner the experiment is unaffected, but a change under test, or its frozen record, may be shifted by a merge they are told is harmless.
   - The record must say whether any E-003 run or blind dispatch has started, what base commit it was pinned to, and whether the frozen figures need a superseding entry. The card must then say so.

2. **Blocking. Card line 22 and Option A; record lines 38-39.** The research-matching risk is stated in one direction only, and it is not in the options.
   - The card says screening work could count in the prompt engine's records.
   - The same matching works the other way. Because `match` takes the latest Discovery run starting at or before a line, any prompt-engine groundwork research dispatched after the screening's Discovery run begins would match the screening's run, and it could count toward the screening's Discovery-3.
   - Round 1 asked that the card say the upgrade does not remove this risk. It now appears only in a Context bullet.
   - The ordering rule (file the screening before any of its research) and the reverse exposure belong in Option A's Cost.

3. **Non-blocking. Option A's cost (line 9).** This is mostly met. The "sprint was merged" test becoming a note is now stated, along with "a slightly weaker check run, not an equal one".
   - It does not say who then catches a bad sprint line (the pull request's own checks run on full history, per CHANGELOG 3.7.2).
   - The words "check run" and "pull request's own checks" are never told apart for a non-expert.

4. **Non-blocking. Card line 5.** The list of changed files names 20 of the 21. intake/requests/README.md is not mentioned, and the list does not say which items are the "two forms". The count of 21 is correct. The record's table has the complete list.

5. **Non-blocking. Card line 24 (Context).** It cites the owner's "Size it first (Recommended)" ruling to questions/P-002-route-stop.md, but that file is the question, not the answer.
   - There is no decisions/questions/P-002-route-stop.md yet, and the card says the answer record "follows once that question is on main".
   - The claim therefore has no supporting record at this moment, which is the Every-ask-is-filed rule (S-033). The answer should be filed before the card is put.

6. **Non-blocking. Card lines 5 and 20.** "Every rule check gave the same result" is slightly loose. The record says check_all output differed in "509 file(s)" becoming "511 file(s)", and that the surface guard refused the trial's single commit. The card does not tell the owner the upgrade is two commits in one pull request. It says "one pull request", which is true.

7. **Non-blocking. Recommendation (line 11).** Confidence "medium-high" and the stated change conditions are fair, and the options are fairly put. Once findings 1 and 2 are fixed, this line needs re-checking, because "the two cases that differ do not arise" is no longer the whole list of differences.

8. **Non-blocking. Record lines 13 and 33. Method.** The commands are stated well enough to repeat. These are the gaps:
   - The temp-folder-name replacement rule is not given.
   - The sort and hash command is not given.
   - The "per-test list" format is not given.
   - A repeater can compare before and after test by test but cannot reproduce the hashes 2645a119… and 72fbbaf0….
   - Please state the exact command and normalisation, or say the hashes are not meant to be reproduced.

9. **Non-blocking. Record line 8.** The summary sentence says "the surface map counts two more files", but line 34 says the two extra files are the new docs/projects files counted by check_all. The wording should match.
