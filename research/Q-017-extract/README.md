# Extract for research question Q-017

Made by the Orchestrator on 2026-11-09 with extract.py (this folder), run with the owner's configured git address as its argument (used only for classing, and not written), from full clones of shumpmaster/Service-Desk, shumpmaster/Model-Lab and shumpmaster/Personal-Org-Operating-Model at origin/main. The clones were shallow until 2026-11-09 and were deepened to the full history first.

No commit subjects or messages are included. All dates are UTC.

## <repo>.commits.jsonl, one line per commit reachable from the default branch
- hash, parents (two for a merge), author_date, commit_date, author, committer;
- author_class: "agent" for an address ending in agents.invalid; "owner" for the GitHub account shumpmaster and the addresses it uses; "other" for anything else (for example a GitHub Actions bot, or a tool's default identity). Addresses are not written;
- kind: "merge-pr" (a merge commit that GitHub committed for a pull request, recognised by GitHub as committer and a subject that starts "Merge pull request #n" or ends "(#n)"), "other-merge" (any other merge commit, including local merges whose subject names a pull request), or "plain". A single-parent commit is always plain, even one committed by GitHub whose subject names a pull request (as a squash merge would be); none of the plain commits committed by GitHub names a pull request today;
- pr: the pull request number for merge-pr, else null;
- revert: true if the subject starts "Revert"; a revert worded otherwise is not found;
- mentions_prs: other pull request numbers the subject names;
- co_author_classes: the class of each Co-authored-by trailer;
- files: each changed path with its status (added, modified or deleted, from git's name-status) and its added and removed line counts (null for a binary file). Merge commits list no files. Renames show as a deletion and an addition, so a moved file gets a new label.

## <repo>.prs.jsonl, one line per pull request merged into the default branch
- pr, merged_at (the merge commit's commit date), merge_commit, merge_commit_author and its class. For these merges, which GitHub committed, the author is the account that merged the pull request; for a merge made by a workflow, that account is the workflow's bot;
- commits: the commits reachable from the merge commit's second parent and not from its first (the pull request's own commits);
- commit_author_classes: the count of those commits by author class; co_author_classes;
- files: the union of those commits' paths, with summed line counts.

## Labels in place of paths
Paths under questions/, decisions/, docs/projects/, ideas/ or sessions/chief-of-staff/, docs/PROJECT.md, and any file ending -notes.md, are shown as <questions:id>, <decisions:id>, <project-plan:id>, <ideas:id>, <cos-session:id> or <notes:id>. Paths under docs/handoff/, and any path containing chief-of-staff, are shown as <cos-handoff:id>. Any path segment that contains a project item's id (P and three digits, with or without a hyphen, in either case) or the word widget is shown as item-<id>. Each id is the first 8 hex digits of the SHA-1 of the full path or segment, so the same file always has the same label.
