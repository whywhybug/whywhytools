"""This module provides common file system utilities."""

from pathlib import Path


def create_parent_dirs(file: str | Path) -> None:
    """Ensure the parent directories of a file exist."""
    # dir_path = os.path.dirname(file)
    # if dir_path != "":
    #     os.makedirs(dir_path, exist_ok=True)
    Path(file).parent.mkdir(parents=True, exist_ok=True)
