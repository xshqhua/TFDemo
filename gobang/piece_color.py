#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: piece_color.py
    @time: 2019/12/24 21:20
"""
from enum import Enum, unique


@unique
class PieceColor(Enum):
    BLACK = (0, 0, 0)
    WHITE = (1, 1, 1)
