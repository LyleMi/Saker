#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class FMTStr(Fuzzer):

    """Format String test"""

    payloads = [
        "%s",
        "%n",
        "%hhn",
        "%6$n",
        "%2044c%10$hn%38912c%11$hn"
    ]

    def __init__(self):
        super(FMTStr, self).__init__()
