#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: number_split.py
    @time: 2020/7/14 23:06
"""


# import re
# list_worsd=["黄色","暴力","武力"]
# re.sub()

# def fun_process(n, s, m):
#     if n == 0:
#         str1 = s[:len(s) - 1]
#         print(str1)
#     for i in range(1, n):
#         s1 = s + str(i) + "+"
#         fun_process(n - i, s1, m)
#
#
# def func():
#     while True:
#         try:
#             n = int(input())
#             s = str(n) + "="
#             fun_process(n, s, 1)
#         except:
#             break
#
#
# func()


lis = []


def func_split(pre, num, max):
    if num <= max:
        lis.append(pre + str(num))
        for i in range(num - 1):
            if i > 0:
                func_split(str(pre) + str(i) + " + ", num - i, i)
                i -= 1
    else:
        for i in range(num - 1):
            if i > 0:
                func_split(str(pre) + str(i) + " + ", num - i, i)
                i -= 1

    return lis


def fff():
    n = int(input())
    lis = func_split(str(n) + " = ", n, n - 1)
    for i in lis:
        print(i)


fff()
