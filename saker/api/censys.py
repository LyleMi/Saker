#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import requests


class Censys(object):

    url = "https://www.censys.io/api/v1"

    def __init__(self, uid=None, secret=None):
        self.uid = uid or os.environ.get("CENSYS_UID", None)
        self.secret = secret or os.environ.get("CENSYS_SECRET", None)
        if not self.uid or not self.secret:
            raise Exception("No API ID or secret configured.")
        self.s = requests.Session()
        self.s.auth = (self.uid, self.secret)

    def search(self, ip):
        api = '/search/ipv4'
        page = 1
        data = {
            'query': ip,
            'page': page
        }
        r = self.s.post(self.url + api, json=data)
        data = r.json()
        return data

    def view(self, addr):
        api = '/view/ipv4/%s'
        api = api % addr
        r = self.s.get(self.url + api)
        data = r.json()
        return data
