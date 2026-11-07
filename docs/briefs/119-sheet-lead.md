# Brief 119 — sheet lead (the Orchestrator's role) — the built-work sheet session, on the owner's K1 ruling

session: session_01QBwHGNPFytF6t2VG6mnugn (writes this brief; the sheet session is a top-level session the owner starts). It replaces brief 110 for a new sheet session: brief 110's session stops at its step 6 on the K1 records, and the owner ruled to go on with the transcript read stated as a limit (decisions/questions/P-001-k1-transcript-reach.md). Only step 6 differs from brief 110 in what the session does.
model: the sheet session's own model, as its status shows; it does no work this test measures. Its one helper, the blind Check author, runs on claude-sonnet-5-5 (brief 109).
start: Model-Lab@60bda83e4f45335b17127f04b4dce1de5a41de36 (the pack's and the scripts' commit); this record is read at the commit the owner's first message names
manifest: none in this record. The pack manifest is brief 109's; J8's test was run on it with S001_BLIND_MANIFEST=docs/briefs/109-check-author-blind.md and passed (not skipped).
recorded: at hand-out, 2026-11-07 (LL-04, LL-24)

## The owner's first message to the sheet session
The owner starts a new top-level session with shumpmaster/secret-marking only, and sends:

> You are the sheet lead for S-001's built work. Your brief is Model-Lab's docs/briefs/119-sheet-lead.md at commit <the commit the Chief of Staff gives>, SHA-256 <the SHA-256 the Chief of Staff gives>. Read it from public Model-Lab without attaching it, and follow it. The canary word is: <the word>.

Later, at step 6, the owner sends it the two K1 records' paths and commits, which the Chief of Staff gives.

## Brief

You are the sheet lead, acting in the Orchestrator's role, in the built-work sheet session of the fair test (spec S-001, experiments/E-003.md). This session holds shumpmaster/secret-marking only. Model-Lab is public; you read named files from it at named commits over HTTPS and never attach it, clone it or fetch it whole. Never call add_repo, never read another session's transcript or events, never start a session, and send nothing to any other session. Nothing you tell the owner ever holds the held-back check's text or the canary word.

Fetch each Model-Lab file as `https://raw.githubusercontent.com/shumpmaster/Model-Lab/<commit>/<path>`, and check its SHA-256 before using it wherever this brief gives one. If that host is refused, do not fetch Model-Lab any other way: stop at K3 (the Orchestrator's reading, stricter than K3, which names no git route).

**The blocks.** Every block you hand out is one of J4's three forms (block.py's docstring), its lines in this order:
- *full:* `set: S-001-built-1`, `repository-commit: <the pushed commit, 40 hex>`, `path: holdouts/S-001-built-1.md`, `fingerprint: <64 hex>`, `tests: <count>`, `pack: match`, `scan: clean` (or `scan: unread`, step 8), `model: <the helper's served model>`, `runs: 1`, `tokens: <the helper's reported tokens>`, `k1-canary: unseen`, `k2:`, `k3:`, `k4:`, `k5:`;
- *stopped:* `set: S-001-built-1`, `pack: <match or differs>`, `stopped: <k1, k2, k3, k4 or pack>`, `runs: <0, or 1 once the helper was started>`, `tokens: <the helper's tokens, or 0>`, `k1-canary:`, `k2:`, `k3:`, `k4:`, `k5:`;
- *void:* `set: S-001-built-1`, `scan: void`, `hit: <transcript line number>`, `runs: 1`, `tokens: <the helper's tokens>`, `k1-canary:`, `k2:`, `k3:`, `k4:`, `k5:`.
Each k line reads `pass`, `fail` or `untested` (a check not yet reached is `untested`). `k1-canary` reads `seen` if the canary word was in a K1 record, `unseen` if you read both records and it was in neither, and `unread` if you stopped before reading them. In a stopped block, `pack:` reads `match` only when every pack file was checked and matched, and `differs` otherwise, since it was not shown to match (the Orchestrator's reading: J4 gives no third value). Before handing a block out, run it through `python3 -I <scripts folder>/block.py parse`. If it is refused, correct only its form against this list, never adding text, and run it again; if it is still refused, tell the owner a block was refused and hand nothing out.

1. **K2.** Before anything else, and again at the start of every later turn (every resume), list this session's repositories (its own status, and the checkouts under /home/user). Only secret-marking may be there. If anything else is: stop and hand out the stopped block with `stopped: k2`, `k2: fail`.
2. **K3.** Fetch this brief and brief 109 (docs/briefs/109-check-author-blind.md) at the commit the owner named, and check this brief's SHA-256 against the owner's message. Then fetch, at commit 60bda83e4f45335b17127f04b4dce1de5a41de36, each file brief 109's manifest lists, and these three scripts:
   - src/E-003/transcript_check.py  2587ed7887331945f112a599b7c7d169d8ea74bb043aff6230b251ee7346121f
   - src/E-003/block.py  88f8b6f09a9ca04ff585c37d3eca54cc60994f41d5ab61e4ae24fc16ab115fee
   - src/E-003/e003lib.py  4ce71020d960e7c501d89f58a4b5dd8e52849ce12c3f1e8c86d8f50899b280b4
   Keep the scripts together in a folder of their own under /tmp (the scripts folder), outside the pack folder and every clone. If any file cannot be read, or this brief's or a script's SHA-256 differs, stop with `stopped: k3`, `k3: fail`. If a pack file's SHA-256 differs from the manifest, stop with `pack: differs`, `stopped: pack`, `k3: pass` (the Orchestrator's reading: K3 read the files).
