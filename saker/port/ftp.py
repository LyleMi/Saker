#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ftplib import FTP


class ftpDetect(object):

    def __init__(self):
        super(ftpDetect, self).__init__()
        self.name = "ftpDetect"

    def run(self, ip, port=21, timeout=2):
        try:
            ftp = FTP()
            ftp.connect(ip, port, timeout=timeout)
            self.banner = ftp.getwelcome()
            ftp.login()
            self.anonymous = True
            flist = []
            ftp.retrlines('LIST', lambda i: flist.append(i))
            ftp.quit()
            self.flist = flist
        except Exception, e:
            # print(str(e), 'error')
            return None
        finally:
            self.clear()

        return True
