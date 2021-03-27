#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import chardet


class HTMLHandler(object):

    '''
    handle html content
    '''

    _links = None

    class RegExp(object):

        title = re.compile(r'<title>(.*?)</title>')
        desc = re.compile(r'<meta name="description" content="(.*?)">')
        keywords = re.compile(r'<meta name="keywords" content="(.*?)">')
        link = re.compile(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')")
        js = re.compile(r'<script.*?</script>')
        css = re.compile(r'<style.*?</style>')
        comment = re.compile(r'<!--[\s\S]*?-->')
        jscomment = re.compile(r'(\/\/.*)|(\/\*[\s\S]*?\*\/)')
        meta = re.compile(r'<meta.*?>')

    def __init__(self, content):
        super(HTMLHandler, self).__init__()
        if isinstance(content, bytes):
            content = self.chardecode(content)
        self.content = content

    def chardecode(self, string):
        encoding = chardet.detect(string)['encoding']
        if encoding is None:
            return string.decode(errors="ignore")
        return string.decode(encoding, errors="ignore")

    @property
    def title(self):
        title = self.RegExp.title.findall(self.content)
        return title[0] if len(title) else 'None'

    @property
    def desc(self):
        desc = self.RegExp.desc.findall(self.content)
        return desc[0] if len(desc) else 'None'

    @property
    def keywords(self):
        keywords = self.RegExp.keywords.findall(self.content)
        return keywords if len(keywords) else 'None'

    @property
    def links(self):
        if self._links is None:
            links = list(set(self.RegExp.link.findall(self.content)))
            self._links = links if len(links) else []
        return self._links

    @property
    def size(self):
        if len(self.content) < (1 << 10):
            return "%sB" % len(self.content)
        elif len(self.content) < (1 << 20):
            return "%sKB" % (len(self.content) >> 10)
        else:
            return "%sMB" % (len(self.content) >> 20)

    def subdomains(self, domain):
        reg = re.compile(r'[a-zA-Z0-9\-\.]+\.' + domain.replace('.', '\\.'), re.IGNORECASE)
        datas = reg.findall(self.content)
        datas = list(set(datas))
        return datas if len(datas) else []
