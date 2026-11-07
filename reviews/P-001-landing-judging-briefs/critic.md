Verdict: FAIL

*The Critic on docs/briefs/124-orchestrator-landing.md and docs/briefs/125-judging-lead.md, brief 126 (docs/briefs/126-critic.md, on branch claude/p-001-model-lab-continue-ohykg9) for round 1; a session on a different model from the briefs' writer. Recorded verbatim by the Orchestrator, 2026-11-08. The first line is the latest round's verdict, and each round's verdict line is given here rather than in its section (LL-68).*

## Round 1 (commit ef3e2b0)

I read briefs 124 and 125 against S-001 (the sections you named, K1 to K7, J3 to J5, AC5, AC8), E-003 (Step 4, Sample, Exclusions), the scripts in src/E-003/, AGENTS.md, CLAUDE.md, briefs 113 and 119, P-001-k1-transcript-reach.md, and the reviews/E-003/built/ records. I have no shell, so I judged commands only by reading the code. I could not compute the SHA-256s the briefs list, so those are unchecked. I did not re-judge your runs (export.py make, the clone checked out at the label, fill_judge_brief.py, followup-text, list).

What holds. Both briefs carry the spec's steps in its order:
- Brief 124 has the weekly wake, K7, the K5 wake order, the guard, suite, Reviewer and merge route, counts and blocks.
- Brief 125 has K2, K3, K5, the Tuesday wake, the fingerprint check, the copy, fill, judge, reruns, transcript check, J5 line, counts and closing blocks.
- The cap of 132 matches `caps()` (120 + 12).
- The 14 J5 fields match `verdicts.py`.
- The K3 SHA-256s for transcript_check.py and e003lib.py match brief 119.
- The hook marker matches the label rule.
- The commands for `judge.py followup-text`, `parse-return`, `export.py list`, `verify` and `fill_judge_brief.py` match the scripts' flags.

**Blocking**

1. Brief 125 step 6: the first fill would refuse. `fill_judge_brief.py` never creates a folder and refuses if `--out`'s folder is missing, but the brief never creates `/tmp/s001-judge-briefs`. `<lists>` is used (the `<label>.files` redirect, `--filelists`) and never defined or created. The brief also says that a refusal means no judgement and tell the owner, so the brief as written stops at its first judgement. Fix: make both folders in K3's set-up, and name `<lists>`.

2. Brief 125 step 9: the K1 record check is weaker than the spec. It reads each record "that you have not read before". The records are append-only: each turn adds lines to sessions.md and to the work session's `session-*.md`. A file read once would never be read again, so later `k1-` lines and the canary check on them are skipped. S-001 K1 says "the K1 records added since its last block". Fix: re-read a listed file whenever it changed since the last block (by SHA-256 or line count) and check its new lines.

3. Brief 125 steps 1 and 2: a block handed out before any INDEX is read cannot be valid. `k2: fail` and `k3: fail` blocks are handed out at the start, but `index-commit` must be 40 hex (`parse_counts_lines`). The brief says "the commit you last read the INDEX at", which does not exist yet, so `verdicts.py check --counts` refuses the block. Fix: say what goes there, for example the `ls-remote` tip. Note that a K3 failure may also mean `ls-remote` fails.

4. Brief 124 steps 5 and 6: the commands do not match the interfaces.
   - `counts.py due` is given with no arguments, but it requires `--kind --side --runs --run-cards-sent --weeks --review-cards-sent`. No record keeps "cards sent", and `--weeks` has no stated source (opened.md).
   - `counts.py card` needs `--kind --work --judging --weeks`. `--judging` must be one 13-line block file (`parse_counts_lines`), but counts.md is an append-only file of many blocks.
   - `verdicts.py check` needs `--index --filelists --tests 8 --set S-001-built-1`, and takes a file, not text. The brief does not say to put each passed block or closing block into a temporary file. The closing block needs the verdict-file part cut out to record verdicts.tsv.
   - Fix: give the commands whole, and say where each number comes from.

