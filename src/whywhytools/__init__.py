"""The whywhytools package provides a collection of utility functions for file I/O.

This module exposes functions for reading and writing various file formats including
JSON, JSONL, Pickle, Text, PyTorch tensors, and Safetensors, along with common file system utilities.
"""

from importlib.metadata import version, PackageNotFoundError


try:
    __version__ = version("whywhytools")
except PackageNotFoundError:
    # Package is not installed (e.g., running directly from source without installation)
    __version__ = "unknown"

from .io_managers import *
from .utils import create_parent_dirs
from .logging_utils import setup_logger


__all__ = [
    "__version__",
    "create_parent_dirs",
    "setup_logger",
]
