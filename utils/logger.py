#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from os.path import join
from utils.mtime import today

CONSOLE_PRINT = logging.DEBUG
commonlogpath = join(".", "logs", "ctf-"+today()+".log")

formatter_str = '[%(asctime)s] [%(levelname)s] %(message)s'

logger = logging.getLogger("logger")

logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(commonlogpath)
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
chformatter = logging.Formatter(formatter_str)

ch.setLevel(CONSOLE_PRINT)

formatter = logging.Formatter(formatter_str)
fh.setFormatter(formatter)
ch.setFormatter(chformatter)

logger.addHandler(fh)
logger.addHandler(ch)
