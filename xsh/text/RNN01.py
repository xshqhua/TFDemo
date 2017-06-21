#!/usr/bin/env python  
# -*- coding=utf-8 -*-
"""
@version: v1.0 
@author: XSH 
@license: xshqhua  
@contact: xshqhua@foxmail.com 
@site:  
@software: PyCharm 
@file: RNN01.py 
@time: 2017/6/20 12:55 
"""
import tensorflow as tf
import codecs
import collections
import numpy as np
import sys
import time

# sys.setdefaultencoding("utf8")
# rel
sess = tf.Session()

poetry_file = "./corpus/poetry.txt"
batch_size = 3


def read_data(file_path):
	poetrys = []
	with codecs.open(file_path, "r", "utf-8") as file_read:
		for line in file_read:
			title, poetry = line.strip().replace("\:", "").split(":")
			poetry = poetry.replace(" ", "")
			poetry = poetry.replace("-", "")
			poetry = poetry.replace("_", "")
			poetry = poetry.replace("(", "")
			poetry = poetry.replace(u")", "")
			poetry = poetry.replace(u"（", "")
			poetry = poetry.replace(u"）", "")
			poetry = poetry.replace(u"《", "")
			poetry = poetry.replace(u"》", "")
			poetry = poetry.replace(u"【", "")
			poetry = poetry.replace(u"】", "")
			poetry = poetry.replace("[", "")
			poetry = poetry.replace("]", "")
			# poetry = "[" + poetry + "]"
			if poetry != "":
				poetrys.append(poetry)
		poetrys = sorted(poetrys, key=lambda line: len(line))
		print(len(poetrys))
		return poetrys


def init():
	poetrys = read_data(poetry_file)
	all_words = []
	i = 0
	for poetry in poetrys:
		all_words += [word for word in poetry]
	# if len(all_words)>100*i:
	#     print(all_words)
	#     i+=1
	counter = collections.Counter(all_words)
	# 统计单词的个数
	# print(counter)
	# 将单词进行逆序排序
	count_pair = sorted(counter.items(), key=lambda x: -x[1])
	# print(count_pair)
	# 过滤部分非单词的词
	count_pair = count_pair[4:]
	# print(count_pair[4:])
	# 选取一部分单词作为有用的信息
	words, _ = zip(*count_pair)
	# print(words)
	# print(len(words))
	words = words[:len(words)] + (" ",)
	# print(words)
	# print(len(words))
	# 将单词进行ID标识
	words_2_number = dict(zip(words, range(len(words))))
	# print(words_2_number)
	# 将单词进行ID标识，逆序
	words_2_number_dev = dict(zip(words_2_number.values(), words_2_number.keys()))
	# print(words_2_number_dev)
	# 定义一个匿名函数
	to_num = lambda word: [words_2_number.get(w, len(words)) for w in word]
	# print(to_num)
	poetrys_vector = [str(list(map(to_num, poetry))) for poetry in poetrys]
	# print(poetrys_vector[0])
	# print(poetrys_vector[1])
	# print(poetrys_vector[2])
	# print(type(poetrys_vector))
	# print(type(poetrys_vector[0]))
	# print(type(poetrys_vector[0][0]))
	poetrys_vector = [[int(int_str.replace("]", "").replace("[", "")) for int_str in poetry.split(",")] for poetry in
	                  poetrys_vector]
	
	# for i in poetrys_vector:
	#     print(len(i))
	# print(type(i[0]))
	# time.sleep(0.1)
	
	n_chunk = len(poetrys_vector)
	x_batchs = []
	y_batchs = []
	start_index = i * batch_size
	end_index = start_index + batch_size
	batchs = poetrys_vector[start_index:end_index]
	length = max(map(len, batchs))
	# np.fu
	# print(words_2_number[" "])
	# print(type(words_2_number[" "]))
	# print ((batch_size,length))
	x_data = np.full((batch_size, length), words_2_number[" "], np.int32)
	for row in range(batch_size):
		# print("row=", row)
		# print("len(batchs)=", len(batchs))
		# print("len(x_data)=", len(x_data))
		if row < len(batchs):
			x_data[row, :len(batchs[row])] = batchs[row]
	y_data = np.copy(x_data)
	print("x_data=", x_data)
	y_data[:, :-1] = x_data[:, 1:]
	print("y_data=", y_data)
	x_batchs.append(x_data)
	y_batchs.append(y_data)
	pass


class Main():
	def __init__(self):
		pass


if __name__ == "__main__":
	init()
	pass
