"""Build the hand check's extract for research question Q-018 (S-002, M8; run by the Orchestrator).

Run as: python3 -I -B extract.py <the owner's configured git address> <clones dir> <github dir> <out dir>
  <clones dir> holds full clones of the three repositories at origin/main, with GitHub's
  pull-request heads fetched to refs/pull/<n>/head; <github dir> holds GitHub's pull-request records
  as read by this session (see README.md, "GitHub's records"). The address is used only to class
  commits and is not written anywhere.

Writes, per repository, <repo>.M.jsonl, <repo>.U.jsonl and <repo>.D.jsonl (frames M, U and D of
S-002's step 2), <repo>.merged.jsonl (every merged pull request, for C1's statement test; brief 294),
frames.json, and sample.json (the drawn sample, written only by `draw`). No subject, title,
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
    m = re.fullmatch(r"([PQE]-[0-9]+):([a-z][a-z0-9-]*):(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)", rest)
    if m and repo == "Service-Desk": return (None, rest, "control")
    if repo == "Model-Lab":
        m = re.fullmatch(r"([a-z\-]+)-(\d+)", rest)
        return (m.group(1), m.group(2), "ml-brief") if m else (None, None, None)
    if not rest or rest.startswith("gha-"): return (None, None, None)
    toks = rest
    role = next((r for r in ROLES if re.search(r"(^|-)" + re.escape(r) + r"($|-)", toks)), None)
    for special in ("adopt-v3-stamp", "adopt-v3"):
        if special in toks: return (role, special, "brief-file")
    m = re.search(r"(?:^|-)s-?(\d{3})(?=$|-)", toks)
    if not m: return (role, None, None)
    # a suffixed brief record s-NNN-<suffix>.md is named when the value holds its suffix; the longest such wins
    after = toks[m.end():]
    return (role, ("s-" + m.group(1)) + ("\x00" + after if after else ""), "brief-file")

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
        for line in git(self.path, "log", self.cut, "--diff-filter=A", "--no-renames", "--name-only", "--format=%x1e%cI").split("\n"):
            if line.startswith("\x1e"): cur = utc(line[1:])
            elif line and cur and (line not in out or cur < out[line]): out[line] = cur   # the earliest commit time that adds it
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
                rec = f"docs/briefs/{bid}-{role}.md"
                if rec not in R.first_add and len(bid) == 1: rec = f"docs/briefs/0{bid}-{role}.md"
                t = R.first_add.get(rec)
            elif kind == "brief-file":
                bid, rec = resolve_brief_file(R, bid); t = R.first_add.get(rec)
            else:  # control: the reviews/<id>/_control/*.json file whose "session" is this value
                role, t, rec = control_file(R, bid)
            key = (kind, bid)
            if key not in out:
                out[key] = {"brief": bid if kind != "control" else "control:" + lab(bid), "from": {"ml-brief": "brief record", "brief-file": "brief record", "control": "control file"}[kind],
                            "role": role, "record_exists": t is not None, "record_first_added": t}
    return list(out.values())

UNMATCHED = collections.defaultdict(set)   # values with text after the brief number that matched no suffixed file
def resolve_brief_file(R, bid):
    base, _, after = bid.partition("\x00")
    if after:
        names = [p for p in R.first_add if p.startswith(f"docs/briefs/{base}-") and p.endswith(".md")]
        hits = [p for p in names if p[len(f"docs/briefs/{base}-"):-3] in after]
        if hits:
            p = max(hits, key=len); return (p[len("docs/briefs/"):-3], p)
        UNMATCHED[R.name].add(base + after)
    return (base, f"docs/briefs/{base}.md")

_CF = {}
CTRL_CHECK = collections.defaultdict(dict)
NO_CONTROL = collections.defaultdict(set)   # control-form values with no control file   # control values whose dispatch-log line time differs from the file's first add
def control_file(R, value):
    if R.name not in _CF:
        idx = {}
        for p in git(R.path, "ls-tree", "-r", "--name-only", R.cut, "reviews/").split():
            if re.fullmatch(r"reviews/[^/]+/_control/[^/]+\.json", p):
                try: d = json.loads(R.show(R.cut, p) or "")
                except ValueError: continue
                if isinstance(d, dict) and d.get("session"): idx.setdefault(d["session"], []).append((d.get("role"), p))
        _CF[R.name] = idx
    hits = _CF[R.name].get(value)
    if not hits:
        NO_CONTROL[R.name].add("control:" + lab(value)); return (None, None, None)
    # every control file a session has; the earliest first add among them, and its role
    role, p, t = min(((r, q, R.first_add.get(q)) for r, q in hits), key=lambda x: (x[2] is None, x[2] or ""))
    item, route, tm = value.split(":", 2)
    _, lt, _ = control_line(R, item, route, tm)
    if lt != t: CTRL_CHECK[R.name]["control:" + lab(value)] = {"control": "control:" + lab(value), "file_first_added": t, "dispatch_log_line_first_added": lt}
    return (role, t, p)

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
    log = git(R.path, "log", R.cut, "--format=%cI", "-S", prev, "--", f).split()
    return (role, min(utc(x) for x in log) if log else None, f)

# ---------------- fields --------------------------------------------------------------------------
def commit_fields(R, h, with_files=True):
    c = R.commits[h]
    tr = [parse_trailer(v, R.name) for v in c["sess"]]
    reverts = re.findall(r"This reverts commit ([0-9a-f]{7,40})", c["body"])
    d = {"hash": h, "parents": len(c["parents"]), "author_class": author_class(c["an"], c["ae"]),
         "committer_class": committer_class(c["cn"], c["ce"]), "author_time": c["ad"], "commit_time": c["cd"],
         "agent_session": bool(c["sess"]),
         "trailer_briefs": [trailer_brief(R, r, b, k) for r, b, k in tr if k],
         "spec": c["spec"], "revert_subject": c["subj"].startswith("Revert"), "reverts_commits": reverts,
         "subject_names_prs": sorted({int(x) for x in re.findall(r"#(\d+)\b", c["subj"])})}
    if with_files:
        d["files"] = [{"label": lab(f["path"]), "class": k1(f["path"], R.name), "status": f["status"], "added": f["added"], "removed": f["removed"]} for f in c["files"]]
    return d

def trailer_brief(R, role, bid, kind):
    if kind == "control": return {"role": control_file(R, bid)[0], "brief": "control:" + lab(bid)}
    if kind == "brief-file": return {"role": role, "brief": resolve_brief_file(R, bid)[0]}
    return {"role": role, "brief": bid}

def own_commits(R, pr):
    """A merged pull request's own commits: reachable from its head and not from the merge commit's first parent."""
    mc = pr["_merge"]
    return [h for h in git(R.path, "rev-list", f"{R.commits[mc]['parents'][0]}..{pr['head_sha']}").split()]

QD_RX = None
def qd_files(R):
    """Every question file and decision record first added on the default branch, with its text as first added (never written)."""
    out = []
    log = git(R.path, "log", R.cut, "--diff-filter=A", "--no-renames", "--name-only", "--format=%x1e%H %cI", "--", "questions/", "decisions/")
    cur = None; first = {}
    for line in log.split("\n"):
        if line.startswith("\x1e"): cur = line[1:].split()
        elif line and cur and (line.startswith("questions/") or line.startswith("decisions/")):
            t = utc(cur[1])
            if line not in first or t < first[line][1]: first[line] = (cur[0], t)   # the earliest commit time that adds it
    for path, (h, t) in sorted(first.items(), key=lambda kv: kv[1][1]):
        out.append({"path": path, "time": t, "text": R.show(h, path) or ""})
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

# ================ the fields S-002's corrected rules need (brief 294; README, "The widened fields") ============
# Every field below is added beside the fields above, which are kept as they were; none is used by the draw.
STD_MS = re.compile(r"(?<![\w-])((?:Discovery|Design|Build|Launch)-\d+)(?![\w-])")
GATE_MS = {"Discovery-2", "Discovery-8", "Design-6", "Launch-3", "Launch-5"}
OWNER_WORD_LINE = re.compile(r"^[\s>*_-]*(Ruling|Answer|Decision)(\*\*)?\s*:")
NAMING_LINE = re.compile(r"(?i)owner's words|\banswer|\bnotes?\b|\bruling")
RT5_NAME = re.compile(r"(?:^|-)(design-gate|build-gate|launch-gate|value-target)(?:-|$)")

def qd_history(R, path):
    """Every commit reachable from the default branch at the cut-off that adds lines to `path` (merges' own diffs
    are not read), as (hash, commit time, [added line numbers, 1-based]), oldest commit time first."""
    out = []; cur = None
    for line in git(R.path, "log", R.cut, "--full-history", "--no-renames", "--format=%x1e%H %cI", "-p", "--unified=0", "--", path).split("\n"):
        if line.startswith("\x1e"):
            h, t = line[1:].split(); cur = [h, utc(t), []]; out.append(cur)
        elif line.startswith("@@") and cur:
            m = re.match(r"@@ -\S+ \+(\d+)(?:,(\d+))? @@", line)
            if m:
                a, k = int(m.group(1)), int(m.group(2)) if m.group(2) is not None else 1
                cur[2].extend(range(a, a + k))
    return sorted((tuple(x) for x in out if x[2]), key=lambda x: (x[1], x[0]))

def owner_word_counts(lines, added):
    """RT1(a)'s owner words among the added lines: (a `Ruling:`, `Answer:` or `Decision:` line; a quoted line whose
    nearest line above that is neither quoted nor blank names the owner's words, an answer, a note or a ruling)."""
    a = b = 0
    for i in added:
        l = lines[i - 1] if 0 < i <= len(lines) else ""
        if OWNER_WORD_LINE.match(l): a += 1; continue
        if l.lstrip().startswith(">"):
            j = i - 2
            while j >= 0 and (lines[j].lstrip().startswith(">") or not lines[j].strip()): j -= 1
            if j >= 0 and NAMING_LINE.search(lines[j]): b += 1
    return a, b

