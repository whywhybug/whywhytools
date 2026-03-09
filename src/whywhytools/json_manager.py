from pathlib import Path
from typing import Union
import os
import sys
import json
from .type_checker import check_type
from .utils import create_parent_dir

def read_json(file: Union[str, Path]) -> dict:
    """
    Read a JSON file and return its content.

    Args:
        file (Union[str, Path]): The path to the JSON file.

    Returns:
        dict: The JSON object read from the file.
    """
    check_type(file, (str, Path))

    with open(file, mode='r', encoding='utf-8') as reader:
        df = json.load(reader)
    return df

def write_json(
    obj: Union[dict],
    file: Union[str, Path],
    force: bool = False,
    silent: bool = False,
    raise_on_exists: bool = False,
) -> None:
    """
    Write a dictionary to a JSON file.

    Args:
        obj (Union[dict]): The dictionary object to write.
        file (Union[str, Path]): The path to the output JSON file.
        force (bool, optional): If True, overwrite the file if it exists. Defaults to False.
        silent (bool, optional): If True, suppress print messages. Defaults to False.
        raise_on_exists (bool, optional): If True, raise FileExistsError with full
            traceback instead of exiting cleanly. Defaults to False.

    Raises:
        TypeError: If obj or file is not the expected type.
        FileExistsError: If the file exists, force is False, and traceback is True.
    """
    check_type(file, (str, Path))
    if os.path.exists(file) and not force:
        msg = '[ERROR] {} already exists.'.format(file)
        if raise_on_exists:
            raise FileExistsError(msg)
        sys.exit(msg)
    create_parent_dir(file)
    
    check_type(obj, dict)

    with open(file, mode='w', encoding='utf-8', newline='\n') as fp:
        json.dump(obj, fp, ensure_ascii=False, indent=4)
        print(file=fp)
    
    if not silent:
        print('[INFO] save to {}'.format(file))
