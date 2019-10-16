#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from saker.fuzzers.fileinclude import FileInclude


class FileIncludeTest(unittest.TestCase):

    def test_parent(self):
        o = FileInclude()
        self.assertEqual(o.parent('/var/www/html/index.php'), '/var/www/html')

    def test_fuzz(self):
        o = FileInclude()
        for i in o.fuzz():
            print(i)

    def test_proc(self):
        o = FileInclude()
        for i in o.proc(maxpid=3, maxfd=3):
            print(i)
        for i in o.proc(maxpid=1, maxfd=1):
            print(i)


if __name__ == '__main__':
    unittest.main()
