# Brief 283 — critic — the hand check's extract README: the brief-record and control files, before the draw (P-002, M8)

session: session_01QBwHGLzNntKRtg2k1GSyYr
model: the Critic runs in a fresh session, on a different model from the Definer who wrote S-002 (D-056). Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@45b672a (branch claude/great-newton-o6ep0u); clones of Service-Desk at 9811f81d03c5 and Personal-Org-Operating-Model at ac6bd989b329 in /home/user/hc/
manifest: research/Q-018-extract/README.md and extract.py; specs/S-002.md ("What a touch is"; "The hand check", steps 1 to 3); /home/user/hc/Service-Desk and /home/user/hc/Personal-Org-Operating-Model (read-only)
recorded: at hand-out, 2026-11-12

## Brief
You are the Critic. S-002's hand check, step 1: the extract's README "states the file that holds the brief records or control files in Service-Desk and in Personal-Org-Operating-Model (for a piece's dispatch time, \"What a touch is\"); the Critic checks those two against the repositories before the sample is drawn." The sample is not drawn yet. Read only; write nothing.
Check, against the two repositories' own files (their docs/briefs/README.md, dispatch-log/, AGENTS.md and governance files, and the trailers you can find in their records):
1. that the README's section "Where a piece's dispatch comes from" names the right files for each repository, and that no other file in either repository holds brief records or control files that a piece's dispatch should come from;
2. that the reading of `Agent-Session:` values it states (and extract.py's parse_trailer, brief_records and control_line) links a trailer to the record S-002 means, and misses or mislinks none you can find;
3. that nothing in that section, or in how extract.py applies it, lets the Orchestrator choose which pull requests are drawn (the draw is fixed by S-002 step 2; the edge-case filters are in extract.py's FILTERS).
Anything else in the README you find wrong may be reported as non-blocking. Rate a finding blocking only if it would give a piece a wrong dispatch time or let the draw be steered.
Return first a column-0 line `Verdict: PASS` or `Verdict: FAIL`, then numbered findings each marked blocking or not, with file, line and a fix, then the six-part contract.
