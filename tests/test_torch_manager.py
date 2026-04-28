import pytest

torch = pytest.importorskip("torch")

from pathlib import Path
from whywhytools import load_pt, save_pt


def test_save_and_load_pt(tmp_path: Path):
    test_file = tmp_path / "test.pt"
    data = {"hello": "world", "values": torch.tensor([1, 2, 3])}

    save_pt(data, test_file, silent=True)
    assert test_file.exists()

    loaded_data = load_pt(test_file)
    assert loaded_data["hello"] == data["hello"]
    assert torch.equal(loaded_data["values"], data["values"])


def test_save_pt_force(tmp_path: Path):
    test_file = tmp_path / "test.pt"
    data1 = torch.tensor([1, 2, 3])
    data2 = torch.tensor([4, 5, 6])

    save_pt(data1, test_file, silent=True)

    # force=False should exit with error message
    with pytest.raises(SystemExit) as exc_info:
        save_pt(data2, test_file, force=False, silent=True)
    assert "already exists" in str(exc_info.value)
    assert torch.equal(load_pt(test_file), data1)

    # force=True should overwrite
    save_pt(data2, test_file, force=True, silent=True)
    assert torch.equal(load_pt(test_file), data2)


def test_torch_manager_type_error():
    with pytest.raises(TypeError):
        load_pt(123)
