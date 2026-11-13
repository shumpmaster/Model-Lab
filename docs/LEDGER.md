# Ledger

*Append-only. Every ruling, predeclaration, reading, kill, incident and delegation is a new entry
at the bottom. A mistake is corrected by a new entry that says what was wrong, never by editing.
CI proves the old file is a byte-for-byte prefix of the new one and that IDs are unique.*

*Entries hold facts at the time of writing only. Whether an entry is still active is computed
into docs/DIGEST.md, never written back here. The title states the outcome. Write for a reader
who wasn't in the conversation: no "as discussed".*

*Fields: date · type (ruling | predeclaration | reading | kill | incident | postmortem |
delegation | defaulted | tier-change | rule-experiment | correction) · supersedes · scope ·
expires · asked · decision · licenses_next · options_considered · decided_by · proposed_by ·
reversibility.*

*Before your first commit, set L-0001's date to your start date.*

## L-0001 — Project founded under the AI Build Operating Model at tier T1
date: 2026-11-01
type: ruling
supersedes: []
scope: project
expires: never
asked: Stand the project up under a governed operating model from day one.
decision: Adopt the AI Build Operating Model at the version in governance/OPERATING_MODEL_VERSION, at tier T1. AGENTS.md is the charter.
licenses_next: Writing MISSION.md and SCOPE.md, then opening the first sprint.
decided_by: owner
proposed_by: orchestrator
reversibility: reversible

