from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AimAssist:
    pm: object
    scanner: object
    player: object
    cfg: object
    enabled: bool = False
    smoothness: float = 0.35
    fov: float = 120.0
    bone: str = "head"

    def enable(self) -> None:
        self.enabled = True

    def toggle(self) -> None:
        self.enabled = not self.enabled

    def update(self) -> None:
        target = self.player.closest_in_fov(self.fov)
        if target is None:
            return
        dx, dy = self.player.delta_to(target, self.bone)
        self.player.apply_mouse_delta(dx * self.smoothness, dy * self.smoothness)