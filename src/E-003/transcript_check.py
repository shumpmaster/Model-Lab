"""The transcript check (spec S-001, "The sheet's route" step 3 and J5; E-003 Exclusions 2; E-001 F4).

  python3 -I src/E-003/transcript_check.py check --cwd DIR [--web-sources FILE] [--allow-path P ...]
          [--sheets-repo NAME ...] TRANSCRIPT.jsonl

Reads one helper transcript (Claude Code's subagents/agent-<id>.jsonl, one JSON object per line) and
prints `clean` (exit 0), or `leak@<line>` (exit 1) for the first transcript line that leaks, the reason
on standard error.  A missing or unreadable transcript prints `missing` and exits 1 (E-001 F4: a missing
transcript fails by rule).  Used on arms and source checks (the work side), on the blind Check author
(the sheet lead) and on judges (the judging lead), with --cwd the run's copy or pack folder.

A line leaks when it holds:
  - a tool call that reads, searches, writes or runs a command on a path outside --cwd, other than
      * /usr, /bin, /lib and /etc, read only (E-001 F4), and /dev/null as a redirection target;
      * a path under /tmp that the run itself created, on the line that creates it and on later lines
        only, never before: created means a Bash `>` or `>>` redirection target (also `>|`, `&>`,
        `&>>`, `2>`), a `touch` or `mkdir` argument, or a Write or Edit file_path; a path inside a
        folder the run made with `mkdir` counts as created with it;
      * each --allow-path, exactly (a file the harness saved of the run's own output, at the path the
        harness named to it; E-003 Exclusions 2);
    relative paths are read from --cwd, `..` included; `~` and $HOME are outside;
  - web or network use: WebFetch or WebSearch, any URL or `git@host:` in a command, curl, wget, ssh,
    scp, sftp, rsync, nc, telnet, ftp, a git fetch, pull, clone, push, ls-remote or submodule, or a
    package install; with --web-sources, a WebFetch (or a curl or wget) of a URL listed there is
    allowed, and nothing else (the research judge opens only the memo's sources);
  - any mention of a --sheets-repo name, in any tool call;
  - a tool this check does not know (an MCP tool, a helper started by the helper, a skill): its reach
    cannot be shown to stay in --cwd, so it counts as a leak;
  - a `cwd` field outside --cwd, or a line that is not JSON (a call it may hide cannot be checked).
"""
import argparse
import json
import os
import posixpath
import re
import shlex
import sys

READ_ONLY_SYSTEM = ("/usr", "/bin", "/lib", "/etc")
DEVICES = ("/dev/null",)
PATH_TOOLS = {"Read": ("file_path", "r"), "NotebookRead": ("notebook_path", "r"),
              "Write": ("file_path", "w"), "Edit": ("file_path", "w"), "MultiEdit": ("file_path", "w"),
              "NotebookEdit": ("notebook_path", "w"), "Glob": ("path", "r"), "Grep": ("path", "r"),
              "LS": ("path", "r")}
HARMLESS_TOOLS = ("TodoWrite", "ToolSearch", "BashOutput", "KillShell", "KillBash", "SubagentHandback")
NET_COMMANDS = ("curl", "wget", "ssh", "scp", "sftp", "rsync", "nc", "ncat", "netcat", "telnet", "ftp", "lftp",
                "aria2c", "http", "https")
GIT_NET = ("fetch", "pull", "clone", "push", "ls-remote", "submodule")
INSTALLERS = ("pip", "pip3", "npm", "npx", "yarn", "pnpm", "gem", "cargo", "apt", "apt-get", "brew", "uv")
REDIRECTS = (">", ">>", ">|", "&>", "&>>")
SEPARATORS = (";", "&&", "||", "|", "&", "(", ")", "\n", "|&")
URL = re.compile(r"\b[A-Za-z][A-Za-z0-9+.-]*://[^\s'\"`<>]*")
SCP_URL = re.compile(r"\b[\w.-]+@[\w.-]+:")
# A command can reach the network when it names a network tool or library; a URL in any other command
# (for example in text a script writes) is data.
NET_HINT = re.compile(r"\b(urllib|urlopen|requests|http\.client|httpx|aiohttp|socket|webbrowser|fetch|curl|wget)\b")


