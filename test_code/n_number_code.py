#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: n_number_code.py
    @time: 2020/7/20 22:07
"""


# from collections import Counter
#
# x = "133"
# y = "2333"
#
# x_counter = Counter(x)
# print(x_counter)
# y_counter = Counter(y)
# print(y_counter)
#
# sum = 0
# for x_k, x_v in x_counter.items():
#     for y_k, y_v in y_counter.items():
#         sum += int(x_k) % int(y_k) * x_v * y_v
# print(sum)


def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)


known = {0: 0, 1: 1}


def fib2(n):
    if n in known:
        return known[n]
    res = fib2(n - 1) + fib2(n - 2)
    known[n] = res
    return res


import time

t1 = time.time()
for i in range(40):
    print(fib1(i), end=" ")
t2 = time.time()
print()
print(t2 - t1)

print('*'*20)
t1 = time.time()
for i in range(40):
    print(fib2(i), end=" ")
t2 = time.time()
print()
print(t2 - t1)