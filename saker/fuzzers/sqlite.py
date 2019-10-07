#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


from saker.fuzzers.sqli import SQLi


class SQLitei(SQLi):

    @classmethod
    def ascii(cls, c):
        return 'unicode(%s)' % c

    @classmethod
    def version(cls):
        return 'sqlite_version()'

    @classmethod
    def info(cls):
        return 'SELECT * FROM sqlite_master'

    @classmethod
    def offset(limit, offset):
        return 'limit %s offset %s' % (limit, offset)