class Leak(Exception):
    pass


class Checker:
    def __init__(self, cwd, sources=None, allow=(), sheets=()):
        self.cwd = posixpath.normpath(os.path.abspath(cwd))
        self.sources = None if sources is None else {s.rstrip("/") for s in sources}
        self.allow = {posixpath.normpath(os.path.abspath(p)) for p in allow}
        self.sheets = [s.lower() for s in sheets if s]
        self.created = set()
        self.created_dirs = set()

    # -- paths ---------------------------------------------------------------------------------
    def resolve(self, p, base=None):
        if p.startswith("~") or "$HOME" in p or "${HOME}" in p:
            return None                      # the home folder: outside
        if not p.startswith("/"):
            p = posixpath.join(base or self.cwd, p)
        return posixpath.normpath(p)

    @staticmethod
    def under(p, root):
        return p == root or p.startswith(root.rstrip("/") + "/")

    def tmp_created(self, p):
        return p in self.created or any(self.under(p, d) for d in self.created_dirs)

    def path_ok(self, raw, mode, base=None):
        p = self.resolve(raw, base)
        if p is None:
            return False
        if self.under(p, self.cwd) or p in self.allow:
            return True
        if p in DEVICES:
            return True
        if any(self.under(p, s) for s in READ_ONLY_SYSTEM):
            return mode == "r"
        if self.under(p, "/tmp"):
            return self.tmp_created(p)
        return False

    def create(self, raw, is_dir=False, base=None):
        p = self.resolve(raw, base)
        if p is None or not self.under(p, "/tmp"):
            return
        (self.created_dirs if is_dir else self.created).add(p)
        if is_dir:
            self.created.add(p)

    def url_ok(self, url):
        return self.sources is not None and url.rstrip("/") in self.sources

    # -- one tool call -------------------------------------------------------------------------
    def call(self, name, inp, base=None):
        blob = (name + " " + json.dumps(inp, ensure_ascii=False)).lower()
        for s in self.sheets:
            if s in blob:
                raise Leak("names the sheets repository")
        if name in ("WebFetch",):
            if not self.url_ok(str(inp.get("url", ""))):
                raise Leak("web use outside the allowed sources")
            return
        if name == "Bash":
            self.bash(str(inp.get("command", "")), base)
            return
        if name in PATH_TOOLS:
            key, mode = PATH_TOOLS[name]
            raw = inp.get(key)
            if name in ("Write", "Edit", "MultiEdit") and isinstance(raw, str):
                self.create(raw)
            if isinstance(raw, str) and raw:
                if name == "Glob":
                    raw = glob_root(raw)
                if not self.path_ok(raw, mode):
                    raise Leak("%s on a path outside the copy" % name)
            if name == "Glob":
                pat = inp.get("pattern")
                if isinstance(pat, str) and (pat.startswith("/") or pat.startswith("~") or ".." in pat.split("/")):
                    base = inp.get("path") if isinstance(inp.get("path"), str) else self.cwd
                    root = glob_root(pat)
                    p = self.resolve(root, self.resolve(base) or self.cwd)
                    if p is None or not self.path_ok(p, "r"):
                        raise Leak("Glob pattern outside the copy")
            return
        if name in HARMLESS_TOOLS:
            return
        if name == "WebSearch":
            raise Leak("web search")
        raise Leak("a tool whose reach cannot be checked (%s)" % name)

    def bash(self, cmd, base=None):
        base = base or self.cwd
        words = shell_words(cmd)
        commands, current = [], []
        for w in words:
            if w in SEPARATORS:
                if current:
                    commands.append(current)
                current = []
            else:
                current.append(w)
        if current:
            commands.append(current)
        # creations first: the line that creates a /tmp path is clean for it (and only from then on)
        for c in commands:
            for i, w in enumerate(c):
                if w in REDIRECTS and i + 1 < len(c):
                    self.create(c[i + 1], base=base)
                m = re.fullmatch(r"\d*(?:>>?|>\||&>>?)(.+)", w)
                if m:
                    self.create(m.group(1), base=base)
            args = strip_assignments(c)
            if args and posixpath.basename(args[0]) in ("touch", "mkdir"):
                for x in args[1:]:
                    if x in REDIRECTS:
                        break
                    if not x.startswith("-"):
                        self.create(x, is_dir=posixpath.basename(args[0]) == "mkdir", base=base)
        # network
        urls = URL.findall(cmd)
        reaches = bool(NET_HINT.search(cmd))
        if SCP_URL.search(cmd) and re.search(r"\b(git|scp|rsync|ssh|sftp)\b", cmd):
            raise Leak("a remote repository or host in a command")
        for c in commands:
            args = strip_assignments(c)
            if not args:
                continue
            word = posixpath.basename(args[0])
            if word in NET_COMMANDS:
                reaches = True
                if word in ("curl", "wget") and urls and all(self.url_ok(u) for u in urls):
                    continue
                raise Leak("network use (%s)" % word)
            if word == "git" and any(a in GIT_NET for a in args[1:]):
                raise Leak("a git command that reaches another repository")
            if word in INSTALLERS and any(a in ("install", "add", "i", "get", "fetch") for a in args[1:]):
                raise Leak("a package install")
        if reaches and any(not self.url_ok(u) for u in urls):
            raise Leak("a URL in a command that can reach the network")
        # paths, word by word, following `cd`
        here = base
        for c in commands:
            args = strip_assignments(c)
            if args and args[0] == "cd":
                target = args[1] if len(args) > 1 else "~"
                p = self.resolve(target, here)
                if p is None or not self.path_ok(p, "r"):
                    raise Leak("a command on a path outside the copy (cd)")
                here = p
                continue
            scripts = script_positions(c)
            for i, w in enumerate(c):
                if i in scripts:
                    continue                 # a sed, awk, grep or perl script, not a path
                mode = "w" if i > 0 and c[i - 1] in REDIRECTS else "r"
                if re.fullmatch(r"\d*(?:>>?|>\||&>>?).+", w):
                    mode = "w"
                for cand in candidates(w):
                    if URL.match(cand):
                        continue
                    if cand.startswith("~") or "$HOME" in cand or "${HOME}" in cand:
                        raise Leak("a command on the home folder")
                    if cand.startswith("/") or ".." in cand.split("/"):
                        if not self.path_ok(cand, mode, base=here):
                            raise Leak("a command on a path outside the copy")


