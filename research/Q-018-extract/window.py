# Orchestrator helper: the E-RT4 window lists for the records pack. Run: P=<out dir> python3 -I -B window.py
import json, os, subprocess, hashlib
P=os.environ["P"]; D=os.path.dirname(os.path.abspath(__file__))
cut={r:v["default_branch_at_cutoff"] for r,v in json.load(open(D+"/frames.json")).items()}
def git(r,*a): return subprocess.run(["git","-C","/home/user/hc/"+r,*a],capture_output=True,text=True).stdout
first={}
for r in cut:
    cur=None
    for line in git(r,"log",cut[r],"--diff-filter=A","--no-renames","--name-only","--format=\x1e%H %cI","--","questions/","decisions/").split("\n"):
        if line.startswith("\x1e"): cur=line[1:].split()
        elif line and cur:
            t=cur[1]
            import datetime as dt
            t=dt.datetime.fromisoformat(t).astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            k=(r,line)
            if k not in first or t<first[k][1]: first[k]=(cur[0],t)
os.makedirs(P+"/window",exist_ok=True)
out=["# Every question and decision file first added between each sampled piece's dispatch and merge (for E-RT4), whether or not it names the piece","","Order: sample.jsonl line order; and, after it, each piece's place in the SHA-256 order of `S-002-handcheck:<repository>:<number>` (lowest first) across the three repositories.",""]
rows=[]
for i,l in enumerate(open(D+"/sample.jsonl"),1):
    x=json.loads(l)
    if x["frame"]!="M" or not ({f["class"] for f in x["files"]} & {"built","plan","research"}): continue
    r=x["repository"]; n=x["number"]
    h=hashlib.sha256(f"S-002-handcheck:{r}:{n}".encode()).hexdigest()
    ins=sorted((t,p,c) for (rr,p),(c,t) in first.items() if rr==r and x["dispatch"]<=t<=x["merged_at"])
    rows.append((h,i,r,n,x["dispatch"],x["merged_at"],ins))
for rank,(h,i,r,n,d,m,ins) in enumerate(sorted(rows),1): pass
hr={row[1]:k for k,row in enumerate(sorted(rows),1)}
for h,i,r,n,d,m,ins in rows:
    out.append(f"## L{i} {r}#{n} (hash-order place {hr[i]} of {len(rows)} sampled pieces by RP2's file classes): dispatch {d}, merged {m}")
    for t,p,c in ins:
        fn=f"{r}--{p.replace('/','__')}"
        open(f"{P}/window/{fn}","w").write(f"<!-- {r}:{p} as first added in {c} at {t} -->\n"+git(r,"show",f"{c}:{p}"))
        out.append(f"- {t} {p} → window/{fn}")
    if not ins: out.append("- none")
open(P+"/E-RT4-windows.md","w").write("\n".join(out)+"\n")
print(len(rows))
