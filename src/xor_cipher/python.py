from itertools import cycle

from xor_cipher.bytes import expect_byte

__all__ = ("xor", "cyclic_xor", "xor_in_place", "cyclic_xor_in_place")


def xor(data: bytes, key: int) -> bytes:
    """Applies XOR operation (`byte ^ key`) for each `byte` in `data`.

    This function is its own inverse, meaning

    ```python
    xor(xor(data, key), key) == data
    ```

    for any `data` and `key`.

    Arguments:
        data: The data to encode.
        key: The key to use for encoding. Must be in range `[0, 255]`.

    Raises:
        ValueError: If the `key` is not in `[0, 255]` range.

    Returns:
        The encoded data.
    """
    key = expect_byte(key)

    if not key:
        return data

    return bytes(byte ^ key for byte in data)


def cyclic_xor(data: bytes, key: bytes) -> bytes:
    """Applies XOR operation (`byte ^ key_byte`) for each `byte` in `data`
    and `key_byte` in `key`, which is cycled to fit the length of the `data`.

    This function is its own inverse, meaning

    ```python
    cyclic_xor(cyclic_xor(data, key), key) == data
    ```

    for any `data` and `key`.

    Arguments:
        data: The data to encode.
        key: The key to use for encoding.

    Returns:
        The encoded data.
    """
    if not key:
        return data

    return bytes(byte ^ key_byte for byte, key_byte in zip(data, cycle(key)))


def xor_in_place(data: bytearray, key: int) -> None:
    """Similar to [`xor`][xor_cipher.python.xor], except it operates *in-place*.

    Arguments:
        data: The data to encode.
        key: The key to use for encoding. Must be in range `[0, 255]`.

    Raises:
        ValueError: If the `key` is not in `[0, 255]` range.
    """
    key = expect_byte(key)

    if not key:
        return

    length = len(data)

    for index in range(length):
        data[index] ^= key


def cyclic_xor_in_place(data: bytearray, key: bytes) -> None:
    """Similar to [`cyclic_xor`][xor_cipher.python.cyclic_xor], except it operates *in-place*.

    Arguments:
        data: The data to encode.
        key: The key to use for encoding.
    """
    if not key:
        return

    key_length = len(key)

    length = len(data)

    for index in range(length):
        data[index] ^= key[index % key_length]
