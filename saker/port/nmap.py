#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import json
import uuid
import subprocess
import xml.etree.cElementTree as ET


class Nmap(object):

    args = ['-sV', '-sT', '-Pn']
    ports = '21-25,80-89,110,111,143,443,513,873,1080,1158,1433,1521,2049,2181,3306-3308,3389,3690,5900,6370-6379,7001,8000-8090,8161,9000,9418,11211,27017-27019,50060'

    def __init__(self, target, options=[]):
        self.target = target
        self.options = options

    def run(self):
        cmd = ["nmap"]
        cmd += self.args + self.options
        cmd += ["-p", self.ports, self.target]
        tmpName = '.tmp-nmap.%s.xml' % uuid.uuid4().hex
        cmd.extend(["-oX", tmpName])
        ret = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, error = ret.communicate()
        if error:
            print(error)
            return False

        tree = ET.parse(tmpName)
        os.remove(tmpName)
        root = tree.getroot()
        result = {}
        filter_flag = True
        for host in root.findall('host'):
            ip = host.find('address').get('addr')
            result[ip] = {}
            for port in host.find('ports').findall('port'):
                if port.find('state').get('state') not in ('filtered', 'closed'):
                    filter_flag = False
                if port.find('state').get('state') == 'open':
                    service = port.find('service')
                    if service is None:
                        continue
                    service = service.attrib
                    if service['name'] == 'tcpwrapped':
                        continue
                    service.pop('conf')
                    service.pop('method')
                    result[ip][port.get('portid')] = service
            if result[ip] == {}:
                del result[ip]

        if not result:
            if filter_flag:
                print('All open ports detected by zmap are actually filtered or closed!')
            else:
                print('Failed to parse nmap xml!')
            return None
        return result



if __name__ == '__main__':
    import time
    ip = "localhost"
    content = ""
    with open("domain.txt", "rb") as fh:
        content = fh.read()
    for domain in content.split("\n"):
        print("[%s] try %s now..." % (time.time(), domain))
        break
        n = Nmap(domain)
        ret = n.run()
        if ret:
            with open(domain, "wb") as fh:
                fh.write(json.dumps(n.ret))
