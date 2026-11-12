"""Build the hand check's extract for research question Q-018 (S-002, M8; run by the Orchestrator).

Run as: python3 -I -B extract.py <the owner's configured git address> <clones dir> <github dir> <out dir>
  <clones dir> holds full clones of the three repositories at origin/main, with GitHub's
  pull-request heads fetched to refs/pull/<n>/head; <github dir> holds GitHub's pull-request records
  as read by this session (see README.md, "GitHub's records"). The address is used only to class
  commits and is not written anywhere.

Writes, per repository, <repo>.M.jsonl, <repo>.U.jsonl and <repo>.D.jsonl (frames M, U and D of
S-002's step 2), and sample.json (the drawn sample, written only by `draw`). No subject, title,
message, comment or path text is written: paths are written as their class (rule K1) and an
opaque label. Times are UTC.
"""
import json, re, subprocess, sys, hashlib, datetime as dt, collections, os

REPOS = ["Model-Lab", "Service-Desk", "Personal-Org-Operating-Model"]
SEED = "S-002-handcheck"
WIN0 = dt.datetime(2026, 10, 1, tzinfo=dt.timezone.utc)
CUT = dt.datetime(2026, 11, 12, tzinfo=dt.timezone.utc)
DAY30 = dt.timedelta(days=30)

def T(s): return dt.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
def utc(s): return dt.datetime.fromisoformat(s).astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def lab(s): return hashlib.sha1(s.encode()).hexdigest()[:8]
def git(repo, *a): return subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True, check=True).stdout

# ---------------- rule K1 (S-002): research/Q-017-memo.md §1's twelve rules on real paths -------------
CODE_EXT = (".py", ".js", ".mjs", ".sh", ".yml", ".yaml", ".toml", ".json", ".jsonl.lock", ".woff2", ".css")
TEMPLATE_TOP = {"template", "template-v3", "portfolio-template"}
REC_TOP = {"reviews", "dispatch-log", "status", "digest", "queue", "triage", "intake"}
REC_DOCS = {"briefs", "reports", "handover", "trials", "archive", "checkpoints", "audit"}
REC_DESIGN_SUB = {"builds", "audits"}; REC_DESIGN_PREFIX = ("audit-", "inventory-")
RES_TOP = {"research", "library", "experiments"}
PLAN_DOCS = {"proposals", "sprints", "gates", "design"}
BUILT_TOP = {"src", "tests", "tools", "scripts", ".github", ".claude"}
REC_WORDS = {"LEDGER", "DIGEST", "LESSONS", "CHECKPOINT", "PROGRESS", "CHANGELOG", "VERSION"}
PLAN_WORDS = {"MISSION", "SCOPE"}
def _stem(p):
    b = p.split("/")[-1]; return b[:-3] if b.endswith(".md") else b
def _caps(p): s = _stem(p); return s.replace("_", "").replace("-", "").isalpha() and s.isupper()
def _rec_name(p):
    s = _stem(p); q = p.split("/"); return _caps(p) and (len(q) == 1 or q[0] == "docs") and (s in REC_WORDS or s.endswith(("_REGISTER", "_REVIEW")))
def _label_of(p):
    """The Q-017 label a real path was given (research/Q-017-extract/extract.py, redact()), with S-002
    K1 change (i): a question or decision file is one under a top-level questions/ or decisions/ only."""
    if p.startswith("questions/") or p.startswith("decisions/"): return "qa"
    for pre in ("sessions/chief-of-staff/",):
        if p.startswith(pre) or ("/" + pre) in p: return "rec"
    for pre in ("docs/projects/", "docs/PROJECT.md", "ideas/"):
        if p.startswith(pre) or ("/" + pre) in p: return "plan"
    if p.endswith("-notes.md"): return "rec"
    if p.startswith("docs/handoff/") or "chief-of-staff" in p: return "rec"
    return None
