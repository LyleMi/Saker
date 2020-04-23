#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from saker.utils.flaskencoder import FlaskEncoder


class FlaskEncoderTest(unittest.TestCase):

    def test_decode(self):
        fe = FlaskEncoder()
        cookie = 'InRlc3QgY29va2llIg.XqGdsQ.sTvgJniGlc-4-MMAOaak4oTuhKE'
        print(fe.decode(cookie))

    def test_encode(self):
        fe = FlaskEncoder('test key')
        cookie = 'test cookie'
        print(fe.encode(cookie))


if __name__ == '__main__':
    unittest.main()
