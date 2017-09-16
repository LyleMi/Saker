#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

libPath = os.path.realpath(
    os.path.dirname(os.path.dirname(__file__))
)

fuzztxt = os.path.join(libPath, "data", "fuzz.txt")
