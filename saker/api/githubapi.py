#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pip install PyGithub

import re
import time
from collections import defaultdict
from github import Github


class GithubAPI(object):

    '''
    https://github.com/settings/tokens
    public_repo, read:user, repo:status, user:email
    '''

    def __init__(self, token=None):
        super(GithubAPI, self).__init__()
        if token is None:
            self.g = Github()
        else:
            self.g = Github(token)

    def getUsersByOrg(self, org):
        org = self.g.get_organization(org)
        members = []
        for member in org.get_members():
            m = {
                'email': member.email,
                'realname': member.name,
                'username': member.login,
                'company': member.company,
                'addr': member.location,
                'site': m.html_url,
                'source': org,
            }
            for k in m:
                if m[k] is None:
                    m[k] = ''
            members.append(m)
        return members

    def getUserInfo(self, user):
        if isinstance(user, str):
            user = self.g.get_user(user)
        repose = user.get_repos()
        orgs = user.get_orgs()
        return user

    def gatherByEmail(self, suffix, interval=2):
        '''
        note: search need token
        '''
        emails = []
        reg = re.compile(r'[a-zA-Z0-9\-\.]*' + suffix.replace('.', '\\.'), re.IGNORECASE)
        pages = self.g.search_code(suffix)
        for page in pages:
            # for access rate limit
            time.sleep(interval)
            datas = reg.findall(page.decoded_content.decode())
            for email in datas:
                if email not in emails:
                    yield email
                    emails.append(email)

    def gatherParameter(self, interval=2):
        parameters = defaultdict(int)
        pages = self.g.search_code('$_GET')
        reg = re.compile(r'''\$_GET\[['"]?(.*?)['"]?\]''')
        for page in pages:
            time.sleep(interval)
            datas = reg.findall(page.decoded_content.decode())
            for parameter in datas:
                print(parameter)
                parameters[parameter] += 1
            break

if __name__ == '__main__':
    token = ''
    g = GithubAPI(token)
    # print(g.gatherByEmail('@github.com'))
    g.gatherParameter()
