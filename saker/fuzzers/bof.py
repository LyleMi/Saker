#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class BOF(Fuzzer):

    """Buffer Overflow test"""

    payloads = [
        'A' * 1024,
        'A' * 2048,
        'A' * 4096,
        'A' * 8192,
    ]

    def __init__(self):
        super(BOF, self).__init__()
