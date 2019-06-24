#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class Template(Fuzzer):

    """Template"""

    payloads = ['test']

    def __init__(self):
        super(Template, self).__init__()
