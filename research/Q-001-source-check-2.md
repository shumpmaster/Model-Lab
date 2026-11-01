Verdict: PASS

Every known (A/B) item I could test is confirmed, with the wording slips listed below. I wrote no files. I did not open /home/user/portfolio, /home/user/Model-Lab/decisions or any earlier source-check file. Every assumed item is unreachable: arxiv.org, psnet.ahrq.gov, pmc.ncbi.nlm.nih.gov, deepmind.google, hms.harvard.edu, www.fiercehealthcare.com, www.sup.org and awesomepapers.io all fail DNS (getaddrinfo ENOTFOUND). These hosts need to be allowed in the session's network settings. I did not upgrade any of them to known.

Wording slips (none changes a conclusion):
1. J1: critic.md:14 is 1,269 characters (1,272 bytes). The map says 1,272 characters. Line 18 is 1,957 either way.
2. J1 and the "Fixing after each failure" trap: the map calls the "before the project took model 3.4.0" exception "a rule dated to a later model version". The text confirms the exception and the "model 3.4.0" wording. The rulebook header is v3.0.0, so "later" is the map's inference, not a stated date.
3. C1: the map cites control record :54-55 for "the agent file's SHA-256". Only :54 is the agent file's hash. :55 is BRIEF.md's hash, and :56-57 hold two more file hashes.
4. A3: the Anthropic page says the model's ability to recall "decreases" as context grows. The map's "recall 'decreases' as the context window fills" is a fair paraphrase.

**Records (Personal-Org-Operating-Model and Service-Desk)**

