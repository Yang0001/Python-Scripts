#!/usr/bin/env python
# coding:utf-8

import time
import os



time_str = time.strftime("%Y-%m-%d", time.localtime())

file_name = "./" + time_str + ".log"

if os.path.exists(file_name) == False:
    os.mknod(file_name)
    handle = open(file_name, "w")
else:
    handle = open(file_name, "a")

