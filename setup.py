import sys

from pybind11.setup_helpers import Pybind11Extension
from setuptools import setup
from Cython.Build import cythonize

sys.argv.append('build_ext')
sys.argv.append('--inplace')

setup(
    ext_modules=cythonize(["levensteine.pyx"], compiler_directives={'language_level': "3"})
)

setup(
    ext_modules=[
        Pybind11Extension(
            "cpplev",
            ["cpplev.cpp"],
            cxx_std=20
        )
    ]
)
