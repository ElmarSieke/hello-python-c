from cffi import FFI

ffi = FFI()
libhello = ffi.dlopen('./libhello.so')

ffi.cdef("""
    int printMsg(char *msg, int len);
""")

# output: Hello World!
msg = ('Hello World!'.encode('utf-8'))
if libhello.printMsg(msg, len(msg)):
    print('Error: msg to long')

# output: Error: msg to long
msg = ('Hello World!!!'.encode('utf-8'))
if libhello.printMsg(msg, len(msg)):
    print('Error: msg to long')