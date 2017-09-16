#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string
from payloads.payload import Payload


class Misc(Payload):

    """Misc Payload"""

    def __init__(self):
        super(Misc, self).__init__()

    def randomPrintable(self, length=0):
        ret = ""
        if length == 0:
            length = random.randint(1, 100)
        for i in range(length):
            ret += random.choice(string.printable)
        return ret

    def randomStr(self, length=0):
        ret = ""
        if length == 0:
            length = random.randint(1, 100)
        for i in range(length):
            ret += chr(random.randint(0, 255))
        return ret
