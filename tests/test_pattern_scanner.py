from __future__ import annotations

from unittest.mock import MagicMock

from modmenu_core.memory.pattern_scanner import PatternScanner


def test_scan_first_finds_pattern():
    pm = MagicMock()
    pm.read_bytes.return_value = b"\x00\x01\xAA\xBB\xCC\xDD\x02\x03"
    scanner = PatternScanner(pm, base=0x1000, size=8)
    assert scanner.scan_first("AA BB CC DD") == 0x1002


def test_scan_first_returns_none_when_missing():
    pm = MagicMock()
    pm.read_bytes.return_value = b"\x00" * 16
    scanner = PatternScanner(pm, base=0x1000, size=16)
    assert scanner.scan_first("DE AD BE EF") is None