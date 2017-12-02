#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class BasicAuth(object):

    '''
    brute test for http basic auth
    '''

    def __init__(self, url):
        super(BasicAuth, self).__init__()
        self.url = url

    def do(self, args, res):
        # todo
        if len(res) > 0:
            return
        user, pwd = arg
        r = requests.get(self.url, auth=(user, pwd))
        res.append(arg)
