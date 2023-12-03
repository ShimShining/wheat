# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/3
Describe:14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

输入：strs = ["flower","flow","flight"]
输出："fl"
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
"""


def longest_common_prefix(strs):
    """
    横向比较
    :param strs:
    :return:
    """
    if not strs:
        return ""
    pre, count = strs[0], len(strs)
    for i in range(1, count):
        pre = lcp(pre, strs[i])
        if not pre:
            break
    return pre


def lcp(s1, s2):
    length = min(len(s1), len(s2))
    index = 0
    while index < length and s1[index] == s2[index]:
        index += 1
    return s1[:index]


def longest_common_prefix_1(strs):
    """
    纵向比较
    :param strs:
    :return:
    20ms 击败 63.89%使用 Python 的用户
    13.28MB 击败 10.47%使用 Python 的用户
    """
    if not strs:
        return ""
    n = len(strs)
    m = len(strs[0])
    for i in range(1, m):
        ch = strs[0][i]
        for j in range(1, n):
            if len(strs[j]) < i or strs[j][i] != ch:
                return strs[0][:i]
    return strs[0]


if __name__ == '__main__':
    ss = ["abc", "acd", "aef"]
    print(longest_common_prefix(ss))
