# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/10
Describe:面试题 08.08. 有重复字符串的排列组合
有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。
 输入：S = "qqe"
 输出：["eqq","qeq","qqe"]

 输入：S = "ab"
 输出：["ab", "ba"]
"""
import itertools


def permutation(s: str):
    return list(set(''.join(tmp) for tmp in itertools.permutations(s, len(s))))


def permutation_r(S: str):
    def trace(S, cur, choose):
        if len(cur) == len(S):
            return ["".join(cur)]
        res, cut = [], set()
        for i in range(len(S)):
            if choose[i] or S[i] in cut:
                continue
            choose[i] = True
            cur.append(S[i])
            res.extend(trace(S, cur, choose))
            cur.pop()
            choose[i] = False
            cut.add(S[i])
        return res

    return trace(S, [], [False] * len(S))


def permutation_dfs(S):
    res = []
    path = []
    visited = [False] * len(S)

    def dfs(S, k):
        if k == len(S):
            res.append("".join(path))
            return
        for i in range(len(S)):
            if i > 0 and S[i] == S[i - 1] and not visited[i - 1]:
                continue
            if not visited[i]:
                visited[i] = True
                path.append(S[i])
                dfs(S, k + 1)
                path.pop()
                visited[i] = False

    S = list(S)
    S.sort()
    dfs(S, 0)
    return res


if __name__ == '__main__':
    s = 'eqq'
    print(permutation_r(s))
