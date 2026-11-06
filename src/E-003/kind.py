"""Whether a kind's comparison may open (spec S-001, AC4 and J4; E-003 Step 1).

  python3 -I src/E-003/kind.py can-open --kind plans|built|research --holdouts FILE --sheet-record FILE

--holdouts is governance/HOLDOUTS.md; --sheet-record is the sheet lead's block as the Orchestrator
recorded it (reviews/E-003/<kind>/sheet.md).  The kind opens only when:
  - the block is exactly the full form of J4 (block.py's parser), so a stopped or void sheet, or a block
    with any other line, does not open it;
  - its set id is the kind's, S-001-<kind>-<n>;
  - governance/HOLDOUTS.md's holdouts block holds the line `<set id>  <fingerprint>` (two spaces, 64
    lowercase hex digits) with the block's fingerprint.
A sheet placed with `scan: unread` (K4 failed and the owner ruled to go on) opens it, with that limit
named.  What a file cannot show (which repositories each session held, who wrote the sheet) is shown by
the first-use checks K1 to K7 in the kind's record, not here.  Prints {"eligible", "reason"}.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import e003lib as L  # noqa: E402

HOLD_LINE = re.compile(r"(S-001-(?:built|plans|research)-[1-9][0-9]*)  ([0-9a-f]{64})")


def holdout_sets(text):
    m = re.search(r"^```holdouts[ \t]*\n(.*?)^```", text, re.S | re.M)
    out = {}
    if not m:
        return out
    for line in m.group(1).split("\n"):
        h = HOLD_LINE.fullmatch(line)
        if h:
            out.setdefault(h.group(1), set()).add(h.group(2))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(prog="kind.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("can-open")
    c.add_argument("--kind", required=True, choices=L.KINDS)
    c.add_argument("--holdouts", required=True)
    c.add_argument("--sheet-record", required=True)
    a = ap.parse_args(argv)
    if not os.path.isfile(a.sheet_record):
        L.emit({"eligible": False, "reason": "no sheet record for the kind: no held-back check, the kind does not open"})
    block, err = L.parse_sheet_block(L.read_text(a.sheet_record))
    if err:
        L.emit({"eligible": False, "reason": "the sheet record is not a block of J4's forms (%s): not recorded" % err})
    if block["form"] != "full":
        L.emit({"eligible": False, "reason": "the sheet lead's block is the %s form: no held-back check is placed"
                % block["form"]})
    f = block["fields"]
    set_id = f["set"]
    if not set_id.startswith("S-001-%s-" % a.kind):
        L.emit({"eligible": False, "reason": "the sheet's set %s is not this kind's" % set_id})
    sets = holdout_sets(L.read_text(a.holdouts))
    if set_id not in sets:
        L.emit({"eligible": False, "reason": "governance/HOLDOUTS.md holds no line for the held-back set %s" % set_id})
    if f["fingerprint"] not in sets[set_id] or len(sets[set_id]) != 1:
        L.emit({"eligible": False, "reason": "the fingerprint recorded for %s is not the sheet lead's" % set_id})
    note = "" if f["scan"] == "clean" else "placed with scan: unread (K4 failed and the owner ruled to go on); " \
                                           "the record states that limit"
    L.emit({"eligible": True, "reason": note, "set": set_id, "fingerprint": f["fingerprint"]})


if __name__ == "__main__":
    main()
