# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/4
Describe: 387. 字符串中的第一个唯一字符
给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。
输入: s = "leetcode"
输出: 0
输入: s = "loveleetcode"
输出: 2
输入: s = "aabb"
输出: -1
"""


def first_uniq_char(s: str) -> int:
    """
    :param s:
    :return:
    140ms 击败 26.36%使用 Python3 的用户
    16.11MB 击败 71.27%使用 Python3 的用户
    """

    for i in range(len(s)):
        if s[i] not in s[i + 1:] and s[i] not in s[:i]:
            return i
    return -1


def first_uniq_char_1(s: str) -> int:
    """
    :param s:
    :return:
    104ms 击败 56.36%使用 Python3 的用户
    16.09MB 击败 75.58%使用 Python3 的用户

    """
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    for i in range(len(s)):
        if d[s[i]] == 1:
            return i
    return -1


def first_uniq_char_2(s: str) -> int:
    chars = [0] * 26
    for c in s:
        i = ord(c) - ord('a')
        chars[i] += 1
    for i in range(len(s)):
        index = ord(s[i]) - ord('a')
        if chars[index] == 1:
            return i
    return -1


def first_uniq_char_3(s: str) -> int:
    """
    :param s:
    :return:
    84ms 击败 87.09%使用 Python3 的用户
    16.27MB 击败 20.79%使用 Python3 的用户
    """
    pos = dict()
    n = len(s)
    for i, ch in enumerate(s):
        if ch in pos:
            pos[ch] = -1
        else:
            pos[ch] = i
    first = n
    for p in pos.values():
        if p != -1 and p < first:
            first = p
    if first == n:
        first = -1
    return first
