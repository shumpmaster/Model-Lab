# The Critic on the hand check's extract README (Q-018, S-002 step 1), before the draw

*Recorded verbatim by the Orchestrator. Brief 283 (docs/briefs/283-critic.md), on Model-Lab@1869a30 (extract at 45b672a), with Service-Desk at 9811f81d03c5 and Personal-Org-Operating-Model at ac6bd989b329. The Critic runs on a different model from S-002's writer (D-056).*

## Round 1
Verdict: FAIL

In short: the README names the wrong file as Service-Desk's control file. The real control files hold the brief and are kept somewhere else. Separately, extract.py gives the wrong role for a control-file trailer, which changes which edge cases get drawn. And frame M depends on an input file the Orchestrator makes by hand, which can drop pull requests without anyone seeing. Personal-Org-Operating-Model's brief folder is named correctly, but its trailer reading has two gaps (findings 4 and 5). Nothing in the section on where a dispatch comes from lets anyone choose the random part of the sample. I wrote nothing.

## Findings

1. **Blocking: Service-Desk's control files are in reviews/<item>/_control/, not in dispatch-log/ (gives a wrong dispatch time).** README.md line 18; extract.py lines 183–185 and 193–207.
   - Service-Desk uses "control file" for `reviews/<item>/_control/<n>-<hash12>.json` (format `session-runner-control/1`). A builder's control file is `reviews/<spec>/_control/…` (governance/checks/orchestrator_git.py lines 102–105 and 1797; record_checks.py lines 157–163). Each one holds the brief text verbatim (`"brief"`), the `"session"` value that the commits' `Agent-Session:` trailer carries, the `role` and `dispatched_at`. Example: reviews/Q-016/_control/0-4700faf68f34.json, with session `Q-016:ready-dispatch:2026-11-02T00:46:09Z`.
   - So under S-002 ("the file that holds the brief"), this is the brief record. A dispatch-log line holds no brief.
   - The two are committed differently. The control file goes on `item/<item>`. The dispatch-log line goes in the run's default-branch commit, and that commit is rebased if its push is rejected, which changes its commit time (orchestrator_git.py lines 113–123). I cannot read commits, so I cannot show the two first-add times agree.
   - Fix: name `reviews/<item>/_control/*.json` and `reviews/<spec>/_control/*.json` as Service-Desk's control files. Link a `<item>:<route>:<time>` value to the one whose `"session"` equals it. Take the role from its `"role"` and the dispatch time from the commit time of its first add. Keep the dispatch-log line only as a cross-check, and list any value where the two times differ.

2. **Blocking: a control trailer's role is lost, so the E-K2 filter fires wrongly (the draw departs from S-002 step 2).** extract.py lines 119–120, 217 and 379; README.md line 18.
   - `parse_trailer` returns role `None` for a control value. `commit_fields` copies that `None` into `trailer_briefs`. E-K2 then tests `b["role"] not in K2_LIST`, so every frame M pull request carrying a control trailer matches E-K2, even when its line's role is `researcher` or `builder`.
   - This contradicts README line 18 ("its role is the line's role") and S-002 step 3 ("that trailer's role"). The row-level `briefs` list does get the right role, but the filter does not use it.
   - Fix: in `commit_fields`, resolve a control value's role through the control-file lookup (finding 1), so `trailer_briefs[].role` is the recorded role. Use the same role in E-K2.

3. **Blocking: frame M depends on `merge.json`, an input the README does not describe, and drops pull requests silently (the draw can be steered).** extract.py lines 281–284; README.md line 9.
   - A pull request merged in GitHub's list is left out of frame M, and its commits can fall into frame D, when either:
     - its number is missing from `<github dir>/<repo>.merge.json`, a hand-made input whose making the README never states and whose shape (`[...][1][0]`) is undocumented; or
     - the merge commit it gives is not on the default branch.
   - Nothing is reported either way. frames.json (line 360) does not hold GitHub's count of merged pull requests to compare against README line 9's figures (103, 340, 55). S-002 step 2 says "the Orchestrator chooses nothing".
   - Fix: find each merge commit inside extract.py from git: the first-parent default-branch commit whose second parent is the pull request's `head_sha`. Otherwise, state exactly how merge.json is made. Either way, make extract.py stop on, or list in frames.json, every merged pull request that gets no frame M row, and record per repository the merged count in GitHub's list beside the frame-eligible count.

4. **Non-blocking (would be blocking if any such trailer exists): a suffixed Personal-Org-Operating-Model brief is mislinked.** README.md line 21; extract.py line 127.
   - docs/briefs holds suffixed brief records: s-014-r2.md, s-015-proof-brief.md, -start, -sandbox-deps, -diagnostics, -diagnostics-r2, -diagnostics-r3, -diagnostics-structure and -bash-diag.
   - A value naming one of them (for example `…/tools-builder-s015-proof-brief`) would be linked to s-015.md. That file was first added earlier, so the dispatch time would come out too early, widening the touch window.
   - The README's own example (`s-015-proof-brief.md`) shows it knows these files exist. Every such brief tells its builder to sign `Agent-Session:` with no form given, so I found no suffixed value in the files, but I cannot read commit trailers.
   - Fix: match the longest `docs/briefs/s-NNN-<suffix>.md` whose suffix the value holds, and fall back to `s-NNN.md` only when none matches. Or have extract.py list every value with text after the number, so the Critic can check them.

