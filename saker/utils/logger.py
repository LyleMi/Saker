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


def getLogger(loggername="saker", logpath=None):
    logger = logging.getLogger(loggername)
    if len(logger.handlers) > 0:
        return logger
    logger.setLevel(logging.DEBUG)
    ch = commandHandler()
    logger.addHandler(ch)
    if logpath is not None:
        fh = fileHandler(logpath)
        logger.addHandler(fh)
    return logger


def commandHandler(loggerLevel=logging.DEBUG):
    formatStr = '[%(asctime)s] [%(levelname)s] %(message)s'
    ch = logging.StreamHandler()
    ch.setLevel(loggerLevel)
    chformatter = ColoredFormatter(formatStr)
    ch.setFormatter(chformatter)
    return ch


def fileHandler(logpath, loggerLevel=logging.DEBUG):
    if logpath is None:
        logdir = os.path.join(".", "logs")
        logpath = os.path.join(logdir, "saker-" + today() + ".log")
        if not os.path.exists(logdir):
            os.mkdir(logdir)

    formatStr = '[%(asctime)s] [%(levelname)s] %(message)s'
    formatter = logging.Formatter(formatStr)

    fh = logging.FileHandler(logpath)
    fh.setLevel(loggerLevel)
    fh.setFormatter(formatter)
    return fh
