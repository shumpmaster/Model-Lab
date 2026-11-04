"""How fast new work arrives, from the records (experiments/E-003.md, spec S-001). Standard library
and git only; it reads the three repositories and changes nothing.

Run: python3 experiments/E-003/arrivals.py [--sd DIR] [--poom DIR] [--ml DIR] [--to YYYY-MM-DD]

It prints four things, each with the files or log lines it rests on:
1. Q-008's window. Q-008 counts pieces (docs/PROJECT.md section 6: plans 44, built work 80, research
   19) but states no dates. The window is taken as the dates of the first and last check records
   the count rests on: the first is the build review of the operating model's S-002 (POOM
   reviews/1/reviewer.md, Q-008 section 2.3), the last is Model-Lab's corrections confirmation of
   Q-002 to Q-007 (ML research/Q-002-to-Q-007-corrections-confirmation.md, Q-008 section 2.1).
   As a cross-check it prints, per repository, the first and last date a check record (reviews/**,
   research/*source-check*, dispatch-log/**) was added before Q-008's memo was first committed.
2. The rates over that window, pooled (what section 6's figures imply) and for the Service Desk
   alone (the one project still producing plans and built work: the operating model repository
   has had no commit since 24 October, and Model-Lab's research is this project's own Discovery).
3. The recent pace: the 14 days ending --to, counted mechanically (rules below).
4. Which recent pieces had brief, start commit and model on record at dispatch, and which of these
   fields Model-Lab's brief records (docs/briefs/*.md) carry.

Dates are the dates files were added to git. Some records were filed in batches after the work
(for example SD reviews/S-001-notifications, six rounds filed on 18 October), so a date can be
later than the dispatch; over weeks this moves a rate little, over days it can move it a lot.
"""
import argparse
import datetime as dt
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path

Q008 = {"plans": 44, "built work": 80, "research": 19}  # docs/PROJECT.md:99
Q008_SD = {"plans": 18, "built work": 51, "research": 12}  # Q-008 sections 2.1-2.3: SD 1+17 plans, 51 units, 12 logged items


def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True,
                          check=True).stdout


def added(repo, *paths, since=None, until=None):
    """(date, path) for every file added under paths, oldest first."""
    args = ["log", "--diff-filter=A", "--format=@@%aI", "--name-only"]
    if since:
        args.append(f"--since={since}")
    if until:
        args.append(f"--until={until}")
    out, date = [], None
    for line in git(repo, *args, "--", *paths).splitlines():
        if line.startswith("@@"):
            date = line[2:12]
        elif line.strip():
            out.append((date, line.strip()))
    return sorted(out)


def first_added(repo, path):
    rows = added(repo, path)
    return rows[0][0] if rows else None


def weeks(a, b):
    return ((dt.date.fromisoformat(b) - dt.date.fromisoformat(a)).days + 1) / 7


# Recent pieces in the Service Desk, by the file names its review records use (Q-008 section 1.1,
# SD split rule): a plan is a series folder's first plan-review round-1 file; a built piece is a
# stage's or build unit's first round-1 review file, or a round-1 file in LA1, LA2 or
# md-sandbox. Research is counted from the dispatch log: an item whose first dispatch to its
# source check falls in the window.
R1 = r"(?:r1|round1)-"
PLAN = re.compile(rf"^reviews/([^/]+)/_plan-review-{R1}")
BUILT = re.compile(rf"^reviews/([^/]+)/_(?:stage|build)-([a-z0-9-]+?)-review-(?:round1|r1)-"
                   rf"|^reviews/([^/]+)/_build-review-{R1}"
                   rf"|^reviews/(LA1|LA2|md-sandbox)/_(?:review|design)-{R1}")


def sd_recent(sd, since, until):
    plans, built = {}, {}
    for date, path in added(sd, "reviews", since=None, until=until + "T23:59:59"):
        m = PLAN.match(path)
        if m and m.group(1) not in plans:
            plans[m.group(1)] = date
        m = BUILT.match(path)
        if m:
            key = (m.group(1), m.group(2)) if m.group(1) else (m.group(3) or m.group(4), "")
            if key not in built:
                built[key] = date
    inwin = lambda d: since <= d <= until
    plans = {k: d for k, d in plans.items() if inwin(d)}
    built = {k: d for k, d in built.items() if inwin(d)}
    research = {}
    for f in sorted((sd / "dispatch-log").glob("*.jsonl")):
        for line in f.read_text().splitlines():
            if not line.strip():
                continue
            e = json.loads(line)
            if e.get("action") == "dispatch" and e.get("role") == "source-checker":
                research.setdefault(e["item"], e["time"][:10])
    research = {k: d for k, d in research.items() if inwin(d)}
    return plans, built, research


