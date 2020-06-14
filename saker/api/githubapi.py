#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pip install PyGithub

import re
import time
import random
from collections import defaultdict
from github import Github

from saker.utils.serializer import Serializer
from saker.utils.logger import getLogger


class GithubAPI(object):

    '''
    https://github.com/settings/tokens
    public_repo, read:user, repo:status, user:email
    '''

    def __init__(self, token=None, interval=1):
        super(GithubAPI, self).__init__()
        if token is None:
            self.g = Github()
        else:
            self.g = Github(token)
        self.interval = interval
        # save intermediate result
        self.sr = Serializer('pickle', 'archive')
        self.logger = getLogger()

    def wait(self):
        # limit access rate
        time.sleep(random.random() * 2 * self.interval)

    def getUser(self, user):
        if isinstance(user, str):
            user = self.g.get_user(user)
        return user

    def getUserInfo(self, user):
        user = self.getUser(user)
        info = {
            'email': user.email,
            'realname': user.name,
            'username': user.login,
            'company': user.company,
            'addr': user.location,
            'site': user.html_url,
        }
        return info

    def getUserInfoDetail(self, user):
        user = self.getUser(user)
        info = self.getUserInfo(user)
        repos = user.get_repos()
        orgs = user.get_orgs()
        return user

    def getRepo(self, repo):
        if isinstance(repo, str):
            repo = self.g.get_repo(repo)
        return repo

    def getOrg(self, org):
        if isinstance(org, str):
            org = self.g.get_organization(org)
        return org

    def getUsersByOrg(self, org):
        org = self.getRepo(org)
        members = []
        for member in org.get_members():
            members.append(member)
        return members

    def getReposByOrg(self, org):
        org = self.getOrg(org)
        repos = []
        for repo in org.get_repos():
            repos.append(repo)
        return repos

    def getUsersByOrgContributors(self, org):
        repos = self.getReposByOrg(org)
        self.sr.save(repos, 'repos')
        users = set()
        for repo in repos:
            # skip fork projects
            if repo.parent is not None:
                continue
            self.logger.debug('get contributors from %s' % repo.name)
            contributors = set(self.getContributorsByRepo(repo))
            users = users.union(contributors)
            self.wait()
            self.sr.save(contributors, '%s-users' % repo.name)
        self.sr.save(users, 'users')
        return users

    def dumpUsersInfo(self, users):
        infos = []
        count = 0
        total = len(users)
        for u in users:
            if count % 20 == 0:
                self.sr.save(infos, 'infos')
                self.wait()
                self.logger.debug('spider user info %s of %s' % (count, total))
            infos.append(self.getUserInfo(u))
            count += 1
        self.sr.save(infos, 'infos')
        return infos

    def getContributorsByRepo(self, repo):
        repo = self.getRepo(repo)
        contributors = []
        for c in repo.get_contributors():
            contributors.append(c)
        return contributors

    def gatherByEmail(self, suffix):
        '''
        note: search need token
        '''
        emails = []
        reg = re.compile(r'[a-zA-Z0-9\-\.]*' + suffix.replace('.', '\\.'), re.IGNORECASE)
        pages = self.g.search_code(suffix)
        for page in pages:
            # for access rate limit
            self.wait()
            datas = reg.findall(page.decoded_content.decode())
            for email in datas:
                if email not in emails:
                    yield email
                    emails.append(email)

    def gatherParameter(self):
        parameters = defaultdict(int)
        pages = self.g.search_code('$_GET')
        reg = re.compile(r'''\$_GET\[['"]?(.*?)['"]?\]''')
        for page in pages:
            self.wait()
            datas = reg.findall(page.decoded_content.decode())
            for parameter in datas:
                print(parameter)
                parameters[parameter] += 1
