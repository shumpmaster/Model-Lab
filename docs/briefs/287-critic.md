# Brief 287 — critic — the hand check, step 5: every edge case's coding against the records (P-002, M8)

session: session_01QBwHGLzNntKRtg2k1GSyYr
model: the Critic runs in a fresh session, on a different model from S-002's writer (D-056), and apart from the Researcher who coded the memo. Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@9c6a229 (branch claude/great-newton-o6ep0u)
manifest: specs/S-002.md ("The hand check", steps 2 to 5, and the rules it quotes); research/Q-018.md; research/Q-018-memo.md; research/Q-018-extract/ (README.md, sample.json, sample.jsonl, github_reads.json); reviews/Q-018-extract/critic.md; a records pack built by the Orchestrator at /tmp/claude-0/-home-user/30b94246-fed8-5fa1-8056-3bd31c75ef0f/scratchpad/q018-pack (INDEX.md; one file per drawn item with real paths, full commit messages and the first-check records found; records/ and window/ hold question and decision files as first added; E-RT4-windows.md; comments-RT1b.md holds the 8 owner-account comments verbatim); the clones at /home/user/hc/<repository> (working trees at origin/main)
recorded: at hand-out, 2026-11-12

## Brief
You are the Critic, doing S-002's hand check step 5: "for every pull request or commit the memo lists under an edge case, it opens the records (the repositories and GitHub's records) and says whether the rule's result is right. It reads every owner comment counted under RT1(b) and says how many were not stepping in (E-RT5), and it does the checks the edge-case table gives for E-RT4, E-RR1 and E-RR3." Read only; write nothing.
1. For every item the memo lists under an edge case (section 2d, and the random-part items section 5 names as shapes of a case), say whether each rule's result is right against the records, with the record you read.
2. E-RT5: read the 8 comments in comments-RT1b.md; say how many were not the owner stepping in, and why.
3. E-RT4: the first 10 sampled pieces in the sample's order (say which order you take, and why, from S-002's words), every question and decision file first added between dispatch and merge (E-RT4-windows.md): list those that name only a milestone or a project, and whether the piece was in fact asked about.
4. E-RR1 and E-RR3: open every E-RR2 candidate of the sampled pieces past their 30 days (the memo's section 2e list; the pack's after_merge lines give the numbers) as far as is needed to say whether any reverts the piece in other words, or fixes a fault of it without naming it. Say how you chose what to open if you did not open every candidate fully.
5. The memo's undecided cases U1 to U7: for each, what the records show, and whether the rule as written decides it.
6. What the rules cannot catch, as this check shows it, for the list S-002 asks for (AC6).
A finding that shows a rule wrong goes to the Definer (S-002: "a rule it shows wrong is corrected in this draft and the Critic re-checks that rule's cases only"); name the rule and the fix.
Return first a column-0 line `Verdict: PASS` or `Verdict: FAIL` (PASS when the memo's coding of the edge cases is right against the records, apart from findings you mark non-blocking), then numbered findings each marked blocking or not, with the record and a fix, then the six-part contract.
