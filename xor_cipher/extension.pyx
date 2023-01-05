from cpython.bytearray cimport PyByteArray_AsString, PyByteArray_FromStringAndSize
from cpython.bytes cimport PyBytes_AsString, PyBytes_FromStringAndSize

from cython import cdivision

from libc.stdlib cimport free, malloc
from libc.string cimport memcpy

# NOTE: `cdivision(True)` removes python integer division checks


cdef char* copy_bytes(bytes data, size_t length):
    cdef char* source = PyBytes_AsString(data)

    cdef char* destination = <char*> malloc(length * sizeof(char))

    memcpy(destination, source, length)

    return destination


@cdivision(True)
cpdef bytes xor(bytes data, int key):
    cdef size_t length = len(data)

    cdef char* c_data = copy_bytes(data, length)

    cdef char c_key = key

    for index in range(length):
        c_data[index] ^= c_key

    cdef bytes result = PyBytes_FromStringAndSize(c_data, length)

    free(c_data)

    return result


@cdivision(True)
cpdef bytes cyclic_xor(bytes data, bytes key):
    cdef size_t key_length = len(key)

    if key_length == 0:
        return data

    cdef size_t length = len(data)

    cdef char* c_data = copy_bytes(data, length)
    cdef char* c_key = key

    for index in range(length):
        c_data[index] ^= c_key[index % key_length]

    cdef bytes result = PyBytes_FromStringAndSize(c_data, length)

    free(c_data)

    return result


@cdivision(True)
cpdef bytes cyclic_xor_unsafe(bytes data, bytes key):
    cdef size_t length = len(data)
    cdef size_t key_length = len(key)

    cdef char* c_data = copy_bytes(data, length)
    cdef char* c_key = key

    cdef size_t index

    for index in range(length):
        c_data[index] ^= c_key[index % key_length]

    cdef bytes result = PyBytes_FromStringAndSize(c_data, length)

    free(c_data)

    return result


@cdivision(True)
cpdef xor_in_place(bytearray data, int key):
    cdef size_t length = len(data)

    cdef char* c_data = data
    cdef char c_key = key

    for index in range(length):
        c_data[index] ^= c_key


@cdivision(True)
cpdef cyclic_xor_in_place(bytearray data, bytes key):
    cdef size_t key_length = len(key)

    if key_length == 0:
        return

    cdef size_t length = len(data)

    cdef char* c_data = data
    cdef char* c_key = key

    for index in range(length):
        c_data[index] ^= c_key[index % key_length]


@cdivision(True)
cpdef cyclic_xor_in_place_unsafe(bytearray data, bytes key):
    cdef size_t length = len(data)
    cdef size_t key_length = len(key)

    cdef char* c_data = data
    cdef char* c_key = key

    cdef size_t index

    for index in range(length):
        c_data[index] ^= c_key[index % key_length]
