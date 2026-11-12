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

## Round 2 (brief 284: round 1's findings 1 to 8 only, on Model-Lab@ec88454)
Verdict: FAIL

In short: seven of round 1's eight findings are fixed. One gap is left under finding 3 (frame M can be shaped by the input). The extract now checks that every merged pull request in the GitHub list gets a row in frame M. It does not check the other direction: that every pull request GitHub merged appears in that list. The list is the Orchestrator's own hand-made file, and frames.json's "GitHub merged" counts are taken from it, so they cannot catch a pull request left out of it. A left-out pull request would fall into frame D without anyone seeing. That gap is in the fix I asked for in round 1, so this finding implicates my own earlier check (D-050 flag). I wrote nothing.

## Findings

1. **Blocking (round 1 finding 3, not closed; implicates my round-1 check, D-050): nothing checks that GitHub's list is complete.** extract.py lines 328–343 and 419–421; README.md lines 9–10.
   - `github_merged_in_window` and `github_merged_all` are counted from `<github dir>/<repo>.list.jsonl`. That is the same input frame M is built from, so it is not an independent check.
   - If a merged pull request is missing from the list, its merge commit is not in `in_pr`. That merge commit, which GitHub committed with two parents, and the pull request's own commits then fall into frame D (line 413) with nothing reported. Frame D in Service-Desk holds 566 commits, so this would not stand out.
   - Fix: extract.py already builds `by_head` from git. Count every first-parent default-branch commit committed by GitHub with two parents and merged in the window, and stop (or list in frames.json) on any whose second parent matches no listed pull request's `head_sha`. Write that count in frames.json beside `M`.

2. **Round 1 finding 1: closed.** README.md line 19 and extract.py lines 190–191 and 211–227 now name `reviews/<item>/_control/*.json` (and `reviews/<spec>/_control/…` for a builder). A value is linked to the file by its `session`, the role comes from the file's `role`, and the time is the file's earliest first add. The dispatch-log line is kept as a cross-check only. frames.json lists 17 values: 16 differ by 1 to 6 seconds, and 1 (`control:48ef806e`) has no dispatch-log line. That matches README line 19.
   - Non-blocking: line 218 uses `idx.setdefault`. A session with control files in both `reviews/<item>/_control/` and `reviews/<spec>/_control/` (a builder's) therefore takes the time of whichever path is listed first. Fix: keep every path for a session and take the earliest first add among them.
   - Non-blocking: line 226 appends to `CTRL_CHECK` on every call. Today the 17 entries are all different, but a value carried by two commits would be listed twice. Fix: key the list by value.

3. **Round 1 finding 2: closed.** extract.py lines 254 and 261–262 now give a control trailer the role from its control file, so the E-K2 filter (line 442) sees `researcher`, `builder` and so on.
   - Non-blocking: a control value with no control file still gets role `None`, which matches E-K2. Fix: list such values in frames.json (today, by the cross-check, there may be none).

4. **Round 1 finding 4: closed.** extract.py lines 129–133 and 199–207, README.md line 22: the record is now the longest suffixed `s-NNN-<suffix>.md` whose suffix the value holds, else `s-NNN.md`. Values that match no suffixed file are listed (frames.json: none in all three).

5. **Round 1 finding 5: closed.** README.md line 22 and extract.py lines 127–128 now name `adopt-v3-stamp` and `adopt-v3`, the longer one tested first.

6. **Round 1 finding 6: closed.** extract.py line 119 uses the loop's own patterns, `[PQE]-[0-9]+` and `[a-z][a-z0-9-]*`. README.md line 19 says so.

7. **Round 1 finding 7: closed.** Each first add is now the earliest commit time, not the first in git's listing: `_first_adds` (line 171), `control_line` (line 244, `min`) and `qd_files` (line 281). README.md line 23 says so.

8. **Round 1 finding 8: closed.** frames.json gives `"github_records": "read"` per repository (extract.py line 419; README.md line 57).

Also checked, no finding:
- The Model-Lab zero-padding fallback (extract.py line 186; README.md line 17) is right.
- The merge commit is now found from git (lines 328–341), and the run stops on an in-window merged pull request with no row (lines 342–343). frames.json shows M equal to GitHub's in-window count in each repository: 98/98, 322/322 and 43/43, with no pull request lacking a row.
- The draw code (lines 449–476) is unchanged and matches S-002 step 2.

## Six-part contract
- **Changed:** nothing (no write tool).
- **Why:** brief 284, a round-2 re-check of round 1's findings 1 to 8.
- **Verified:** read in full research/Q-018-extract/README.md, extract.py and frames.json. Checked Service-Desk governance/checks/session_runner.py lines 775–814: a `checks` session has its own session value and its own control file, so it does not collide with a builder's. Read docs/briefs/284-critic.md. Commits and git objects could not be read, so frames.json's figures are taken as the run's output and were not re-derived.
- **Undone:** I could not count GitHub-committed merge commits in the window myself (no shell, git objects not readable). That is why finding 1 asks extract.py to do it.
- **Needed outside my surface:** the Orchestrator fixes finding 1, plus the non-blocking points under findings 2 and 3 if it wishes, and returns them for a re-check of finding 1 only. The sample stays undrawn until then.
- **Open questions:** none new. Round 1's open questions (whether Personal-Org-Operating-Model's `Spec:` trailer may name a brief; which time S-002 means for a control file) are still with the Definer and the owner.

