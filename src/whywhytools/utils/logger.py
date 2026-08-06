"""Shared logging utilities for whywhytools CLI commands."""

from __future__ import annotations

import logging
import sys


def setup_logger(
    logger_instance: logging.Logger | None = None, level: str | int = "INFO"
) -> logging.Logger:
    """Configure and return the application logger.

    Args:
        logger_instance: The logger instance to configure. If None, the root logger is used.
        level: Logging level as a string (e.g., "INFO") or integer constant.

    Returns:
        A configured instance of `logging.Logger`.
    """
    if logger_instance is None:
        logger_instance = logging.getLogger()  # no argument → root logger

    if isinstance(level, str):
        numeric_level = getattr(logging, level.upper(), None)
        if numeric_level is None:
            print(f"Warning: Invalid log level '{level}'. Falling back to 'INFO'.")
            numeric_level = logging.INFO
    else:
        numeric_level = level

    logger_instance.setLevel(numeric_level)

    if not logger_instance.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt="%(asctime)s - [%(filename)s] %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger_instance.addHandler(handler)
        # Disable propagation to prevent duplicate output when both the logger
        # and root logger have handlers. No-op for root logger (no parent).
        logger_instance.propagate = False

    return logger_instance
