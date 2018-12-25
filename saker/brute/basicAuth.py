#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from saker.brute.brute import Brute


class BasicAuth(Brute):

    '''brute test for http basic auth
    '''

    def __init__(self, url):
        super(BasicAuth, self).__init__()
        self.url = url

    def do(self):
        if len(self.res) > 0:
            return
        user, pwd = self.queue.get()
        r = requests.get(self.url, auth=(user, pwd))
        if self.check(r):
            self.res.append([user, pwd])

    @staticmethod
    def check(self, r):
        # overwrite this line if needed
        return r.status_code == 200

    def autorun(self):
        from saker.utils.paths import Paths
        self.run()
        with open(Paths.usernames, 'rb') as fh:
            with open(Paths.passwords, 'rb') as fh:
                for user in fh:
                    for pwd in fh:
                        self.feed([user.strip('\n'), pwd.strip('\n')])
        print(self.finish())


if __name__ == '__main__':
    url = 'http://127.0.0.1/auth'
    b = BasicAuth(url)
    b.autorun()
