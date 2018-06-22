#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymongo


class mongoDetect(object):

    def __init__(self):
        super(mongoDetect, self).__init__()
        self.name = "mongoDetect"

    def run(self, ip, port=27017):
        try:
            conn = pymongo.MongoClient(ip, port)
            dbname = conn.database_names()
            return True
        except pymongo.errors.ServerSelectionTimeoutError as e:
            return False


if __name__ == '__main__':
    pass
