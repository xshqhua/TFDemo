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
import sys
import time

# sys.setdefaultencoding("utf8")
# rel
sess = tf.Session()

poetry_file = "./corpus/poetry.txt"


def read_data(file_path):
    peotrys = []
    with codecs.open(file_path, "r", "utf-8") as file_read:
        for line in file_read:
            title, peotry = line.strip().replace("\:", "").split(":")
            peotry = peotry.replace(" ", "")
            peotry = peotry.replace("-", "")
            peotry = peotry.replace("_", "")
            peotry = peotry.replace("(", "")
            peotry = peotry.replace(u")", "")
            peotry = peotry.replace(u"（", "")
            peotry = peotry.replace(u"）", "")
            peotry = peotry.replace(u"《", "")
            peotry = peotry.replace(u"》", "")
            peotry = peotry.replace(u"【", "")
            peotry = peotry.replace(u"】", "")
            peotry = peotry.replace("[", "")
            peotry = peotry.replace("]", "")
            peotry = "[" + peotry + "]"
            peotrys.append(peotry)
        peotrys = sorted(peotrys, key=lambda line: len(line))
        print(len(peotrys))
        return peotrys


def init():
    peotrys = read_data(poetry_file)
    all_words = []
    i = 0
    for peotry in peotrys:
        all_words += [word for word in peotry]
        # if len(all_words)>100*i:
        #     print(all_words)
        #     i+=1
    counter = collections.Counter(all_words)
    # 统计单词的个数
    print(counter)
    # 将单词进行逆序排序
    count_pair = sorted(counter.items(), key=lambda x: -x[1])
    print(count_pair)
    # 过滤部分非单词的词
    count_pair = count_pair[4:]
    print(count_pair[4:])
    # 选取一部分单词作为有用的信息
    words, _ = zip(*count_pair)
    print(words)
    print(len(words))
    words = words[:len(words)] + (" ",)
    print(words)
    print(len(words))
    # 将单词进行ID标识
    words_2_number = dict(zip(words, range(len(words))))
    print(words_2_number)
    # 将单词进行ID标识，逆序
    words_2_number_dev = dict(zip(words_2_number.values(), words_2_number.keys()))
    print(words_2_number_dev)
    # 定义一个匿名函数
    to_num = lambda word: [words_2_number.get(w, len(words)) for w in word]
    # print(to_num)
    peotrys_vector = [list(map(to_num, peotry)) for peotry in peotrys]
    # print(peotrys_vector[0])
    for i in peotrys_vector:
        print(i)
        time.sleep(0.1)
    pass


class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    init()
    pass
