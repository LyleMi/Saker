#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class Password(Fuzzer):

    """Password"""

    pwdlist = [
        "{username}321",
        "{username}521",
        "{username}2016",
        "{username}2017",
        "{username}123!",
        "{username}1!",
        "{username}2@",
        "{username}3#",
        "{username}123!@#",
        "{username}123#@!",
        "{username}123$%^",
        "{username}!@#456",
        "{username}123",
        "{username}123qwe",
        "{username}qwe123",
        "{username}qwe",
        "{username}1234",
        "{username}12345",
        "{username}123456",
        "123456",
        "password",
        "12345678",
        "qwerty",
        "123456789",
        "111111",
        "1234567",
    ]

    def __init__(self):
        super(Password, self).__init__()

    @classmethod
    def fuzz(cls, username=''):
        info = {
            "username": username
        }
        for p in cls.pwdlist:
            yield p.format(**info)
