#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: execute_main.py
    @time: 2019/12/22 0:38
"""

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Intelligence Poem Writer.')
    help_ = 'choose to train or generate.'
    parser.add_argument('--train', dest='train', action='store_true', help=help_)
    parser.add_argument('--no-train', dest='train', action='store_false', help=help_)
    parser.set_defaults(train=True)

    args_ = parser.parse_args()
    return args_


if __name__ == '__main__':
    args = parse_args()
    from poetry.tang_poems import main
    if args.train:
        main(True)
    else:
        main(False)
