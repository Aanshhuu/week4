###ASSIGNMENT 1

import ctypes

lib = ctypes.CDLL('./libfunctions.so')  # use './functions.dll' on Windows

lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
lib.add.restype = ctypes.c_int

lib.multiply.argtypes = [ctypes.c_int, ctypes.c_int]
lib.multiply.restype = ctypes.c_int

lib.subtract.argtypes = [ctypes.c_int, ctypes.c_int]
lib.subtract.restype = ctypes.c_int

print(f"Add: {lib.add(10, 5)}")
print(f"Multiply: {lib.multiply(10, 5)}")
print(f"Subtract: {lib.subtract(10, 5)}")