def k1(p, repo):
    # change (ii): in Personal-Org-Operating-Model the operating model's own text is built work
    if repo == "Personal-Org-Operating-Model" and (p == "OPERATING_MODEL.md" or "/playbooks/" in "/" + p):
        return "built"
    l = _label_of(p)
    if l == "qa": return "owner_qa"
    if l == "rec": return "records"
    if l == "plan": return "plan"
    s = p.split("/"); top = s[0]; sub = s[1] if len(s) > 2 else None
    if top in TEMPLATE_TOP and len(s) > 1: return "built"
    if len(s) > 1 and top in REC_TOP: return "records"
    if top == "docs" and sub in REC_DOCS: return "records"
    if top == "docs" and len(s) > 2 and s[1] == "design" and (s[2] in REC_DESIGN_SUB and len(s) > 3 or (len(s) == 3 and s[2].startswith(REC_DESIGN_PREFIX))): return "records"
    if _rec_name(p): return "records"
    if (top in RES_TOP and len(s) > 1) or (top == "docs" and sub == "research") or (top == "docs" and sub == "design" and len(s) > 3 and s[2] == "references"): return "research"
    if (top == "specs" and len(s) > 1) or (top == "docs" and sub in PLAN_DOCS) or (top == "docs" and len(s) == 2 and _caps(p) and _stem(p) in PLAN_WORDS): return "plan"
    if (top in BUILT_TOP and len(s) > 1) or (top == "governance" and sub == "checks") or (len(s) == 1 and p.startswith(".") and p.endswith("ignore")) or p.endswith(CODE_EXT) \
       or (top == "governance" and len(s) == 2 and _caps(p) and _stem(p).endswith("_VERSION")): return "built"
    return "other"
def left_out(p):
    """Files left out of the file-sharing test, as Q-017 §4 left them out (its by_design())."""
    s = p.split("/"); top = s[0]
    if p.startswith("sessions/chief-of-staff/") or p.startswith("docs/handoff/") or "chief-of-staff" in p or p.endswith("-notes.md"): return True
    if top in ("dispatch-log", "status", "digest") and len(s) > 1: return True
    if _rec_name(p): return True
    if top == "intake" and len(s) == 2 and p.endswith(".jsonl"): return True
    if any(x.endswith("-extract") for x in s[:-1]): return True
    if s[-1].endswith("-lock.json"): return True
    return False

# ---------------- classes -----------------------------------------------------------------------
OWNER = sys.argv[1] if len(sys.argv) > 1 else ""
def author_class(name, email):
    if email.endswith("@agents.invalid"): return "agent"
    if name == "shumpmaster" or (OWNER and email == OWNER) or email.endswith("+shumpmaster@users.noreply.github.com"): return "owner"
    return "other"
def merger_class(name, email):
    """The merging account, from the author of GitHub's merge commit (README)."""
    if name.endswith("[bot]"): return "bot"
    return author_class(name, email)
def committer_class(name, email):
    if name == "GitHub" and email == "noreply@github.com": return "GitHub web editor"
    if email.endswith("@agents.invalid"): return "agent"
    if name.endswith("[bot]"): return "bot"
    return "other"
def account_class(login):
    if login is None: return None
    if login == "shumpmaster": return "owner"
    if login.endswith("[bot]"): return "bot"
    return "other"
def branch_prefix(ref):
    m = re.match(r"build/([^/]+)/", ref)
    if m: return "build/" + m.group(1) + "/"
    if ref.startswith("orch/"): return "orch/"
    return "other"

# ---------------- brief records and control files (README, "Where a piece's dispatch comes from") --
ROLES = sorted(["builder", "tools-builder", "definer", "critic", "reviewer", "researcher", "source-checker",
                "input-reader", "check-author", "release", "coder", "test-author", "orchestrator",
                "chief-of-staff", "user-rep", "design-reviewer"], key=len, reverse=True)
def parse_trailer(v, repo):
    """Returns (role, brief_id, kind) from one Agent-Session value. kind: 'ml-brief', 'brief-file',
    'control', or None (no brief named)."""
    v = v.strip()
    rest = re.sub(r"^session_[A-Za-z0-9]+[/\-]?", "", v)
    m = re.fullmatch(r"((?:Q|P)-\d+):([a-z\-]+):(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)", rest)
    if m and repo == "Service-Desk": return (None, rest, "control")
    if repo == "Model-Lab":
        m = re.fullmatch(r"([a-z\-]+)-(\d+)", rest)
        return (m.group(1), m.group(2), "ml-brief") if m else (None, None, None)
    if not rest or rest.startswith("gha-"): return (None, None, None)
    toks = rest
    role = next((r for r in ROLES if re.search(r"(^|-)" + re.escape(r) + r"($|-)", toks)), None)
    m = re.search(r"(?:^|-)s-?(\d{3})(?=$|-)", toks)
    return (role, ("s-" + m.group(1)) if m else None, "brief-file" if m else None)

