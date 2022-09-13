from xor_cipher import xor_static
import copy

def test_reversability() -> None:
    content = b"Hello, world!"
    key = 0x69

    reversed_c = xor_static(xor_static(content, key), key)
    print(reversed_c)

    assert reversed_c == content, "The reversed content is not the same as the original content."

def test_immutability() -> None:
    content = b"Hello, world!"
    key = 0x69

    old_content = copy.copy(content)
    xor_static(content, key)

    assert content == old_content, "The original content was modified."

def test_known() -> None:
    content = b'Yt}}~=1f~c}u0'
    key = 0x11

    decoded = xor_static(content, key)

    assert decoded == b"Hello, world!", "The function output does not match the known answer!"
