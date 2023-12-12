# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/12
Describe:leetcode 剑指offer 32 — III.从上到下打印二叉树 III
实现一个函数按照之字形打印二叉树,第一行按照从左到右的顺序打印
第二行按照从右到左的顺序打印,第三行再从左到右
"""
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order_iii(root):
    if not root:
        return []
    res = []
    q = deque()
    q.append((root, 1))
    while q:
        tmp = []
        for _ in range(len(q)):
            cur_node, d = q.popleft()
            if d % 2 != 0:
                tmp.append(cur_node.val)
            else:
                tmp.insert(0, cur_node.val)
            if cur_node.left:
                q.append((cur_node.left, d + 1))
            if cur_node.right:
                q.append((cur_node.right, d + 1))
        res.append(tmp)
    return res


if __name__ == '__main__':
    a = TreeNode(2)
    a.left = TreeNode(9)
    b = TreeNode(20)
    a.right = b
    c = TreeNode(15)
    d = TreeNode(7)
    b.left = c
    b.right = d
    c.left = TreeNode(12)
    c.right = TreeNode(5)
    d.right = TreeNode(8)
    print(level_order_iii(a))
