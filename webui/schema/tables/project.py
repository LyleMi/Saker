#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import and_
from sqlalchemy import Column, BOOLEAN, VARCHAR, INT
from sqlalchemy.sql import func

from schema.tables.base import BaseTable


class Project(BaseTable):

    __tablename__ = 'project'

    pid = Column(INT, primary_key=True)
    name = Column(VARCHAR(200))
    domain = Column(VARCHAR(200))
    desc = Column(VARCHAR(10))

    @classmethod
    def add(cls, db, name, domain, desc):
        p = Project()
        p.name = name
        p.domain = domain
        p.desc = desc
        db.add(p)
        db.commit()
        return True

