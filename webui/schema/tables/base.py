#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
from copy import deepcopy

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import as_declarative

from schema.db import engine


@as_declarative()
class BaseTable(object):

    def toStr(self, blist=[]):
        s = deepcopy(self.__dict__)
        del(s['_sa_instance_state'])
        for i in s:
            if isinstance(s[i], datetime.datetime):
                s[i] = str(s[i])
        for b in blist:
            if b in s:
                del s[b]
        return s

    @classmethod
    def getAll(cls, toStr=False, blist=[]):
        if toStr:
            return [i.toStr(blist) for i in cls.db.query(cls).all()]
        else:
            return cls.db.query(cls).all()

    @classmethod
    def get(cls, uid):
        obj = cls.db.query(cls).filter(cls.uid == uid)
        if obj.count() < 1:
            return None
        else:
            return obj.one()

    @classmethod
    def delete(cls, uid):
        obj = cls.db.query(cls).filter(cls.uid == uid).delete()
        cls.db.commit()
        return True


def DBSession(forceNew=False):
    if hasattr(DBSession, "_db") and not forceNew:
        return DBSession._db
    # 初始化数据库
    session_factory = sessionmaker()
    session_factory.configure(bind=engine)
    BaseTable.metadata.create_all(engine)
    DBSession._db = scoped_session(session_factory)
    return DBSession._db


BaseTable.db = DBSession()
