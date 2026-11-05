"""The pair: entry, copies and briefs, the in-flight audit, the context comparison, reruns and the locked
checks (spec S-001, AC2, AC3, AC5 and J2; E-003 Steps 2 and 3, Exclusions 1 to 3 and 6, Sample "Reruns").

  python3 -I src/E-003/pair.py entry --source FILE --now ISO [--role ROLE] [--kind K] [--repo NAME]
          [--memo-commit SHA] [--dispatched-at ISO] [--round-1-verdict-at ISO]
  python3 -I src/E-003/pair.py plan --entry FILE --repos-root DIR --change Cn --now ISO --no-run
  python3 -I src/E-003/pair.py audit --repo DIR --start SHA --submission SHA --named-input PATH ...
          [--default-branch B]
  python3 -I src/E-003/pair.py context-compare --a FILE --b FILE --change-text FILE --path-a P --path-b P
  python3 -I src/E-003/pair.py rerun-decision --history FILE
  python3 -I src/E-003/pair.py locked-checks --copy DIR --command "<shell command>"

entry   One entry per piece from its record at dispatch (J2): a Model-Lab brief record (docs/briefs/:
        `model:`, `start: <repository>@<full commit id>`, `recorded: at hand-out, <date>`, then a
        `## Brief` section, which is the brief) or a Service Desk control file (JSON with `brief`,
        `model`, `source_tip`, `role`, `dispatched_at`; one object or a list, the entry being the one
        whose `role` is --role).  Not eligible, with the reason: no brief, model or full start commit; a
        record written after the dispatch or after the round-1 verdict; for research, no memo
        submission commit or no source check on record; a repository that is not public (Service-Desk
        and Model-Lab only, ruling 9); first found more than 7 days after its dispatch.  The dispatch
        time is --dispatched-at, else the record's own `dispatched_at`, else its `recorded:` date.
plan    Makes the two fresh copies of the entry's start commit under --repos-root (E-001 step 2.1: a new
        repository fetching only that commit, checked to hold it and its ancestors only) and returns
        both arms: the recorded brief with the real repository's absolute path replaced by the copy's
        (nothing else changed) for the control arm, and the same with the change paragraph inserted
        after the task statement for the change arm; the same model; the same start time (--now).
        Each arm also carries `prompt`: its brief followed by E-001's confinement paragraph with its
        copy's path, the text a run is started with.  With --no-run no session is started.  A pair is
        refused (no arms) if --now is more than 7 days after the dispatch, or the change cannot be
        filled (C1 without the plan-check role file, C2 with an empty list).
audit   E-003 Exclusions 1, from git: the pair is left out when a named input changed on the default
        branch between the start commit and the real round-1 submission (the default branch as it was at
        the submission's committer date), or when the submission takes in a commit of the default
        branch that is not an ancestor of the start commit.  A named folder counts its files.
context-compare  E-003 Exclusions 3: the two arms' starting context (every transcript line before the
        first assistant line) must match once each copy path is read as one placeholder and the change
        paragraph is taken out; ids and times that differ in every session (uuid, parentUuid,
        timestamp, sessionId, promptId, agentId, requestId) are not compared.
rerun-decision  Sample, Reruns (b): one rerun of both arms for a first set-up fault (a context that
        differs is one) found before judging; a second leaves the pair out; in-flight inputs and leaks
        always leave it out; nothing is rerun once the pair is judged ("completed").  Actions: rerun,
        leave-out, judge (no fault yet), keep (judged, stands).
locked-checks  Runs the stage's locked checks in the arm's copy by script and returns their exit status.
"""
import argparse
import datetime
import json
import os
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import e003lib as L  # noqa: E402
import change as C  # noqa: E402

SEVEN_DAYS = datetime.timedelta(days=7)
CONFINEMENT = ("Work only in {copy}. Do not read, search or run commands on any path outside it, do not\n"
               "use the web, and do not run git commands that reach any other repository.")
TASK_RX = re.compile(r"(?im)^(task statement|your task|task)\s*:")


