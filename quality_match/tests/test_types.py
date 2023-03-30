import pytest

from quality_match.types import from_bool, from_str


@pytest.mark.parametrize("test_input,expected", [(True, True), (False, False)])
def test_from_bool(test_input, expected):
    assert from_bool(test_input) == expected


def test_from_bool_raises():
    with pytest.raises(AssertionError):
        from_bool("no-a-valid-bool")

def test_from_str():
    assert from_str("hello") == "hello"

def test_from_str_raises():
    with pytest.raises(AssertionError):
        from_str(0)