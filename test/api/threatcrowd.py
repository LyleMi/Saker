#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import unittest

from saker.api.threatcrowd import Threatcrowd


class ThreatcrowdTest(unittest.TestCase):

    def test_domain(self):
        domain = 'example.com'
        result = Threatcrowd.domainReport(domain)


if __name__ == '__main__':
    unittest.main()
