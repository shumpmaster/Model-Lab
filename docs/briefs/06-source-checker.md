# Brief 06 — source-checker — file the checked facts from Q-002 to Q-007 in the portfolio library

session: session_01QBwHGHrHnEvMNYgKDoaH8w
model: claude-sonnet-5-5 (the Researchers on Q-002 to Q-007 ran on claude-opus-5-5; D-056)
recorded: at dispatch, 2026-11-01 (LL-04, LL-24)

## Brief

You are the Source checker (your role file: /home/user/Model-Lab/.claude/agents/source-checker.md). Today is 2026-11-01. Your task is the filing half of your duty: file in the portfolio library the entries that have already passed their source checks. You are not re-checking the memos; the checks are done.

**What may be filed, and with which cautions** (read these first; they decide everything):
- /home/user/Model-Lab/research/Q-002-to-Q-007-corrections-confirmation.md, section "Library entries that may be filed" (Q-002, Q-003, Q-004, Q-005, Q-007), and the wording cautions in the per-memo sections above it (LF-Q005-05a in the paper's wording; Q-007 F14 without "changing tests or scoring code"; Q-004 F-Q004-8 without "1.9–7.6%"; F-Q004-4 with "tentative" dates; and so on).
- /home/user/Model-Lab/research/Q-006-source-check.md, its confirmation section at the end (from "Library entries." on), for Q-006.

**The entries themselves:** the "Proposed library entries" section (or equivalent table) of each memo, /home/user/Model-Lab/research/Q-00N-memo.md for N = 2 to 7. Where a memo's entry and the confirmation disagree, the confirmation wins. Read the source checks beside each memo (research/Q-00N-source-check*.md, research/Q-002-to-Q-004-source-check-2.md) to fill in who opened each source.

**File only** entries the confirmation lists as fileable, with every qualifier it attaches. Do not file anything listed as Hold or Not filed. Do not strengthen any statement. If an entry cannot be filed as the confirmation requires (for example the memo's text cannot be reworded to the required wording without saying more than the source), leave it out and list it in your return.

**Where and how:**
- Work only in the git worktree /home/user/wt/pf-library (the portfolio repository, on branch build/source-checker/p001-library). The library does not exist there yet. First copy the two forms from /home/user/Personal-Org-Operating-Model/portfolio-template/library/facts/_TEMPLATE.md and .../patterns/_TEMPLATE.md to library/facts/_TEMPLATE.md and library/patterns/_TEMPLATE.md, unchanged.
- One file per entry: library/facts/<memo>-<entry id>.md (for example library/facts/Q-002-F-c.md) and library/patterns/<memo>-<entry id>.md. Fill the form exactly. `type:` fact, estimate or opinion, as the memo marks it. `grade:` strong, moderate or weak; map the memo's A/B/C grade to strong/moderate/weak and add the memo's letter in brackets, e.g. `moderate (B)`. `checked_on:` the date of the source check that confirmed the source (all 2026-11-01). `shelf_life:` the memo's proposed shelf life, followed by `(proposed by the memo; the model's shelf lives are an open owner call, OPERATING_MODEL §6)`. `topics:` from the memo. Under Statement, the corrected statement, then a line `Status: <the confirmation's filing status, e.g. single-source, attributed, not load-bearing>` and `Project: P-001 (Model-Lab), research <Q-id>`. Under Sources, each source with `— opened by: <role and record>`, naming the Researcher and/or Source checker and the record that shows the source was opened (e.g. `source-checker, research/Q-004-source-check.md (Model-Lab)`). Name a session only if the record names it.
- Add library/README.md: one paragraph saying what the library is (OPERATING_MODEL §6, D-031, D-032, D-064), then an index table of every file you filed: file · one-line statement · type · grade · status.
- Commit in small logical commits (e.g. the forms and README, then one commit per memo) with
  `git -c user.name=source-checker -c user.email=source-checker@agents.invalid commit`, each message ending with a blank line and then the two trailer lines
  `Agent-Session: session_01QBwHGHrHnEvMNYgKDoaH8w` and `Spec: none (library filing from research Q-002 to Q-007, P-001)`. No model names in commits or files. Do not push, do not merge, do not open a pull request.

**Do not** open /home/user/Model-Lab/decisions, /home/user/Model-Lab/docs/PROJECT.md, /home/user/Model-Lab/docs/handoff or /home/user/portfolio/ideas (they hold the owner's leanings, which you must not see). Do not use the web: everything you need is in the memos and checks. Do not edit anything in /home/user/Model-Lab.

**Return** the six-part contract: changed (by file, or by count per memo plus the README) · why · verified (`git -C /home/user/wt/pf-library log --oneline` and a count of filed files per memo) · undone (every fileable entry you did not file, and why) · needed outside your surface · open questions.
