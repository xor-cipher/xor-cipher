from hypothesis import given
from pytest import raises

from tests.strategies import invalid_key_strategy
from xor_cipher.keys import validate_key


@given(invalid_key_strategy)
def test_validate_key(invalid_key: int) -> None:
    with raises(ValueError):
        validate_key(invalid_key)
