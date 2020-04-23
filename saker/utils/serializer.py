#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import pickle


class Serializer(object):

    def __init__(self, serializer='json', savepath='.'):
        super(Serializer, self).__init__()
        if serializer == 'json':
            self.suffix = 'json'
            self.serializer = json
        elif serializer == 'pickle':
            self.suffix = 'pkl'
            self.serializer = pickle
        self.dir = os.path.abspath(savepath)
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)

    def getPath(self, identifier):
        return os.path.join(self.dir, identifier + "." + self.suffix)

    def save(self, val, identifier):
        """
        save variable into file
        :param val: the val you want to save
        :param identifier: str. the identifier of variable
        :return: bool. status of save
        """
        with open(self.getPath(identifier), 'wb') as fh:
            self.serializer.dump(val, fh)
        return True

    def load(self, identifier):
        """
        load variable from file
        :param identifier: str. the identifier of variable
        :return: variable
        """
        with open(self.getPath(identifier), 'rb') as fh:
            data = self.serializer.load(fh)
        return data
