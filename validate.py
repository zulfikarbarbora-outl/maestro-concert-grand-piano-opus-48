#!/usr/bin/env python3
"""Validate audio data collection integrity."""
import json
import sys
from pathlib import Path


def validate(collection_dir: str = ".") -> int:
    """Validate the audio collection: check index.json + audio files exist."""
    base = Path(collection_dir)
    index_path = base / "index.json"

    if not index_path.exists():
        print("ERROR: index.json not found", file=sys.stderr)
        return 1

    with open(index_path) as f:
        index = json.load(f)

    files = index.get("files", [])
    print(f"Index: {len(files)} entries")

    missing = 0
    for entry in files:
        filename = entry.get("filename", "")
        if not filename:
            continue
        audio_path = base / filename
        if not audio_path.exists():
            missing += 1

    if missing:
        print(f"WARNING: {missing}/{len(files)} files missing")
        return 1

    print(f"OK: all {len(files)} files present")
    return 0


if __name__ == "__main__":
    sys.exit(validate(sys.argv[1] if len(sys.argv) > 1 else "."))