# Words that come before a command word: shell keywords and wrappers.
PREFIX_WORDS = ("do", "then", "else", "elif", "if", "while", "until", "!", "{", "sudo", "env", "command", "exec",
                "time", "nohup", "xargs")
SCRIPT_COMMANDS = ("sed", "awk", "gawk", "mawk", "nawk", "grep", "egrep", "fgrep", "rg", "perl")
VALUE_OPTIONS = ("-F", "-v", "-A", "-B", "-C", "-m", "-f", "-i.bak", "--file", "-t", "--type", "-g", "--glob")


def script_positions(c):
    """Word positions of the script or pattern argument of sed, awk, grep, rg and perl in one simple
    command: each word after -e, or else the first word that is not an option."""
    out = set()
    i = 0
    while i < len(c) and re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*=.*", c[i]):
        i += 1
    while i < len(c) and (c[i] in PREFIX_WORDS or c[i] == "timeout"):
        i += 2 if c[i] == "timeout" else 1
    if i >= len(c) or posixpath.basename(c[i]) not in SCRIPT_COMMANDS:
        return out
    args = list(range(i + 1, len(c)))
    with_e = [j for j in args if c[j] in ("-e", "--expression", "--regexp")]
    if with_e:
        return {j + 1 for j in with_e if j + 1 < len(c)}
    j = i + 1
    while j < len(c):
        w = c[j]
        if w in REDIRECTS:
            break
        if w in VALUE_OPTIONS:
            j += 2
            continue
        if w.startswith("-") and w != "-":
            j += 1
            continue
        out.add(j)
        break
    return out


