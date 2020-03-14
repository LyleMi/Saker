#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string


class Fuzzer(object):

    specialChars = string.printable[62:]
    payloads = []
    ints = [
        "1",
        "-1",
        "0",
        "0x1",
        "0xf",
        "01",
    ]

    def __init__(self):
        super(Fuzzer, self).__init__()

    @classmethod
    def intFuzz(cls):
        for i in cls.ints:
            yield i
        for i in range(10):
            yield 2 ** i

    @classmethod
    def randomInt(cls, min, max):
        return random.randint(min, max)

    @classmethod
    def randomStr(cls, charset=string.printable, length=random.randint(1, 100)):
        return "".join([random.choice(charset) for i in range(length)])

    @classmethod
    def randomCStr(cls, length=random.randint(1, 100)):
        return cls.randomStr(string.letters + string.digits, length)

    @classmethod
    def randomDict(cls, length=random.randint(1, 10)):
        ret = {}
        for i in range(length):
            ret[cls.randomStr()] = cls.randomStr()
        return ret

    @classmethod
    def randomHex(cls, length=random.randint(1, 100)):
        return cls.randomStr(string.hexdigits, length)

    @classmethod
    def randomPrintable(cls, length=random.randint(1, 100)):
        return cls.randomStr(string.printable, length)

    @classmethod
    def randomAscii(cls, length=random.randint(1, 100)):
        return cls.randomStr([chr(i) for i in xrange(256)], length)

    @classmethod
    def fuzz(cls):
        for p in cls.payloads:
            yield p
