#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import unittest
from saker.port.nmap import Nmap


class NmapTest(unittest.TestCase):

    def test_scan(self):
        n = Nmap('github.com')
        n.dump()

if __name__ == '__main__':
    unittest.main()
