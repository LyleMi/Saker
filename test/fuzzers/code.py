#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from saker.fuzzers.code import Code


class CodeTest(unittest.TestCase):

    def test_fuzz(self):
        print([c for c in Code().fuzz()])

    def test_upper(self):
        self.assertEqual(Code.findUpper('S'), ['S', 's', 'ſ'])

    def test_lower(self):
        self.assertEqual(Code.findLower('k'), ['K', 'k', 'K'])

    def test_normalize(self):
        self.assertEqual(Code.findNormalize('a'), ['a', 'ª', 'ᵃ', 'ẚ', 'ₐ', '℀', '℁', 'ⓐ', '㏂', 'ａ'])

    def test_enconding(self):
        print([c for c in Code.fuzzEncoding('a')])

    def test_urlencode(self):
        self.assertEqual(Code.urlencode('k+=1'), 'k%2B%3D1')
        self.assertEqual(Code.urlencode('k+=1', True), '%6b%2b%3d%31')


if __name__ == '__main__':
    unittest.main()
