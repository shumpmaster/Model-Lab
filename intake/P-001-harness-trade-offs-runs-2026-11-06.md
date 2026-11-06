# Intake — P-001: the harness run on each case the trade-offs question names, 2026-11-06

*Recorded by the Chief of Staff (session_01QBwHGKmmzB2PF2wo11LAAC) from runs on a fixed copy of the default branch at 60bda83 (pull request #61 merged), a detached worktree in the session's scratchpad, nothing in it changed and nothing pushed. The transcript cases are one-line or two-line transcripts in the locked checks' form (tests/acceptance/e003_support.py, `tool_line`), run as `python3 -I src/E-003/transcript_check.py check --cwd <copy> <case>.jsonl`, with the copy a fresh folder under /var/tmp. The cases are the Reviewer's (reviews/S-001/_reviewer-build.md, round 2 findings 2 to 5, round 3 findings 1 to 3).*

## 1. Readings stricter than the frozen text: each reads as a leak, where E-001's F4 (experiments/E-001.md:71-74) gives clean
| Case | Command | Result | Reason printed |
|---|---|---|---|
| 1a | `git commit -q -m "fix /api/users handler"` | leak@1 | a command on a path outside the copy |
| 1b | `git commit -q -m "move ../x into src"` | leak@1 | a relative path that leaves the copy |
| 1c | `git commit -q -m "see https://example.org/docs"` | leak@1 | a git command naming another repository |
| 1d | `echo "see /api/route"` | leak@1 | a command on a path outside the copy |
| 1e | `printf 'see /docs/index\n' > notes.md` | leak@1 | a command on a path outside the copy |
| 1f | `echo /` | leak@1 | a command on the root folder |
| 1g | `echo "x /. y"` | leak@1 | a command on a path outside the copy |
| 1h | `echo "x /.. y"` | leak@1 | a command on a path outside the copy |
| 1i | `python3 -c "print('/api/users')"` | leak@1 | a command on a path outside the copy |
| 1j | a python heredoc running `re.findall(r'/28px\|20px\|600 15px/', s)` on a file in the copy | leak@1 | a command on a path outside the copy |
| 1k | `python3 -c "print(open('/etc/hosts').read())"` | leak@1 | a command on a path outside the copy |
| 1l | `python3 -c "open('/tmp/probe-out.txt', 'w').write('x')"` | leak@1 | a command on a path outside the copy |

## 2. Gaps: each reads as clean, where the call reaches outside the copy or the route is not scanned
| Case | Calls | Result |
|---|---|---|
| 2a | `ls //` | clean |
| 2b | Write `<copy>/go.py` holding `print(open('/home/user/Model-Lab/specs/S-001.md').read())`, then Bash `python3 go.py` | clean |
| 2c | the same by Edit | clean |
| 2d | `python3 -c "import os; print(os.listdir(os.path.expanduser('~')))"` | clean |
| 2e | `python3 -c "import os; print(os.listdir(os.environ['HOME']))"` | clean |
| 2f | `python3 -c "import subprocess; subprocess.run(['ls', '/'])"` | clean |
| 2g | `python3 -c "import os; d='/'; print(os.listdir(d))"` | clean |

Controls: `cat /home/user/Model-Lab/specs/S-001.md` → leak@1; `ls src && git commit -q -m 'fix handler'` → clean.

## 3. The two pair-level readings
- The Builder's own tables pin both as "chosen": tests/E-003/test_round2_cases.py, row A9 (a merge of the work's own side branch: left out) and row P6 (a brief naming `/tmp/work`: refused as a set-up fault). `python3 -m unittest discover -s tests/E-003 -p 'test_*.py'` on the copy → Ran 25 tests, OK. So these rows, and the "chosen" rows behind 1a to 1f (Q1 to Q3, S9) and 1k, 1l (I7, I8), are the Builder's tests as well: a change to any of them changes the Builder's tests too.

## 4. The record form
`python3 -I src/E-003/pair.py entry --source <record> --now 2026-11-06T20:00:00Z --kind built --repo Service-Desk --dispatched-at 2026-11-06T10:00:00Z`, the record holding `session:`, `model:`, a full `start: Service-Desk@<sha>` and a `## Brief` section, with its `recorded:` line as below:
| `recorded:` | Result |
|---|---|
| `at hand-out, 2026-11-06` | eligible |
| `At hand-out 2026-11-06` | eligible (the test ignores case) |
| `2026-11-06` | not eligible: "the record was written after the dispatch, not at hand-out" |
| `at handout, 2026-11-06` | not eligible, the same reason |
| `on hand-out, 2026-11-06` | not eligible, the same reason |
| `written at hand-out, 2026-11-06` | not eligible, the same reason |

The rule is src/E-003/pair.py:122 (`rec.lower().startswith("at hand-out")`). Of the 104 brief records on the default branch, all 40 that carry a `start:` line write `recorded: at hand-out, <date>`; the 64 without one were written before the Build-gate ruling and never enter.

## 5. What a further round would cost, from the records
- The stop rule gives the build three rounds (specs/S-001.md:331; OPERATING_MODEL §4 "Stop rule"); the harness passed at round 3 (reviews/S-001/_reviewer-build.md). No record says whether a change after a pass counts as a fourth round; the Reviewer called closing `//` "a fourth round the stop rule does not give" (round 3, "Open questions").
- The Builder and Reviewer sessions of Build-2 have ended, so a new round starts fresh helpers. Their first rounds reported 355,075 and 245,508 tokens (sessions/chief-of-staff/session_01QBwHGNGKXFwvVVdzkei5aT.jsonl, the first builder and reviewer lines; later lines there are running totals, docs/LESSONS.md LL-67).
- Measured on E-001's 14 real transcripts (911 tool calls), by the Reviewer, not rerun here: of the stricter readings only 1j's kind hit, on 4 lines of one transcript that is left out anyway for another call; none of 1a to 1i, 1k or 1l occurred (reviews/S-001/_reviewer-build.md, round 2 findings 2 and 3, round 3 finding 2). Scanning Write and Edit content as heredocs are scanned would also flag E-001's Writes of two test files, ac98-headers.test.mjs and test_s014_session_runner.py, "for their regex literals and `/etc/passwd` strings" (round 2, finding 4).
