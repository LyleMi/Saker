#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from saker.utils.logger import getLogger


class LoggerTest(unittest.TestCase):

    def test_commandHandler(self):
        logger = getLogger("test1")
        logger.info("test command handler")

    def test_fileHandler(self):
        logpath = "test.log"
        logger = getLogger("test2", logpath=logpath)
        logger.info("test command handler")
        for handler in logger.handlers:
            handler.close()
        os.unlink(logpath)


if __name__ == '__main__':
    unittest.main()
