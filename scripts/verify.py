#!/usr/bin/env python3
"""Quote verifier: mechanically checks every evidence span in a diagnosis.

Every proximate cause in a diagnosis must be formatted:

    EVIDENCE: <path relative to workspace root> :: "<exact span from the file>"

This script string-matches each span against the named file. A fabricated or
paraphrased quote fails no matter how convincing it reads. See
reference/evidence-standards.md rule 1.

Usage:
    python verify.py <diagnosis.md> <workspace-path>

Exit codes: 0 all spans verified, 1 failures found, 2 usage/input error.
"""

import re
import sys
from pathlib import Path

PATTERN = re.compile(r'EVIDENCE:\s*(?P<path>[^:]+?)\s*::\s*"(?P<span>.+?)"', re.DOTALL)


def main() -> int:
    # Windows consoles default to cp1252; evidence spans routinely hold umlauts,
    # middle dots, or emoji. Encode output as UTF-8 so a match never dies in print().
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    diagnosis, ws = Path(sys.argv[1]), Path(sys.argv[2])
    if not diagnosis.is_file():
        print(f"diagnosis file not found: {diagnosis}", file=sys.stderr)
        return 2
    if not ws.is_dir():
        print(f"workspace not found: {ws}", file=sys.stderr)
        return 2

    claims = list(PATTERN.finditer(diagnosis.read_text(encoding="utf-8", errors="replace")))
    if not claims:
        print("no EVIDENCE: lines found. A diagnosis without evidence spans "
              "cannot be verified; hypothesis-grade verdicts should say so themselves.")
        return 1

    failures = 0
    for i, m in enumerate(claims, 1):
        rel, span = m.group("path").strip(), m.group("span")
        target = ws / rel
        if not target.is_file():
            print(f"[{i}] FAIL  file not found: {rel}")
            failures += 1
            continue
        text = target.read_text(encoding="utf-8", errors="replace")
        if span in text:
            print(f'[{i}] PASS  {rel} :: "{span[:60]}{"..." if len(span) > 60 else ""}"')
        else:
            print(f'[{i}] FAIL  span not present verbatim in {rel}: "{span[:80]}"')
            failures += 1

    print(f"\n{len(claims)} evidence spans checked, {failures} failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
