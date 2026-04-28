"""This module provides utility functions for managing text files."""

import sys
from pathlib import Path

from ..type_checker import check_list_type, check_type
from ..utils import create_parent_dirs


def read_file(file: str | Path, lines: bool = False) -> str | list[str]:
    """
    Read a text file and return its content.

    Args:
        file (Union[str, Path]): The path to the text file.
        lines (bool, optional): If True, return a list of strings, one for each line.
            Defaults to False.

    Returns:
        Union[str, list[str]]: The content of the file as a single string or a list of strings.
    """
    check_type(file, (str, Path))

    with open(file, mode="r", encoding="utf-8") as reader:
        content = reader.read()
        if lines:
            content = content.splitlines()

    return content


def write_file(
    lines: str | list[str],
    file: str | Path,
    force: bool = False,
    silent: bool = False,
    raise_on_exists: bool = False,
) -> None:
    """
    Write a string or a list of strings to a text file.

    Args:
        lines (Union[str, list[str]]): A single string or a list of strings to write.
        file (Union[str, Path]): The path to the output text file.
        force (bool, optional): If True, overwrite the file if it exists. Defaults to False.
        silent (bool, optional): If True, suppress print messages. Defaults to False.
        raise_on_exists (bool, optional): If True, raise FileExistsError with full
            traceback instead of exiting cleanly. Defaults to False.

    Raises:
        FileExistsError: If the file exists, force is False, and raise_on_exists is True.
    """
    check_type(file, (str, Path))
    if Path(file).exists() and not force:
        msg = f"[ERROR] {file} already exists."
        if raise_on_exists:
            raise FileExistsError(msg)
        sys.exit(msg)  # exit 1
    create_parent_dirs(file)

    if isinstance(lines, str):
        lines = [lines]
    check_list_type(lines, str)

    with open(file, mode="w", encoding="utf-8", newline="\n") as fp:
        for line in lines:
            print(line, file=fp)

    if not silent:
        print(f"[INFO] save to {file}")


def append_file(lines: str | list[str], file: str | Path) -> None:
    """
    Append a string or a list of strings to an existing text file.

    Args:
        lines (Union[str, list[str]]): A single string or a list of strings to append.
        file (Union[str, Path]): The path to the text file.
    """
    check_type(file, (str, Path))
    create_parent_dirs(file)

    if isinstance(lines, str):
        lines = [lines]
    check_list_type(lines, str)

    with open(file, mode="a", encoding="utf-8", newline="\n") as fp:
        for line in lines:
            print(line, file=fp)
