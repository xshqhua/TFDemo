#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: xxxxx.py
    @time: 2020/6/16 23:19
"""

str_1 = "0000110110100001100"
max_len = 0
target_i = '1'
j = 0
start_i = 0
end_i = 0
curr_len = 0
rec = {}
for i in range(len(str_1)):
    if str_1[i] == target_i:
        curr_len += 1
        end_i = i
        if curr_len >= max_len:
            # v1 = [start_i, end_i + 1]
            # if max_len in rec.keys():
            #     t1 = rec.get(max_len)
            #     t1.append(v1)
            #     rec[max_len] = t1
            # else:
            rec[i] = [start_i, end_i + 1]
            max_len = curr_len
    else:
        start_i = i + 1
        curr_len = 0
print(str_1)
print(rec)

# rec = sorted(rec.items(), key=lambda x: abs(x[1][0] - x[1][1]))
print(rec)
for k, v in rec.items():
    print(str_1[int(v[0]): int(v[1])])
# print(str_1[0:3])
