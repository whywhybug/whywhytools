import pytest
torch = pytest.importorskip("torch")

from pathlib import Path
from whywhytools.torch_manager import load_torch, save_torch

def test_save_and_load_torch(tmp_path: Path):
    test_file = tmp_path / "test.pt"
    data = {"hello": "world", "values": torch.tensor([1, 2, 3])}
    
    save_torch(data, test_file, silent=True)
    assert test_file.exists()
    
    loaded_data = load_torch(test_file)
    assert loaded_data["hello"] == data["hello"]
    assert torch.equal(loaded_data["values"], data["values"])

def test_save_torch_force(tmp_path: Path, capsys):
    test_file = tmp_path / "test.pt"
    data1 = torch.tensor([1, 2, 3])
    data2 = torch.tensor([4, 5, 6])
    
    save_torch(data1, test_file, silent=True)
    
    # force=False
    save_torch(data2, test_file, force=False, silent=True)
    assert torch.equal(load_torch(test_file), data1)
    
    captured = capsys.readouterr()
    assert "already exists" in captured.out
    
    # force=True
    save_torch(data2, test_file, force=True, silent=True)
    assert torch.equal(load_torch(test_file), data2)

def test_torch_manager_type_error():
    with pytest.raises(TypeError):
        load_torch(123)
