#!/usr/bin/python
# coding:utf-8

# Execute shell cmd within an IP range
import paramiko
import threading

def ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Accept hosts that are not under local Know_host file
        ssh.connect(ip,username,passwd,timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
#           stdin.write("yes")
            # Enter yes to execute
            out = stdout.readlines()
            for o in out:
                print (o)
        print ('%s\tOK\n'%(ip))
        ssh.close()
    except :
        print ('%s\tError\n'%(ip))


if __name__=='__main__':
    cmd = ['date','df -h']
    username = ""
    passwd = ""
    threads = []
    for i in range(1,255):
        ip = '192.168.31.'+str(i)
        a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
        a.start()