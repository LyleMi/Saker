#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from saker.fuzzers.url import URL
from saker.fuzzers.cmdi import CmdInjection


class Mutator(object):

    """Request Mutator
    """

    def __init__(self, req):
        """Summary
        
        Args:
            req (saker.core.Request): request object
        """
        super(Mutator, self).__init__()
        self.req = req

    def fuzz(self, part:str, key:str='', vuln:str=''):
        """fuzz request
        
        Args:
            part (str): fuzz part, be url/params/data/header/cookies
            key (str): fuzz key
            vuln (str, optional): Description
        
        Returns:
            TYPE: Description
        """
        if part == 'url':
            original = self.req.url
            for url in self.fuzzurl(original):
                self.req.url = url
                self.req.submit()
                print(url, self.req.brief())
        elif part in ['params', 'data', 'header', 'cookies']:
            if key == '':
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

    def fuzzurl(self, url:str):
        """fuzz url
        
        Args:
            url (str): url to be fuzz
        
        Yields:
            str: mutated url
        """
        for mutateUrl in URL.test(url):
            yield mutateUrl

    def fuzzdata(self, data:str, vuln:str):
        '''
        Args:
            data (str): Description
            vuln (str): Description
        
        Yields:
            TYPE: Description
        
        '''
        vuln = vuln.split(',')
        if 'cmdi' == vuln:
            for c in CmdInjection.test():
                yield data + c
        else:
            yield data
