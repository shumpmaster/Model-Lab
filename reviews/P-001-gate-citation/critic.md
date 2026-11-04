# The Critic on questions/P-001-gate-citation.md, verbatim

*Brief 48 (docs/briefs/48-critic.md, on the default branch once the design pull request merges); a fresh session on a different model from the card's writer. Recorded verbatim by the Orchestrator, 2026-11-04.*

## Round 1 (commit 15e5fae)

Verdict: FAIL

I read the card cold and checked it against the code and records it cites. Most of its claims about the check hold. The card still leaves out two consequences of option A, and it overstates what option B proves. The fixes are small.

Findings

1. BLOCKING. Option A leaves out what a red run on the default branch does.
   - The card says the check "runs red again on the default branch" and that this teaches everyone to read past red. It does not say that the Orchestrator loop reacts to that red run.
   - The header of .github/workflows/governance.yml says the decide job of orchestrator.yml reads these runs. While the latest run on the default tip is failed, running or absent, the loop starts no session and merges nothing.
   - orchestrator.yml runs on a 30-minute schedule in this repository. governance/checks/orchestrator_git.py documents the hold: decisions apply, nothing is dispatched, and a hold of over 60 minutes on one tip raises a "ci-hold" card in queue/.
   - SURFACES.md line 15 and asks-merge.yml say merges happen only after every check has passed.
   - So "you would merge past a red check" understates the cost. The merged red freezes the loop until a later green run, and every later change to the case turns it red again.
   - This is a consequence the owner needs when choosing between A and B (LL-46, LL-50). The card should either state it or say it checked that the loop does not apply here.

2. BLOCKING. Option A is described as "red on the citation lines", but A as written also fails the word limit, which cannot be fixed.
   - A has the case quote the criteria, power figures and options.
   - case_problems (v3_checks.py, WORD_LIMIT = 350) caps sections 1 to 8 at 350 counted words.
   - The gate Critic counted about 320 words in the current case (reviews/P-001/_build-gate-1-critic.md line 32).
   - Eleven criteria, quoted whole from specs/S-001.md lines 250-260, run to several hundred words. A therefore adds a second red, "sections 1 to 8 hold N counted words", which no citation fix removes.
   - The card's cost for A should say so, or A should be redefined as a pointer-only case. A pointer-only case would not meet the Critic's finding that the case shows no criteria.

3. NON-BLOCKING, needs rewording. Option B proves less than the card says.
   - "The criteria you see are proven to be the plan's own words" holds only for the proposal's section 3 lines. For those, proposal_problems tests `words in specline`, which is a substring test. A truncated criterion would pass, so the check proves the words are in the plan's line, not that each criterion is quoted whole.
   - The case itself is not word-checked. The case check (cited_ok and the line-count test at v3_checks.py lines 2646-2656) only confirms that the cited file and line exist. So the owner sees the criteria in the proposal, not in the case, and must open it.
   - The case cannot hold the criteria itself within the word limit (finding 2). The card should say that the owner reads the criteria in the proposal file.

4. NON-BLOCKING. B does not say how the other two missing things reach the owner.
   - The opening names three gaps: the criteria, the budget options, and the open questions. It also names too few risks.
   - B settles only the criteria and the run and week totals. The nine open questions (specs/S-001.md lines 333-348) and the options A to D are not placed anywhere.
   - plan.md:253-256 and :960 are citable and could carry them. The card should say where they go, so the owner does not think B fixes the whole Critic finding.

5. NON-BLOCKING. Option C's gain overstates an unwritten change.
   - "It would also let the checks open this project's plan" is a claim about a spec that does not exist. The earlier ruling is about the checks seeing recorded rulings.
   - Whether the change would fill {spec} is not shown by any record. Say "is meant to" or drop the claim.

6. NON-BLOCKING. Wording for a cold reader.
   - "the reading lists" appears in the opening with no explanation.
   - "the plan" is used for two things. It means the spec in the criteria sentences ("its line in the plan"), and the plan's review in other places ("the plan's review").
   - "conversation-run", "status record" and "pipeline's script" are jargon in the first paragraph.
   - The opening does lead with what failed and has no ids or paths. The paths are in the WHY and Context lines, which is fine.

