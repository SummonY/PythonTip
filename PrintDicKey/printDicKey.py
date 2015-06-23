#!/usr/bin/python
#-*- coding:utf-8 -*-

a = {1:1, 2:2, 3:3}

print reduce(lambda x, y:str(x) + "," + str(y), a.keys())
