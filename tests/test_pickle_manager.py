import pytest
from pathlib import Path
from whywhytools import load_pickle, save_pickle


def test_save_and_load_pickle(tmp_path: Path):
    test_file = tmp_path / "test.pkl"
    data = {"hello": "world", "values": [1, 2, 3]}

    save_pickle(data, test_file, silent=True)
    assert test_file.exists()

    loaded_data = load_pickle(test_file)
    assert loaded_data == data


def test_save_pickle_force(tmp_path: Path):
    test_file = tmp_path / "test.pkl"
    data1 = "data1"
    data2 = "data2"

    save_pickle(data1, test_file, silent=True)

    # force=False should exit with error message
    with pytest.raises(SystemExit) as exc_info:
        save_pickle(data2, test_file, force=False, silent=True)
    assert "already exists" in str(exc_info.value)
    assert load_pickle(test_file) == data1

    # force=True should overwrite
    save_pickle(data2, test_file, force=True, silent=True)
    assert load_pickle(test_file) == data2


def test_pickle_manager_type_error():
    with pytest.raises(TypeError):
        load_pickle(123)
