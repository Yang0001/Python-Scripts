#!/usr/bin/env python
# coding:utf-8

# check CPU、Memory and Disk space usage
# check the Average network speed with in given seconds

import psutil, time
import time
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", "--time", dest="time",
                  help="Enter the interal to testing the Network IO", metavar="10")


def Sysinfo():
    Boot_Start = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(psutil.boot_time()))
    time.sleep(0.5)
    Cpu_usage = psutil.cpu_percent()
    RAM = int(psutil.virtual_memory().total/(1027*1024))
    RAM_percent = psutil.virtual_memory().percent
    Swap = int(psutil.swap_memory().total/(1027*1024))
    Swap_percent = psutil.swap_memory().percent
    Net_sent = psutil.net_io_counters().bytes_sent
    Net_recv = psutil.net_io_counters().bytes_recv
    Net_spkg = psutil.net_io_counters().packets_sent
    Net_rpkg = psutil.net_io_counters().packets_recv
    BFH = r'%'
    print (" \033[1;32mPower up time：%s\033[1;m"  % Boot_Start)
    print (" \033[1;32mCurrent CPU usage：%s%s\033[1;m" % (Cpu_usage,BFH))
    print (" \033[1;32mPhysical memory：%dM\tUsage：%s%s\033[1;m" % (RAM,RAM_percent,BFH))
    print (" \033[1;32mSwap：%dM\tUsage：%s%s\033[1;m" % (Swap,Swap_percent,BFH))
    print (" \033[1;32mSend：%d Byte\tSend packets：%d个\033[1;m" % (Net_sent,Net_spkg))
    print (" \033[1;32mReceive：%d Byte\tReceive packets：%d个\033[1;m" % (Net_recv,Net_rpkg))

    for i in psutil.disk_partitions():
        print (" \033[1;32mDrive: %s Mount on: %s Usage: %s%s\033[1;m" % (i[0],i[1],psutil.disk_usage(i[1])[3],BFH))

def Net_io(s):
    x = 0
    sum = 0
    while True:
        if x >= s:
            break
        r1 = psutil.net_io_counters().bytes_recv
        time.sleep(1)
        r2 = psutil.net_io_counters().bytes_recv
        y = r2 - r1
        print ("%.2f Kb/s" % (y / 1024.0))
        sum += y
        x += 1
    result = sum / x
    print ("\033[1;32mNetwork IO average speed in %ss：%.2f Kb/s \033[1;m"  % (x,result / 1024.0))

if __name__ == "__main__":
    (options, args) = parser.parse_args()
    if options.time:
        Net_io(int(options.time))
    else:
        Sysinfo()