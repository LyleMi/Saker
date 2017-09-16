#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time


from payloads.payload import Payload


class SQLi(Payload):

    """generate SQLi payload and test"""

    def __init__(self):
        super(SQLi, self).__init__()

    def fuzz(self):
        return "'\""

    def timeInjection(self):
        pass

    def boolInjection(self):
        pass
