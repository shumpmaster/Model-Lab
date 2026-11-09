# Extract for research question Q-017

Made by the Orchestrator on 2026-11-09 with extract.py and rounds.py (this folder); extract.py was run with the owner's configured git address as its argument (used only for classing, and not written), from full clones of shumpmaster/Service-Desk, shumpmaster/Model-Lab and shumpmaster/Personal-Org-Operating-Model at origin/main. The clones were shallow until 2026-11-09 and were deepened to the full history first.

No commit subjects or messages are included. All dates are UTC.

## <repo>.commits.jsonl, one line per commit reachable from the default branch
- hash, parents (two for a merge), author_date, commit_date, author, committer;
- author_class: "agent" for an address ending in agents.invalid; "owner" for the GitHub account shumpmaster and the addresses it uses; "other" for anything else (for example a GitHub Actions bot, or a tool's default identity). Addresses are not written;
- kind: "merge-pr" (a merge commit that GitHub made for a pull request, recognised by a "Merge pull request #n" subject or a subject ending "(#n)"), "squash-pr" (a single-parent commit whose subject ends "(#n)"), "other-merge" (any other merge commit), or "plain";
- pr: the pull request number for merge-pr and squash-pr, else null;
- revert: true if the subject starts "Revert";
- mentions_prs: other pull request numbers the subject names;
- co_author_classes: the class of each Co-authored-by trailer;
- files: each changed path with its added and removed line counts (null for a binary file). Merge commits list no files. Renames show as a removal and an addition.

## <repo>.prs.jsonl, one line per pull request merged into the default branch
- pr, how ("merge" or "squash"), merged_at (the merge or squash commit's commit date), merge_commit, merge_commit_author and its class. For a merge, GitHub authors the merge commit as the account that merged it; for a squash, the commit's author is the pull request's author and the merging account is not recorded;
- commits: for a merge, the commits reachable from its second parent and not from its first (the pull request's own commits); for a squash, the squash commit alone;
- commit_author_classes: the count of those commits by author class; co_author_classes;
- files: the union of those commits' paths, with summed line counts.

## Labels in place of paths
Paths under questions/, decisions/, docs/projects/, ideas/ or sessions/chief-of-staff/, docs/PROJECT.md, and any file ending -notes.md, are shown as <questions:id>, <decisions:id>, <project-plan:id>, <ideas:id>, <cos-session:id> or <notes:id>. Paths under docs/handoff/, and any path containing chief-of-staff, are shown as <cos-handoff:id>. Any path segment that contains a project item's id (P and three digits, with or without a hyphen, in either case) or the word widget is shown as item-<id>. Each id is the first 8 hex digits of the SHA-1 of the full path or segment, so the same file always has the same label.

## <repo>.rounds.jsonl, one line per round of checking
Made by rounds.py, which reads each repository's default branch with git show and git log only.
- source: "verdict-file" (a file under reviews/, or research/*-source-check.md or *-entries-check.md) or "dispatch-log" (a verdict record in Service-Desk's dispatch-log/);
- file: the verdict file's path, labelled as above;
- piece: for a verdict file, its folder and file name with any round number (-r1, _round2) removed; for a dispatch record, its item id;
- checker: from the file name (source-check and entries-check files are the source checker; plan-review, build-review and review files are the reviewer; design files are the design reviewer; and so on), or the dispatch record's role; "unknown" where neither says;
- round: the number from a "## Round n" heading or from -rN in the file name, else null;
- verdict: pass, fail, other, or none (no verdict recorded). A file with "## Round n" sections takes each round's verdict from its own "The round's verdict was …" or "Verdict: …" line. Where the last section has none, it takes the file's first "Verdict:" line, coded pass-from-file or fail-from-file; earlier sections without one are none;
- date: for a section, the commit date of the first commit that added its "## Round n" heading; otherwise the date the file was first added; for a dispatch record, its own time (all UTC);
- record: for a dispatch record, the record it names, labelled as above.

No text from the records is included.
