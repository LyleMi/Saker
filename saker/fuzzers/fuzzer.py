#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string


class Fuzzer(object):

    specialChars = string.printable[62:]

    def __init__(self):
        super(Fuzzer, self).__init__()

    @staticmethod
    def randomInt(min, max):
        return random.randint(min, max)

    @staticmethod
    def randomStr(charset=string.printable, length=random.randint(1, 100)):
        return "".join([random.choice(charset) for i in range(length)])

    @staticmethod
    def randomCStr(length=random.randint(1, 100)):
        return Fuzzer.randomStr(string.letters + string.digits, length)

    @staticmethod
    def randomHex(length=random.randint(1, 100)):
        return Fuzzer.randomStr(string.hexdigits, length)

    @staticmethod
    def randomPrintable(length=random.randint(1, 100)):
        return Fuzzer.randomStr(string.printable, length)

    @staticmethod
    def randomAscii(length=random.randint(1, 100)):
        return Fuzzer.randomStr([chr(i) for i in xrange(256)], length)
