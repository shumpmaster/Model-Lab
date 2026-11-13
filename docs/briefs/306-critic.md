# Brief 306 — critic — S-002: re-check of brief 305's K1 fix on its cases (P-002, M8)

session: session_01QBwHGLHPCVt3NpHNqhuahM
model: the Critic runs in a fresh session, on a different model from S-002's writer (D-056), and apart from the Definer who made the fix. Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@a1c6f404b5e0a07c2fa881eec8a1629bea452d99 (branch claude/gallant-keller-1245m3)
manifest: specs/S-002.md (as merged from brief 305, commit c866461); docs/briefs/305-definer.md; reviews/Q-018-recode-2/_critic-verbatim.md (findings 1, 6(a), 8); reviews/Q-018-rules-2/_critic-verbatim.md (findings 3, 5, 6); research/Q-018-memo-3.md; research/Q-018-extract/ (README.md, sample.json, sample.jsonl); questions/P-002-unasked-notes.md; full clones with history at /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/hc/<repository> (read only; the earlier records pack is gone)
recorded: at hand-out, 2026-11-12

## Brief
You are the Critic, re-checking brief 305's changes to specs/S-002.md (the diff a1d9f1f..c866461). Read only; write nothing.
1. K1 change (iii): does it class every file at RT1(a)'s owner-answer paths, and Service-Desk's other `docs/design/references/owner-*` files, as owner question or answer, and does it catch nothing it should not (an agent's research or records file under those paths)? Test it on Service-Desk #237, #148 and #61 and on Personal-Org-Operating-Model #25, #27, #30, #35, #49 and #50 against the clones, and say whether each one's RP2 status and kind are as the Definer's table gives.
2. Does any other rule that reads a file's class (RT1(b), RT2(a), K3, the edge-case filters as applied at the draw) now give a different result on any sampled item? Name each.
3. The new step 3 fields for clear `Q-<nnn>` ids, step 6's list (a) to (h), open question 16, and the rewordings of open question 15 and line 48: right against the records they state, and codable with no text written?
4. The two-form matching order and the changed-ruling case (brief 301 finding 6): codable, and does either change a sampled count?
Flag any self-implication (D-050). Start with exactly one line, `Verdict: PASS` or `Verdict: FAIL`, then a paragraph in plain words, then numbered findings (blocking or non-blocking, with file and line), then the six-part contract.
