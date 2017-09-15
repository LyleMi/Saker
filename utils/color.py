#!/usr/bin/python
# -*- coding: utf-8 -*-

from termcolor import colored


def red(s):
    return colored(s, 'red')


def cyan(s):
    return colored(s, 'cyan')


def green(s):
    return colored(s, 'green')


def danger(s):
    return colored(s, 'grey', 'on_red')


def yellow(s):
    return colored(s, 'yellow')
