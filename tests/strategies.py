from funcs.functions import complement
from hypothesis.strategies import binary, integers

from xor_cipher.typing import MIN_BYTE, MAX_BYTE, is_byte

bytes_strategy = binary()
byte_strategy = integers(MIN_BYTE, MAX_BYTE)

not_byte_strategy = integers().filter(complement(is_byte))
