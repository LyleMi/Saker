#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


from saker.utils.domain import cidrize
from saker.utils.domain import isIPv4


class DomainTest(unittest.TestCase):

    def test_cidrize(self):
        self.assertEqual(cidrize('127.0.0.1'), ['127.0.0.1'])
        self.assertEqual(
            set(cidrize('127.0.0.1,8.8.8.8')),
            set(['127.0.0.1', '8.8.8.8'])
        )
        self.assertEqual(
            set(cidrize('192.168.1.11-192.168.1.15')),
            set(['192.168.1.11', '192.168.1.12', '192.168.1.13', '192.168.1.14', '192.168.1.15'])
        )
        self.assertEqual(
            set(cidrize('192.168.1.11-15')),
            set(['192.168.1.11', '192.168.1.12', '192.168.1.13', '192.168.1.14', '192.168.1.15'])
        )
        self.assertEqual(
            set(cidrize('192.168.11-15.1')),
            set(['192.168.11.1', '192.168.12.1', '192.168.13.1', '192.168.14.1', '192.168.15.1'])
        )
        self.assertEqual(
            set(cidrize('192.168.1.1[1-5]')),
            set(['192.168.1.11', '192.168.1.12', '192.168.1.13', '192.168.1.14', '192.168.1.15'])
        )
        self.assertEqual(
            set(cidrize('192.168.1.1[12345]')),
            set(['192.168.1.11', '192.168.1.12', '192.168.1.13', '192.168.1.14', '192.168.1.15'])
        )
        self.assertEqual(
            set(cidrize('192.168.1.1/30')),
            set(['192.168.1.0', '192.168.1.1', '192.168.1.2', '192.168.1.3'])
        )

    def test_ipv4(self):
        self.assertEqual(isIPv4('127.0.0.1'), True)


if __name__ == '__main__':
    unittest.main()
