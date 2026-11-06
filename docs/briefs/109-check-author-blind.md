# Brief 109 — check-author (blind, dispatch (a)) — the held-back check for built work, S-001-built-1

session: session_01QBwHGKmmzB2PF2wo11LAAC
model: claude-sonnet-5-5 (the blind Check author, as S-001's locked checks' writer at briefs 72 to 88 and 99; the work its check judges is done by doers on claude-opus-5-5 and judged by judges on claude-fable-5-1; D-056). A fresh helper of the built-work sheet session, started there by the sheet lead; it signs nothing, since it commits nothing.
start: Model-Lab@60bda83e4f45335b17127f04b4dce1de5a41de36 (the default branch after pull request #61; the manifest's commit, from which the sheet lead reads each pack file)
manifest: S001_BLIND_MANIFEST=docs/briefs/109-check-author-blind.md is the setting J8's test reads for this record (tests/acceptance/test_j8_holdout_pack.py); S001_ANALYSIS_MANIFEST is not set for it.
recorded: at hand-out, 2026-11-06 (LL-04, LL-24); written before the sheet session is started, as the sheet's route requires (experiments/E-003.md, Step 1, 1)

## How the sheet lead uses this record
- It builds the pack folder from the files below, each read from public Model-Lab at the commit the manifest names and checked against its SHA-256 (K3), plus BRIEF.md.
- BRIEF.md is the section "## Helper brief" below: every byte after the blank line that follows that heading, to the end of this file. Its SHA-256 is the manifest's `brief:` line.
- Any difference is `pack: differs` and no dispatch (J8).

## Pack manifest

```manifest
055c65ceebdd6c05f5e91e432556533ed98cd085b7ba0444eff4f5b3f1ff1437  .claude/agents/check-author.md
64b7c274ab5a8552f4601d201153d78d636450c5cc418e8529fe8836f194c6b0  .claude/agents/critic.md
135c3b8fbd793acd9d2a4037348b722bcbc0a50b4a354add6d6b41ce285ecc3f  .claude/agents/reviewer.md
8117387d10426b60e88f53a786a4920d316e00ee63050c0f7631ed031cfb63eb  .claude/agents/source-checker.md
977a07d1652ea418af2419139a6340877ba423a01e53057ae69cefba2a5db346  docs/playbooks/software.md
57d16aa2f127c124fe073e17f2b4b5add818dcaa2fc5ac923de2bc13a524d878  experiments/E-003/check-author-extract.md
commit: 60bda83e4f45335b17127f04b4dce1de5a41de36
brief: 3c0680afb4a7905f965171b118b1f1a41e91ca63b979cad202a33361b5746c1d
```

## Helper brief

You are the Check author. Your task is the one in experiments/E-003/check-author-extract.md, in your pack folder, which is your working directory. Read it first; it says which lines of your agent file do not apply to this task.

Kind of work: built work.
Set id: S-001-built-1.

The file you write from, as the extract's table gives it for built work, as it stands in your pack folder, with its SHA-256:
- .claude/agents/reviewer.md  135c3b8fbd793acd9d2a4037348b722bcbc0a50b4a354add6d6b41ce285ecc3f
The pack also holds the standards the extract gives for the other kinds, with their SHA-256:
- .claude/agents/critic.md  64b7c274ab5a8552f4601d201153d78d636450c5cc418e8529fe8836f194c6b0
- .claude/agents/source-checker.md  8117387d10426b60e88f53a786a4920d316e00ee63050c0f7631ed031cfb63eb
- docs/playbooks/software.md  977a07d1652ea418af2419139a6340877ba423a01e53057ae69cefba2a5db346
and your agent file, .claude/agents/check-author.md.

Read only the files in your pack folder; do not read, search or run commands on any path outside it, do not use the web, and do not fetch from any repository. Write no file and commit nothing. Return as the extract's "Return" section says, to the agent that started you only.
