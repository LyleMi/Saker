#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string
from payloads.payload import Payload


class Misc(Payload):

    """Misc Payload"""

    def __init__(self):
        super(Misc, self).__init__()

    @staticmethod
    def randomPrintable(self, length=0):
        ret = ""
        if length == 0:
            length = random.randint(1, 100)
        for i in range(length):
            ret += random.choice(string.printable)
        return ret

    @staticmethod
    def randomStr(self, length=0):
        ret = ""
        if length == 0:
            length = random.randint(1, 100)
        for i in range(length):
            ret += chr(random.randint(0, 255))
        return ret

    @staticmethod
    def fuzzUnicode(s, type, cnt=1):
        if type == 0:
            # Greek letter
            s = s.replace("a", "α", cnt) 
        elif type == 1:
            # Russian letter 1-4
            s = s.replace("e", "е", cnt) 
        elif type == 2:
            s = s.replace("a", "а", cnt) 
        elif type == 3:
            s = s.replace("e", "ё", cnt) 
        elif type == 4:
            s = s.replace("o", "о", cnt) 
        return s

    @staticmethod
    def fuzzErrorUnicode(s):
        # https://www.leavesongs.com/PENETRATION/mysql-charset-trick.html
        return s + chr(random.randint(0xC2, 0xef))