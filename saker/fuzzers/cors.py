#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from saker.fuzzers.fuzzer import Fuzzer


class CORS(Fuzzer):

    """CORS"""

    def __init__(self):
        super(CORS, self).__init__()

    @staticmethod
    def test(self, url, origin=""):
        if not origin:
            origin = url
        headers = {
            "Origin": origin
        }
        r = requests.get(url, headers=headers)
        if "Access-Control-Allow-Origin" in r.headers:
            return True
        return False
