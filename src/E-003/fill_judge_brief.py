"""The judge-brief fill script (spec S-001, J4 and J5; E-003 Step 4).

  python3 -I src/E-003/fill_judge_brief.py --sheet FILE --fingerprint HEX --fill FILE.json --label L
          --copy-path DIR --out FILE

Run by the judging lead, in the judging session, before every judgement.  It reads the sheet
(holdouts/<set id>.md from the lead's clone of the sheets repository) and checks the SHA-256 of its bytes
against --fingerprint, the fingerprint the lead's brief copies from governance/HOLDOUTS.md.
  - On a match it writes the filled judge brief to --out: E-002's judge-brief template
    (experiments/E-002.md) with exactly E-003 Step 4's seven changes, filled from the export's
    `<label>.fill.json`, the neutral label and the copy's path.  The same inputs give the same brief,
    byte for byte.  It prints one line, the start of the judgement's J5 line: label, set id, the
    sheet's SHA-256 and the filled brief's SHA-256, tab-separated (no sheet text).
  - On a mismatch, or any other fault, it exits 1, writes nothing and prints a first line naming what it
    refused, never the sheet's text.
It creates no file but --out, and never creates a folder.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import e003lib as L  # noqa: E402

# E-002's template, as frozen, with E-003 Step 4's changes marked by number:
#   1 checker role id and role file; 2 the piece id is the neutral label; 3 what "Judge it against:"
#   names; 4 "Apply this check:", the check in full and the failing rule, after "Judge it against";
#   5 research only: the web for the memo's sources; 6 the return asks for the failed tests' numbers;
#   7 the foreground paragraph.
TEMPLATE = (
    "You are the {role} (your role file: {role_file}),\n"                                    # 1
    "doing the {review} of {label}.\n"                                                       # 2
    "\n"
    "Read your role file and the files its context pack names, as they are in {copy}. The work\n"
    "to judge: {judged}. Judge it\n"
    "against: {against}\n"                                                                   # 3
    "\n"
    "Apply this check:\n"                                                                    # 4
    "\n"
    "{sheet}"
    "\n"
    "The work fails if any test of this check fails.\n"                                      # 4
    "\n"
    "Work only in {copy}. Do not read, search or run commands on any path outside it, {web},"
    " and do not run git commands that reach any other repository. You are one of\n"
    "several independent judgements and see no other verdict.\n"
    "\n"
    "Return, first line: `Verdict: PASS` or `Verdict: FAIL`. Then the numbers of the tests of the check\n"
    "that failed, each citing file:line.\n"                                                  # 6
    "\n"
    "Run every command in the foreground and wait for it to end. Do not start background tasks. Your last\n"
    "message must begin with the verdict line.\n"                                            # 7
)
WEB_BAR = "do not\nuse the web"
WEB_RESEARCH = "use the web only to open the sources the memo cites"                         # 5


def sentence(text):
    text = text.strip()
    return text if text[-1:] in (".", "!", "?") else text + "."


def main(argv=None):
    ap = argparse.ArgumentParser(prog="fill_judge_brief.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sheet", required=True)
    ap.add_argument("--fingerprint", required=True)
    ap.add_argument("--fill", required=True)
    ap.add_argument("--label", required=True)
    ap.add_argument("--copy-path", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)

    if not L.full(L.SHA64, a.fingerprint):
        L.refuse("refused: the fingerprint is not 64 lowercase hex digits")
    try:
        with open(a.sheet, "rb") as fh:
            sheet_bytes = fh.read()
    except OSError:
        L.refuse("refused: the sheet cannot be read")
    sheet_sha = L.sha256_bytes(sheet_bytes)
    if sheet_sha != a.fingerprint:
        L.refuse("refused: the sheet's SHA-256 does not match the fingerprint; no brief written")
    try:
        sheet = sheet_bytes.decode("utf-8")
    except UnicodeDecodeError:
        L.refuse("refused: the sheet is not UTF-8")
    if not sheet.endswith("\n"):
        sheet += "\n"
    try:
        fill = L.read_json(a.fill)
    except (OSError, ValueError):
        L.refuse("refused: the fill file cannot be read as JSON")
    if fill.get("label") != a.label:
        L.refuse("refused: the fill file's label is not --label")
    kind = fill.get("kind")
    if kind not in L.KINDS:
        L.refuse("refused: the fill file names no kind")
    for key in ("checker_role", "role_file", "review", "judged"):
        if not isinstance(fill.get(key), str) or not fill[key]:
            L.refuse("refused: the fill file lacks %s" % key)
    if kind == "plans":
        against = fill.get("task_statement_text")
    else:
        against = fill.get("task_statement_path")
    if not isinstance(against, str) or not against.strip():
        L.refuse("refused: the fill file lacks the task statement (%s)" % (
            "its text" if kind == "plans" else "its path"))
    judged = fill["judged"]
    judged = ("the commit range %s in the copy" % judged) if ".." in judged else judged
    brief = TEMPLATE.format(role=fill["checker_role"], role_file=fill["role_file"], review=fill["review"],
                            label=a.label, copy=a.copy_path, judged=judged, against=sentence(against),
                            sheet=sheet, web=WEB_RESEARCH if kind == "research" else WEB_BAR)
    out_dir = os.path.dirname(os.path.abspath(a.out))
    if not os.path.isdir(out_dir):
        L.refuse("refused: the folder of --out does not exist")
    data = brief.encode("utf-8")
    with open(a.out, "wb") as fh:
        fh.write(data)
    base = os.path.basename(a.sheet)
    set_id = base[:-3] if base.endswith(".md") and L.full(L.SET_ID, base[:-3]) else "-"
    sys.stdout.write("\t".join([a.label, set_id, sheet_sha, L.sha256_bytes(data)]) + "\n")


if __name__ == "__main__":
    main()
