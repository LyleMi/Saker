#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from common.sqlconfig import mysql


engine = create_engine('mysql+pymysql://%s:%s@%s/%s?charset=%s' %
                       (mysql['user'], mysql['pass'],
                        mysql['host'], mysql['db'], 'utf8'),
                       encoding='utf8', echo=False,
                       pool_size=100, pool_recycle=10)
