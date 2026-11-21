from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class PatternScanner:
    pm: object
    base: int
    size: int

    def _compile(self, sig: str) -> re.Pattern[bytes]:
        tokens = sig.strip().split()
        parts = [b"." if t in ("??", "?") else re.escape(bytes([int(t, 16)])) for t in tokens]
        return re.compile(b"".join(parts), re.DOTALL)

    def scan_first(self, sig: str) -> int | None:
        needle = self._compile(sig)
        chunk = self.pm.read_bytes(self.base, self.size)
        m = needle.search(chunk)
        return self.base + m.start() if m else None

    def scan_all(self, sig: str, limit: int = 32) -> list[int]:
        needle = self._compile(sig)
        chunk = self.pm.read_bytes(self.base, self.size)
        return [self.base + m.start() for m in needle.finditer(chunk)][:limit]