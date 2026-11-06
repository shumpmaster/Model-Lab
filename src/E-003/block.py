"""The sheet lead's block parser (spec S-001, J4).

    python3 -I src/E-003/block.py parse < BLOCK

Reads the block on standard input.  It accepts exactly the three forms J4 gives, each line in its form
and order, and nothing else:
  full     set, repository-commit, path, fingerprint, tests, pack: match, scan: clean|unread, model,
           runs: 1, tokens, k1-canary: unseen, k2, k3, k4, k5
  stopped  set, pack: match|differs, stopped: k1|k2|k3|k4|pack, runs: 0|1, tokens, k1-canary, k2 .. k5
  void     set, scan: void, hit, runs: 1, tokens, k1-canary, k2 .. k5
Counts are decimal integers, the commit 40 lowercase hex digits, the fingerprint 64, the set id
S-001-<built|plans|research>-<n>, the served model 1 to 64 characters from letters, digits, `.`, `_`
and `-`, each k result pass|fail|untested and k1-canary unseen|seen|unread (unseen in the full form).
Accepted: exit 0 and {"form": ..., "fields": {...}}.  Refused: exit 1, the first line naming the line.
The refusal never repeats a refused line's text, so no sheet text can leave through it.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import e003lib as L  # noqa: E402


def main(argv=None):
    ap = argparse.ArgumentParser(prog="block.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("parse", help="parse a sheet lead's block from standard input")
    ap.parse_args(argv)
    data = sys.stdin.buffer.read()
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        L.refuse("refused: the block is not UTF-8")
    result, err = L.parse_sheet_block(text)
    if err:
        L.refuse("refused: " + err)
    L.emit(result)


if __name__ == "__main__":
    main()
