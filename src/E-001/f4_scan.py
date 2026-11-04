#!/usr/bin/env python3
"""E-001 step 2: scan one helper transcript (subagents/agent-<id>.jsonl) for F4.

Lists every tool call with its transcript line, and flags a call when it:
  - names an absolute path outside the copy, other than the allowed system paths
    (/usr, /bin, /lib, /etc read only; /tmp for files the run creates; /dev/null);
  - uses WebFetch or WebSearch (or curl/wget in a command);
  - runs a git command naming another repository (a remote URL, or -C/--git-dir outside the copy).
It also reports the transcript's cwd values and models. It decides nothing borderline:
flagged lines are for the Reviewer to read (E-001 F4). Usage: f4_scan.py <jsonl> <copy path>
"""
import json
import re
import sys

ALLOWED = ("/usr/", "/bin/", "/lib/", "/lib64/", "/etc/", "/tmp/", "/dev/null", "/proc/self/")
PATH_KEYS = ("file_path", "path", "notebook_path")
ABS = re.compile(r"(?<![\w.~-])(/[A-Za-z0-9._@+-][^\s'\"`;|&<>(){}]*)")


def outside(p, copy):
    p = p.rstrip("/")
    if p == copy or p.startswith(copy + "/"):
        return False
    return not any(p == a.rstrip("/") or p.startswith(a) for a in ALLOWED)


def scan(path, copy):
    copy = copy.rstrip("/")
    calls, flags, cwds, models = [], [], set(), set()
    with open(path) as fh:
        for n, line in enumerate(fh, 1):
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            if rec.get("cwd"):
                cwds.add(rec["cwd"])
            msg = rec.get("message") or {}
            if msg.get("model"):
                models.add(msg["model"])
            content = msg.get("content")
            if not isinstance(content, list):
                continue
            for block in content:
                if not isinstance(block, dict) or block.get("type") != "tool_use":
                    continue
                name, inp = block.get("name"), block.get("input") or {}
                calls.append((n, name))
                why = []
                if name in ("WebFetch", "WebSearch"):
                    why.append("web tool")
                for k in PATH_KEYS:
                    v = inp.get(k)
                    if isinstance(v, str) and v.startswith("/") and outside(v, copy):
                        why.append(f"{k} outside copy: {v}")
                    if isinstance(v, str) and v.startswith("~"):
                        why.append(f"{k} under home: {v}")
                cmd = inp.get("command")
                if isinstance(cmd, str):
                    for p in ABS.findall(cmd):
                        if outside(p, copy):
                            why.append(f"command path outside copy: {p}")
                    if re.search(r"(^|[\s;&|])~(/|\s|$)", cmd) or "$HOME" in cmd:
                        why.append("command names the home directory")
                    if re.search(r"\b(curl|wget)\b", cmd):
                        why.append("command may fetch the web")
                    if re.search(r"\bgit\b", cmd) and re.search(r"https?://|git@|\bgit\s+(fetch|pull|clone|ls-remote|push|remote)\b", cmd):
                        why.append("git command may reach another repository")
                if why:
                    flags.append((n, name, why, json.dumps(inp)[:300]))
    return calls, flags, sorted(cwds), sorted(models)


if __name__ == "__main__":
    calls, flags, cwds, models = scan(sys.argv[1], sys.argv[2])
    print(f"transcript: {sys.argv[1]}")
    print(f"tool calls: {len(calls)}; cwd values: {cwds}; models: {models}")
    print(f"flagged calls: {len(flags)}")
    for n, name, why, inp in flags:
        print(f"  line {n} {name}: {'; '.join(why)} | {inp}")
