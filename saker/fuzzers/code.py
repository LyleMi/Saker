#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string
from urllib import quote
from saker.fuzzers.fuzzer import Fuzzer


class Code(Fuzzer):

    """Code Payload"""

    def __init__(self):
        super(Code, self).__init__()

    @staticmethod
    def fuzzAscii():
        for i in xrange(256):
            yield chr(i)

    @staticmethod
    def fuzzUnicode(cnt=1):
        for i in xrange(cnt):
            yield unichr(random.randint(0, 0xffff))

    @staticmethod
    def fuzzUnicodeReplace(s, cnt=1):
        # Greek letter
        s = s.replace("A", "Ā", cnt)
        s = s.replace("A", "Ă", cnt)
        s = s.replace("A", "Ą", cnt)
        s = s.replace("a", "α", cnt)
        # Russian letter 1-4
        s = s.replace("e", "е", cnt)
        s = s.replace("a", "а", cnt)
        s = s.replace("e", "ё", cnt)
        s = s.replace("o", "о", cnt)
        return s

    @staticmethod
    def fuzzErrorUnicode(s):
        # https://www.leavesongs.com/PENETRATION/mysql-charset-trick.html
        return s + chr(random.randint(0xC2, 0xef))

    @staticmethod
    def urlencode(s, force=False):
        if not force:
            s = quote(s)
        else:
            s = map(lambda i: hex(ord(i)).replace("0x", "%"), s)
            s = "".join(s)
        return s
