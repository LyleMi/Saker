#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from saker.core.request import Request
from saker.core.mutator import Mutator


class MutatorTest(unittest.TestCase):

    def test_mutate(self):
        options = {
            "url": "http://127.0.0.1:7777/"
        }
        r = Request(options=options)
        m = Mutator(r)
        m.fuzz('url')
        m.fuzz('params', 'test')


if __name__ == '__main__':
    unittest.main()
