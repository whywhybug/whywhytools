import pytest


torch = pytest.importorskip("torch")
safetensors = pytest.importorskip("safetensors")

from pathlib import Path

from whywhytools import load_safetensors, save_safetensors


def test_save_and_load_safetensors(tmp_path: Path):
    test_file = tmp_path / "test.safetensors"
    data = {"hello": torch.tensor([1, 2, 3]), "world": torch.tensor([4.0, 5.0, 6.0])}

    save_safetensors(data, test_file, silent=True)
    assert test_file.exists()

    loaded_data = load_safetensors(test_file)
    assert "hello" in loaded_data
    assert "world" in loaded_data
    assert torch.equal(loaded_data["hello"], data["hello"])
    assert torch.equal(loaded_data["world"], data["world"])


def test_save_safetensors_metadata(tmp_path: Path):
    test_file = tmp_path / "test_metadata.safetensors"
    data = {"tensor": torch.tensor([1])}
    metadata = {"author": "whywhybug", "version": "1.0"}

    save_safetensors(data, test_file, metadata=metadata, silent=True)
    assert test_file.exists()

    from safetensors import safe_open

    with safe_open(test_file, framework="pt") as f:
        loaded_metadata = f.metadata()
    assert loaded_metadata == metadata


def test_save_safetensors_force(tmp_path: Path):
    test_file = tmp_path / "test_force.safetensors"
    data1 = {"tensor": torch.tensor([1, 2, 3])}
    data2 = {"tensor": torch.tensor([4, 5, 6])}

    save_safetensors(data1, test_file, silent=True)

    # force=False should exit with error message
    with pytest.raises(SystemExit) as exc_info:
        save_safetensors(data2, test_file, force=False, silent=True)
    assert "already exists" in str(exc_info.value)

    loaded_data = load_safetensors(test_file)
    assert torch.equal(loaded_data["tensor"], data1["tensor"])

    # On Windows, safetensors keeps a memory mapping open while tensors exist
    del loaded_data
    import gc

    gc.collect()

    # force=True should overwrite
    save_safetensors(data2, test_file, force=True, silent=True)
    loaded_data_2 = load_safetensors(test_file)
    assert torch.equal(loaded_data_2["tensor"], data2["tensor"])


def test_save_safetensors_raise_on_exists(tmp_path: Path):
    test_file = tmp_path / "test_raise.safetensors"
    data = {"tensor": torch.tensor([1, 2, 3])}
    save_safetensors(data, test_file, silent=True)

    # raise_on_exists=True should raise FileExistsError instead of SystemExit
    with pytest.raises(FileExistsError) as exc_info:
        save_safetensors(data, test_file, force=False, silent=True, raise_on_exists=True)
    assert "already exists" in str(exc_info.value)


def test_safetensors_manager_type_error():
    with pytest.raises(TypeError):
        load_safetensors(123)
