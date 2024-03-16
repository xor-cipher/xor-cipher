from hypothesis.strategies import binary, integers

from xor_cipher.keys import MAX_KEY, MIN_KEY

bytes_strategy = binary()
byte_strategy = integers(MIN_KEY, MAX_KEY)


def is_invalid_key(key: int) -> bool:
    return key < MIN_KEY or key > MAX_KEY


invalid_key_strategy = integers().filter(is_invalid_key)
