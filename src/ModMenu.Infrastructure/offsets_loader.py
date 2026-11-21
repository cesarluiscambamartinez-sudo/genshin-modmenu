from __future__ import annotations

import json
from pathlib import Path


OFFSETS_DIR = Path(__file__).resolve().parents[2] / "data" / "offsets"


def load_offsets(build_id: str) -> dict[str, int]:
    """Load per-build offsets from data/offsets/<build>.json."""
    path = OFFSETS_DIR / f"{build_id}.json"
    if not path.exists():
        path = OFFSETS_DIR / "fallback.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))