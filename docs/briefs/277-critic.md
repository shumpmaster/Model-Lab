# Brief 277 — critic — the changed cases of S-002 and E-004 after round 3 (P-002, M8 to M10)

session: session_01QBwHGNPKhVy6fgoUjKtW6q
model: the Critic runs on a different model from the plan's writer, the Definer (D-056), in a fresh session. Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@678fd25294eabc773130fa6b4e359173ebf5197d, read from a fixed copy at /home/user/ml-fixed-277
manifest: the fixed copy; reviews/S-002/plan.md (rounds 1 to 3); the Definer's brief 276 and its change, commit f833d70; specs/S-002.md; experiments/E-004.md and experiments/E-004/line-output.txt; docs/gates/P-002/trial-terms.md; governance/SURFACES.md
recorded: at hand-out, 2026-11-12

## Brief
You are the Critic (plan review, D-043; your role file .claude/agents/critic.md). Read from the fixed copy only; write nothing. Your return is recorded verbatim in reviews/S-002/plan.md as the re-check after round 3. The plan passed at round 3; this is not a new round. As round 3's finding 9 and S-002 line 72 say, check only what the Definer's change on brief 276 (commit f833d70) touched, and the cases it changes:
1. that round 3's findings 1 to 8 are fixed as stated, or the chosen fix is sound;
2. E-RP1 and rule RP1 against frame D as now written (finding 2);
3. the new E-004 Exclusions entry "An entry and its pull requests", the void entries, the J2 judging join and J2's new awkward cases, and the entry time against the dispatch time (finding 4): that each is consistent with the rest of both files and that none lets a trial be steered after the sides are known;
4. the Definer's open question: a void later entry can leave a look judged on fewer than 30 a side, while the figures in line-output.txt assume 30 each way. Say whether the plan states this truly, and whether it needs a reserve place or only a stated limit.
A finding about text the change did not touch is out of scope unless the change makes it false. Rate each finding blocking only if it makes the plan wrong or lets a trial or the hand check be steered.

Return first a column-0 line `Verdict: PASS` or `Verdict: FAIL`, then numbered findings each marked blocking or not, each with file, line and a fix, then the six-part contract.
