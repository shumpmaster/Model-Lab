Verdict: FAIL

*The Critic on docs/briefs/109-check-author-blind.md and docs/briefs/110-sheet-lead.md, brief 111 (docs/briefs/111-critic.md, on branch claude/chief-of-staff-p001-continue-qx252a) for round 1; a fresh session on a different model from the briefs' writer. Recorded verbatim by the Orchestrator, 2026-11-06. The first line is the latest round's verdict.*

## Round 1 (commit 053eb22)

Brief 109 passes everything I could check. Brief 110 fails: it leaves out spec steps and has two steps the sheet lead cannot carry out as written. All five blocking findings are in brief 110. The fixes are small.

Paths are relative to /tmp/claude-0/-home-user/0b617245-e428-5d0a-a3b5-c45887a920ed/scratchpad/fix-sheet.

**Findings**

1. BLOCKING, brief 110 step 8 (line 31) leaves out a spec stop. J4 (S-001 line 266) says that after `stopped: k4` the lead holds the return, and "if the owner rules to go on, it places the sheet and hands out the full block with `scan: unread`". K4 (line 181) gives the same fallback. The brief ends at "hold the return unplaced and stop". It never says what the lead does on the owner's go-on, and the step-11 block has no `scan: unread` case.

2. BLOCKING, brief 110 step 1 (line 20) leaves out K2's "at every resume". K2 (S-001 line 179) says each lead lists its repositories "at its start and at every resume". The brief lists them once, "before anything else". Step 6 waits across owner turns, so a resume is expected. Step 10 records K5 on a resumed machine, but nothing re-runs K2 there.

3. BLOCKING, brief 110 step 5 (line 28), question 4. The lead cannot carry it out as written.
   - The hook code is "Model-Lab src/E-001/RESULT.md, 'Working directory'" (lines 166-175 of that file).
   - Step 2 (lines 21-25) does not fetch that file, and gives it no commit or SHA-256. Line 18 requires every Model-Lab file to be hash-checked before use.
   - The lead would have to read an unnamed-commit, unverified file and install code from it.
   - Give the path, the commit 60bda83 and a SHA-256 in step 2. Or state the hook's few lines in the brief.
   - The marker change itself matches the E-001 regex form: `^CWD: (\/tmp\/s001-pack-built-1)\n`. The step-7 prompt (`CWD: ...` line, then BRIEF.md exactly) fits it.

4. BLOCKING, brief 110 step 6 (line 29), question 4. "under src/E-003/records/built/" names a directory, not a file.
   - The raw-URL route cannot fetch a directory.
   - The git fallback is restricted to "named paths only", so the lead cannot list the directory either.
   - The brief names no file or filename rule for the work session's K1 record. The owner's message does not give one either.
   - Name the file, or tell the owner to give the path with the commit.

5. BLOCKING, brief 110 steps 1, 2, 6 and 8 (lines 20, 25, 29, 31) against J4's stopped and void forms (S-001 line 266; src/E-003/block.py docstring lines 9-10).
   - The stopped form needs `pack: match|differs`, `tokens`, `k1-canary` and `k2` to `k5` lines. The void form needs `tokens` and the five k lines.
   - Step 1 says only "`stopped: k2`, `runs: 0`".
   - Step 6 gives `k1-canary: seen` for a stop but not the value on other k1 stops.
   - Step 8's void form gives only `hit: <n>`.
   - Nothing says what `pack:` reads when a stop comes before the pack is checked (k1, k2, k3), or which k lines a stopped block carries (for example `untested`).
   - The lead must guess, and block.py would refuse a wrong guess.

6. Non-blocking, brief 110 step 6 (line 29). K1 (S-001 line 176) has the probing session also record `k1: pass` and show the sheets repository absent from its listing. The brief checks only that "every part reads `refused`" and that the canary is absent. Add the `k1:` line.

7. Non-blocking, brief 110 steps 4 and 8.
   - Step 4 says the BRIEF.md hash "must equal" the manifest's `brief:` line but gives no stop. Brief 109 (line 12) says any difference is `pack: differs` and no dispatch.
   - Step 8 does not say where the helper's transcript folder is. S-001 line 141 and E-001 RESULT.md :299 say "the starting session's folder". The lead must find it itself.
   - Step 11 does not say what to do if block.py refuses the block. It also says to parse "its stopped or void form" too, which is fine.

