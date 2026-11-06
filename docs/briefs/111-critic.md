# Brief 111 — critic — round 1 on the built-work sheet session's two briefs (109 and 110)

session: session_01QBwHGKmmzB2PF2wo11LAAC
model: claude-sonnet-5-5 (both briefs' writer, the Orchestrator in the Chief of Staff's session, runs on claude-opus-5-5; D-056). A fresh session.
start: Model-Lab@053eb2295e43fad0a55c99e234bff477a7bafdc0 (fixed copy /tmp/claude-0/-home-user/0b617245-e428-5d0a-a3b5-c45887a920ed/scratchpad/fix-sheet, the records branch claude/chief-of-staff-p001-continue-qx252a at that commit)
manifest: none. This brief records no pack manifest of its own, so neither S001_BLIND_MANIFEST (J8) nor S001_ANALYSIS_MANIFEST (J7) is set for it; it reads brief 109's manifest as the work under check.
recorded: at hand-out, 2026-11-06 (LL-04, LL-24)

## Brief

You are the Critic (.claude/agents/critic.md). Today is 2026-11-06. You hold Read, Grep and Glob only; everything is in one fixed copy, /tmp/claude-0/-home-user/0b617245-e428-5d0a-a3b5-c45887a920ed/scratchpad/fix-sheet, which nothing changes while you run.

Check two dispatch records written by the Orchestrator on claude-opus-5-5 (you run on claude-sonnet-5-5) against the frozen texts they carry out:
- docs/briefs/109-check-author-blind.md: the blind Check author's record, its pack manifest and its helper brief;
- docs/briefs/110-sheet-lead.md: the brief for the built-work sheet session's lead, which the owner starts with the sheets repository only.

The standard: specs/S-001.md (the sessions table, "Two Check author jobs", "How a hand-assembled pack is routed", "The sheet's route", "What the sheet session holds", K1 to K5, J4, J8), experiments/E-003.md ("Who does what", Step 1), experiments/E-003/check-author-extract.md, governance/PACKS.toml (`[roles.S-001-holdout]`), tests/acceptance/test_j8_holdout_pack.py and tests/acceptance/e003_support.py (`parse_manifest`), src/E-003/block.py's docstring, src/E-001/RESULT.md ("Working directory"), and docs/briefs/README.md.

In particular:
1. Does every step of brief 110 follow the spec, in its order, and does it leave out any step, stop or check the spec gives the sheet lead? Does it add any rule the spec does not give? Name each by brief line and spec line.
2. Does brief 109's manifest list exactly the files the pack entry allows plus the agent file, in the named form, sorted, with the commit and brief lines? Does its helper brief follow the extract (kind, set id, the standard for built work, the SHA-256 of each file, no withheld path, no change id, no word "arm")? You cannot run sha256sum: say which hashes you could only take as given.
3. Does anything in either brief let the sheet's text, or the canary word, leave the sheet session other than as J4 allows?
4. Could the sheet lead follow brief 110 as written, with no step it cannot carry out from what the brief gives it?

Return: first line `Verdict: PASS` or `Verdict: FAIL`; numbered findings, each blocking or not, citing the brief's line and the spec's; the six-part contract.
