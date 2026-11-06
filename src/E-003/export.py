"""The neutral export and the export reader (spec S-001, J3; E-003 Step 3).

  python3 -I src/E-003/export.py make --kind plans|built|research --repo DIR --label L --out DIR
          --checker-role ID --role-file PATH [--task-statement-path P] [--task-statement-text T]
          [--memo-path P] (--start SHA --final SHA | --memo-commit SHA) [--no-deliverable]
        (--task-statement-path is required for built work and research, --task-statement-text for plans)
  python3 -I src/E-003/export.py finish --out DIR --kind K
  python3 -I src/E-003/export.py verify --out DIR --kind K
  python3 -I src/E-003/export.py list BUNDLE

make    For plans and built work: a git bundle of exactly two commits, the first holding the tree of the
        piece's start commit (message `start`) and the second, its child, the arm's final tree (message
        `<label>`); for research: one commit, the tree at the memo's submission commit (message
        `<label>`).  Every commit has one neutral author and committer and one fixed date, the same in
        every export, so no arm commit, message, author or date reaches the judge.  The bundle holds the
        branch `<label>` (and HEAD); a two-commit bundle also holds the tag `start`, so the judge's
        range is `start..<label>` in a fresh clone.  Beside it, `<label>.fill.json` (the judge brief's
        fill values: checker role id, role file path, the judged range or memo path, the task
        statement's path, and for plans the task statement's text), and one line appended to the
        folder's INDEX: label, kind, bundle path, the bundle's SHA-256, the fill file's SHA-256,
        tab-separated.  The bundle path is from the repository root when --out lies in a git work
        tree (as src/E-003/exports/<kind>/ in Model-Lab does), else from --out.
        With --no-deliverable nothing is written: the arm fails (E-003 Exclusions 4) and the command
        prints {"exported": false, "arm_result": "FAIL"}.
finish  Appends the final line `last`, once every pair of the kind has its exports.
verify  Checks each INDEX line's bundle and fill file against their SHA-256s; exit 1 on the first that
        differs (that export gets no judgement and is written again by the work session).
list    The export reader: the files of the bundle's final tree, one path per line.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import e003lib as L  # noqa: E402

NEUTRAL = {"GIT_AUTHOR_NAME": "E-003 export", "GIT_AUTHOR_EMAIL": "export@e003.invalid",
           "GIT_COMMITTER_NAME": "E-003 export", "GIT_COMMITTER_EMAIL": "export@e003.invalid",
           # one fixed date for every export: 2000-01-01T00:00:00Z
           "GIT_AUTHOR_DATE": "946684800 +0000", "GIT_COMMITTER_DATE": "946684800 +0000",
           "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}
REVIEW = {"plans": "plan review", "built": "build review", "research": "source check"}
RESERVED = ("start", "last", "HEAD")


def run(args, cwd=None, env=None):
    e = dict(os.environ)
    e.update(NEUTRAL)
    if env:
        e.update(env)
    p = subprocess.run(args, cwd=cwd, env=e, capture_output=True)
    if p.returncode != 0:
        raise L.GitError("%s: %s" % (" ".join(args[:4]), p.stderr.decode("utf-8", "replace").strip()))
    return p.stdout.decode("utf-8", "replace").strip()


def toplevel(path):
    p = subprocess.run(["git", "-C", path, "rev-parse", "--show-toplevel"], capture_output=True)
    if p.returncode != 0:
        return None
    return p.stdout.decode("utf-8", "replace").strip()


def index_path_for(out, bundle):
    top = toplevel(out)
    if top:
        return os.path.relpath(os.path.realpath(bundle), os.path.realpath(top))
    return os.path.relpath(bundle, out)


def resolve(out, rel):
    for base in (out, toplevel(out)):
        if base:
            p = os.path.join(base, rel)
            if os.path.isfile(p):
                return p
    return None


def tree_of(repo, commit):
    try:
        return run(["git", "-C", repo, "rev-parse", "--verify", "%s^{tree}" % commit])
    except L.GitError:
        L.refuse("refused: commit %s is not in %s" % (commit, repo))


def cmd_make(a):
    if a.no_deliverable:
        L.emit({"exported": False, "arm_result": "FAIL", "label": a.label})
    if not L.full(L.LABEL, a.label) or a.label in RESERVED:
        L.refuse("refused: label %r is not a neutral label (letters, digits, . _ -; not start or last)" % a.label)
    if a.kind == "research":
        if not a.memo_commit or a.start or a.final:
            L.refuse("refused: research takes --memo-commit only")
        if not a.memo_path:
            L.refuse("refused: research needs --memo-path")
    elif not (a.start and a.final) or a.memo_commit:
        L.refuse("refused: plans and built work take --start and --final")
    if a.kind in ("built", "research") and not a.task_statement_path:
        L.refuse("refused: %s needs --task-statement-path (J3: the fill values carry the task statement's path)"
                 % a.kind)
    if a.kind == "plans" and not a.task_statement_text:
        L.refuse("refused: plans need --task-statement-text (the task statement of the worker's recorded brief)")
    os.makedirs(a.out, exist_ok=True)
    index = os.path.join(a.out, "INDEX")
    bundle = os.path.join(a.out, a.label + ".bundle")
    fill = os.path.join(a.out, a.label + ".fill.json")
    if os.path.isfile(index):
        rows, last = L.read_index(index)
        if last:
            L.refuse("refused: the INDEX already ends with `last`")
        if any(r["label"] == a.label for r in rows):
            L.refuse("refused: label %s is already in the INDEX" % a.label)
    if os.path.exists(bundle) or os.path.exists(fill):
        L.refuse("refused: an export for label %s already exists" % a.label)
    objects = run(["git", "-C", a.repo, "rev-parse", "--path-format=absolute", "--git-path", "objects"])
    work = tempfile.mkdtemp(prefix="e003-export-")
    try:
        bare = os.path.join(work, "x.git")
        run(["git", "init", "-q", "--bare", bare])
        with open(os.path.join(bare, "objects", "info", "alternates"), "w", encoding="utf-8") as fh:
            fh.write(objects + "\n")
        refs = ["HEAD", "refs/heads/" + a.label]
        if a.kind == "research":
            tip = run(["git", "-C", bare, "commit-tree", "--no-gpg-sign", tree_of(a.repo, a.memo_commit), "-m", a.label])
            judged = a.memo_path
        else:
            first = run(["git", "-C", bare, "commit-tree", "--no-gpg-sign", tree_of(a.repo, a.start), "-m", "start"])
            tip = run(["git", "-C", bare, "commit-tree", "--no-gpg-sign", tree_of(a.repo, a.final), "-p", first,
                       "-m", a.label])
            run(["git", "-C", bare, "update-ref", "refs/tags/start", first])
            refs.append("refs/tags/start")
            judged = "start..%s" % a.label
        run(["git", "-C", bare, "update-ref", "refs/heads/" + a.label, tip])
        run(["git", "-C", bare, "symbolic-ref", "HEAD", "refs/heads/" + a.label])
        tmp_bundle = os.path.join(work, "b.bundle")
        run(["git", "-C", bare, "bundle", "create", "-q", tmp_bundle] + refs)
        values = {"label": a.label, "kind": a.kind, "checker_role": a.checker_role, "role_file": a.role_file,
                  "review": REVIEW[a.kind], "judged": judged}
        if a.task_statement_path:
            values["task_statement_path"] = a.task_statement_path
        if a.task_statement_text:
            values["task_statement_text"] = a.task_statement_text
        fill_bytes = (json.dumps(values, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")
        shutil.move(tmp_bundle, bundle)
    finally:
        shutil.rmtree(work, True)
    with open(fill, "wb") as fh:
        fh.write(fill_bytes)
    line = "\t".join([a.label, a.kind, index_path_for(a.out, bundle), L.sha256_file(bundle),
                      L.sha256_bytes(fill_bytes)])
    with open(index, "a", encoding="utf-8", newline="") as fh:
        fh.write(line + "\n")
    L.emit({"exported": True, "label": a.label, "bundle": bundle, "fill": fill, "index_line": line})


def cmd_finish(a):
    index = os.path.join(a.out, "INDEX")
    if not os.path.isfile(index):
        L.refuse("refused: no INDEX in %s" % a.out)
    rows, last = L.read_index(index)
    if last:
        L.refuse("refused: the INDEX already ends with `last`")
    bad = [r["label"] for r in rows if r["kind"] != a.kind]
    if bad:
        L.refuse("refused: INDEX lines of another kind: %s" % ",".join(bad))
    text = L.read_text(index)
    with open(index, "a", encoding="utf-8", newline="") as fh:
        if text and not text.endswith("\n"):
            fh.write("\n")
        fh.write("last\n")
    L.emit({"finished": True, "exports": len(rows)})


def cmd_verify(a):
    index = os.path.join(a.out, "INDEX")
    if not os.path.isfile(index):
        L.refuse("refused: no INDEX in %s" % a.out)
    try:
        rows, last = L.read_index(index)
    except ValueError as exc:
        L.refuse("refused: %s" % exc)
    for r in rows:
        if r["kind"] != a.kind:
            L.refuse("refused: %s: kind %s is not %s" % (r["label"], r["kind"], a.kind))
        b = resolve(a.out, r["bundle"])
        if b is None:
            L.refuse("refused: %s: bundle %s is missing" % (r["label"], r["bundle"]))
        if L.sha256_file(b) != r["bundle_sha256"]:
            L.refuse("refused: %s: the bundle's SHA-256 differs from its index line" % r["label"])
        f = os.path.join(os.path.dirname(b), r["label"] + ".fill.json")
        if not os.path.isfile(f) or L.sha256_file(f) != r["fill_sha256"]:
            L.refuse("refused: %s: the fill file is missing or its SHA-256 differs from its index line" % r["label"])
    L.emit({"verified": len(rows), "last": last})


def cmd_list(a):
    work = tempfile.mkdtemp(prefix="e003-list-")
    try:
        dest = os.path.join(work, "x.git")
        try:
            run(["git", "clone", "-q", "--bare", os.path.abspath(a.bundle), dest])
            names = subprocess.run(["git", "-C", dest, "ls-tree", "-r", "-z", "--name-only", "HEAD"],
                                   capture_output=True, check=True).stdout
        except (L.GitError, subprocess.CalledProcessError):
            L.refuse("refused: %s is not a readable export bundle" % a.bundle)
    finally:
        shutil.rmtree(work, True)
    paths = [p for p in names.decode("utf-8", "replace").split("\0") if p]
    sys.stdout.write("".join(p + "\n" for p in paths))


def main(argv=None):
    ap = argparse.ArgumentParser(prog="export.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("make")
    m.add_argument("--kind", required=True, choices=L.KINDS)
    m.add_argument("--repo", required=True)
    m.add_argument("--label", required=True)
    m.add_argument("--out", required=True)
    m.add_argument("--checker-role", required=True)
    m.add_argument("--role-file", required=True)
    m.add_argument("--task-statement-path")
    m.add_argument("--task-statement-text")
    m.add_argument("--memo-path")
    m.add_argument("--start")
    m.add_argument("--final")
    m.add_argument("--memo-commit")
    m.add_argument("--no-deliverable", action="store_true")
    for name in ("finish", "verify"):
        s = sub.add_parser(name)
        s.add_argument("--out", required=True)
        s.add_argument("--kind", required=True, choices=L.KINDS)
    li = sub.add_parser("list")
    li.add_argument("bundle")
    a = ap.parse_args(argv)
    try:
        {"make": cmd_make, "finish": cmd_finish, "verify": cmd_verify, "list": cmd_list}[a.cmd](a)
    except L.GitError as exc:
        L.refuse("refused: %s" % exc)


if __name__ == "__main__":
    main()
