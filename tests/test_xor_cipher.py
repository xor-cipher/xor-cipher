from xor_cipher import xor


def test_xor_involution() -> None:
    data = b"Hello, world!"
    key = 0x69

    result = xor(xor(data, key), key)

    assert result == data


def test_xor_expected() -> None:
    expected = b"Hello, world!"

    data = b"\n'..-nb5-0.&c"
    key = 0x42

    result = xor(data, key)

    assert result == expected
