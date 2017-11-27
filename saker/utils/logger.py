#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

from saker.utils.mtime import today

logdir = os.path.join(".", "logs")

logpath = os.path.join(logdir, "saker-"+today()+".log")

formatStr = '[%(asctime)s] [%(levelname)s] %(message)s'

logger = logging.getLogger("saker")

logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(formatStr)

if False:
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    fh = logging.FileHandler(logpath)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

ch = logging.StreamHandler()
chformatter = logging.Formatter(formatStr)
ch.setLevel(logging.DEBUG)
ch.setFormatter(chformatter)
logger.addHandler(ch)
