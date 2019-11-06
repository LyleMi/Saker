#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


from saker.utils.url import urlRelativeToAbsolute
from saker.utils.url import urlBaseDir
from saker.utils.url import urlBaseUrl
from saker.utils.url import urlFile
from saker.utils.url import normalizeUrl
from saker.utils.url import parseQuery


class UrlTest(unittest.TestCase):

    def test_urlRelativeToAbsolute(self):
        self.assertEqual(urlRelativeToAbsolute('http://example.com/../../index.php'), 'http://example.com/index.php')
        self.assertEqual(urlRelativeToAbsolute('http://example.com/a/../../index.php'), 'http://example.com/index.php')
        self.assertEqual(urlRelativeToAbsolute('http://example.com/a/../b/../index.php'), 'http://example.com/index.php')
        self.assertEqual(urlRelativeToAbsolute('http://example.com/a/../b/c/../index.php'), 'http://example.com/b/index.php')
        self.assertEqual(urlRelativeToAbsolute('http://example.com/a/../b/./c/../index.php'), 'http://example.com/b/index.php')
        self.assertEqual(urlRelativeToAbsolute('http://example.com/index/'), 'http://example.com/index/')

    def test_urlBaseDir(self):
        self.assertEqual(urlBaseDir('http://example.com/about/config/index.php'), 'http://example.com/about/config/')

    def test_urlBaseUrl(self):
        self.assertEqual(urlBaseUrl('http://example.com/about/config/index.php'), 'http://example.com')

    def test_urlFile(self):
        self.assertEqual(urlFile('http://example.com/about/config/index.php'), 'index.php')

    def test_urlFile(self):
        self.assertEqual(normalizeUrl('example.com'), 'http://example.com/')
        self.assertEqual(normalizeUrl('example.com:443'), 'https://example.com/')
        self.assertEqual(normalizeUrl('example.com:8080'), 'http://example.com:8080/')
        self.assertEqual(normalizeUrl('https://example.com:1443'), 'https://example.com:1443/')

    def test_parseQuery(self):
        self.assertEqual(parseQuery('a=1'), {'a': '1'})
        self.assertEqual(parseQuery('a=%2f'), {'a': '/'})
        self.assertEqual(parseQuery('a=%2f&b=3'), {'a': '/', 'b': '3'})
        self.assertEqual(parseQuery('a=1&b=%253'), {'a': '1', 'b': '%3'})
        self.assertEqual(parseQuery('a[]=1&b=%253'), {'a[]': '1', 'b': '%3'})
        self.assertEqual(parseQuery('a[]=1&a[]=2'), {'a[]': ['1', '2']})
        self.assertEqual(parseQuery('a=1&a=2'), {'a': ['1', '2']})


if __name__ == '__main__':
    unittest.main()
