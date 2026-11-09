# Q-017 memo: who makes, merges and changes again the organisation's changes, as of 2026-11-09 (Researcher, 2026-11-09)

*The Researcher's memo for Q-017 on brief 229 (docs/briefs/229-researcher.md), 2026-11-09, recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p) from the helper's return, less its closing note to the Orchestrator; only this italic line is the Orchestrator's. Its figures stay unconfirmed until the Source checker has rerun them (research/Q-017-source-check.md).*

The extract has 447 merged pull requests: 312 in Service-Desk, 85 in Model-Lab and 50 in Personal-Org-Operating-Model (POOM). They change 322,755, 87,968 and 109,461 lines. Agent identities wrote 94.2%, 98.9% and 97.8% of plain commits. The owner's identity wrote 5.8%, 1.1% and 2.2%. No commit has a co-author trailer. The owner's account merged 226 of 312 pull requests (72.4%) in Service-Desk, and a workflow bot merged the other 86 (27.6%). The owner's account merged all 85 in Model-Lab and all 50 in POOM. The share of pull requests with at least one commit under the owner's identity is 48/312 (15.4%), 6/85 (7.1%) and 16/50 (32.0%). Files first added with a question label: 540, 82 and 29. Files first added with a decision label: 78, 1 and 1. No commit is marked revert. Within 14 days, a later merged pull request changed at least one of the same files (by-design files left out) for 202/312, 42/85 and 33/50 pull requests. A later commit named the pull request within 14 days for 37, 17 and 6. All 447 were merged less than 60 days before 2026-11-09, so no 60-day window is complete. Every figure here is counted from the extract (grade A) unless it is marked otherwise.

## 1. Units

