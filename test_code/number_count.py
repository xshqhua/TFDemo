#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: number_count.py
    @time: 2020/7/14 22:25
"""


def num(n, res=[]):
    if n == 0:
        res.append(0)
        return 0
    elif n == 1:
        res.append(1)
        return 1
    else:
        for i in range(n):
            re = num(n - i, []) + i
            if re == n:
                print(res)
                return re


num(2)
