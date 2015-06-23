#!/usr/bin/python
#-*- coding:utf-8 -*-

a = "12345"

print a[::-1]

print reduce(lambda x, y: y+x, a)
