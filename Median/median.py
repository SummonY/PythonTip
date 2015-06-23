#!/usr/bin/python
#-*- coding:utf-8 -*-

L = [0, 1, 2.5, 7, 4, 5]

length = len(L)
L.sort()

if length % 2 == 0:
    left = length / 2 - 1
    right = length / 2
    value = (L[left] + L[right]) / float(2)
    if value % 1 == 0:
        print "%d" % (value)
    else:
        print "%.1f" % (value)
else:
    median = length / 2
    if median % 1 == 0:
        print "%d" %(L[median])
    else:
        print "%.1f"  % (L[median])