def asked_class(text):
    """RT5's class from a decision record's `Asked:` line (its first): the words before the colon of the sentence
    holding ': the owner's own <word>, never a default' (or '..., never a default or a proxy')."""
    for l in (text or "").splitlines():
        m = re.match(r"^[\s*_]*Asked(?:\*\*)?:(?:\*\*)?\s*(.*)$", l)
        if not m: continue
        mm = re.search(r": the owner's own \w+, never a default(?: or a proxy)?", l)
        if not mm: return None
        pre = l[:mm.start()]; k = pre.rfind(". ")
        return pre[k + 2:].strip() if k >= 0 else pre.strip()
    return None

def risk_class(text):
    """RT5's class from a question file's `RISK CLASS:` line: the words in its parenthesis before ', the owner's own <word>)'."""
    for l in (text or "").splitlines():
        if "RISK CLASS:" in l:
            m = re.search(r"RISK CLASS:[^()]*\(([^()]*), the owner's own \w+\)", l)
            return m.group(1).strip() if m else None
    return None

def milestone_line(text):
    for l in (text or "").splitlines():
        m = re.match(r"^[\s*_]*Milestone(?:\*\*)?:(?:\*\*)?\s*(.*)$", l)
        if m: return STD_MS.findall(m.group(1))
    return None

