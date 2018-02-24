#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

from schema.db import engine
from schema.tables.base import BaseTable

def initDB():
    # 初始化数据库
    session_factory = sessionmaker()
    session_factory.configure(bind=engine)
    BaseTable.metadata.create_all(engine)
    return scoped_session(session_factory)
