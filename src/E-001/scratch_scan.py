#!/usr/bin/env python3
"""E-001 step 2: which helpers named which files in the shared session scratchpad (/tmp/...).
F4 allows /tmp files a run creates itself; a file named by two runs could be a cross-run read.
Usage: scratch_scan.py <subagents dir> <scratchpad dir> <agent id>..."""
import json, re, sys, collections
d, pad, ids = sys.argv[1], sys.argv[2].rstrip('/'), sys.argv[3:]
pat = re.compile(re.escape(pad) + r"(/[A-Za-z0-9._/-]*)?")
by_file = collections.defaultdict(set)
for a in ids:
    for n, line in enumerate(open(f"{d}/agent-{a}.jsonl"), 1):
        rec = json.loads(line)
        c = (rec.get("message") or {}).get("content")
        if not isinstance(c, list):
            continue
        for b in c:
            if b.get("type") != "tool_use":
                continue
            s = json.dumps(b["input"])
            # expand $S-style variables set to the pad
            for m in pat.finditer(s):
                by_file[m.group(1) or "/"].add((a, n))
            for v in re.findall(r"(\w+)=" + re.escape(pad), s):
                for m in re.finditer(r"\$\{?" + v + r"\}?(/[A-Za-z0-9._/-]*)", s):
                    by_file[m.group(1)].add((a, n))
for f, uses in sorted(by_file.items()):
    agents = sorted({a for a, _ in uses})
    print(f"{'SHARED ' if len(agents) > 1 else ''}{f}: " + ", ".join(f"{a}:{sorted(n for x, n in uses if x == a)[:6]}" for a in agents))
