#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from saker.brute.brute import Brute


class BasicAuth(Brute):

    '''brute test for http basic auth
    '''

    def __init__(self, url):
        super(BasicAuth, self).__init__()
        self.url = url

    def do(self, arg, res):
        # todo
        if len(res) > 0:
            return
        user, pwd = arg
        r = requests.get(self.url, auth=(user, pwd))
        res.append(arg)
