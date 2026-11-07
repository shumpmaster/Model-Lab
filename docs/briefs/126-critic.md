# Brief 126 — critic — briefs 124 (the weekly landing) and 125 (the judging lead)

session: session_01QBwHGNPFytF6t2VG6mnugn
model: claude-sonnet-5-5 (the briefs' writer, the Orchestrator in the Chief of Staff's session, runs on claude-opus-5-5; D-056). A new Critic session.
start: Model-Lab@ef3e2b02900877074b2cc700d1ff9c2a2e6e23b9 (fixed copy /tmp/claude-0/-home-user/9a06fe22-60e0-580d-8926-30c8a46558b9/scratchpad/fix-judge, the records branch at that commit)
manifest: none. This brief records no pack manifest of its own, so neither S001_BLIND_MANIFEST (J8) nor S001_ANALYSIS_MANIFEST (J7) is set for it.
recorded: at hand-out, 2026-11-07 (LL-04, LL-24)

## Brief

Read docs/briefs/124-orchestrator-landing.md and docs/briefs/125-judging-lead.md in /tmp/claude-0/-home-user/9a06fe22-60e0-580d-8926-30c8a46558b9/scratchpad/fix-judge. Brief 124 is the Orchestrator's own weekly landing of the built-work work session; brief 125 is the judging lead's, for a top-level session holding the sheets repository only. Check them against specs/S-001.md ("The sessions, and what each holds", "What wakes the long-lived sessions", "The landing's authority", "The judging route", K1 to K7, J3 to J5, AC5, AC8), experiments/E-003.md (Step 4, Sample, Exclusions), the scripts in src/E-003/ (their docstrings and code), AGENTS.md, CLAUDE.md, and briefs 113 and 119, which they must fit with, and decisions/questions/P-001-k1-transcript-reach.md. Check: that every step the spec gives each session is there and in order; that each command matches the script's real interface; that each session can carry out each step as written; that each sentence is supported by the record it carries out; and that the readings marked "the Orchestrator's reading" are needed and are the stricter ones (the landing branch being main, with the owner's weekly merge; the judging lead's ls-remote for main's tip; the K1 record list; the owner's questions on held pairs). The Orchestrator ran, from a folder outside any repository: export.py make on a test repository, a clone of its bundle checked out at the label, fill_judge_brief.py on a stand-in sheet (exit 0, a brief of 1,040 bytes), judge.py followup-text and export.py list; you cannot run them, so judge the commands against the code. Nothing changes in this copy while you run.

Return: first line `Verdict: PASS` or `Verdict: FAIL`; numbered findings, each blocking or not; the six-part contract.