def rt5_reading(cls, name_word):
    if cls is not None:
        if re.search(r"(?i)(?<![\w])stop rule(?![\w])", cls): return "a (class names a stop rule)"
        if re.search(r"(?i)(?<![\w])(phase gate|value target)(?![\w])", cls) or re.search(r"(?i)(?<![\w])value target's", cls): return "b (class names a phase gate or a value target)"
        return "c (class names neither)"
    return "d (no class; name holds a gate or value-target word)" if name_word else "d (no class; name holds no gate or value-target word)"

def naming(text, n, briefs, specs, repo):
    """S-002 'What a touch is': which parts of the naming rule a text matches (the text is never written)."""
    parts = []
    hit = False
    for m in re.finditer(rf"#{n}(?![\w])", text):
        pre = text[:m.start()]
        own_repo = pre.endswith("shumpmaster/" + repo) or (pre.endswith(repo) and (len(pre) == len(repo) or not re.match(r"[A-Za-z0-9_/-]", pre[-len(repo) - 1])))
        if not pre or not re.match(r"[A-Za-z0-9_]", pre[-1]) or own_repo:
            hit = True; break
    if hit or re.search(rf"(?i)(?<![\w])(?:pr|pull request) {n}(?![\w])", text): parts.append("number")
    bs = [b for b in briefs if b and not b.startswith("control:")]
    if any(re.search(rf"(?i)(?<![\w])brief {re.escape(b)}(?![\w-])", text) or ("briefs/" + b + "-") in text or ("briefs/" + b + ".md") in text for b in bs): parts.append("brief")
    sp = [s for s in specs if not (repo == "Service-Desk" and s == "S-001")]
    if any(re.search(rf"(?<![\w-]){re.escape(s)}(?![\w-])", text) for s in sp): parts.append("spec")
    return parts

def qd_files_full(R):
    """As qd_files, with every commit the default branch at the cut-off reaches, a merged pull request's own commits
    included, even where a pull request adds a file and deletes it again (S-002 'What a touch is'; brief 296)."""
    log = git(R.path, "log", R.cut, "--full-history", "--diff-filter=A", "--no-renames", "--name-only", "--format=%x1e%H %cI", "--", "questions/", "decisions/")
    cur = None; first = {}
    for line in log.split("\n"):
        if line.startswith("\x1e"): cur = line[1:].split()
        elif line and cur and (line.startswith("questions/") or line.startswith("decisions/")):
            t = utc(cur[1])
            if line not in first or (t, cur[0]) < (first[line][1], first[line][0]): first[line] = (cur[0], t)
    return [{"path": p, "time": t, "hash": h, "text": R.show(h, p) or ""} for p, (h, t) in sorted(first.items(), key=lambda kv: (kv[1][1], kv[0]))]

class QD_:
    """Every question file and decision record first added on the default branch by the cut-off (deleted ones included),
    each read as S-002 'What a touch is' says: as first added, then each later commit's added lines."""
    def __init__(self, R):
        self.R = R; self.recs = []
        for q in qd_files_full(R):
            path = q["path"]; hist = qd_history(R, path)
            hist = [x for x in hist if (x[1], x[0]) >= (q["time"], q["hash"])]
            first_hash = q["hash"]
            commits = []
            for h, t, added in hist:
                txt = R.show(h, path) or ""; lines = txt.split("\n")
                a, b = owner_word_counts(lines, added)
                commits.append({"hash": h, "time": t, "first_add": h == first_hash, "added": "\n".join(lines[i - 1] for i in added if 0 < i <= len(lines)),
                                "n_added": len(added), "owner_word_lines": a, "quoted_lines_under_a_naming_line": b})
            self.recs.append({"path": path, "time": q["time"], "text": q["text"], "first_hash": first_hash, "commits": commits})
        self.by_path = {r["path"]: r for r in self.recs}
    def pair(self, path):
        m = re.fullmatch(r"(?:questions|decisions/questions)/(.+\.md)", path)
        return m.group(1) if m else None
    def rt5(self, path):
        """The class, where it came from, and the milestone, for the question a record belongs to."""
        name = self.pair(path)
        dec = self.by_path.get("decisions/questions/" + name) if name else (self.by_path.get(path) if path.startswith("decisions/") else None)
        que = self.by_path.get("questions/" + name) if name else None
        cls, src = None, "none"
        if dec and asked_class(dec["text"]) is not None: cls, src = asked_class(dec["text"]), "decision record's Asked: line, as first added"
        elif que and risk_class(que["text"]) is not None: cls, src = risk_class(que["text"]), "question file's RISK CLASS: line, as first added"
        ms, msrc = None, "none"
        if dec and milestone_line(dec["text"]) is not None: ms, msrc = milestone_line(dec["text"]), "decision record, as first added"
        elif que and milestone_line(que["text"]) is not None: ms, msrc = milestone_line(que["text"]), "question file, as first added"
        stem = path.split("/")[-1][:-3] if path.endswith(".md") else path.split("/")[-1]
        nw = bool(RT5_NAME.search(stem))
        rd = rt5_reading(cls, nw)
        other = rd.startswith("b") and cls.strip().lower() not in ("a phase gate", "a value target", "part of a value target")
        return {"rt5_class": cls, "rt5_class_from": src, "rt5_name_holds_word": nw, "rt5_reading": rd, "rt5_names_other_rulings": other,
                "standard_milestones": ms, "milestone_from": msrc, "gate_or_value_target_milestone": bool(ms and set(ms) & GATE_MS)}
    def for_piece(self, n, briefs, specs, own, first_hash, dispatch, merged_at):
        """`own`: the piece's own commits, as (author time, hash, commit time, set of paths)."""
        out = []
        for r in self.recs:
            mine = sorted((a, h, c) for a, h, c, ps in own if r["path"] in ps)
            names_from, parts = None, []
            for c in r["commits"]:
                p = naming(r["text"] if c["first_add"] else c["added"], n, briefs, specs, self.R.name)
                if p: names_from, parts = c, p; break
            own_start = None
            if mine:
                parts = parts + ["own file"]
                a, h, ct = mine[0]
                own_start = next((c for c in r["commits"] if c["hash"] == h), None) or {"hash": h, "time": ct, "first_add": h == r["first_hash"]}
            if not parts: continue
            cands = [c for c in (names_from, own_start) if c is not None]
            start = min(cands, key=lambda c: (c["time"], c["hash"])) if cands else None
            row = {"label": lab(r["path"]), "kind": "question" if r["path"].startswith("questions/") else "decision",
                   "question_label": lab(self.pair(r["path"])) if self.pair(r["path"]) else None,
                   "notes_file": r["path"].endswith("-notes.md"), "first_added": r["time"],
                   "first_added_in_pieces_first_commit": r["first_hash"] == first_hash,
                   "names_by": parts, "names_from": None if start is None else ("first add" if start["first_add"] else ("own commit" if start is own_start else "append")),
                   "names_from_time": None if start is None else start["time"]}
            row.update(self.rt5(r["path"]))
            row["window_commits"] = [{"commit_time": c["time"], "first_add": c["first_add"], "read_for_piece": start is not None and (c["time"], c["hash"]) >= (start["time"], start["hash"]),
                                      "added_lines": c["n_added"], "owner_word_lines": c["owner_word_lines"],
                                      "quoted_lines_under_a_naming_line": c["quoted_lines_under_a_naming_line"]}
                                     for c in r["commits"] if dispatch and dispatch < c["time"] < merged_at]
            out.append(row)
        return out

