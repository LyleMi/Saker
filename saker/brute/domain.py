#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dns.resolver

from saker.brute.brute import Brute
from saker.utils.paths import Paths


class Domain(Brute):

    """subdomain brute"""

    def __init__(self, domain):
        super(Domain, self).__init__()
        self.domain = domain
        self.resolvers = [dns.resolver.Resolver(configure=False) for _ in range(self.cpuCount)]
        for _r in self.resolvers:
            _r.lifetime = _r.timeout = 6.0

    def feedDomain(self, main, level):
        with open(Paths.subnames, "rb") as fh:
            for subname in fh:
                self.feed(subname.strip() + "." + main)

    def run(self, func=None):
        self.processes = [
            Process(
                target=self.do,
                args=(func, )
            )
            for i in range(num)
        ]
        for p in self.processes:
            p.start()

    def do(self, func=None):
        try:
            answers = self.resolvers[j].query(cur_sub_domain)
        except dns.resolver.NoAnswer as e:
            pass
        if func is not None:
            func(answers)
        return True


if __name__ == '__main__':
    d = Domain("github.com")

