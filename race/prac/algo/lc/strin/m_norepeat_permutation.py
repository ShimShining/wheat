# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/10
Describe:面试题 08.07. 无重复字符串的排列组合
无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。

 输入：S = "qwe"
 输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]

 输入：S = "ab"
 输出：["ab", "ba"]
 字符都是英文字母。
字符串长度在[1, 9]之间。
"""
import itertools


def permutation_no_repeat(S):
    res = []
    visited = [False] * len(S)
    path = []

    def dfs(S, k):
        if k == len(S):
            res.append("".join(path))
        for i in range(len(S)):
            if visited[i]:
                continue
            visited[i] = True
            path.append(S[i])
            dfs(S, k + 1)
            path.pop()
            visited[i] = False

    dfs(S, 0)
    return res


def permutation_1(S):
    return list("".join(t) for t in itertools.permutations(S, len(S)))
