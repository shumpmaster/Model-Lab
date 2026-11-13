# Orchestrator helper: builds the Critic's step-5 records pack (free text; never committed). Run: P=<out dir> HC=<clones dir> python3 -I -B pack.py
import json, os, sys, subprocess, hashlib, re
sys.argv=[sys.argv[0],"x"]
import importlib.util
spec=importlib.util.spec_from_file_location("ex",os.path.join(os.path.dirname(os.path.abspath(__file__)),"extract.py")); ex=importlib.util.module_from_spec(spec); spec.loader.exec_module(ex)
P=os.environ["P"]; D=os.path.dirname(os.path.abspath(__file__))
HC=os.environ.get("HC","/home/user/hc")
def git(r,*a): return subprocess.run(["git","-C",os.path.join(HC,r),*a],capture_output=True,text=True).stdout
cut={r:v["default_branch_at_cutoff"] for r,v in json.load(open(D+"/frames.json")).items()}
labels={}
for r in ex.REPOS:
    for p in git(r,"log",cut[r],"--all","--name-only","--format=","--no-renames").split("\n")+git(r,"ls-tree","-r","--name-only",cut[r]).split("\n"):
        if p: labels.setdefault(r,{})[ex.lab(p)]=p
os.makedirs(P+"/records",exist_ok=True)
idx=[]
for i,l in enumerate(open(D+"/sample.jsonl"),1):
    x=json.loads(l); r=x["repository"]; L=labels[r]
    key=x.get("number") or x["hash"]
    out=[f"# sample.jsonl line {i}: {r} {'#'+str(key) if x.get('number') else 'commit '+key} (drawn as {x['drawn_as']}, frame {x['frame']})",""]
    if x.get("files") is not None and x["frame"]!="D":
        out.append("## Files (label → real path, class)")
        for f in x["files"]: out.append(f"- {f['label']} → {L.get(f['label'],'?')} ({f['class']}, {'/'.join(f['status'])}, +{f['added']} -{f['removed']})")
    out.append("\n## Commits (full message)")
    for c in ([x] if x["frame"]=="D" else x["commits"]):
        out.append(f"### {c['hash']} (author {c['author_class']}, committer {c['committer_class']}, {c['author_time']})")
        out.append("```\n"+git(r,"log","-1","--format=%B",c["hash"]).strip()+"\n```")
        out.append("files: "+", ".join(f"{L.get(f['label'],'?')} ({f['class']})" for f in c.get("files",[])))
    if x.get("questions_decisions"):
        out.append("\n## Question and decision records naming it (path, first added, text as first added in records/)")
        for q in x["questions_decisions"]:
            p=L.get(q["label"],"?"); out.append(f"- {q['label']} → {p}, {q['kind']}, first added {q['first_added']}, names by {q['names_by']}")
            h=git(r,"log",cut[r],"--diff-filter=A","--format=%H %cI","--",p).split("\n")
            h=sorted([y.split() for y in h if y],key=lambda y:y[1])
            if h:
                fn=f"{P}/records/{r}--{q['label']}.md"
                if not os.path.exists(fn): open(fn,"w").write(f"<!-- {r}:{p} as first added in {h[0][0]} at {h[0][1]} -->\n"+git(r,"show",f"{h[0][0]}:{p}"))
    for fc in x.get("first_check") or []:
        out.append(f"\n## First-check record found: {fc}")
    if x.get("briefs"): out.append(f"\n## Briefs: {x['briefs']}")
    if x.get("after_merge"): out.append(f"\n## After merge (30 days): {json.dumps(x['after_merge'])}")
    if x.get("rt3b_matches"): out.append(f"\n## RT3(b) matches: {x['rt3b_matches']}")
    for k in ("dispatch","dispatch_from","merged_at","closed","merging_account_class","closing_account_class","head_prefix","owner_comments"):
        if k in x: out.append(f"- {k}: {x[k]}")
    fn=f"{P}/L{i:02d}-{r}-{key}.md"; open(fn,"w").write("\n".join(out)+"\n"); idx.append(os.path.basename(fn))
open(P+"/INDEX.md","w").write("# Records pack for the Critic's step 5 (Q-018)\n\nOne file per sample.jsonl line; question and decision records as first added are in records/<repo>--<label>.md. Built by the Orchestrator from the clones at the cut-off; no coding or results in it. The Critic codes from this pack, not from the full clones, which hold docs/briefs/** and docs/reports/** (S-002 step 3, *Later work*; governance/PACKS.toml [roles.critic]); brief 323.\n\n"+"\n".join("- "+n for n in idx)+"\n")
print(len(idx))
