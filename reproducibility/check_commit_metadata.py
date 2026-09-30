"""Reject tool identities and promotional signatures in Git metadata, not AI disclosures."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TOOLS = re.compile(r"\b(?:claude|anthropic|chatgpt|openai|codex|copilot)\b", re.I)
TRAILER = re.compile(r"^(?:co-authored-by|signed-off-by|generated(?:-by| with| by)|assisted(?:-by| by))\s*:?", re.I)

def problems(author: str, committer: str, message: str) -> list[str]:
    errors = []
    for field, value in [('author', author), ('committer', committer)]:
        if TOOLS.search(value):
            errors.append(f'{field}: tool identity')
    for line in message.splitlines():
        if TRAILER.search(line.strip()) and TOOLS.search(line):
            errors.append('message: tool attribution or promotional signature')
    return errors

def git(*args: str) -> str:
    return subprocess.check_output(['git', *args], cwd=ROOT, encoding='utf-8').strip()

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--message-file', type=Path, help='Validate a proposed commit before creation')
    args = parser.parse_args()
    if args.message_file:
        records = [('proposed', git('var', 'GIT_AUTHOR_IDENT'), git('var', 'GIT_COMMITTER_IDENT'), args.message_file.read_text(encoding='utf-8'))]
    else:
        records = []
        for sha in git('rev-list', '--all').splitlines():
            author, committer, message = git('show', '-s', '--format=%an <%ae>%x00%cn <%ce>%x00%B', sha).split('\0', 2)
            records.append((sha, author, committer, message))
    errors = [(sha, err) for sha, a, c, m in records for err in problems(a, c, m)]
    for sha, err in errors:
        print(f'FAIL {sha}: {err}')
    if errors:
        print('Use human commit identities. Preserve scientific authorship and AI disclosure in the manuscript.')
        return 1
    print(f'PASS human Git metadata: {len(records)} commit(s) checked')
    return 0

if __name__ == '__main__':
    sys.exit(main())
