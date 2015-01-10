#!/usr/bin/env python

import os
import sys

import pygn

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'pygn',
]

requires = [
]

with open('README.md') as f:
    readme = f.read()

setup(
    name='pygn',
    version='0.1',
    description='A simple Python client for the Gracenote Music API',
    long_description=readme + '\n\n',
    author='Ching-Wei Chen',
    url='https://github.com/cweichen/pygn',
    packages=packages,
    package_data={},
    package_dir={},
    include_package_data=True,
    install_requires=requires,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
    ),
)
