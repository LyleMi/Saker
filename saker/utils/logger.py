#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

from saker.utils.mtime import today


class ColoredFormatter(logging.Formatter):

    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

    COLORS = {
        'WARNING': YELLOW,
        'INFO': WHITE,
        'DEBUG': BLUE,
        'CRITICAL': YELLOW,
        'ERROR': RED
    }

    RESET_SEQ = "\033[0m"
    COLOR_SEQ = "\033[1;%dm"
    BOLD_SEQ = "\033[1m"

    def __init__(self, msg, use_color=True):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        levelname = record.levelname
        if self.use_color and levelname in self.COLORS:
            levelname_color = self.COLOR_SEQ % (30 + self.COLORS[levelname]) + levelname + self.RESET_SEQ
            record.levelname = levelname_color
        return logging.Formatter.format(self, record)


def getLogger(loggername="saker"):
    logger = logging.getLogger(loggername)
    if len(logger.handlers) > 0:
        return logger
    return initLogger(logger)


def initLogger(logger, logfile=False, logpath=None):
    logger.setLevel(logging.DEBUG)
    formatStr = '[%(asctime)s] [%(levelname)s] %(message)s'
    formatter = logging.Formatter(formatStr)

    # command line logger
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    chformatter = ColoredFormatter(formatStr)
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
