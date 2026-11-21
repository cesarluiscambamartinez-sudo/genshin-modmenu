from __future__ import annotations

import sqlite3
from pathlib import Path


class SignatureDb:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self._conn: sqlite3.Connection | None = None

    def open(self) -> None:
        self._conn = sqlite3.connect(self.path)
        self._conn.execute(
            "CREATE TABLE IF NOT EXISTS sigs (name TEXT PRIMARY KEY, pattern TEXT, build TEXT)"
        )

    def get(self, name: str, build: str) -> str | None:
        row = self._conn.execute(
            "SELECT pattern FROM sigs WHERE name=? AND build=?", (name, build)
        ).fetchone()
        return row[0] if row else None

    def put(self, name: str, pattern: str, build: str) -> None:
        self._conn.execute(
            "INSERT OR REPLACE INTO sigs (name, pattern, build) VALUES (?,?,?)",
            (name, pattern, build),
        )
        self._conn.commit()