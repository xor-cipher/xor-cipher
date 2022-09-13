from libc.stdint cimport *

cpdef bytes xor_static(bytes content, int key):
    cdef char* c_content = content
    cdef uint8_t length = len(content)

    for i in range(length):
        c_content[i] ^= key
    
    return bytes(c_content)

cpdef bytes xor_cyclic(bytes content, bytes key):
    cdef char* c_content = content
    cdef char* c_key = key
    cdef uint8_t length = len(content)
    cdef uint8_t key_length = len(key)
    cdef uint8_t i = 0

    for i in range(length):
        c_content[i] ^= c_key[i % key_length]
    
    return bytes(c_content)