**Rules.**
- A pull request is one line of a repository's pull-request file. Its month is the month of merged_at (UTC).
- Each changed path is put into one kind, checking the rules below in order, first match wins:
  - **owner question or answer:** question or decision labels.
  - **records:** session, handoff and notes labels; review records; dispatch logs; status, digest, queue, triage and intake records; briefs, reports, handover, trial, archive, checkpoint and audit documents; build screenshots and design audits; and the ledger, digest, lessons, improvement register, progress, changelog and version files.
  - **built work:** the shipped template and kit folders (POOM's product). These are checked before records, so a ledger template inside a kit counts as built.
  - **research:** research questions, memos and checks; research docs; the facts and patterns library; experiments; design reference images.
  - **plan or spec:** specs, project-plan and idea labels, proposals, sprint plans, gate cases, other design files, mission and scope.
  - **built work (rest):** source, tests, tools, scripts, CI and agent definitions, check code, ignore files, and any code or config extension (.py .js .mjs .sh .yml .yaml .toml .json .css .woff2).
  - **other:** everything left, mainly rule and guidance prose such as the agents file, readmes, the operating-model text, governance prose, glossary and setup.
- A pull request is counted under every kind it touches. It is flagged when it touches more than one.
- Changed lines are added plus removed. Binary files count 0 lines; Service-Desk has 525 binary entries.

**Pull requests per month: count (changed lines)**
- Service-Desk:
  - 2026-09: 1 (15,305)
  - 2026-10: 245 (289,165)
  - 2026-11: 66 (18,285)
- Model-Lab:
  - 2026-11: 85 (87,968)
- POOM:
  - 2026-09: 10 (57,938)
  - 2026-10: 28 (42,078)
  - 2026-11: 12 (9,445)

**By kind.** Each entry is: pull requests touching the kind / lines in that kind's files / single-kind pull requests (their lines). All A.

| Kind | Service-Desk | Model-Lab | POOM |
|---|---|---|---|
| built | 90 / 188,888 / 1 (7) | 8 / 20,554 / 0 | 26 / 64,836 / 0 |
| plan or spec | 100 / 60,698 / 7 (657) | 19 / 2,690 / 0 | 31 / 18,902 / 1 (2) |
| research | 29 / 6,634 / 1 (74) | 21 / 42,423 / 0 | 5 / 431 / 0 |
| records only | 173 / 49,382 / 21 (796) | 62 / 18,331 / 16 (2,833) | 49 / 21,168 / 11 (112) |
| owner question/answer | 204 / 14,803 / 107 (4,792) | 54 / 3,730 / 18 (1,084) | 22 / 1,283 / 0 |
| other | 22 / 2,350 / 0 | 4 / 240 / 1 (9) | 19 / 2,841 / 0 |
| flagged (more than one kind) | 175 | 50 | 38 |

**Commits.** The extract lists each pull request's commits, and no commit appears in two pull requests. Local merge commits ("other-merge") are counted apart from the work they bring in. That work is counted through its plain commits.

| | Service-Desk | Model-Lab | POOM |
|---|---|---|---|
| plain commits in a merged pull request (lines) | 1,648 (322,755) | 844 (87,968) | 827 (109,461) |
| plain commits on the default branch in no merged pull request (lines) | 434 (85,303) | 4 (20,915) | 1 (1) |
| other-merge commits inside a pull request | 291 | 38 | 70 |
| other-merge commits outside any pull request | 73 | 0 | 0 |

- Service-Desk's 434 commits outside any pull request: 375 have an agent author and 59 the owner's identity. 356 touch records, 116 research, 49 owner question/answer files, 1 plan and 1 other.
- Of Service-Desk's 73 local merges outside pull requests, 1 names a merged pull request.

**What the extract cannot show here.**
- Whether the path-to-kind rule matches what the work was for.
- Pull request titles.
- Pull requests closed without merging. In the numbering, 29 Service-Desk numbers and 1 POOM number have no merged line. They may be closed pull requests, issues, or merges made another way; the extract cannot say which.

## 2. Who made and merged each change

**Rule.** The extract's author_class is used as given.
- A pull request's commits are classed by author, other-merge commits included. A second view counts plain commits only.
- The account that merged a pull request is the author of its merge commit.
- The "other" names are kept as a separate class. Shares are given both ways: with "other" counted as not an agent, and with it counted as an agent.

**Names (commit counts), A.**
- **Agent class:**
  - Service-Desk: orchestrator 1,100; chief-of-staff 484; builder 476; definer 207; source-checker 28.
  - Model-Lab: orchestrator 474; chief-of-staff 354; definer 23; builder 18; check-author 7.
  - POOM: orchestrator 704; tools-builder 159.
- **Owner class:** shumpmaster. Service-Desk 346 (226 merges, 120 plain); Model-Lab 94 (85, 9); POOM 68 (50, 18).
- **Other class:**
  - github-actions[bot]: 86 in Service-Desk, all pull-request merges.
  - "Claude" (a tool's default identity): Service-Desk 31, Model-Lab 1, POOM 17. Every one is an other-merge commit.
- "Claude" is also the committer on 684, 6 and 25 agent-authored commits.
- Committer names besides "Claude": GitHub, orchestrator, chief-of-staff, builder, definer, check-author, tools-builder.
- All 147 plain commits under the owner's identity have GitHub as committer and change exactly one file:
  - Service-Desk: 72 records added, 46 question/answer files added, 1 built file modified, 1 other added.
  - Model-Lab: 5 records added, 1 record modified, 2 question/answer files added, 1 other added.
  - POOM: 17 records added, 1 other added.

**Per pull request, A.**

| | Service-Desk (312) | Model-Lab (85) | POOM (50) |
|---|---|---|---|
| agent commits only | 259 | 78 | 32 |
| agent + owner | 45 | 6 | 15 |
| agent + other | 5 | 1 | 2 |
| agent + other + owner | 3 | 0 | 1 |
| with an owner-identity commit | 48 (15.4%) | 6 (7.1%) | 16 (32.0%) |
| without one | 264 (84.6%) | 79 (92.9%) | 34 (68.0%) |
| all-agent, "other" counted as not agent | 259 (83.0%) | 78 (91.8%) | 32 (64.0%) |
| all-agent, "other" counted as agent | 264 (84.6%) | 79 (92.9%) | 34 (68.0%) |

- Changed lines by commit-author group in Service-Desk: agent only 155,242; agent + owner 137,599; agent + other 1,697; agent + other + owner 28,217. Model-Lab: 73,170; 11,124; 3,674. POOM: 34,073; 39,893; 33,067; 2,428.
- Counting plain commits only, the split is agent-only versus agent + owner: 264/48, 79/6 and 34/16.
- No pull request has a co-author class.

**Merging account, A.**
- Service-Desk:
  - Owner's account: 226 (72.4%). 48 of these have an owner commit and 178 do not.
  - github-actions[bot]: 86 (27.6%), none with an owner commit.
- Model-Lab: owner's account 85 (100%): 6 with an owner commit, 79 without.
- POOM: owner's account 50 (100%): 16 with an owner commit, 34 without.
- Merges made outside GitHub (other-merge):
  - Service-Desk 364: 333 agent-authored, 31 "Claude".
  - Model-Lab 38: 37 agent, 1 "Claude".
  - POOM 70: 53 agent, 17 "Claude".

**Commit level, A.**
- Plain commits:
  - Service-Desk: agent 1,962 (94.2%, 407,360 lines); owner 120 (5.8%, 698 lines).
  - Model-Lab: agent 839 (98.9%, 108,845 lines); owner 9 (1.1%, 38 lines).
  - POOM: agent 810 (97.8%, 109,425 lines); owner 18 (2.2%, 37 lines).
- All commits:
  - Service-Desk: agent 83.2%, owner 12.5%, other 4.2%.
  - Model-Lab: 90.2%, 9.7%, 0.1%.
  - POOM: 91.0%, 7.2%, 1.8%.
- Leaving out pull-request merge commits:
  - Service-Desk: 93.8%, 4.9%, 1.3%.
  - Model-Lab: 98.9%, 1.0%, 0.1%.
  - POOM: 96.1%, 2.0%, 1.9%.

**When the agents.invalid convention starts, A.** In each repository exactly one non-agent commit comes first, under the owner's identity.

| | First agents.invalid commit | Owner plain commits after it |
|---|---|---|
| Service-Desk | 2026-09-30T19:04:45Z | 119 |
| Model-Lab | 2026-11-01T16:58:40Z | 8 |
| POOM | 2026-09-24T14:59:13Z | 17 |

**What the extract cannot show.**
- Who actually did the work. An identity is not proof of it.
- Whether owner-identity commits were typed by the owner or made by a session using the owner's settings. All are single-file commits that GitHub committed.
- Who is behind the "Claude" identity.
- Who started each workflow-bot merge.

## 3. Questions put to the owner

**Rule.**
- Each labelled file's events are sorted by commit_date.
- A file is counted once, at its first "added". Later "added" events are re-additions.
- A file belongs to a pull request when its first-adding commit is in that pull request's commit list.
- Matching rule (an estimate): a unit (a merged pull request, or a plain commit outside every pull request) that first-adds a decision file and also deletes a question file is a candidate match.
- Moves are estimated as a question file deleted and another added in the same commit with equal line counts.

**Figures, A unless marked.**

| | Service-Desk | Model-Lab | POOM |
|---|---|---|---|
| Question files first added | 540 (Sep 1, Oct 494, Nov 45) | 82 (all Nov) | 29 (Sep 17, Oct 6, Nov 6) |
| re-additions | 3 | 3 | 0 |
| deletions | 189 | 41 | 27 |
| still present at the end | 351 | 44 | 2 |
| first-added through merged pull requests | 516 in 175 pull requests | 79 in 48 | 29 in 12 |
| first-added outside any pull request | 24 | 3 | 0 |
| first-adding commit by agent / owner identity | 518 / 22 | 80 / 2 | 29 / 0 |
| Decision files first added | 78 (Sep 1, Oct 49, Nov 28) | 1 (Nov) | 1 (Sep) |
| re-additions | 0 | 0 | 0 |
| deletions | 1 | 0 | 0 |
| first-added through merged pull requests | 52 in 26 pull requests | 0 | 1 in 1 |
| first-added outside any pull request | 26 | 1 | 0 |
| first-adding commit by agent / owner identity | 54 / 24 | 1 / 0 | 1 / 0 |

- Service-Desk pull requests by number of question files they first add: none 137; one 99; two 37; three 8; four 11; then one or a few each at 5–22; one pull request adds 75.
- Model-Lab: none 37; one 31; two 11; three 2; four 2; five 1; seven 1.
- POOM: none 38; one 6; two 4; six 1; nine 1.

**Matching questions to answers (estimate).**

| | Service-Desk | Model-Lab | POOM |
|---|---|---|---|
| Units that add a decision and delete a question | 3 (2 one-to-one; 3 decisions, 4 questions) | 0 | 0 |
| Units that add a decision and delete no question | 49 | 1 | 1 |
| Units that delete a question and add no decision | 78 | 29 | 12 |
| Probable moves of question files (estimated) | 7 | 0 | 1 |

A move shows as one deletion plus a first addition, so it can inflate first additions.

**What the extract cannot show.**
- Labels are opaque, so a question cannot be matched to its answer, except by the weak same-unit test above.
- Whether a question was ever shown to the owner.
- Who wrote an answer.
- Decisions given in conversation.

## 4. Merged changes later reverted or changed again

**Rule.** For each pull request, three tests are run for windows of 14, 30 and 60 days after merged_at. A later commit falls in a window by commit_date; a later pull request by merged_at.
- **Revert:** a commit marked revert.
- **Named:** a later commit whose mentions_prs includes the pull request's number.
- **File overlap:** a later merged pull request that shares at least one file. This is a coarse test, because the extract has no line-level history.
- **Left out of the overlap test** (files edited in turn by design), counted as distinct files in pull requests:
  - Service-Desk 71 of 2,622: session records 30, handoff records 27, ledgers/registers/logs/changelog/version 6, digests 4, generated files 2, status records 1, notes 1.
  - Model-Lab 51 of 685: handoff 19, generated (the extract's own earlier versions and lockfiles) 15, session 12, digests 3, ledgers 2.
  - POOM 8 of 575: ledgers etc. 5, digests 3.
- After those are left out, 14, 9 and 11 pull requests have no file left to test.
- Supplementary test: overlap with later plain commits outside every pull request.
- A window counts as complete when merged_at plus the window is no later than 2026-11-09T00:00Z.

**Reverts, A.** No commit in any repository is marked revert, so the count is 0 in every window.

**Named and overlap counts, A.**

| Window | Group | n | Named | Overlap with a later pull request | Named or overlap | Overlap with a later commit outside pull requests |
|---|---|---|---|---|---|---|
| **Service-Desk** | | | | | | |
| 14 days | complete | 230 | 30 | 159 | 167 | 12 |
| 14 days | incomplete | 82 | 7 | 43 | 45 | 1 |
| 30 days | complete | 53 | 5 | 38 | 40 | 12 |
| 30 days | incomplete | 259 | 36 | 165 | 175 | 1 |
| 60 days | all incomplete | 312 | 41 | 203 | 215 | 13 |
| **Model-Lab** (every window incomplete) | | | | | | |
| 14, 30 and 60 days | incomplete | 85 | 17 | 42 | 52 | 0 |
| **POOM** | | | | | | |
| 14 days | complete | 38 | 6 | 26 | 26 | 0 |
| 14 days | incomplete | 12 | 0 | 7 | 7 | 0 |
| 30 days | complete | 23 | 2 | 14 | 14 | 0 |
| 30 days | incomplete | 27 | 4 | 19 | 19 | 0 |
| 60 days | all incomplete | 50 | 6 | 33 | 33 | 0 |

- Pull requests merged less than 60 days before 2026-11-09: 312/312, 85/85 and 50/50.
- Of the numbers in mentions_prs, 148/148, 44/44 and 52/53 equal a merged pull-request number in the same repository. Even so, a number may refer to an issue or to another repository's pull request.

**What the extract cannot show.**
- Reverts worded any other way.
- Fixes that name nothing.
- Whether a shared file means a change to the same lines.
- Whether a mention is a fix or only a record, such as filing a review.
- Whether the earlier change was at fault.

## 5. What the records cannot show (limits on every figure above)

- Decisions, approvals and reviews given in conversation, or in pull-request reviews and comments. These are not in the extract.
- Pull-request titles, and pull requests closed without merging.
- The owner's time.
- Work dropped before any commit.
- Fixes that do not name what they fix.

**Where the extract's coding may be wrong:**
- Labelling is by path pattern. A path anywhere under a question or decision folder gets that label, so template copies would count as owner questions. Any path containing the chief-of-staff role name becomes a handoff label, so an agent-definition file for that role would be classed as a record.
- A rename shows as a delete plus an add, so moved files count as new.
- The owner class rests partly on an author-name match.
- A revert is found only by the subject prefix "Revert".
- mentions_prs takes any "#n" in a subject.
- A pull request merged by a local merge, not by GitHub, has no pull-request line.
- Author date differs from commit date on 86, 43 and 18 commits (Service-Desk, Model-Lab, POOM). All dating here uses commit_date.
- Binary files count no lines.
- The Model-Lab records contain earlier versions of this extract.

**What it would take to measure better:** pull-request metadata and review records, line-level history for each changed file, revert detection from the message body, and the conversation logs where decisions were given.

## Script (run as `python3 -I q017.py <extract folder>`; it reads only the extract)

```python
# Q-017 counts. Reads only the extract folder. Run: python3 -I q017.py <extract folder>
import json, collections, datetime as dt, sys
D=sys.argv[1].rstrip("/")+"/"   # the extract folder
REPOS=["Service-Desk","Model-Lab","Personal-Org-Operating-Model"]
REF=dt.datetime(2026,11,9,tzinfo=dt.timezone.utc)   # question's "as of" date, 00:00 UTC
def T(s): return dt.datetime.strptime(s,"%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
CODE_EXT=(".py",".js",".mjs",".sh",".yml",".yaml",".toml",".json",".jsonl.lock",".woff2",".css")
REC_FILES={"docs/LEDGER.md","docs/DIGEST.md","docs/LESSONS.md","docs/CHECKPOINT.md",
  "docs/IMPROVEMENT_REGISTER.md","docs/sprints/PROGRESS.md","CHANGELOG.md","VERSION","docs/design/JOIN_UP_REVIEW.md"}
def kind(p):
    if p.startswith(("<questions:","<decisions:")): return "owner_qa"
    if p.startswith(("<cos-session:","<cos-handoff:","<notes:")): return "records"
    if p.startswith(("<project-plan:","<ideas:")): return "plan"
    if p.startswith(("template/","template-v3/","portfolio-template/")): return "built"
    if p.startswith("reviews/"): return "records"
    if p.startswith(("dispatch-log/","status/","digest/","queue/","triage/","intake/")): return "records"
    if p.startswith(("docs/briefs/","docs/reports/","docs/handover/","docs/trials/","docs/archive/",
                     "docs/checkpoints/","docs/audit/","docs/design/builds/","docs/design/audits/",
                     "docs/design/audit-","docs/design/inventory-")) or p in REC_FILES: return "records"
    if p.startswith(("research/","docs/research/","library/","experiments/","docs/design/references/")): return "research"
    if p.startswith(("specs/","docs/proposals/","docs/sprints/","docs/gates/","docs/design/")) \
       or p in ("docs/MISSION.md","docs/SCOPE.md"): return "plan"
    if p.startswith(("src/","tests/","tools/","scripts/",".github/",".claude/","governance/checks/")) \
       or p==".gitignore" or p.endswith(CODE_EXT) or p=="governance/OPERATING_MODEL_VERSION": return "built"
    return "other"
# files edited in turn by design, left out of the file-overlap test (item 4)
def by_design(p):
    if p.startswith("<cos-session:"): return "session records"
    if p.startswith("<cos-handoff:"): return "handoff records"
    if p.startswith("<notes:"): return "notes"
    if p.startswith("dispatch-log/"): return "dispatch logs"
    if p.startswith("status/"): return "status records (generated/updated each run)"
    if p.startswith("digest/") or p=="docs/DIGEST.md": return "digests"
    if p in ("docs/LEDGER.md","docs/LESSONS.md","docs/IMPROVEMENT_REGISTER.md","docs/CHECKPOINT.md",
             "docs/sprints/PROGRESS.md","docs/audit/CLAIMS_REGISTER.md","intake/estimates.jsonl","CHANGELOG.md","VERSION"):
        return "ledgers, registers, logs, changelog and version"
    if p.startswith("research/Q-017-extract/") or p.endswith("package-lock.json"): return "generated files"
    return None
KINDS=["built","plan","research","records","owner_qa","other"]
def lines(f): return (f["added"] or 0)+(f["removed"] or 0)
def pct(a,b): return f"{a}/{b} ({100*a/b:.1f}%)" if b else f"{a}/0"
OUT=[]
def pr_(*a): print(*a)
G=collections.Counter()
for r in REPOS:
    C=[json.loads(l) for l in open(D+r+".commits.jsonl")]
    P=[json.loads(l) for l in open(D+r+".prs.jsonl")]
    H={c["hash"]:c for c in C}
    order={c["hash"]:i for i,c in enumerate(reversed(C))}   # git log order reversed = oldest first
    P.sort(key=lambda p:p["merged_at"])
    inpr={}
    for p in P:
        for h in p["commits"]: inpr[h]=p["pr"]
    pr_("\n"+"="*30,r,"commits",len(C),"merged PRs",len(P))
    # ---------- 1. units
    pr_("\n[1] PRs per month of merged_at (count / changed lines)")
    m=collections.Counter(); ml=collections.Counter()
    for p in P:
        k=p["merged_at"][:7]; m[k]+=1; ml[k]+=sum(lines(f) for f in p["files"])
    for k in sorted(m): pr_("  ",k,m[k],ml[k])
    pr_("   total",len(P),sum(ml.values()))
    kc=collections.Counter(); kl=collections.Counter(); kpl=collections.Counter(); single=collections.Counter(); singlel=collections.Counter()
    nmulti=0; combos=collections.Counter()
    for p in P:
        ks=collections.Counter()
        for f in p["files"]: ks[kind(f["path"])]+=lines(f)
        ks_set=set(ks) if p["files"] else {"(no files)"}
        tot=sum(ks.values())
        for k in ks_set: kc[k]+=1; kl[k]+=ks.get(k,0); kpl[k]+=tot
        if len(ks_set)>1: nmulti+=1
        else: single[next(iter(ks_set))]+=1; singlel[next(iter(ks_set))]+=tot
        combos[tuple(sorted(ks_set))]+=1
    pr_("   by kind (PRs counted under each kind they touch; lines in that kind's files; lines of those PRs in total)")
    for k in KINDS+["(no files)"]:
        if kc[k] or single[k]: pr_(f"     {k:9s} PRs {kc[k]:4d} lines_in_kind {kl[k]:7d} pr_total_lines {kpl[k]:7d} | single-kind PRs {single[k]} lines {singlel[k]}")
    pr_("   flagged (more than one kind):",nmulti,"of",len(P))
    pr_("   commonest kind combinations:",combos.most_common(6))
    # commits outside merged PRs
    out=[c for c in C if c["hash"] not in inpr and c["kind"]=="plain"]
    om_in=[c for c in C if c["kind"]=="other-merge" and c["hash"] in inpr]
    om_out=[c for c in C if c["kind"]=="other-merge" and c["hash"] not in inpr]
    pl_in=[c for c in C if c["kind"]=="plain" and c["hash"] in inpr]
    pr_("\n[1] commits: merge-pr",sum(c["kind"]=="merge-pr" for c in C),
        "| plain in a merged PR",len(pl_in),"lines",sum(lines(f) for c in pl_in for f in c["files"]),
        "| plain in no merged PR",len(out),"lines",sum(lines(f) for c in out for f in c["files"]),
        "| other-merge inside a PR",len(om_in),"| other-merge outside any PR",len(om_out))
    pr_("    plain-in-no-PR by month",sorted(collections.Counter(c["commit_date"][:7] for c in out).items()),
        "by author class",dict(collections.Counter(c["author_class"] for c in out)))
    okind=collections.Counter(); 
    for c in out:
        for k in {kind(f["path"]) for f in c["files"]}: okind[k]+=1
    pr_("    plain-in-no-PR commits touching each kind",dict(okind))
    # outside-PR commits: are they after the last merge (pending) ?
    lastm=P[-1]["merged_at"]
    pr_("    plain-in-no-PR committed after the last merged PR:",sum(c["commit_date"]>lastm for c in out))
    pr_("    binary file entries (null line counts):",sum(1 for c in C for f in c["files"] if f["added"] is None))
    # ---------- 2. who
    pr_("\n[2] identities (author names by class; committer names)")
    names=collections.defaultdict(collections.Counter)
    for c in C: names[c["author_class"]][c["author"]]+=1
    for k in names: pr_("   ",k,dict(names[k]))
    pr_("    committers",dict(collections.Counter(c["committer"] for c in C)))
    pr_("    'other' authors by commit kind",dict(collections.Counter((c["author"],c["kind"]) for c in C if c["author_class"]=="other")))
    pr_("    agent-authored commits whose committer is 'Claude'",sum(1 for c in C if c["author_class"]=="agent" and c["committer"]=="Claude"))
    fa=min(c["commit_date"] for c in C if c["author_class"]=="agent")
    pr_("    first agents.invalid commit",fa,"| non-agent commits before it",sum(1 for c in C if c["commit_date"]<fa and c["author_class"]!="agent"),
        "| owner plain commits after it",sum(1 for c in C if c["commit_date"]>=fa and c["author_class"]=="owner" and c["kind"]=="plain"))
    # per PR
    cat=collections.Counter(); catl=collections.Counter()
    any_owner=any_other=0; plain_only=collections.Counter()
    merger=collections.Counter(); merger_x=collections.Counter()
    for p in P:
        cc=collections.Counter(H[h]["author_class"] for h in p["commits"])
        pc=collections.Counter(H[h]["author_class"] for h in p["commits"] if H[h]["kind"]=="plain")
        lab="+".join(sorted(cc)); cat[lab]+=1; catl[lab]+=sum(lines(f) for f in p["files"])
        if cc["owner"]: any_owner+=1
        if cc["other"]: any_other+=1
        plain_only["+".join(sorted(pc)) or "(none)"]+=1
        merger[(p["merge_commit_author"],p["merge_commit_author_class"])]+=1
        merger_x[(p["merge_commit_author"],"has owner commit" if cc["owner"] else "no owner commit")]+=1
    n=len(P)
    pr_("    PRs by author classes of their commits (incl. other-merge):",dict(cat),"lines",dict(catl))
    pr_("    PRs by author classes of their plain commits only:",dict(plain_only))
    pr_("    PRs with >=1 owner-identity commit",pct(any_owner,n),"| without",pct(n-any_owner,n))
    pr_("    PRs with >=1 'other' commit",pct(any_other,n),
        "| all-agent if 'other' counted as non-agent:",pct(cat.get("agent",0),n),
        "| all-agent if 'other' counted as agent:",pct(sum(v for k,v in cat.items() if "owner" not in k),n))
    pr_("    co-author classes on PRs:",dict(collections.Counter(tuple(p["co_author_classes"]) for p in P)))
    pr_("    merging account:",{f"{a} ({b})":pct(v,n) for (a,b),v in merger.items()})
    pr_("    merging account x owner commit:",dict(merger_x))
    pr_("    other-merge commits (merges outside GitHub):",len(om_in)+len(om_out),"by author",dict(collections.Counter((c["author"],c["author_class"]) for c in om_in+om_out)),
        "by committer",dict(collections.Counter(c["committer"] for c in om_in+om_out)))
    # commit level
    pls=[c for c in C if c["kind"]=="plain"]
    pr_("    commit level, plain commits by class:",{k:pct(v,len(pls)) for k,v in collections.Counter(c["author_class"] for c in pls).items()},
        "lines",dict(collections.Counter({k:0 for k in []}) or {k:sum(lines(f) for c in pls if c["author_class"]==k for f in c["files"]) for k in {c["author_class"] for c in pls}}))
    pr_("    commit level, all commits by class:",{k:pct(v,len(C)) for k,v in collections.Counter(c["author_class"] for c in C).items()},
        "| excluding merge-pr commits:",{k:pct(v,len(C)-n) for k,v in collections.Counter(c["author_class"] for c in C if c["kind"]!="merge-pr").items()})
    pr_("    plain commits in a PR by class",dict(collections.Counter(c["author_class"] for c in pl_in)),
        "| plain commits in no PR by class",dict(collections.Counter(c["author_class"] for c in out)))
    # ---------- 3. questions / decisions
    pr_("\n[3] owner questions and decisions")
    ev=collections.defaultdict(list)   # path -> [(date,ord,status,hash)]
    for c in C:
        for f in c["files"]:
            if f["path"].startswith(("<questions:","<decisions:")):
                ev[f["path"]].append((c["commit_date"],order[c["hash"]],f["status"],c["hash"],f))
    first={}; readd=collections.Counter(); deletes=collections.Counter(); present=collections.Counter()
    firstadd_commits={}
    for p_,es in ev.items():
        es.sort(); lab=p_[1:p_.index(":")]
        adds=[e for e in es if e[2]=="added"]
        if adds:
            first[p_]=adds[0]; firstadd_commits.setdefault(adds[0][3],[]).append(p_)
            readd[lab]+=len(adds)-1
        else: readd[lab+"_never_added_in_extract"]+=1
        deletes[lab]+=sum(e[2]=="deleted" for e in es)
        if es[-1][2]!="deleted": present[lab]+=1
    for lab in ("questions","decisions"):
        fs=[(p_,e) for p_,e in first.items() if p_.startswith("<"+lab)]
        pr_(f"   {lab}: files first added {len(fs)}; per month",sorted(collections.Counter(e[0][:7] for _,e in fs).items()),
            "; re-additions",readd[lab],"; deletions",deletes[lab],"; present at end",present[lab],
            "; touched but never added",readd[lab+"_never_added_in_extract"])
        viapr=collections.Counter(inpr.get(e[3]) for _,e in fs)
        npr=sum(1 for k in viapr if k is not None)
        pr_(f"     first-added through a merged PR: {sum(v for k,v in viapr.items() if k is not None)} files in {npr} PRs (of {len(P)}); outside any merged PR: {viapr.get(None,0)}")
        dist=collections.Counter(viapr[p['pr']] for p in P)
        pr_("     PRs by number of first-added files:",sorted(dist.items()))
    # moves: same commit deletes a question file and adds one with equal line count
    mv=0; mvd=0
    for c in C:
        dq=[f for f in c["files"] if f["path"].startswith("<questions:") and f["status"]=="deleted"]
        aq=[f for f in c["files"] if f["path"].startswith("<questions:") and f["status"]=="added"]
        used=set()
        for d in dq:
            for i,a in enumerate(aq):
                if i not in used and a["added"]==d["removed"]: used.add(i); mv+=1; break
        dd=[f for f in c["files"] if f["path"].startswith("<decisions:") and f["status"]=="deleted"]
        ad=[f for f in c["files"] if f["path"].startswith("<decisions:") and f["status"]=="added"]
        u2=set()
        for d in dd:
            for i,a in enumerate(ad):
                if i not in u2 and a["added"]==d["removed"]: u2.add(i); mvd+=1; break
    pr_("   probable moves (same commit: one deleted, one added, equal line counts): questions",mv,"decisions",mvd)
    # matching: units (PR, or commit outside PRs) that add a decision and delete a question
    units=[("pr",p["pr"],p["commits"]) for p in P]+[("commit",c["hash"][:8],[c["hash"]]) for c in out]
    both=one2one=dec_only=q_del_only=0; dec_in_both=q_in_both=0
    for typ,idn,hs in units:
        qd=sum(1 for h in hs for f in H[h]["files"] if f["path"].startswith("<questions:") and f["status"]=="deleted")
        da=sum(1 for h in hs if h in firstadd_commits for p_ in firstadd_commits[h] if p_.startswith("<decisions:"))
        if qd and da:
            both+=1; dec_in_both+=da; q_in_both+=qd
            if qd==1 and da==1: one2one+=1
        elif da: dec_only+=1
        elif qd: q_del_only+=1
    pr_("   units (merged PRs + plain commits in no PR) that first-add a decision AND delete a question:",both,
        f"(1:1 {one2one}; decisions in them {dec_in_both}, questions deleted in them {q_in_both})",
        "| first-add decision, no question deleted:",dec_only,"| delete question, no decision added:",q_del_only)
    # ---------- 4. later change
    pr_("\n[4] later changes")
    excl=collections.defaultdict(set)
    for p in P:
        for f in p["files"]:
            b=by_design(f["path"])
            if b: excl[b].add(f["path"])
    pr_("   left out (distinct files):",{k:len(v) for k,v in excl.items()},"total",sum(len(v) for v in excl.values()),
        "of",len({f["path"] for p in P for f in p["files"]}))
    FS={p["pr"]:{f["path"] for f in p["files"] if not by_design(f["path"])} for p in P}
    mention=collections.defaultdict(list)
    prnums={p["pr"] for p in P}
    allm=[x for c in C for x in c["mentions_prs"]]
    pr_("   mentions_prs numbers:",len(allm),"of which a merged PR number in this repo:",sum(x in prnums for x in allm))
    for c in C:
        for x in c["mentions_prs"]: mention[x].append(c)
    for W in (14,30,60):
        res=collections.Counter()
        for p in P:
            t0=T(p["merged_at"]); t1=t0+dt.timedelta(days=W); comp=t1<=REF
            ov=any(FS[p["pr"]]&FS[q["pr"]] for q in P if t0<T(q["merged_at"])<=t1)
            ovd=any(FS[p["pr"]]&{f["path"] for f in c["files"]} for c in out if t0<T(c["commit_date"])<=t1)
            nm=any(t0<T(c["commit_date"])<=t1 for c in mention[p["pr"]])
            rv=any(c["revert"] and t0<T(c["commit_date"])<=t1 for c in C)
            for tag,cond in (("all",True),("complete" if comp else "incomplete",True)):
                res[(tag,"n")]+=1
                res[(tag,"overlap_later_PR")]+=ov; res[(tag,"overlap_direct_commit")]+=ovd
                res[(tag,"named")]+=nm; res[(tag,"revert")]+=rv; res[(tag,"overlap_PR_or_named")]+=(ov or nm)
                res[(tag,"no_checked_files")]+=(not FS[p["pr"]])
        for tag in ("all","complete","incomplete"):
            if res[(tag,"n")]:
                pr_(f"   {W}d {tag:10s} n={res[(tag,'n')]:3d} revert={res[(tag,'revert')]} named={res[(tag,'named')]} "
                    f"overlap_laterPR={res[(tag,'overlap_later_PR')]} overlap_or_named={res[(tag,'overlap_PR_or_named')]} "
                    f"overlap_direct_commit={res[(tag,'overlap_direct_commit')]} prs_with_no_checked_files={res[(tag,'no_checked_files')]}")
    pr_("   PRs merged < 60 days before",REF.date(),":",sum(T(p["merged_at"])>REF-dt.timedelta(days=60) for p in P),"of",len(P))
    # ---------- extra checks used in the memo
    pr_("\n[extra]")
    pr_("   owner plain commits: committers",dict(collections.Counter(c["committer"] for c in pls if c["author_class"]=="owner")),
        "files per commit",dict(collections.Counter(len(c["files"]) for c in pls if c["author_class"]=="owner")),
        "kind/status of their files",dict(collections.Counter((kind(f["path"]),f["status"]) for c in pls if c["author_class"]=="owner" for f in c["files"])))
    pr_("   other-merge commits outside any PR that name a merged PR:",sum(any(x in prnums for x in c["mentions_prs"]) for c in om_out))
    nums=sorted(prnums); pr_("   PR numbers",nums[0],"to",nums[-1],"; numbers in that range with no merged PR line:",len(set(range(nums[0],nums[-1]+1))-prnums))
    pr_("   label files first added, by author class of the adding commit:",
        dict(collections.Counter((p_[1:p_.index(":")],H[e[3]]["author_class"]) for p_,e in first.items())))
```

Total tokens: I cannot see my token count.
