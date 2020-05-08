#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requires = fh.read().split("\n")
    requires.remove('')

setup(
    name="Saker",
    version="1.0.5",
    keywords=("Web Security", "Fuzz"),
    description="Tool For Fuzz Web Applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3 Licence",
    url="https://github.com/LyleMi/Saker",
    author="Lyle",
    author_email="lylemi@126.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    platforms="any",
    package_data={
        'saker': [
            'data/*.*',
            'data/sample/*',
            'data/domains/*',
        ]
    },
    scripts=[],
)
