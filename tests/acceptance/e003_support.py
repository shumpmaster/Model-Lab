"""Shared helpers for S-001's locked checks (Python standard library only).

Locked: written by the Check author from the frozen spec specs/S-001.md (frozen @ f4298cd) before
any harness code exists. Never edited once locked; a new spec supersedes it.

Run every test of this folder with
    python3 -m unittest discover -s tests/acceptance -p 'test_*.py'
or one file with
    python3 -m unittest discover -s tests/acceptance -p 'test_j7*.py'
Before a blind dispatch run J8 with S001_BLIND_MANIFEST=<brief record>, and before the analysis dispatch
J7 with S001_ANALYSIS_MANIFEST=<brief record>; each test checks only its own setting's record, whatever it
holds, and never skips it
(from the repository root).

THE INTERFACES THE TESTS CALL (the Builder's harness; none exists yet).  The spec fixes the pieces
("the fill script, the transcript check and the export reader", the block parser, the harness, the
exports under src/E-003/exports/<kind>/, the records under src/E-003/records/<kind>/) but not their
file names or command lines, so these are the names the tests use, invented only as far as a test needs
(each use is listed in the Check author's return as a gap).  Every script is
`python3 -I src/E-003/<name>.py <subcommand> <options>` run with the repository root as the working
directory.  A decision command prints exactly one JSON object on stdout and exits 0 (a negative
decision is still exit 0); a command that REFUSES (fill script, block parser, verdict checker,
transcript check on a leak, export verify) exits 1 and prints a first line naming what was refused; a
usage error exits 2.  A missing script fails its test with "interface missing".

  change.py   apply   --change C1|C2|C3 --brief FILE --task-statement FILE --fill TEXT
                          -> {"brief": <change-arm brief>, "placement": "after-task-statement"
                              | "after-first-paragraph", "recorded": bool}
              remove  --change Cn --brief FILE --fill TEXT   -> {"brief": <text without the paragraph>}
              verify-removal --change Cn --control FILE --changed FILE --fill TEXT -> {"clean": bool}
              fill-c1 --repo DIR --commit SHA                -> {"eligible": bool, "fill": <path>, "reason": str}
              fill-c2 --repo DIR --commit SHA --task-file F  -> {"eligible": bool, "fill": <list>, "reason": str}
  pair.py     entry   --source FILE --now ISO [--role ROLE] [--kind K] [--repo NAME] [--memo-commit SHA]
                          [--dispatched-at ISO] [--round-1-verdict-at ISO]
                          -> {"eligible": bool, "reason": str, "entry": {"brief","start","repo","kind","model",
                              "dispatched_at"[,"memo_commit"]}}   (the source: a docs/briefs record, or a
                              Service Desk control file as JSON, one object or a list of them)
              plan    --entry FILE --repos-root DIR --change Cn --now ISO --no-run
                          -> {"arms": [{"arm": "control"|"change","copy","commit","brief","model","start_at"}]}
                             (copies made, no session started; entry FILE is JSON with the entry keys above
                              plus "real_path", the absolute path the brief uses)
              audit   --repo DIR --start SHA --submission SHA --named-input PATH ... [--default-branch B]
                          -> {"include": bool, "reason": str}
              context-compare --a FILE --b FILE --change-text FILE --path-a P --path-b P
                          -> {"same": bool, "reason": str}
              rerun-decision --history FILE  -> {"action": "rerun"|"leave-out", "reason": str}
                          FILE is a JSON list of {"event": W}, W one of: "set-up-fault", "context-differs",
                          "in-flight-inputs", "leak", "arms-finished" (both arms ended, not yet judged),
                          "completed" (judged: nothing is rerun for a better answer)
              locked-checks --copy DIR --command "<shell command>"   -> {"exit": N}
  transcript_check.py check --cwd DIR [--web-sources FILE] [--allow-path P] [--sheets-repo NAME] TRANSCRIPT.jsonl
                          -> stdout `clean` exit 0, or `leak@<line>` exit 1.  Allowed outside the copy (E-001 F4):
                          /usr, /bin, /lib, /etc (read only) and files the run itself created in /tmp
                          (a /tmp path is clean on the line that creates it and on any later line, and only then; a Bash
                          `>` or `>>` redirect target, a `touch` or `mkdir` argument, or a Write/Edit file_path counts as created); web only for URLs listed in --web-sources
  fill_judge_brief.py --sheet FILE --fingerprint HEX --fill FILE.json --label L --copy-path DIR --out FILE
                          -> on a match writes the filled judge brief (E-002's template with E-003 Step 4's
                             changes) to --out; on a mismatch exit 1 and writes nothing
  export.py   make    --kind plans|built|research --repo DIR --label L --out DIR --checker-role ID
                      --role-file PATH [--task-statement-path P] [--task-statement-text T] [--memo-path P]
                      (--start SHA --final SHA | --memo-commit SHA) [--no-deliverable]
              finish  --out DIR --kind K        (appends the final line `last`)
              verify  --out DIR --kind K        (exit 1 on a bundle whose SHA-256 differs from its index line)
              list    BUNDLE                    (the export reader: one path per line)
              With --no-deliverable make exports nothing and prints {"exported": false, "arm_result": "FAIL"}.
  block.py    parse   < BLOCK                    -> {"form": "full"|"stopped"|"void", ...}; exit 1 on refusal
  verdicts.py check   --index FILE --filelists DIR --tests N --set SETID
                      (--verdicts FILE | --counts FILE | --closing FILE)    exit 1, first line names the line
  judge.py    next-step --state JSON ({"verdict","follow_up_sent","sessions"}) -> {"action"}
              parse-return --text-file F [--background-running] -> {"verdict","failed","multiple"}
              followup-text | arm-outcome --verdict V [--locked-exit N] | check-model --doer M --judge M
  cards.py    draw --pairs FILE --seed N --set SETID [--answers FILE] | rescore --pairs FILE --answers FILE
              | file --kind K --set SETID --cards FILE --answers FILE --out ROOT [--sheet FILE]
  analyse.py  run --pairs FILE --cards FILE --kind K | v2 --kind K --passes N
              (a mechanical reference for the Reviewer's analysis: the spec has the Reviewer analyse, and names
               no script; this is an added Builder deliverable that the tests need, in src/E-003/**)
  counts.py   card | due | cap | may-start | record-ruling   (arguments in test_ac08_counts_card.py)
  kind.py     can-open --kind K --holdouts FILE --sheet-record FILE
"""
import hashlib
import importlib.util
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "src", "E-003")
FROZEN = "f4298cdf19a5abf17e34d7979846252819c2b14b"

