#!/usr/bin/env python3
"""E-001 step 2: check a helper received its brief file byte for byte (transcript line 1)."""
import json, sys
first = json.loads(open(sys.argv[1]).readline())["message"]["content"]
if isinstance(first, list):
    first = "".join(b.get("text", "") for b in first if b.get("type") == "text")
brief = open(sys.argv[2]).read()
print("match" if first == brief else f"DIFFER (transcript {len(first)} chars, file {len(brief)} chars)")
