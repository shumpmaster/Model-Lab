# Orchestrator helper (brief 332): adds the checked `later_work` codes to sample.jsonl (S-002 step 3, *Later work*;
# "What the owner's rulings of 2026-11-12 need of the hand check", item (3)). Run after sample_rows.py:
#   HC=<clones dir> python3 -I -B later_work.py <this folder>
# The codes come from the two review records, reviews/Q-018-later-work/_critic-coder-verbatim.md (the Critic's 131
# codes, brief 328) and _critic-check-verbatim.md (the second Critic's check, brief 330). A code the second Critic did
# not confirm is taken as "not said" (S-002 step 3). The script rebuilds, as pack2.py builds CODING.md, the list of
# every first add and append the Critic codes, in CODING.md's order, places each code on the `window_commits` entry
# or `ledger_entries` entry it names by sample line, label and commit, and checks that every code is placed once.
# It writes no text: per entry, `later_work` holds the code taken, the commit, the row of the two records and both
# Critics' codes.
# Since brief 340: rows 60 and 61 (Personal-Org-Operating-Model #49, de17627b at 568cd6e0 and 0e57b841), "not said"
# when the second Critic did not confirm them, take "this piece" under the owner's ruling on a plan a piece's own work
# wrote (decisions/questions/P-002-plan-written-by-piece.md), as the third record, _critic-reread-verbatim.md (brief
# 339), confirms; it changes none of the other codes. Those two entries also hold `reread`, the re-read's code.
import json, os, sys, subprocess, hashlib, importlib.util
D = os.path.abspath(sys.argv[1]); HC = os.environ["HC"]
REV = os.path.join(D, "..", "..", "reviews", "Q-018-later-work")
sys.argv = [sys.argv[0], "x"]
_spec = importlib.util.spec_from_file_location("ex", os.path.join(D, "extract.py")); ex = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(ex)
CODES = {"this piece", "later work", "not said"}
def rows(path, width):
    out = []
    for l in open(path):
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) == width and c[0].isdigit(): out.append(c)
    return out
coder = rows(os.path.join(REV, "_critic-coder-verbatim.md"), 8)       # # | Sample line | Piece | Kind | Label | Commit | Code | Reason
check = rows(os.path.join(REV, "_critic-check-verbatim.md"), 6)       # Row | Label | Commit | Coder's code | My code | Reason
assert [int(c[0]) for c in coder] == list(range(1, 132)), "the coder's table is not rows 1 to 131"
assert all(c[6] in CODES for c in coder)
notconf = {int(c[0]): c for c in check}
for n, c in notconf.items():
    k = coder[n - 1]
    assert (c[1], c[2], c[3]) == (k[4], k[5], k[6]) and c[4] in CODES and c[4] != c[3], n
# The re-read (brief 339): no code of the table changes, and rows 60 and 61 read "this piece".
REREAD = {60: "this piece", 61: "this piece"}
_rr = open(os.path.join(REV, "_critic-reread-verbatim.md")).read()
assert "Changed: 0 of 61" in _rr and "| (none) |" in _rr
assert '**Rows 60 and 61 (Personal-Org-Operating-Model #49, label de17627b, commits 568cd6e0 and 0e57b841): confirmed "this piece".**' in _rr
for n in REREAD:
    assert n in notconf and coder[n - 1][4] == "de17627b" and coder[n - 1][6] == "later work" and notconf[n][4] == "this piece", n
KIND = {"first add": "first add", "append": "append", "append (listed as not an append)": "append, listed as not an append",
        "append (before the record names the piece)": "append, before the record names the piece", "ledger": "ledger entry, first add"}
