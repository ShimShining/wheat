# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/10
Describe:LCR 080. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
输入: n = 1, k = 1
输出: [[1]]
"""
import itertools


def combine(n: int, k: int):
    """超出内存限制"""

    def check(tmp):
        for i in range(1, len(tmp)):
            if tmp[i] < tmp[i - 1]:
                return False
        return True

    a = list(set(itertools.permutations(list(range(1, n + 1)), k)))
    print(a)
    if k == 1:
        res = [list(item) for item in a]
    else:
        res = [item for item in a if check(item)]
    return res


def combine_dfs(n, k):
    """
    :param n:
    :param k:
    :return:
    300ms 击败 41.31%使用 Python3 的用户
    17.50MB击败 46.33%使用 Python3 的用户
    """
    res = []
    # visited = [False] * n
    path = []

    def dfs(num, cnt):
        if num - 1 <= n and cnt == k:
            res.append(path.copy())
            return
        for i in range(num, n + 1):
            if i <= n:
                path.append(i)
                dfs(i + 1, cnt + 1)
                path.pop()

    dfs(1, 0)
    return res


if __name__ == '__main__':
    # print(combine(1, 1))
    print(combine_dfs(1, 1))
