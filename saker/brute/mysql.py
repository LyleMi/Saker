#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

class MySQL(object):
    
    """
    MySQL password brute
    """
    
    def __init__(self, addr, port):
        super(MySQL, self).__init__()
        self.addr = addr
        self.port = port
        
    def brute(self):
        raise Exception("not implement")