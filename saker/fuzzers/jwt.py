#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jwt
from saker.fuzzers.fuzzer import Fuzzer


class JWT(Fuzzer):

    def __init__(self):
        super(JWT, self).__init__()

    @classmethod
    def encode(cls, data, key="", algo="HS256"):
        return jwt.encode(data, key, algo)

    @classmethod
    def encodeNone(cls, data):
        return jwt.encode(data, "", "none")
