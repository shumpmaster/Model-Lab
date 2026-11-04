# Handoff — the prompt engine (P-001), 4 November 2026

*Written by the Chief of Staff (session_01QBwHGN4kVVA3rfHx2b4FsF) at a natural stopping point, so a fresh session can carry on without this conversation. It follows docs/handoff/2026-11-01-chief-of-staff-2.md, whose last updates this session wrote.*

## Where it stands
- **Phase:** Design, first run. The owner passed the Design gate on 2026-11-02 ("A: proceed (Recommended)", decisions/questions/P-001-design-gate.md) and accepted M1 (decisions/questions/P-001-accept-m1.md); M1's reached mark waits on LL-43.
- **The two Design checks are done:**
  - **Replay (E-001):** run in 14 of its 20 runs (about 2.5 million tokens) and analysed by the Reviewer: every kind goes to the fallback (reviews/E-001/reviewer.md). U2's fallback applies: the fair test compares new work with and without each change over the same period, with its larger sample stated.
  - **Judge consistency (E-002):** not run, recorded as "not tested" by the owner's ruling (decisions/questions/P-001-e002-not-tested.md). U3's fallback applies: held-back checks the work never sees, and a sample the owner looks at, decide.
- **Test runs used through Design:** 14 of about 100.
- **Owner rulings this session:** the open unknowns (accepted), the Design gate (proceed), M1 accepted, Model-Lab stays public ("Model lag is intended to be temporary, therefore leave it as public.", decisions/questions/P-001-model-lab-public.md), E-002 not run.
- **Lessons:** LL-38 to LL-45 (LL-42 is the briefing session's).

## Next, in order
1. **The fair test (M2).** Brief the Definer to write S-001 (specs/S-001.md, a draft) on the two fallbacks: candidate changes chosen from the count's causes (research/Q-008-memo.md) and the research; each compared with no change on new work over the same period; the pieces needed per kind and the runs and tokens that implies (E-001's runs cost about 180,000 tokens each); the held-back checks and the owner's sample; criteria as scenarios traced to V1 and V2. Then the Critic's plan review (three rounds at most), the Design standard milestones' records, the join-up review, and the Build gate case, where the owner sets the test's budget.
2. **LL-43 to the owner:** how this conversation-run project's gate approval reaches a record the checks read (the Orchestrator's status record, or the checks reading the ruling record). The Orchestrator script runs every 30 minutes and acts on status records, so this needs the owner's ruling before anything is written; then add M1's reached mark.
3. **At the end of the cycle:** the two rule-change rulings and LL-01 to LL-45 into the operating model (M5, M6); before the second idea, LL-16.

## How work runs here (learned this session)
- **Helpers cannot start helpers.** Work that must start its own helper sessions (as E-001's Builder had to) runs as a separate cloud session (create_session), which can; it needs the owner's approvals in that session for add-ons and for attaching private repositories, and cannot message back, so schedule check-ins (send_later). Copy its helpers' transcripts into the repository for the Reviewer.
- **Model-Lab is public.** Check each repository's visibility before a brief moves records between them (LL-45).
- **Every builder commit names a spec** in specs/ (LL-44); results go in the builder's lane under src/, inside the spec's Areas touched; a pull request touching src/ needs reviews/<PR>/reviewer.md.
- **Each session clones fresh:** run `git fetch --unshallow origin` in Service-Desk and Personal-Org-Operating-Model before any replay or history count.
- **Pushes:** this session pushes only claude/chief-of-staff-discovery-064xiz; keep build/ branches local and merge them with merge commits. The session's safety check refused one push of private-repository records until later; the owner's ruling covers them.
- **The stop hook asks for commits re-authored as the default identity:** do not; the repository's surface guard requires agent identities (LL-41).

## Token checkpoint
This session, by its own status at the last reading: about 490,000 tokens of context in use and about $61 estimated cost. Helpers this session: about 3.9 million tokens reported, of which the replay runs were about 2.5 million (the Builder's cloud session itself, about $58 estimated). The plan's remaining allowance cannot be read.

## Every pull request here needs the owner's merge
Model-Lab has no asks-merge grant (LL-33).
