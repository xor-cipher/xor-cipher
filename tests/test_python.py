import pytest
from hypothesis import given

from tests.strategies import byte_strategy, bytes_strategy
from xor_cipher.python import cyclic_xor, cyclic_xor_in_place, xor, xor_in_place

EXPECTED = b"Hello, world!"


@pytest.fixture
def expected_data() -> bytes:
    return EXPECTED


DATA = b"\n'..-nb5-0.&c"


@pytest.fixture
def given_data() -> bytes:
    return DATA


KEY = 0x42


@pytest.fixture
def given_key() -> int:
    return KEY


CYCLIC_DATA = b"\n)#.-`o5->#&c"


@pytest.fixture
def given_cyclic_data() -> bytes:
    return CYCLIC_DATA


CYCLIC_KEY = b"BLOB"


@pytest.fixture
def given_cyclic_key() -> bytes:
    return CYCLIC_KEY


@given(bytes_strategy, byte_strategy)
def test_xor(data: bytes, key: int) -> None:
    assert xor(xor(data, key), key) == data


def test_cyclic_xor_expected(
    given_cyclic_data: bytes, given_cyclic_key: bytes, expected_data: bytes
) -> None:
    assert cyclic_xor(given_cyclic_data, given_cyclic_key) == expected_data


@given(bytes_strategy, bytes_strategy)
def test_cyclic_xor(data: bytes, key: bytes) -> None:
    assert cyclic_xor(cyclic_xor(data, key), key) == data


def test_xor_in_place_expected(given_data: bytes, given_key: int, expected_data: bytes) -> None:
    array = bytearray(given_data)

    xor_in_place(array, given_key)

    assert array == expected_data


@given(bytes_strategy, byte_strategy)
def test_xor_in_place(data: bytes, key: int) -> None:
    array = bytearray(data)

    xor_in_place(array, key)
    xor_in_place(array, key)

    assert array == data


def test_cyclic_xor_in_place_expected(
    given_cyclic_data: bytes, given_cyclic_key: bytes, expected_data: bytes
) -> None:
    array = bytearray(given_cyclic_data)

    cyclic_xor_in_place(array, given_cyclic_key)

    assert array == expected_data


@given(bytes_strategy, bytes_strategy)
def test_cyclic_xor_in_place(data: bytes, key: bytes) -> None:
    array = bytearray(data)

    cyclic_xor_in_place(array, key)
    cyclic_xor_in_place(array, key)

    assert array == data
