from cpython.bytes cimport PyBytes_FromStringAndSize
import cython

# Removes Python's integer checks.
@cython.cdivision(True)
cpdef bytes xor_static(bytes content, int key):
    cdef char* c_content = content
    cdef size_t length = len(content)

    for i in range(length):
        c_content[i] ^= key
    
    return PyBytes_FromStringAndSize(c_content, length)

@cython.cdivision(True)
cpdef bytes xor_cyclic(bytes content, bytes key):
    cdef size_t key_length = len(key)
    if key_length == 0:
        raise ValueError("Key cannot be empty!")

    cdef char* c_content = content
    cdef char* c_key = key
    cdef size_t length = len(content)
    cdef size_t i = 0

    for i in range(length):
        c_content[i] ^= c_key[i % key_length]
    
    return PyBytes_FromStringAndSize(c_content, length)

@cython.cdivision(True)
cpdef bytes xor_cyclic_unsafe(bytes content, bytes key):
    cdef char* c_content = content
    cdef char* c_key = key
    cdef size_t length = len(content)
    cdef size_t key_length = len(key)
    cdef size_t i = 0

    for i in range(length):
        c_content[i] ^= c_key[i % key_length]
    
    return PyBytes_FromStringAndSize(c_content, length)
