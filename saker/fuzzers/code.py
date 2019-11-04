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

    # https://docs.python.org/3/library/codecs.html
    # cpython/Lib/encodings
    encodings = [
        'cp1251',
        'cp775',
        'cp869',
        'hp_roman8',
        'iso8859_14',
        'koi8_u',
        'oem',
        'utf_16_be',
        'cp1252',
        'cp850',
        'cp874',
        'hz',
        'iso8859_15',
        'kz1048',
        'palmos',
        'utf_16_le',
        'ascii',
        'cp1253',
        'cp852',
        'cp875',
        'idna',
        'iso8859_16',
        'latin_1',
        'ptcp154',
        'utf_32',
        'cp1254',
        'cp855',
        'cp932',
        'iso2022_jp',
        'iso8859_2',
        'mac_arabic',
        'punycode',
        'utf_32_be',
        'big5',
        'cp1255',
        'cp856',
        'cp949',
        'iso2022_jp_1',
        'iso8859_3',
        'mac_croatian',
        'utf_32_le',
        'big5hkscs',
        'cp1256',
        'cp857',
        'cp950',
        'iso2022_jp_2',
        'iso8859_4',
        'mac_cyrillic',
        'raw_unicode_escape',
        'utf_7',
        'cp1257',
        'cp858',
        'euc_jis_2004',
        'iso2022_jp_2004',
        'iso8859_5',
        'mac_farsi',
        'utf_8',
        'charmap',
        'cp1258',
        'cp860',
        'euc_jisx0213',
        'iso2022_jp_3',
        'iso8859_6',
        'mac_greek',
        'shift_jis',
        'utf_8_sig',
        'cp037',
        'cp273',
        'cp861',
        'euc_jp',
        'iso2022_jp_ext',
        'iso8859_7',
        'mac_iceland',
        'shift_jis_2004',
        'cp1006',
        'cp424',
        'cp862',
        'euc_kr',
        'iso2022_kr',
        'iso8859_8',
        'mac_latin2',
        'shift_jisx0213',
        'cp1026',
        'cp437',
        'cp863',
        'gb18030',
        'iso8859_1',
        'iso8859_9',
        'mac_roman',
        'tis_620',
        'cp1125',
        'cp500',
        'cp864',
        'gb2312',
        'iso8859_10',
        'johab',
        'mac_romanian',
        'cp1140',
        'cp720',
        'cp865',
        'gbk',
        'iso8859_11',
        'koi8_r',
        'mac_turkish',
        'unicode_escape',
        'cp1250',
        'cp737',
        'cp866',
        'iso8859_13',
        'koi8_t',
        'mbcs',
        'utf_16'
    ]

    def __init__(self):
        super(Code, self).__init__()

    @staticmethod
    def fuzzAscii():
        for i in range(256):
            yield chr(i)

    @staticmethod
    def fuzzUnicode(cnt: int = 1):
        for i in range(cnt):
            yield chr(random.randint(0, 0xffff))

    @staticmethod
    def fuzzUnicodeReplace(s: str, cnt: int = 1):
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
    def fuzzErrorUnicode(s: str):
        # https://www.leavesongs.com/PENETRATION/mysql-charset-trick.html
        return s + chr(random.randint(0xC2, 0xef))

    @staticmethod
    def urlencode(s: str, force: bool = False):
        if not force:
            s = quote(s)
        else:
            s = "".join(map(lambda i: hex(ord(i)).replace("0x", "%"), s))
        return s

    @staticmethod
    def urlutf8encode(s: str):
        return "".join(map(lambda i: hex(ord(i)).replace("0x", "%00"), s))

    @staticmethod
    def findUpper(dst: str):
        return list(filter(lambda i: i.upper() == dst, map(chr, range(1, 0x10000))))

    @staticmethod
    def findLower(dst: str):
        return list(filter(lambda i: i.lower() == dst, map(chr, range(1, 0x10000))))

    @staticmethod
    def findNormalize(dst: str, form: str = 'NFKC'):
        # form should in ['NFC', 'NFKC', 'NFD', 'NFKD']
        return list(filter(lambda i: normalize(form, i)[0] == dst, map(chr, range(1, 0x10000))))

    @classmethod
    def fuzzEncoding(cls, dst: str):
        for encoding in cls.encodings:
            yield dst.encode(encoding)

    def fuzz(self, level: int = 1):
        yield ''
        for c in self.fuzzAscii():
            yield c
        if level > 1:
            for c in self.fuzzUnicode():
                yield c
