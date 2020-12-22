#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


from saker.utils.mtime import *


class MTimeTest(unittest.TestCase):

    def test_unixtoday(self):
        print(unixtoday())

    def test_weekday(self):
        print(weekday())

    def test_str2time(self):
        self.assertEqual(
            str2time("2020-12-22 08:30:50"),
            1608597050.0
        )

    def test_time2str(self):
        self.assertEqual(time2str(1608597050), "2020-12-22 08:30:50")


if __name__ == '__main__':
    unittest.main()
