# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/18
Describe: 链表实现二叉树
"""


class BinaryTree:

    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key


if __name__ == '__main__':
    r = BinaryTree('a')
    r.insert_left('b')
    r.insert_right('c')
    print(r.get_right_child().get_root_val())
    r.get_right_child().set_root_val("hello")
    print(r.get_right_child().get_root_val())
    r.get_left_child().insert_right('d')



