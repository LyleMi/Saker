#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

stripslash = False

file = "path.txt"
file = "sqlkeywords.txt"
file = "weakfile.txt"
file = "linuxfile.txt"
tmp = file + ".tmp"
x = [i for i in open(file)]

# strip slash
if stripslash:
    for i in range(len(x)):
        if x[i].startswith("/"):
            x[i] = x[i][1:]

x = list(set(x))

x.sort()

y = open(tmp, "w")
for i in x:
    y.writelines(i)

y.close()

os.remove(file)
os.rename(tmp, file)
