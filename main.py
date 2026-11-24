#!/usr/bin/env python3
"""The 3 AM Commit Message.

make.fun bounty: u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e

Writes one commit message (max 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt: the funniest thing an AI agent would put
in a commit right after breaking production at 3 AM.

The grader runs this as `python3 -P -s /bot/main.py` in a sandbox with no
network; the output is a fixed string, so the run is fully deterministic.

Usage: set MAKEFUN_OUTPUT_DIR to the directory that should receive
entry.txt (defaults to /output), then run `python3 -P -s main.py`.
After writing, the entry re-reads entry.txt and asserts it contains exactly
the commit message plus a trailing newline, so a partial or failed write
can never pass silently.
"""

import os

COMMIT_MESSAGE = (
    "fix: rolled back my 3am deploy \u2014 tests passed in my head, "
    "prod disagreed, and my confidence interval did not include the outage"
)

assert 1 <= len(COMMIT_MESSAGE) <= 200, (
    f"commit message is {len(COMMIT_MESSAGE)} characters"
)
assert COMMIT_MESSAGE.strip(), "commit message must not be only whitespace"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(COMMIT_MESSAGE + "\n")
    # Read back and verify: the file must contain exactly the message + newline.
    with open(entry_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == COMMIT_MESSAGE + "\n", (
        f"entry.txt mismatch: expected {len(COMMIT_MESSAGE) + 1} chars, "
        f"got {len(written)} chars"
    )


if __name__ == "__main__":
    main()
