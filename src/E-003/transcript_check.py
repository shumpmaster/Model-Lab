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
    in a Bash command, every path anywhere inside every word is checked, a quoted argument included:
      * a shell run with -c (`bash -c`, `sh -lc`, `sudo sh -c`, `find -exec sh -c`) and `eval` have
        their script checked as a command of its own, /tmp creation inside it included;
      * inline code (`python3 -c`, a heredoc to an interpreter, `node -e`, `perl -e`, `ruby -e`,
        `php -r`, an awk program) may read or write, so there even /usr, /bin, /lib and /etc leak, and
        a network library leaks;
      * `$PWD` and `$(pwd)` are the working directory; a path rooted in any other variable
        (`$D/x`, `${D}/../x`) leaks, since it may lie anywhere;
      * a quoted string that only looks like a path (`echo "/home/user"`) is read as a path, and so is
        one in a heredoc's body given to cat or tee, where only `$NAME/` is read as text;
      * only a sed or grep pattern is never opened, so it is not checked, except sed's r and w commands;
  - web or network use: WebFetch or WebSearch, any URL or `git@host:` in a command, curl, wget, ssh,
    scp, sftp, rsync, nc, socat, telnet, ftp, a git fetch, pull, clone, push, ls-remote or submodule, a
    git subcommand naming a URL or address or `git remote add|set-url`, a network listener
    (`python3 -m http.server`, `php -S`), or a package install; with --web-sources, a WebFetch (or a
    curl or wget) of a URL listed there is allowed, and nothing else (the research judge opens only the
    memo's sources);
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
                "aria2c", "http", "https", "socat")
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
            return mode == "r"           # "x" (inside inline code) may read or write: not allowed
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

    def bash(self, cmd, base=None, depth=0):
        if depth > 8:
            raise Leak("wrappers nested too deep to check")
        base = base or self.cwd
        cmd = PWD_CMD.sub("$PWD", cmd)
        rest, bodies = cut_heredocs(cmd)
        commands = split_commands(shell_words(rest))
        docs = assign_heredocs(commands, bodies)
        # creations first, wrapped scripts and heredocs to a shell included: the line that creates a /tmp
        # path is clean for it
        self.creations(commands, base, depth, docs)
        # network
        if LISTEN_RX.search(cmd):
            raise Leak("a network listener")
        urls = URL.findall(cmd)
        reaches = bool(NET_HINT.search(cmd))
        if SCP_URL.search(cmd) and re.search(r"\b(git|scp|rsync|ssh|sftp)\b", cmd):
            raise Leak("a remote repository or host in a command")
        for c in commands:
            k = command_start(c)
            if k >= len(c):
                continue
            word, args = posixpath.basename(c[k]), c[k:]
            if word in NET_COMMANDS:
                reaches = True
                if word in ("curl", "wget") and urls and all(self.url_ok(u) for u in urls):
                    continue
                raise Leak("network use (%s)" % word)
            if word == "git":
                if any(a in GIT_NET for a in args[1:]):
                    raise Leak("a git command that reaches another repository")
                if any(URL.search(a) or SCP_URL.search(a) for a in args[1:]):
                    raise Leak("a git command naming another repository")
                for j, a in enumerate(args[1:-1], 1):
                    if a == "remote" and args[j + 1] in ("add", "set-url"):
                        raise Leak("a git command naming another repository (remote %s)" % args[j + 1])
            if word in INSTALLERS and any(a in ("install", "add", "i", "get", "fetch") for a in args[1:]):
                raise Leak("a package install")
        if reaches and any(not self.url_ok(u) for u in urls):
            raise Leak("a URL in a command that can reach the network")
        # paths, following `cd`
        here = base
        for n, c in enumerate(commands):
            k = command_start(c)
            if k < len(c) and c[k] == "cd":
                target = c[k + 1] if len(c) > k + 1 else "~"
                p = self.resolve(PWD_WORD.sub(lambda m: here, target), here)
                if p is None or not self.path_ok(p, "r"):
                    raise Leak("a command on a path outside the copy (cd)")
                here = p
                continue
            wrapped = wrapper_scripts(c)
            for script in wrapped.values():
                self.bash(script, here, depth + 1)
            skip = set(wrapped)
            # each heredoc body by what it is given to: a shell runs it as commands, an interpreter as
            # code; anything else (cat, tee, git commit -F -) takes it as data
            family = heredoc_family(c)
            for body in docs.get(n, ()):
                if family == SHELL:
                    self.bash(body, here, depth + 1)
                elif family == TEXT:
                    self.scan_word(body, "r", here, TEXT)
                else:
                    if NET_CODE_RX.search(body):
                        raise Leak("network use in inline code")
                    self.scan_word(body, "x", here, family)
            if k < len(c) and posixpath.basename(c[k]) == "eval":
                continue                     # its words were checked as a command above
            patterns, code = pattern_positions(c), code_positions(c)
            for i, w in enumerate(c):
                if i in skip:
                    continue
                if i in patterns:
                    if posixpath.basename(c[command_start(c)]) == "sed":
                        for cmdch, target in SED_FILE_RX.findall(w):
                            mode = "w" if cmdch in "wW" else "r"
                            if not self.path_ok(target.strip(), mode, base=here):
                                raise Leak("a sed script reads or writes a file outside the copy")
                    continue                 # a sed or grep pattern, never opened
                family = None
                if i in code:
                    if NET_CODE_RX.search(w):
                        raise Leak("network use in inline code")
                    mode, family = "x", code[i]
                elif (i > 0 and c[i - 1] in REDIRECTS) or REDIRECT_WORD.fullmatch(w):
                    mode = "w"
                else:
                    mode = "r"
                self.scan_word(w, mode, here, family)

    def creations(self, commands, base, depth, docs=None):
        for n, c in enumerate(commands):
            for i, w in enumerate(c):
                if w in REDIRECTS and i + 1 < len(c):
                    self.create(c[i + 1], base=base)
                m = REDIRECT_WORD.fullmatch(w)
                if m:
                    self.create(m.group(1), base=base)
            k = command_start(c)
            if k < len(c) and posixpath.basename(c[k]) in ("touch", "mkdir"):
                for x in c[k + 1:]:
                    if x in REDIRECTS:
                        break
                    if not x.startswith("-"):
                        self.create(x, is_dir=posixpath.basename(c[k]) == "mkdir", base=base)
            if depth < 8:
                scripts = list(wrapper_scripts(c).values())
                if docs and heredoc_family(c) == SHELL:
                    scripts += docs.get(n, [])
                for script in scripts:
                    rest, bodies = cut_heredocs(PWD_CMD.sub("$PWD", script))
                    inner = split_commands(shell_words(rest))
                    self.creations(inner, base, depth + 1, assign_heredocs(inner, bodies))

    def scan_word(self, w, mode, here, family=None):
        """Every path inside one shell word, wherever it sits in the word (a quoted argument included).
        `family` names the interpreter when the word is inline code: there `$NAME/` is text, not a
        variable, except in perl and php, whose variables are written so."""
        w = PWD_WORD.sub(lambda m: here, w)
        s = PLACEHOLDER.sub("X", URL.sub(" ", w))
        if HOME_RX.search(s):
            raise Leak("a command on the home folder")
        if (family is None or family in SIGIL_FAMILIES) and VAR_PATH_RX.search(s):
            raise Leak("a path rooted in a variable, which may lie anywhere")
        for m in ABS_RX.finditer(s):
            p = m.group(1).rstrip(".,")
            if not self.path_ok(p, mode, base=here):
                raise Leak("a command on a path outside the copy")
        for tok in TOKEN_SPLIT.split(s):
            if family is None and tok in ("/", "/.", "/.."):
                raise Leak("a command on the root folder")   # in code, a lone `/` is division
            if tok and not tok.startswith("/") and ".." in tok.split("/"):
                if "$" in tok or not self.path_ok(tok, mode, base=here):
                    raise Leak("a relative path that leaves the copy")


