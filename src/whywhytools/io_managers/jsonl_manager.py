"""This module provides utility functions for managing JSONL (JSON Lines) files."""

import json
import sys
from pathlib import Path

from ..type_checker import check_list_type, check_type
from ..utils import create_parent_dirs


def read_jsonl(file: str | Path) -> list[dict]:
    """
    Read a JSONL file and return a list of dictionaries.

    Args:
        file (Union[str, Path]): The path to the JSONL file.

    Returns:
        list[dict]: A list containing the JSON objects read from the file.
    """
    check_type(file, (str, Path))

    df = []
    with open(file, mode="r", encoding="utf-8") as reader:
        line = reader.readline()
        while line:
            obj = json.loads(line)
            df.append(obj)
            line = reader.readline()
    return df


def write_jsonl(
    obj_list: dict | list[dict],
    file: str | Path,
    force: bool = False,
    silent: bool = False,
    raise_on_exists: bool = False,
) -> None:
    """
    Write a list of dictionaries to a JSONL file.

    Args:
        obj_list (Union[dict, list[dict]]): A single dictionary or a list of dictionaries to write.
        file (Union[str, Path]): The path to the output JSONL file.
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

    if isinstance(obj_list, dict):
        obj_list = [obj_list]
    check_list_type(obj_list, dict)

    with open(file, mode="w", encoding="utf-8", newline="\n") as fp:
        for obj in obj_list:
            json.dump(obj, fp, ensure_ascii=False)
            print(file=fp)

    if not silent:
        print(f"[INFO] save to {file}")


def append_jsonl(obj_list: dict | list[dict], file: str | Path) -> None:
    """
    Append a list of dictionaries to an existing JSONL file.

    Args:
        obj_list (Union[dict, list[dict]]): A single dictionary or a list of dictionaries to append.
        file (Union[str, Path]): The path to the JSONL file.
    """
    check_type(file, (str, Path))
    create_parent_dirs(file)

    if isinstance(obj_list, dict):
        obj_list = [obj_list]
    check_list_type(obj_list, dict)

    with open(file, mode="a", encoding="utf-8", newline="\n") as fp:
        for obj in obj_list:
            json.dump(obj, fp, ensure_ascii=False)
            print(file=fp)
