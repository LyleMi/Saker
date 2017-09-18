#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name="Saker",
    version="1.0",
    keywords=("CTF", "Web"),
    description="CTF Web framework and fuzz tool",
    license="GPLv3 Licence",
    author="lyle",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    scripts=["./saker/classes/saker.py"],
)
