#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct


def p32(u):
    return struct.pack('>I', u)


def u32(p):
    return struct.unpack('>I', p)[0]
