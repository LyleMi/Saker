#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import random
from datetime import date
from datetime import timedelta
from saker.utils.paths import Paths


def fakemobile():
    prefix = ['133', '149', '153', '173', '177', '180', '181', '189', '199', '130', '131', '132', '145', '155', '156', '166', '171', '175', '176', '185', '186', '134', '135', '136', '137', '138', '139', '147', '150', '151', '152', '157', '158', '159', '172', '178', '182', '183', '184', '187', '188', '198']
    p = random.choice(prefix)
    return p + str(random.randint(10000000, 99999999))


def lastname():
    with open(Paths.names, 'r', encoding='utf-8') as fh:
        names = fh.read().strip().split()
    return random.choice(names)


def firstname():
    return chr(random.randint(0x4e00, 0x9fa5)) + chr(random.randint(0x4e00, 0x9fa5))


def fakename():
    return lastname() + firstname()


def fakeid():
    with open(Paths.areaid, 'r', encoding='utf-8') as fh:
        areaid = json.load(fh)
    ids = list(areaid.keys())
    aid = random.choice(ids)
    age = random.randint(20, 40)
    dates = date(date.today().year - age, 1, 1) + timedelta(days=random.randint(0, 364))
    dates = str(dates).replace("-", "")
    seq = str(random.randint(1, 99)).rjust(2, '0')
    gender = str(random.randint(1, 9))
    code = aid + dates + seq + gender
    code += checkCodeCal(code)
    return code


def checkCodeCal(code):
    code = list(map(int, code))
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    code = sum([a * b for a, b in zip(weight, code)])
    code %= 11
    codes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    return codes[code]
