#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: setup.py
    @time: 2019/12/21 23:14
"""

from setuptools import setup

setup(
    name='TFDemo',
    version='20.19.12.21.0.1',
    url='https://github.com/xshqhua/TFDemo',
    author='xushihua',
    author_email='xshqhua@gmail.com',
    license='open sources',
    description='just a study',
    # packages=["mrcnn"],  # setup.py同级目录下文件夹mrcnn中含有__init__.py文件
    install_requires=['numpy', 'tensorflow'],
    include_package_data=True,
    python_requires='>=3.7',
    long_description="just a study",
    classifiers=[
        "xx"
    ],
    keywords=["xx", ],
)
