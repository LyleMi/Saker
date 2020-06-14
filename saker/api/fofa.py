#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

from saker.utils.encode import b64e


class Fofa(object):

    url = "https://fofa.so/api/"

    def __init__(self, email, key):
        super(Fofa, self).__init__()
        self.s = requests.Session()
        self.email = email
        self.key = key

    def search(self, query, page=1, size=100, full="false"):
        qbase64 = b64e(query)
        api = "v1/search/all"
        params = {
            "qbase64": qbase64,
            "page": page,
            "size": size,
            "full": full,
            "email": self.email,
            "key": self.key,
        }
        r = self.s.get(self.url + api, params=params)
        data = json.loads(r.text)
        return data
