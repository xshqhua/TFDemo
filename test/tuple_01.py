#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: tuple_01.py
    @time: 2019/12/23 23:56
"""
xx = (1, 2)
print(xx)


def convert_2_location(xx):
    return tuple([(i + 1) * 50 for i in xx])


print(convert_2_location(xx))
