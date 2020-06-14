#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def extractIP(content):
    ipre = r'(((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3})'
    reg = re.compile(ipre)
    datas = reg.findall(content)
    for data in datas:
        yield data


def extractPhone(content):
    phone = r'((13[0-9]|14[5-9]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8})'
    reg = re.compile(phone)
    datas = reg.findall(content)
    for data in datas:
        yield data