class Repo:
    def __init__(self, name, clones, ghdir):
        self.name = name; self.path = os.path.join(clones, name)
        fp = [l.split("|") for l in git(self.path, "log", "--first-parent", "--format=%H|%cI", "HEAD").split("\n") if l]
        self.cut = next(h for h, c in fp if T(utc(c)) < CUT)        # default branch at the cut-off
        self.gh = [json.loads(l) for l in open(os.path.join(ghdir, name + ".list.jsonl"))]
        self.commits = {}
        self._load()
        self.first_add = self._first_adds()
    def _load(self):
        fmt = "%x1e%H%x1f%P%x1f%aI%x1f%cI%x1f%an%x1f%ae%x1f%cn%x1f%ce%x1f%s%x1f%(trailers:key=Agent-Session,valueonly,separator=%x1d)%x1f%(trailers:key=Spec,valueonly,separator=%x1d)%x1f%b%x1f"
        refs = ["HEAD"] + [r for r in git(self.path, "for-each-ref", "--format=%(refname)", "refs/pull").split()]
        raw = git(self.path, "log", *refs, "--numstat", "--no-renames", "--format=" + fmt)
        st = {}; cur = None
        for line in git(self.path, "log", *refs, "--name-status", "--no-renames", "--format=%x1e%H").split("\n"):
            if line.startswith("\x1e"): cur = line[1:]; st[cur] = {}
            elif "\t" in line and cur: s, p = line.split("\t", 1); st[cur][p] = s[0]
        for rec in raw.split("\x1e")[1:]:
            f = rec.split("\x1f")
            h, par, ad, cd, an, ae, cn, ce, subj, sess, spec, body, tail = f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8], f[9], f[10], f[11], f[12]
            files = []
            for line in tail.splitlines():
                q = line.split("\t")
                if len(q) == 3 and (q[0].isdigit() or q[0] == "-"):
                    files.append({"path": q[2], "status": {"A": "added", "M": "modified", "D": "deleted"}.get(st.get(h, {}).get(q[2]), "other"),
                                  "added": None if q[0] == "-" else int(q[0]), "removed": None if q[1] == "-" else int(q[1])})
            self.commits[h] = dict(hash=h, parents=par.split(), ad=utc(ad), cd=utc(cd), an=an, ae=ae, cn=cn, ce=ce, subj=subj,
                                   sess=[x for x in sess.split("\x1d") if x.strip()], spec=[x.strip() for x in spec.split("\x1d") if x.strip()],
                                   body=body, files=files)
        self.on_main = set(git(self.path, "rev-list", self.cut).split())
    def _first_adds(self):
        """For every path, the commit time of the first commit on the default branch (at the cut-off) that adds it."""
        out = {}
        cur = None
        for line in git(self.path, "log", self.cut, "--reverse", "--diff-filter=A", "--no-renames", "--name-only", "--format=%x1e%cI").split("\n"):
            if line.startswith("\x1e"): cur = utc(line[1:])
            elif line and cur and line not in out: out[line] = cur
        return out
    def show(self, rev, path):
        try: return git(self.path, "show", f"{rev}:{path}")
        except subprocess.CalledProcessError: return None

def brief_records(R, commits):
    """The briefs a set of commits names by trailer, each with its role, record and first-add time."""
    out = {}
    for h in commits:
        for v in R.commits[h]["sess"]:
            role, bid, kind = parse_trailer(v, R.name)
            if kind is None: continue
            if kind == "ml-brief":
                rec = f"docs/briefs/{bid}-{role}.md"; t = R.first_add.get(rec)
            elif kind == "brief-file":
                rec = f"docs/briefs/{bid}.md"; t = R.first_add.get(rec)
            else:  # control: the dispatch-log line with this item, route and time
                item, route, tm = bid.split(":", 2)
                role, t, rec = control_line(R, item, route, tm)
            key = (kind, bid)
            if key not in out:
                out[key] = {"brief": bid if kind != "control" else "control:" + lab(bid), "from": {"ml-brief": "brief record", "brief-file": "brief record", "control": "control file"}[kind],
                            "role": role, "record_exists": t is not None, "record_first_added": t}
    return list(out.values())