def git(r, *a): return subprocess.run(["git", "-C", os.path.join(HC, r), *a], capture_output=True, text=True).stdout
cut = {r: v["default_branch_at_cutoff"] for r, v in json.load(open(os.path.join(D, "frames.json"))).items()}
labels = {}
for r in cut:
    names = git(r, "log", "--all", "--full-history", "--name-only", "--format=", "--no-renames").split("\n")
    names += git(r, "ls-tree", "-r", "--name-only", cut[r]).split("\n")
    for p in names:
        if p: labels.setdefault(r, {})[hashlib.sha1(p.encode()).hexdigest()[:8]] = p
class _R: pass
def history(r, p):
    R = _R(); R.path = os.path.join(HC, r); R.cut = cut[r]; R.name = r
    fa = ex.first_adds_full(R, [p], lambda q: q == p).get(p)
    return fa, [(h, t) for h, t, _, _ in ex.qd_history(R, p) if fa and (t, h) >= (fa[1], fa[0])]
RL = _R(); RL.path = os.path.join(HC, "Personal-Org-Operating-Model"); RL.cut = cut["Personal-Org-Operating-Model"]; RL.name = "Personal-Org-Operating-Model"
RL.show = lambda rev, path: subprocess.run(["git", "-C", RL.path, "show", f"{rev}:{path}"], capture_output=True, text=True).stdout or None
LX = ex.ledger_index(RL)
# Every sample line's listed first adds and appends, in pack2.py's order; the count must equal the coder's 131 rows.
S = [json.loads(l) for l in open(os.path.join(D, "sample.jsonl"))]
seq = []   # (line, repository, key, kind, label, hash, entry)
for i, x in enumerate(S, 1):
    r = x["repository"]; key = x.get("number") or x["hash"]
    for q in x.get("questions_decisions_named") or []:
        wc = q.get("window_commits") or []
        if not wc: continue
        p = labels[r][q["label"]]
        fa, hist = history(r, p)
        win = [(h, t) for h, t in hist if x.get("dispatch") and x["dispatch"] < t < x["merged_at"]]
        assert [t for _, t in win] == [w.get("commit_time") for w in wc], (r, key, q["label"])
        for (h, t), w in zip(win, wc):
            what = "first add" if w.get("first_add") else ("append, listed as not an append" if w.get("not_an_append") else "append")
            if not w.get("read_for_piece"): what = "append, before the record names the piece" if what == "append" else what + ", before the record names the piece"
            seq.append((i, r, key, what, q["label"], h, w))
    for e in x.get("ledger_entries") or []:
        fx = LX[e["label"]]; assert fx["time"] == e["first_added"], e["label"]
        seq.append((i, r, key, "ledger entry, first add", e["label"], fx["hash"], e))
assert len(seq) == len(coder), (len(seq), len(coder))
placed = 0
for s, c in zip(seq, coder):
    i, r, key, what, label, h, ent = s
    n = int(c[0])
    assert (f"L{i:02d}", f"{r} #{key}", label) == (c[1], c[2], c[4]) and h.startswith(c[5]) and KIND[c[3]] == what, (n, s[:6], c[:6])
    second = notconf[n][4] if n in notconf else "confirmed"
    ent["later_work"] = {"code": "not said" if n in notconf else c[6], "commit": h, "row": n, "first_critic": c[6], "second_critic": second}
    if n in REREAD: ent["later_work"].update(code=REREAD[n], reread=REREAD[n])
    placed += 1
assert len({(s[0], s[4], s[5]) for s in seq}) == len(seq), "a code is placed twice"
with open(os.path.join(D, "sample.jsonl"), "w") as fh:
    for x in S: fh.write(json.dumps(x, sort_keys=True) + "\n")
left = sum(1 for x in S for q in x.get("questions_decisions_named") or [] for w in q.get("window_commits") or [] if "later_work" not in w) + \
       sum(1 for x in S for e in x.get("ledger_entries") or [] if "later_work" not in e)
print(placed, "codes placed;", len(notconf), "not confirmed, of which", len(REREAD), "read \"this piece\" on the re-read and", len(set(notconf) - set(REREAD)), "taken as not said;", left, "listed entries without a code")