5. Brief 124 step 4 against brief 113: the ruling has no way back to the work session. Brief 113 says the Orchestrator "rules on that pair at its landing" (`locked: unrun`) and releases a held no-spec pair "with that path". Brief 124 instead asks the owner a question. But nothing says where the ruling is recorded or how the work session reads it. Brief 113 reads only `rulings.md`, which is for counts. The Orchestrator cannot write src/**. So a held pair stays held for good, and a `locked: unrun` pair has no recorded outcome for the analysis. Fix: name the file on main that holds the ruling and have brief 113 read it, or say that the owner relays it. The reading itself (ask the owner) is the stricter one and is needed, so keep it.

**Non-blocking**

6. Brief 125 step 7:
   - `judge.py next-step --state` takes JSON `{"verdict","follow_up_sent","sessions"}`, and the brief shows no shape for it. For `sessions`, the script's rule is that 2 means leave out.
   - "Send it, in the same helper" names no mechanism, while the header bars `send_message`. Say that it continues the helper by its agent id and is not the session `send_message`.
   - It does not say what goes in `tokens` when a follow-up or a new session was used.
   - The `differs` flow (one new judge) is only named.

7. Brief 125 step 7 refers to `counts.py cap`, but counts.py is not among the fetched and hashed scripts. The brief also gives no instruction for when the 12-run reserve is spent (leave the output out and list it, per Sample). `reserve-used` is not defined. `judge.py check-model` is unused (AC5), and `brief_match.py` is not hashed (it is described in-line). Either drop the reference or add and hash the script.

8. Brief 125 step 5, the `ls-remote` reading. It is needed: nothing else pins a commit, since a raw URL on the branch name is not fixed. It is not "stricter", though. It is a second route (git over github.com) that K3 never tests, and brief 119 bars any route other than raw. Add `ls-remote` to K3, and say what to do if it is refused (`k3: fail`). Keep `main` as the landing branch: it is stricter and fits AGENTS §5 (no agent merges) and brief 113's `origin/main` reads.

9. Brief 125 gives `k2`, `k3`, `k5` and `k7` no value for "not reached". Say `untested`, as brief 119 does, and `k5: untested` if no turn found the marker gone.

10. Brief 124 step 3 order and steps:
    - The Reviewer's record path needs the PR number, which exists only after the PR is opened. Say it is pushed after opening.
    - It does not say what happens if last week's PR is still unmerged. The range `origin/main..` would re-include it. Say whether to reuse the PR or wait.
    - "Anything else … the work session's next record shows why" has no route, because the Orchestrator cannot message that session. Use "give the finding to the owner for the work session", as the FAIL clause does.

11. Brief 124 step 3 and `k1-records.md`: the file already lists sessions.md. Say not to add a path twice. Brief 124 also never says to write the `limit:` line (ruling B) for later K1 records. The existing one is already there, so this is minor.

12. Brief 125 says to read only the named paths. Add that the lead reads no other file of src/E-003/records/, since pairs/*.json hold the label draw, which the spec says the judging session never holds.

**Six-part contract**
- Changed: nothing. I hold no write tool.
- Why: to check that both briefs carry out the spec, scripts and records, as asked.
- Verified: by reading the code and records. The findings above cite the code and records they rest on. I could not run commands and I could not check the SHA-256 values.
- Undone: the SHA-256s in brief 125 (steps 2 and 3) are unchecked. Your runs were not repeated.
- Needed outside my lane: the fixes to briefs 124 and 125 (Chief of Staff or Orchestrator). Item 5 may also need a change to brief 113, and the choice of ruling channel goes to the owner.
- Open questions: where a held-pair or `locked: unrun` ruling is recorded for the work session to read (item 5). Whether the owner accepts the extra `ls-remote` route in K3 (item 8).

Files read are in /tmp/claude-0/-home-user/9a06fe22-60e0-580d-8926-30c8a46558b9/scratchpad/fix-judge/ (docs/briefs/124-orchestrator-landing.md, docs/briefs/125-judging-lead.md, src/E-003/*.py, specs/S-001.md, experiments/E-003.md, reviews/E-003/built/*).
