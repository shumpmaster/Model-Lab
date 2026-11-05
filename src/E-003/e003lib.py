"""Shared pieces of the E-003 harness (spec S-001, frozen at f4298cd).  Python standard library only.

Every script in this folder is run as `python3 -I src/E-003/<name>.py ...` from the repository root.
With -I the script's folder is not on sys.path, so each script adds its own folder explicitly before it
imports this module.

Conventions (tests/acceptance/e003_support.py, "THE INTERFACES THE TESTS CALL"):
  - a decision command prints exactly one JSON object on stdout and exits 0, a negative decision
    included;
  - a command that refuses exits 1 and prints a first line naming what it refused;
  - a usage error exits 2 (argparse's own exit code).
"""
import datetime
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

KINDS = ("plans", "built", "research")
CHANGE_OF_KIND = {"plans": "C1", "built": "C2", "research": "C3"}
KIND_OF_CHANGE = {v: k for k, v in CHANGE_OF_KIND.items()}
# The repositories whose pieces may enter (S-001 ruling 9: public repositories only).
PUBLIC_REPOS = ("Service-Desk", "Model-Lab")

SHA40 = re.compile(r"[0-9a-f]{40}")
SHA64 = re.compile(r"[0-9a-f]{64}")
INT = re.compile(r"0|[1-9][0-9]*")
POS_INT = re.compile(r"[1-9][0-9]*")
SET_ID = re.compile(r"S-001-(built|plans|research)-[1-9][0-9]*")
MODEL = re.compile(r"[A-Za-z0-9._-]{1,64}")
LABEL = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}")
K_RESULT = ("pass", "fail", "untested")
CANARY = ("unseen", "seen", "unread")
# A cited path (S-001 J5): 1 to 200 characters from letters, digits, . _ - / +, no `..` segment, no
# leading `/`.
PATH_CHARS = re.compile(r"[A-Za-z0-9._/+-]{1,200}")


def full(rx, s):
    return isinstance(s, str) and rx.fullmatch(s) is not None


def cited_path_ok(path):
    if not full(PATH_CHARS, path) or path.startswith("/"):
        return False
    segs = path.split("/")
    return all(seg not in ("", ".", "..") for seg in segs)


# ---------------------------------------------------------------------------------------------
# Output.

def emit(obj):
    """A decision: one JSON object on stdout, exit 0."""
    sys.stdout.write(json.dumps(obj, sort_keys=False) + "\n")
    sys.stdout.flush()
    sys.exit(0)


def refuse(message):
    """A refusal: the first line names what was refused, exit 1."""
    sys.stdout.write(message.splitlines()[0] if message else "refused")
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.exit(1)


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_text(path):
    """Read a text file exactly (no newline translation)."""
    with open(path, encoding="utf-8", newline="") as fh:
        return fh.read()


def read_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


# ---------------------------------------------------------------------------------------------
# Time.

def parse_time(s):
    """ISO 8601 instant (a trailing Z allowed); a bare date is its start, UTC."""
    if s is None:
        return None
    s = s.strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
        return datetime.datetime.fromisoformat(s + "T00:00:00+00:00")
    t = datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))
    if t.tzinfo is None:
        t = t.replace(tzinfo=datetime.timezone.utc)
    return t


def iso(t):
    return t.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------------------------
# Git.

def git(repo, *args, check=True, env=None, input_bytes=None):
    e = dict(os.environ)
    if env:
        e.update(env)
    p = subprocess.run(["git", "-C", repo] + list(args), capture_output=True, env=e, input=input_bytes)
    if check and p.returncode != 0:
        raise GitError("git %s failed: %s" % (" ".join(args[:3]), p.stderr.decode("utf-8", "replace").strip()))
    return p.stdout.decode("utf-8", "replace").strip()


def git_ok(repo, *args):
    p = subprocess.run(["git", "-C", repo] + list(args), capture_output=True)
    return p.returncode == 0


class GitError(RuntimeError):
    pass


def files_at(repo, commit):
    """Every file path in the tree of `commit`."""
    out = subprocess.run(["git", "-C", repo, "ls-tree", "-r", "-z", "--name-only", commit], capture_output=True)
    if out.returncode != 0:
        raise GitError("cannot list the tree of %s" % commit)
    return [p for p in out.stdout.decode("utf-8", "replace").split("\0") if p]


def show_at(repo, commit, path):
    p = subprocess.run(["git", "-C", repo, "show", "%s:%s" % (commit, path)], capture_output=True)
    if p.returncode != 0:
        return None
    return p.stdout.decode("utf-8", "replace")


# ---------------------------------------------------------------------------------------------
# Loading the registered sizing (experiments/E-003/sizing.py), used for power.

