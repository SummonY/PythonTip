#!/usr/bin/python
#-*- coding:utf-8 -*-

def GCD(a, b):
    c = a % b
    while c:
        a = b
        b = c
        c = a % b
    return b


if __name__=='__main__':
    a = input()
    b = input()
    print GCD(a, b)