5. **Non-blocking: README line 21 says every task id is `s-<three digits>`, which is false.** docs/briefs also holds adopt-v3.md and adopt-v3-stamp.md. A value naming them falls back to the first commit. Fix: state these two, and read `adopt-v3`, `adopt-v3-stamp` as brief ids.

6. **Non-blocking: the control-value pattern is narrower than the loop's own.** extract.py line 119 accepts items `(Q|P)-\d+` and routes `[a-z\-]+`. The loop allows items `[PQE]-[0-9]+` and routes `[a-z][a-z0-9-]*` (session_runner.py lines 149–151). No E- item and no route with a digit appears in dispatch-log/ today, so nothing is mislinked now. Fix: use the loop's patterns.

7. **Non-blocking: the "first add" is the first in git's listing, not the earliest commit time.** extract.py lines 164–167 and 206.
   - `git log --reverse` without `--topo-order` or `--date-order` is not strictly in commit-time order when committer dates are out of order (rebased commits, the loop's rebased default commit).
   - Fix: take the minimum commit time over every commit that adds the path, or every commit whose `-S` count changes for the line.

8. **Non-blocking: frames.json lacks each repository's "read" / "not read".** S-002 step 3 requires that field per repository. extract.py line 360 does not write it. Fix: add it.

9. **Non-blocking, for the Definer (spec, not README): most Personal-Org-Operating-Model pieces fall back to their first commit.**
   - That repository's briefs are `s-NNN.md` for spec S-NNN. Its builders sign a bare `Agent-Session:` plus `Spec: S-NNN` (docs/briefs/s-035.md, s-036.md, s-037.md, line 8).
   - S-002 links briefs by `Agent-Session:` only, so these pieces get no brief record even though one exists, and is linkable through `Spec:`. The README follows S-002 correctly (line 22).

10. **Non-blocking, for the memo:**
    - Model-Lab's brief 103 tells its builder to sign `…/builder-90` (docs/briefs/103-builder.md line 13). That work links to 90-builder.md, which is correct under S-002's words but is a brief dispatched earlier.
    - Model-Lab briefs 01–09 are zero-padded (`04-builder.md`), and extract.py line 180 would build `4-builder.md` from a value ending `-4`. I found no such value.
    - Service-Desk's loop lands items by its own merge and push, not through pull requests (orchestrator_git.py lines 2991–2995). So E-K3 and other control-dispatched cases may be "not seen" in frame M.

On check 3: the random part (lines 390–400), the order (line 369) and the edge-case pass (lines 401–410) match S-002 step 2. Reviews and closing accounts are read after the draw and no filter uses them. Apart from findings 2 and 3, nothing in the section or code lets anyone choose the draw. README lines 25–49 match S-002 lines 74–97 word for word.

## Six-part contract
- **Changed:** nothing (no write tool).
- **Why:** brief 283, which carries out S-002's hand check step 1 before the sample is drawn.
- **Verified:** read with Read, Grep and Glob, no shell:
  - research/Q-018-extract/README.md and extract.py; specs/S-002.md lines 1–196.
  - Service-Desk: docs/briefs/ (README only), dispatch-log/2026-10.jsonl and 2026-11.jsonl (dispatch lines; no item other than Q-/P-; no route with digits), reviews/*/_control/ (more than 100 files; one read: reviews/Q-016/_control/0-4700faf68f34.json), governance/checks/orchestrator_git.py (lines 96–150, 1560–1700, trailer code), session_runner.py and orchestrator.py id patterns.
  - Personal-Org-Operating-Model: docs/briefs/ (27 files, including suffixed ones and adopt-v3*), its README, the trailer lines in its briefs and docs/reports/s-004.md and s-006.md; no dispatch-log/ or _control/ there.
  - Model-Lab: docs/briefs/01–09 and 103-builder.md.
- **Undone:** commit trailers and commit times could not be read (git objects not readable). So I could not confirm whether any suffixed or control-form trailer sits in a frame M pull request (findings 1, 2, 4), or whether the control-file and dispatch-log first-add times agree. S-002 lines 197–255 were not read; they were not in the manifest's sections.
- **Needed outside my surface:**
  - Orchestrator: fix the README and extract.py for findings 1–8, then return them for a re-check of those findings only.
  - Definer: consider finding 9.
- **Open questions:**
  - Should Personal-Org-Operating-Model's `Spec:` trailer be allowed to name a brief? That is the owner's or Definer's call; it changes S-002.
  - For a control trailer, is S-002's dispatch the control file's first add or the line's `dispatched_at` / `time`? S-002 says commit time; the record also holds the dispatch time itself.
