# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/12
Describe:leetcode 剑指offer 32 — II.从上到下打印二叉树 II
"""
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order(root: TreeNode):
    if not root:
        return []
    q = deque()
    q.append(root)
    res = []
    while q:
        tmp = []
        for _ in range(len(q)):
            cur_node = q.popleft()
            tmp.append(cur_node.val)
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
        res.append(tmp)
    return res


if __name__ == '__main__':
    a = TreeNode(3)
    a.left = TreeNode(9)
    b = TreeNode(20)
    a.right = b
    b.left = TreeNode(15)
    b.right = TreeNode(7)
    print(level_order(a))