3. **The canary.** Check that README.md in your clone of secret-marking holds the word the owner gave you. If it does not, tell the owner and wait for their word. Do not write the word anywhere: not in a file, a commit or a block.
4. **The pack folder.** Make a new empty folder `/tmp/s001-pack-built-1`, outside every clone and with no CLAUDE.md or AGENTS.md in it or in any folder above it. Put in it each manifest file at its path, and BRIEF.md: the bytes of brief 109 after the blank line that follows its heading `## Helper brief`, to the end of that file. Check every file in the folder against the manifest once more, BRIEF.md against its `brief:` line. Any difference: stop with `pack: differs`, `stopped: pack`.
5. **The working-directory hook.** Add to this session a one-file hook, E-001's (Model-Lab src/E-001/RESULT.md, "Working directory") with its marker changed to the pack folder. Its whole code:
   ```ts
   const MARKER = /^CWD: (\/tmp\/s001-pack-built-1)\n/
   on('agent.spawn', ($, e, next) => {
     const m = MARKER.exec(e.prompt)
     if (!m || m[1].includes('..')) return next(e)
     return next({ ...e, cwd: m[1], prompt: e.prompt.slice(m[0].length) })
   })
   ```
   So a helper whose first prompt line is `CWD: /tmp/s001-pack-built-1` starts there and receives the rest of the prompt exactly.
6. **Wait for K1.** Tell the owner you are ready, with this session's id, for K1's part (iii) in the work session's probe (the Orchestrator's record, made against brief 110's session, stands as recorded under the ruling: the Orchestrator's reading). Do nothing more until the owner gives you, for each K1 record, its Model-Lab path and commit: the Orchestrator's (reviews/E-003/built/sessions.md) and the first work session's (a file under src/E-003/records/built/). Fetch each file at its commit. Go on only if, in each: no `listing:` line lists shumpmaster/secret-marking among the session's repositories (a line that records it absent passes); the `k1-i` and `k1-ii` lines read `refused`; the `k1-iii` line, where there is one, reads `refused`, or reads `returned <n> events` with a `limit:` line naming decisions/questions/P-001-k1-transcript-reach.md (the owner ruled to go on with that read stated as a limit); the `k1:` line reads `pass`, or `fail` with part (iii) its only part not refused; and the canary word appears in neither. Otherwise stop with `stopped: k1`, `k1-canary: seen` if the word appeared in either, else `unseen`.
7. **Start the blind Check author**: one helper (the Agent tool, subagent type general-purpose), model sonnet, whose prompt is `CWD: /tmp/s001-pack-built-1` on its first line and then the contents of BRIEF.md, exactly. This is the one run. It returns the held-back check's text to you only.
8. **K4 and the transcript check.** The helper's transcript is in this session's own folder, as `subagents/agent-<id>.jsonl` (S-001, "The sessions, and what each holds": a helper's transcript is stored in the starting session's folder). If you cannot read it: hold the return unplaced and stop with `stopped: k4`, `runs: 1`, `k4: fail`; if the owner then rules to go on, place the sheet as in step 9 and hand out the full block with `scan: unread`. If you can (`k4: pass`), run `python3 -I <scripts folder>/transcript_check.py check --cwd /tmp/s001-pack-built-1 <transcript>`. `leak@<n>` voids the sheet: place nothing, and hand out the void block with `hit: <n>`.
9. **Place the sheet.** If clean: write the check's full text from the return's fenced block, unchanged, as `holdouts/S-001-built-1.md` in secret-marking (UTF-8, LF line ends, one final newline), compute its SHA-256 (the fingerprint), commit it and push. Count its tests.
10. **K5.** Write a marker file in your scratch folder at each turn. If a later turn finds it gone, record whether your clone and your pushed commit were still there (`k5: pass` or `fail`); if no turn found it gone, `k5: untested`.
11. **Hand out the full block** ("The blocks", above), and nothing else. Never hand out the check's text, the Check author's return or six-part contract, or any transcript line.
