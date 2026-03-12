"""The whywhytools package provides a collection of utility functions for file I/O.

This module exposes functions for reading and writing various file formats including
JSON, JSONL, Pickle, Text, PyTorch tensors, and Safetensors, along with common file system utilities.
"""

from .json_manager import (
    read_json,
    write_json,
)
from .jsonl_manager import (
    append_jsonl,
    read_jsonl,
    write_jsonl,
)
from .pickle_manager import (
    load_pickle,
    save_pickle,
)
from .safetensors_manager import (
    load_safetensors,
    save_safetensors,
)
from .text_manager import (
    append_file,
    read_file,
    write_file,
)
from .torch_manager import (
    load_pt,
    save_pt,
)
from .utils import create_parent_dirs


__all__ = [
    "read_jsonl",
    "write_jsonl",
    "append_jsonl",
    "read_json",
    "write_json",
    "read_file",
    "write_file",
    "append_file",
    "load_pickle",
    "save_pickle",
    "load_pt",
    "save_pt",
    "load_safetensors",
    "save_safetensors",
    "create_parent_dirs",
]
