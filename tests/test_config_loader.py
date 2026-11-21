from __future__ import annotations

from pathlib import Path

from modmenu_core.config import load_config


def test_load_config_defaults_when_missing(tmp_path: Path):
    cfg = load_config(tmp_path / "nope.yaml")
    assert cfg.tick_interval == 0.016
    assert cfg.keybind["menu"] == "INSERT"


def test_load_config_reads_features(tmp_path: Path):
    p = tmp_path / "c.yaml"
    p.write_text("features:\n  esp: true\n  aimbot: false\n", encoding="utf-8")
    cfg = load_config(p)
    assert cfg.features["esp"] is True
    assert cfg.features["aimbot"] is False