import pytest

from hello_py.main import greet


def test_main() -> None:
    assert greet('Luck') == 'Hello, Luck'

def test_greet_negative() -> None:
    with pytest.raises(TypeError):
        greet(123)  # type: ignore