from __future__ import annotations

import time
from dataclasses import dataclass, field

import psutil
from pymem import Pymem
from pymem.process import module_from_name

from .config import ModMenuConfig
from .memory.pattern_scanner import PatternScanner
from .features import FeatureRegistry


@dataclass
class ProcessLoader:
    cfg: ModMenuConfig
    pid: int | None = None
    build_id: str = "unknown"
    _pm: Pymem | None = field(default=None, repr=False)
    _scanner: PatternScanner | None = field(default=None, repr=False)

    def attach(self, pid: int | None = None) -> bool:
        target = pid or self._find_game_pid()
        if target is None:
            return False
        self._pm = Pymem(target)
        self.pid = target
        mod = module_from_name(self._pm.process_handle, "GenshinImpact.exe")
        if mod is None:
            return False
        self._scanner = PatternScanner(self._pm, mod.lpBaseOfDll, mod.SizeOfImage)
        self.build_id = self._detect_build()
        return True

    def _find_game_pid(self) -> int | None:
        for proc in psutil.process_iter(["name", "pid"]):
            if proc.info["name"] == "GenshinImpact.exe":
                return proc.info["pid"]
        return None

    def _detect_build(self) -> str:
        # build string lives near the module header in most 4.x/5.x builds
        addr = self._scanner.scan_first(self.cfg.patterns["build_string"])
        return self._pm.read_string(addr, 24) if addr else "unknown"

    def run_headless(self) -> None:
        registry = FeatureRegistry(self._pm, self._scanner, self.cfg)
        registry.enable_from_config()
        while True:
            registry.tick()
            time.sleep(self.cfg.tick_interval)