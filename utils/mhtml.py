#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import chardet


TITLE_REG = re.compile(r'<title>(.*?)</title>')
DESC_REG = re.compile(r'<meta name="description" content="(.*?)">')
KEY_REG = re.compile(r'<meta name="keywords" content="(.*?)">')
LINK_REG = re.compile(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')")


def chardecode(string):
    string = string.decode('hex')
    return string.decode(chardet.detect(string)['encoding'])


def contents_handler_reg(contents):
    title = TITLE_REG.findall(contents)
    title = title[0] if len(title) else 'None'

    desc = DESC_REG.findall(contents)
    desc = desc[0] if len(desc) else 'None'

    keywords = KEY_REG.findall(contents)
    keywords = keywords[0] if len(keywords) else 'None'

    if title == keywords == desc == 'None' or (not title):
        return False

    return [title, keywords, desc]


def detect(session, entities, url, headers, timeout, proxies):

    tmp = []

    for i in entities:
        r = session.get(url + i, headers=headers,
                        timeout=timeout, proxies=proxies)
        if r.status_code != 200:
            pass
        else:
            tmp += LINK_REG.findall(r.content)

    for i in tmp:
        r = session.get(url + i, headers=headers,
                        timeout=timeout, proxies=proxies)
        print(url+i), '\tstatus code: ', r.status_code
        if r.status_code != 200:
            pass
        else:
            entities.append(i)

    return list(set(entities))


def remove_js_css(content):
    r = re.compile(r'<script.*?</script>', re.I | re.M | re.S)
    s = r.sub('', content)
    r = re.compile(r'<style.*?</style>', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'<!--.*?-->', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'<meta.*?>', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'<ins.*?</ins>', re.I | re.M | re.S)
    s = r.sub('', s)
    return s
