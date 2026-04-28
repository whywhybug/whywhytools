"""This module provides utility functions for managing PyTorch files."""

import sys
from pathlib import Path
from typing import Any

from ..type_checker import check_type
from ..utils import create_parent_dirs


def load_pt(file: str | Path, map_location: Any = None, weights_only: bool = False, **kwargs: Any) -> Any:
    """
    Read a PyTorch file and return the loaded object.

    Args:
        file (Union[str, Path]): The path to the PyTorch file.
        map_location (Any, optional): A function, torch.device, string or a dict specifying how to remap storage locations.
        weights_only (bool, optional): If True, only weights will be loaded. Defaults to False.
        **kwargs: Additional keyword arguments to pass to torch.load.

    Returns:
        Any: The object read from the PyTorch file.
    """
    check_type(file, (str, Path))
    import torch

    return torch.load(file, map_location=map_location, weights_only=weights_only, **kwargs)


def save_pt(
    obj: Any,
    file: str | Path,
    force: bool = False,
    silent: bool = False,
    raise_on_exists: bool = False,
    **kwargs: Any,
) -> None:
    """
    Write an object to a PyTorch file.

    Args:
        obj (Any): The object to write to the file.
        file (Union[str, Path]): The path to the output PyTorch file.
        force (bool, optional): If True, overwrite the file if it exists. Defaults to False.
        silent (bool, optional): If True, suppress print messages. Defaults to False.
        raise_on_exists (bool, optional): If True, raise FileExistsError with full
            traceback instead of exiting cleanly. Defaults to False.
        **kwargs: Additional keyword arguments to pass to torch.save.

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

    import torch

    torch.save(obj, file, **kwargs)

    if not silent:
        print(f"[INFO] save to {file}")