_CTRL = {}
def control_line(R, item, route, tm):
    if R.name not in _CTRL:
        lines = {}
        for f in sorted(x for x in git(R.path, "ls-tree", "--name-only", R.cut, "dispatch-log/").split() if x.endswith(".jsonl")):
            for l in (R.show(R.cut, f) or "").splitlines():
                try: d = json.loads(l)
                except ValueError: continue
                if d.get("action") == "dispatch": lines[(d.get("item"), d.get("route"), d.get("time"))] = (d.get("role"), d.get("prev"), f)
        _CTRL[R.name] = lines
    hit = _CTRL[R.name].get((item, route, tm))
    if not hit: return (None, None, None)
    role, prev, f = hit
    # the commit time of the first commit that adds the line (found by its unique "prev" hash)
    log = git(R.path, "log", R.cut, "--reverse", "--format=%cI", "-S", prev, "--", f).split()
    return (role, utc(log[0]) if log else None, f)

# ---------------- fields --------------------------------------------------------------------------
def commit_fields(R, h, with_files=True):
    c = R.commits[h]
    tr = [parse_trailer(v, R.name) for v in c["sess"]]
    reverts = re.findall(r"This reverts commit ([0-9a-f]{7,40})", c["body"])
    d = {"hash": h, "parents": len(c["parents"]), "author_class": author_class(c["an"], c["ae"]),
         "committer_class": committer_class(c["cn"], c["ce"]), "author_time": c["ad"], "commit_time": c["cd"],
         "agent_session": bool(c["sess"]),
         "trailer_briefs": [{"role": r, "brief": (("control:" + lab(b)) if k == "control" else b)} for r, b, k in tr if k],
         "spec": c["spec"], "revert_subject": c["subj"].startswith("Revert"), "reverts_commits": reverts,
         "subject_names_prs": sorted({int(x) for x in re.findall(r"#(\d+)\b", c["subj"])})}
    if with_files:
        d["files"] = [{"label": lab(f["path"]), "class": k1(f["path"], R.name), "status": f["status"], "added": f["added"], "removed": f["removed"]} for f in c["files"]]
    return d

def own_commits(R, pr):
    """A merged pull request's own commits: reachable from its head and not from the merge commit's first parent."""
    mc = pr["_merge"]
    return [h for h in git(R.path, "rev-list", f"{R.commits[mc]['parents'][0]}..{pr['head_sha']}").split()]

QD_RX = None
def qd_files(R):
    """Every question file and decision record first added on the default branch, with its text as first added (never written)."""
    out = []
    log = git(R.path, "log", R.cut, "--reverse", "--diff-filter=A", "--no-renames", "--name-only", "--format=%x1e%H %cI", "--", "questions/", "decisions/")
    cur = None; seen = set()
    for line in log.split("\n"):
        if line.startswith("\x1e"): cur = line[1:].split()
        elif line and cur and line not in seen and (line.startswith("questions/") or line.startswith("decisions/")):
            seen.add(line); out.append({"path": line, "time": utc(cur[1]), "text": R.show(cur[0], line) or ""})
    return out

def names_piece(text, n, briefs, specs, paths):
    hits = []
    if re.search(rf"#{n}(?!\d)", text) or re.search(rf"\bPR {n}(?!\d)", text) or re.search(rf"\bpull request {n}(?!\d)", text): hits.append("number")
    for b in briefs:
        if b and not b.startswith("control:") and (re.search(rf"\bbrief {re.escape(b)}(?![\w-])", text) or ("briefs/" + b + "-") in text or ("briefs/" + b + ".") in text): hits.append("brief"); break
    for s in specs:
        if re.search(rf"(?<![\w-]){re.escape(s)}(?![\w-])", text): hits.append("spec"); break
    for p in paths:
        if re.search(rf"(?<![\w./-]){re.escape(p)}(?![\w/-])", text): hits.append("path"); break
    return hits

