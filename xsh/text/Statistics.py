#-*- encoding=utf-8 -*-  
'''
Created on 2017年5月9日

@author: xsh
'''

from xsh.text import Input_Data 

ipt =  Input_Data.Read_Date()

ipt.load()
# print(ipt.result_data["train"][0][0])
train  = ipt.result_data["train"]

tt = ipt.next_batch(batch_size=4, name="train")
# tt = ipt.next_batch(batch_size=4, name="train")
# print(tt)
print(type(tt[0]))
print(tt[0])
print(type(tt[0][0]))
# print(type(tt[0][0][0]))


