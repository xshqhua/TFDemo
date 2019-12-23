#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: gym_01_pong_v0.py
    @time: 2019/12/22 20:48
"""
import time;
ticks = time.time()
localtime = time.localtime(ticks)
asctime = time.asctime( time.localtime(time.time()) )

print ("当前时间戳为:", ticks)
print ("本地时间为:", localtime)
print ("本地时间为 :", asctime)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

# 以下输出2019年1月份的日历
import calendar
cal = calendar.month(2019, 12)
print("以下输出2019年1月份的日历:")
print (cal)


def printme( str ):
   "you are my supper star!"
   print (str)
   return
printme("再次调用同一函数")

import math
content = dir(math)
print(content)