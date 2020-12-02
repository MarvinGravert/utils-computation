
from setuptools import setup, find_packages

import gen_code
import os

modules = gen_code.generate_proto_code()
os.chdir("./protodef_files")
setup(
    name='point_matching',  # name which will be used to install via pip
    version='0.1',  # version number simple as that
    description='module to run different point matching algorithms',
    long_description='',
    author='Marvin Gravert',
    author_email='marvin.gravert@gmail.com',

    license='MIT',
    # which directories to search for imports. Importable dirs are marked by
    packages=find_packages(),
    # py_modules=modules,
    # packages=find_packages()#also possible but may include unwanted dir such as tests
    zip_safe=False,
)