def first_check(R, kind_files, specs, n):
    out = []
    def verdict(path):
        t = R.show(R.cut, path)
        if t is None: return None
        rounds = len(re.findall(r"^## Round \d+", t, re.M))
        i = t.find("## Round 1") if rounds else 0
        m = re.search(r"^Verdict: (PASS|FAIL)", t[max(i, 0):], re.M)
        return {"verdict": m.group(1) if m else "none found", "rounds": rounds if rounds else (1 if m else 0)}
    for s in specs:
        v = verdict(f"reviews/{s}/plan.md")
        if v: out.append({"kind": "Critic plan review", "for": "plan", **v})
    v = verdict(f"reviews/{n}/reviewer.md")
    if v: out.append({"kind": "Reviewer", "for": "built", **v})
    for q in sorted({m.group(1) for p in kind_files.get("research", []) for m in [re.search(r"(Q-\d+)", p.split("/")[-1])] if m}):
        v = verdict(f"research/{q}-source-check.md")
        if v: out.append({"kind": "Source checker", "for": "research", **v})
    return out

def build(clones, ghdir, outdir):
    repos = {r: Repo(r, clones, ghdir) for r in REPOS}
    reopen_marks = []   # (repo, n, time) from review records with a Reopens: line, in all three
    for R in repos.values():
        for line in git(R.path, "log", R.cut, "--reverse", "--format=%x1e%cI", "-G", r"^Reopens: ", "-p", "--", "reviews/").split("\n"):
            if line.startswith("\x1e"): cur = utc(line[1:])
            m = re.match(r"^\+Reopens: (\S+)#(\d+)", line)
            if m: reopen_marks.append((m.group(1).split("/")[-1], int(m.group(2)), cur))
    summary = {}
    for name, R in repos.items():
        merge = json.load(open(os.path.join(ghdir, name + ".merge.json")))
        merged = [p for p in R.gh if p["merged_at"] and str(p["number"]) in merge]
        for p in merged: p["_merge"] = merge[str(p["number"])][1][0]
        merged = [p for p in merged if p["_merge"] in R.on_main]
        own = {p["number"]: own_commits(R, p) for p in merged}
        in_pr = {h for v in own.values() for h in v} | {p["_merge"] for p in merged}
        U = [p for p in R.gh if not p["merged_at"] and p["closed_at"] and WIN0 <= T(p["closed_at"]) < CUT]
        U_open_or_late = [p for p in R.gh if not p["merged_at"] and p["closed_at"] and T(p["closed_at"]) >= CUT]
        QD = qd_files(R)
        # frame U, with its brief ids for RT3(b) matching
        Urows = []
        for p in U:
            hs = git(R.path, "rev-list", p["head_sha"], f"^{R.cut}").split()
            br = brief_records(R, hs)
            Urows.append({"repository": name, "number": p["number"], "created": p["created_at"], "closed": p["closed_at"], "merged": False,
                          "closing_account_class": None, "head_prefix": branch_prefix(p["head_ref"]), "head_label": lab(p["head_ref"]),
                          "commits": [commit_fields(R, h) for h in hs], "briefs": br})
        Ms = []
        for p in sorted(merged, key=lambda p: p["merged_at"]):
            if not (WIN0 <= T(p["merged_at"]) < CUT): continue
            n = p["number"]; hs = own[n]; mc = R.commits[p["_merge"]]
            cf = [commit_fields(R, h) for h in hs]
            agg = {}
            for h in hs:
                for f in R.commits[h]["files"]:
                    a = agg.setdefault(f["path"], {"label": lab(f["path"]), "class": k1(f["path"], name), "status": set(), "added": 0, "removed": 0})
                    a["status"].add(f["status"]); a["added"] += f["added"] or 0; a["removed"] += f["removed"] or 0
            files = [dict(v, status=sorted(v["status"])) for v in agg.values()]
            kind_files = collections.defaultdict(list)
            for path, v in agg.items(): kind_files[v["class"]].append(path)
            br = brief_records(R, hs)
            first = sorted(R.commits[h]["ad"] for h in hs)
            recs = [b["record_first_added"] for b in br if b["record_first_added"]]
            dispatch = (min(recs), sorted({b["from"] for b in br if b["record_first_added"] == min(recs)})[0]) if recs else ((first[0], "first commit") if first else (None, None))
            specs = sorted({s for h in hs for s in R.commits[h]["spec"]})
            bids = [b["brief"] for b in br]
            # RT1(a): question and decision files naming the pull request
            qd = []
            for q in QD:
                hit = names_piece(q["text"], n, bids, specs, list(agg))
                if hit: qd.append({"label": lab(q["path"]), "kind": "question" if q["path"].startswith("questions/") else "decision", "first_added": q["time"], "names_by": hit})
            # RT3(b): closed-unmerged pull requests with the same head label or a shared brief
            rt3b = [{"number": u["number"], "closing_account_class": u["closing_account_class"], "closed": u["closed"], "by": ("branch" if u["head_label"] == lab(p["head_ref"]) else "brief")}
                    for u in Urows if u["head_label"] == lab(p["head_ref"]) or set(b["brief"] for b in u["briefs"]) & set(bids)]
            # the 30 days after merging, read up to the cut-off
            t0 = T(p["merged_at"]); t1 = min(t0 + DAY30, CUT)
            mine = set(hs)
            later_prs = []
            for q in merged:
                tq = T(q["merged_at"])
                if q["number"] != n and t0 < tq <= t1:
                    shared = {x for x in agg if not left_out(x)} & {f["path"] for h in own[q["number"]] for f in R.commits[h]["files"] if not left_out(f["path"])}
                    if shared: later_prs.append({"number": q["number"], "merged": q["merged_at"], "shared_files": len(shared)})
            later_named, reverts = [], []
            for h in R.on_main:
                c = R.commits[h]; tc = T(c["cd"])
                if not (t0 < tc <= t1): continue
                nm = n in {int(x) for x in re.findall(r"#(\d+)\b", c["subj"])} and h != p["_merge"]
                if nm: later_named.append({"hash": h, "commit_time": c["cd"]})
                if c["subj"].startswith("Revert") and (nm or any(any(x.startswith(r) or r.startswith(x) for x in mine) for r in re.findall(r"This reverts commit ([0-9a-f]{7,40})", c["body"]))):
                    reverts.append({"hash": h, "commit_time": c["cd"]})
            marks = [{"time": t} for (rr, nn, t) in reopen_marks if rr == name and nn == n and t0 < T(t) <= t1]
            Ms.append({"repository": name, "number": n, "created": p["created_at"], "merged_at": p["merged_at"], "closed": p["closed_at"], "merged": True,
                       "merge_commit": p["_merge"], "merging_account_class": merger_class(mc["an"], mc["ae"]),
                       "head_prefix": branch_prefix(p["head_ref"]), "head_label": lab(p["head_ref"]),
                       "dispatch": dispatch[0], "dispatch_from": dispatch[1], "briefs": br, "commits": cf, "files": files,
                       "questions_decisions": qd, "first_check": first_check(R, kind_files, specs, n), "rt3b_matches": rt3b,
                       "after_merge": {"days30_complete": t0 + DAY30 <= CUT, "later_prs_sharing_a_file": later_prs,
                                       "later_commits_naming_it": later_named, "reverts_naming_it": reverts, "reopens_marks": marks}})
        # frame D
        Ds = []
        for h in R.on_main:
            c = R.commits[h]
            if h in in_pr or not (WIN0 <= T(c["ad"]) < CUT): continue
            Ds.append(commit_fields(R, h))
        Ds.sort(key=lambda d: d["author_time"])
        for frame, rows in (("M", Ms), ("U", Urows), ("D", Ds)):
            with open(os.path.join(outdir, f"{name}.{frame}.jsonl"), "w") as fh:
                for row in rows: fh.write(json.dumps(row, sort_keys=True) + "\n")
        summary[name] = {"default_branch_at_cutoff": R.cut, "M": len(Ms), "U": len(Urows), "D": len(Ds),
                         "M_30_days_complete": sum(1 for m in Ms if m["after_merge"]["days30_complete"]),
                         "closed_unmerged_after_cutoff_left_out": len(U_open_or_late)}
    json.dump(summary, open(os.path.join(outdir, "frames.json"), "w"), indent=1, sort_keys=True)
    print(json.dumps(summary, indent=1))

