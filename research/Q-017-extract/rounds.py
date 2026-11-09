"""Build the rounds extract for research question Q-017 (run by the Orchestrator).

Reads, from each repository's origin/main (read-only, with git show and git log), every
verdict file under reviews/, research/*-source-check.md and research/*-entries-check.md,
and, for Service-Desk, the verdict records in dispatch-log/*.jsonl. Writes <repo>.rounds.jsonl:
one line per round, with no text from the records. See README.md for the coding rules.
"""
import json, re, subprocess, datetime, sys
sys.path.insert(0, "/home/user/Model-Lab/research/Q-017-extract")
from extract import redact, utc
def git(repo,*a): return subprocess.run(["git","-C",repo,*a],capture_output=True,text=True).stdout
def norm(v):
    v=v.strip().upper()
    if v.startswith("PASS"): return "pass"
    if v.startswith("FAIL"): return "fail"
    if v in ("NONE",""): return "none"
    return "other"
CHECKERS=[("source-checker","source-checker"),("check-author","check-author"),("design-reviewer","design-reviewer"),("plan-review","reviewer"),("build-review","reviewer"),("reviewer","reviewer"),("review","reviewer"),("critic","critic"),("design","design-reviewer"),("user-rep","user-rep"),("triage","triage"),("owner","owner")]
def checker(path):
    base=path.rsplit("/",1)[-1].lower()
    if base.endswith("-source-check.md") or base.endswith("-entries-check.md"): return "source-checker"
    for k,c in CHECKERS:
        if k in base: return c
    return "unknown"
def first_date(repo,path,needle=None):
    a=["log","origin/main","--format=%cI","--reverse"]
    if needle: a+=["-S",needle]
    else: a+=["--diff-filter=A"]
    out=git(repo,*a,"--",path).split()
    return utc(out[0]) if out else None
def run(repo,name):
    files=[f for f in git(repo,"ls-tree","-r","--name-only","origin/main").splitlines()
           if f.endswith(".md") and (f.startswith("reviews/") or re.match(r"research/.*-(source|entries)-check\.md$",f))]
    rows=[]
    for f in files:
        text=git(repo,"show","origin/main:"+f)
        secs=re.split(r"^## Round (\d+)[^\n]*$",text,flags=re.M)
        stem=re.sub(r"[-_]r(ound)?\d+(?=[-_.])","",f.rsplit("/",1)[-1])
        piece=redact(f.rsplit("/",1)[0]+"/"+stem) if "/" in f else redact(stem)
        m=re.search(r"[-_]r(?:ound)?(\d+)[-_.]",f.rsplit("/",1)[-1])
        if len(secs)>1:
            top=re.search(r"^Verdict: *([^\n]+)",secs[0],re.M)
            for i in range(1,len(secs),2):
                n=int(secs[i]); body=secs[i+1]
                v=re.search(r"^The round's verdict was ([A-Za-z]+)",body,re.M) or re.search(r"^Verdict: *([^\n]+)",body,re.M)
                last=(i==len(secs)-2)
                verdict=norm(v.group(1)) if v else (norm(top.group(1))+"-from-file" if (last and top) else "none")
                rows.append({"source":"verdict-file","file":redact(f),"piece":piece,"checker":checker(f),"round":n,
                    "verdict":verdict,"date":first_date(repo,f,"## Round %d"%n) or first_date(repo,f)})
        else:
            v=re.search(r"^Verdict: *([^\n]+)",text,re.M)
            rows.append({"source":"verdict-file","file":redact(f),"piece":piece,"checker":checker(f),"round":int(m.group(1)) if m else None,
                "verdict":norm(v.group(1)) if v else "none","date":first_date(repo,f)})
    for f in [x for x in git(repo,"ls-tree","-r","--name-only","origin/main").splitlines() if x.startswith("dispatch-log/") and x.endswith(".jsonl")]:
        for line in git(repo,"show","origin/main:"+f).splitlines():
            try:o=json.loads(line)
            except: continue
            if "verdict" in o:
                rows.append({"source":"dispatch-log","file":redact(f),"piece":o.get("item"),"checker":o.get("role"),"round":None,
                    "verdict":norm(str(o["verdict"])),"date":o.get("time"),"record":redact(o["record"]) if o.get("record") else None})
    with open(f"/home/user/Model-Lab/research/Q-017-extract/{name}.rounds.jsonl","w") as out:
        for r in rows: out.write(json.dumps(r)+"\n")
    return rows
for name in ["Service-Desk","Model-Lab","Personal-Org-Operating-Model"]:
    R=run("/home/user/"+name,name)
    import collections
    print(name,len(R),collections.Counter(r["verdict"] for r in R),collections.Counter(r["source"] for r in R),collections.Counter(r["checker"] for r in R).most_common(6))
