#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class OpenRedirect(Fuzzer):

    """Open Redirect"""

    def __init__(self):
        super(OpenRedirect, self).__init__()
