#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: string_tree.py
    @time: 2020/3/11 22:24
"""


def create_tree(contend, node_tree):
    if len(contend) == 0:
        return {'END': "END"}
    else:
        temp = node_tree.get(contend[0], {})
        node_tree[contend[0]] = create_tree(contend[1:], temp)
        return node_tree


# l1 = ['abc', 'def', 'abcdd', "xxxx"]
# for i in l1:
#     create_tree(i, tree)
# print(tree)


def is_contains(tree, contend):
    temp = tree
    for i in contend:
        temp = temp.get(i, {})
        if len(temp) == 0:
            return False
    return "END" in temp.values()


start = 1030040080
alpha_data = [str(i) for i in range(start, start + 10000, 2343)]
print(alpha_data)

tree = {}
for i in alpha_data:
    create_tree(i, tree)

print(is_contains(tree, alpha_data[1]))
print(is_contains(tree, alpha_data[3]))
print(is_contains(tree, "abcd"))
print(is_contains(tree, "xxx"))
