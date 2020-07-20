#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: add_string.py
    @time: 2020/6/17 22:16
"""


# 题目描述
# 连续输入字符串(输出次数为N,字符串长度小于100)，请按长度为8拆分每个字符串后输出到新的字符串数组，
#
# 长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
#
# 首先输入一个整数，为要输入的字符串个数。
#
# 例如：
#
# 输入：2
#
# abc
#
# 12345789
#
# 输出：abc00000
#
# 12345678
#
# 90000000
# 输入描述:
# 首先输入数字n，表示要输入多少个字符串。连续输入字符串(输出次数为N,字符串长度小于100)。
#
# 输出描述:
# 按长度为8拆分每个字符串后输出到新的字符串数组，长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
#
# 示例1
# 输入
# 复制
# 2
# abc
# 123456789
# 输出
# 复制
# abc00000
# 12345678
# 90000000
# def func():
#     # n = int(input())
#     n = 3
#     str_1 = ["123", '123456789', '12345678123456789']
#     for i in range(n):
#         # str = input()
#         str = str_1[i]
#         if 0 < len(str) < 8:
#             str1 = "{:0<8d}".format(int(str))
#             print(str1)
#         if len(str) > 8:
#             for j in range(len(str) // 8):
#                 str2 = str[j * 8:(j + 1) * 8]
#                 if len(str2.strip()) < 8:
#                     str2 = "{:0<8d}".format(str2)
#                 print(str2)
#
#             m = len(str) % 8
#             if m != 0:
#                 str = str[-m:] + "0" * (8 - m)
#                 print(str)
#
#
# def func1():
#     # n = int(input())
#     n = 3
#     str_1 = ["123", '123456789', '12345678123456789']
#     for i in range(n):
#         # str = input()
#         str = str_1[i]
#         str1 = str + "0" * 7
#         m = len(str1) // 8
#         for j in range(m):
#             print(str1[j * 8:(j + 1) * 8])
#
#
# func()
print(bin(256))