SHELLS = ("bash", "sh", "zsh", "dash", "ksh", "ash", "mksh", "fish")
INTERPRETER_RX = re.compile(r"(python[0-9.]*|pypy[0-9.]*|node|nodejs|deno|bun|perl|ruby|php|lua|luajit|Rscript|"
                            r"tclsh|osascript)")
CODE_FLAGS = {"python": ("-c",), "pypy": ("-c",), "node": ("-e", "-p", "--eval", "--print"),
              "nodejs": ("-e", "-p", "--eval", "--print"), "bun": ("-e", "-p", "--eval", "--print"),
              "ruby": ("-e",), "php": ("-r",), "lua": ("-e",), "luajit": ("-e",), "Rscript": ("-e",),
              "osascript": ("-e",)}
AWKS = ("awk", "gawk", "mawk", "nawk")
SIGIL_FAMILIES = ("perl", "php")
TEXT = "text"
SHELL = "shell"
PATTERN_COMMANDS = ("sed", "grep", "egrep", "fgrep", "rg")
# A word that is itself a redirection with its target, e.g. `2>/dev/null` or `>out.txt`.
REDIRECT_WORD = re.compile(r"\d*(?:>>?|>\||&>>?)(.+)")
# An absolute path anywhere in a word, not counting a slash that follows a word character, a dot, a glob
# character, another slash, a variable's closing brace or a `$` (those are relative or variable paths).
ABS_RX = re.compile(r"(?<![\w.~*?\]/$}-])(/[A-Za-z0-9._@+-][^\s'\"`;|&<>(){},]*)")
HOME_RX = re.compile(r"(?<![\w$])~(?=/|$|\s|[A-Za-z_])|\$HOME\b|\$\{HOME\}")
VAR_PATH_RX = re.compile(r"\$\{?[A-Za-z0-9_]+\}?/")
PWD_WORD = re.compile(r"\$\{PWD\}|\$PWD\b")
PWD_CMD = re.compile(r"\$\(\s*pwd\s*\)|`\s*pwd\s*`")
# A `<name>` placeholder in text (`refs/remotes/<remote>/HEAD`) is a word, so the path after it is relative.
PLACEHOLDER = re.compile(r"<[A-Za-z][A-Za-z0-9 _.-]*>")
TOKEN_SPLIT = re.compile(r"[\s'\"`(),;=<>{}\[\]|&:]+")
SED_FILE_RX = re.compile(r"(?:^|[;\n{}/0-9$!])\s*([rRwW])\s+([^;\n}]+)")
LISTEN_RX = re.compile(r"\b(http\.server|SimpleHTTPServer|socketserver|xmlrpc\.server|smtpd)\b|\bphp\s+(-\S+\s+)*-S\b|"
                       r"\bsocat\b|\b(http-server|ngrok)\b")
