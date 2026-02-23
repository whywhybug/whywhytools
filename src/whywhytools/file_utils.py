from pathlib import Path
from typing import Union
import os
from .type_checker import check_file

def read_file(file: Union[str, Path], lines: bool = False) -> Union[str, list[str]]:
    """
    Read a text file and return its content.

    Args:
        file (Union[str, Path]): The path to the text file.
        lines (bool, optional): If True, return a list of strings, one for each line. Defaults to False.

    Returns:
        Union[str, list[str]]: The content of the file as a single string or a list of strings.
    """
    check_file(file)
    
    with open(file, mode='r', encoding='utf-8') as reader:
        if lines:
            content = reader.read().splitlines()
        else:
            content = reader.read()
    return content

def write_file(lines: Union[str, list[str]], file: Union[str, Path], force=False, silent=False) -> None:
    """
    Write a string or a list of strings to a text file.

    Args:
        lines (Union[str, list[str]]): A single string or a list of strings to write.
        file (Union[str, Path]): The path to the output text file.
        force (bool, optional): If True, overwrite the file if it exists. Defaults to False.
        silent (bool, optional): If True, suppress print messages. Defaults to False.
    """
    check_file(file)
    
    if isinstance(lines, str):
        lines = [lines]
    elif not isinstance(lines, list):
        raise TypeError(f"lines must be a str or list[str]; got {type(lines).__name__}")
    
    if os.path.exists(file) and force == False:
        print('[INFO] {} already exists.'.format(file))
        return
    
    dir_path = os.path.dirname(file)
    if dir_path != '':
        os.makedirs(dir_path, exist_ok=True)
    
    with open(file, mode='w', encoding='utf-8', newline='\n') as fp:
        for line in lines:
            print(line, file=fp)
    
    if not silent:
        print('[INFO] save to {}'.format(file))

def append_file(lines: Union[str, list[str]], file: Union[str, Path]) -> None:
    """
    Append a string or a list of strings to an existing text file.

    Args:
        lines (Union[str, list[str]]): A single string or a list of strings to append.
        file (Union[str, Path]): The path to the text file.
    """
    check_file(file)
    
    if isinstance(lines, str):
        lines = [lines]
    elif not isinstance(lines, list):
        raise TypeError(f"lines must be a str or list[str]; got {type(lines).__name__}")
    
    dir_path = os.path.dirname(file)
    if dir_path != '':
        os.makedirs(dir_path, exist_ok=True)
    
    with open(file, mode='a', encoding='utf-8', newline='\n') as fp:
        for line in lines:
            print(line, file=fp)
