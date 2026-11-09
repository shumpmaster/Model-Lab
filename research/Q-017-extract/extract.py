"""Build the commit and pull-request extract for research question Q-017 (run by the Orchestrator).

Run as: python3 extract.py <the owner's configured git address>. The address is used only to class
commits and is not written anywhere.

Writes, per repository, <name>.commits.jsonl (one line per commit reachable from origin/main) and
<name>.prs.jsonl (one line per pull request merged into it). No commit subjects or messages are
written. Dates are in UTC. Paths that name the owner's records, or a project item, are replaced by
an opaque label (see README.md).
"""
import json, re, subprocess, sys, hashlib, datetime
OWNER_ADDR = sys.argv[1]
PRIV = [("questions/","questions"),("decisions/","decisions"),("docs/projects/","project-plan"),
        ("docs/PROJECT.md","project-plan"),("ideas/","ideas"),("sessions/chief-of-staff/","cos-session")]
def oid(s): return hashlib.sha1(s.encode()).hexdigest()[:8]
def redact(path):
    for pre,lab in PRIV:
        if path.startswith(pre) or ("/"+pre) in path: return f"<{lab}:{oid(path)}>"
    if path.endswith("-notes.md"): return f"<notes:{oid(path)}>"
    return "/".join(re.sub(r"^P-\d{3}.*", lambda m: "P-item-"+oid(m.group(0)), seg) for seg in path.split("/"))
def cls(name, email):
    if email.endswith("@agents.invalid"): return "agent"
    if name == "shumpmaster" or email == OWNER_ADDR or email.endswith("+shumpmaster@users.noreply.github.com"): return "owner"
    return "other"
def utc(s): return datetime.datetime.fromisoformat(s).astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def git(repo,*a): return subprocess.run(["git","-C",repo,*a],capture_output=True,text=True,check=True).stdout
def run(repo, name):
    fmt="%x1e%H%x1f%P%x1f%aI%x1f%cI%x1f%an%x1f%ae%x1f%cn%x1f%s%x1f%b"
    raw=git(repo,"log","origin/main","--numstat","--no-renames","--format="+fmt)
    commits={}
    for rec in raw.split("\x1e")[1:]:
        head,_,rest=rec.partition("\x1f")
        h=head; p,ad,cd,an,ae,cn,s,tail=rest.split("\x1f",7)
        body,_,num=tail.partition("\n\n") if "\t" not in tail.split("\n")[0] else ("",None,tail)
        files=[]
        for line in tail.splitlines():
            parts=line.split("\t")
            if len(parts)==3 and (parts[0].isdigit() or parts[0]=="-"):
                a,r,path=parts; files.append({"path":redact(path),"added":None if a=="-" else int(a),"removed":None if r=="-" else int(r)})
        m=re.match(r"Merge pull request #(\d+) from ([^\s]+)",s)
        sq=re.search(r"\(#(\d+)\)$",s)
        coauth=[cls(n.strip(),e.strip()) for n,e in re.findall(r"^Co-authored-by:\s*(.*?)\s*<([^>]+)>",tail,re.M)]
        two=len(p.split())>1
        kind="merge-pr" if (two and (m or sq)) else ("squash-pr" if (sq and not two) else ("other-merge" if two else "plain"))
        commits[h]={"hash":h,"parents":p.split(),"author_date":utc(ad),"commit_date":utc(cd),"author":an,"author_class":cls(an,ae),
            "committer":cn,"kind":kind,"pr":int(m.group(1)) if m else (int(sq.group(1)) if sq else None),
            "revert":s.startswith("Revert"),"mentions_prs":sorted({int(x) for x in re.findall(r"#(\d+)",s)}-({int(m.group(1))} if m else set())-({int(sq.group(1))} if sq else set())),
            "co_author_classes":coauth,"files":files}
    with open(f"/home/user/Model-Lab/research/Q-017-extract/{name}.commits.jsonl","w") as f:
        for c in commits.values(): f.write(json.dumps(c)+"\n")
    with open(f"/home/user/Model-Lab/research/Q-017-extract/{name}.prs.jsonl","w") as f:
        for c in commits.values():
            if c["kind"] not in ("merge-pr","squash-pr"): continue
            if c["kind"]=="merge-pr":
                inner=[x for x in git(repo,"rev-list",f"{c['parents'][0]}..{c['parents'][1]}").split() if x in commits]
            else: inner=[c["hash"]]
            fl={}
            for h in inner:
                for x in commits[h]["files"]:
                    d=fl.setdefault(x["path"],{"path":x["path"],"added":0,"removed":0})
                    d["added"]+=x["added"] or 0; d["removed"]+=x["removed"] or 0
            cc={}
            for h in inner: cc[commits[h]["author_class"]]=cc.get(commits[h]["author_class"],0)+1
            f.write(json.dumps({"pr":c["pr"],"how":"merge" if c["kind"]=="merge-pr" else "squash","merged_at":c["commit_date"],
                "merge_commit":c["hash"],"merge_commit_author":c["author"],"merge_commit_author_class":c["author_class"],
                "commits":inner,"commit_author_classes":cc,"co_author_classes":sorted(set(sum((commits[h]["co_author_classes"] for h in inner),[]))),
                "files":sorted(fl.values(),key=lambda d:d["path"])})+"\n")
for name in ["Service-Desk","Model-Lab","Personal-Org-Operating-Model"]:
    run("/home/user/"+name, name)
