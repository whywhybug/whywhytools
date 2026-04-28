"""
CLI tool: wwt-reencode

Re-encodes a text file from a source encoding (default: cp950) to a target
encoding (default: utf-8) in-place.
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from ..logging_utils import setup_logger

logger = logging.getLogger(__name__)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """
    Parse command-line arguments for wwt-reencode.

    Uses allow_abbrev=False to prevent ambiguous abbreviation matches.
    File path is resolved to a pathlib.Path object immediately.

    Args:
        argv: Argument list for testing; defaults to sys.argv when None.

    Returns:
        Parsed argument namespace.
    """
    parser = argparse.ArgumentParser(
        prog="wwt-reencode",
        description="Re-encode a text file from one encoding to another in-place.",
        allow_abbrev=False,
    )
    parser.add_argument(
        "file",
        type=Path,
        help="Path to the text file to re-encode.",
    )
    parser.add_argument(
        "from_encoding",
        metavar="FROM_ENCODING",
        help="Source encoding of the input file (e.g. cp950, big5).",
    )
    parser.add_argument(
        "to_encoding",
        metavar="TO_ENCODING",
        help="Target encoding to write the file as (e.g. utf-8).",
    )
    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        dest="log_level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level (default: INFO).",
    )

    args = parser.parse_args(argv)
    validate_args(parser, args)
    return args


def validate_args(parser: argparse.ArgumentParser, args: argparse.Namespace) -> None:
    """
    Validate parsed arguments before any file I/O is performed.

    Strictly side-effect-free: only raises errors or exits; creates no resources.

    Args:
        parser: The ArgumentParser instance used to report errors via parser.error().
        args: The parsed argument namespace to validate.
    """
    if not args.file.exists():
        parser.error(f"File '{args.file}' does not exist.")

    if not args.file.is_file():
        parser.error(f"'{args.file}' is not a regular file.")


def run(args: argparse.Namespace) -> None:
    """
    Re-encode the target file in-place.

    Reads the file using the source encoding, then writes the content back
    using the target encoding, overwriting the original file.

    Args:
        args: Validated argument namespace with file, from_encoding, and to_encoding.
    """
    logger.debug("Reading '%s' with encoding '%s'.", args.file, args.from_encoding)
    content = args.file.read_text(encoding=args.from_encoding)

    logger.debug("Writing back with encoding '%s'.", args.to_encoding)
    args.file.write_text(content, encoding=args.to_encoding)

    logger.debug("Done. '%s' re-encoded from %s to %s.", args.file, args.from_encoding, args.to_encoding)


def main(argv: list[str] | None = None) -> None:
    """
    Entry point for the wwt-reencode command.

    Args:
        argv: Argument list for testing; defaults to sys.argv when None.
    """
    args = parse_args(argv)

    try:
        setup_logger(level=args.log_level)
        for key, value in vars(args).items():
            logger.debug("%s: %s", key, value)
        run(args)
    except UnicodeDecodeError as e:
        logger.error("Failed to decode '%s' with encoding '%s': %s", args.file, args.from_encoding, e)
        sys.exit(1)
    except OSError as e:
        logger.error("File I/O error: %s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