def sizing():
    path = os.path.join(ROOT, "experiments", "E-003", "sizing.py")
    spec = importlib.util.spec_from_file_location("e003_sizing", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


SIZING_KEY = {"plans": "plans", "built": "built work", "research": "research"}


# ---------------------------------------------------------------------------------------------
# Fixed-form lines shared by the J4 and J5 parsers.

def split_lines(text):
    """Lines of a block: LF only, one final newline allowed, no empty line anywhere."""
    if text == "":
        return None, "empty block"
    if "\r" in text:
        return None, "line 1: carriage return in the block"
    body = text[:-1] if text.endswith("\n") else text
    lines = body.split("\n")
    for i, line in enumerate(lines, 1):
        if line == "":
            return None, "line %d: blank line" % i
    return lines, None


def key_value(line, key):
    """`<key>: <value>` with exactly one space after the colon and no trailing space; value or None."""
    prefix = key + ": "
    if not line.startswith(prefix):
        return None
    value = line[len(prefix):]
    if value == "" or value != value.strip() or "  " in value:
        return None
    return value


# J4: the sheet lead's block, three forms.  Each field: (key, check(value, ctx) -> bool).
def _set(v, ctx):
    if full(SET_ID, v):
        ctx["set"] = v
        return True
    return False


def _in(*words):
    return lambda v, ctx: v in words


def _int(v, ctx):
    return full(INT, v)


def _pos(v, ctx):
    return full(POS_INT, v)


J4_FORMS = {
    "full": [("set", _set), ("repository-commit", lambda v, c: full(SHA40, v)),
             ("path", lambda v, c: v == "holdouts/%s.md" % c.get("set")),
             ("fingerprint", lambda v, c: full(SHA64, v)), ("tests", _pos), ("pack", _in("match")),
             ("scan", _in("clean", "unread")), ("model", lambda v, c: full(MODEL, v)), ("runs", _in("1")),
             ("tokens", _int), ("k1-canary", _in("unseen"))],
    "stopped": [("set", _set), ("pack", _in("match", "differs")), ("stopped", _in("k1", "k2", "k3", "k4", "pack")),
                ("runs", _in("0", "1")), ("tokens", _int), ("k1-canary", _in(*CANARY))],
    "void": [("set", _set), ("scan", _in("void")), ("hit", _pos), ("runs", _in("1")), ("tokens", _int),
             ("k1-canary", _in(*CANARY))],
}
for _form in J4_FORMS.values():
    _form += [("k2", _in(*K_RESULT)), ("k3", _in(*K_RESULT)), ("k4", _in(*K_RESULT)), ("k5", _in(*K_RESULT))]
J4_SECOND = {"repository-commit": "full", "pack": "stopped", "scan": "void"}


def parse_sheet_block(text):
    """Parse the sheet lead's block (S-001 J4).  Returns (result dict, None) or (None, refusal)."""
    lines, err = split_lines(text)
    if err:
        return None, err
    if len(lines) < 2:
        return None, "line %d: the block is not one of the three forms (too short)" % (len(lines) + 1)
    second = lines[1].split(":", 1)[0]
    form = J4_SECOND.get(second)
    if form is None:
        return None, "line 2: its key does not start any of the three forms"
    fields = J4_FORMS[form]
    if len(lines) != len(fields):
        return None, "line %d: the %s form has %d lines, the block %d" % (
            min(len(lines), len(fields)) + 1, form, len(fields), len(lines))
    ctx, values = {}, {}
    for i, (line, (key, ok)) in enumerate(zip(lines, fields), 1):
        v = key_value(line, key)
        if v is None:
            return None, "line %d: expected `%s: <value>` in the %s form" % (i, key, form)
        if not ok(v, ctx):
            return None, "line %d: `%s` value not in its form" % (i, key)
        values[key] = v
    return {"form": form, "fields": values}, None


# J5: the judging lead's counts block.
COUNTS_KEYS = ["counts", "index-commit", "judged", "runs", "reserve-used", "tokens", "left-out", "k1-canary",
               "k2", "k3", "k4", "k5", "k7"]


def parse_counts_lines(lines, set_id=None, labels=None, first_line=1):
    """Check the 13 lines of a counts block.  `labels`, if given, is the INDEX's labels."""
    if len(lines) != len(COUNTS_KEYS):
        return None, "line %d: a counts block has %d lines, this one %d" % (
            first_line + min(len(lines), len(COUNTS_KEYS)), len(COUNTS_KEYS), len(lines))
    values = {}
    for i, (line, key) in enumerate(zip(lines, COUNTS_KEYS), first_line):
        v = key_value(line, key)
        if v is None:
            return None, "line %d: expected `%s: <value>`" % (i, key)
        if key == "counts":
            ok = full(SET_ID, v) and (set_id is None or v == set_id)
        elif key == "index-commit":
            ok = full(SHA40, v)
        elif key in ("judged", "runs", "reserve-used", "tokens"):
            ok = full(INT, v)
        elif key == "left-out":
            if v == "-":
                ok = True
            else:
                parts = v.split(",")
                ok = all(full(LABEL, x) for x in parts) and len(set(parts)) == len(parts)
                if ok and labels is not None:
                    ok = all(x in labels for x in parts)
        elif key == "k1-canary":
            ok = v in CANARY
        else:
            ok = v in K_RESULT
        if not ok:
            return None, "line %d: `%s` value not in its form" % (i, key)
        values[key] = v
    return values, None


def read_index(path):
    """The kind's INDEX (S-001 J3): label, kind, bundle path, bundle SHA-256, fill SHA-256; final `last`."""
    rows, last = [], False
    text = read_text(path)
    for n, line in enumerate(text.split("\n"), 1):
        if line == "":
            continue
        if last:
            raise ValueError("INDEX line %d: a line after `last`" % n)
        if line == "last":
            last = True
            continue
        f = line.split("\t")
        if len(f) != 5 or not full(LABEL, f[0]) or f[1] not in KINDS or not full(SHA64, f[3]) or not full(SHA64, f[4]):
            raise ValueError("INDEX line %d: not `label, kind, bundle path, bundle SHA-256, fill SHA-256`" % n)
        rows.append({"label": f[0], "kind": f[1], "bundle": f[2], "bundle_sha256": f[3], "fill_sha256": f[4]})
    return rows, last
