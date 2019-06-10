#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string
from urllib.parse import quote
from unicodedata import normalize
from saker.fuzzers.fuzzer import Fuzzer


class Code(Fuzzer):

    """Code Payload"""

    homograph = {
        'a': '\u0430',
        'c': '\u03F2',
        'd': '\u0501',
        'e': '\u0435',
        'h': '\u04BB',
        'i': '\u0456',
        'j': '\u0458',
        'l': '\u04CF',
        'o': '\u043E',
        'p': '\u0440',
        'r': '\u0433',
        'q': '\u051B',
        's': '\u0455',
        'w': '\u051D',
        'x': '\u0445',
        'y': '\u0443',
    }

    fuzzencodings = ['IBM-Thai', 'IBM00924', 'IBM01047', 'IBM01140', 'IBM01141', 'IBM01142', 'IBM01143', 'IBM01144', 'IBM01145', 'IBM01146', 'IBM01147', 'IBM01148', 'IBM01149', 'IBM037', 'IBM1026', 'IBM273', 'IBM277', 'IBM278', 'IBM280', 'IBM284', 'IBM285', 'IBM290', 'IBM297', 'IBM420', 'IBM423', 'IBM424', 'IBM500', 'IBM870', 'IBM871', 'IBM880', 'IBM905', 'cp1025', 'cp875', 'unicodeFFFE', 'utf-16', 'utf-32', 'utf-32BE', 'x-EBCDIC-KoreanExtended']

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

    @staticmethod
    def findUpper(dst):
        return list(filter(lambda i: i.upper() == dst, map(chr, range(1, 0x10000))))

    @staticmethod
    def findLower(dst):
        return list(filter(lambda i: i.lower() == dst, map(chr, range(1, 0x10000))))

    @staticmethod
    def findNormalize(dst, form='NFKC'):
        # form should in ['NFC', 'NFKC', 'NFD', 'NFKD']
        return list(filter(lambda i: normalize(form, i)[0] == dst, map(chr, range(1, 0x10000))))
