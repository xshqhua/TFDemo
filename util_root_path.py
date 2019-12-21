#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: util_root_path.py
    @time: 2019/12/21 23:39
"""
import os
import os.path as osp

project_name = 'TFDemo'
root_path = osp.join(os.path.abspath(os.path.dirname(__file__)).split('TFDemo')[0], project_name)
poetry_demo_root_path = osp.join(root_path, 'poetry')