#!/usr/bin/env python
# coding:utf-8

import socket
import threading

lock = threading.Lock()
threads_list = []


def Get_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.error as e:
        print ('[-]%s: %s' % (domain, e))
        return 0


def PortScan(ip, port):
    try:
        s = socket.socket()
        s.settimeout(0.1)
        s.connect((ip, port))
        lock.acquire()
        openstr = "[-] PORT:" + str(port) + " OPEN "
        print (openstr)
        lock.release()
        s.close()
    except:
        pass


def main():
    banner = '''
    ################################
    ###########Port Scan############
    ################################
            '''
    print (banner)

    domain = input("PLEASE INPUT YOUR TARGET:")

    ip = Get_ip(domain)
    print ('[-] IP:' + ip)

    for n in range(1, 100):
        for p in range((n - 1) * 660, n * 660):
            t = threading.Thread(target=PortScan, args=(ip, p))
            threads_list.append(t)
            t.start()

        for t in threads_list:
            t.join()
    print (' Scan complete !')


if __name__ == '__main__':
    main()