# ---- C1: check records at the cut-off, by S-002's check-record paths -----------------------------------------
V = r"(?:-[A-Za-z0-9-]+)?-verbatim\.md"     # a name may carry a suffix before -verbatim
def c1_form(repo, path):
    """(path form, kind) for a file at C1's check-record paths, or None for a file at none of them."""
    s = path.split("/")
    if s[0] == "research" and len(s) == 2 and repo in ("Model-Lab", "Service-Desk"):
        b = s[1]
        if re.fullmatch(r"Q-\d+-source-check\.md", b): return ("research/Q-<n>-source-check.md", "research")
        m = re.fullmatch(r"Q-\d+-source-check-(\d+)\.md", b)
        if m and int(m.group(1)) >= 2: return ("research/Q-<n>-source-check-<k>.md (a later round)", "research")
        if re.fullmatch(r"Q-\d+-to-Q-\d+-source-check(?:-\d+)?\.md", b): return ("research/Q-<n>-to-Q-<m>-source-check-<k>.md (a later round)", "research")
        return None
    if s[0] != "reviews" or len(s) != 3 or not s[2].endswith(".md"): return None
    f, b = s[1], s[2]
    if re.search(r"(?i)design|security|owner|triage|confirmation", b): return ("a file name holding design, security, owner, triage or confirmation", "another kind")
    if re.match(r"P-\d+", f) and "critic" in b: return ("a Critic's check of a question card, a proposal or a gate case (reviews/P-<n>…)", "another kind")
    num, spec = f.isdigit(), bool(re.fullmatch(r"S-\d+", f))
    if repo == "Model-Lab":
        if spec and b == "plan.md": return ("reviews/<spec id>/plan.md", "plan")
        if num and b == "reviewer.md": return ("reviews/<pull request number>/reviewer.md", "build")
        if re.fullmatch(r"[QE]-\d+", f) and b == "critic.md": return ("reviews/Q-<n>/critic.md or reviews/E-<n>/critic.md", "research")
    elif repo == "Service-Desk":
        for rx, form in ((r"_plan-review-round\d+" + V, "_plan-review-round<n>-verbatim.md"), (r"_plan-review-r\d+" + V, "_plan-review-r<n>-verbatim.md"),
                         (r"_plan-critic-r\d+" + V, "_plan-critic-r<n>-verbatim.md")):
            if re.fullmatch(rx, b): return (form, "plan")
        if re.match(r"S-\d+", f) and re.fullmatch(r"_critic-round\d+" + V, b): return ("_critic-round<n>-verbatim.md in a spec's folder", "plan")
        for rx, form in ((r"reviewer\.md", "reviewer.md"), (r"_reviewer-r\d+" + V, "_reviewer-r<n>-verbatim.md"), (r"_reviewer" + V, "_reviewer-verbatim.md"),
                         (r"_build-review-round\d+" + V, "_build-review-round<n>-verbatim.md"), (r"_build-[A-Za-z0-9]+-review-round\d+" + V, "_build-<step>-review-round<n>-verbatim.md"),
                         (r"_review-round\d+" + V, "_review-round<n>-verbatim.md"), (r"_review-r\d+" + V, "_review-r<n>-verbatim.md"),
                         (r"_stage-[A-Za-z0-9]+-review-r\d+" + V, "_stage-<stage>-review-r<n>-verbatim.md")):
            if re.fullmatch(rx, b): return (form, "build")
        if re.fullmatch(r"(?:Q|EXP)-\d+", f) and (b == "critic.md" or re.fullmatch(r"_critic-r\d+" + V, b)): return ("critic.md or _critic-r<n>-verbatim.md in reviews/Q-<n>/ or reviews/EXP-<n>/", "research")
    else:
        s0 = bool(re.fullmatch(r"S-0\d\d", f))
        if s0:
            for rx, form in ((r"_plan-review-round\d+" + V, "reviews/S-0nn/_plan-review-round<n>-verbatim.md"), (r"_plan-review-s0\d\d-round\d+" + V, "reviews/S-0nn/_plan-review-s0nn-round<n>-verbatim.md"),
                             (r"_draft\d+-plan-review-round\d+" + V, "reviews/S-0nn/_draft<k>-plan-review-round<n>-verbatim.md")):
                if re.fullmatch(rx, b): return (form, "plan")
            if re.fullmatch(r"_build-review-round\d+" + V, b): return ("reviews/S-0nn/_build-review-round<n>-verbatim.md", "build")
            if re.fullmatch(r"_source-check-[A-Za-z0-9-]+-verbatim\.md", b): return ("reviews/S-0nn/_source-check-<topic>-verbatim.md", "research")
        if num:
            if re.fullmatch(r"_plan-review-s0\d\dr?-round\d+" + V, b): return ("reviews/<pull request number>/_plan-review-s0nn-round<n>-verbatim.md (also s0nnr)", "plan")
            for rx, form in ((r"reviewer\.md", "reviewer.md"), (r"_reviewer-round\d+" + V, "_reviewer-round<n>-verbatim.md"), (r"_reviewer-r\d+" + V, "_reviewer-r<n>-verbatim.md"),
                             (r"_review-r\d+" + V, "_review-r<n>-verbatim.md"), (r"_build-review-s0\d\d-round\d+" + V, "_build-review-s0nn-round<n>-verbatim.md")):
                if re.fullmatch(rx, b): return ("reviews/<pull request number>/" + form, "build")
    return ("unclassed (in these folders, fitting no form)", "unclassed")

