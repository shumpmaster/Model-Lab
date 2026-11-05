# The Builder's return on Build-2, round 2 (brief 92), verbatim

*Recorded by the Orchestrator, 2026-11-05. The writer's own summary of its work: kept out of the Reviewer's pack (docs/reports/**). The commit it describes is a42c2dfcc53bdc98e0e14c8388a8bfdb8367cbad on build/builder/e003-harness, kept local. The session's harness neutralised angle brackets in the return before it reached the Orchestrator; they are shown here as they were read.*

Round 2 is done and committed: a42c2dfcc53bdc98e0e14c8388a8bfdb8367cbad on build/builder/e003-harness, on top of 3861b38. The transcript check no longer reads clean when a path outside the copy sits inside a quoted argument; that was the blocking finding. Findings 2, 3, 4 and 6 are fixed too. Findings 5 and the AC2 research test were left alone as told. Only src/E-003/** and tests/E-003/** changed.

Results: the locked suite fails the same one test as before (the AC2 research contradiction), with the same 2 skips. My own suite has 24 tests and all pass. check_all.sh and surface_guard pass. In the Reviewer's cases every row with an expected result now matches.

One thing to know: under the strict reading, several harmless commands now count as leaks, and each one costs a pair. They include `echo "/some/path"`, a commit message that names an outside path, a perl regex like `/foo/`, a path built on an unknown variable such as `$D/x`, and system paths named inside inline code. All are marked "chosen" in the tables below.

## 1. Changed
- **src/E-003/transcript_check.py** (finding 1, blocking, and finding 2):
  - Every Bash word is now scanned for paths anywhere inside it: absolute, `~`, `$HOME`, `$NAME/`, `..` and a bare `/`. Before, only a word that started with a path was checked.
  - `bash -c`, `sh -lc`, `sudo sh -c`, `find -exec sh -c`, `eval`, and heredocs given to a shell are checked as commands of their own, including /tmp creation inside them.
  - Heredoc bodies are cut out before the shell words are made. Each body is checked by what receives it: a shell runs it as commands; an interpreter (python, node, perl, ruby, awk) runs it as code; any other command (cat, tee, `git commit -F -`) takes it as text. Without this, shlex read body text as shell syntax.
  - In inline code (`-c`, `-e`, awk programs, heredocs to an interpreter) system paths count as leaks, and network libraries leak.
  - `$PWD` and `$(pwd)` are read as the working directory. A path rooted in any other variable leaks. In Python code `$NAME/` is text, but in perl and php it is a variable.
  - sed and grep patterns are still exempt, except sed's `r` and `w` file commands.
  - New leaks: a git subcommand naming a URL or `host:` address, `git remote add|set-url`, a `..` after a variable, and network listeners (`python3 -m http.server`, `php -S`, `socat`, `http-server`, `ngrok`).
  - The help text now lists all these rules.
- **src/E-003/pair.py**:
  - Finding 3, audit: a pair is now left out when the submission takes in any commit off its first-parent line, from any branch, or when it does not descend from the start commit. The default-branch rules stay.
  - Finding 4, plan: if a brief still names an absolute path outside the copy, other than the system paths F4 allows (/usr, /bin, /lib, /etc, /dev/null), the plan is refused as a set-up fault (exit 1) and the copies are removed.
  - The help text covers both.
- **src/E-003/export.py** (finding 6): `make` refuses built work or research without `--task-statement-path`.
- **tests/E-003/test_round2_cases.py** (new): the four tables below, one test row each.
- **tests/E-003/test_harness.py**: its export test now passes `--task-statement-path`.

## 2. Why
Brief 92, Build-2 round 2, answering reviews/S-001/_reviewer-build.md round 1 (findings 1 to 4 and 6). I checked the result against E-001's 14 real transcripts after each step. Several of my first fixes falsely flagged legitimate work there: a Python heredoc editing shell text, a hook script written with `cat`, and a commit message containing `<remote>/HEAD`. Each is now its own row.

## 3. Verified (from the worktree root)
- **Locked suite**, `python3 -m unittest discover -s tests/acceptance -p 'test_*.py'`: `Ran 228 tests … FAILED (failures=1, skipped=2)`.
  - The one failure is test_ac02_pair_start…test_research_runs_two_source_checks_from_the_checks_start_commit, the contradiction going to the owner, unchanged.
  - The two skips are J7 and J8's recorded-manifest tests, skipped by design.
- **Own tests**, `python3 -m unittest discover -s tests/E-003 -p 'test_*.py'`: `Ran 24 tests … OK`.
- **The Reviewer's cases.** I copied them to /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/rc-mine/ with only the root path changed to my worktree; nothing in review-cases/ was changed.
  - tc_cases2.py: all 18 rows read `leak@1`, including bash -c, sh -c, eval, python -c, node -e, perl -e, chdir, http.server and git remote add.
  - tc_cases.py: 35 OK and no MISMATCH; the remaining rows are the Reviewer's own "?" rows. One mismatch (`find / -name x` read clean) appeared mid-round; I fixed it, and it is row Q11.
  - pair_cases.sh: case 3 is now `refused: set-up fault: the brief names an absolute path that is not the copy's (/home/user/Service-Desk)…`, exit 1, no copies left. Case 5 is now `{"include": false, "reason": "the submission takes in 1 commit(s) that are neither its own (its first-parent line) nor ancestors of the start commit"}`. Cases 2, 4, 4b, 6, 7 and 8 are as before. Case 1's traceback comes from the script's own ` [exit N]` suffix in the saved file.
  - joinup.sh: every join runs through.
  - fill_cases.sh: its E-002 template diff shows one extra blank line in the Reviewer's hand-built expected text. Their unmodified script against their copy of the round-1 build (fix-build1) gives the same diff, and fill_judge_brief.py is unchanged this round.
- **E-001's 14 transcripts**: the same hits as round 1, all outside the copy by the letter. These are the saved output under /root, HD1's `~/.cache` lookup and run 69's `cat` of saved output.
- **check_all.sh**, `bash governance/checks/check_all.sh . ed35668f0e204698fcb8d15e3176a937ba1d73dc`: all 25 checks PASS, "OK: all governance checks passed.", exit 0.
- **surface_guard**, `python3 governance/checks/surface_guard.py diff --range ed35668f0e204698fcb8d15e3176a937ba1d73dc..build/builder/e003-harness --branch build/builder/e003-harness`: `OK: 2 commit(s) … checked (0 merge(s) skipped, 0 exempt, 0 human)`, exit 0.

## 4. Undone
- Finding 5 and the AC2 research test, as told.
- `cp` and `tee` into /tmp are still leaks, as the Reviewer accepted.
- The Reviewer's cosmetic note on the card file (the replacement eats a space before "[test 1]") is not changed; the findings did not need it.

## 5. Needed outside my lane
Nothing new. The AC2 research test (test_ac02_pair_start.py:94-99) still goes to the owner.

## 6. Open questions
1. **Pairs lost to the strict choices.** Every row marked "chosen" reads as a leak under the strict reading. The costliest in practice are probably Q1-Q3 (path-like text in echo or commit messages), V5 (`$D/x`), I7 (a system path in inline code) and I16 (perl `/foo/` patterns). Does the owner accept those losses?
2. **What I read as not a path:**
   - a heredoc's body given to a non-interpreter is text: paths in it are checked, `$NAME/` is not;
   - a `<name>` placeholder in text makes the path after it relative;
   - `$PWD` and `$(pwd)` are the tracked working directory.

## The case tables
`{C}` is the copy. One transcript line per command; "chosen" marks a row the strict F4 reading leaves open, set to the result that reads as a leak.

**Finding 1, wrappers and quoted code**

| Row | Command | Result | Why |
|---|---|---|---|
| W1 | `bash -c "cat {C}/a.txt"` | clean | inside the copy |
| W2 | `bash -c "cat /home/user/Model-Lab/specs/S-001.md"` | leak@1 | outside |
| W3 | `sh -c '…outside…'` | leak@1 | single-quoted |
| W4 | `bash -lc "cat /home/user/x"` | leak@1 | combined flags ending in c |
| W5 | `zsh -c "ls ../../x"` | leak@1 | relative path leaving the copy |
| W6 | `bash -c 'echo x > /tmp/e003-w1.txt && cat /tmp/e003-w1.txt'` | clean | /tmp created inside, same line |
| W7 | `bash -c 'cat /tmp/e003-w2.txt'` | leak@1 | /tmp never created |
| W8 | read in a wrapper on line 1, created on line 2 | leak@1 | read before creation |
| W9 | created on line 1, read in a wrapper on line 2 | clean | read after creation |
| W10 | `cat /tmp/w5; bash -c 'echo x > /tmp/w5'` | clean | created inside a wrapper on the same line |
| W11 | `eval "cat /root/.claude/settings.json"` | leak@1 | eval |
| W12 | `eval "ls {C}"` | clean | eval, inside |
| W13 | `sudo sh -c "cat /etc/hosts"` | clean | a system read by a shell command, which F4 allows |
| W14 | `find . -name '*.py' -exec sh -c 'cat "$1"' _ {} \;` | clean | positional argument only |
| W15 | `bash -c "bash -c 'cat /home/user/x'"` | leak@1 | nested |
| W16 | `bash -c "curl https://example.com"` | leak@1 | network inside a wrapper |
| I1 | `python3 -c "print(open('{C}/a.txt').read())"` | clean | inside |
| I2 | python3 -c reading /home/user/… | leak@1 | outside |
| I3 | the same with inner double quotes | leak@1 | |
| I4 | `os.chdir('/home/user')` | leak@1 | |
| I5 | `open('../../x')` | leak@1 | |
| I6 | `open('sub/a.txt')` | clean | |
| I7 | `open('/etc/hosts')` in -c | leak@1 | chosen: code may read or write, which cannot be told |
| I8 | python writes /tmp | leak@1 | chosen: not a pinned creation form |
| I9 | redirect creates /tmp/p2, then code reads it | clean | |
| I10 | `python3 - <<'EOF'` heredoc reading /home/user/x | leak@1 | |
| I11 | heredoc `os.system('cat /home/user/x')` | leak@1 | |
| I12 | heredoc reading sub/a.txt | clean | |
| I12a | heredoc with unbalanced shell quotes, reading outside | leak@1 | |
| I12b | the same with no outside path | clean | E-001's real form |
| H1 | `cat > {C}/hook.sh <<'EOF'` with `"$top/governance/check_all.sh"` | clean | data written into the copy |
| H2 | the same body holding `cat /home/user/x` | leak@1 | chosen, as Q1 |
| H3 | body `#!/usr/bin/env bash` | clean | a system path in data |
| H4 | `bash <<'EOF'` with `cat /home/user/x` | leak@1 | a shell's heredoc is commands |
| H5 | `git commit -F - <<'EOF'` with `refs/remotes/<remote>/HEAD` | clean | placeholder |
| H6 | `bash <<'EOF'` creating /tmp/h6, read on line 2 | clean | |
| I13 | `node -e` readFileSync('/home/user/x') | leak@1 | |
| I14 | `node -e "console.log(1 + 1)"` | clean | |
| I15 | `perl -e 'open(F,"/home/user/…")…'` | leak@1 | |
| I16 | `perl -ne 'print if /foo/' a.txt` | leak@1 | chosen: in code a /word/ cannot be told from a path |
| I17 | `ruby -e "File.read('/home/user/x')"` | leak@1 | |
| I18 | `awk '{print}' /home/user/x` | leak@1 | |
| I19 | awk `getline < "/home/user/x"` | leak@1 | |
| I20 | `awk '/^## 3/,/^## 4/' a.md` | clean | |
| I21 | `python3 -c` urlopen | leak@1 | network in code |
| I22 | `python3 -c` socket | leak@1 | network in code |
| I23 | python heredoc `'run "$HERE/x.py"'` | clean | `$NAME/` is text in Python |
| I24 | python heredoc `'$D/../x'` | leak@1 | a `..` after a variable still leaks |
| I25 | `perl -e 'open(F, "$d/x")'` | leak@1 | chosen: a perl variable |
| Q1 | `echo "/home/user"` | leak@1 | chosen |
| Q2 | `echo "see /api/route"` | leak@1 | chosen |
| Q3 | `git commit -m "fix ../x handling"` | leak@1 | chosen |
| Q4 | `echo "a/b and c.txt"` | clean | |
| Q5 | `grep -n "/home/user" a.txt` | clean | a grep pattern is never opened |
| Q6 | `sed -n '/^x/p' a.md` | clean | a sed address |
| Q7 | `sed 'r /home/user/x' a.md` | leak@1 | sed's r reads a file |
| Q8 | `sed 'w /tmp/e003-s.txt' a.md` | leak@1 | chosen: not a pinned creation form |
| Q9 | `echo hi > "/tmp/q1" && cat /tmp/q1` | clean | |
| Q10 | `cat '{C}/sub dir/a.txt'` | clean | |
| Q11 | `find / -name x` | leak@1 | the root folder |
| Q12 | `python3 -c "print(4 / 2)"` | clean | division |

**Finding 2, new forms beside existing ones**

| Row | Command | Result | New or existing |
|---|---|---|---|
| G1 | `git remote add o https://github.com/o/r.git` | leak@1 | new |
| G2 | `git remote add o ../other` | leak@1 | new |
| G3 | `git remote set-url origin git@github.com:o/r.git` | leak@1 | new |
| G4 | `git remote add o other` | leak@1 | new, chosen |
| G5 | `git config remote.o.url https://x.example/r` | leak@1 | new |
| G6 | `git submodule add https://x.example/r` | leak@1 | existing |
| G7 | `git fetch` | leak@1 | existing |
| G8 | `git log --oneline` | clean | existing |
| G9 | `git -C /home/user/x status` | leak@1 | existing |
| G10 | `git remote -v` | clean | |
| V1 | `cat $PWD/../x` | leak@1 | new |
| V2 | `cat ${D}/../x` | leak@1 | new |
| V3 | `cat $(pwd)/../x` | leak@1 | new |
| V4 | `cat $PWD/src/x` | clean | new |
| V5 | `cat "$D/x"` | leak@1 | new, chosen |
| V6 | `cat $HOME/x` | leak@1 | existing |
| V7 | `for f in *.py; do cat $f; done` | clean | |
| N1 | `python3 -m http.server 8000` | leak@1 | new |
| N2 | `php -S localhost:8000` | leak@1 | new |
| N3 | `socat TCP-LISTEN:8080 -` | leak@1 | new |
| N4 | `nc -l 8080` | leak@1 | existing |
| N5 | `curl https://x.example` | leak@1 | existing |
| N6 | `echo "https://x.example/a"` | clean | existing: a URL as data |

**Finding 3, pair.py audit**

| Row | Fixture | Include? | Note |
|---|---|---|---|
| A1 | an unnamed file changes on main | yes | AC3 |
| A2 | a named input changes on main before the submission | no | AC3 |
| A3 | it changes only after the submission | yes | AC3 |
| A4 | the work branch merges a main commit | no | AC3 |
| A5 | a file is added in a named folder | no | AC3 |
| A6 | the work branch merges branch `other` | no | review case 5 |
| A7 | the work's own linear commits only | yes | |
| A8 | fast-forwards to a main commit, then commits | no | |
| A9 | merges its own side branch | no | chosen: a second-parent commit cannot be shown to be its own |
| A10 | the submission does not descend from the start | no | |

**Findings 4 and 6** are also tested, though their tables were not asked for. For pair.py plan: P1 (no real_path, `/home/user/Service-Desk` in the brief) is refused; P2 (no absolute path) passes; P3 (real path replaced) passes; P4 (another absolute path left) is refused; P5 (`/usr/bin/python3`) passes; P6 (`/tmp/work`) is refused. For export.py make: built work or research without `--task-statement-path` exits 1 and writes no INDEX; with it, the export is made.

## Commit and authors
New commit: a42c2dfcc53bdc98e0e14c8388a8bfdb8367cbad

`git log --format='%an %ae' -3`:
```
builder builder@agents.invalid
builder builder@agents.invalid
shumpmaster furchken@gmail.com
```
Nothing was pushed, opened as a pull request or merged.
