"""Build the commit and pull-request extract for research question Q-017 (run by the Orchestrator).

Run as: python3 extract.py <the owner's configured git address>. The address is used only to class
commits and is not written anywhere.

Writes, per repository, <name>.commits.jsonl (one line per commit reachable from origin/main) and
<name>.prs.jsonl (one line per pull request merged into it). No commit subjects or messages are
written. Dates are in UTC. Paths that name the owner's records, or a project item, are replaced by
an opaque label (see README.md).
"""
import json, re, subprocess, sys, hashlib, datetime
OWNER_ADDR = sys.argv[1] if len(sys.argv)>1 else ""
PRIV = [("questions/","questions"),("decisions/","decisions"),("docs/projects/","project-plan"),
        ("docs/PROJECT.md","project-plan"),("ideas/","ideas"),("sessions/chief-of-staff/","cos-session")]
def oid(s): return hashlib.sha1(s.encode()).hexdigest()[:8]
def redact(path):
    for pre,lab in PRIV:
        if path.startswith(pre) or ("/"+pre) in path: return f"<{lab}:{oid(path)}>"
    if path.endswith("-notes.md"): return f"<notes:{oid(path)}>"
    if path.startswith("docs/handoff/") or "chief-of-staff" in path: return f"<cos-handoff:{oid(path)}>"
    return "/".join(("item-"+oid(seg)) if re.search(r"(?i)p-?\d{3}|widget", seg) else seg for seg in path.split("/"))
def cls(name, email):
    if email.endswith("@agents.invalid"): return "agent"
    if name == "shumpmaster" or email == OWNER_ADDR or email.endswith("+shumpmaster@users.noreply.github.com"): return "owner"
    return "other"
def utc(s): return datetime.datetime.fromisoformat(s).astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def git(repo,*a): return subprocess.run(["git","-C",repo,*a],capture_output=True,text=True,check=True).stdout
def run(repo, name):
    fmt="%x1e%H%x1f%P%x1f%aI%x1f%cI%x1f%an%x1f%ae%x1f%cn%x1f%s%x1f%b"
    raw=git(repo,"log","origin/main","--numstat","--no-renames","--format="+fmt)
    st={}
    cur=None
    for line in git(repo,"log","origin/main","--name-status","--no-renames","--format=%x1e%H").split("\n"):
        if line.startswith("\x1e"): cur=line[1:]; st[cur]={}
        elif "\t" in line and cur:
            s,path=line.split("\t",1); st[cur][path]=s[0]
    commits={}
    for rec in raw.split("\x1e")[1:]:
        head,_,rest=rec.partition("\x1f")
        h=head; p,ad,cd,an,ae,cn,s,tail=rest.split("\x1f",7)
        body,_,num=tail.partition("\n\n") if "\t" not in tail.split("\n")[0] else ("",None,tail)
        files=[]
        for line in tail.splitlines():
            parts=line.split("\t")
            if len(parts)==3 and (parts[0].isdigit() or parts[0]=="-"):
                a,r,path=parts; files.append({"path":redact(path),"status":{"A":"added","M":"modified","D":"deleted"}.get(st.get(h,{}).get(path),"other"),"added":None if a=="-" else int(a),"removed":None if r=="-" else int(r)})
        m=re.match(r"Merge pull request #(\d+)\b",s)
        sq=re.search(r"\(#(\d+)\)$",s)
        coauth=[cls(n.strip(),e.strip()) for n,e in re.findall(r"^Co-authored-by:\s*(.*?)\s*<([^>]+)>",tail,re.M)]
        two=len(p.split())>1
        kind="merge-pr" if (two and cn=="GitHub" and (m or sq)) else ("other-merge" if two else "plain")
        commits[h]={"hash":h,"parents":p.split(),"author_date":utc(ad),"commit_date":utc(cd),"author":an,"author_class":cls(an,ae),
            "committer":cn,"kind":kind,"pr":(int(m.group(1)) if m else (int(sq.group(1)) if sq else None)) if kind=="merge-pr" else None,
            "revert":s.startswith("Revert"),"mentions_prs":sorted({int(x) for x in re.findall(r"#(\d+)",s)}-(({int(m.group(1))} if m else set())|({int(sq.group(1))} if sq else set()) if kind=="merge-pr" else set())),
            "co_author_classes":coauth,"files":files}
    with open(f"/home/user/Model-Lab/research/Q-017-extract/{name}.commits.jsonl","w") as f:
        for c in commits.values(): f.write(json.dumps(c)+"\n")
    with open(f"/home/user/Model-Lab/research/Q-017-extract/{name}.prs.jsonl","w") as f:
        for c in commits.values():
            if c["kind"]!="merge-pr": continue
            if True:
                inner=[x for x in git(repo,"rev-list",f"{c['parents'][0]}..{c['parents'][1]}").split() if x in commits]
            else: inner=[c["hash"]]
            fl={}
            for h in inner:
                for x in commits[h]["files"]:
                    d=fl.setdefault(x["path"],{"path":x["path"],"added":0,"removed":0})
                    d["added"]+=x["added"] or 0; d["removed"]+=x["removed"] or 0
            cc={}
            for h in inner: cc[commits[h]["author_class"]]=cc.get(commits[h]["author_class"],0)+1
            f.write(json.dumps({"pr":c["pr"],"merged_at":c["commit_date"],
                "merge_commit":c["hash"],"merge_commit_author":c["author"],"merge_commit_author_class":c["author_class"],
                "commits":inner,"commit_author_classes":cc,"co_author_classes":sorted(set(sum((commits[h]["co_author_classes"] for h in inner),[]))),
                "files":sorted(fl.values(),key=lambda d:d["path"])})+"\n")
if __name__=="__main__":
    for name in ["Service-Desk","Model-Lab","Personal-Org-Operating-Model"]:
        run("/home/user/"+name, name)