NET_CODE_RX = re.compile(r"urllib\.request|urlopen|\brequests\.(get|post|put|head|patch|delete|request|Session)\b|"
                         r"http\.client|\bhttpx\b|\baiohttp\b|\bsocket\b|\bfetch\s*\(|\bhttps?\.(get|request)\b|"
                         r"\bnet\.(connect|createConnection)\b|XMLHttpRequest|LWP::|IO::Socket|Net::HTTP|open-uri")


def split_commands(words):
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
    return commands


def command_start(c):
    """Index of the command word of one simple command, past assignments, keywords and wrappers."""
    i = 0
    while i < len(c) and re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*=.*", c[i]):
        i += 1
    while i < len(c) and (c[i] in PREFIX_WORDS or c[i] == "timeout"):
        i += 2 if c[i] == "timeout" else 1
    return i


def wrapper_scripts(c):
    """{word position: script} for each shell run with -c (bash -c, sh -lc, sudo sh -c, find -exec sh -c)
    and for eval, whose words are the script."""
    out = {}
    k = command_start(c)
    if k < len(c) and posixpath.basename(c[k]) == "eval" and len(c) > k + 1:
        out[k + 1] = " ".join(c[k + 1:])
        return out
    for i, w in enumerate(c):
        if posixpath.basename(w) not in SHELLS:
            continue
        j = i + 1
        while j < len(c) and c[j].startswith("-") and not c[j].startswith("--"):
            if "c" in c[j][1:]:
                if j + 1 < len(c):
                    out[j + 1] = c[j + 1]
                break
            j += 1
    return out


