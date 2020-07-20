#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: split_01.py
    @time: 2020/3/1 0:33
"""
import re

s = "100Ce10/0//000"
# re.find
# print(s[::-1])
print(re.search("[\d/]+", s[::-1]).group())
print(s.replace(re.search("[\d/]+", s[::-1]).group(0)[::-1], ""))
print(re.search("\d+[a-zA-Z]+",s).group())




str1="googleggg"









