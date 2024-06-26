from hypothesis import given
from pytest import raises

from tests.strategies import not_byte_strategy
from xor_cipher.bytes import expect_byte


@given(not_byte_strategy)
def test_check_byte(not_byte: int) -> None:
    with raises(ValueError):
        expect_byte(not_byte)
