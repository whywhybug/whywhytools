from pathlib import Path

import pytest

from whywhytools import append_file, read_file, write_file


def test_write_and_read_file(tmp_path: Path):
    test_file = tmp_path / "test.txt"
    lines = ["Line 1", "Line 2", "Line 3"]

    # Test write_file
    write_file(lines, test_file, silent=True)
    assert test_file.exists()

    # Test read_file with lines=True
    read_lines = read_file(test_file, lines=True)
    assert read_lines == lines

    # Test read_file with lines=False
    read_content = read_file(test_file, lines=False)
    assert read_content.strip() == "\n".join(lines)


def test_write_file_string_and_force(tmp_path: Path):
    test_file = tmp_path / "test.txt"

    # Single string
    write_file("Initial Content", test_file, silent=True)
    assert read_file(test_file) == "Initial Content\n"

    # force=False should exit with error message
    with pytest.raises(SystemExit) as exc_info:
        write_file("New Content", test_file, force=False, silent=True)
    assert "already exists" in str(exc_info.value)
    assert read_file(test_file, lines=False) == "Initial Content\n"

    # force=True should overwrite
    write_file("Forced Content", test_file, force=True, silent=True)
    assert read_file(test_file, lines=False) == "Forced Content\n"


def test_append_file(tmp_path: Path):
    test_file = tmp_path / "test.txt"

    # Append to non-existent creates it
    append_file("First Line", test_file)
    assert read_file(test_file, lines=True) == ["First Line"]

    # Append multiple lines
    append_file(["Second", "Third"], test_file)
    assert read_file(test_file, lines=True) == ["First Line", "Second", "Third"]


def test_text_manager_type_error(tmp_path: Path):
    test_file = tmp_path / "test.txt"

    with pytest.raises(TypeError):
        write_file([1, 2, 3], test_file)  # List elements must be strings

    with pytest.raises(TypeError):
        read_file(123)
