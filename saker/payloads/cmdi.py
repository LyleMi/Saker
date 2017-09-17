#!/usr/bin/env python
# -*- coding: utf-8 -*-

from payloads.payload import Payload


class CmdInjection(Payload):

    """CmdInjection"""

    def __init__(self):
        super(CmdInjection, self).__init__()

    @staticmethod
    def test(self):
        return ";id"
