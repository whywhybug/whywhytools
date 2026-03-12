# whywhytools

whywhytools is a lightweight Python package for reading and writing JSON, JSON Lines (`.jsonl`), and Pickle files. It provides simple and intuitive APIs for handling these common data formats.

## Installation

The package can be installed via pip:

```bash
pip install whywhytools
```

For extended functionalities, optional dependencies are available. 

To install dependencies for specific features:

```bash
pip install "whywhytools[torch]"
pip install "whywhytools[safetensors]"
```

To install all optional dependencies simultaneously:

```bash
pip install "whywhytools[all]"
```

## Quickstart

### JSON Lines (`.jsonl`)

Handle `.jsonl` files, supporting read, write, and append operations.

##### Write JSONL File

```python
from whywhytools import write_jsonl

data = [
    {'id': 'data-1', 'text': 'hello world'},
    {'id': 'data-2', 'text': 'whywhytools is awesome'}
]

# Write to file
write_jsonl(data, 'output.jsonl') # [INFO] save to output.jsonl

# If file exists
write_jsonl(data, 'output.jsonl') # [INFO] output.jsonl already exists.

# Force overwrite existing file
write_jsonl(data, 'output.jsonl', force=True) # [INFO] save to output.jsonl

# Silent mode (not print any message)
write_jsonl(data, 'output.jsonl', force=True, silent=True)
```

##### Append to JSONL File

```python
from whywhytools import append_jsonl

new_data = [{'id': 'data-3', 'text': 'new line'}]
append_jsonl(new_data, 'output.jsonl')
```

##### Read JSONL File

```python
from whywhytools import read_jsonl

data = read_jsonl('output.jsonl')
print(data)
# [{'id': 'data-1', 'text': 'hello world'}, {'id': 'data-2', 'text': 'whywhytools is awesome'}, {'id': 'data-3', 'text': 'new line'}]
```

### JSON (`.json`)

Handle standard `.json` files.

##### Write JSON File

```python
from whywhytools import write_json

data = {'project': 'whywhytools', 'version': '0.1.0'}

# Write to file
write_json(data, 'config.json')
```

##### Read JSON File

```python
from whywhytools import read_json

config = read_json('config.json')
print(config)
```

### Pickle (`.pkl`)

Handle Python's pickle serialization format.

##### Save Pickle File

```python
from whywhytools import save_pickle

model_data = {'weights': [0.1, 0.5, 0.9], 'bias': 0.01}
save_pickle(model_data, 'model.pkl')
```

##### Load Pickle File

```python
from whywhytools import load_pickle

data = load_pickle('model.pkl')
print(data)
```

### Plain Text (`.txt` or general text files)

Handle plain text files, supporting direct string reading or line-by-line list loading, as well as write and append operations.

##### Write Text File

```python
from whywhytools import write_file

lines = [
    "First line of the text file.",
    "Second line is here."
]

# Write a list of strings to a file
write_file(lines, "document.txt")

# Write a single string
write_file("Just one line here.", "single_doc.txt")
```

##### Append to Text File

```python
from whywhytools import append_file

# Append single or multiple lines
append_file("This is a newly appended line.", "document.txt")
```

##### Read Text File

```python
from whywhytools import read_file

# Read entire file as a single string
content = read_file("document.txt")
print(content)

# Read file line by line into a list
lines = read_file("document.txt", lines=True)
print(lines)
```

### PyTorch (`.pt` or `.pth`)

Handle PyTorch files. Compared to the original `torch.save` and `torch.load`, `whywhytools` provides built-in path type checking, automatic parent directory creation, and safety guards like `force` argument to prevent accidental overwrites.

##### Save PyTorch File

```python
import torch
from whywhytools import save_pt

model_data = {'weights': torch.tensor([0.1, 0.5, 0.9])}
save_pt(model_data, 'model.pt')
```

##### Load PyTorch File

```python
from whywhytools import load_pt

data = load_pt('model.pt')
print(data)

# Load safely with weights_only=True
safe_data = load_pt('model.pt', weights_only=True)
```

## License

MIT
