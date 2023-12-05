# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/4
Describe:111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。
输入：root = [3,9,20,null,null,15,7]
输出：2
输入：root = [2,null,3,null,4,null,5,null,6]
输出：5
"""

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


def min_depth(root):
    """
    深度优先搜索
    :param root:
    :return:
    """
    if root is None:
        return 0
    if not root.left and not root.rigth:
        return 1
    m1 = min_depth(root.left)
    m2 = min_depth(root.right)
    # if m1 == 0:
    #     return m2 + 1
    # elif m2 == 0:
    #     return m1 + 1
    # else:
    #     return min(m1, m2) + 1

    return m1 + m2 + 1 if root.left is None or root.right is None else min(m1, m2) + 1


def min_depth_1(root):
    if root is None:
        return 0
    if not root.left and not root.rigth:
        return 1
    min_dep = 10 ** 9
    if root.left:
        min_dep = min(min_depth_1(root.left), min_dep)
    if root.rigth:
        min_dep = min(min_depth_1(root.right), min_dep)
    return min_dep + 1


def min_depth_2(root):
    """广度优先搜索
    368ms 击败 98.92%使用 Python3 的用户
    57.58MB 击败 67.58%使用 Python3 的用户
    """
    if not root:
        return 0
    q = collections.deque([(root, 1)])
    while q:
        node, d = q.popleft()
        if not node.left and not node.right:
            return d
        if node.left:
            q.append((node.left, d + 1))
        if node.right:
            q.append((node.right, d + 1))
    return 0
