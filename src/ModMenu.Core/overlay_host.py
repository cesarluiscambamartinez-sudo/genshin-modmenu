from __future__ import annotations

import subprocess
import sys
from pathlib import Path


class OverlayHost:
    """Spawns the C# DX11 overlay and pipes feature state to it."""

    def __init__(self, loader, cfg):
        self.loader = loader
        self.cfg = cfg
        self.bin = Path(__file__).resolve().parents[2] / "src" / "ModMenu.Overlay.Host" / "bin" / "Release" / "net8.0-windows" / "ModMenu.Overlay.Host.exe"

    def run(self) -> int:
        if not self.bin.exists():
            print(f"[!] overlay host not built: {self.bin}", file=sys.stderr)
            print("    run scripts/build_overlay.ps1 first", file=sys.stderr)
            return 3
        proc = subprocess.Popen([str(self.bin), "--pid", str(self.loader.pid)])
        try:
            return proc.wait()
        except KeyboardInterrupt:
            proc.terminate()
            return 0