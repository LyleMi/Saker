#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from saker.fuzzers.url import URL
from saker.fuzzers.bof import BOF
from saker.fuzzers.cmdi import CmdInjection
from saker.fuzzers.code import Code
from saker.core.request import Request


class Mutator(object):

    """Request Mutator
    """

    def __init__(self, req):
        """Summary

        Args:
            req (saker.core.Request): request object
        """
        super(Mutator, self).__init__()
        if isinstance(req, dict):
            self.req = Request(req)
        elif isinstance(req, Request):
            self.req = req

    def fuzz(self, part: str, key: str = '', vuln: str = '', interval: int = -1):
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
                print(url, self.req.brief(), self.req.lastr.url)
                time.sleep(interval)
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
                time.sleep(interval)

    def fuzzurl(self, url: str):
        """fuzz url

        Args:
            url (str): url to be fuzz

        Yields:
            str: mutated url
        """
        for mutateUrl in URL.fuzz(url):
            yield mutateUrl

    def fuzzdata(self, data: str, vuln: str):
        '''
        Args:
            data (str): Description
            vuln (str): Description

        Yields:
            TYPE: Description

        '''
        vuln = vuln.split(',')
        if 'bof' in vuln or '*' in vuln:
            for p in BOF.fuzz():
                yield data + p
        if 'cmdi' in vuln or '*' in vuln:
            for p in CmdInjection.fuzz():
                yield data + p
        if 'code' in vuln or '*' in vuln:
            C = Code()
            for p in C.fuzz():
                yield data + p
