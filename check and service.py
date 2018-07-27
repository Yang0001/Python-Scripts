#!/usr/bin/env python
# coding:utf-8

import os
import sys

service_name= sys.argv[1]

def startService():
    service_status = os.popen('sudo netstat -tulnp | grep '+service_name,'r').readlines()

    if service_status == []:
       cmd_result = os.system('sudo service '+service_name+' start')

       if cmd_result == 0:
          print('service: '+service_name+' start success')

       else:
          print('service: '+service_name+' start fail')

    else:
        print('service: ' + service_name + ' already started')

startService()