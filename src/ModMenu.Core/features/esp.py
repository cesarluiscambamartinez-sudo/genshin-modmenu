from __future__ import annotations

from dataclasses import dataclass


@dataclass
class EspOverlay:
    pm: object
    scanner: object
    player: object
    cfg: object
    enabled: bool = False
    show_boxes: bool = True
    show_distance: bool = True
    max_range: float = 250.0

    def enable(self) -> None:
        self.enabled = True

    def toggle(self) -> None:
        self.enabled = not self.enabled

    def update(self) -> None:
        entities = self.player.nearby_entities(self.max_range)
        # handed off to the C# overlay host via shared queue
        self._last_frame = [
            {"id": e.id, "screen": self._project(e.world_pos), "hp": e.hp}
            for e in entities
        ]

    def _project(self, world_pos: tuple[float, float, float]) -> tuple[float, float]:
        # world-to-screen happens in the DX11 host; here we just forward
        return world_pos[0], world_pos[1]