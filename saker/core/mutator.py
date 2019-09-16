#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.url import URL


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

    def fuzz(self, fuzzpart, fuzzkey=None):
        """fuzz request

        Args:
            fuzzpart (TYPE): fuzz part
            fuzzkey (TYPE): fuzz key
        """
        if fuzzpart == 'url':
            original = self.req.url
            for url in self.fuzzurl(original):
                self.req.url = url
                self.req.submit()
                print(url, self.req.brief())
        elif fuzzpart in ['params', 'data', 'header', 'cookies']:
            if fuzzkey is None:
                return
            data = getattr(self.req, fuzzpart)
            if fuzzkey in data:
                original = data[fuzzkey]
            else:
                original = ''
            for d in self.fuzzdata(original):
                getattr(self.req, fuzzpart)[fuzzkey] = d
                self.req.submit()
                print(d, self.req.brief())

    def fuzzurl(self, url):
        for mutateUrl in URL.test(url):
            yield mutateUrl

    def fuzzdata(self, data):
        yield data
