#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from saker.fuzzers.fuzzer import Fuzzer


class Nginx(Fuzzer):

    # nginx off by slash
    @staticmethod
    def slash(url, file, static='static'):
        url = url.sgtrip("/")
        first = requests.get(url + "/" + file)
        second = requests.get(url + "../" + static + "/" + file)
        if first.status_code == 200 and second.status_code == 200:
            return True
        return Fals
