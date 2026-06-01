"""This module provides common file system utilities."""

from __future__ import annotations

from pathlib import Path


def create_parent_dirs(file: str | Path) -> None:
    """Ensure the parent directories of a file exist."""
    Path(file).parent.mkdir(parents=True, exist_ok=True)
