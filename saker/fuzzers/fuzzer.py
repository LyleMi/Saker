#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import string
import bisect


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

    empty = [
        "\x09",
        "\x0a",
        "\x0c",
        "\x20",
    ]

    space = [
        " ",
        "\t",
    ]

    r = random
    choice = random.choice

    def __init__(self):
        super(Fuzzer, self).__init__()

    @classmethod
    def int(cls):
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
    def randomBytes(cls, length=random.randint(1, 100)):
        return os.urandom(length)

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
        return cls.randomStr([chr(i) for i in range(256)], length)

    @classmethod
    def weightRandom(cls, weight):
        sumList = []
        weightSum = 0
        for w in weight:
            weightSum += w
            sumList.append(weightSum)
        pick = random.randint(0, weightSum - 1)
        return bisect.bisect_right(sumList, pick)

    @classmethod
    def fuzz(cls):
        for p in cls.payloads:
            yield p
