#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import requests


def DNSdumpster(domain):
    """使用DNSdumpster API获取子域名信息"""
    target = "https://dnsdumpster.com/"
    headers = {
        'Referer': target
    }
    timeout = 60
    s = requests.Session()

    try:
        r = s.get(target, headers=headers, timeout=timeout)
    except requests.exceptions.Timeout as e:
        return False, "timeout"

    csrftoken = r.cookies.get('csrftoken')
    data = {
        "csrfmiddlewaretoken": csrftoken,
        "targetip": domain
    }

    try:
        req = s.post(target, data=data, headers=headers, timeout=timeout)
    except requests.exceptions.Timeout as e:
        return False, "timeout"

    if req.status_code != 200:
        return False, "dnsdumpster return a %d" % req.status_code

    regRel = re.compile('[a-zA-Z0-9\-\.]+\.' + domain, re.IGNORECASE)
    domains = regRel.findall(req.content)

    if not domains:
        return False, "no result"

    return True, list(set(domains))

if __name__ == '__main__':
    print DNSdumpster("baidu.com")
