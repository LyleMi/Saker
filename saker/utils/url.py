#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import urllib.parse as uparse


def urlRelativeToAbsolute(url):
    # Turn a relative path into an absolute path
    finalBits = list()
    if '..' not in url:
        return url
    bits = url.split('/')
    for chunk in bits:
        if chunk == '..':
            # Don't pop the last item off if we're at the top
            if len(finalBits) <= 1:
                continue
            # Don't pop the last item off if the first bits are not the
            # path
            if '://' in url and len(finalBits) <= 3:
                continue
            finalBits.pop()
            continue
        elif chunk == '.':
            continue
        finalBits.append(chunk)
    return '/'.join(finalBits)


def urlBaseDir(url):
    # Extract the top level directory from a URL
    bits = url.split('/')
    # For cases like 'www.somesite.com'
    if len(bits) == 0:
        return url + '/'
    # For cases like 'http://www.blah.com'
    if '://' in url and url.count('/') < 3:
        return url + '/'
    base = '/'.join(bits[:-1])
    return base + '/'


def urlBaseUrl(url):
    # Extract the scheme and domain from a URL
    # Does not return the trailing slash! So you can do .endswith()
    # checks.
    if '://' in url:
        bits = re.match('(\w+://.[^/:]*)[:/].*', url)
    else:
        bits = re.match('(.[^/:]*)[:/]', url)
    if bits is None:
        return url.lower()
    return bits.group(1).lower()


def urlFile(url):
    # For cases like 'http://www.blah.com'
    url = url.split('://')
    url = url[0] if len(url) == 1 else url[1]
    if '/' not in url:
        return ''
    return url.split('/')[-1].split('?')[0]


def normalizeUrl(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        if ':443' in url:
            url = "https://" + url.replace(':443', '', 1)
        else:
            url = "http://" + url
    url = (url + '/') if url[-1] != '/' else url
    return url


def parseQuery(query):
    ret = {}
    for k, v in uparse.parse_qs(query).items():
        if len(v) < 2:
            ret[k] = uparse.unquote(v[0])
        else:
            ret[k] = [uparse.unquote(i) for i in v]
    return ret
