#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time


from saker.fuzzers.fuzzer import Fuzzer
from saker.utils.paths import Paths


class SQLi(Fuzzer):

    """generate SQLi payload and test"""

    def __init__(self):
        super(SQLi, self).__init__()

    @staticmethod
    def fuzz(quote=["'", '"']):
        l = []
        l.append('\\')
        l.append('"')
        l.append('")')
        l.append('a" -- +')
        l.append('a") -- +')
        l.append('a") #')
        l.append('a" or "1"="1')
        l.append('%df%27')
        l.extend(map(lambda i: i.replace('"', "'"), l))
        return l

    @classmethod
    def keyword(cls):
        with open(Paths.sqlkeywords) as keywords:
            for k in keywords:
                yield k.strip("\n")
        for k in cls.specialChars:
            yield k

    def timeInjection(self):
        pass

    def boolInjection(self):
        pass
