#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: clean_cn_01.py
    @time: 2019/12/21 23:34
"""
import os.path as osp

from poetry.clean_data import *
from util_root_path import root_path

corpus_dir = osp.join(root_path, 'poetry', 'corpus', 'poetry.txt')
print(corpus_dir)
clean_cn_corpus(corpus_dir)
