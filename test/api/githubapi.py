#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from saker.api.githubapi import GithubAPI


class GithubTest(unittest.TestCase):

    def test_main(self):
        token = ''
        g = GithubAPI(token)
        print(g.gatherByEmail('@github.com'))
        # g.gatherParameter()
        # g.getUsersByOrgContributors('')
        # g.dumpUsersInfo()


if __name__ == '__main__':
    unittest.main()
