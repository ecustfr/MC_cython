# -*- coding: utf-8 -*-
"""
Created on Thu May 15 19:37:19 2025

@author: Administrator
"""

from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    ext_modules=cythonize("overlap1.pyx",language_level = 3),
    include_dirs=[numpy.get_include()],
)