#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: process_string.py
    @time: 2020/6/16 22:07
"""


# def func():
#     n = int(input())
#     list_id = []
#     for i in range(n):
#         str = input().replace(" ", "")
#         str1 = str
#         if len(str1) > 9:
#             continue
#         a = str1[0]
#         str2 = str1[1:]
#         if "a" <= a <= "z" or "A" <= a <= "Z":
#             a = a.lower()
#         else:
#             continue
#         if not str2.isdigit():
#             continue
#         str3 = a + str2
#         if len(str3) < 9:
#             for j in range(len(str3) - 9):
#                 str2 = "0" + str2
#         id = a + str2
#         list_id.append(id)
#     ids = set(list_id)
#     for id in ids:
#         print(id)
#
# func()


def func():
    n = int(input())
    list_id = []
    for i in range(n):
        str = input().replace(" ", "")
        str1 = str.lower()
        if len(str1) <= 9 and "a" <= str1[0] <= "z" and str1[1:].isdigit():
            list_id.append(str1[0] + "{:0>8d}".format(int(str1[1:])))
    list_id.sort()
    ids = set(list_id)
    for id in ids:
        print(id)


func()

# print()/

# 7
# w123
# aa445
# a1237465493976352
# a 00 35
# x897
# ss789
# a 00 35
