from hypothesis import given

from tests.strategies import binary_strategy, bytes_strategy
from xor_cipher.core import cyclic_xor as python_cyclic_xor
from xor_cipher.core import cyclic_xor_in_place as python_cyclic_xor_in_place
from xor_cipher.core import xor as python_xor
from xor_cipher.core import xor_in_place as python_xor_in_place
from xor_cipher.extension import (
    cyclic_xor,
    cyclic_xor_in_place,
    xor,
    xor_in_place,
)


@given(binary_strategy, bytes_strategy)
def test_xor_consistency(data: bytes, key: int) -> None:
    assert xor(data, key) == python_xor(data, key)


@given(binary_strategy, binary_strategy)
def test_cyclic_xor_consistency(data: bytes, key: bytes) -> None:
    assert cyclic_xor(data, key) == python_cyclic_xor(data, key)


@given(binary_strategy, bytes_strategy)
def test_xor_in_place_consistency(data: bytes, key: int) -> None:
    array = bytearray(data)
    python_array = bytearray(data)

    xor_in_place(array, key)
    python_xor_in_place(python_array, key)

    assert array == python_array


@given(binary_strategy, binary_strategy)
def test_cyclic_xor_in_place_consistency(data: bytes, key: bytes) -> None:
    array = bytearray(data)
    python_array = bytearray(data)

    cyclic_xor_in_place(array, key)
    python_cyclic_xor_in_place(python_array, key)

    assert array == python_array
