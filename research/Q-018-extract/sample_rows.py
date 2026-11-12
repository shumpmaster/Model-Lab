"""Write sample.jsonl: the extract's line for each drawn pull request or commit, with the GitHub fields of
github_reads.json added (README). Run as: python3 -I -B sample_rows.py <this folder>. Also fills frame U's
closing_account_class in the U files."""
import json, os, sys
D = sys.argv[1]
S = json.load(open(os.path.join(D, "sample.json"))); G = json.load(open(os.path.join(D, "github_reads.json")))
def cls(login): return "owner" if login == "shumpmaster" else ("bot" if login.endswith("[bot]") else "other")
rows = {}
for r in ["Model-Lab", "Service-Desk", "Personal-Org-Operating-Model"]:
    for f in "MUD":
        p = os.path.join(D, f"{r}.{f}.jsonl"); L = [json.loads(l) for l in open(p)]
        if f == "U":
            for u in L: u["closing_account_class"] = cls(G["closing_accounts"][r][str(u["number"])])
            with open(p, "w") as fh:
                for u in L: fh.write(json.dumps(u, sort_keys=True) + "\n")
        for x in L: rows[(r, f, x["hash"] if f == "D" else x["number"])] = x
def gh(r, x, f):
    if f == "D": return x
    end = x.get("merged_at") or x.get("closed")
    cs = G["comments"].get(r, {}).get(str(x["number"]), [])
    oc = [t for a, t in cs if cls(a) == "owner"]
    x = dict(x, reviews=[], owner_comments={"on_pull_request": {"before_merge_or_close": sum(1 for t in oc if t < end), "after": sum(1 for t in oc if t >= end)},
                                           "on_lines": {"before_merge_or_close": 0, "after": 0}},
             other_comments=len(cs) - len(oc))
    return x
out = []
for r, ns in S["random_part"].items():
    for n in ns: out.append(dict(gh(r, rows[(r, "M", n)], "M"), drawn_as="random", frame="M"))
for case, v in S["edge_case_part"].items():
    if v == "not seen": continue
    for e in v: out.append(dict(gh(e["repository"], rows[(e["repository"], e["frame"], e["key"])], e["frame"]), drawn_as=case, frame=e["frame"], repository=e["repository"]))
with open(os.path.join(D, "sample.jsonl"), "w") as fh:
    for x in out: fh.write(json.dumps(x, sort_keys=True) + "\n")
print(len(out), "lines")
