"""This module provides utility functions for managing Pickle files."""

import pickle
import sys
from pathlib import Path
from typing import Any

from ..type_checker import check_type
from ..utils import create_parent_dirs


def load_pickle(file: str | Path) -> Any:
    """
    Load an object from a pickle file.

    Args:
        file (Union[str, Path]): The path to the pickle file.

    Returns:
        Any: The object loaded from the pickle file.
    """
    check_type(file, (str, Path))

    with open(file, "rb") as f:
        obj = pickle.load(f)
    return obj


def save_pickle(
    obj,
    file: str | Path,
    force: bool = False,
    silent: bool = False,
    raise_on_exists: bool = False,
) -> None:
    """
    Save an object to a pickle file.

    Args:
        obj (Any): The object to save.
        file (Union[str, Path]): The path to the output pickle file.
        force (bool, optional): If True, overwrite the file if it exists. Defaults to False.
        silent (bool, optional): If True, suppress print messages. Defaults to False.
        raise_on_exists (bool, optional): If True, raise FileExistsError with full
            traceback instead of exiting cleanly. Defaults to False.

    Raises:
        TypeError: If file is not the expected type.
        FileExistsError: If the file exists, force is False, and raise_on_exists is True.
    """
    check_type(file, (str, Path))
    if Path(file).exists() and not force:
        msg = f"[ERROR] {file} already exists."
        if raise_on_exists:
            raise FileExistsError(msg)
        sys.exit(msg)  # exit 1
    create_parent_dirs(file)

    with open(file, "wb") as f:
        pickle.dump(obj, f)

    if not silent:
        print(f"[INFO] save to {file}")
