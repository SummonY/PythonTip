#!/usr/bin/python
#-*- coding:utf-8 -*-

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 25]

count5 = 0
count2 = 0

for i in L:
    while i % 5 == 0:
        count5 += 1
        i /= 5
    while i % 2 == 0:
        count2 += 1
        i /= 2

count = count5 if count5 < count2 else count2
print count
