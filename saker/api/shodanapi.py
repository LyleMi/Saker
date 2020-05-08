#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pip install shodan
# https://shodan.readthedocs.io

import shodan


class ShodanAPI(object):

    def __init__(self, token):
        super(ShodanAPI, self).__init__()
        self.api = shodan.Shodan(token)

    def search(self, query, page=1, facets=None):
        self.api.search(query, page=page, facets=facets)

    def scan(self, ips, force=False):
        self.api.scan(ips, force=force)
