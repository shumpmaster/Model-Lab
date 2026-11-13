# Orchestrator helper: adds to the Critic's step-5 records pack (built by pack.py) the records the widened
# fields name (brief 299). Free text; the pack is never committed. Run after pack.py:
#   P=<out dir> HC=<clones dir> python3 -I -B pack2.py
# Each in-window commit is matched to its record's history as extract.py reads it (its qd_history, from the first add on),
# one to one in (commit time, hash) order, so commits sharing a commit time are each shown once (brief 307; brief 304,
# finding 7 note); a record named by more than one sampled piece gets each piece's window, and each commit's diff once.
import json, os, sys, subprocess, hashlib, importlib.util
P = os.environ["P"]; HC = os.environ.get("HC", "/home/user/hc"); D = os.path.dirname(os.path.abspath(__file__))
sys.argv = [sys.argv[0], "x"]
_spec = importlib.util.spec_from_file_location("ex", os.path.join(D, "extract.py")); ex = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(ex)
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
class _R: pass
_hist = {}
def history(r, p):
    """The record's first add (hash, time) and the commits extract.py reads in it after that, as (hash, time)."""
    if (r, p) not in _hist:
        R = _R(); R.path = os.path.join(HC, r); R.cut = cut[r]; R.name = r
        fa = ex.first_adds_full(R, [p], lambda q: q == p).get(p)
        _hist[(r, p)] = (fa, [(h, t) for h, t, _, _ in ex.qd_history(R, p) if fa and (t, h) >= (fa[1], fa[0])])
    return _hist[(r, p)]
# brief 323: the ledger entries the widened `ledger_entries` field lists, each as the commit that first adds it left it
LX = {}
class _RL: pass
_RLx = _RL(); _RLx.path = os.path.join(HC, "Personal-Org-Operating-Model"); _RLx.cut = cut.get("Personal-Org-Operating-Model"); _RLx.name = "Personal-Org-Operating-Model"
_RLx.show = lambda rev, path: subprocess.run(["git", "-C", _RLx.path, "show", f"{rev}:{path}"], capture_output=True, text=True).stdout or None
if _RLx.cut: LX = ex.ledger_index(_RLx)
coding = []   # (line, repository, key, kind, label, commit) for every first add and append the Critic codes (later_work)
shown = {}
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
            fa, hist = history(r, p) if p != "?" else (None, [])
            rec = f"{P}/records2/{r}--{q['label']}.md"
            if fa:
                body = []
                if rec not in shown:
                    shown[rec] = set()
                    body += [f"<!-- {r}:{p} as first added in {fa[0]} at {fa[1]} -->", git(r, "show", f"{fa[0]}:{p}")]
                win = [(h, t) for h, t in hist if x.get("dispatch") and x["dispatch"] < t < x["merged_at"]]
                wc = q.get("window_commits") or []
                assert [t for _, t in win] == [w.get("commit_time") for w in wc], (r, key, p)
                if wc: body.append(f"\n<!-- the window of sample.jsonl line {i} ({r} #{key}): {len(wc)} commit(s) -->")
                for (h, t), w in zip(win, wc):
                    what = "first add" if w.get("first_add") else ("append, listed as not an append" if w.get("not_an_append") else "append")
                    coding.append((i, r, key, what + ("" if w.get("read_for_piece") else " (before the record names the piece: read_for_piece false)"), q["label"], h))
                    if h in shown[rec]:
                        body.append(f"\n<!-- in-window commit {h} at {t} : {json.dumps(w)} ; its diff is shown above -->")
                    else:
                        shown[rec].add(h)
                        body.append(f"\n<!-- in-window commit {h} at {t} : {json.dumps(w)} -->\n```diff\n" + git(r, "show", "--format=", h, "--", p) + "\n```")
                if body: open(rec, "a").write("\n".join(body) + "\n")
    le = x.get("ledger_entries") or []
    if le:
        out.append("\n## Widened (brief 323): ledger entries quoting the owner first added in its window (records2/ holds each as first added)")
        for e in le:
            out.append(f"- {e['label']} → docs/LEDGER.md entry: {json.dumps(e)}")
            fx = LX.get(e["label"])
            rec = f"{P}/records2/{r}--ledger-{e['label']}.md"
            if fx and not os.path.exists(rec):
                open(rec, "w").write(f"<!-- {r}:docs/LEDGER.md, the entry as first added in {fx['hash']} at {fx['time']} -->\n" + fx["text"] + "\n")
            coding.append((i, r, key, "ledger entry, first add", e["label"], fx["hash"] if fx else "?"))
    if x["frame"] != "D":
        bn = sorted({b["brief"] for b in x.get("briefs") or []})
        sp = sorted({s for c in x.get("commits") or [] for s in c.get("spec") or []})
        out.append(f"\n## Widened (brief 323): the brief numbers its trailers name: {json.dumps(bn)}; the spec ids its `Spec:` trailers give: {json.dumps(sp)}")
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
with open(P + "/CODING.md", "w") as fh:
    fh.write("# What the Critic codes for `later_work` (S-002 step 3, *Later work*; brief 323)\n\nOne line per record's first add or append that the extract's *Questions and decisions* (`questions_decisions_named`, its in-window `window_commits`) and *Ledger entries* (`ledger_entries`) fields list for a sampled piece: the sample.jsonl line, the piece, what it is, the record's label and the commit. The piece's file L<nn>-… gives the fields; records2/ gives the text.\n\n")
    for c in coding: fh.write(f"- L{c[0]:02d} {c[1]} #{c[2]}: {c[3]}, {c[4]}, {c[5]}\n")
print(n, len(coding))
