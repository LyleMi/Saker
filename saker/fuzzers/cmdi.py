#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fuzzers.fuzzer import Fuzzer


class CmdInjection(Fuzzer):

    """CmdInjection"""

    def __init__(self):
        super(CmdInjection, self).__init__()

    @staticmethod
    def test(self):
        return ";id"
