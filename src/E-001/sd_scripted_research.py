#!/usr/bin/env python3
"""E-001 step 1, SD scripted research: for each item, find the round-1 researcher dispatch's
control record, its recorded brief and manifest, the commit that first adds the memo and its
parent (F1: parent of the work's first commit), and check each manifest entry's sha256 against
the file at that parent (F2). Read-only on the clone."""
import hashlib, json, subprocess, sys
SD = "/home/user/Service-Desk"
def git(*a, check=True):
    r = subprocess.run(["git", "-C", SD, *a], capture_output=True)
    if check and r.returncode: return None
    return r.stdout
def first_add(path):
    out = git("log", "--all", "--diff-filter=A", "--reverse", "--format=%H %P", "--", path).decode().split("\n")
    out = [l for l in out if l]
    return out[0].split() if out else None
for item in sys.argv[1:]:
    print(f"## {item}")
    log = git("show", f"HEAD:dispatch-log/2026-10.jsonl").decode().splitlines()
    disp = [(i+1, json.loads(l)) for i, l in enumerate(log) if l.strip()]
    d1 = [(n, e) for n, e in disp if e.get("item") == item and e.get("action") == "dispatch" and e.get("role") == "researcher"]
    o1 = [(n, e) for n, e in disp if e.get("item") == item and e.get("trigger") == "outcome" and e.get("role") == "researcher"]
    print("researcher dispatch lines:", [(n, e["time"], e["route"]) for n, e in d1][:3])
    print("researcher outcome lines:", [(n, e["result"], e.get("record")) for n, e in o1][:3])
    sc = [(n, e.get("verdict")) for n, e in disp if e.get("item") == item and e.get("trigger") == "outcome" and e.get("role") == "source-checker"]
    print("source-check outcome lines:", sc)
    if not d1: continue
    t = d1[0][1]["time"]
    # control record with that dispatch time, anywhere in history
    files = git("log", "--all", "--diff-filter=A", "--format=", "--name-only", "--", f"reviews/{item}/_control/").decode().split()
    ctl = None
    for f in files:
        c = first_add(f)
        blob = git("show", f"{c[0]}:{f}")
        j = json.loads(blob)
        if j.get("dispatched_at") == t and j.get("role") == "researcher":
            ctl = (f, c[0], j); break
    if not ctl: print("no control record for", t); continue
    f, cadd, j = ctl
    print("control:", f, "added in", cadd[:7])
    print("brief:", json.dumps(j["brief"]))
    print("model:", j.get("model"), "tools:", j.get("tools"), "source_tip:", j.get("source_tip"))
    memo = f"research/{item}-memo.md"
    fa = first_add(memo)
    print("memo first added:", fa[0][:7], "parent:", fa[1][:7])
    start = fa[1]
    ok = True
    for p, h in j["manifest"].items():
        if p == "BRIEF.md":
            hh = hashlib.sha256(j["brief"].encode()).hexdigest()
            print(f"  BRIEF.md (from control brief text) sha {'match' if hh==h else 'DIFF'}")
            continue
        b = git("show", f"{start}:{p}")
        if b is None: print(f"  {p}: MISSING at {start[:7]}"); ok = False; continue
        hh = hashlib.sha256(b).hexdigest()
        print(f"  {p}: {'match' if hh==h else 'DIFF'} at {start[:7]}"); ok &= hh == h
    print("F2 manifest all match:", ok)
