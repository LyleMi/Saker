#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name="Saker",
    version="1.0",
    keywords=("Web Security", "Fuzz"),
    description="Tool For Fuzz Web Applications",
    license="GPLv3 Licence",
    url="https://github.com/LyleMi/Saker",
    author="Lyle",
    author_email="lylemi@126.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    package_data={
        'saker': [
            'data/*.*',
            'data/sample/*',
        ]
    },
    scripts=[],
)
