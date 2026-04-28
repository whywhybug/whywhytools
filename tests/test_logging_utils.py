"""Tests for the setup_logger utility in logging_utils."""

import logging
import sys

import pytest

from whywhytools.logging_utils import setup_logger


@pytest.fixture(autouse=True)
def reset_root_logger():
    """Reset the root logger state between tests to prevent handler accumulation."""
    root = logging.getLogger()
    original_handlers = root.handlers[:]
    original_level = root.level
    yield
    root.handlers = original_handlers
    root.setLevel(original_level)


def test_setup_logger_default_level():
    """setup_logger with string 'INFO' sets root logger level to INFO."""
    root = logging.getLogger()
    root.handlers.clear()

    setup_logger(level="INFO")

    assert root.level == logging.INFO
    assert len(root.handlers) == 1
    assert isinstance(root.handlers[0], logging.StreamHandler)


def test_setup_logger_integer_level():
    """setup_logger accepts integer log level constants."""
    root = logging.getLogger()
    root.handlers.clear()

    setup_logger(level=logging.DEBUG)

    assert root.level == logging.DEBUG


def test_setup_logger_string_case_insensitive():
    """setup_logger normalises string level to uppercase."""
    root = logging.getLogger()
    root.handlers.clear()

    setup_logger(level="debug")

    assert root.level == logging.DEBUG


def test_setup_logger_invalid_level_falls_back_to_info(capsys):
    """setup_logger falls back to INFO and prints a warning for invalid level strings."""
    root = logging.getLogger()
    root.handlers.clear()

    setup_logger(level="INVALID_LEVEL")

    assert root.level == logging.INFO
    captured = capsys.readouterr()
    assert "Warning" in captured.out
    assert "INVALID_LEVEL" in captured.out


def test_setup_logger_handler_added_only_once():
    """Calling setup_logger multiple times does not add duplicate handlers."""
    root = logging.getLogger()
    root.handlers.clear()

    setup_logger(level="INFO")
    setup_logger(level="INFO")

    assert len(root.handlers) == 1


def test_setup_logger_stdout_handler():
    """The attached StreamHandler writes to sys.stdout."""
    root = logging.getLogger()
    root.handlers.clear()

    setup_logger(level="INFO")

    handler = root.handlers[0]
    assert handler.stream is sys.stdout