7. NON-BLOCKING. Two Context claims I could not verify from the records I was given.
   - "The only red check on PR #44 today is review_check pr 44" cites a CI run, not a file. Give a link or the run id.
   - I did not confirm from origin/main that no spec exists for the operating-model change. The working tree has no specs/S-035*. I checked only the working tree and could not run git. The LEDGER lines L-0150 and L-0151 are consistent with "stopped twice".

Verified and true
- citable_paths builds the pack from status/<item>.toml's `spec`. This project has no status file, so `{spec}` is None. `_fill` drops the `specs/{spec}.md` and `reviews/{spec}/**` patterns.
- `reviews/**` and `docs/gates/{item}/**` stay in the pack, so a case can cite the plan's review and a proposal file.
- The refusal message "not one the Critic's gate pack holds" is the real text (v3_checks.py line 2802 for proposals, line 2649 for cases).
- Proposal scenario lines are checked against `specs/<spec>.md:<line>` word for word, and the `spec` match is skipped when spec is None. They are not held to the pack rule, and sections 1, 2 and 5 are (PROPOSAL_COUNTED).
- A proposal is not seen as a user-representative step here. orchestrator.py `has_profile` and `user_step` need docs/users/PROFILE.md, which this project lacks. PROJECT.md section 9 says "The owner is the user."
- SURFACES.md line 88 puts `*-proposal.md` in the Chief of Staff's lane.
- The push trigger on main, and the check_all.sh call to `v3_checks gates --base`, confirm that a merged case is re-checked on the default branch. The claim that later changes to the case turn red holds.
- LL-29, LL-42 and LL-48 are about pushing after a red check, so they fit the A cost loosely.
- The gate Critic's finding 1 (reviews/P-001/_build-gate-1-critic.md) supports the claim that the case shows no scenarios. The same record shows the case lacks budget options, open questions and several risks.

Fairness, earlier rulings and the form
- The three options each give gain, cost and reversibility. B's recommendation is argued from checks, not from the owner's leaning.
- None of the options goes against the earlier gate-record ruling (decisions/questions/P-001-gate-record.md, "Ruling: A"). The card says the operating-model change stays owed under every option.
- Risk class R0, "reversible", default B and a 72-hour timeout are acceptable. A and C would hold or redden the gate, so B is the safe default.
- The blast radius should add, under A, "the Orchestrator loop on the default branch" (finding 1).

The six-part contract
1. What I changed: nothing. I am read-only and wrote no file.
2. Why: the brief asked for a cold read of questions/P-001-gate-citation.md, checked against the code and records it cites.
3. What I verified: v3_checks.py (check_gates, citable_paths, case_problems, proposal_problems, the regexes and limits), PACKS.toml critic-gate, orchestrator.py (has_profile, user_step, load_statuses), governance.yml, check_all.sh, orchestrator.yml and orchestrator_git.py headers, SURFACES.md, status/README.md, PROJECT.md section 9, the gate Critic record, the gate-record ruling, LESSONS LL-29, 42, 46, 48, 49 and 50, OPERATING_MODEL §2, and LEDGER L-0150 and L-0151. I did not run `v3_checks gates`.
4. What is undone: I did not run the gates check in a scratch copy. I did not read reviews/S-001/plan.md or the Critic's earlier rounds beyond the gate Critic's quotations. I did not confirm PR #44's run, GitHub's merge settings, or the S-035 spec on origin/main.
5. Needed outside my lane: the Chief of Staff, to redraft the card for findings 1 and 2 (blocking) and 3 to 7. A fresh Critic should check the redraft.
6. Open questions: does the loop's ci-hold apply to this project? Does the owner want the case to carry the criteria at all, given the 350-word limit? That limit pushes the owner to the proposal file under B.

