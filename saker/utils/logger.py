#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

from saker.utils.mtime import today

logpath = os.path.join(".", "logs")

CONSOLE_PRINT = logging.DEBUG
commonlogpath = os.path.join(logpath, "ctf-"+today()+".log")

formatter_str = '[%(asctime)s] [%(levelname)s] %(message)s'

logger = logging.getLogger("logger")

logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(formatter_str)

if False:
    if not os.path.exists(logpath):
        os.mkdir(logpath)
    fh = logging.FileHandler(commonlogpath)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

ch = logging.StreamHandler()
chformatter = logging.Formatter(formatter_str)
ch.setLevel(CONSOLE_PRINT)
ch.setFormatter(chformatter)
logger.addHandler(ch)
