# setup.py
from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        'rectangle',  # Module name
        ['question3.cpp'], 
        include_dirs=[pybind11.get_include()],
        language='c++'
    ),
]

setup(
    name='rectangle',
    version='0.1',
    ext_modules=ext_modules,
)

