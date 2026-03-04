# API Reference

Detailed documentation for `whywhytools` functions.

## JSON Lines (`.jsonl`)

Utilities for handling JSON Lines files.

### `read_jsonl`

```python
def read_jsonl(file: Union[str, Path]) -> list[dict]
```

Read a JSONL file and return a list of dictionaries.

**Args:**
* **file** (`Union[str, Path]`): The path to the JSONL file.

**Returns:**
* `list[dict]`: A list containing the JSON objects read from the file.

---

### `write_jsonl`

```python
def write_jsonl(obj_list: Union[dict, list[dict]], file: Union[str, Path], force=False, silent=False) -> None
```

Write a list of dictionaries to a JSONL file.

**Args:**
* **obj_list** (`Union[dict, list[dict]]`): A single dictionary or a list of dictionaries to write.
* **file** (`Union[str, Path]`): The path to the output JSONL file.
* **force** (`bool`, optional): If True, overwrite the file if it exists. Defaults to False.
* **silent** (`bool`, optional): If True, suppress print messages. Defaults to False.

---

### `append_jsonl`

```python
def append_jsonl(obj_list: Union[dict, list[dict]], file: Union[str, Path]) -> None
```

Append a list of dictionaries to an existing JSONL file.

**Args:**
* **obj_list** (`Union[dict, list[dict]]`): A single dictionary or a list of dictionaries to append.
* **file** (`Union[str, Path]`): The path to the JSONL file.

## JSON (`.json`)

Utilities for handling standard JSON files.

### `read_json`

```python
def read_json(file: Union[str, Path]) -> dict
```

Read a JSON file and return its content.

**Args:**
* **file** (`Union[str, Path]`): The path to the JSON file.

**Returns:**
* `dict`: The JSON object read from the file.

---

### `write_json`

```python
def write_json(obj: Union[dict], file: Union[str, Path], force=False, silent=False) -> None
```

Write a dictionary to a JSON file.

**Args:**
* **obj** (`Union[dict]`): The dictionary object to write.
* **file** (`Union[str, Path]`): The path to the output JSON file.
* **force** (`bool`, optional): If True, overwrite the file if it exists. Defaults to False.
* **silent** (`bool`, optional): If True, suppress print messages. Defaults to False.

**Raises:**
* `TypeError`: If obj is not a dictionary.

## Pickle (`.pkl`)

Utilities for handling Python pickle files.

### `load_pickle`

```python
def load_pickle(file: Union[str, Path]) -> Any
```

Load an object from a pickle file.

**Args:**
* **file** (`Union[str, Path]`): The path to the pickle file.

**Returns:**
* `Any`: The object loaded from the pickle file.

---

### `save_pickle`

```python
def save_pickle(obj, file: Union[str, Path], force=False, silent=False) -> None
```

Save an object to a pickle file.

**Args:**
* **obj** (`Any`): The object to save.
* **file** (`Union[str, Path]`): The path to the output pickle file.
* **force** (`bool`, optional): If True, overwrite the file if it exists. Defaults to False.
* **silent** (`bool`, optional): If True, suppress print messages. Defaults to False.

---

## Text (`.txt`)

Utilities for handling standard text files.

### `read_file`

```python
def read_file(file: Union[str, Path], lines: bool = False) -> Union[str, list[str]]
```

Read a text file and return its content.

**Args:**
* **file** (`Union[str, Path]`): The path to the text file.
* **lines** (`bool`, optional): If True, return a list of strings, one for each line. Defaults to False.

**Returns:**
* `Union[str, list[str]]`: The content of the file as a single string or a list of strings.

---

### `write_file`

```python
def write_file(lines: Union[str, list[str]], file: Union[str, Path], force=False, silent=False) -> None
```

Write a string or a list of strings to a text file.

**Args:**
* **lines** (`Union[str, list[str]]`): A single string or a list of strings to write.
* **file** (`Union[str, Path]`): The path to the output text file.
* **force** (`bool`, optional): If True, overwrite the file if it exists. Defaults to False.
* **silent** (`bool`, optional): If True, suppress print messages. Defaults to False.

---

### `append_file`

```python
def append_file(lines: Union[str, list[str]], file: Union[str, Path]) -> None
```

Append a string or a list of strings to an existing text file.

**Args:**
* **lines** (`Union[str, list[str]]`): A single string or a list of strings to append.
* **file** (`Union[str, Path]`): The path to the text file.

## PyTorch (`.pt`, `.pth`)

Utilities for handling PyTorch files. Compared to the original `torch.save` and `torch.load`, `whywhytools` provides built-in path type checking, automatic parent directory creation, and safety guards like `force` argument to prevent accidental overwrites.

### `load_torch`

```python
def load_torch(file: Union[str, Path], map_location: Any = None, weights_only: bool = False, **kwargs: Any) -> Any
```

Read a PyTorch file and return the loaded object.

**Args:**
* **file** (`Union[str, Path]`): The path to the PyTorch file.
* **map_location** (`Any`, optional): A function, torch.device, string or a dict specifying how to remap storage locations.
* **weights_only** (`bool`, optional): If True, only weights will be loaded. Defaults to False.
* **\*\*kwargs**: Additional keyword arguments to pass to `torch.load`.

**Returns:**
* `Any`: The object read from the PyTorch file.

---

### `save_torch`

```python
def save_torch(obj: Any, file: Union[str, Path], force: bool = False, silent: bool = False, **kwargs: Any) -> None
```

Write an object to a PyTorch file.

**Args:**
* **obj** (`Any`): The object to write to the file.
* **file** (`Union[str, Path]`): The path to the output PyTorch file.
* **force** (`bool`, optional): If True, overwrite the file if it exists. Defaults to False.
* **silent** (`bool`, optional): If True, suppress print messages. Defaults to False.
* **\*\*kwargs**: Additional keyword arguments to pass to `torch.save`.
