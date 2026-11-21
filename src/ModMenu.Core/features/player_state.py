from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Entity:
    id: int
    world_pos: tuple[float, float, float]
    hp: float
    bones: dict[str, tuple[float, float, float]]


class PlayerState:
    def __init__(self, pm, scanner):
        self.pm = pm
        self.scanner = scanner
        self.local_player: Entity | None = None
        self.entities: list[Entity] = []

    def refresh(self) -> None:
        # offsets resolved once at attach time, refreshed per frame
        self.entities = self._read_entity_list()

    def _read_entity_list(self) -> list[Entity]:
        return []

    def nearby_entities(self, radius: float) -> list[Entity]:
        return [e for e in self.entities if self._dist(e) <= radius]

    def closest_in_fov(self, fov_deg: float) -> Entity | None:
        best, best_d = None, fov_deg
        for e in self.entities:
            d = self._screen_angle(e)
            if d < best_d:
                best, best_d = e, d
        return best

    def delta_to(self, e: Entity, bone: str) -> tuple[float, float]:
        return 0.0, 0.0

    def apply_mouse_delta(self, dx: float, dy: float) -> None:
        pass

    def _dist(self, e: Entity) -> float:
        return 0.0

    def _screen_angle(self, e: Entity) -> float:
        return 180.0