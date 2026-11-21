from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import yaml


@dataclass
class ModMenuConfig:
    tick_interval: float = 0.016
    overlay: dict = field(default_factory=dict)
    patterns: dict = field(default_factory=dict)
    features: dict = field(default_factory=dict)
    keybind: dict = field(default_factory=lambda: {"menu": "INSERT"})


def load_config(path: str | Path) -> ModMenuConfig:
    p = Path(path)
    if not p.exists():
        return ModMenuConfig()
    raw = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    return ModMenuConfig(
        tick_interval=float(raw.get("tick_interval", 0.016)),
        overlay=raw.get("overlay", {}),
        patterns=raw.get("patterns", {}),
        features=raw.get("features", {}),
        keybind=raw.get("keybind", {"menu": "INSERT"}),
    )