# Recursive function to calculate factorial in Python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial (Python): {factorial(5)}")



import ctypes
import time


lib = ctypes.CDLL('./question2.so')


lib.factorial.argtypes = [ctypes.c_int]
lib.factorial.restype = ctypes.c_int

def factorial_python(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_python(n - 1)

# For measuring performance of C function
start = time.time()
print(f"Factorial (C): {lib.factorial(10)}")
end = time.time()
print(f"C Time: {end - start} seconds")

# For measuring performance of Python function
start = time.time()
print(f"Factorial (Python): {factorial_python(10)}")
end = time.time()
print(f"Python Time: {end - start} seconds")