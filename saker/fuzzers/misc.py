#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string
from saker.fuzzers.fuzzer import Fuzzer


class Misc(Fuzzer):

    """Misc Payload"""

    def __init__(self):
        super(Misc, self).__init__()


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