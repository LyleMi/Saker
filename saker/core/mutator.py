#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from saker.fuzzers.url import URL
from saker.fuzzers.cmdi import CmdInjection


class Mutator(object):

    """Request Mutator

    Attributes:
        cookies (TYPE): Description
        data (TYPE): Description
        headers (TYPE): Description
        method (TYPE): Description
        params (TYPE): Description
        sess (TYPE): Description
        url (TYPE): Description
    """

    def __init__(self, req):
        """Summary

        Args:
            sess (requests.sessions.Session): request Session
            options (saker.core.Request): request object
        """
        super(Mutator, self).__init__()
        self.req = req

    def fuzz(self, part, key=None, vuln=''):
        """fuzz request

        Args:
            part (TYPE): fuzz part
            key (TYPE): fuzz key
        """
        if part == 'url':
            original = self.req.url
            for url in self.fuzzurl(original):
                self.req.url = url
                self.req.submit()
                print(url, self.req.brief())
        elif part in ['params', 'data', 'header', 'cookies']:
            if key is None:
                return
            data = getattr(self.req, part)
            if key in data:
                original = data[key]
            else:
                original = ''
            for d in self.fuzzdata(original, vuln):
                getattr(self.req, part)[key] = d
                self.req.submit()
                print(repr(d) + '\t' + self.req.brief())

    def fuzzurl(self, url):
        for mutateUrl in URL.test(url):
            yield mutateUrl

    def fuzzdata(self, data, vuln):
        if vuln == 'cmdi':
            for c in CmdInjection.test():
                yield data + c
        else:
            yield data
