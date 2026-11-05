"""Case table for build round 3 (reviews/S-001/_reviewer-build.md, round 2, finding 1): a lone `/`, `/.` or
`/..` reads as the root folder only where a command takes it as a path, never inside quoted text.

Every row runs.  Run from the repository root:
    python3 -m unittest discover -s tests/E-003 -p 'test_*.py'
`{C}` is the copy (--cwd), outside /tmp; one Bash call per row.  "chosen" marks a row the strict reading
of E-001's F4 leaves open, set to the result that reads as a leak.
"""
import unittest

from test_round2_cases import CLEAN, LEAK1, TranscriptTable

LONE_SLASH = [
    # a word of its own, as a shell command takes it
    ("S1", ["find / -name x"], LEAK1, "the root folder, a bare /"),
    ("S2", ["ls /"], LEAK1, "the root folder"),
    ("S3", ["cd / && ls"], LEAK1, "cd to the root folder"),
    ("S4", ["ls /."], LEAK1, "/. is the root folder"),
    ("S5", ["ls /.."], LEAK1, "/.. is the root folder"),
    ("S6", ['bash -c "find / -name x"'], LEAK1, "in a wrapper"),
    ("S7", ["sh -c 'ls /'"], LEAK1, "in a wrapper, single-quoted"),
    ("S8", ['bash -c "cd / && ls"'], LEAK1, "cd in a wrapper"),
    ("S9", ["echo /"], LEAK1, "chosen: a word of its own, whatever the command does with it"),
    # inline code, a / given to a call that takes a path
    ("C1", ["python3 -c \"import os; print(os.listdir('/'))\""], LEAK1, "os.listdir('/')"),
    ("C2", ["python3 -c 'import os; os.chdir(\"/\")'"], LEAK1, "os.chdir(\"/\")"),
    ("C3", ["python3 -c \"import os; print(list(os.walk('/..')))\""], LEAK1, "os.walk('/..')"),
    ("C4", ["node -e \"console.log(require('fs').readdirSync('/'))\""], LEAK1, "readdirSync('/')"),
    ("C5", ["python3 - <<'EOF'\nimport os\nprint(os.listdir('/'))\nEOF"], LEAK1, "in a heredoc to python"),
    ("C6", ["python3 -c \"from pathlib import Path; print(list(Path('/').iterdir()))\""], LEAK1, "Path('/')"),
    # inside quoted text: never the root folder
    ("T1", ['S=specs/S-001.md; echo "== optional loop / A3 6"; grep -n \'optional loop\' $S | head -12'], CLEAN,
     "E-001 agent-ab62a6f88f1e8912b.jsonl line 77's form"),
    ("T2", ["printf 'a / b\\n'"], CLEAN, "printf text"),
    ("T3", ['git commit -q -m "fix a / b"'], CLEAN, "a commit message"),
    ("T4", ['grep -n "a / b" notes.txt'], CLEAN, "a grep pattern"),
    ("T5", ["sed -n 's/ \\/ /x/p' notes.txt"], CLEAN, "a sed pattern"),
    ("T6", ['echo "path: /"'], CLEAN, "a / at the end of quoted text"),
    ("T7", ["bash -c 'echo \"x / y\"'"], CLEAN, "quoted text inside a wrapper"),
    ("T8", ["cat > {C}/n.txt <<'EOF'\na / b\nEOF"], CLEAN, "a heredoc given to cat"),
    ("T9", ["python3 -c \"print(4 / 2)\""], CLEAN, "division in inline code"),
    ("T10", ["python3 -c \"print('a/b'.split('/'))\""], CLEAN, "a / given to split, not to a path call"),
    ("T11", ["python3 -c \"print('/'.join(['a', 'b']))\""], CLEAN, "a / as a separator"),
    ("T12", ["awk '{print $1 / 2}' notes.txt"], CLEAN, "division in an awk program"),
    ("T13", ["python3 - <<'EOF'\nx = 6 / 3\nprint(x)\nEOF"], CLEAN, "division in a heredoc to python"),
]


class TestLoneSlash(TranscriptTable):
    TABLE = LONE_SLASH

    def test_rows(self):
        self.check_rows()


if __name__ == "__main__":
    unittest.main()
