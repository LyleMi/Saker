#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


from saker.fuzzers.sqli import SQLi


class SQLitei(SQLi):

    @classmethod
    def ascii(cls, c):
        return 'unicode(%s)' % c
