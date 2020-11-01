#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


from saker.utils.mtime import *


class MTimeTest(unittest.TestCase):

    def test_unixtoday(self):
        print(unixtoday())

    def test_weekday(self):
        print(weekday())


if __name__ == '__main__':
    unittest.main()
