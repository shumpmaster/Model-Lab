"""Compare the extract before and after brief 294 on the keys it had before (README, "The old fields, unchanged").
Run as: python3 -I -B compare_old_new.py <the folder before> <the folder after>. Prints, per file, rows whose old keys differ."""
import json,sys,os
O,N=sys.argv[1],sys.argv[2]
ORDERLESS={"later_commits_naming_it"}
def norm(x,k=None):
    if isinstance(x,dict): return {a:norm(b,a) for a,b in x.items()}
    if isinstance(x,list):
        y=[norm(v) for v in x]
        return sorted(y,key=lambda v: json.dumps(v,sort_keys=True)) if k in ORDERLESS else y
    return x
def onold(o,n):
    if isinstance(o,dict): return {k:onold(o[k],n.get(k) if isinstance(n,dict) else None) for k in o}
    if isinstance(o,list) and isinstance(n,list) and len(o)==len(n): return [onold(a,b) for a,b in zip(o,n)]
    return n
tot={}
for f in sorted(os.listdir(O)):
    if not f.endswith(".jsonl") or f.endswith(".list.jsonl"): continue
    A=[json.loads(l) for l in open(os.path.join(O,f))]; B=[json.loads(l) for l in open(os.path.join(N,f))]
    key=(lambda x:(x.get("repository"),x.get("drawn_as"),x.get("number") or x.get("hash"))) if f=="sample.jsonl" else (lambda x:x.get("number") or x.get("hash"))
    ka={key(x):x for x in A}; kb={key(x):x for x in B}
    same_order=[key(x) for x in A]==[key(x) for x in B]
    raw=strict=0; newkeys=set()
    for k,a in ka.items():
        b=kb.get(k)
        if b is None: print(f,"missing",k); continue
        newkeys|=set(b)-set(a)
        if onold(a,b)!=a: strict+=1
        if norm(onold(a,b))!=norm(a): raw+=1; print(f,k,"DIFF on old keys")
    print(f"{f}: rows old {len(A)} new {len(B)}; same keys {set(ka)==set(kb)}; same line order {same_order}; rows whose old keys differ only in order of later_commits_naming_it {strict-raw}; rows whose old keys differ otherwise {raw}; new keys {sorted(newkeys)}")
fo=json.load(open(os.path.join(O,"frames.json"))); fn=json.load(open(os.path.join(N,"frames.json")))
print("frames.json old keys equal:", all(fo[r]=={k:fn[r][k] for k in fo[r]} for r in fo), "new keys:", sorted(set(fn["Model-Lab"])-set(fo["Model-Lab"])))
for r in fo: print(r, {k:fo[r][k] for k in ("M","U","D","M_30_days_complete")})