# ---------------- the draw (S-002 step 2), run only after the Critic has checked the README -----
K2_LIST = {"builder", "check-author", "tools-builder", "release", "definer", "researcher", "source-checker", "input-reader"}
BPR = {"built", "plan", "research"}
def order(repo, key): return hashlib.sha256(f"{SEED}:{repo}:{key}".encode()).hexdigest()
def classes(m): return {f["class"] for f in m["files"]}
FILTERS = [
    ("E-RP1", "D", lambda r, x: True),
    ("E-RP2", "U", lambda r, x: True),
    ("E-RP3", "M", lambda r, x: "other" in classes(x) and not (classes(x) & BPR)),
    ("E-RP4", "M", lambda r, x: len({b["brief"] for c in x["commits"] for b in c["trailer_briefs"] if b["brief"]}) >= 2),
    ("E-RP5", "M", lambda r, x: x["merging_account_class"] == "bot" and bool(classes(x) & BPR)),
    ("E-RP6", "M", lambda r, x: any(c["revert_subject"] for c in x["commits"])),
    ("E-K1", "M", lambda r, x: len(classes(x) & BPR) >= 2),
    ("E-K2", "M", lambda r, x: any(b["role"] not in K2_LIST for c in x["commits"] for b in c["trailer_briefs"])),
    ("E-K3", "M", lambda r, x: r == "Service-Desk" and x["dispatch_from"] == "control file" and "research" in classes(x)),
    ("E-RT1", "M", lambda r, x: any(c["author_class"] == "owner" and c["agent_session"] for c in x["commits"])),
    ("E-RT2", "M", lambda r, x: any(c["author_class"] == "other" for c in x["commits"])),
    ("E-RT3", "M", lambda r, x: any(c["author_class"] == "owner" and c["committer_class"] == "GitHub web editor" and c["files"] and all(f["class"] == "owner_qa" for f in c["files"]) for c in x["commits"])),
    ("E-RR2", "M", lambda r, x: x["after_merge"]["days30_complete"] and bool(x["after_merge"]["later_prs_sharing_a_file"] or x["after_merge"]["later_commits_naming_it"])),
]
def draw(outdir):
    rows = {(r, f): [json.loads(l) for l in open(os.path.join(outdir, f"{r}.{f}.jsonl"))] for r in REPOS for f in "MUD"}
    key = lambda f, x: x["hash"] if f == "D" else x["number"]
    drawn, random_part, shortfall = set(), {}, {}
    for r in REPOS:
        M = sorted(rows[(r, "M")], key=lambda x: order(r, x["number"]))
        if r == "Model-Lab": strata = [M]; want = [20]
        else:
            strata = [[x for x in M if x["after_merge"]["days30_complete"]], [x for x in M if not x["after_merge"]["days30_complete"]]]; want = [10, 10]
            for i in (0, 1):
                if len(strata[i]) < 10: want[i] = len(strata[i]); want[1 - i] = 20 - want[i]
        pick = [x["number"] for s, w in zip(strata, want) for x in s[:w]]
        random_part[r] = sorted(pick, key=lambda n: order(r, n))
        shortfall[r] = 20 - len(pick)
        drawn |= {(r, "M", n) for n in pick}
    edge = {}
    for case, frame, flt in FILTERS:
        pool = sorted(((r, x) for r in REPOS for x in rows[(r, frame)]), key=lambda t: order(t[0], key(frame, t[1])))
        got = []
        for r, x in pool:
            k = (r, frame, key(frame, x))
            if k in drawn or not flt(r, x): continue
            got.append({"repository": r, "frame": frame, "key": key(frame, x)}); drawn.add(k)
            if len(got) == 2: break
        edge[case] = got if got else "not seen"
    out = {"seed": SEED, "cut_off": CUT.strftime("%Y-%m-%dT%H:%M:%SZ"), "random_part": random_part, "shortfall": shortfall, "edge_case_part": edge}
    json.dump(out, open(os.path.join(outdir, "sample.json"), "w"), indent=1)
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    if sys.argv[1] == "draw": draw(sys.argv[2])
    else: build(sys.argv[2], sys.argv[3], sys.argv[4])
