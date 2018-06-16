#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import and_
from sqlalchemy import Column, BOOLEAN, VARCHAR, INT
from sqlalchemy.sql import func

from schema.tables.base import BaseTable
from common.utils import guid


class Asset(BaseTable):

    __tablename__ = 'asset'

    uid = Column(VARCHAR(32), primary_key=True, default=guid)
    pid = Column(VARCHAR(32))
    atype = Column(VARCHAR(200))
    data = Column(VARCHAR(200))
    desc = Column(VARCHAR(1000))

    @classmethod
    def add(cls, name, target, desc):
        o = Asset()
        o.name = name
        o.target = target
        o.desc = desc
        cls.db.add(o)
        cls.db.commit()
        return True
