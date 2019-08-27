#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pip install PyGithub

from github import Github


class GithubAPI(object):

    def __init__(self, token=None):
        super(GithubAPI, self).__init__()
        if token is None:
            self.g = Github()
        else:
            self.g = Github(token)

    def getUsersByOrg(self, org):
        org = self.g.get_organization(org)
        members = org.get_members()
        return members

    def getUserInfo(self, user):
        if isinstance(user, str):
            user = self.g.get_user(user)
        repose = user.get_repos()
        orgs = user.get_orgs()
        return user