def code_positions(c):
    """{word position: interpreter family} of inline interpreter code: python -c, node -e, perl -e,
    ruby -e, an awk program, deno eval.  (A heredoc's body is cut out before the words are made.)"""
    out = {}
    k = command_start(c)
    if k >= len(c):
        return out
    name = posixpath.basename(c[k])
    m = INTERPRETER_RX.fullmatch(name)
    family = "awk" if name in AWKS else re.sub(r"[0-9.]+$", "", name)
    if name in AWKS:
        j = k + 1
        while j < len(c):
            if c[j] in ("-f", "--file"):
                return out
            if c[j] in ("-F", "-v") :
                j += 2
                continue
            if c[j].startswith("-") and c[j] != "-":
                j += 1
                continue
            out[j] = family
            break
        return out
    if not m:
        return out
    if family == "deno" and len(c) > k + 2 and c[k + 1] == "eval":
        out[k + 2] = family
    for j in range(k + 1, len(c) - 1):
        w = c[j]
        if family == "perl":
            if re.fullmatch(r"-[A-Za-z]*[eE]", w):
                out[j + 1] = family
        elif w in CODE_FLAGS.get(family, ()):
            out[j + 1] = family
        elif family in ("python", "pypy") and re.fullmatch(r"-[A-Za-z]*c", w):
            out[j + 1] = family
    return out


def heredoc_family(c):
    """What a heredoc in this simple command is given to: SHELL (bash, sh: run as commands), an
    interpreter's family (code), or TEXT (any other command: data written out, not run)."""
    k = command_start(c)
    if k >= len(c):
        return TEXT
    name = posixpath.basename(c[k])
    if name in SHELLS:
        return SHELL
    if name in AWKS:
        return "awk"
    return re.sub(r"[0-9.]+$", "", name) if INTERPRETER_RX.fullmatch(name) else TEXT


HEREDOC_RX = re.compile(r"(?<!<)<<(?!<)(-?)[ \t]*(['\"]?)([A-Za-z0-9_.-]+)\2")


def cut_heredocs(cmd):
    """(the command with each heredoc's body and terminator line taken out, [bodies in order]).  The
    marker (`<<'EOF'`) stays, so the command still shows where each body belongs."""
    bodies, pos = [], 0
    while True:
        m = HEREDOC_RX.search(cmd, pos)
        if not m:
            break
        nl = cmd.find("\n", m.end())
        if nl < 0:
            break
        dash, delim = m.group(1), m.group(3)
        j, start = nl + 1, nl + 1
        end_start = end_after = len(cmd)
        while j < len(cmd):
            k = cmd.find("\n", j)
            line = cmd[j:k if k >= 0 else len(cmd)]
            if (line.lstrip("\t") if dash else line) == delim:
                end_start, end_after = j, (k + 1 if k >= 0 else len(cmd))
                break
            if k < 0:
                break
            j = k + 1
        bodies.append(cmd[start:end_start])
        cmd = cmd[:start] + cmd[end_after:]
        pos = m.end()
    return cmd, bodies


def assign_heredocs(commands, bodies):
    """{command index: [bodies]}, one body per heredoc marker word, in order."""
    out, it = {}, iter(bodies)
    for n, c in enumerate(commands):
        for w in c:
            if HEREDOC_RX.match(w) or w in ("<<", "<<-"):
                body = next(it, None)
                if body is not None:
                    out.setdefault(n, []).append(body)
    return out


def pattern_positions(c):
    """Word positions of the pattern or script of sed, grep and rg in one simple command: each word after
    -e, or else the first word that is not an option.  (awk and perl programs are code, not patterns.)"""
    out = set()
    i = command_start(c)
    if i >= len(c) or posixpath.basename(c[i]) not in PATTERN_COMMANDS:
        return out
    with_e = [j for j in range(i + 1, len(c)) if c[j] in ("-e", "--expression", "--regexp")]
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


# Words that come before a command word: shell keywords and wrappers.
PREFIX_WORDS = ("do", "then", "else", "elif", "if", "while", "until", "!", "{", "sudo", "env", "command", "exec",
                "time", "nohup", "xargs")
VALUE_OPTIONS = ("-F", "-v", "-A", "-B", "-C", "-m", "-f", "--file", "-t", "--type", "-g", "--glob")


def shell_words(cmd):
    try:
        lex = shlex.shlex(cmd, posix=True, punctuation_chars=True)
        lex.whitespace_split = True
        return list(lex)
    except ValueError:
        return cmd.split()


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
