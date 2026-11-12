# Orchestrator helper: adds to the Critic's step-5 records pack (built by pack.py) the records the widened
# fields name (brief 299). Free text; the pack is never committed. Run after pack.py:
#   P=<out dir> HC=<clones dir> python3 -I -B pack2.py
import json, os, subprocess, hashlib, datetime as dt
P = os.environ["P"]; HC = os.environ.get("HC", "/home/user/hc"); D = os.path.dirname(os.path.abspath(__file__))
def git(r, *a): return subprocess.run(["git", "-C", os.path.join(HC, r), *a], capture_output=True, text=True).stdout
def lab(s): return hashlib.sha1(s.encode()).hexdigest()[:8]
cut = {r: v["default_branch_at_cutoff"] for r, v in json.load(open(D + "/frames.json")).items()}
labels = {}
for r in cut:
    names = git(r, "log", "--all", "--full-history", "--name-only", "--format=", "--no-renames").split("\n")
    names += git(r, "ls-tree", "-r", "--name-only", cut[r]).split("\n")
    for p in names:
        if p: labels.setdefault(r, {})[lab(p)] = p
os.makedirs(P + "/records2", exist_ok=True)
def first_add(r, p):
    h = git(r, "log", "--all", "--full-history", "--diff-filter=A", "--format=%H %cI", "--", p).split("\n")
    h = sorted([y.split() for y in h if y], key=lambda y: y[1])
    return h[0] if h else None
n = 0
for i, l in enumerate(open(D + "/sample.jsonl"), 1):
    x = json.loads(l); r = x["repository"]; L = labels.get(r, {})
    key = x.get("number") or x["hash"]
    fn = f"{P}/L{i:02d}-{r}-{key}.md"
    if not os.path.exists(fn): continue
    out = []
    qd = x.get("questions_decisions_named") or []
    if qd:
        out.append("\n## Widened: question and decision records naming it (records2/ holds each as first added, and each in-window commit's diff)")
        for q in qd:
            p = L.get(q["label"], "?")
            out.append(f"- {q['label']} → {p}: {json.dumps({k: v for k, v in q.items() if k != 'window_commits'})}")
            fa = first_add(r, p) if p != "?" else None
            rec = f"{P}/records2/{r}--{q['label']}.md"
            if fa and not os.path.exists(rec):
                body = [f"<!-- {r}:{p} as first added in {fa[0]} at {fa[1]} -->", git(r, "show", f"{fa[0]}:{p}")]
                hist = {}
                for y in git(r, "log", "--all", "--full-history", "--format=%H %cI", "--", p).split("\n"):
                    if y:
                        hh, tt = y.split()
                        hist.setdefault(dt.datetime.fromisoformat(tt).astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), []).append(hh)
                for w in q.get("window_commits") or []:
                    for h in hist.get(w.get("commit_time"), []):
                        body.append(f"\n<!-- in-window commit {h} at {w.get('commit_time')} : {json.dumps(w)} -->\n```diff\n" + git(r, "show", "--format=", h, "--", p) + "\n```")
                open(rec, "w").write("\n".join(body))
    c1 = x.get("c1_records") or []
    if c1:
        out.append("\n## Widened: C1 check records (records2/ holds each as at the cut-off)")
        for c in c1:
            p = L.get(c["label"], "?")
            out.append(f"- {c['label']} → {p}: {json.dumps(c)}")
            rec = f"{P}/records2/{r}--{c['label']}.md"
            if p != "?" and not os.path.exists(rec):
                open(rec, "w").write(f"<!-- {r}:{p} at the cut-off {cut[r]} -->\n" + git(r, "show", f"{cut[r]}:{p}"))
    for k in ("owner_account_comments", "comment_records", "owner_items_listed_in_window", "k2_roles", "research_questions", "research_memos", "has_memo", "c1_summary"):
        if x.get(k): out.append(f"\n## Widened: {k}: {json.dumps(x[k])}")
    if out:
        open(fn, "a").write("\n".join(out) + "\n"); n += 1
print(n)
