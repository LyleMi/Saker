#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time


from saker.fuzzers.fuzzer import Fuzzer


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
        l.extend(map(lambda i: i.replace('"', "'"), l))
        return l

    @staticmethod
    def keyword():
        return ["@version", "@user", "@@datadir"]

    def timeInjection(self):
        pass

    def boolInjection(self):
        pass
