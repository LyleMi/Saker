#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

from saker.utils.mtime import today


def getLogger():
    logger = logging.getLogger("saker")
    if len(logger.handlers) > 0:
        return logger
    return initLogger(logger)


def initLogger(logger, logfile=False, logpath=None):
    logger.setLevel(logging.DEBUG)
    formatStr = '[%(asctime)s] [%(levelname)s] %(message)s'
    formatter = logging.Formatter(formatStr)

    # command line logger
    ch = logging.StreamHandler()
    chformatter = logging.Formatter(formatStr)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(chformatter)
    logger.addHandler(ch)

    # file logger
    if logfile:
        if logpath is None:
            logdir = os.path.join(".", "logs")
            logpath = os.path.join(logdir, "saker-" + today() + ".log")
            if not os.path.exists(logdir):
                os.mkdir(logdir)
        fh = logging.FileHandler(logpath)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger
