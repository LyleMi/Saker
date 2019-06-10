#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'ipaddress>=1.0.19',
    'netaddr>=0.7.19',
    'requests>=2.20.0',
    'six>=1.11.0',
    'urllib3>=1.22',
    'dnspython>=1.15.0'
]

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