Files:
- /home/user/ml-ask/questions/P-001-gate-citation.md
- /home/user/ml-ask/governance/checks/v3_checks.py
- /home/user/ml-ask/.github/workflows/governance.yml
- /home/user/ml-ask/governance/checks/orchestrator_git.py
- /home/user/Model-Lab/reviews/P-001/_build-gate-1-critic.md

## Round 2 (commit 10d5a11; brief 50, a fresh session)

Verdict: PASS

I read questions/P-001-gate-citation.md (commit 10d5a11) cold and checked it against the code and records you named. Round 1's findings 1 to 7 are all resolved, and I found no blocking error. The two Context lines that cite GitHub Actions run links (#43 merge run 41877228609 and PR #44 run 41878559060) I could not open. I judged them only as stated: the card says the loop stopped for want of a token setting, and that only the review check is red on PR #44. The code is consistent with both. I had no shell, so I could not run `git ls-tree origin/main specs/` or `v3_checks gates`.

Round 1 findings, one by one
1. Resolved (it was blocking).
   - Option A now says a red run on the default branch holds the loop, which starts nothing and merges nothing.
   - It says a CI-hold card follows after an hour. orchestrator_git.py `hold_card` fires when HOLD_MINUTES (60) is passed on one tip, and `runs_state` treats anything but a completed success as not green.
   - It says the loop does not run here today. orchestrator.yml's decide job runs `token-mode` first, and `token-mode` refuses when TOKEN_ENVIRONMENT is unset (orchestrator_git.py `TOKEN_UNSET`). That matches the card's account of the #43 run.
   - The card does not claim the red lasts for ever. Only a changed case is re-checked from the base, and the card says "every later change to the case".
2. Resolved (it was blocking).
   - The 350-word cap is now stated under every option. WORD_LIMIT is 350 (v3_checks.py line 2447, enforced at line 2679).
   - The "about 320" figure comes from the gate Critic's estimate (reviews/P-001/_build-gate-1-critic.md line 32).
   - Eleven criteria is right: AC1 to AC11 are at specs/S-001.md lines 250 to 260, each a long line, so they cannot fit in the headroom.
3. Resolved.
   - B now says the owner reads the criteria in the proposal file, not in the case.
   - B says the check cannot catch a cut-short criterion. That is correct: the check is a substring test, `sm.group("words") not in specline` (line 2837).
4. Resolved. The card says that under every option the budget totals are cited from the plan review and the open questions go on the terms card, which exists and lists the nine questions (questions/P-001-build-gate-terms.md).
5. Resolved. C now says "meant to" and "no spec yet says so". The LL-44 correction line (docs/LESSONS.md line 365) shows the intent but not a spec.
6. Resolved. "Reading lists" is gone. "The plan" and "the review of the plan" are kept apart. The opening leads with what failed and holds no ids or paths. It is dense but readable.
7. Resolved as far as I can judge. The PR #44 claim now has a run link, which I could not open. On no spec on the operating model's default branch:
   - The working tree has no S-035 or any spec beyond S-034, and no spec for this change.
   - L-0150 and L-0151 show the open plan, S-035, stopped twice.
   - I could not run the origin/main listing myself.

Findings on the redraft
1. NON-BLOCKING. Option B says "the Critic would check" that each criterion is copied whole, but the gate Critic's pack cannot do this.
   - citable_paths drops `specs/{spec}.md` here because there is no status record, so the spec is not in the pack.
   - Round 1's gate Critic read specs/S-001.md only "as allowed" by its brief, and marked what rested on it "spec only".
   - The claim is true only if the Critic's brief lets it read the spec, as before. The card should say so, or say the Orchestrator checks the copy.
2. NON-BLOCKING. The cost under A says a known red "teaches everyone to read past red (lessons 29, 42, 48)".
   - Those lessons record pushes made beside a red local check, not merges past a red PR check. They fit loosely.
   - Say "as in lessons 29, 42 and 48" or drop the word "teaches".