# A stand-in sheet: no real check (J4). Its marker words let a test find any copy of its text.
STAND_IN_SHEET = (
    "Stand-in sheet. This is not a real check.\n"
    "1. STANDIN-T1: the piece cites a file that is not in it.\n"
    "2. STANDIN-T2: the piece contradicts the task it was set.\n"
    "3. STANDIN-T3: the piece leaves a stated requirement unmet.\n"
)
STAND_IN_MARKERS = ("STANDIN-T1", "STANDIN-T2", "STANDIN-T3")


def sha256(data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def norm(path):
    """As governance/checks/session_runner.py `norm`: Unicode NFC, case folded."""
    return unicodedata.normalize("NFC", path).casefold()


def load_module(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    old = list(sys.path)
    sys.path.insert(0, os.path.join(ROOT, "governance", "checks"))
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.path[:] = old
    return mod


def session_runner():
    return load_module("session_runner_ref", "governance/checks/session_runner.py")


def govlib():
    return load_module("govlib_ref", "governance/checks/govlib.py")


def sizing():
    return load_module("sizing_ref", "experiments/E-003/sizing.py")


# ---------------------------------------------------------------------------------------------
# Reference statistics, worked independently of the Builder's code.

def binom_p_ge(k, d):
    """P(X >= k | d, 1/2)."""
    return sum(math.comb(d, j) for j in range(k, d + 1)) / 2 ** d


def kept_by_test(n10, n01):
    d = n10 + n01
    return d > 0 and binom_p_ge(n10, d) <= 1 / 40


def wilson(x, n, z=1.959963984540054):
    if n == 0:
        return 0.0, 1.0
    p = x / n
    den = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return centre - half, centre + half


def newcombe_paired(a, b, c, d, z=1.959963984540054):
    """Newcombe's method 10 for the difference of two paired proportions.
    a both pass, b first-only (n10), c second-only (n01), d neither. Returns (diff, lower, upper)."""
    n = a + b + c + d
    p1, p2 = (a + b) / n, (a + c) / n
    l1, u1 = wilson(a + b, n, z)
    l2, u2 = wilson(a + c, n, z)
    diff = p1 - p2
    big_a = (a + b) * (c + d) * (a + c) * (b + d)
    cc = a * d - b * c
    if cc > n / 2:
        cc -= n / 2
    elif cc >= 0:
        cc = 0.0
    else:
        cc += n / 2
    phi = 0.0 if big_a == 0 else cc / math.sqrt(big_a)
    lower = diff - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2 - 2 * phi * (p1 - l1) * (u2 - p2))
    upper = diff + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2 - 2 * phi * (u1 - p1) * (p2 - l2))
    return diff, lower, upper


