#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


class Fuzzer(object):

    def __init__(self):
        super(Fuzzer, self).__init__()

    @staticmethod
    def generateInt(min, max):
        return random.randint(min, max)

    @staticmethod
    def randomPrintable(length=0):
        ret = ""
        if length == 0:
            length = random.randint(1, 100)
        for i in range(length):
            ret += random.choice(string.printable)
        return ret

    @staticmethod
    def randomStr(length=0):
        ret = ""
        if length == 0:
            length = random.randint(1, 100)
        for i in range(length):
            ret += chr(random.randint(0, 255))
        return ret
