# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/22
Describe: 树的遍历
"""


# 递归
from race.prac.ds.tree.build_parse_tree import build_parse_tree


def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def postorder(tree):
    if tree is not None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())


def inorder(tree):
    if tree is not None:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())


if __name__ == '__main__':
    expr = "( ( 3 + 4 ) * ( 5 + 6 ) )"

    p_tree = build_parse_tree(expr)

    # preorder(p_tree)
    # inorder(p_tree)
    postorder(p_tree)



