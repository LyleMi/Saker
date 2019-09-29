#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


from saker.fuzzers.sqli import SQLi


class PostgreSQLi(SQLi):

    @classmethod
    def char(cls, c):
        return 'char(%s)' % c

    @classmethod
    def ascii(cls, c):
        return 'ascii(%s)' % c