# ---------------------------------------------------------------------------------------------
# Git fixtures.

def git(repo, *args, env=None, check=True):
    e = dict(os.environ)
    e.update({"GIT_AUTHOR_NAME": "Fixture Author", "GIT_AUTHOR_EMAIL": "fixture@example.invalid",
              "GIT_COMMITTER_NAME": "Fixture Committer", "GIT_COMMITTER_EMAIL": "fixture@example.invalid",
              "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_SYSTEM": os.devnull})
    if env:
        e.update(env)
    p = subprocess.run(["git", "-C", repo] + list(args), capture_output=True, text=True, env=e)
    if check and p.returncode != 0:
        raise RuntimeError("git %s failed: %s" % (" ".join(args), p.stderr))
    return p.stdout.strip()


def init_repo(path):
    os.makedirs(path, exist_ok=True)
    git(path, "init", "-q", "-b", "main")
    return path


def commit_files(repo, files, message, when="2026-11-05T10:00:00Z", delete=()):
    for rel, text in files.items():
        full = os.path.join(repo, rel)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8", newline="") as fh:
            fh.write(text)
    for rel in delete:
        os.remove(os.path.join(repo, rel))
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "--allow-empty", "-m", message,
        env={"GIT_AUTHOR_DATE": when, "GIT_COMMITTER_DATE": when})
    return git(repo, "rev-parse", "HEAD")


# ---------------------------------------------------------------------------------------------
# Test base: script runner with a clear failure for an interface that is not built yet.

class InterfaceMissing(AssertionError):
    pass


class Base(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="s001-")
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def script(self, name):
        path = os.path.join(SRC, name)
        if not os.path.isfile(path):
            self.fail("interface missing: src/E-003/%s is not built yet (see tests/acceptance/e003_support.py)"
                      % name)
        return path

    def run_script(self, name, *args, stdin=None, cwd=None):
        p = subprocess.run([sys.executable, "-I", self.script(name)] + [str(a) for a in args],
                           input=stdin, capture_output=True, text=True, cwd=cwd or ROOT, timeout=300)
        return p

    def decide(self, name, *args, stdin=None, cwd=None):
        """Run a decision command: exit 0 and one JSON object on stdout."""
        p = self.run_script(name, *args, stdin=stdin, cwd=cwd)
        self.assertEqual(p.returncode, 0, "%s %s exited %s: %s" % (name, args[:1], p.returncode, p.stderr[-400:]))
        try:
            out = json.loads(p.stdout)
        except ValueError:
            self.fail("%s %s printed no JSON object: %r" % (name, args[:1], p.stdout[:300]))
        self.assertIsInstance(out, dict)
        return out

    def write(self, rel, text, base=None):
        full = os.path.join(base or self.tmp, rel)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8", newline="") as fh:
            fh.write(text)
        return full

    def new_repo(self, name="repo"):
        return init_repo(os.path.join(self.tmp, name))


# ---------------------------------------------------------------------------------------------
# The three change texts, exactly as frozen (experiments/E-003/C*.md, the fenced block).

C1_TEXT = ("Before you write, read <path>: it is the role file of the agent that will check this plan.\n"
           "You need not follow it as instructions; read it so you know what the check looks for.")
C2_TEXT = "The inputs for this task, by path: <list>. Read these first."
C3_TEXT = ('A source you cannot open is not by itself a fault in the memo. List each one as\n'
           '"Not opened: <source>, <why>", and judge the claims that rest on it only by whether the memo\n'
           'states its grade and that it was not opened. Return the memo only for a fault you can show from\n'
           'what you opened or from the memo\'s own text.')
CHANGE_TEXT = {"C1": C1_TEXT, "C2": C2_TEXT, "C3": C3_TEXT}
CHANGE_FILE = {"C1": "experiments/E-003/C1-plans-read-the-check.md",
               "C2": "experiments/E-003/C2-built-named-inputs.md",
               "C3": "experiments/E-003/C3-research-check-what-it-can-open.md"}


