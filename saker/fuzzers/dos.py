#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class DoS(Fuzzer):

    """DoS"""

    payloads = ['test']

    def __init__(self):
        super(DoS, self).__init__()

    @classmethod
    def hugeDict(cls, dictLength=100, strLength=1000):
        r = {}
        for i in range(dictLength):
            r[str(i)] = 'a' * strLength
        return r

    @classmethod
    def hugeFiles(cls, dictLength=100, strLength=1000):
        r = {}
        for i in range(dictLength):
            r[str(i)] = (str(i), 'a' * strLength)
        return r
