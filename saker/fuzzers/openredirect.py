#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class OpenRedirect(Fuzzer):

    """Open Redirect"""

    special = [
        "\\\\",
        "\\",
        r"%EF%BC%BC",
        r'%0A',
        r'%0D',
        r'%20',
        ".",
        ":",
        "@",
        "../",
        "../;",
        "./;",
        r"%2e%2e",
    ]

    def __init__(self):
        super(OpenRedirect, self).__init__()
