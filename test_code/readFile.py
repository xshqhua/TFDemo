#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: readFile.py
    @time: 2020/3/1 15:59
"""

file = open('C:/Users/hanqing/Desktop/hanqing.txt', mode='r', encoding='utf-8')
# 在桌面打开一个.txt文本文档，并且是读的模式
# 读取文件，并且输出：
text = file.read()
print(file.read())
import re

words = re.findall(r'[a-zA-Z]+', text)
count = len(words)

print(count)
