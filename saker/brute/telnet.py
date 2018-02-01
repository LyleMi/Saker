#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telnetlib

from saker.brute.brute import Brute


class Telnet(Brute):

    """Telnet password brute
    """

    def __init__(self, addr, port):
        super(Telnet, self).__init__()
        self.addr = addr
        self.port = port

    def do(self, arg, res):

        if len(res) > 0:
            return
        user, pwd = arg
        try:
            tn = telnetlib.Telnet(host=self.addr, port=self.port)
            tn.read_until("login: ")
            tn.write(user + "\n")
            if pwd:
                tn.read_until("Password: ")
                tn.write(pwd + "\n")
            tn.write("ls\n")
            tn.write("exit\n")
            tn.read_all()
            tn.close()
            res.append(arg)
            return True
        except Exception as e:
            # print(e)
            return False
