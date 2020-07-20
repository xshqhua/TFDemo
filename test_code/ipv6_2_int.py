#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: ipv6_2_int.py
    @time: 2020/3/11 22:13
"""
import ipaddress

print(int(ipaddress.ip_address('aaa:fe80::aa2a:fbd6:7860')))
print(ipaddress.ip_address(int(ipaddress.ip_address('aaa:fe80::aa2a:fbd6:7860'))))

