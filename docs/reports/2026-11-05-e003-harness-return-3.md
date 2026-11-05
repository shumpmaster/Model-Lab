# The Builder's return on Build-2, round 3 (brief 97), verbatim

*Recorded by the Orchestrator, 2026-11-05. The writer's own summary of its work: kept out of the Reviewer's pack (docs/reports/**). The commit it describes is 9caff21a5be3f6e434cfd4daee6d6f3a9df7d4db on build/builder/e003-harness, kept local.*

Round 3's one blocking finding is fixed and committed: 9caff21a5be3f6e434cfd4daee6d6f3a9df7d4db, on top of a42c2df. A lone `/` inside quoted text, such as `echo "== optional loop / A3 6"`, no longer reads as the root folder. It still does as a word of its own (`find / -name x`, `ls /`, `cd /`), including inside a wrapper. Over all 911 tool-call lines of E-001's 14 transcripts, exactly one result changed: line 77 of agent-ab62a6f88f1e8912b.jsonl now reads clean. Nothing else changed. Round 2's findings 2 to 5 are untouched, as briefed, and only src/E-003/** and tests/E-003/** changed.

The locked suite fails the same one test as before, the AC2 research contradiction that goes to the owner, with the same two skips. My own tests, check_all.sh and surface_guard all pass.

## 1. Changed
- **src/E-003/transcript_check.py**, in `scan_word`: the lone-slash rule is now applied to the whole word, not to every token inside it. A word that is exactly `/`, `/.` or `/..` is the root folder. In inline code only, a `'/'` passed straight to a call that takes a path is too: listdir, scandir, chdir, walk, open, opendir, readdir, readdirSync, stat, exists, isdir, isfile, iterdir, glob, rmtree, Path, readFileSync, Ruby's Dir.entries and File.read, and a few more. The new code is two constants, `ROOT_WORDS` and `ROOT_CALL_RX`, plus the check that replaces the old token check.
- **tests/E-003/test_round3_cases.py** (new): the case table below, one test row each. It uses the same row runner as test_round2_cases.py, which is unchanged.

## 2. Why
Brief 97, build round 3. The round-2 rule counted a lone `/` anywhere inside a word as the root folder. A whole quoted string is one shell word, so `echo "… / …"` read as a leak. E-001's F4 does not make that a leak, and the Reviewer measured it as costing a real pair.

Inline code needed its own rule, because there `/` is usually division or a separator, as in `.split('/')`. a42c2df reads those E-001 lines clean, and this round had to leave them unchanged.

## 3. Verified (from the worktree root)
- **Locked suite**, `python3 -m unittest discover -s tests/acceptance -p 'test_*.py'`: `Ran 228 tests … FAILED (failures=1, skipped=2)`. The failure is test_ac02_pair_start…test_research_runs_two_source_checks_from_the_checks_start_commit, the contradiction going to the owner, unchanged. The two skips are J7 and J8's recorded-manifest tests, skipped by design.
- **Own tests**, `python3 -m unittest discover -s tests/E-003 -p 'test_*.py'`: `Ran 25 tests … OK`. Every round-2 row passes unchanged, Q11 (`find / -name x` leaks) and Q12 (`print(4 / 2)` clean) included.
- **The E-001 comparison.** I wrote my own script, /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/r3cmp/perline.py, rather than the Reviewer's e001_perline.py: theirs compares their two fixed copies, not a42c2df against this build. Mine follows their method: per line, with each run's saved outputs under /root/.claude/…/tool-results allowed. It checks a42c2df's checker, taken with `git show`, against the new one over all 14 transcripts.

| Transcript | a42c2df hits | New hits |
|---|---|---|
| agent-a1529681c3c6999ea | none | none |
| agent-a38329abe6de7db22 | none | none |
| agent-a6cbb56bbe1225ac8 | none | none |
| agent-a70b45e766b529403 | 90, 126, 130, 149, 152, 194, 201, 238, 262 | the same |
| agent-a764fd78aa3c29e53 | none | none |
| agent-a906f2abb95b010ac | 84, 89, 93 | the same |
| agent-aac871dc35a9c9e1e | 65, 76, 85, 103-109, 124-126, 145, 149 | the same |
| agent-ab62a6f88f1e8912b | **77** | **none** |
| agent-ab887fdf99fa3f869 | none | none |
| agent-ac84c57d54199393d | none | none |
| agent-acb867b190aa02251 | none | none |
| agent-ad906ab597fdf5cd8 | none | none |
| agent-ade76f14edd6cd6ec | none | none |
| agent-ae56bbe512ac13ad1 | 178 | the same |

Totals: 911 lines with a tool call; 29 hits at a42c2df, 28 now. The script's own output: `lines whose result changed: [('agent-ab62a6f88f1e8912b.jsonl', 77, 'a command on the root folder', 'clean')]`.
- **check_all.sh**, `bash governance/checks/check_all.sh . ed35668f0e204698fcb8d15e3176a937ba1d73dc`: no FAIL, "OK: all governance checks passed.", exit 0.
- **surface_guard**, `python3 governance/checks/surface_guard.py diff --range ed35668f0e204698fcb8d15e3176a937ba1d73dc..build/builder/e003-harness --branch build/builder/e003-harness`: `OK: 3 commit(s) … checked (0 merge(s) skipped, 0 exempt, 0 human)`, exit 0.
- `git diff --stat a42c2df HEAD`: 2 files, 69 insertions and 2 deletions.

## 4. Undone
Round 2's findings 2 to 5 (regex literals in inline code, the over-strict rows, Write and Edit content, forms the check cannot resolve), as briefed. They go to the owner as trade-offs and limits.

## 5. Needed outside my lane
Nothing new. The AC2 research test still goes to the owner.

## 6. Open questions
1. **S9, `echo /`.** It leaks, because a word of its own is read as a path whatever the command does with it. I chose the strict result; the gate may disagree.
2. **The list of path-taking calls is finite.** A `'/'` handed to a call outside it, or through a variable such as `d = '/'; os.listdir(d)`, reads clean. That belongs with round 2's finding 5, forms the check cannot resolve.

## The case table (tests/E-003/test_round3_cases.py)
`{C}` is the copy; one Bash call per row.

| Row | Command | Result | Why |
|---|---|---|---|
| S1 | `find / -name x` | leak@1 | the root folder, a bare / |
| S2 | `ls /` | leak@1 | |
| S3 | `cd / && ls` | leak@1 | |
| S4 | `ls /.` | leak@1 | |
| S5 | `ls /..` | leak@1 | |
| S6 | `bash -c "find / -name x"` | leak@1 | in a wrapper |
| S7 | `sh -c 'ls /'` | leak@1 | in a wrapper |
| S8 | `bash -c "cd / && ls"` | leak@1 | cd in a wrapper |
| S9 | `echo /` | leak@1 | chosen: a word of its own |
| C1 | `python3 -c "import os; print(os.listdir('/'))"` | leak@1 | |
| C2 | `python3 -c 'import os; os.chdir("/")'` | leak@1 | |
| C3 | `python3 -c "…os.walk('/..')…"` | leak@1 | |
| C4 | `node -e "…readdirSync('/')…"` | leak@1 | |
| C5 | a heredoc to python3 calling `os.listdir('/')` | leak@1 | |
| C6 | `python3 -c "…Path('/').iterdir()…"` | leak@1 | |
| T1 | `S=specs/S-001.md; echo "== optional loop / A3 6"; grep -n 'optional loop' $S \| head -12` | clean | line 77's form |
| T2 | `printf 'a / b\n'` | clean | |
| T3 | `git commit -q -m "fix a / b"` | clean | a commit message |
| T4 | `grep -n "a / b" notes.txt` | clean | a grep pattern |
| T5 | `sed -n 's/ \/ /x/p' notes.txt` | clean | a sed pattern |
| T6 | `echo "path: /"` | clean | |
| T7 | `bash -c 'echo "x / y"'` | clean | quoted text inside a wrapper |
| T8 | a heredoc to `cat > {C}/n.txt` holding `a / b` | clean | |
| T9 | `python3 -c "print(4 / 2)"` | clean | division |
| T10 | `python3 -c "print('a/b'.split('/'))"` | clean | not a path call |
| T11 | `python3 -c "print('/'.join(['a', 'b']))"` | clean | a separator |
| T12 | `awk '{print $1 / 2}' notes.txt` | clean | division in awk |
| T13 | a heredoc to python3 with `x = 6 / 3` | clean | division |

Against a42c2df, ten rows of this table failed: T1-T3, T6, T7, C1, C2 and C4-C6. All pass now.

## Commit and authors
New commit: 9caff21a5be3f6e434cfd4daee6d6f3a9df7d4db

`git log --format='%an %ae' -3`:
```
builder builder@agents.invalid
builder builder@agents.invalid
builder builder@agents.invalid
```
Nothing was pushed, opened as a pull request or merged.
