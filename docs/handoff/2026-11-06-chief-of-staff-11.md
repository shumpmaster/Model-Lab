# Handoff — the prompt engine (P-001), 6 November 2026, eleventh stopping point

*Written by the Chief of Staff (session_01QBwHGNGKXFwvVVdzkei5aT). It follows docs/handoff/2026-11-05-chief-of-staff-10.md.*

## Where it stands
- **Build-2 has landed** (pull request #60): the harness scripts under src/E-003/ and their tests under tests/E-003/. On main, the locked suite passes, 228 tests with 2 skipped by design (J7 and J8's recorded-manifest tests), the Builder's 25 tests pass, and every governance check passes.
- **The owner ruled twice this session**: A on the locked AC2 research test (decisions/questions/P-001-ac2-research-test.md; the Check author corrected only its comparison, pull request #57, with the Reviewer's run of every case and the owner's verdict), and A on how the harness lands (decisions/questions/P-001-harness-landing.md; the Builder re-signed its commits as `session_01QBwHGNGKXFwvVVdzkei5aT/builder-90`, same trees, confirmed by the Reviewer, reviews/60/reviewer.md).
- main's questions/ holds only the template.

## Next, in order
1. **File the trade-offs question** the Reviewer left for the owner (reviews/S-001/_reviewer-build.md, round 2 findings 2 to 5 and round 3 findings 1 to 3; reviews/57/reviewer.md, finding 2):
   - readings stricter than the frozen text, each costing a pair (or a sheet) per hit: path-like text in echo, printf or commit messages; `echo /`; `/`-tokens and regex literals in inline code (4 lines in one of E-001's 14 transcripts); code reading /etc or writing /tmp; a merge of the worker's own side branch; a brief naming /tmp/work;
   - gaps, to close or record as limits: `ls //`; `/.` and `/..` inside quoted text read as leaks; scripts written by Write or Edit are not scanned; paths built in code are not resolved; the change paragraph checked only by its first words (AC2, both kinds);
   - the brief record form: pair.py admits a record only when its `recorded:` line starts "at hand-out".
   Any change to the harness or the locked checks after this needs the owner's ruling. Run the check on copies for each option before writing it (as intake/P-001-harness-landing-runs-2026-11-05.md did), and have the Critic check the card.
2. **Signing form:** later helpers sign `Agent-Session: <session id>/<role>-<brief>` (the ruling's "later helpers would sign this way"); CLAUDE.md still shows the bare `<session id>`. Propose its update as a mechanics change; the Check author's daa44a3 keeps the bare id.
3. **Local check runs on orch/ and records branches:** `record_checks merges` fails locally on any orchestrator commit without `Item:` (LL-29); run it the way CI does (on a test merge onto main, base `HEAD^1`) before calling a branch red, as reviews/60/reviewer.md round 2 did.
4. **Then the fair test's set-up before the first kind (built work):** the K1 probe of the sheets repository; the first sheet session; the work session. Every brief that records a pack manifest names its setting (S001_BLIND_MANIFEST for J8, S001_ANALYSIS_MANIFEST for J7), and the Orchestrator confirms the run checked the record, not skipped it.
5. The three non-blocking points on the locked checks stay for a later superseding change, by the owner's instruction; the AC2 prefix-only check joins them.

## Token checkpoint
This session's own usage is not read here. The figures the harness reports for a resumed helper are running totals (LL-67), so the helper lines in this session's file are not to be summed; the last reported figure for each helper this session was: Builder 519,881; Reviewer 421,310; Critic 132,027; Check author 95,066. No test runs have been used: the fair test's 732 runs start with the first kind.
