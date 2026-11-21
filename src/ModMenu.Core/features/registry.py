from __future__ import annotations

from .esp import EspOverlay
from .aimbot import AimAssist
from .player_state import PlayerState


class FeatureRegistry:
    """Holds active feature modules and ticks them each overlay frame."""

    def __init__(self, pm, scanner, cfg):
        self.cfg = cfg
        self.player = PlayerState(pm, scanner)
        self.features = {
            "esp": EspOverlay(pm, scanner, self.player, cfg),
            "aimbot": AimAssist(pm, scanner, self.player, cfg),
        }

    def enable_from_config(self) -> None:
        for name, enabled in self.cfg.features.items():
            if name in self.features and enabled:
                self.features[name].enable()

    def tick(self) -> None:
        self.player.refresh()
        for feature in self.features.values():
            if feature.enabled:
                feature.update()

    def handle_menu_toggle(self) -> None:
        for feature in self.features.values():
            feature.toggle()