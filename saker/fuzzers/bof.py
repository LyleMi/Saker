#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class BOF(Fuzzer):

    """Buffer Overflow test"""

    def __init__(self):
        super(BOF, self).__init__()

    @classmethod
    def fuzz(cls, data=''):
        for i in range(8, 16):
            yield 'A' * (2**i)
