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
