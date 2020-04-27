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

    @classmethod
    def domainReport(cls, domain):
        api = "/searchApi/v2/domain/report/"
        params = {
            "domain": domain
        }
        r = requests.get(cls.url + api, params=params)
        data = json.loads(r.text)
        data = data["subdomains"]
        return data
