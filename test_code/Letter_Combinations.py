#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: Letter_Combinations.py
    @time: 2020/7/29 21:42
"""

num = {"2": "abc", "3": "def","4":"ghi","5":"jkl","6": "mno", "7": "pqrs","8":"tuv","9":"wxyz"}


class Slouation(object):
    def letterCombinations(self, digits):
        pass


result = []


def xy(x, y):
    temp = []
    for i in x:
        for j in y:
            temp.append(i + j)
    return temp


def num_digit(digit):
    if len(digit) == 1:
        return num[digit]
    elif len(digit) == 2:
        return xy(num[digit[0]], num[digit[1]])
    else:
        return xy(num[digit[0]], num_digit(digit[1:]))


print(xy("abc", "def"))
print(num_digit("23"))
print(num_digit("233"))
