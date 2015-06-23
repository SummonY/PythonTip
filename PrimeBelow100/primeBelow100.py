#!/usr/bin/python
#-*- coding:utf-8 -*-

import math

def isPrime(n):
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    for i in range(5, int(math.floor(math.sqrt(n))) + 1, 6):
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
    return True


array = [2]
for i in range(3, 100, 2):
    if isPrime(i):
        array.append(i)

print reduce(lambda x, y: str(x) + " " + str(y), array)
