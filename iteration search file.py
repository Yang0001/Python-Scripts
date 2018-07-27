#!/usr/bin/env python
# coding:utf-8

import os

dir = "/tmp/"
filename = 'access.log'
findfile = 0

for root,dirs,files in os.walk(dir):
    for f in files:
      if f == filename:
          print (os.path.join(root, f))
          findfile = 1

if findfile != 1:
  print("not find")


