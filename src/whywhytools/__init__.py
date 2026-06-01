"""The whywhytools package provides a collection of utility functions for file I/O.

This module exposes functions for reading and writing various file formats including
JSON, JSONL, Pickle, Text, PyTorch tensors, and Safetensors, along with common file system utilities.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from .io_managers import (
    append_file,
    append_jsonl,
    load_pickle,
    load_pt,
    load_safetensors,
    read_file,
    read_json,
    read_jsonl,
    save_pickle,
    save_pt,
    save_safetensors,
    write_file,
    write_json,
    write_jsonl,
)
from .utils import create_parent_dirs, setup_logger

try:
    __version__ = version("whywhytools")
except PackageNotFoundError:
    # Package is not installed (e.g., running directly from source without installation)
    __version__ = "unknown"

__all__ = [
    "__version__",
    "create_parent_dirs",
    "setup_logger",
    "read_json", "write_json",
    "read_jsonl", "write_jsonl", "append_jsonl",
    "load_pickle", "save_pickle",
    "load_safetensors", "save_safetensors",
    "read_file", "write_file", "append_file",
    "load_pt", "save_pt",
]