def name_round(path):
    for part in re.split(r"[-_.]", path.split("/")[-1]):
        m = re.fullmatch(r"(?:round|r)(\d+)", part)
        if m: return int(m.group(1))
    return None

def statements(text):
    """C1: the record's statement of what it reviews, as a list read in turn: its first line starting `Reviewed` or
    `Read:`; else its opening (its first paragraph that is not a heading, a `Verdict:` line or a `---` rule, with the
    headings above it), then, where the opening names no subject, its first heading with the first such paragraph after it."""
    L = text.split("\n")
    for l in L:
        if re.match(r"(?i)^[\s*_]*(reviewed|read:)", l): return [l]
    def skip(t): return not t or t.startswith("#") or re.match(r"(?i)^[*_]*verdict", t) or re.fullmatch(r"-{3,}", t)
    def para(start):
        out, at = [], None
        for k in range(start, len(L)):
            t = L[k].strip()
            if not out and skip(t): continue
            if out and (not t or t.startswith("#")): break
            if at is None: at = k
            out.append(L[k])
        return at, "\n".join(out)
    at, body = para(0)
    heads = [l for l in L[:at if at is not None else len(L)] if l.lstrip().startswith("#")]
    out = ["\n".join(heads + [body])]
    h = next((k for k, l in enumerate(L) if l.lstrip().startswith("#")), None)
    if h is not None: out.append(L[h] + "\n" + para(h + 1)[1])
    return out

KIND_WORDS = {"plan": r"plan review", "build": r"build review", "research": r"source check"}
def own_kind_segments(line, kind):
    """A line giving words for more than one kind of check: only the parts for the record's own kind."""
    hits = sorted((m.start(), k) for k, rx in KIND_WORDS.items() for m in re.finditer("(?i)" + rx, line))
    if len({k for _, k in hits}) < 2: return [line]
    return [line[a:(hits[i + 1][0] if i + 1 < len(hits) else len(line))] for i, (a, k) in enumerate(hits) if k == kind]