3. NON-BLOCKING. A's "it stops at its first step" is loose. The token-mode step is the third step of the decide job, after checkout, but it is the first that does any work. I could not verify the run itself. Say "at its token check" if the run log says so.
4. NON-BLOCKING. The Milestone line says Design-6. Its text is "the plan changes the model's own rules and must pass review before anything is built". The card is about the Build gate case, so the link is loose. Round 1 did not raise it. The Orchestrator may know why it was chosen.
5. NON-BLOCKING. The Context line on lessons 29, 42 and 48 is not cited. The lessons are in docs/LESSONS.md, so add that file as the source for the A cost.

Checked and true
- Every claim about what a check, the pipeline's script or the loop does traces to code and holds:
  - the refusal text "not one the Critic's gate pack holds" (v3_checks.py lines 2649 and 2802);
  - the pack: `docs/gates/{item}/**` and `reviews/**` stay in, and `specs/{spec}.md` goes when the spec is None (citable_paths and PACKS.toml critic-gate);
  - proposal scenario lines are checked against the spec line and are not held to the pack rule, while sections 1, 2 and 5 are (PROPOSAL_COUNTED, 200 words);
  - the script reads only status records and runs the user representative only with a profile (orchestrator.py `has_profile`, `user_step`, `case_written`), and PROJECT.md section 9 says "The owner is the user.";
  - the proposal file is in the Chief of Staff's lane (SURFACES.md line 88);
  - the push trigger on main and check_all.sh line 139 re-run `v3_checks gates --base`.
- The check that blocks a case or proposal "changed after the Critic was dispatched" cannot bite here. This project has no dispatch-log, so neither A nor B is affected.
- Options are fair. Each gives gain, cost and reversibility. The recommendation, B at medium confidence, is argued from the checks and gives what would change it. A's gain is called "the fastest" and B's costs are stated.
- No option goes against the earlier gate-record ruling. The card says the operating-model change stays owed under every option.
- Risk class R0, reversible, default B and the 72-hour timeout are acceptable. B is the safe default, and the blast radius names A's and C's extra effects.
- Nothing an option would cause is left out, apart from the small points above.

The six-part contract
1. What I changed: nothing. I am read-only and wrote no file.
2. Why: the brief asked for a cold read of the redraft and a check of round 1's findings 1 to 7 against the code and records.
3. What I verified: v3_checks.py (check_gates, citable_paths, case_problems, proposal_problems, WORD_LIMIT); PACKS.toml critic-gate; orchestrator.py (load_statuses, has_profile, user_step, case_written); orchestrator_git.py (token-mode, hold_card, runs_state, HOLD_MINUTES); orchestrator.yml and governance.yml headers and triggers; check_all.sh; SURFACES.md; status/README.md; PROJECT.md section 9 and the Design-6 line; the gate Critic's record; specs/S-001.md lines 248 to 260; LESSONS LL-29, 42, 43, 48; LEDGER L-0150 and L-0151; the terms card; and the gate-record ruling.
4. What is undone: I did not open the two GitHub run links. I did not run `v3_checks gates` or `git ls-tree origin/main specs/`, because I had no shell. I did not confirm GitHub's merge settings, which the card says it cannot read either. I did not re-read reviews/S-001/plan.md for the power figures beyond the lines the grep returned, which agree with "one size of one kind". I did not read OPERATING_MODEL §2 and §4 again beyond the card's use of them.
5. Needed outside my lane: the Chief of Staff may fix non-blocking findings 1 to 5 in a small edit. None needs another Critic round.
6. Open questions: Does the gate Critic's brief for the next case name specs/S-001.md as readable, so B's "the Critic would check" holds? Is Design-6 the milestone the Orchestrator wants this card filed under?

Files: /home/user/ml-ask/questions/P-001-gate-citation.md; /home/user/ml-ask/reviews/P-001-gate-citation/critic.md; /home/user/ml-ask/governance/checks/v3_checks.py; /home/user/ml-ask/governance/checks/orchestrator_git.py; /home/user/ml-ask/.github/workflows/orchestrator.yml; /home/user/Model-Lab/reviews/P-001/_build-gate-1-critic.md; /home/user/Model-Lab/specs/S-001.md
