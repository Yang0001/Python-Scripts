#!/usr/bin/env python
# coding:utf-8

import os

# for root,dirs,files in os.walk('/tmp'):
for root,dirs,files in os.walk('/tmp/'):
    for name in files:
        print(os.path.join(root, name))
