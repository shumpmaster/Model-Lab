"""Build the commit extract for research question Q-017 (run by the Orchestrator).

For each repository, one JSON line per commit reachable from origin/main:
hash, parents, author date, author name, author class, committer name, subject, and
per changed path its added and removed line counts (numstat; binary files show null).
Author class: "agent" for an address ending in agents.invalid, "owner" for the GitHub
account shumpmaster and the addresses it uses, "other" for anything else. Addresses are
not written. A commit that changes any path under questions/, decisions/, docs/projects/,
docs/PROJECT.md, ideas/ or sessions/chief-of-staff/, or any *-notes.md file, has its subject
left out, so the extract carries no wording from those records.
"""
import json, subprocess, sys
OWNER_NAMES = {"shumpmaster"}
def cls(name, email):
    if email.endswith("@agents.invalid"): return "agent"
    if name in OWNER_NAMES or email.endswith("+shumpmaster@users.noreply.github.com") or email == sys.argv[1]: return "owner"
    return "other"
def run(repo, out):
    fmt = "%x1e%H%x1f%P%x1f%aI%x1f%an%x1f%ae%x1f%cn%x1f%s"
    raw = subprocess.run(["git","-C",repo,"log","origin/main","--numstat","--no-renames","--format="+fmt],capture_output=True,text=True,check=True).stdout
    with open(out,"w") as f:
        for rec in raw.split("\x1e")[1:]:
            head, _, body = rec.partition("\n")
            h,p,d,an,ae,cn,s = head.split("\x1f")
            files=[]
            for line in body.strip().splitlines():
                a,r,path = line.split("\t",2)
                files.append({"path":path,"added":None if a=="-" else int(a),"removed":None if r=="-" else int(r)})
            PRIV=("questions/","decisions/","docs/projects/","docs/PROJECT.md","ideas/","sessions/chief-of-staff/")
            private = any(x["path"].startswith(PRIV) or x["path"].endswith("-notes.md") for x in files)
            f.write(json.dumps({"hash":h,"parents":p.split(),"date":d,"author":an,"author_class":cls(an,ae),"committer":cn,"subject":None if private else s,"files":files})+"\n")
for name in ["Service-Desk","Model-Lab","Personal-Org-Operating-Model"]:
    run("/home/user/"+name, f"/home/user/Model-Lab/research/Q-017-extract/{name}.jsonl")
