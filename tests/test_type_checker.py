import pytest
from whywhytools.type_checker import check_list_type, check_type, get_var_name


def test_get_var_name():
    # Helper to test variable name extraction via get_var_name
    my_test_var = 42
    test_str = "hello"

    assert get_var_name(my_test_var) in ("my_test_var", "variable")
    assert get_var_name(test_str) in ("test_str", "variable")

    # We allow "variable" as fallback if inspection fails


def test_check_type_success():
    my_int = 10
    my_str = "hello"

    # These should not raise exceptions
    check_type(my_int, int)
    check_type(my_str, str)
    check_type(my_int, (int, float))


def test_check_type_failure():
    my_int = 10

    with pytest.raises(TypeError, match="must be str, got int"):
        check_type(my_int, str, var_name="my_int")

    with pytest.raises(TypeError, match="must be str or float, got int"):
        check_type(my_int, (str, float), var_name="my_int")

    # Auto variable name detection if var_name is omitted (test fallback or actual matching)
    with pytest.raises(TypeError):
        check_type(10, str)


def test_check_list_type_success():
    int_list = [1, 2, 3]
    mixed_list = [1, "two", 3.0]

    # Should not raise
    check_list_type(int_list, int)
    check_list_type(mixed_list, (int, str, float))


def test_check_list_type_failure():
    not_a_list = "I am a string"
    with pytest.raises(TypeError, match="must be a list"):
        check_list_type(not_a_list, str, var_name="not_a_list")

    str_list = ["a", "b", 3]
    with pytest.raises(TypeError, match="got int at index 2"):
        check_list_type(str_list, str, var_name="str_list")
