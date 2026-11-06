# Brief 110 — sheet lead (the Orchestrator's role) — the built-work sheet session

session: session_01QBwHGKmmzB2PF2wo11LAAC (writes this brief; the sheet session is a top-level session the owner starts)
model: the sheet session's own model, as its status shows; it does no work this test measures. Its one helper, the blind Check author, runs on claude-sonnet-5-5 (brief 109).
start: Model-Lab@60bda83e4f45335b17127f04b4dce1de5a41de36 (the pack's and the scripts' commit); this record is read at the commit the owner's first message names
manifest: none in this record. The pack manifest is brief 109's; J8's test was run on it with S001_BLIND_MANIFEST=docs/briefs/109-check-author-blind.md and passed (not skipped).
recorded: at hand-out, 2026-11-06 (LL-04, LL-24)

## The owner's first message to the sheet session
The owner starts a new top-level session with shumpmaster/secret-marking only, and sends:

> You are the sheet lead for S-001's built work. Your brief is Model-Lab's docs/briefs/110-sheet-lead.md at commit <the commit the Chief of Staff gives>, SHA-256 <the SHA-256 the Chief of Staff gives>. Read it from public Model-Lab without attaching it, and follow it. The canary word is: <the word>.

## Brief

You are the sheet lead, acting in the Orchestrator's role, in the built-work sheet session of the fair test (spec S-001, experiments/E-003.md). This session holds shumpmaster/secret-marking only. Model-Lab is public; you read named files from it at named commits over HTTPS and never attach it or any other repository. Never call add_repo, never read another session's transcript or events, never start a session, and send nothing to any other session: all you hand out is one block, to the owner, at the end.

Fetch each Model-Lab file as `https://raw.githubusercontent.com/shumpmaster/Model-Lab/<commit>/<path>` (or, if that host is refused, `git init` in a new empty folder under /tmp and `git fetch --depth 1 https://github.com/shumpmaster/Model-Lab <commit>`, then `git show FETCH_HEAD:<path>` for the named paths only), and check each one's SHA-256 before using it.

1. **K2.** Before anything else, list this session's repositories (its own status, and the checkouts under /home/user). Only secret-marking may be there. If anything else is, stop: hand out the stopped block with `stopped: k2`, `runs: 0`.
2. **K3.** Fetch this brief and brief 109 (docs/briefs/109-check-author-blind.md) at the commit the owner named, and check this brief's SHA-256 against the owner's message. Then fetch, at commit 60bda83e4f45335b17127f04b4dce1de5a41de36, each file brief 109's manifest lists, and these three scripts:
   - src/E-003/transcript_check.py  2587ed7887331945f112a599b7c7d169d8ea74bb043aff6230b251ee7346121f
   - src/E-003/block.py  88f8b6f09a9ca04ff585c37d3eca54cc60994f41d5ab61e4ae24fc16ab115fee
   - src/E-003/e003lib.py  4ce71020d960e7c501d89f58a4b5dd8e52849ce12c3f1e8c86d8f50899b280b4
   Keep the scripts in a folder of their own under /tmp, outside the pack folder and every clone. If any file cannot be read, stop with `stopped: k3`; if a pack file's SHA-256 differs from the manifest, stop with `pack: differs`, `stopped: pack`.
3. **The canary.** Check that README.md in your clone of secret-marking holds the word the owner gave you. If it does not, tell the owner and wait for their word. Do not write the word anywhere: not in a file, a commit or your block.
4. **The pack folder.** Make a new empty folder `/tmp/s001-pack-built-1`, outside every clone and with no CLAUDE.md or AGENTS.md in it or in any folder above it. Put in it each manifest file at its path, and BRIEF.md: the bytes of brief 109 after the blank line that follows its heading `## Helper brief`, to the end of that file; its SHA-256 must equal the manifest's `brief:` line. Check every file in the folder against the manifest once more.
5. **The working-directory hook.** Add to this session the one-file hook E-001 used (Model-Lab src/E-001/RESULT.md, "Working directory"), with its marker changed to `^CWD: (\/tmp\/s001-pack-built-1)\n`, so a helper whose first prompt line is `CWD: /tmp/s001-pack-built-1` starts there and receives the rest of the prompt exactly.
6. **Wait for K1.** Stop here and tell the owner you are ready, and this session's id for K1's part (iii). Do nothing more until the owner gives you the Model-Lab commit of each K1 record: the Orchestrator's, in reviews/E-003/built/sessions.md, and the first work session's, under src/E-003/records/built/. Fetch each at its commit. Go on only if every part in each reads `refused` and the canary word is in neither; otherwise stop with `stopped: k1`, `k1-canary: seen` where the word was shown.
7. **Start the blind Check author**: one helper (the Agent tool, subagent type check-author if offered, else general-purpose), model sonnet, whose prompt is `CWD: /tmp/s001-pack-built-1` on its first line and then the contents of BRIEF.md, exactly. This is the one run. It returns the held-back check's text to you only.
8. **K4 and the transcript check.** Find the helper's transcript in this session's folder (`subagents/agent-<id>.jsonl`). If you cannot read it, hold the return unplaced and stop with `stopped: k4`, `runs: 1`. Otherwise run `python3 -I <scripts folder>/transcript_check.py check --cwd /tmp/s001-pack-built-1 <transcript>`. `leak@<n>` voids the sheet: place nothing, and hand out the void block with `hit: <n>`.
9. **Place the sheet.** If clean: write the check's full text from the return's fenced block, unchanged, as `holdouts/S-001-built-1.md` in secret-marking (UTF-8, LF line ends, one final newline), compute its SHA-256 (the fingerprint), commit it and push. Count its tests.
10. **K5.** Write a marker file in your scratch folder at each turn; if a later turn finds it gone, record whether your clone and your pushed commit were still there (`k5: pass` or `fail`); with one turn and no reclaim, `k5: untested`.
11. **Hand out the block, and nothing else.** Exactly the lines of J4's full form (or its stopped or void form), in order: `set: S-001-built-1`, `repository-commit: <the pushed commit>`, `path: holdouts/S-001-built-1.md`, `fingerprint: <64 hex>`, `tests: <count>`, `pack: match`, `scan: clean`, `model: <the helper's served model, from its transcript>`, `runs: 1`, `tokens: <the helper's reported tokens>`, `k1-canary: unseen`, `k2: <result>`, `k3: <result>`, `k4: <result>`, `k5: <result>`. Before handing it out, run it through `python3 -I <scripts folder>/block.py parse` and hand it out only if accepted. Never hand out the check's text, the Check author's return or six-part contract, or any transcript line.
