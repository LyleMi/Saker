#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis


class redisDetect(object):

    def __init__(self):
        super(redisDetect, self).__init__()
        self.name = "redisDetect"

    def run(self, host, port=6379, timeout=2):
        try:
            r = redis.StrictRedis(host=host, port=6379, db=0, socket_timeout=timeout)
            self.config = r.config_get()
            return True
        except redis.exceptions.ConnectionError as e:
            return False
        except redis.exceptions.TimeoutError as e:
            return False


if __name__ == '__main__':
    pass
