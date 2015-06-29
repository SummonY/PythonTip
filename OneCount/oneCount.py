#!/usr/bin/python
#-*- coding:utf-8 -*-

a = 678976754567248

count = 0

while a:
    if a & 1:
        count += 1
    a = a >> 1

print count
