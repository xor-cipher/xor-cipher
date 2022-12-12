from itertools import cycle

__all__ = (
    "DEFAULT_ENCODING",
    "DEFAULT_ERRORS",
    "FAST",
    "cyclic_xor",
    "cyclic_xor_in_place",
    "cyclic_xor_in_place_unsafe",
    "cyclic_xor_unsafe",
    "cyclic_xor_string",
    "cyclic_xor_string_unsafe",
    "xor",
    "xor_in_place",
    "xor_string",
)


def xor(data: bytes, key: int) -> bytes:
    """Applies *XOR* operation (`byte ^ key`) for each `byte` in `data`.

    Arguments:
        data: The data to encode.
        key: The key to use for encoding. Must be in range `[0, 255]`.

    Returns:
        The encoded data.
    """
    return bytes(byte ^ key for byte in data)


def cyclic_xor(data: bytes, key: bytes) -> bytes:
    """Applies *XOR* operation (`byte ^ key_byte`) for each `byte` in `data`
    and `key_byte` in `key`, which is cycled to fit the length of the `data`.

    Arguments:
        data: The data to encode.
        key: The key to use for encoding.

    Returns:
        The encoded data.
    """
    if not key:
        return data

    return bytes(byte ^ key_byte for byte, key_byte in zip(data, cycle(key)))


def cyclic_xor_unsafe(data: bytes, key: bytes) -> bytes:
    """Similar to [`cyclic_xor`][xor_cipher.core.cyclic_xor], except this function omits key checks.

    Warning:
        This function can *not* be called with an empty key, as it would crash the interpreter!

    Arguments:
        data: The data to encode.
        key: The key to use for encoding. Must be non-empty!

    Returns:
        The encoded data.
    """
    if not key:
        return data

    return bytes(byte ^ key_byte for byte, key_byte in zip(data, cycle(key)))


def xor_in_place(data: bytearray, key: int) -> None:
    """Similar to [`xor`][xor_cipher.core.xor], except it operates *in-place*.

    Arguments:
        data: The data to encode.
        key: The key to use for encoding. Must be in range `[0, 255]`.
    """
    length = len(data)

    for index in range(length):
        data[index] ^= key


def cyclic_xor_in_place(data: bytearray, key: bytes) -> None:
    """Similar to [`cyclic_xor`][xor_cipher.core.cyclic_xor], except it operates *in-place*.

    Arguments:
        data: The data to encode.
        key: The key to use for encoding.
    """
    key_length = len(key)

    if not key:
        return

    length = len(data)

    for index in range(length):
        data[index] ^= key[index % key_length]


def cyclic_xor_in_place_unsafe(data: bytearray, key: bytes) -> None:
    """Similar to [`cyclic_xor_unsafe`][xor_cipher.core.cyclic_xor_unsafe],
    except it operates *in-place*.

    Warning:
        This function can *not* be called with an empty key, as it would crash the interpreter!

    Arguments:
        data: The data to encode.
        key: The key to use for encoding. Must be non-empty!
    """
    key_length = len(key)

    if not key:
        return

    length = len(data)

    for index in range(length):
        data[index] ^= key[index % key_length]


DEFAULT_ENCODING = "utf-8"
"""The default encoding to use."""

DEFAULT_ERRORS = "strict"
"""The default errors strategy to use."""


def xor_string(
    string: str,
    key: int,
    encoding: str = DEFAULT_ENCODING,
    errors: str = DEFAULT_ERRORS,
) -> str:
    """Wraps [`xor`][xor_cipher.core.xor] to handle string encoding.

    Arguments:
        string: The string to encode.
        key: The key to use for encoding.
        encoding: The encoding to use.
        errors: The errors strategy to use.

    Returns:
        The encoded string.
    """
    result = xor(string.encode(encoding, errors), key)

    return result.decode(encoding, errors)


def cyclic_xor_string(
    string: str,
    key: str,
    encoding: str = DEFAULT_ENCODING,
    errors: str = DEFAULT_ERRORS,
) -> str:
    """Wraps [`cyclic_xor`][xor_cipher.core.cyclic_xor] to handle string encoding.

    Arguments:
        string: The string to encode.
        key: The key to use for encoding. Must be in range `[0, 255]`.
        encoding: The encoding to use.
        errors: The errors strategy to use.

    Returns:
        The encoded string.
    """
    result = cyclic_xor(string.encode(encoding, errors), key.encode(encoding, errors))

    return result.decode(encoding, errors)


def cyclic_xor_string_unsafe(
    string: str,
    key: str,
    encoding: str = DEFAULT_ENCODING,
    errors: str = DEFAULT_ERRORS,
) -> str:
    """Wraps [`cyclic_xor_unsafe`][xor_cipher.core.cyclic_xor_unsafe] to handle string encoding.

    Warning:
        This function can *not* be called with an empty key, as it would crash the interpreter!

    Arguments:
        string: The string to encode.
        key: The key to use for encoding. Must be non-empty!
        encoding: The encoding to use.
        errors: The errors strategy to use.

    Returns:
        The encoded string.
    """
    result = cyclic_xor(string.encode(encoding, errors), key.encode(encoding, errors))

    return result.decode(encoding, errors)


FAST = True
"""Whether the library is fast (i.e. the extension is available)."""


try:
    from xor_cipher.extension import (  # type: ignore
        cyclic_xor,
        cyclic_xor_in_place,
        cyclic_xor_in_place_unsafe,
        cyclic_xor_unsafe,
        xor,
        xor_in_place,
    )

except ImportError:
    FAST = False
