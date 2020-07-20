#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: datetime_01.py
    @time: 2019/12/22 1:08
"""
from datetime import datetime
t1=datetime.now()
t2=datetime.now()
print('[INFO] Epoch: %d , training cost time : %s' % (1, t1-t2))