8. Non-blocking: rules added that the spec does not give.
   - Step 3 (line 26): on a canary mismatch, "tell the owner and wait". Also "do not write the word anywhere". The spec (K1, line 172) gives only the check. Both are protective and compatible.
   - Step 2 (line 25): block.py and e003lib.py are fetched and block.py is run before hand-out (step 11). J4 makes the parser a Model-Lab test, not a lead step. K3 (line 180) lists the scripts for the judging session.
   - Step 2 (line 18): the git-fetch fallback puts a whole Model-Lab commit's objects, including the spec and change texts, on the lead's machine under /tmp. The spec says the sheet session holds no Model-Lab repository. The pack folder bar and the transcript check still apply. The fallback does widen what is readable on the machine, so flag it to the owner.
   - Step 7 (line 30): "subagent type check-author if offered". A type defined in secret-marking would be a different agent file from the manifest's. The pack folder's `.claude/agents/check-author.md` is the one that counts.
   - Step 7 (line 30): "model sonnet" is an alias. Step 11 records the served model, so this is covered.
   - Lines 16 versus 20, 26 and 29: line 16 says "all you hand out is one block, to the owner, at the end". Steps 1, 3 and 6 also tell the owner things (ready, session id, canary missing). These messages hold no sheet text. Reword line 16.

9. Brief 110 steps that match the spec, in order:
   - K2 (step 1), K3 (step 2), canary (step 3), pack folder (step 4), hook (step 5), K1 wait (step 6), helper (step 7), K4 and transcript check (step 8), place (step 9), K5 (step 10), block (step 11) follow the sheet's route (S-001 lines 214-218) and K1's "When" (line 176).
   - The pack folder rules match line 214: new, empty, outside every clone, no CLAUDE.md or AGENTS.md in it or above it.
   - The block's line order matches J4.
   - The K5 text matches line 182, and "untested" for one turn is consistent.
   - Step 9's file rules match J4 (UTF-8, LF, one final newline, SHA-256 of the file's bytes).

10. Brief 109 passes.
    - The manifest lists exactly six files: check-author.md, critic.md, reviewer.md, source-checker.md, docs/playbooks/software.md and the extract. They are the entry's must_read plus the agent file. Only software.md exists under docs/playbooks/, so `docs/playbooks/**` expands to it.
    - Nothing withheld is listed, and there is no HOLDOUTS or holdouts/ path. The paths are sorted in byte order.
    - Each file line is 64 hex, two spaces, then the path (8 matching lines of the regex: 6 files, commit, brief). `commit:` is 40 hex and `brief:` is 64 hex. The section heading and the `manifest` info string are as parse_manifest requires. The commit equals the `start:` commit.
    - The helper brief states the kind (built work) and the set id (S-001-built-1). It names reviewer.md as the file to write from, and lists the other three standards. All four SHA-256s equal the manifest's. It names no withheld path, no change id and no "arm" (checked by case-insensitive grep). The only E-003 path it names is the extract, which is allowed.
    - It bars reads and searches outside the folder, web use and fetches, and bars writing and committing. It returns to the agent that started it only. It follows the extract's "Return".
    - Minor: the record header (line 7) cites experiments/E-003.md. That is outside the helper brief and outside the pack, so it is fine.

11. Question 3, leaks. Nothing in either brief lets the sheet's text or the canary word leave the sheet session except as J4 allows.
    - The lead hands out only the J4 block. Step 11 says never the check, its return, the six-part contract or any transcript line.
    - The canary is not written to a file, a commit or the block (step 3). The helper's prompt holds only BRIEF.md.
    - Step 8 void and stop blocks carry no text.
    - The sheet is written only to secret-marking (step 9).
    - The leak surfaces are all already accepted by the spec (S-001 line 237): the lead's own reads, and the whole-tree fetch in finding 8.

**Hashes taken as given.** I cannot run sha256sum, so I could not verify any of these.
- All six manifest file hashes.
- The `brief:` hash 3c0680af…746c1d. I could not check which bytes it covers, or whether a trailing newline is included.
- The three script hashes in brief 110: transcript_check.py 2587ed78…, block.py 88f8b6f0…, e003lib.py 4ce71020….
- Brief 110's own claim that J8's test passed unskipped on brief 109 (line 6). I did not run it.
- The only internal check was that the helper brief's four hashes equal the manifest's, which they do.
- Whether commit 60bda83's files equal this fixed copy.

**Six-part contract**
1. Task: check dispatch records 109 and 110 against S-001, E-003, PACKS.toml, the J8 test, parse_manifest, block.py, E-001 and the briefs README.
2. Result: FAIL. Brief 109 passes. Brief 110 has five blocking findings (1 to 5).
3. Evidence: brief and spec line numbers above; the PACKS.toml `[roles.S-001-holdout]` entry at lines 103-121; parse_manifest at e003_support.py:298-334; block.py docstring lines 5-14; the E-001 hook at RESULT.md:166-175.
4. Not checked: any SHA-256; commit 60bda83's contents; whether the J8 test passes; the real behaviour of the hook, raw-URL fetch and transcript folder.
5. Risks: the lead guessing at stopped or void block fields; unverified hook code; a missing K4 go-on path; skipped K2 re-listing on resume.
6. Next: the Orchestrator revises brief 110 for findings 1 to 5, and ideally 6 to 8. It re-records brief 110, changing nothing in brief 109, and sends brief 110 back for a fresh check.
