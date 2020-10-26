#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko

from saker.brute.brute import Brute


class SSH(Brute):

    """SSH password brute
    """

    def __init__(self, addr, port):
        super(SSH, self).__init__()
        self.addr = addr
        self.port = port

    def do(self, arg, res):

        if len(res) > 0:
            return
        user, pwd = arg
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=self.addr,
                           port=self.port,
                           username=user,
                           password=pwd,
                           timeout=20)
            res.append(arg)
            return True
        except Exception as e:
            return False