## L-0002 — Incident: this session's checkers ran on the same model as the work they checked
date: 2026-11-01
type: incident
supersedes: []
scope: P-001
expires: never
asked: Saving each helper's brief and model (decisions/questions/P-001-session-records.md) showed that every helper the Chief of Staff started on 2026-11-01 ran on the same model as the Chief of Staff and as each other: the Critic on the Chief of Staff's research question and owner questions, and the Source checker on the Researcher's map (docs/briefs/01 to 05). Model diversity (OPERATING_MODEL.md §5, D-056) requires each checker to run on a different model from what it checks; another model was available, so no waiver applies.
decision: The checks that still bear on open work are re-run on a different model: the Source checker on the revised groundwork map, and the Critic on research question Q-001. The owner questions had already been put and answered; their Critic check stands as recorded, with this entry noting it was not model-diverse. From now on each brief in docs/briefs/ names the model it asked for, and checkers are started on a different model from the doer.
licenses_next: The re-run checks; evidence for P-001 (the same gap shows in Service-Desk's records: reviews/259/reviewer.md, line 48, in that repository).
decided_by: chief-of-staff (an incident record; no ruling)
proposed_by: chief-of-staff
reversibility: reversible

## L-0003 — Q-001's model-diverse Critic check failed; its findings are carried into the research shortlist, not a new map
date: 2026-11-01
type: correction
supersedes: []
scope: P-001
expires: never
asked: Re-run on a different model (L-0002), the Critic failed research question Q-001 (reviews/Q-001/critic-diverse.md): its framing leans towards instructions being the thing to change and is sceptical of written procedure; it leaves out instruction design (length, structure, examples), levers other than instructions, how "good work" is defined and judged, handoff losses and injection, and a statement of what is out of scope. The groundwork map (research/Q-001-memo.md) was made from the failed question.
decision: The map stands as a map of questions, read with this entry. Its research shortlist is not sent as written: the Chief of Staff redrafts the research questions so that, together, they cover the map's five and the Critic's findings 1, 2 and 4 to 7, with benefits and risks put evenly; the redraft goes to the Critic on a different model before any Researcher sees it. The map already holds some of the ground (B1, I1, I2 on measures and checkers; M1, M2 on visibility and injection).
licenses_next: The redrafted research questions and their Critic check.
decided_by: chief-of-staff (a correction to its own work; no ruling)
proposed_by: chief-of-staff
reversibility: reversible

## L-0004 — Correction: Q-001's model-diverse Critic record is at reviews/Q-001-diverse/critic.md
date: 2026-11-01
type: correction
supersedes: []
scope: P-001
expires: never
asked: L-0003 cites reviews/Q-001/critic-diverse.md, a name the review check refuses (a review file is named for its reviewer's roster id).
decision: The record moved, unchanged, to reviews/Q-001-diverse/critic.md; read L-0003's citation as that path.
licenses_next: nothing new.
decided_by: chief-of-staff (a correction to its own record; no ruling)
proposed_by: chief-of-staff
reversibility: reversible

## L-0005 — Incident: researchers were briefed to read the web directly, though the rulebook routes untrusted text through the Input reader
date: 2026-11-01
type: incident
supersedes: []
scope: P-001
expires: never
asked: The Q-007 memo (research/Q-007-memo.md, S-b2) notes that OPERATING_MODEL.md §5 says untrusted text "is read only by the Input reader", while the template's researcher.md grants WebSearch and WebFetch. The Chief of Staff's briefs for Q-001 to Q-007 (docs/briefs/) let each Researcher read the web directly, treating pages as untrusted claims.
decision: Recorded as an inconsistency in the model (rule against tool grant) and in this session's briefs. The memos stand, with every web claim already marked as an untrusted claim and each source-checked on a different model. It becomes evidence for P-001 (how instructions and tool grants interact) and an item for the model's integration work; no further dispatch here reads the web directly until the owner or the model resolves which governs.
licenses_next: An owner question or model change on the Researcher's web access, raised with the Design gate case.
decided_by: chief-of-staff (an incident record; no ruling)
proposed_by: chief-of-staff
reversibility: reversible

## L-0006 — Build gate passed for P-001: proceed at size A, with the terms as recommended
date: 2026-11-04
type: ruling
supersedes: []
scope: P-001
expires: never
asked: The Build gate for the prompt engine (questions/P-001-build-gate.md, case docs/gates/P-001/build-gate-4-case.md), with the fair test's terms (questions/P-001-build-gate-terms.md).
decision: Proceed at size A: the plan's criteria are approved, and the fair test (specs/S-001.md, experiments/E-003.md) runs at 60 pieces of each kind, built work first, then plans, then research, about 732 runs and 132 million tokens. The terms are ruled as recommended (A for terms 1 to 7, the plan's answer for 8 to 11). The owner's words are recorded verbatim in decisions/questions/P-001-build-gate.md and decisions/questions/P-001-build-gate-terms.md. No status record is written by hand (decisions/questions/P-001-gate-record.md, ruling A).
licenses_next: Carrying out the terms; the Definer's freeze of S-001 through the freeze gate's check; then the Check author's locked checks, once the owner's private sheets repository is set up.
options_considered: proceed at sizes A to D; hold; recycle into Design; kill.
decided_by: owner
proposed_by: chief-of-staff
reversibility: irreversible

## L-0007 — The built-work held-back check S-001-built-1 is written, and its fingerprint recorded
date: 2026-11-07
type: reading
supersedes: []
scope: P-001
expires: never
asked: The built-work sheet session (brief 119) returned its full block (reviews/E-003/built/sheet.md): the blind Check author's check, 8 tests, placed at holdouts/S-001-built-1.md in the sheets repository at commit c4a42d5d566ede55f0585dcd1d8ca8b64b993cb5, with the pack matched, the transcript clean, the canary unseen and K2 to K4 passed (E-003 Step 1, step 6; S-001 J4).
decision: The set S-001-built-1 and its fingerprint ee47900c8fdd0e9c599ad7838d051dfaa5b517a02c23dc6d3211da2b34152fc3 are recorded in governance/HOLDOUTS.md, and the block byte for byte as reviews/E-003/built/sheet.md. K1's transcript read stands as the limit the owner ruled (decisions/questions/P-001-k1-transcript-reach.md).
licenses_next: The built-work comparison opens once this is on the default branch (src/E-003/kind.py can-open); the work session starts pairs for pieces dispatched after that.
holdouts: changed
decided_by: orchestrator (a record of the sheet route; no ruling)
proposed_by: claude-opus-5-5 (the Orchestrator in the Chief of Staff's session)
reversibility: irreversible

## L-0008 — Model v3.7.2 adopted: a later project item may have a plan of its own, keeping the Critic's role file for experiment E-003
date: 2026-11-08
type: ruling
supersedes: []
scope: project
expires: never
asked: Model-Lab runs model 3.6.0, whose checks assume one project per repository, so the second idea (the screening of cutting-edge practice, P-002) cannot be filed here (docs/LESSONS.md LL-16). Bring Model-Lab to 3.7.2 (S-035 one plan per project item; S-036 the check run's copy; S-037 a cut-short history), as the owner ruled on 2026-11-08 ("Upgrade now, then start (Recommended)", questions/P-002-route.md), without disturbing the prompt engine (P-001)?
decision: Copied byte for byte from the model at a1706c2 (tools/ and template-v3/ unchanged since b18259c, 3.7.2): governance/checks/ governance_checks.py, govlib.py, orchestrator.py, orchestrator_git.py, session_runner.py and v3_checks.py (each was the model's 3.6.0 copy, 3a2606a); template-v3's .github/workflows/orchestrator.yml, governance/BRIEFS.toml, intake/requests/README.md, docs/SETUP.md, docs/gates/_GATE.md, docs/users/_PROFILE.md, .claude/agents/builder.md, definer.md and researcher.md, and docs/projects/README.md and _TEMPLATE.md (new). The model's 3.6.0-to-3.7.2 change is applied to governance/PACKS.toml (docs/projects lines in nine standard roles; this repository's roles, S-001-analysis and S-001-holdout among them, unchanged) and governance/SURFACES.md (two lines). OPERATING_MODEL_VERSION reads 3.7.2. Two known deviations: .claude/agents/critic.md keeps its 3.6.0 text until experiment E-003 has its result, because E-003's held-back checks are written from it as it stands (experiments/E-003.md:31); until then each brief sending the Critic a P-002 plan carries its S-035 line, and the file takes the model's copy in a change of its own after E-003. docs/PROJECT.md keeps its section 3 instruction line unchanged, so the prompt engine's plan reads exactly as before. On a copy of main, every prompt-engine test and every governance check gave the same result before and after (intake/P-002-upgrade-footprint-2026-11-08.md). Nothing written before is rewritten.
licenses_next: The screening files its project request with its own plan, docs/projects/P-002.md, before any of its research; its Discovery begins. LL-16 is closed by this entry.
decided_by: owner (ruled on 2026-11-08 in session_01QBwHGNSLmSrYQgS6BPjV8p; merges this pull request)
proposed_by: chief-of-staff
reversibility: reversible

## L-0009 — The holdouts check judges a merge by its first parent
date: 2026-11-09
type: ruling
supersedes: []
scope: P-001
expires: never
asked: The first weekly landing of the built-work work session read to `v3_checks holdouts` as a change to governance/HOLDOUTS.md, though the file is unchanged on main, because the work session's branch starts before pull request #69 and `--full-history` lists a merge that differs from any parent; it would recur every week.
decision: The owner chose to fix the check (decisions/questions/P-001-holdouts-check-merges.md): `check_holdouts` follows the first-parent line, each commit against its first parent, and still compares the file at the base and at HEAD.
licenses_next: The weekly landings of the built-work work session, under brief 124.
options_considered: fix the check; let the work session bring main into its branch once (one failing landing).
decided_by: owner
proposed_by: claude-opus-5-5 (the Chief of Staff)
reversibility: reversible