def filled(change, fill):
    text = CHANGE_TEXT[change]
    return text.replace("<path>" if change == "C1" else "<list>", fill)


# ---------------------------------------------------------------------------------------------
# Pack manifests (spec: "How a hand-assembled pack is routed"), shared by the J7 and J8 tests.

MANIFEST_LINE = re.compile(r"^([0-9a-f]{64})  (\S.*)$")


def parse_manifest(text):
    """Parse the `## Pack manifest` section of a brief record in the named form.
    Returns (files, commit, brief_sha, problems); files is [(sha, path)]."""
    problems = []
    m = re.search(r"^## Pack manifest[ \t]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        return [], None, None, ["no section headed exactly `## Pack manifest`"]
    body = m.group(1)
    blocks = re.findall(r"^```manifest[ \t]*\n(.*?)^```[ \t]*$", body, re.S | re.M)
    if len(blocks) != 1:
        return [], None, None, ["the section must hold exactly one fenced block whose info string is `manifest` "
                                "(found %d)" % len(blocks)]
    files, commit, brief = [], None, None
    for line in blocks[0].splitlines():
        if not line.strip():
            continue
        fm = MANIFEST_LINE.match(line)
        if fm:
            if commit is not None or brief is not None:
                problems.append("file line after the commit/brief lines: %r" % line)
            files.append((fm.group(1), fm.group(2)))
        elif re.fullmatch(r"commit: [0-9a-f]{40}", line):
            commit = line.split(": ", 1)[1]
        elif re.fullmatch(r"brief: [0-9a-f]{64}", line):
            brief = line.split(": ", 1)[1]
        else:
            problems.append("line not in the named form: %r" % line)
    paths = [p for _, p in files]
    if paths != sorted(paths, key=lambda s: s.encode("utf-8")):
        problems.append("paths not sorted in byte order")
    if len(set(paths)) != len(paths):
        problems.append("a path is listed twice")
    if commit is None:
        problems.append("no `commit: <full commit id>` line")
    if brief is None:
        problems.append("no `brief: <sha256>` line")
    return files, commit, brief, problems


def pack_entry(role):
    import tomllib
    with open(os.path.join(ROOT, "governance", "PACKS.toml"), "rb") as fh:
        return tomllib.load(fh)["roles"].get(role)


def pattern_matches(pattern, path):
    """Case-folded glob match, as session_runner.py compares (norm) and govlib.glob_match matches."""
    return govlib().glob_match(norm(pattern), norm(path))


def manifest_violations(entry, files, withheld=(), agent_file=None, extra_forbidden=()):
    """Paths in the manifest that the entry does not allow. `agent_file` alone is exempt from must_read."""
    bad = []
    must_read = entry.get("must_read", [])
    must_not = list(entry.get("must_not_see", [])) + list(withheld) + list(extra_forbidden)
    for _, path in files:
        if agent_file is not None and norm(path) == norm(agent_file):
            continue
        if not any(pattern_matches(p, path) for p in must_read):
            bad.append("%s: not allowed by must_read" % path)
        if any(pattern_matches(p, path) for p in must_not):
            bad.append("%s: matched by must_not_see" % path)
        n = norm(path)
        if n == "governance/holdouts.md" or n.startswith("holdouts/"):
            bad.append("%s: a holdout path" % path)
    return bad


# ---------------------------------------------------------------------------------------------
# Synthetic helper transcripts (Claude Code subagent form: one JSON object per line).

def tool_line(name, **inp):
    return json.dumps({"type": "assistant", "message": {"role": "assistant", "content": [
        {"type": "tool_use", "id": "toolu_x", "name": name, "input": inp}]}})


def text_line(text, role="assistant"):
    return json.dumps({"type": role, "message": {"role": role, "content": [{"type": "text", "text": text}]}})


def write_transcript(base, name, lines):
    path = os.path.join(base, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    return path


# ---------------------------------------------------------------------------------------------
# Reference for the owner's cards (experiments/E-003.md, Step 5), worked independently.
#
# A pairs file is a JSON list, in dispatch order, of
#   {"piece": id, "change": <label>, "control": <label>,
#    "verdicts": {<label>: "PASS"|"FAIL"}, "failed": {<label>: "2@src/x.py:3,..." or "-"},
#    "locked_failed": {<label>: bool}}            (built work only; absent = false)

def ref_groups(pairs):
    g1, g2, g3 = [], [], []
    for p in pairs:
        labels = sorted([p["change"], p["control"]])
        v = p["verdicts"]
        locked = p.get("locked_failed", {})
        for lab in labels:
            if locked.get(lab):
                continue
            if v[p["change"]] != v[p["control"]]:
                g1.append(lab)
            elif v[lab] == "PASS":
                g2.append(lab)
            else:
                g3.append(lab)
    return g1, g2, g3


def ref_allocation(g1, g2, g3, total=8):
    k = [4, 2, 2]
    have = [len(g1), len(g2), len(g3)]
    short = 0
    for i in range(3):
        if have[i] < k[i]:
            short += k[i] - have[i]
            k[i] = have[i]
    for i in (0, 2, 1):                       # the shortfall is drawn from G1, then G3, then G2
        take = min(short, have[i] - k[i])
        k[i] += take
        short -= take
    return k


def ref_sequence(pairs, seed, answers=None):
    """The cards shown, in order, as (label, group): 8, then one at a time while fewer than 6 hold a yes/no
    and fewer than 12 have been shown."""
    import random
    g = list(ref_groups(pairs))
    k = ref_allocation(*g)
    rng = random.Random(seed)
    seq = []
    for i in range(3):
        for lab in rng.sample(g[i], k[i]):
            seq.append((lab, "G%d" % (i + 1)))
    left = {i: [x for x in g[i] if x not in {s[0] for s in seq}] for i in range(3)}
    if answers is None:
        return seq                            # the first eight, before any answer
    while True:
        answered = sum(1 for lab, _ in seq if answers.get(lab, "").lower().strip() in ("yes", "no"))
        if answered >= 6 or len(seq) >= 12:
            break
        for i in (0, 2, 1):                    # further cards: G1, then G3, then G2
            if left[i]:
                lab = rng.choice(left[i])
                left[i].remove(lab)
                seq.append((lab, "G%d" % (i + 1)))
                break
        else:
            break
    return seq


def make_pairs(spec, locked=()):
    """spec: list of (change verdict, control verdict); labels are c<i>, k<i>."""
    out = []
    for i, (vc, vk) in enumerate(spec):
        c, k = "c%02d" % i, "k%02d" % i
        out.append({"piece": "p%02d" % i, "change": c, "control": k, "verdicts": {c: vc, k: vk},
                    "failed": {c: "-" if vc == "PASS" else "1@src/a.py:%d" % (i + 1),
                               k: "-" if vk == "PASS" else "2@src/b.py:%d" % (i + 1)},
                    "locked_failed": {c: c in locked, k: k in locked}})
    return out


def recorded_manifests(setting=None):
    """[(brief path, text)] of every docs/briefs record holding a `## Pack manifest` section.  If the
    environment variable `setting` is set (J8: S001_BLIND_MANIFEST; J7: S001_ANALYSIS_MANIFEST; a path from
    the repository root), that one record is returned whatever it holds, and nothing is scanned."""
    env = os.environ.get(setting) if setting else None
    paths = []
    if env:
        paths = [env]
    else:
        d = os.path.join(ROOT, "docs", "briefs")
        paths = [os.path.join("docs", "briefs", f) for f in sorted(os.listdir(d)) if f.endswith(".md")]
    out = []
    for rel in paths:
        with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
            text = fh.read()
        if env or re.search(r"^## Pack manifest[ \t]*$", text, re.M):
            out.append((rel, text))   # a record named by the setting is checked whatever it holds
    return out


def manifest_kind(text):
    """Classify a recorded manifest by its parsed file lines (never by the record's other text):
    "analysis" if the files include experiments/E-003.md; "blind" if they include the extract or
    .claude/agents/check-author.md; else None."""
    files, _, _, _ = parse_manifest(text)
    paths = {norm(p) for _, p in files}
    if "experiments/e-003.md" in paths:
        return "analysis"
    if "experiments/e-003/check-author-extract.md" in paths or ".claude/agents/check-author.md" in paths:
        return "blind"
    return None


def good_manifest(paths, commit="0123456789abcdef0123456789abcdef01234567", brief="ab" * 32):
    """Render a manifest section in the named form (sorted by byte order, sha256 + two spaces + path)."""
    lines = ["%s  %s" % (sha256(p), p) for p in sorted(paths, key=lambda s: s.encode("utf-8"))]
    return "## Pack manifest\n\n```manifest\n%s\ncommit: %s\nbrief: %s\n```\n\n## Helper brief\n\nText.\n" % (
        "\n".join(lines), commit, brief)
