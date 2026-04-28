"""Shared logging utilities for whywhytools CLI commands."""

from __future__ import annotations

import logging
import sys


def setup_logger(level: str | int = "INFO") -> None:
    """
    Configure the root logger with a StreamHandler.

    Sets the logging level and attaches a StreamHandler if none exist yet.
    Safe to call multiple times; the handler is only added once.

    Args:
        level: Logging level as a string (e.g., "INFO") or integer constant.
    """
    root = logging.getLogger()

    if isinstance(level, str):
        numeric_level = getattr(logging, level.upper(), None)
        if numeric_level is None:
            print(f"Warning: Invalid log level '{level}'. Falling back to 'INFO'.")
            numeric_level = logging.INFO
    else:
        numeric_level = level

    root.setLevel(numeric_level)

    if not root.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt="%(asctime)s - [%(filename)s] %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        root.addHandler(handler)
