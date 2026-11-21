from __future__ import annotations

import platform
import sys


def collect_diagnostics() -> str:
    lines = [
        "genshin-modmenu diagnostics",
        f"python: {sys.version.split()[0]}",
        f"platform: {platform.platform()}",
        f"arch: {platform.machine()}",
    ]
    try:
        import pywin32  # noqa: F401
        lines.append("pywin32: ok")
    except Exception:
        lines.append("pywin32: missing")
    try:
        import pymem
        lines.append(f"pymem: {pymem.__version__}")
    except Exception:
        lines.append("pymem: missing")
    return "\n".join(lines)