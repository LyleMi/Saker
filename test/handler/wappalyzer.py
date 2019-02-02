#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from saker.handler.wappalyzer import WebPage

class WappalyzerTest(unittest.TestCase):

    def test_webpage(self):
        web = WebPage("https://github.com")
        print(web.info())


if __name__ == '__main__':
    unittest.main()
