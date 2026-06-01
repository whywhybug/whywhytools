"""This module provides utility functions for type checking."""

from __future__ import annotations

import inspect
import re
from typing import Any


def get_var_name(variable: Any, back_frames: int = 2) -> str:
    """
    Attempt to find the name of the variable in the caller's frames.

    Args:
        variable (Any): The variable to find the name for.
        back_frames (int, optional): How many frames to go back. Defaults to 2.
                                     (1 for get_var_name's caller, 2 for the caller's caller).

    Returns:
        str: The name of the variable if found, otherwise "variable".
    """
    try:
        frame = inspect.currentframe()
        prev_frame = None
        for _ in range(back_frames):
            if frame is not None:
                prev_frame = frame
                frame = frame.f_back

        if frame is not None and prev_frame is not None:
            # Try to parse the source code of the call line directly
            caller_func_name = prev_frame.f_code.co_name
            frame_info = inspect.getframeinfo(frame)
            if frame_info.code_context:
                line = frame_info.code_context[0].strip()
                match = re.search(rf"{caller_func_name}\s*\(\s*([^,]+)\s*,", line)
                if match:
                    return match.group(1).strip()

            # Fallback to variable memory identity
            for name, val in frame.f_locals.items():
                if val is variable and not name.startswith("_"):
                    return name
            for name, val in frame.f_globals.items():
                if val is variable and not name.startswith("_"):
                    return name
    except Exception:
        pass
    return "variable"


def check_type(variable: Any, expected_type: type | tuple[type, ...], var_name: str | None = None) -> None:
    """
    Check if a variable is an instance of the expected type(s).

    Args:
        variable (Any): The variable to check.
        expected_type (Union[type, Tuple[type, ...]]): The expected type or a tuple of expected types.
        var_name (str, optional): The name of the variable to use in the error message.
                                  If None, an attempt is made to detect it automatically.

    Raises:
        TypeError: If the variable is not an instance of the expected type(s).
    """
    if not isinstance(variable, expected_type):
        if var_name is None:
            var_name = get_var_name(variable)

        if isinstance(expected_type, tuple):
            type_names = " or ".join([getattr(t, "__name__", str(t)) for t in expected_type])
        else:
            type_names = getattr(expected_type, "__name__", str(expected_type))
        raise TypeError(f"{var_name} must be {type_names}, got {type(variable).__name__}")


def check_list_type(variable_list: Any, expected_type: type | tuple[type, ...], var_name: str | None = None) -> None:
    """
    Check if a variable is a list and all its elements are instances of the expected type(s).

    Args:
        variable_list (Any): The variable to check.
        expected_type (Union[type, Tuple[type, ...]]): The expected type or a tuple of expected types for the elements.
        var_name (str, optional): The name of the variable to use in the error message.
                                  If None, an attempt is made to detect it automatically.

    Raises:
        TypeError: If the variable is not a list, or if any element is not an instance of the expected type(s).
    """
    if var_name is None:
        var_name = get_var_name(variable_list)

    if not isinstance(variable_list, list):
        raise TypeError(f"{var_name} must be a list, got {type(variable_list).__name__}")

    for i, item in enumerate(variable_list):
        if not isinstance(item, expected_type):
            if isinstance(expected_type, tuple):
                type_names = " or ".join([getattr(t, "__name__", str(t)) for t in expected_type])
            else:
                type_names = getattr(expected_type, "__name__", str(expected_type))
            raise TypeError(f"{var_name} must be list[{type_names}]; got {type(item).__name__} at index {i}")
