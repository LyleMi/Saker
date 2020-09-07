#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
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

    @classmethod
    def slowWrite(cls, conn, req, interval):
        for b in req:
            conn.send(b.to_bytes(length=1, byteorder="little"))
            time.sleep(interval)

    @classmethod
    def slowRead(cls, conn, interval):
        while True:
            conn.recv(1)
            time.sleep(interval)
