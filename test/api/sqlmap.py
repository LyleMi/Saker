#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import unittest

from saker.api.sqlmap import SQLmap


class SQLmapTest(unittest.TestCase):

    def test_scan(self):
        options = {
            'url': 'http://127.0.0.1:7788/?user=a&pass=a',
            'method': 'post',
            'data': 'a=1&b=2',
            'skip': 'pass',
            'dbms': 'mysql',
        }
        s = SQLmap()
        taskid = s.scan(options)
        print(taskid)
        time.sleep(5)
        print(s.status(taskid).json())
        print(s.result(taskid).json())


if __name__ == '__main__':
    unittest.main()
