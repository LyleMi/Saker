#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class TypeCasting(Fuzzer):

    """TypeCasting"""

    payloads = [
        'true',
        ['true'],
        {'true': 'true'},
    ]

    def __init__(self):
        super(TypeCasting, self).__init__()