def shell_words(cmd):
    try:
        lex = shlex.shlex(cmd, posix=True, punctuation_chars=True)
        lex.whitespace_split = True
        return list(lex)
    except ValueError:
        return cmd.split()


def candidates(word):
    """The path-like parts of one shell word: the word, a redirection's target, an `=` value, and each
    `:`-separated part of a value that starts with `/`."""
    out = [word]
    m = re.fullmatch(r"\d*(?:>>?|>\||&>>?)(.+)", word)
    if m:
        out.append(m.group(1))
    if "=" in word:
        out.append(word.split("=", 1)[1])
    more = []
    for c in out:
        if c.startswith("/") and ":" in c:
            more += [x for x in c.split(":") if x]
    return out + more


def strip_assignments(args):
    i = 0
    while i < len(args) and re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*=.*", args[i]):
        i += 1
    rest = args[i:]
    while rest and (rest[0] in PREFIX_WORDS or rest[0] == "timeout"):
        rest = rest[2:] if rest[0] == "timeout" else rest[1:]
    return rest


def glob_root(pattern):
    """The part of a glob pattern before its first wildcard segment."""
    segs = pattern.split("/")
    out = []
    for s in segs:
        if any(ch in s for ch in "*?[{"):
            break
        out.append(s)
    root = "/".join(out)
    if pattern.startswith("/") and not root:
        return "/"
    return root or "."


def tool_calls(rec):
    msg = rec.get("message")
    if not isinstance(msg, dict):
        return
    content = msg.get("content")
    if not isinstance(content, list):
        return
    for block in content:
        if isinstance(block, dict) and block.get("type") == "tool_use":
            inp = block.get("input")
            yield str(block.get("name", "")), inp if isinstance(inp, dict) else {}


def check(path, checker):
    try:
        with open(path, encoding="utf-8") as fh:
            lines = fh.read().split("\n")
    except (OSError, UnicodeDecodeError):
        return "missing", "the transcript is missing or unreadable"
    for n, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except ValueError:
            return "leak@%d" % n, "a line that is not JSON"
        if not isinstance(rec, dict):
            return "leak@%d" % n, "a line that is not a JSON object"
        cwd = rec.get("cwd")
        if isinstance(cwd, str) and not checker.under(posixpath.normpath(cwd), checker.cwd):
            return "leak@%d" % n, "a working directory outside the copy"
        base = posixpath.normpath(cwd) if isinstance(cwd, str) else None
        try:
            for name, inp in tool_calls(rec):
                checker.call(name, inp, base)
        except Leak as exc:
            return "leak@%d" % n, str(exc)
    return "clean", ""


def main(argv=None):
    ap = argparse.ArgumentParser(prog="transcript_check.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("--cwd", required=True, help="the run's copy (or pack folder)")
    c.add_argument("--web-sources", help="a file of URLs the run may open, one per line")
    c.add_argument("--allow-path", action="append", default=[], help="a saved-output file the run may read")
    c.add_argument("--sheets-repo", action="append", default=[], help="the sheets repository's name")
    c.add_argument("transcript")
    a = ap.parse_args(argv)
    sources = None
    if a.web_sources:
        with open(a.web_sources, encoding="utf-8") as fh:
            sources = [l.strip() for l in fh if l.strip()]
    result, why = check(a.transcript, Checker(a.cwd, sources, a.allow_path, a.sheets_repo))
    sys.stdout.write(result + "\n")
    if why:
        sys.stderr.write(why + "\n")
    sys.exit(0 if result == "clean" else 1)


if __name__ == "__main__":
    main()
