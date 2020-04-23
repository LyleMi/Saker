#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from saker.fuzzers.password import Password


class PasswordTest(unittest.TestCase):

    def test_fuzz(self):
        print([p for p in Password().fuzz('uname')])

if __name__ == '__main__':
    unittest.main()
