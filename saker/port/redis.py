#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis

class redisDetect(PortBase):

    def __init__(self):
        super(redisDetect, self).__init__()
        self.name = "redisDetect"
        
    def run(self, ip, port=6379, timeout=2):

        try:
            r = redis.StrictRedis(host=host, port=6379, db=0)
            self.config = r.config_get()
            return True
        except Exception, e:
            return False

if __name__ == '__main__':
    pass
