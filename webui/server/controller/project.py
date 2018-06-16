#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
from server.controller.base import BaseHandler
from schema.tables.project import Project


class ProjectHandler(BaseHandler):

    def get(self):
        self.render("index.html")

    def post(self):
        name = self.get_argument('name', '')
        if not name:
            return self.error(200, "name is required")
        target = self.get_argument('target', '')
        if not target:
            return self.error(200, "target is required")
        desc = self.get_argument('desc', '')
        if not desc:
            return self.error(200, "desc is required")
        o = Project.add(name, target, desc)
        return self.ok("suc")
