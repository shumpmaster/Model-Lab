"""The change texts, applied to a copy's brief and taken out again (spec S-001, J1 and AC11; E-003 Step 3;
experiments/E-003/C1-*.md, C2-*.md, C3-*.md).

  python3 -I src/E-003/change.py apply  --change C1|C2|C3 --brief FILE --task-statement FILE --fill TEXT
  python3 -I src/E-003/change.py remove --change Cn --brief FILE --fill TEXT
  python3 -I src/E-003/change.py verify-removal --change Cn --control FILE --changed FILE --fill TEXT
  python3 -I src/E-003/change.py fill-c1 --repo DIR --commit SHA
  python3 -I src/E-003/change.py fill-c2 --repo DIR --commit SHA --task-file FILE

apply   Inserts the change paragraph (the fenced block of the change's file, read from
        experiments/E-003/ in this repository, with `<path>` for C1 or `<list>` for C2 filled) as its own
        paragraph directly after the paragraph that holds the task statement.  When the task statement
        file is empty, or its text is not in the brief, there is no separate task statement: the
        paragraph goes after the brief's first paragraph and `recorded` is true (J1).  The brief's own
        line ends are kept (a CRLF brief gets a CRLF paragraph).  Prints {"brief", "placement",
        "recorded", "reason"}.  The live brief is never written: only the copy's brief, by the caller.
remove  Takes out the paragraph and its blank line, and nothing else (AC11); a brief without it comes
        back unchanged.  Prints {"brief", "removed"}.
verify-removal  The per-pair clean-removal check of each change's removal test: the no-change brief
        equals the change brief with the paragraph and its blank line removed, byte for byte, and the
        change brief does hold the paragraph.  Prints {"clean", "reason"}.
fill-c1 C1's `<path>`: the plan check's role file, .claude/agents/critic.md, at the start commit; a piece
        whose start commit lacks it is not eligible (E-003 Exclusions 6).
fill-c2 C2's `<list>`, mechanically, from files at the start commit only, comma-separated, each once, in
        C2's order: (1) the spec the task names, as specs/<id>.md:<first>-<last> for the stage or
        section the task cites (from its heading to the line before the next heading of the same or a
        higher level, trailing blank lines left out), or the whole file with no range; (2) every
        repository path the task names, a folder expanded to its files; (3) every ruling file under
        decisions/ that the cited stage or section names (the whole spec when none is cited); (4) every
        locked check file (tests/acceptance/**, checks/**) that names the spec's id, by a
        `join-test: <id>/` marker or in its path.  An empty list is not eligible.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import e003lib as L  # noqa: E402

CHANGE_FILES = {"C1": "C1-plans-read-the-check.md", "C2": "C2-built-named-inputs.md",
                "C3": "C3-research-check-what-it-can-open.md"}
PLACEHOLDER = {"C1": "<path>", "C2": "<list>", "C3": None}
PLAN_CHECK_ROLE_FILE = ".claude/agents/critic.md"
LOCKED_ROOTS = ("tests/acceptance/", "checks/")


def change_text(change):
    """The fenced block of the change file's `## The text` section, exactly as frozen."""
    path = os.path.join(L.ROOT, "experiments", "E-003", CHANGE_FILES[change])
    text = L.read_text(path).replace("\r\n", "\n")
    m = re.search(r"^## The text[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    blocks = re.findall(r"^```[^\n]*\n(.*?)^```[ \t]*$", m.group(1), re.S | re.M) if m else []
    if len(blocks) != 1:
        raise SystemExit("change.py: %s has no single fenced block under `## The text`" % path)
    return blocks[0].rstrip("\n")


def filled(change, fill):
    text = change_text(change)
    ph = PLACEHOLDER[change]
    return text.replace(ph, fill) if ph else text


def newline_of(text):
    return "\r\n" if "\r\n" in text else "\n"


def paragraph(change, fill, nl):
    return filled(change, fill).replace("\n", nl)


def para_end(brief, pos, nl):
    """End of the paragraph holding index `pos`: the next blank line, or the end of the text before its
    final line ends."""
    sep = brief.find(nl + nl, pos)
    if sep >= 0:
        return sep
    return len(brief.rstrip("\r\n"))


def apply(brief, task, change, fill):
    nl = newline_of(brief)
    para = paragraph(change, fill, nl)
    task = task.strip()
    pos = brief.find(task) if task else -1
    if pos >= 0:
        placement, recorded, reason = "after-task-statement", False, ""
        end = para_end(brief, pos + len(task), nl)
    else:
        placement, recorded = "after-first-paragraph", True
        reason = ("the brief has no separate task statement" if not task
                  else "the task statement is not in the brief as given")
        first = len(brief) - len(brief.lstrip("\r\n"))
        end = para_end(brief, first, nl)
    out = brief[:end] + nl + nl + para + brief[end:]
    return out, placement, recorded, reason


def remove(text, change, fill):
    for nl in ("\r\n", "\n"):
        para = paragraph(change, fill, nl)
        i = text.find(nl + nl + para)
        if i >= 0:
            return text[:i] + text[i + len(nl + nl + para):], True
        if text.startswith(para + nl + nl):
            return text[len(para + nl + nl):], True
    return text, False


# ---------------------------------------------------------------------------------------------
# Fills.

SPEC_RX = re.compile(r"(?<![\w./-])(specs/[A-Za-z0-9._-]+\.md)")
CITE_RX = re.compile(r"(?i)\b(stage|section|step|part|phase)\s+([A-Za-z0-9][A-Za-z0-9.-]*[A-Za-z0-9]|[A-Za-z0-9])")
SIGN_RX = re.compile(r"§\s*([0-9][0-9.]*)")
RULING_RX = re.compile(r"(?<![\w./-])(decisions/[A-Za-z0-9._/-]+\.md)")
HEADING_RX = re.compile(r"^(#{1,6})\s+(.*)$")


def cited_range(spec_text, task):
    """(first, last) line numbers of the stage or section the task cites, or None."""
    cites = [(w.lower(), n.lower()) for w, n in CITE_RX.findall(task)] + [("§", n) for n in SIGN_RX.findall(task)]
    if not cites:
        return None
    lines = spec_text.split("\n")
    heads = []
    for i, line in enumerate(lines, 1):
        m = HEADING_RX.match(line)
        if m:
            heads.append((i, len(m.group(1)), m.group(2).strip()))
    for word, num in cites:
        for k, (i, level, title) in enumerate(heads):
            t = title.lower()
            if word == "§":
                hit = re.match(r"(§\s*)?%s\b" % re.escape(num), t) is not None
            else:
                hit = re.search(r"\b%s\s+%s\b" % (re.escape(word), re.escape(num)), t) is not None or (
                    word == "section" and re.match(r"%s[.)\s]" % re.escape(num), t + " ") is not None)
            if hit:
                last = len(lines)
                for j, lv, _ in heads[k + 1:]:
                    if lv <= level:
                        last = j - 1
                        break
                while last > i and lines[last - 1].strip() == "":
                    last -= 1
                return i, last
    return None


def task_paths(task, files):
    """Repository paths the task statement names, expanded to files at the start commit, in order."""
    out = []
    fileset = set(files)
    for raw in task.split():
        w = raw.strip("`'\"()[]{}<>,;:!?")
        while w.endswith("."):
            w = w[:-1]
        if not w or w.startswith("/") or w.startswith("~") or "://" in w:
            continue
        if not ("/" in w or re.search(r"\.[A-Za-z0-9]+$", w)):
            continue
        w = re.sub(r":\d+(-\d+)?$", "", w)
        if w in fileset:
            out.append(w)
            continue
        d = w.rstrip("/") + "/"
        under = sorted(f for f in files if f.startswith(d))
        out.extend(under)
    return out


def fill_c2(repo, commit, task):
    files = L.files_at(repo, commit)
    fileset = set(files)
    items, seen = [], set()

    def add(x, key=None):
        k = key or x
        if k not in seen:
            seen.add(k)
            items.append(x)

    spec = next((s for s in SPEC_RX.findall(task) if s in fileset), None)
    section_text = ""
    spec_id = None
    if spec:
        spec_id = os.path.basename(spec)[:-3]
        text = L.show_at(repo, commit, spec) or ""
        rng = cited_range(text, task)
        if rng:
            add("%s:%d-%d" % (spec, rng[0], rng[1]), key=spec)
            section_text = "\n".join(text.split("\n")[rng[0] - 1:rng[1]])
        else:
            add(spec)
            section_text = text
    for p in task_paths(task, files):
        add(p)
    if spec:
        for r in sorted(set(RULING_RX.findall(section_text))):
            if r in fileset:
                add(r)
        marker = "join-test: %s/" % spec_id
        for f in sorted(files):
            if not f.startswith(LOCKED_ROOTS):
                continue
            if spec_id in f:
                add(f)
                continue
            body = L.show_at(repo, commit, f)
            if body is not None and marker in body:
                add(f)
    return items


# ---------------------------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(prog="change.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a1 = sub.add_parser("apply")
    a1.add_argument("--change", required=True, choices=sorted(CHANGE_FILES))
    a1.add_argument("--brief", required=True)
    a1.add_argument("--task-statement", required=True, help="a file holding the task statement's text")
    a1.add_argument("--fill", default="")
    r = sub.add_parser("remove")
    r.add_argument("--change", required=True, choices=sorted(CHANGE_FILES))
    r.add_argument("--brief", required=True)
    r.add_argument("--fill", default="")
    v = sub.add_parser("verify-removal")
    v.add_argument("--change", required=True, choices=sorted(CHANGE_FILES))
    v.add_argument("--control", required=True)
    v.add_argument("--changed", required=True)
    v.add_argument("--fill", default="")
    f1 = sub.add_parser("fill-c1")
    f1.add_argument("--repo", required=True)
    f1.add_argument("--commit", required=True)
    f2 = sub.add_parser("fill-c2")
    f2.add_argument("--repo", required=True)
    f2.add_argument("--commit", required=True)
    f2.add_argument("--task-file", required=True)
    a = ap.parse_args(argv)

    if a.cmd == "apply":
        out, placement, recorded, reason = apply(L.read_text(a.brief), L.read_text(a.task_statement), a.change, a.fill)
        L.emit({"brief": out, "placement": placement, "recorded": recorded, "reason": reason})
    if a.cmd == "remove":
        out, removed = remove(L.read_text(a.brief), a.change, a.fill)
        L.emit({"brief": out, "removed": removed})
    if a.cmd == "verify-removal":
        control, changed = L.read_text(a.control), L.read_text(a.changed)
        back, removed = remove(changed, a.change, a.fill)
        if not removed:
            L.emit({"clean": False, "reason": "the change brief does not hold the change paragraph"})
        if back != control:
            L.emit({"clean": False, "reason": "the briefs differ beyond the change paragraph: a set-up fault"})
        L.emit({"clean": True, "reason": ""})
    if a.cmd == "fill-c1":
        if not L.git_ok(a.repo, "cat-file", "-e", "%s:%s" % (a.commit, PLAN_CHECK_ROLE_FILE)):
            L.emit({"eligible": False, "fill": "", "reason": "no plan-check role file (%s) at the start commit"
                    % PLAN_CHECK_ROLE_FILE})
        L.emit({"eligible": True, "fill": PLAN_CHECK_ROLE_FILE, "reason": ""})
    if a.cmd == "fill-c2":
        try:
            items = fill_c2(a.repo, a.commit, L.read_text(a.task_file))
        except L.GitError as exc:
            L.refuse("refused: %s" % exc)
        if not items:
            L.emit({"eligible": False, "fill": "", "reason": "the list is empty: the task names no spec and no "
                    "path present at the start commit (E-003 Exclusions 6)"})
        L.emit({"eligible": True, "fill": ", ".join(items), "reason": ""})


if __name__ == "__main__":
    main()
