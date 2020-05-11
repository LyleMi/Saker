#!/usr/bin/env python
# -*- coding:utf-8 -*-
# https://github.com/AlienVault-OTX/ApiV2
# Please limit all requests to no more than one request every ten seconds.

import re
import json
import requests


class Threatcrowd(object):

    url = "https://www.threatcrowd.org"

    def __init__(self):
        super(Threatcrowd, self).__init__()
        self.s = requests.Session()

    def domainReport(self, domain):
        api = "/searchApi/v2/domain/report/"
        params = {
            "domain": domain
        }
        r = self.s.get(self.url + api, params=params)
        # print(r.status_code)
        # print(r.text)
        data = json.loads(r.text)
        data = data.get("subdomains", [])
        return data

    def ipReport(self, ip):
        api = "/searchApi/v2/ip/report/"
        params = {
            "ip": ip
        }
        r = self.s.get(self.url + api, params=params)
        # print(r.status_code)
        # print(r.text)
        data = json.loads(r.text)
        return data