VLINE = re.compile(r"^[\s>*_-]*(?i:verdict)(?:\*\*)?:(?:\*\*)?\s*(?:\*\*)?(PASS|FAIL)\b")
def first_round(text, path, kind):
    """C1's readings (i) to (iv), in that order: (reading, verdict, rounds, notes)."""
    L = text.split("\n"); notes = []
    nums = [int(x) for x in re.findall(r"(?i)\brounds? (\d+)", text)] + [int(x) for x in re.findall(r"(?i)\brounds \d+ to (\d+)", text)]
    nr = name_round(path)
    rounds = max(nums + ([nr] if nr else []), default=0)
    if "a later round" in (c1_form_cache.get(path) or ""):
        return ("none: a later round, which gives no round 1", "none found", rounds, notes)
    # (i)
    if nr == 1:
        for l in L:
            m = re.match(r"^(?i:verdict): (PASS|FAIL)\b", l)
            if m: return ("(i)", m.group(1), rounds, notes)
    # (ii)
    heads = [(i, len(re.match(r"#+", l).group())) for i, l in enumerate(L) if re.match(r"^#+\s*Round 1(?:\s*$| \(|:| at |, part \d+)", l)]
    if heads:
        vs = []
        for i, lev in heads:
            v = None
            m = re.search(r"(?i:verdict):?\s*(PASS|FAIL)\b", L[i])
            if m: v = m.group(1)
            else:
                for l in L[i + 1:]:
                    hm = re.match(r"^(#+)\s", l)
                    if hm and len(hm.group(1)) <= lev: break
                    m = VLINE.match(l) or re.search(r"The (?:round's|part's|round-1) verdict was (PASS|FAIL)", l)
                    if m: v = m.group(1); break
            vs.append(v)
            if not re.search(r", part \d+", L[i]): break      # a round not in parts: its first heading
        if "FAIL" in vs: return ("(ii)", "FAIL", rounds, notes)
        if vs and all(v == "PASS" for v in vs): return ("(ii)", "PASS", rounds, notes)
        if any(vs): notes.append("a round in parts with a part that gives no verdict")
    else:
        # (iii)
        pats = [r"(?i:\bround) 1(?!\d)(?:(?!(?i:round) \d)[^\n])*?:\s*\**(PASS|FAIL)\b", r"(?i:\bround) 1:? (PASS|FAIL)\b",
                r"\b(FAIL) (?i:round) 1(?!\d)", r"\b(FAIL) (?i:rounds) 1 to \d+"]
        acct = set(); sec = True; first = next((k for k, l in enumerate(L) if l.strip()), None)
        for k, l in enumerate(L):
            if re.match(r"^#+\s", l) or l.startswith("#"):
                sec = k == first or bool(re.search(r"(?i)(?<![\w])rounds?(?![\w])", l)); continue
            if sec: acct.add(k)
        for i, l in enumerate(L):
            for seg in (own_kind_segments(l, kind) if i in acct else []):
                best = None
                for p in pats:
                    m = re.search(p, seg)
                    if m and (best is None or m.start() < best[0]): best = (m.start(), m.group(1))
                if best: return ("(iii)", best[1], rounds, notes)
            if l.lstrip().startswith("|"):
                cells = [c.strip() for c in l.strip().strip("|").split("|")]
                col = next((j for j, c in enumerate(cells) if re.match(r"Round 1(?!\d)", c)), None)
                if col is not None:
                    for l2 in L[i + 1:]:
                        if not l2.lstrip().startswith("|"): break
                        c2 = [c.strip() for c in l2.strip().strip("|").split("|")]
                        if c2 and re.search(r"(?i)verdict", c2[0]) and col < len(c2):
                            m = re.search(r"\b(PASS|FAIL)\b", c2[col])
                            if m: return ("(iii)", m.group(1), rounds, notes)
    # (iv)
    top = next((l for l in L if l.strip()), "")
    m = re.match(r"^(?i:verdict): (PASS|FAIL)\b", top)
    if m:
        other = [x for x in nums if x != 1] or (nr not in (None, 1))
        why = []
        if other: why.append("names a round other than round 1")
        if re.search(r"(?i)\brounds\b", text): why.append("names rounds")
        if re.search(r"(?i)round-1 finding", text): why.append("names a round-1 finding")
        if re.search(r"(?i)\bre-?check", text): why.append("names a re-check")
        if re.search(r"(?i)\bearlier round", text): why.append("names an earlier round")
        if not why: return ("(iv)", m.group(1), rounds, notes)
        notes.append("top-line verdict not read as round 1's: " + "; ".join(why))
    return ("none", "none found", rounds, notes)

c1_form_cache = {}
class C1:
    """Every file at C1's check-record paths at the cut-off, with its statement's subject (S-002 C1)."""
    def __init__(self, R, merged, own):
        self.R = R
        paths = [p for p in git(R.path, "ls-tree", "-r", "--name-only", R.cut, "reviews/", "research/").split("\n") if p]
        nums = {p["number"] for p in merged}
        heads = collections.defaultdict(set)
        for p in merged: heads[p["head_ref"]].add(p["number"])
        self.shared_heads = sorted(({"head_label": lab(h), "numbers": sorted(v)} for h, v in heads.items() if len(v) > 1), key=lambda d: d["numbers"])
        cprs = collections.defaultdict(set)
        for k, hs in own.items():
            for h in hs: cprs[h].add(k)
        self.recs = []
        for p in paths:
            f = c1_form(R.name, p)
            if f is None: continue
            c1_form_cache[p] = f[0]
            text = R.show(R.cut, p) or ""
            subject, skipped = None, []
            for st in statements(text):
                toks = []
                for m in re.finditer(r"(?i)(?<![\w])(?:pull request |pr #?|#)(\d+)(?![\w])", st): toks.append((m.start(), "number", m.group(1)))
                for m in re.finditer(r"(?<![\w/-])([0-9a-f]{7,40})(?![\w/-])", st): toks.append((m.start(), "hash", m.group(1)))
                for h in heads:
                    for m in re.finditer(re.escape(h), st):
                        a, z = m.start(), m.end(); pre = st[:a]
                        if pre.endswith("origin/"): pre = pre[:-7]
                        if (pre and re.match(r"[\w/-]", pre[-1])) or (z < len(st) and re.match(r"[\w/-]", st[z])): continue
                        toks.append((a, "branch", h))
                for _, kind, v in sorted(toks):
                    if kind == "number":
                        if int(v) in nums: subject = {"by": "number", "number": int(v)}; break
                    elif kind == "branch":
                        if len(heads[v]) == 1: subject = {"by": "head branch", "number": next(iter(heads[v]))}; break
                        skipped.append({"token": "head branch", "head_label": lab(v), "heads": sorted(heads[v])})
                    else:
                        prs = set().union(*[cprs[h] for h in cprs if h.startswith(v)]) if any(h.startswith(v) for h in cprs) else set()
                        if len(prs) == 1: subject = {"by": "commit hash", "number": next(iter(prs))}; break
                        if len(prs) > 1: skipped.append({"token": "commit hash", "hash": v, "own_commit_of": sorted(prs)})
                if subject: break
            kind = f[1]
            reading = first_round(text, p, kind) if kind in ("plan", "build", "research") else ("not read: a record of another kind or unclassed gives no result", "none found", None, [])
            s = p.split("/")
            self.recs.append({"path": p, "label": lab(p), "path_form": f[0], "kind": kind, "folder": s[1] if s[0] == "reviews" else None,
                              "subject": subject, "statement_skipped": skipped,
                              "reading": reading[0], "verdict": reading[1], "rounds": reading[2], "notes": reading[3]})
    def for_piece(self, n, specs, ids, qids):
        out = []
        sp_keys = {s.lower().replace("-", "") for s in specs}
        for r in self.recs:
            why = []
            if r["folder"] == str(n): why.append("pull request folder")
            if self.R.name in ("Model-Lab", "Personal-Org-Operating-Model") and r["folder"] is not None:
                b = r["path"].split("/")[-1]
                if r["folder"] in specs or any(re.search(rf"(?<![a-z0-9]){k}r?(?![0-9])", b) for k in sp_keys): why.append("spec")
            if r["folder"] in ids: why.append("experiment or question id")
            und = []
            if r["folder"] is None:
                q = re.match(r"research/(Q-\d+)-", r["path"]).group(1)
                if q in qids:
                    why.append("question id of the piece's own question or memo file")
            if r["subject"] and r["subject"]["number"] == n: why.append("the record's statement of what it reviews (" + r["subject"]["by"] + ")")
            if not why: continue
            out.append({"label": r["label"], "path_form": r["path_form"], "kind": r["kind"], "piece_by": why, "statement_skipped": r["statement_skipped"],
                        "reading": r["reading"], "verdict": r["verdict"], "rounds": r["rounds"], "notes": r["notes"], "undecided": und})
        return out

