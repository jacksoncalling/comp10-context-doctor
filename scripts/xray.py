#!/usr/bin/env python3
"""Topological X-Ray: a descriptive census of a folder-based AI workspace.

This is an image, not a diagnosis. It contains counts, dates, structure and
gaps. It deliberately contains no severity flags, no "wrong" labels and no
recommendations. Interpretation belongs to the consult (rules.md step 2).

Usage:
    python xray.py <workspace-path> [--stale-days N]
"""

import argparse
import os
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "__MACOSX"}
ENTRY_NAMES = {"readme.md", "claude.md", "gemini.md", "identity.md", "index.md"}
STATE_HINTS = ("status", "state", "pipeline", "log", "lead", "board", "current")


def git_dates(ws: Path) -> dict:
    """Map of relative path -> last commit date (ISO), via one git log pass."""
    try:
        out = subprocess.run(
            ["git", "-C", str(ws), "log", "--format=%%%as", "--name-only"],
            capture_output=True, text=True, timeout=60,
        )
        if out.returncode != 0:
            return {}
    except (OSError, subprocess.TimeoutExpired):
        return {}
    dates, current = {}, None
    for line in out.stdout.splitlines():
        if line.startswith("%"):
            current = line[1:].strip()
        elif line.strip() and current:
            dates.setdefault(line.strip().replace("/", os.sep), current)
    return dates


def main() -> int:
    # Windows consoles default to cp1252; a workspace may hold non-latin1 file
    # names or paths. Encode output as UTF-8 so the census never dies in print().
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("workspace")
    ap.add_argument("--stale-days", type=int, default=45)
    args = ap.parse_args()

    ws = Path(args.workspace).resolve()
    if not ws.is_dir():
        print(f"not a directory: {ws}", file=sys.stderr)
        return 2

    gdates = git_dates(ws)
    instrument = "git last-commit dates" if gdates else "filesystem mtimes (weaker instrument: no git history found)"
    horizon = datetime.now() - timedelta(days=args.stale_days)

    files, empty_dirs = [], []
    for root, dirs, names in os.walk(ws):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        rel_root = Path(root).relative_to(ws)
        if not names and not dirs:
            empty_dirs.append(str(rel_root))
        for n in names:
            rel = str(rel_root / n) if str(rel_root) != "." else n
            iso = gdates.get(rel)
            if iso:
                touched = datetime.strptime(iso, "%Y-%m-%d")
            else:
                touched = datetime.fromtimestamp((Path(root) / n).stat().st_mtime)
            files.append((rel, n.lower(), touched))

    entries = [f for f, low, _ in files if low in ENTRY_NAMES and os.sep not in f]
    identities = [f for f, low, _ in files if low == "identity.md"]
    agents = [f for f, low, _ in files if f.replace(os.sep, "/").startswith(".claude/agents/")]
    claude_mds = [f for f, low, _ in files if low == "claude.md"]
    state_organs = [(f, t) for f, low, t in files
                    if low.endswith(".md") and any(h in low for h in STATE_HINTS)]
    stale = sorted([(f, t) for f, _, t in files if t < horizon], key=lambda x: x[1])
    dupes = defaultdict(list)
    for f, low, _ in files:
        if low.endswith(".md"):
            dupes[low].append(f)
    dupes = {k: v for k, v in dupes.items() if len(v) > 1}

    d = lambda t: t.strftime("%Y-%m-%d")
    print("TOPOLOGICAL X-RAY (descriptive imaging; contains no judgments)")
    print(f"workspace: {ws}")
    print(f"taken: {d(datetime.now())} | timeline instrument: {instrument}")
    print(f"files: {len(files)} | staleness horizon: {args.stale_days} days\n")

    print(f"[entry point candidates at root] {len(entries)}")
    for f in entries:
        print(f"  {f}")
    print(f"\n[identity census] identity.md files: {len(identities)} | "
          f"agent definitions: {len(agents)} | CLAUDE.md files: {len(claude_mds)}")
    for f in identities + agents + claude_mds:
        print(f"  {f}")
    print(f"\n[state organs] filenames hinting at changing facts: {len(state_organs)}")
    for f, t in sorted(state_organs, key=lambda x: x[1]):
        print(f"  {d(t)}  {f}")
    print(f"\n[dead tissue] empty directories: {len(empty_dirs)}")
    for p in empty_dirs:
        print(f"  {p}")
    print(f"\n[untouched beyond horizon] {len(stale)} files; oldest 15:")
    for f, t in stale[:15]:
        print(f"  {d(t)}  {f}")
    print(f"\n[duplicate filenames] markdown names appearing in more than one place: {len(dupes)}")
    for name, paths in sorted(dupes.items()):
        print(f"  {name} x{len(paths)}")
        for p in paths:
            print(f"    {p}")
    print("\nend of image. Interpretation happens in the consult, not here.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
