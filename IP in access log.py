#!/usr/bin/env python
# coding:utf-8

# awk '{print $1}' access.log |sort -n|uniq -c|sort -rn|head

list = []
f = open('access.log')
str1 = f.readlines()
f.close()

for i in str1:
    ip =  i.split(' ')[0]
    if len(ip)!=0 and ip!="\n":
        list.append(ip)

list_num = set(list)
 
for j in list_num:
    num = list.count(j)
    print ('%s : %s' % (j, num))