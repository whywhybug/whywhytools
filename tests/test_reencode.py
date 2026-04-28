"""Tests for the wwt-reencode CLI (parse_args, validate_args, run)."""

import argparse
from pathlib import Path

import pytest

from whywhytools.cli.reencode import parse_args, run, validate_args


# ---------------------------------------------------------------------------
# parse_args
# ---------------------------------------------------------------------------


def test_parse_args_positional(tmp_path: Path):
    """parse_args correctly maps three positional arguments."""
    target = tmp_path / "sample.txt"
    target.write_text("hello", encoding="utf-8")

    args = parse_args([str(target), "cp950", "utf-8"])

    assert args.file == target
    assert args.from_encoding == "cp950"
    assert args.to_encoding == "utf-8"


def test_parse_args_default_log_level(tmp_path: Path):
    """Default --log-level is INFO."""
    target = tmp_path / "sample.txt"
    target.write_text("hello", encoding="utf-8")

    args = parse_args([str(target), "cp950", "utf-8"])

    assert args.log_level == "INFO"


def test_parse_args_custom_log_level(tmp_path: Path):
    """--log-level overrides the default."""
    target = tmp_path / "sample.txt"
    target.write_text("hello", encoding="utf-8")

    args = parse_args([str(target), "cp950", "utf-8", "--log-level", "DEBUG"])

    assert args.log_level == "DEBUG"


def test_parse_args_missing_positional_exits():
    """Missing required positional arguments causes SystemExit."""
    with pytest.raises(SystemExit):
        parse_args([])


# ---------------------------------------------------------------------------
# validate_args
# ---------------------------------------------------------------------------


def test_validate_args_file_not_found(tmp_path: Path):
    """validate_args raises SystemExit when the file does not exist."""
    parser = argparse.ArgumentParser()
    args = argparse.Namespace(
        file=tmp_path / "nonexistent.txt",
        from_encoding="cp950",
        to_encoding="utf-8",
    )

    with pytest.raises(SystemExit):
        validate_args(parser, args)


def test_validate_args_not_a_file(tmp_path: Path):
    """validate_args raises SystemExit when the path is a directory."""
    parser = argparse.ArgumentParser()
    args = argparse.Namespace(
        file=tmp_path,  # directory, not a file
        from_encoding="cp950",
        to_encoding="utf-8",
    )

    with pytest.raises(SystemExit):
        validate_args(parser, args)


# ---------------------------------------------------------------------------
# run
# ---------------------------------------------------------------------------


def test_run_reencodes_file(tmp_path: Path):
    """run re-encodes the file content in-place."""
    target = tmp_path / "test.txt"
    original_text = "Hello, world!"
    target.write_text(original_text, encoding="utf-8")

    args = argparse.Namespace(
        file=target,
        from_encoding="utf-8",
        to_encoding="utf-8",
    )
    run(args)

    assert target.read_text(encoding="utf-8") == original_text


def test_run_changes_encoding(tmp_path: Path):
    """run converts encoding so the file can be read back with the target encoding."""
    target = tmp_path / "test.txt"
    original_text = "Hello"
    target.write_bytes(original_text.encode("ascii"))

    args = argparse.Namespace(
        file=target,
        from_encoding="ascii",
        to_encoding="utf-8",
    )
    run(args)

    assert target.read_text(encoding="utf-8") == original_text


def test_run_bad_from_encoding_raises(tmp_path: Path):
    """run raises UnicodeDecodeError when from_encoding cannot decode the file."""
    target = tmp_path / "test.txt"
    target.write_bytes(b"\xff\xfe")  # BOM that is not valid utf-8

    args = argparse.Namespace(
        file=target,
        from_encoding="utf-8",
        to_encoding="ascii",
    )

    with pytest.raises(UnicodeDecodeError):
        run(args)
