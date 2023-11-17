# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/17
Describe: 列表嵌套递归实现二叉树
递归的数据结构
"""


def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])


def insertRight(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])


def getRootVal(root):
    return root[0]


def setRootVal(root, new_val):
    root[0] = new_val


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


if __name__ == '__main__':

    r = BinaryTree(3)
    insertLeft(r, 4)
    insertLeft(r, 5)
    insertRight(r, 6)
    insertRight(r, 7)
    l = getLeftChild(r)
    print(r)
    print(l)

    setRootVal(l, 9)
    print(r)

    insertLeft(l, 11)
    print(r)
    print(getRightChild(getRightChild(r)))

