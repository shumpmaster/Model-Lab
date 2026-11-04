#!/usr/bin/env python3
"""E-001 step 1 (records check): machine checks behind RESULT.md's F1 and F2 cells.
For each audited piece: F1, that the work's first commit exists and its first parent is the
start commit named; F2, that each named input exists at the start commit (a glob counts its
matches; zero matches means the glob names nothing). Also prints the cited record lines so a
reader can check each cite. Read-only on the clones. Usage: python3 -I records_check.py"""
import fnmatch, subprocess, json
R = {"SD": "/home/user/Service-Desk", "POOM": "/home/user/Personal-Org-Operating-Model",
     "ML": "/home/user/Model-Lab"}
def git(repo, *a):
    r = subprocess.run(["git", "-C", R[repo], *a], capture_output=True, text=True)
    return r.returncode, r.stdout
def line(repo, rev, path, n):
    rc, out = git(repo, "show", f"{rev}:{path}")
    if rc: return "<missing>"
    ls = out.splitlines()
    return ls[n-1][:160] if 0 < n <= len(ls) else "<no such line>"
DEF = [".claude/agents/definer.md", "docs/PROJECT.md", "library/**", "specs/S-001.md"]
BLD = [".claude/agents/builder.md", "specs/S-001.md", "docs/PROJECT.md", "tests/acceptance/**", "checks/**"]
TB = [".claude/agents/tools-builder.md"]
P = [  # id, repo, start, first work commit(s), named inputs, cites [(rev, path, line)]
 ("SD M3B plan","SD","3bfe663",["31ff26d"],DEF,[("HEAD","reviews/M3B/_plan-critic-r1-verbatim.md",3),("3bfe663","docs/PROJECT.md",113)]),
 ("POOM S-007 plan","POOM","03121f0",["fea44b3"],["governance/SURFACES.md"],[("03121f0","governance/SURFACES.md",4),("03121f0","governance/SURFACES.md",5)]),
 ("SD M3C plan","SD","d2a1d60",["b26e876"],DEF,[("HEAD","reviews/M3C/_plan-review-r1-verbatim.md",5),("d2a1d60","docs/PROJECT.md",117)]),
 ("POOM S-012r plan","POOM","5ee6c05",["84caf74"],["governance/SURFACES.md"],[("HEAD","reviews/7/_plan-review-s012r-round1-verbatim.md",2)]),
 ("SD after-glance plan","SD","2d0edb0",["671eada"],DEF+["decisions/questions/P-001-glance2-anchor.md","decisions/questions/P-001-glance2-arrow.md","decisions/questions/P-001-glance2-counts.md","decisions/questions/P-001-glance2-palette.md","decisions/questions/P-001-glance2-standard.md","docs/design/references/owner-request-2026-10-24-glance-emphasis.md"],[("HEAD","reviews/S-001-after-glance/_plan-critic-r1-verbatim.md",3),("2d0edb0","docs/design/references/owner-request-2026-10-24-glance-emphasis.md",62)]),
 ("POOM S-015 plan","POOM","6c3c9a4",["20f25ca"],["governance/SURFACES.md"],[]),
 ("SD desk-v2 plan","SD","87ce4f0",["a0b472a","2ed4269"],DEF+["decisions/questions/P-001-redesign-direction-v2.md"],[("HEAD","reviews/S-001-desk-v2/_critic-round1-verbatim.md",3),("87ce4f0","decisions/questions/P-001-redesign-direction-v2.md",1)]),
 ("POOM S-022 plan","POOM","30cfbaf",["0c0380a"],["governance/SURFACES.md"],[("HEAD","reviews/S-022/_plan-review-s022-round1-verbatim.md",2)]),
 ("SD HD1 stage","SD","2c20c9a",["a1be3ee"],BLD,[("HEAD","reviews/HD1/_stage-hd1-review-r1-verbatim.md",3),("2c20c9a","specs/S-001.md",3727)]),
 ("POOM S-017 build","POOM","fb6d0c8",["cc7730b"],TB+["specs/S-017-loop-and-alerts.md","docs/LEDGER.md"],[("HEAD","reviews/20/reviewer.md",4),("fb6d0c8","docs/LEDGER.md",1737),("fb6d0c8",".claude/agents/tools-builder.md",23)]),
 ("SD M3B VT3 stage","SD","55a2484",["5d9b0d2"],BLD,[("HEAD","reviews/M3B/_stage-vt3-design-r1-verbatim.md",3),("55a2484","specs/S-001.md",3361)]),
 ("POOM S-023/24 build","POOM","6ba7f05",["6788f25","4f41556"],TB+["specs/S-023-six-phases.md","specs/S-024-phase-gates.md","docs/LEDGER.md"],[("HEAD","reviews/26/reviewer.md",5),("6ba7f05","docs/LEDGER.md",1923),("6ba7f05","docs/LEDGER.md",1938)]),
 ("SD M3E G5 stage","SD","87bac4d",["45e09fa"],BLD,[("HEAD","reviews/M3E/_stage-g5-review-r1-verbatim.md",3),("87bac4d","specs/S-001.md",2590)]),
 ("POOM PR5 build","POOM","450c4dd",["a1ac59d"],TB+["docs/briefs/s-005.md","specs/S-005-governance-follow-ups.md","governance/enforcement.toml","docs/research/003*","docs/LEDGER.md","tools/check_all.sh","tools/surface_guard.py"],[("HEAD","reviews/5/_reviewer-round1-verbatim.md",1),("HEAD","reviews/5/_reviewer-round1-verbatim.md",5)]),
 ("SD M3G QW1 stage","SD","c2f6f94",["5f62cd7"],BLD,[("HEAD","reviews/M3G/_stage-qw1-review-r1-verbatim.md",3),("c2f6f94","specs/S-001.md",2962)]),
 ("POOM S-014 build","POOM","6c3c9a4",["17d4a1e"],TB+["docs/briefs/s-014.md","specs/S-014-session-runner.md","template-v3/governance/PACKS.toml","template-v3/governance/RUNNER.toml","template-v3/governance/BRIEFS.toml","tools/govlib.py","tools/review_check.py"],[("HEAD","reviews/7/_build-review-s014-round1-verbatim.md",2)]),
 ("ML Q-001","ML","3d252f2",["78bdbbc"],[".claude/agents/researcher.md","research/Q-001.md","research/_GROUNDWORK.md","OPERATING_MODEL.md","template-v3/.claude/agents/*","template-v3/governance/BRIEFS.toml","template-v3/governance/PACKS.toml","dispatch-log/**"],[("HEAD","docs/briefs/02-researcher.md",7),("HEAD","docs/briefs/02-researcher.md",11)]),
 ("ML Q-002","ML","c42334b",["d879b98"],[".claude/agents/researcher.md","research/Q-002.md","research/_GROUNDWORK.md","library/**","OPERATING_MODEL.md","template-v3/.claude/agents/*","template-v3/governance/BRIEFS.toml","template-v3/governance/PACKS.toml"],[("671335c","research/Q-002.md",7)]),
 ("ML Q-003","ML","671335c",["c42334b"],[".claude/agents/researcher.md","research/Q-003.md","research/_GROUNDWORK.md","library/**","OPERATING_MODEL.md","template-v3/.claude/agents/*","template-v3/governance/BRIEFS.toml","template-v3/governance/PACKS.toml"],[("671335c","research/Q-003.md",7)]),
 ("ML Q-004","ML","d879b98",["f54d6d7"],[".claude/agents/researcher.md","research/Q-004.md","research/_GROUNDWORK.md","library/**","OPERATING_MODEL.md","template-v3/.claude/agents/*","template-v3/governance/BRIEFS.toml","template-v3/governance/PACKS.toml"],[("671335c","research/Q-004.md",7)]),
 ("SD HD1 plan (ftp)","SD","548031e",["f6c194c"],DEF+["decisions/questions/P-001-headers-approve.md"],[("HEAD","reviews/HD1/_plan-review-r1-verbatim.md",3),("HEAD","reviews/HD1/_plan-review-r1-verbatim.md",7),("548031e","decisions/questions/P-001-headers-approve.md",1),("548031e","decisions/questions/P-001-headers-approve.md",8)]),
 ("POOM S-027 plan (ftp)","POOM","93ed08c",["7c81268"],["governance/SURFACES.md"],[("HEAD","reviews/S-027/_plan-review-s027-round1-verbatim.md",4)]),
 ("SD followups build (ftp)","SD","706eb45",["2170e52","2b81fa8"],BLD,[("HEAD","reviews/S-001-followups/_build-review-round1-verbatim.md",1),("706eb45","specs/S-001.md",413),("706eb45","specs/S-001.md",414)]),
 ("POOM S-007 build (ftp)","POOM","8c60a80",["9aa70fb"],TB+["specs/S-007-v3-layout-and-templates.md","docs/LEDGER.md"],[("HEAD","reviews/7/_build-review-s007-verbatim.md",4),("HEAD","reviews/7/_build-review-s007-verbatim.md",6),("HEAD","reviews/1/reviewer.md",7),("8c60a80","docs/LEDGER.md",1047),("b8d54f9","docs/briefs/s-007.md",5)]),
 ("ML Q-006 (web-free)","ML","50d1c5a",["c55d934"],[".claude/agents/researcher.md","research/Q-006.md","research/_GROUNDWORK.md","library/**","OPERATING_MODEL.md","template-v3/governance/PACKS.toml","reviews/**/_*-verbatim.md","dispatch-log/**"],[("c55d934","research/Q-006-memo.md",10),("671335c","research/Q-006.md",5)]),
]
out = []
for pid, repo, start, firsts, inputs, cites in P:
    rc, full = git(repo, "rev-parse", start); full = full.strip()
    f1 = []
    for c in firsts:
        _, ps = git(repo, "log", "-1", "--format=%P %an %aI", c)
        parents, an, ad = ps.split()[:-2], ps.split()[-2], ps.split()[-1]
        _, p0 = git(repo, "rev-parse", parents[0]); f1.append((c, an, ad, p0.strip() == full))
    _, tree = git(repo, "ls-tree", "-r", "--name-only", start); tree = tree.split()
    f2 = []
    for p in inputs:
        n = len([t for t in tree if fnmatch.fnmatchcase(t, p) or (p.endswith("/*") and t.startswith(p[:-1]))]) if "*" in p else int(p in tree)
        f2.append((p, n))
    _, cnt = git(repo, "rev-list", "--count", start)
    out.append({"piece": pid, "repo": repo, "start": full[:12], "ancestors": int(cnt), "first_commits": f1, "inputs": f2,
                "cites": [(f"{r}:{p}:{n}", line(repo, r, p, n)) for r, p, n in cites]})
for o in out:
    print(f"## {o['piece']}  start {o['repo']}:{o['start']} (rev-list --count {o['ancestors']})")
    for c, an, ad, ok in o["first_commits"]:
        print(f"  first work commit {c} by {an} {ad}: first parent == start: {ok}")
    print("  inputs at start: " + "; ".join(f"{p}={n}" for p, n in o["inputs"]))
    for k, v in o["cites"]: print(f"  {k}: {v}")
json.dump(out, open("/home/user/wt/ml-builder/src/E-001/records_check.json", "w"), indent=1)
