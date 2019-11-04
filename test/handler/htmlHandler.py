#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import requests
from saker.handler.htmlHandler import HTMLHandler


class HTMLHandlerTest(unittest.TestCase):

    def test_webpage(self):
        domain = "github.com"
        r = requests.get("https://" + domain)
        h = HTMLHandler(r.text)
        print(h.title)
        print(h.subdomains(domain))
        for link in h.links:
            if link.split(domain)[0] in ['', '//', 'http://', 'https://']:
                print(link)


if __name__ == '__main__':
    unittest.main()
