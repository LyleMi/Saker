#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


from saker.utils.domain import cidrize
from saker.utils.domain import isIPv4


class DomainTest(unittest.TestCase):

    def test_cidrize(self):
        self.assertEqual(cidrize('127.0.0.1'), ['127.0.0.1'])

    def test_ipv4(self):
        self.assertEqual(isIPv4('127.0.0.1'), True)


if __name__ == '__main__':
    unittest.main()