| Item | Claim | Source | Result | Note |
|---|---|---|---|---|
| A2 | S-001.md is 22,883 lines | specs/S-001.md | confirmed | `wc -l` gives 22883. |
| A2, A7 | A plan review cites lines above 19,000 (r1:37) | reviews/M3B/_plan-review-r1-verbatim.md:37 | confirmed | Line 37 cites ":19203-19217". |
| A7, D3, I3 | Plan review ran to r14 with matching design r1-r14 | reviews/M3B/ | confirmed | _plan-review-r1…r14 and _plan-design-r1…r14 all exist. |
| D3 | r1 has five blocking findings (about :20-50); r14 passed (r14:7) | M3B r1, r14 | confirmed | B1-B5 sit at lines 20, 26, 33, 39, 45. r14:7 is `Verdict: PASS`. |
| B1 | builder.md:46-47 "First-pass review yield; defects found after delivery" | template-v3/.claude/agents/builder.md | confirmed | |
| B1 | definer.md:46-47 "Plan review first-pass rate" | definer.md | confirmed | |
| B1, I2 | reviewer.md:42-43 "Catch rate on seeded defects" | reviewer.md | confirmed | |
| B2 | Every rule is "an experiment with a target, a measure and a kill criterion" (OM:425-426); targets set "once real projects give a baseline" (:422-423) | OPERATING_MODEL.md | confirmed | The generalisation gate and rule of two are at :426 (J5). |
| B4, C1, F2, G4 | Control record: brief :3, CLI version :15, hashes :54-55, model :60 ("claude-sonnet-5-5"), source commit :168, limits :43-59 (50 turns, 30 minutes) | reviews/Q-001/_control/0-62b8dda7dcf2.json | confirmed | max_turns is :59 and session_minutes is :51. See slip 3 for :54-55. |
| B5 | OM:299 "No re-running for a better answer" | OPERATING_MODEL.md | confirmed | |
| C1 | Dispatch lines carry action, gate, item, role, route, spec, stage, time and trigger; outcome lines carry item, role, session, time, trigger, result, verdict and record; both carry prev | dispatch-log/2026-10.jsonl:5-15 | confirmed | |
| C1 | Searching "model" or "brief" in the dispatch log finds 0 matches | dispatch-log/2026-10.jsonl | confirmed | 0 matches, case-insensitive. |
| C2 | docs/briefs/README.md says "One file per builder dispatch … the record of what the agent was told"; the folder holds only the README | Service-Desk docs/briefs/ | confirmed | |
| C2, G1 | Chief of Staff session file records roles and times but no brief or model; tokens null on 10 of 15 helper lines (:2-16); reviewer sizes 56,509 to 213,771; `cost_usd_estimate: null` at :17 | sessions/chief-of-staff/session_012RJ…jsonl | confirmed | Lines 2-10 and 13 are null. Lines 11, 12, 14, 15 and 16 hold figures. |
| C3, I3 | S-001 named on 12 dispatch lines, all P-001, 2026-10-05 to 10-06 (:171-189); Triage dispatched after the third plan FAIL (:180-189) | dispatch-log/2026-10.jsonl | confirmed | 12 lines. Three critic FAIL verdicts, then critic-triage on route third-fail at :189. |
| C3 | Later M3B rounds (2026-10-26 to 10-29) are under reviews/ only | dispatch-log and reviews/M3B | confirmed | The log has 0 "M3B" matches and ends 2026-10-08. M3B r1 is dated 10-26 and r14 is dated 10-29. |
| C4 | OM:1 says v3.0.0; critic.md:14 says "model 3.4.0"; Service-Desk records 3.6.0 | OPERATING_MODEL.md; critic.md; governance/OPERATING_MODEL_VERSION | confirmed | |
| C5, H2 | BRIEFS.toml:2 "Changing this file is a rule change (R3)"; R3 changes are the owner's (OM:66); rule changes never delegable (:97-98) | BRIEFS.toml; OPERATING_MODEL.md | confirmed | OM:66 lists "R3 changes (tests, CI, the rules)". The "Never delegable: … rule changes" sentence runs across :97-98. The map's claim that it is unstated whether agent-file edits are R3 is not contradicted. |
| D1 | Checks differ by type (OM:311-316; critic.md:12) | OPERATING_MODEL.md; critic.md | confirmed | critic.md:12 includes "read every decision card cold". |
| D2 | Revise routes are one-line pointers (BRIEFS.toml:22, :28, :30); checker_return at :13 | BRIEFS.toml | confirmed | |
| D4 | Seven-part card; Critic reads it cold (OM:69-73) | OPERATING_MODEL.md | confirmed | |
| E1, E3 | BRIEFS.toml:17 ready-dispatch text; :1-2 no content copied; :9 "Work only from the files in this folder" | BRIEFS.toml | confirmed | The Service-Desk BRIEFS.toml is identical to the template's. |
| E1 | Free-text brief in the conversational path (specs/_TEMPLATE.md:34-37) | Service-Desk specs/_TEMPLATE.md | confirmed | |
| F2, J1 | Models named only by requirement (builder.md:44; OM:254) | builder.md; OPERATING_MODEL.md | confirmed | |
| F3 | Checker on a different model (OM:251-253) | OPERATING_MODEL.md | confirmed | |
| G3, H1 | Research sub-project cost limit is [open] (OM:96); sub-project budget and cap (:190-192); Discovery time limit [open] (:114); owner attention above speed and cost (:35-36) | OPERATING_MODEL.md | confirmed | |
| I2 | Hidden holdouts (OM:324-325) | OPERATING_MODEL.md | confirmed | |
| I3 | Stop rule, three plan rounds and three build rounds (OM:203-206) | OPERATING_MODEL.md | confirmed | |
| J1 | critic.md Duties :12-20 are long paragraphs; S-032 at :14 and :20; L-0119 at :31 | critic.md | confirmed | See slips 1 and 2. |
| L1 | 149 `_*verbatim*.md` files contain a column-0 `Verdict: FAIL`; naming varies; verdict rule at reviews/README.md:10-18 | Service-Desk reviews/ | confirmed | 333 verbatim files in total, 149 with that line. Name patterns include _plan-review-rN, _plan-review-roundN, _stage-…, _build-N…. README:10-18 gives the first-column-0 rule. |
| M1 | PACKS.toml:17-26 (Researcher excludes the hoped-for answer), :66-72 (Builder excludes holdouts); briefs hold ids only | template-v3/governance/PACKS.toml; BRIEFS.toml | confirmed | |
| M2 | Brief header treats handover text as data (BRIEFS.toml:9); untrusted text read only by the Input reader (OM:240-242) | BRIEFS.toml; OPERATING_MODEL.md | confirmed | |

