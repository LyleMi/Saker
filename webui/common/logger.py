#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

logdir = os.path.join(".", "logs")
logpath = os.path.join(logdir, "firewall.log")

formatStr = '[%(asctime)s] [%(levelname)s] %(message)s'
formatter = logging.Formatter(formatStr)

logger = logging.getLogger("console")
ch = logging.StreamHandler()
chformatter = logging.Formatter(formatStr)
ch.setLevel(logging.INFO)
ch.setFormatter(chformatter)
logger.addHandler(ch)