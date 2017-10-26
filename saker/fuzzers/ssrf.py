#!/usr/bin/env python
# -*- coding: utf-8 -*-


from saker.fuzzers.fuzzer import Fuzzer


class SSRF(Fuzzer):
    """Server-Side Request Forgery"""

    def __init__(self):
        super(SSRF, self).__init__()

    @staticmethod
    def test():
        payload = ["http://127.0.0.1"]
        payload += ["http://localhost"]
        payload += ["http://sudo.cc"] # 127.0.0.1
        payload += ["http://127.0.0.1.xip.io"]
        for p in payload:
            yield p
