#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/jhao104/proxy_pool

import requests


def getOne(pooladdr="http://127.0.0.1:5010"):
    r = requests.get(pooladdr + "/get/")
    return r.json().get('proxy')


def proxyOk(proxy, testbase='https://example.com'):
    try:
        r = requests.get(testbase, timeout=3, proxies={'http': proxy, 'https': proxy}, verify=False)
        print(r.text)
    except Exception as e:
        print(e)
        return False
    return True


if __name__ == '__main__':
    # main()
    proxy = getOne()
    print(proxy)
    print(proxyOk(proxy, 'https://ident.me'))
