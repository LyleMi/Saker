#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.brute.brute import Brute
from saker.utils.domain import domain2ips


class Domain(Brute):
    """subdomain brute"""

    def __init__(self, domain):
        super(Domain, self).__init__()
        self.domain = domain

    def do(self, arg, res):
        if len(domain2ips(domain + "." + arg)) == 0:
            return False
        res.append(arg)
        return True
