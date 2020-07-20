#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: num_String.py
    @time: 2020/6/22 23:36
"""
import re


def func():
    str_a = "abcd12345ed125ss123058789ss345"
    path = re.findall("\d+", str_a)
    # 方法一
    # max = 0
    # # list_num=[]
    # for lis in path:
    #     l = len(lis)
    #     if l > max:
    #         max = l
    #         list_num.append(lis)
    # print(list_num[-1] + ","+str(max))
    # 方法二
    tict_l = {len(lis): lis for lis in path}
    list_l = sorted(tict_l.items(), key=lambda a: a[0], reverse=True)
    print(list_l)
    print(list_l[0])
    print(list_l[0][1]+","+str(list_l[0][0]))

func()
