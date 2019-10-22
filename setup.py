#!/usr/bin/env python
import os
from setuptools import setup

LICENSE = open(
    os.path.join(os.path.dirname(__file__), 'LICENSE')).read().strip()
DESCRIPTION = open(
    os.path.join(os.path.dirname(__file__), 'README.md')).read().strip()

setup(
    name='redis-url-py',
    version='0.0.4',
    url='https://github.com/Xopherus/redis-url-py',
    license=LICENSE,
    author='Chris Raborg',
    author_email='craborg1@umbc.edu',
    description='Use Redis URLs in your Python applications',
    long_description=DESCRIPTION,
    py_modules=['redis_url'],
    install_requires = ["future"],
    zip_safe=False,
)
