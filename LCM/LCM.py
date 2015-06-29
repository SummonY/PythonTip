#!/usr/bin/python
#-*- coding:utf-8 -*-

def GCD(a, b):
    c = a % b
    while c:
        a = b
        b = c
        c = a % b
    return b

def LCM(a, b):
    return (a * b) / GCD(a, b)


if __name__=='__main__':
    a = input()
    b = input()
    print LCM(a, b)
