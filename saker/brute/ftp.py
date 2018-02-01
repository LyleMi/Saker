#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ftplib

from saker.brute.brute import Brute


class FTP(Brute):

    """FTP password brute
    """

    def __init__(self, addr, port):
        super(FTP, self).__init__()
        self.addr = addr
        self.port = port

    def testAnonymous(self):
        ftp = ftplib.FTP()
        ftp.connect(self.addr, self.port)
        ftp.login()
        ftp.retrlines('LIST')
        ftp.quit()
        return True

    def do(self, arg, res):

        if len(res) > 0:
            return
        user, pwd = arg
        try:
            ftp = ftplib.FTP()
            ftp.connect(self.addr, self.port)
            ftp.login(user, pwd)
            ftp.retrlines('LIST')
            ftp.quit()
            res.append(arg)
            return True
        except (ftplib.all_errors) as msg:
            return False
