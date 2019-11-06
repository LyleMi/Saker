#!/usr/bin/env python
# -*- coding: utf-8 -*-
# REST API from lib/utils/api.py
# options from lib/core/optiondict.py

from saker.core.sess import Sess


class SQLmap(Sess):

    def __init__(self, url="http://127.0.0.1:8775", adminid=""):
        super(SQLmap, self).__init__(url)
        self.adminid = adminid

    def scan(self, options):
        taskid = self.new()
        # self.set(taskid, options)
        self.start(taskid, options)
        print(self.status(taskid).json())
        return taskid

    def new(self):
        self.get('task/new')
        taskid = self.lastr.json()['taskid']
        return taskid

    def delete(self, taskid):
        self.get('task/%s/delete' % taskid)

    def start(self, taskid, options):
        '''
        options:
            url
            method
            data
            skip
        '''
        self.post('scan/%s/start' % taskid, json=options)

    def stop(self, taskid):
        self.get('scan/%s/stop' % taskid)
        return self.lastr

    def status(self, taskid):
        self.get('scan/%s/status' % taskid)
        return self.lastr

    def result(self, taskid):
        self.get('scan/%s/data' % taskid)
        return self.lastr

    def set(self, taskid, options):
        self.post('option/%s/set' % taskid, json=options)
