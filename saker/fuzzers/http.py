#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer

_status_code = {
    301: "HTTP/1.1 301 Moved Permanently",
    302: "HTTP/1.1 302 Found",
    303: "HTTP/1.1 303 See Other",
    307: "HTTP/1.1 307 Temporary Redirect",
}


class HTTPInjection(Fuzzer):

    """HTTPInjection"""

    def __init__(self):
        super(HTTPInjection, self).__init__()
