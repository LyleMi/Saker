#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string


class Fuzzer(object):

    specialChars = string.printable[62:]

    def __init__(self):
        super(Fuzzer, self).__init__()

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
