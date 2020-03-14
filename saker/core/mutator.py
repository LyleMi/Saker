#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from saker.fuzzers.url import URL
from saker.fuzzers.bof import BOF
from saker.fuzzers.cmdi import CmdInjection
from saker.fuzzers.code import Code
from saker.fuzzers.fileinclude import FileInclude
from saker.fuzzers.ldap import LdapInjection
from saker.fuzzers.sqli import SQLi
from saker.fuzzers.ssi import SSI
from saker.fuzzers.ssrf import SSRF
from saker.fuzzers.ssti import SSTI
from saker.fuzzers.xss import XSS
from saker.fuzzers.xxe import XXE
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

    def fuzz(
        self, part: str, key: str = '',
        vuln: str = '', interval: int = 0,
        replace: bool = False
    ):
        """fuzz request

        Args:
            part (str): fuzz part, be url/params/data/headers/cookies
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
        elif part in ['params', 'data', 'headers', 'cookies']:
            if key == '':
                return
            data = getattr(self.req, part)
            if key in data:
                original = data[key]
            else:
                original = ''
            for d in self.fuzzdata(original, vuln):
                data[key] = original + d
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
        vuln = vuln.lower().split(',')
        support = {
            'bof': BOF,
            'cmdi': CmdInjection,
            'code': Code,
            'fi': FileInclude,
            'ldap': LdapInjection,
            'sqli': SQLi,
            'ssi': SSI,
            'ssrf': SSRF,
            'ssti': SSTI,
            'xss': XSS,
            'xxe': XXE,
        }
        for k in support.keys():
            if k not in vuln and '*' not in vuln:
                continue
            o = support[k]()
            for p in o.fuzz():
                yield p
