#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: sort_key.py
    @time: 2020/6/1 23:32
"""

from collections import Counter


def fun():
    n =   int(input())
    # world_list = ["we", "we", "er", "wr", "wr"]
    world_list = []
    for i in range(n):
        world_list.append(input())
    m = int(input())
    # m = 3
    world_counts = Counter(world_list)
    top_m = world_counts.most_common(m)
    # top_by_sort = sorted(top_m, key=lambda r: (r[1], -int(ord(r[0][0]))), reverse=True)
    top_by_sort = sorted(top_m, key=lambda r: (r[0], r[1]), reverse=False)
    print(top_m)
    for j in top_by_sort:
        print(j[0])


fun()
# 16
# word
# list
# egg
# credits
# red
# total
# find
# word
# cute
# total
# cute
# red
# total
# cute
# hot
# yet
# 3
