#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name="Saker",
    version="1.0",
    keywords=("ctf", "web"),
    description="a ctf web intelligent tool",
    license="GPLv3 Licence",
    author="lyle",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    scripts=["./saker.py"],
)
