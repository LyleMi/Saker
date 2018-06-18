#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import and_
from sqlalchemy import Column, BOOLEAN, VARCHAR, INT, TIMESTAMP
from sqlalchemy.sql import func

from schema.tables.base import BaseTable
from common.utils import guid
from common.utils import now


class Application(BaseTable):

    __tablename__ = 'application'

    uid = Column(VARCHAR(32), primary_key=True, default=guid)
    pid = Column(VARCHAR(32))
    data = Column(VARCHAR(100))
    desc = Column(VARCHAR(1000))
    created = Column(TIMESTAMP, default=now)

    @classmethod
    def add(cls, name, target, desc):
        o = cls()
        o.name = name
        o.target = target
        o.desc = desc
        cls.db.add(o)
        cls.db.commit()
        return True
