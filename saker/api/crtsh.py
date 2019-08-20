#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2


def crtsh(domain):
    '''
    get subdomain info via certificate identity by crt.sh's database
    '''
    HOST = 'crt.sh'
    NAME = 'certwatch'
    USER = 'guest'
    try:
        conn = psycopg2.connect("dbname=%s user=%s host=%s" % (NAME, USER, HOST))
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("SELECT distinct(NAME_VALUE) FROM certificate_identity WHERE certificate_identity.NAME_TYPE = 'dNSName' AND reverse(lower(certificate_identity.NAME_VALUE)) LIKE reverse(lower('%%.%s'));" % domain)
    except Exception as e:
        print(repr(e))
        return []
    domains = list(map(lambda i: i[0], cursor.fetchall()))
    domains.sort()
    return domains


if __name__ == '__main__':
    print(crtsh('github.com'))
