"""genshin-modmenu entry point.

Boots the loader, resolves the game process, then hands control to the
overlay host which renders the ImGui-style menu via the C# DX11 bridge.
"""
from __future__ import annotations

import argparse
import sys

from modmenu_core.loader import ProcessLoader
from modmenu_core.config import load_config
from modmenu_core.overlay_host import OverlayHost
from modmenu_core.diagnostics import collect_diagnostics


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="genshin-modmenu")
    p.add_argument("--config", default="config/default.yaml")
    p.add_argument("--diagnostics", action="store_true")
    p.add_argument("--no-overlay", action="store_true")
    p.add_argument("--attach", metavar="PID", type=int, default=None)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.diagnostics:
        print(collect_diagnostics())
        return 0

    cfg = load_config(args.config)
    loader = ProcessLoader(cfg)
    if not loader.attach(args.attach):
        print("[!] could not find GenshinImpact.exe — is the game running?", file=sys.stderr)
        return 2

    print(f"[+] attached to pid={loader.pid} build={loader.build_id}")
    if args.no_overlay:
        loader.run_headless()
        return 0

    host = OverlayHost(loader, cfg)
    return host.run()


if __name__ == "__main__":
    raise SystemExit(main())