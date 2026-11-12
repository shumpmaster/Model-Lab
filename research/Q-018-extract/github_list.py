# Orchestrator helper: turns the connector's saved list_pull_requests results into <github dir>/<repo>.list.jsonl (README, "The GitHub input"). Edit T to the folder holding the saved results.
import json,sys,glob
T='/root/.claude/projects/-home-user/30b94246-fed8-5fa1-8056-3bd31c75ef0f/tool-results/'
out={}
for f in sorted(glob.glob(T+'mcp-github-list_pull_requests-*.txt')):
    txt=open(f).read()
    data=json.loads(txt)
    for p in data:
        repo=p['head']['repo']['full_name'].split('/')[1] if p.get('head',{}).get('repo') else None
        base=p['base']['repo']['full_name'].split('/')[1]
        rec={k:p.get(k) for k in ('number','state','merged','created_at','closed_at','merged_at')}
        rec['head_ref']=p['head']['ref']; rec['head_sha']=p['head']['sha']; rec['base_ref']=p['base']['ref']
        rec['user']=p['user']['login']
        out.setdefault(base,{})[p['number']]=rec
for r,d in out.items():
    with open(f'/home/user/hc/gh/{r}.list.jsonl','w') as fh:
        for n in sorted(d): fh.write(json.dumps(d[n])+'\n')
    print(r,len(d),min(d),max(d), sorted(set(range(1,max(d)+1))-set(d))[:20])