**Web pages the Researcher opened (grade B)**

| Item | Claim | Source | Result | Note |
|---|---|---|---|---|
| B3 | Report standard errors, cluster them, compare paired differences, run power analysis (2024-11-19) | anthropic.com/research/statistical-approach-to-model-evals | confirmed | Date November 19, 2024. All four recommendations are present. |
| B3 | "model outputs vary between runs", so run multiple trials (2026-01-09) | anthropic.com/engineering/demystifying-evals-for-ai-agents | confirmed | Date January 9, 2026. |
| B6 | "You won't know if your graders are working well unless you read the transcripts" | demystifying-evals | confirmed | The sentence continues "and grades from many trials". |
| B7 | Grade the outcome produced rather than the path taken (paraphrase) | demystifying-evals | confirmed | |
| F4 | "Evals also shape how quickly you can adopt new models" | demystifying-evals | confirmed | |
| A3 | Recall "decreases" as context fills; context is "a finite resource" (2025-09-29) | anthropic.com/engineering/effective-context-engineering-for-ai-agents | confirmed | Date September 29, 2025. The page says "must be treated as a finite resource with diminishing marginal returns". |
| J1 | Guidance against "a laundry list of edge cases" | effective-context-engineering | confirmed | |

I read the page text only as data.

**Assumed (reported, not opened): every one unreachable**

| Item | Source | Result |
|---|---|---|
| A4 | https://arxiv.org/abs/2310.11324 | unreachable (arxiv.org DNS failure) |
| A5 | https://arxiv.org/abs/2507.11538 | unreachable (arxiv.org DNS failure) |
| A6 | https://arxiv.org/abs/2503.13657 | unreachable (arxiv.org DNS failure) |
| I4 | https://arxiv.org/abs/2404.13076 | unreachable (arxiv.org DNS failure) |
| F1 | https://awesomepapers.io/papers/wang2025promptbridge | unreachable |
| K1 | https://psnet.ahrq.gov/resources/resource/28485 and https://hms.harvard.edu/news/improved-hospital-handoffs-cut-adverse-events-almost-half | unreachable |
| K2 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2810011 and https://www.fiercehealthcare.com/healthcare/surgical-safety-checklists-may-not-improve-patient-outcomes-after-all | unreachable |
| J2 | https://www.sup.org/books/cite/?id=388 | unreachable |
| J3 | https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/ | unreachable |

I could not confirm that any of these supports its claim, and none of them is upgraded. The map already marks all of them assumed. K3 and K4 cite nothing and are marked unknown.

**Shortlists and traps**
- **Counts:** the owner shortlist has 8 items (limit 8). The research shortlist has 5 (limit 5).
- **Dependence on failed items:** no known item failed, so nothing in the shortlists or traps rests on a failed item.
- **Dependence on unreachable items:** these claims lean on unopened literature and stay unverified.
  - Research shortlist 1: its framing leans on A4, A5 and A6.
  - Research shortlist 3: it leans on F1.
  - Research shortlist 4: it leans on K1, K2 and J2.
  - Design trap "Grading with the same model family" leans on I4. The pipeline rule itself (F3, OM:251-253) is confirmed.
  - Design trap "Fitting instructions to pass the checks" leans on J3. The existing tools it points to (OM:324-325 and reviewer.md:42-43) are confirmed.
- **Traps resting on confirmed items:** all other traps rest only on confirmed items, with the J1 slips noted above.
  - "Blaming the wording": A1, A2, A7.
  - "Measuring doers with checkers": I1.
  - "Before-after comparisons": B4, F2, C4.
  - "Baseline only from the scripted path": C1-C3, L1.
  - "Fixing after each failure": J1.
  - "Repeated trials": B5.
  - "Rounds to pass": I3.
  - "Free-text briefs": M1.
  - "Changing rules faster than the owner can approve": C5, H2.

*Recorded verbatim by the orchestrator. The Source checker's second, independent check of the revised map, run on a different model from the Researcher's (L-0002). Session session_01QBwHGJH9m3A4Ray7WpHzBo, 2026-11-01.*
