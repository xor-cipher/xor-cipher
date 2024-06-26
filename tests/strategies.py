from hypothesis.strategies import binary, integers

from xor_cipher.bytes import MIN_BYTE, MAX_BYTE, is_not_byte

bytes_strategy = binary()
byte_strategy = integers(MIN_BYTE, MAX_BYTE)

not_byte_strategy = integers().filter(is_not_byte)
