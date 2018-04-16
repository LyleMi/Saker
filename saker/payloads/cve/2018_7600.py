#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PoC of CVE-2018-7600
"""

import requests


class Exploit(object):

    def __init__(self):
        """init
        """
        super(Exploit, self).__init__()

    def poc(self, url):
        # TODO
        pass


if __name__ == '__main__':
    e = Exploit()
    e.poc("http://172.18.108.215:8000/")