def recorded(sd, folder, role):
    """True if a control file in reviews/<folder>/_control records brief, model and start commit for role."""
    for f in sorted((sd / "reviews" / folder / "_control").glob("*.json")):
        d = json.loads(f.read_text())
        if d.get("role") == role and d.get("brief") and d.get("model") and d.get("source_tip"):
            return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sd", default="/home/user/Service-Desk")
    ap.add_argument("--poom", default="/home/user/Personal-Org-Operating-Model")
    ap.add_argument("--ml", default="/home/user/Model-Lab")
    ap.add_argument("--to", default="2026-11-03")
    a = ap.parse_args()
    sd, poom, ml = Path(a.sd), Path(a.poom), Path(a.ml)

    print("1. Q-008's window")
    first = first_added(poom, "reviews/1/reviewer.md")
    last = first_added(ml, "research/Q-002-to-Q-007-corrections-confirmation.md")
    memo = git(ml, "log", "--diff-filter=A", "--format=%aI", "--", "research/Q-008-memo.md").split()[-1]
    print(f"   first piece's check record: POOM reviews/1/reviewer.md, added {first}")
    print(f"   last piece's check record:  ML research/Q-002-to-Q-007-corrections-confirmation.md, added {last}")
    print(f"   Q-008's memo first committed {memo}")
    for name, repo in (("SD", sd), ("POOM", poom), ("ML", ml)):
        rows = added(repo, "reviews", "research/*source-check*", "dispatch-log", until=memo)
        print(f"   cross-check {name}: check records added {rows[0][0]} to {rows[-1][0]} ({len(rows)} files)")
    w = weeks(first, last)
    print(f"   window: {first} to {last}, {w:.2f} weeks (both days counted)")

    print("\n2. Rates over the window, pieces a week")
    for kind, n in Q008.items():
        print(f"   {kind} all projects {n} / {w:.2f} = {n / w:.1f}")
    sd_rows = added(sd, "reviews", "research/*source-check*", "dispatch-log", until=memo)
    wsd = weeks(sd_rows[0][0], last)
    for kind, n in Q008_SD.items():
        print(f"   {kind} Service Desk {n} / {wsd:.2f} = {n / wsd:.1f}   (SD from {sd_rows[0][0]})")

    since = (dt.date.fromisoformat(a.to) - dt.timedelta(days=13)).isoformat()
    print(f"\n3. Recent pace, {since} to {a.to} (2 weeks)")
    plans, built, research = sd_recent(sd, since, a.to)
    print(f"   SD plans {len(plans)}: " + ", ".join(f"{k} {d}" for k, d in sorted(plans.items(), key=lambda x: x[1])))
    print(f"   SD built {len(built)}: " + ", ".join(f"{f}{'/' + s if s else ''} {d}" for (f, s), d in sorted(built.items(), key=lambda x: x[1])))
    print(f"   SD research (first source check) {len(research)}: " + ", ".join(f"{k} {d}" for k, d in sorted(research.items(), key=lambda x: x[1])))
    mlmemos = added(ml, "research/Q-*-memo.md", since=since, until=a.to + "T23:59:59")
    print(f"   ML research memos {len(mlmemos)} (this project's own Discovery, ending; not counted forward): "
          + ", ".join(Path(p).stem for _, p in mlmemos))
    poomc = git(poom, "log", f"--since={since}", f"--until={a.to}T23:59:59", "--format=%h").split()
    print(f"   POOM commits {len(poomc)}; last commit {git(poom, 'log', '-1', '--format=%as').strip()}")
    for kind, n in (("plans", len(plans)), ("built work", len(built)), ("research", len(research))):
        print(f"   {kind} SD recent {n} / 2 = {n / 2:.1f} a week")

    print("\n4. On record at dispatch (brief, model and start commit in a control file)")
    rc = sorted(k for k in research if recorded(sd, k, "source-checker"))
    rp = sorted(k for k in rc if recorded(sd, k, "researcher"))
    print(f"   SD research: {len(rc)} of {len(research)} recent items record the source check's ({', '.join(rc)}); "
          f"{len(rp)} also the researcher's")
    pc = [k for k in plans if (sd / "reviews" / k / "_control").is_dir()]
    bc = {f for (f, _) in built if (sd / "reviews" / f / "_control").is_dir()}
    print(f"   SD plans: {len(pc)} of {len(plans)} folders have any control file; SD built: {len(bc)} of "
          f"{len({f for f, _ in built})} folders")
    briefs = sorted(p for p in (ml / "docs" / "briefs").glob("*.md") if p.name != "README.md")
    has = lambda p, field: any(l.lower().startswith(field) for l in p.read_text().splitlines())
    nm = sum(has(p, "model:") for p in briefs)
    nc = sum(has(p, "start commit:") or has(p, "start:") for p in briefs)
    print(f"   ML docs/briefs: {len(briefs)} briefs; {nm} have a 'model:' line; {nc} a 'start commit:' line")


if __name__ == "__main__":
    main()
