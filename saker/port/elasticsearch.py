#!/usr/bin/env python
# -*- coding:utf-8 -*-


import requests


class elasticsearchDetect(object):

    def __init__(self):
        super(elasticsearchDetect, self).__init__()
        self.name = "elasticsearchDetect"

    def run(self, ip, port=9200, timeout=5):
        url = 'http://%s:%d/_cat' % (ip, port)
        r = requests.get(url, timeout=timeout)
        if '/_cat/master' in r.content:
            return True
        return False


if __name__ == '__main__':
    pass
