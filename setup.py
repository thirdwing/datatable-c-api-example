from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import sys
import setuptools
import pybind11

__version__ = '0.0.1'

ext_modules = [
    Extension(
        'example',
        sources=['src/example.cc'],
        include_dirs=[pybind11.get_include(),
                      'datatable/datatable/include'],
        language='c++',
        extra_compile_args=['-std=c++11']
    ),
]

setup(name='example',
      version=__version__,
      ext_modules=ext_modules,
      zip_safe=False)
