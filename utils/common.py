#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def randua():
    # 生成随机ua
    return random.choice([i.strip("\n") for i in open("data/user-agents.txt")])
