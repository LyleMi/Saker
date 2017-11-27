#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

libPath = os.path.realpath(
    os.path.dirname(os.path.dirname(__file__))
)

fuzzpath = os.path.join(libPath, "data", "path.txt")
passwordstxt = os.path.join(libPath, "data", "passwords.txt")