def comment_records(R):
    """Lines in records-class files (K1) at the cut-off that name a comment on a pull request: per number,
    the labels of files whose line says 'reviewer comment' and of files whose line says 'comment' otherwise."""
    out = collections.defaultdict(lambda: {"reviewer_comment": set(), "other_wording": set()})
    try: raw = git(R.path, "grep", "-I", "-n", "-i", "-E", r"comment", R.cut, "--")
    except subprocess.CalledProcessError: return out
    for line in raw.split("\n"):
        if not line: continue
        _, path, _, txt = line.split(":", 3)
        if k1(path, R.name) != "records": continue
        for m in re.finditer(r"(?i)(?<![\w])(?:pull request |pr #?|#)(\d+)(?![\w])", txt):
            key = "reviewer_comment" if re.search(r"(?i)reviewer comment", txt) else "other_wording"
            out[int(m.group(1))][key].add(lab(path))
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
        # each merged pull request's merge commit: the first-parent default-branch commit (at the cut-off, or after
        # it for a pull request merged after it) committed by GitHub whose second parent is GitHub's head commit
        fp = [l.split("|") for l in git(R.path, "log", "--first-parent", "--format=%H|%P|%cn", "HEAD").split("\n") if l]
        by_head = {}
        for h, par, cn in fp:
            ps = par.split()
            if cn == "GitHub" and len(ps) == 2: by_head.setdefault(ps[1], h)
        gh_merged = [p for p in R.gh if p["merged_at"]]
        merged, no_row = [], []
        for p in gh_merged:
            mc = by_head.get(p["head_sha"])
            if mc is None or (T(p["merged_at"]) < CUT and mc not in R.on_main):
                no_row.append({"number": p["number"], "merged_at": p["merged_at"], "why": "no merge commit found" if mc is None else "merge commit not on the default branch at the cut-off"})
                continue
            p["_merge"] = mc
            if mc in R.on_main: merged.append(p)
        if any(WIN0 <= T(x["merged_at"]) < CUT for x in no_row):
            raise SystemExit(f"{name}: merged pull requests in the window with no frame M row: {no_row}")
        # independent of GitHub's list: every GitHub merge commit on the default branch's first-parent line with a
        # commit time in the window must be the merge commit of a listed pull request
        listed_heads = {p["head_sha"] for p in gh_merged}
        git_merges = [(h, par.split()[1]) for h, par, cn in fp if cn == "GitHub" and len(par.split()) == 2 and h in R.on_main and WIN0 <= T(R.commits[h]["cd"]) < CUT]
        unlisted = [h for h, second in git_merges if second not in listed_heads]
        if unlisted:
            raise SystemExit(f"{name}: GitHub merge commits in the window matching no listed pull request: {unlisted}")
        own = {p["number"]: own_commits(R, p) for p in merged}
        in_pr = {h for v in own.values() for h in v} | {p["_merge"] for p in merged}
        U = [p for p in R.gh if not p["merged_at"] and p["closed_at"] and WIN0 <= T(p["closed_at"]) < CUT]
        U_open_or_late = [p for p in R.gh if not p["merged_at"] and p["closed_at"] and T(p["closed_at"]) >= CUT]
        QD = qd_files(R)
        QDN = QD_(R); CK = C1(R, merged, own); CR = comment_records(R)
        def crec(n): return {k: sorted(v) for k, v in CR[n].items()} if n in CR else {"reviewer_comment": [], "other_wording": []}
        # frame U, with its brief ids for RT3(b) matching
        Urows = []
        for p in U:
            hs = git(R.path, "rev-list", p["head_sha"], f"^{R.cut}").split()
            br = brief_records(R, hs)
            Urows.append({"repository": name, "number": p["number"], "created": p["created_at"], "closed": p["closed_at"], "merged": False,
                          "closing_account_class": None, "head_prefix": branch_prefix(p["head_ref"]), "head_label": lab(p["head_ref"]),
                          "commits": [commit_fields(R, h) for h in hs], "briefs": br, "comment_records": crec(p["number"])})
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
            for h in sorted(R.on_main, key=lambda h: (R.commits[h]["cd"], h)):
                c = R.commits[h]; tc = T(c["cd"])
                if not (t0 < tc <= t1): continue
                nm = n in {int(x) for x in re.findall(r"#(\d+)\b", c["subj"])} and h != p["_merge"]
                if nm: later_named.append({"hash": h, "commit_time": c["cd"]})
                if c["subj"].startswith("Revert") and (nm or any(any(x.startswith(r) or r.startswith(x) for x in mine) for r in re.findall(r"This reverts commit ([0-9a-f]{7,40})", c["body"]))):
                    reverts.append({"hash": h, "commit_time": c["cd"]})
            marks = [{"time": t} for (rr, nn, t) in reopen_marks if rr == name and nn == n and t0 < T(t) <= t1]
            # the widened fields (brief 294)
            own_paths = set(agg)
            first_hash = min(hs, key=lambda h: (R.commits[h]["ad"], h)) if hs else None
            spec_files = {m.group(1) for x in agg for m in [re.match(r"specs/(S-\d+)", x)] if m}
            ids = {m.group(1) for x in agg for m in [re.match(r"((?:Q|E|EXP)-\d+)(?=[.-]|$)", x.split("/")[-1])] if m}
            qids = {m.group(1) for x in agg for m in [re.fullmatch(r"research/(Q-\d+)(?:-memo)?\.md", x)] if m}
            own_c = [(R.commits[h]["ad"], h, R.commits[h]["cd"], {f["path"] for f in R.commits[h]["files"]}) for h in hs]
            qdn = QDN.for_piece(n, bids, specs, own_c, first_hash, dispatch[0], p["merged_at"])
            c1r = CK.for_piece(n, sorted(set(specs) | spec_files), ids, qids)
            Ms.append({"repository": name, "number": n, "created": p["created_at"], "merged_at": p["merged_at"], "closed": p["closed_at"], "merged": True,
                       "merge_commit": p["_merge"], "merging_account_class": merger_class(mc["an"], mc["ae"]),
                       "head_prefix": branch_prefix(p["head_ref"]), "head_label": lab(p["head_ref"]),
                       "dispatch": dispatch[0], "dispatch_from": dispatch[1], "briefs": br, "commits": cf, "files": files,
                       "questions_decisions": qd, "first_check": first_check(R, kind_files, specs, n), "rt3b_matches": rt3b,
                       "questions_decisions_named": qdn, "c1_records": c1r, "comment_records": crec(n),
                       "after_merge": {"days30_complete": t0 + DAY30 <= CUT, "later_prs_sharing_a_file": later_prs,
                                       "later_commits_naming_it": later_named, "reverts_naming_it": reverts, "reopens_marks": marks}})
        # frame D
        Ds = []
        for h in R.on_main:
            c = R.commits[h]
            if h in in_pr or not (WIN0 <= T(c["ad"]) < CUT): continue
            Ds.append(commit_fields(R, h))
        Ds.sort(key=lambda d: (d["author_time"], d["hash"]))
        with open(os.path.join(outdir, f"{name}.merged.jsonl"), "w") as fh:     # C1's statement test: every merged pull request by the cut-off
            for p in sorted(merged, key=lambda p: p["number"]):
                fh.write(json.dumps({"number": p["number"], "merged_at": p["merged_at"], "head_prefix": branch_prefix(p["head_ref"]), "head_label": lab(p["head_ref"]),
                                     "merge_commit": p["_merge"], "own_commits": sorted(own[p["number"]])}, sort_keys=True) + "\n")
        for frame, rows in (("M", Ms), ("U", Urows), ("D", Ds)):
            with open(os.path.join(outdir, f"{name}.{frame}.jsonl"), "w") as fh:
                for row in rows: fh.write(json.dumps(row, sort_keys=True) + "\n")
        summary[name] = {"default_branch_at_cutoff": R.cut, "github_records": "read", "M": len(Ms), "U": len(Urows), "D": len(Ds),
                         "github_merged_in_window": sum(1 for p in gh_merged if WIN0 <= T(p["merged_at"]) < CUT),
                         "github_merged_all": len(gh_merged), "merged_with_no_row": no_row,
                         "git_github_merge_commits_in_window": len(git_merges), "git_merge_commits_matching_no_listed_pull_request": unlisted,
                         "control_values_with_no_control_file": sorted(NO_CONTROL[name]),
                         "brief_values_with_unmatched_suffix": sorted(UNMATCHED[name]),
                         "control_values_whose_dispatch_log_time_differs": sorted(CTRL_CHECK[name].values(), key=lambda d: d["control"]),
                         "M_30_days_complete": sum(1 for m in Ms if m["after_merge"]["days30_complete"]),
                         "closed_unmerged_after_cutoff_left_out": len(U_open_or_late),
                         "widened": {"merged_by_cutoff": len(merged), "c1_branches_heading_more_than_one_merged_pull_request": CK.shared_heads,
                                     "c1_check_records_at_cutoff_by_kind": dict(sorted(collections.Counter(r["kind"] for r in CK.recs).items())),
                                     "question_and_decision_records_first_added_by_cutoff": len(QDN.recs)}}
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