def not_eligible(reason, entry=None):
    L.emit({"eligible": False, "reason": reason, "entry": entry or {}})


# ---------------------------------------------------------------------------------------------
# entry

def parse_brief_record(text):
    fields = {}
    head = text.split("\n## ", 1)[0]
    for line in head.split("\n"):
        m = re.match(r"^(session|model|start|recorded|dispatched_at):\s*(.*)$", line.strip())
        if m:
            fields.setdefault(m.group(1), m.group(2).strip())
    m = re.search(r"^## Brief[ \t]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    brief = m.group(1).strip("\n") + "\n" if m and m.group(1).strip() else None
    return fields, brief


def record_entry(a, text):
    fields, brief = parse_brief_record(text)
    model = (fields.get("model") or "").split()
    model = model[0] if model else ""
    starts = [s.strip() for s in re.split(r"[,;]|\s+", fields.get("start", "")) if s.strip()]
    start, start_repo = None, None
    pairs = [s.split("@", 1) for s in starts if "@" in s]
    chosen = [p for p in pairs if a.repo and p[0] == a.repo] or (pairs if len(pairs) == 1 else [])
    if chosen:
        start_repo, start = chosen[0]
    rec = fields.get("recorded", "")
    m = re.search(r"\d{4}-\d{2}-\d{2}", rec)
    return {"brief": brief, "model": model, "start": start, "start_repo": start_repo,
            "recorded_at_handout": rec.lower().startswith("at hand-out"), "recorded_date": m.group(0) if m else None,
            "dispatched_at": fields.get("dispatched_at")}


def control_entry(a, data):
    items = data if isinstance(data, list) else [data]
    items = [x for x in items if isinstance(x, dict)]
    if a.role:
        items = [x for x in items if x.get("role") == a.role]
    if len(items) != 1:
        return None
    x = items[0]
    rec = str(x.get("recorded", "at hand-out"))
    m = re.search(r"\d{4}-\d{2}-\d{2}", str(x.get("recorded_at") or x.get("dispatched_at") or ""))
    return {"brief": x.get("brief") or None, "model": str(x.get("model") or "").split()[0] if x.get("model") else "",
            "start": x.get("source_tip") or x.get("start"), "start_repo": None,
            "recorded_at_handout": rec.lower().startswith("at hand-out"), "recorded_date": m.group(0) if m else None,
            "dispatched_at": x.get("dispatched_at"), "memo_commit": x.get("memo_commit")}


def cmd_entry(a):
    text = L.read_text(a.source)
    kind = a.kind
    if kind not in L.KINDS:
        not_eligible("no kind of work given (plans, built or research)")
    is_json = text.lstrip()[:1] in ("{", "[")
    if is_json:
        try:
            e = control_entry(a, json.loads(text))
        except ValueError:
            e = None
        if e is None:
            not_eligible("no record of the dispatched role%s in the control file" % (
                " (%s)" % a.role if a.role else ""))
    else:
        e = record_entry(a, text)
    repo = a.repo or e.get("start_repo")
    if not e["brief"]:
        not_eligible("no brief on record at dispatch")
    if not L.full(L.MODEL, e["model"] or ""):
        not_eligible("no model on record at dispatch")
    if not L.full(L.SHA40, e["start"] or ""):
        not_eligible("no full start commit on record at dispatch (`start: <repository>@<40 lowercase hex>`)")
    if not e["recorded_at_handout"]:
        not_eligible("the record was written after the dispatch, not at hand-out")
    if repo not in L.PUBLIC_REPOS:
        not_eligible("the repository %r is not a participating public repository (ruling 9)" % repo)
    memo = a.memo_commit or e.get("memo_commit")
    if kind == "research" and not L.full(L.SHA40, memo or ""):
        not_eligible("no memo submission commit on record (research needs it beside the source check's record)")
    dispatched = a.dispatched_at or e.get("dispatched_at") or e.get("recorded_date")
    if not dispatched:
        not_eligible("no dispatch time on record")
    try:
        t_dispatch = L.parse_time(dispatched)
        now = L.parse_time(a.now)
    except ValueError:
        not_eligible("a time on record is not ISO 8601")
    if e.get("recorded_date"):
        if L.parse_time(e["recorded_date"]).date() > t_dispatch.date():
            not_eligible("the record is dated after the dispatch")
    if a.round_1_verdict_at:
        verdict = L.parse_time(a.round_1_verdict_at)
        if (e.get("recorded_date") and L.parse_time(e["recorded_date"]).date() > verdict.date()) or t_dispatch > verdict:
            not_eligible("the record was made after the round-1 verdict")
    if now - t_dispatch > SEVEN_DAYS:
        not_eligible("first found more than 7 days after its dispatch (late)")
    entry = {"brief": e["brief"], "start": e["start"], "repo": repo, "kind": kind, "model": e["model"],
             "dispatched_at": L.iso(t_dispatch)}
    if kind == "research":
        entry["memo_commit"] = memo
    L.emit({"eligible": True, "reason": "", "entry": entry})


# ---------------------------------------------------------------------------------------------
# plan

def make_copy(source, commit, parent_dir, name):
    """E-001 step 2.1: a new repository holding the start commit and its ancestors only, checked."""
    copy = tempfile.mkdtemp(prefix=name + "-", dir=parent_dir)
    L.git(copy, "init", "-q")
    L.git(copy, "fetch", "-q", "--no-tags", os.path.abspath(source), commit)
    L.git(copy, "checkout", "-q", "--detach", "FETCH_HEAD")
    if L.git(copy, "rev-parse", "HEAD") != commit:
        raise L.GitError("the copy is not at the start commit")
    if L.git(copy, "rev-list", "--count", "HEAD") != L.git(source, "rev-list", "--count", commit):
        raise L.GitError("the copy's history differs from the start commit's")
    later = L.git(source, "rev-list", "-n1", "--all", "--not", commit, check=False)
    if later and L.git_ok(copy, "cat-file", "-t", later):
        raise L.GitError("the copy holds a commit later than the start")
    return copy


def task_statement(brief):
    for p in brief.split("\n\n"):
        if TASK_RX.match(p.strip()):
            return p.strip()
    return ""


def cmd_plan(a):
    e = L.read_json(a.entry)
    for k in ("brief", "start", "repo", "kind", "model", "dispatched_at"):
        if not e.get(k):
            L.refuse("refused: the entry lacks %s" % k)
    if e["kind"] not in L.KINDS or L.CHANGE_OF_KIND[e["kind"]] != a.change:
        L.refuse("refused: %s is not the change for %s" % (a.change, e["kind"]))
    now = L.parse_time(a.now)
    if now - L.parse_time(e["dispatched_at"]) > SEVEN_DAYS:
        L.emit({"arms": [], "eligible": False, "reason": "more than 7 days after the dispatch: no arm may start"})
    source = e.get("real_path")
    if not source or not os.path.isdir(source):
        source = os.path.join(a.repos_root, e["repo"])
    if not os.path.isdir(source):
        L.refuse("refused: no clone of %s under --repos-root and no real_path" % e["repo"])
    parent = os.path.join(a.repos_root, "e003-copies")
    os.makedirs(parent, exist_ok=True)
    base = "%s-%s" % (re.sub(r"[^A-Za-z0-9._-]", "-", e["repo"]), e["start"][:12])
    try:
        copies = {arm: make_copy(source, e["start"], parent, "%s-%s" % (base, arm)) for arm in ("control", "change")}
    except L.GitError as exc:
        L.refuse("refused: set-up fault: %s" % exc)
    real = e.get("real_path")
    briefs = {}
    for arm, copy in copies.items():
        b = e["brief"].replace(real, copy) if real else e["brief"]
        briefs[arm] = b
    task = task_statement(briefs["change"])
    if a.change == "C1":
        if not L.git_ok(copies["change"], "cat-file", "-e", "HEAD:%s" % C.PLAN_CHECK_ROLE_FILE):
            L.emit({"arms": [], "eligible": False, "reason": "no plan-check role file at the start commit"})
        fill = C.PLAN_CHECK_ROLE_FILE
    elif a.change == "C2":
        items = C.fill_c2(copies["change"], e["start"], task or briefs["change"])
        if not items:
            L.emit({"arms": [], "eligible": False, "reason": "C2's list is empty"})
        fill = ", ".join(items)
    else:
        fill = ""
    changed, placement, recorded, reason = C.apply(briefs["change"], task, a.change, fill)
    briefs["change"] = changed
    arms = []
    for arm in ("control", "change"):
        conf = CONFINEMENT.format(copy=copies[arm])
        arms.append({"arm": arm, "copy": copies[arm], "commit": e["start"], "brief": briefs[arm],
                     "prompt": briefs[arm].rstrip("\n") + "\n\n" + conf + "\n", "model": e["model"],
                     "start_at": L.iso(now)})
    L.emit({"arms": arms, "eligible": True, "change": a.change, "fill": fill, "placement": placement,
            "recorded": recorded, "reason": reason, "started": False})


# ---------------------------------------------------------------------------------------------
# audit

def cmd_audit(a):
    repo, start, sub, branch = a.repo, a.start, a.submission, a.default_branch
    try:
        sub_t = L.git(repo, "log", "-1", "--format=%ct", sub)
        tip = L.git(repo, "rev-list", "-n1", "--first-parent", "--before=%s" % sub_t, branch)
    except L.GitError as exc:
        L.refuse("refused: %s" % exc)
    if tip:
        changed = L.git(repo, "log", "--format=%H", "%s..%s" % (start, tip), "--", *a.named_input)
        if changed:
            names = L.git(repo, "diff", "--name-only", start, tip, "--", *a.named_input).split("\n")
            L.emit({"include": False, "reason": "in-flight inputs: %s changed on %s before the round-1 submission"
                    % (", ".join(n for n in names if n) or ", ".join(a.named_input), branch)})
        own = set(L.git(repo, "rev-list", "%s..%s" % (start, sub)).split())
        main = set(L.git(repo, "rev-list", "%s..%s" % (start, tip)).split())
        foreign = sorted(own & main)
        if foreign:
            L.emit({"include": False, "reason": "the submission takes in %d commit(s) of %s that are not ancestors "
                    "of the start commit" % (len(foreign), branch)})
    L.emit({"include": True, "reason": ""})


# ---------------------------------------------------------------------------------------------
# context-compare

VOLATILE = ("uuid", "parentUuid", "timestamp", "sessionId", "promptId", "agentId", "requestId")


def starting_context(path):
    out = []
    for line in L.read_text(path).split("\n"):
        if not line.strip():
            continue
        rec = json.loads(line)
        if isinstance(rec, dict) and rec.get("type") == "assistant":
            break
        out.append(rec)
    return out


def scrub(obj, copy, change):
    if isinstance(obj, dict):
        return {k: scrub(v, copy, change) for k, v in obj.items() if k not in VOLATILE}
    if isinstance(obj, list):
        return [scrub(v, copy, change) for v in obj]
    if isinstance(obj, str):
        s = obj.replace(copy, "<COPY>") if copy else obj
        if change:
            for nl in ("\r\n", "\n"):
                para = change.replace("\n", nl)
                s = s.replace(nl + nl + para, "").replace(para + nl + nl, "")
            s = s.replace(change, "").replace(change.replace("\n", "\r\n"), "")
        return s
    return obj


def cmd_context(a):
    change = L.read_text(a.change_text).strip("\r\n")
    ca = scrub(starting_context(a.a), a.path_a, change)
    cb = scrub(starting_context(a.b), a.path_b, change)
    if len(ca) != len(cb):
        L.emit({"same": False, "reason": "the starting contexts have %d and %d lines" % (len(ca), len(cb))})
    for i, (x, y) in enumerate(zip(ca, cb), 1):
        if x != y:
            L.emit({"same": False, "reason": "starting-context line %d differs beyond the change paragraph and "
                    "the copy path: a set-up fault" % i})
    L.emit({"same": True, "reason": ""})


# ---------------------------------------------------------------------------------------------
# rerun-decision

def cmd_rerun(a):
    history = L.read_json(a.history)
    events = [h.get("event") for h in history if isinstance(h, dict)]
    known = ("set-up-fault", "context-differs", "in-flight-inputs", "leak", "arms-finished", "completed")
    for ev in events:
        if ev not in known:
            L.refuse("refused: unknown event %r" % ev)
    faults, judged = 0, False
    for ev in events:
        if ev == "completed":
            judged = True
        elif ev in ("in-flight-inputs", "leak"):
            L.emit({"action": "leave-out", "reason": "%s: the pair is left out and never rerun (E-003 Exclusions %s)"
                    % (ev, "1" if ev == "in-flight-inputs" else "2")})
        elif ev in ("set-up-fault", "context-differs"):
            if judged:
                L.emit({"action": "leave-out", "reason": "a set-up fault found after judging: nothing is rerun for "
                        "a better answer; the pair is left out and listed"})
            faults += 1
    if faults >= 2:
        L.emit({"action": "leave-out", "reason": "a second set-up fault: the one rerun is spent (Sample, Reruns (b))"})
    if faults == 1:
        L.emit({"action": "rerun", "reason": "a set-up fault found before judging: both arms are run again once"})
    if judged:
        L.emit({"action": "keep", "reason": "judged: the pair stands and is never rerun"})
    L.emit({"action": "judge", "reason": "no fault: judge the pair as it stands"})


# ---------------------------------------------------------------------------------------------
# locked-checks

def cmd_locked(a):
    t0 = datetime.datetime.now()
    p = subprocess.run(a.command, shell=True, cwd=a.copy, capture_output=True)
    secs = (datetime.datetime.now() - t0).total_seconds()
    L.emit({"exit": p.returncode, "command": a.command, "seconds": round(secs, 1)})


def main(argv=None):
    ap = argparse.ArgumentParser(prog="pair.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("entry")
    e.add_argument("--source", required=True)
    e.add_argument("--now", required=True)
    e.add_argument("--role")
    e.add_argument("--kind", choices=L.KINDS)
    e.add_argument("--repo")
    e.add_argument("--memo-commit")
    e.add_argument("--dispatched-at")
    e.add_argument("--round-1-verdict-at")
    p = sub.add_parser("plan")
    p.add_argument("--entry", required=True)
    p.add_argument("--repos-root", required=True)
    p.add_argument("--change", required=True, choices=("C1", "C2", "C3"))
    p.add_argument("--now", required=True)
    p.add_argument("--no-run", action="store_true", required=True,
                   help="make the copies and briefs only; this harness starts no session itself")
    au = sub.add_parser("audit")
    au.add_argument("--repo", required=True)
    au.add_argument("--start", required=True)
    au.add_argument("--submission", required=True)
    au.add_argument("--named-input", action="append", required=True)
    au.add_argument("--default-branch", default="main")
    c = sub.add_parser("context-compare")
    c.add_argument("--a", required=True)
    c.add_argument("--b", required=True)
    c.add_argument("--change-text", required=True)
    c.add_argument("--path-a", required=True)
    c.add_argument("--path-b", required=True)
    r = sub.add_parser("rerun-decision")
    r.add_argument("--history", required=True)
    lc = sub.add_parser("locked-checks")
    lc.add_argument("--copy", required=True)
    lc.add_argument("--command", required=True)
    a = ap.parse_args(argv)
    {"entry": cmd_entry, "plan": cmd_plan, "audit": cmd_audit, "context-compare": cmd_context,
     "rerun-decision": cmd_rerun, "locked-checks": cmd_locked}[a.cmd](a)


if __name__ == "__main__":
    main()