## Round 3 (brief 285: round 2's finding 1 and the non-blocking points under its findings 2 and 3, on Model-Lab@feacfa3)
Verdict: PASS

In short: round 2's one blocking finding is closed. extract.py now counts GitHub's merge commits from git itself, without using the Orchestrator's list, and stops if any of them matches no listed pull request. Its counts equal frame M in all three repositories (98, 322 and 43), with none unmatched. The non-blocking points under round 2's findings 2 and 3 are closed as well. Nothing left in the extract lets the draw be steered or gives a wrong dispatch time as far as these checks reach, so the sample may be drawn. I wrote nothing.

## Findings

1. **Round 2 finding 1 (no check that GitHub's list is complete): closed.**
   - extract.py lines 346–352 take every first-parent commit on the default branch that GitHub committed, that has two parents and whose commit time falls in the window. They read these from git (`fp`, line 330), not from the list. If any one's second parent is not a listed pull request's head commit, the run stops.
   - frames.json gives `git_github_merge_commits_in_window` as 98, 322 and 43, equal to `M` in each repository, and `git_merge_commits_matching_no_listed_pull_request` as empty in all three. README.md line 10 says the same.
   - A merged pull request left out of the list can no longer fall into frame D unseen.
   - Non-blocking, for the record only: the check covers merge commits that GitHub committed, which README.md line 10 says is how all 498 merged. A pull request merged some other way would already have stopped the forward check at lines 337–345 if it was listed. If it was not listed, it looks the same as a local merge, which S-002 puts in frame D under E-RP1 anyway. No fix needed.

2. **Round 2 finding 2, both non-blocking points: closed.**
   - Sessions with more than one control file: line 219 now keeps every control file a session has, and line 225 takes the earliest first add among them. README.md line 19 says so.
   - Repeated cross-check entries: `CTRL_CHECK` is now keyed by value (lines 210 and 228), so a value carried by two commits is listed once.
   - Non-blocking, cosmetic: line 211 carries a stray copy of the old `CTRL_CHECK` comment after the `NO_CONTROL` comment. Fix: delete the second comment.

3. **Round 2 finding 3, non-blocking point: closed.** A control-form value with no control file is now added to `NO_CONTROL` (line 223) and listed in frames.json as `control_values_with_no_control_file`. That list is empty in all three repositories, so no such value reaches the E-K2 filter with role `None`.

## Six-part contract
- **Changed:** nothing (no write tool).
- **Why:** brief 285, round 3: round 2's finding 1 and the non-blocking points under its findings 2 and 3.
- **Verified:** read docs/briefs/285-critic.md; extract.py lines 205–234 and 324–355, plus a grep for the new frames.json keys (lines 210–211, 219–229, 330–352, 431–434); README.md lines 9–19; frames.json keys `M`, `D`, `git_github_merge_commits_in_window`, `git_merge_commits_matching_no_listed_pull_request` and `control_values_with_no_control_file` for all three repositories. Commits could not be read (no shell, git objects not readable), so frames.json's figures are taken as the run's output and were not re-derived.
- **Undone:** none within this brief.
- **Needed outside my surface:** none beyond what is already routed: the Orchestrator may draw the sample (`python3 -I -B extract.py draw <this folder>`); round 1's finding 9 is with the Definer and finding 10 goes to the memo.
- **Open questions:** none new. Round 1's open questions (whether a Personal-Org-Operating-Model `Spec:` trailer may name a brief, and which time S-002 means for a control file) are still with the Definer and the owner.
