#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from saker.core.mutator import Mutator


class MutatorTest(unittest.TestCase):

    def test_mutate(self):
        options = {
            "url": "http://127.0.0.1:7777/",
            "params": {
                "test": "test"
            }
        }
        m = Mutator(options)
        # m.fuzz('url')
        # m.fuzz('params', 'test')

    def test_fuzzdata(self):
        m = Mutator({})
        test = ['bof', 'cmdi', 'code']
        for t in [test.pop()]:
            for payload in m.fuzzdata('', t):
                print(payload)


if __name__ == '__main__':
    unittest.main()
