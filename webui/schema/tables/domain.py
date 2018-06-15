#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import and_
from sqlalchemy import Column, BOOLEAN, VARCHAR, INT
from sqlalchemy.sql import func

from schema.tables.base import BaseTable
from common.utils import guid


class Domain(BaseTable):

    __tablename__ = 'domain'

    pid = Column(VARCHAR(32), primary_key=True, default=guid)
    name = Column(VARCHAR(200))
    target = Column(VARCHAR(200))
    desc = Column(VARCHAR(1000))

    @classmethod
    def add(cls, name, target, desc):
        p = Domain()
        p.name = name
        p.target = target
        p.desc = desc
        cls.db.add(p)
        cls.db.commit()
        return True
